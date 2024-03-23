#Integrate with OpenAI API
import os
from constants import openai_key
from langchain.llms import OpenAI
import streamlit as st

os.environ['OPENAI_API_KEY'] = openai_key

st.title("Langchain demo with OpeAI")
input_text  = st.text_input("Search whatever you want")

llm = OpenAI(temperature=0.8)

if input_text:
    st.write(llm(input_text))