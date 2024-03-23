#Integrate with OpenAI API
import os
from constants import openai_key
from langchain.llms import OpenAI
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.chains import SimpleSequentialChain

os.environ['OPENAI_API_KEY'] = openai_key

st.title("Celebrity Search Results")
input_text  = st.text_input("Search whatever you want")


first_input_prompt =  PromptTemplate(
    input_variables=["name"],
    template="Tell me about Celebrity {name}"
)

llm = OpenAI(temperature=0.8)

chain1  = LLMChain(llm = llm,prompt = first_input_prompt, verbose=True,output_key="person")


second_input_prompt =  PromptTemplate(
    input_variables=["person"],
    template="when was {person} born"
)

chain2  = LLMChain(llm = llm,prompt = second_input_prompt, verbose=True,output_key="dob")

parent_chain = SimpleSequentialChain(chains=[chain1,chain2],verbose=True)


if input_text:
    st.write(parent_chain.run(input_text))