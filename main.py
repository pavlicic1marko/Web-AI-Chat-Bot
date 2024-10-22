import streamlit as st
from ollama_ai_api import ask_ollama

st.title("AI web chat bot")

prompt = st.chat_input("Ask AI something")
if prompt:
    answer = ask_ollama(prompt)
    st.write(f"AI: {answer}")