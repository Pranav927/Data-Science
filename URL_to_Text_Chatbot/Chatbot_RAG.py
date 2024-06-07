import os
import streamlit as st
import pickle
import time
import langchain
from langchain_openai import OpenAI
from langchain.chains import retrieval_qa
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import url_selenium
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_community.vectorstores import chroma

os.environ['OPENAI_API_KEY'] = 'API_KEY'
LLM = OpenAI(temperature=0.7, max_tokens=500)

def main():
    st.title("News Chatbot")
    
    # Retrieve text input from user
    #st.write("Please provide the text of two paragraphs:")
    #input1 = st.text_input("LINK 1:")
    #input2 = st.text_input("LINK 2:")

    # Combine the input paragraphs
    urls = ["https://indianexpress.com/article/india/brs-k-kavitha-it-ed-searches-hyderabad-9216207/", "https://indianexpress.com/article/technology/artificial-intelligence/centre-artificial-intelligence-advisory-9216810/",]
    loader = url_selenium.SeleniumURLLoader(urls=urls)
    combined_input = loader.load()

    # Process and split the combined input
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=600,
        chunk_overlap=200
    )
    docs = text_splitter.split_documents(combined_input)

    # Embeddings and vector index
    embeddings = OpenAIEmbeddings()
    vectorindex_openai = embeddings.embed_documents(docs)
    #chroma.from_documents(docs, embeddings)

    # Initialize RAG model
    rag_chain = retrieval_qa(
        vectorindex_openai,
        LLM,
        num_sources=2
    )

    # User query
    user_query = st.text_input("Ask your question:")
    if user_query:
        # Get response from RAG model
        response = rag_chain(user_query)

        # Display response
        st.write("Chatbot's Response:")
        st.write(response)

if __name__ == "__main__":
    main()