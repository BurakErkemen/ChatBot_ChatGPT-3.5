import streamlit as st
import openai 

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
prompt1 = """If you are given an entry with "bihter das" in it, you can use the text {Bihter das is a faculty member at the university of fırat. She continues her studies in the fields of artificial intelligence and molecular biology.} text."""
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    
    st.session_state.messages.append({"role":"user","content":prompt1})
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