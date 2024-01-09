import streamlit as st
import openai 
import Selenium_VeriCekme as cek
import os
import pandas as pd

from langchain_community.document_loaders import CSVLoader
#from langchain.document_loaders import CSVLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain_openai import OpenAIEmbeddings  # Değişiklik burada
import os

os.environ["OPENAI_API_KEY"] = "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"

# Load the documents
#loader = CSVLoader(file_path='D:\GitHub\ChatBot_ChatGPT-3.5\duyuru_dataset.csv')
loader = CSVLoader(file_path="D:\GitHub\ChatBot_ChatGPT-3.5\duyuru_dataset.csv", encoding="utf-8")

# Create an index using the loaded documents
index_creator = VectorstoreIndexCreator()
docsearch = index_creator.from_loaders([loader])

docsearch

chain = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=docsearch.vectorstore.as_retriever(), input_key="question")

query = "Staj ilanı var mı? Varsa bana bunları söyle."

prompt = f"""

Given the dataset about announcements (duyuru_dataset.csv), you can find information about recent announcements. 
If there is no information available in the dataset, you can respond with "no such information has been released recently".

When it comes to academic information, you can refer to the academic dataset (akademik_dataset.csv). 
If you are provided with the name of an official from the academic dataset, you can retrieve their fields of study and title information.

If you are asked a question related to a specific field in the academic dataset, you can let the user know that you can provide assistance regarding the lecturer who specializes in that field.

You know Turkish very well and you will reply with Turkish only.
Make sure you provide detailed info about the given context.
{query}
"""

# Pass a query to the chain
response = chain({"question": prompt})

print(response['result']) 