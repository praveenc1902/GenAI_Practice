#Integrate with OpenAI API
import os
from constants import openai_key
from langchain.llms import OpenAI
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

os.environ['OPENAI_API_KEY'] = openai_key

st.title("Celebrity Search Results")
input_text  = st.text_input("Search whatever you want")


first_input_prompt =  PromptTemplate(
    input_variables=["name"],
    template="Tell me about Celebrity {name}"
)

llm = OpenAI(temperature=0.8)

chain  = LLMChain(llm = llm,prompt = first_input_prompt, verbose=True)

if input_text:
    st.write(chain.run(input_text))