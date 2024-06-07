from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Function to load Gemini Pro model
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_geminipro_response(question):
    response = chat.send_message(question,stream=True)
    return response

#Initialize Streamlit App

st.set_page_config(page_title="QA ChatBot")
st.header("GeminiPro LLM Application")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input Question:", key="input")
submit = st.button("Ask question")

if submit and input:
    response=get_geminipro_response(input)

    #Add user query and response to session history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("Response:")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("ChatBot", chunk.text))

chat_history = st.button("Chat History:")

if chat_history:
    for role,text in st.session_state['chat_history']:
        st.write(f"{role}:{text}")