import os
import streamlit as st
import openai

api_key = os.environ.get("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")

#streamlit düzenlemesi
st.title("FU Bot")

if "message" not in st.session_state:
    st.session_state.message=[]

for message in st.session_state.message:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("")

if prompt:
    with st.chat_message(name="user"):
        st.markdown(prompt)
    st.session_state.message.append({"role":"user","content":prompt})

    response = f"FU Bot: {prompt}"

    with st.chat_message("assistant"):
        st.markdown(response)
    
    st.session_state.message.append({"role":"assistant","content":response})

#with st.chat_message(name="Assistant"):
#    st.write("Hello!!")