# app.py
import streamlit as st 

st.title("무엇이든 물어보살!")

if question := st.chat_input("질문을 입력하세요."):
    
    with st.chat_message("user"):
        st.markdown(question)
    
    response = f"전 아무 것도 몰라요!"
    with st.chat_message("assistant"):
        st.markdown(response)