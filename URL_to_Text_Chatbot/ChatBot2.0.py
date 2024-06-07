import os
import time
import streamlit as st
import pickle
from langchain_openai import OpenAI
from langchain.chains.qa_with_sources.retrieval import RetrievalQAWithSourcesChain
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.document_loaders.url_selenium import SeleniumURLLoader
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS

from dotenv import load_dotenv
load_dotenv()

st.title("URLChatBot")
st.sidebar.title("Article URLS")

urls = []
for i in range(2):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_URL_clicked = st.sidebar.button("Process URL's")
file_path = "openai_pickle.pkl"
main_placeholder = st.empty()
llm = OpenAI(temperature=0.9, max_tokens=500)

if process_URL_clicked:
    loader = SeleniumURLLoader(urls=urls)
    data = loader.load()
    main_placeholder.text("Loading Data")

    #Text Splitting
    text_splitter = RecursiveCharacterTextSplitter(
        separators = ['\n\n', '.', '\n', ','],
        chunk_size = 600,
        chunk_overlap = 200
    )
    docs = text_splitter.split_documents(data)
    main_placeholder.text("Splitting Data")

    #Create Embeddings and save in pickle format
    embeddings = OpenAIEmbeddings() 
    vectorstore_openai = FAISS.from_documents(docs, embeddings)
    main_placeholder.text("Data embeddings Started")
    time.sleep(2)
    
    # FAISS index to pickle file
    with open(file_path, "wb") as f:
        pickle.dump(vectorstore_openai, f)

query = main_placeholder.text_input("Question: ")

if query:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            vectorstore = pickle.load(f)
            chain = RetrievalQAWithSourcesChain.from_llm(llm = llm, retriever = vectorstore.as_retriever())
            result = chain({"question": query}, return_only_outputs = True)
            st.header("Answer")
            st.subheader(result["answer"])