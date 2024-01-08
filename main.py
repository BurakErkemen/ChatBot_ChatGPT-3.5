import streamlit as st
import openai 
import Selenium_VeriCekme as cek
import os
import pandas as pd

st.title("Fırat BOT")

# API Key
openai.api_key = st.secrets["OPENAI_API_KEY"]

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages= []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("What is up?")
prompt1 = """If you are given an entry with the word "Announcements" in it, you can look in the [duyurular_dataset.csv](link_to_duyurular_dataset) file and answer that {no such information has been released recently} if the information asked for is not there.
If you are given the name of an official from the [akademik_dataset.csv](link_to_akademik_dataset) database, you can give his/her fields of study and title information.
If you are asked a question about a field in the [akademik_dataset.csv](link_to_akademik_dataset) database, you can let them know that you can get help about the lecturer who deals with it."""

prompt3 = """
Given the dataset about announcements (duyuru_dataset.csv), you can find information about recent announcements. 
If there is no information available in the dataset, you can respond with "{no such information has been released recently}".

When it comes to academic information, you can refer to the academic dataset (akademik_dataset.csv). 
If you are provided with the name of an official from the academic dataset, you can retrieve their fields of study and title information.

If you are asked a question related to a specific field in the academic dataset, you can let the user know that you can provide assistance regarding the lecturer who specializes in that field.
"""

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    
    st.session_state.messages.append({"role":"user","content":prompt3})
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.ChatCompletion.create(
            model = st.session_state["openai_model"],
            temperature=0.1,
            max_tokens=150,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream = True,
        ):
            full_response += response.choices[0].delta.get("content","")
            message_placeholder.markdown(full_response + "|")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant","content":full_response})

