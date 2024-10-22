import streamlit as st
from ollama_ai_api import ask_ollama

st.title("AI web chat bot")


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

prompt = st.chat_input("Ask AI something")
if prompt:
    answer = ask_ollama(prompt)
    st.session_state.messages.append({"user question":prompt,"AI answer":answer})
    for question_answer in st.session_state.messages:
        st.write(question_answer)
