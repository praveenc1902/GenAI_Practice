#Integrate with OpenAI API
import os
from constants import openai_key
from langchain.llms import OpenAI
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.chains import SequentialChain
from langchain.memory import ConversationBufferMemory

os.environ['OPENAI_API_KEY'] = openai_key

st.title("Celebrity Search Results")
input_text  = st.text_input("Search whatever you want")


first_input_prompt =  PromptTemplate(
    input_variables=["name"],
    template="Tell me about Celebrity {name}"
)

llm = OpenAI(temperature=0.8)

name_memory = ConversationBufferMemory(input_key="name",memory_key="abc")

chain1  = LLMChain(llm = llm,prompt = first_input_prompt, verbose=True,output_key="person",memory=name_memory)


second_input_prompt =  PromptTemplate(
    input_variables=["person"],
    template="when was {person} born"
)

person_memory = ConversationBufferMemory(input_key="person",memory_key="abc")

chain2  = LLMChain(llm = llm,prompt = second_input_prompt, verbose=True,output_key="dob",memory=person_memory)

third_input_prompt =  PromptTemplate(
    input_variables=["dob"],
    template="Mention 5 major events happened around {dob} in india"
)
dob_memory = ConversationBufferMemory(input_key="dob",memory_key="abc")


chain3  = LLMChain(llm = llm,prompt = third_input_prompt, verbose=True,output_key="description",memory=dob_memory)


parent_chain = SequentialChain(
    chains=[chain1,chain2,chain3],input_variables=['name'],output_variables=['person','dob','description'],verbose=True)


if input_text:
    st.write(parent_chain({'name':input_text}))

    with st.expander("Person Name"):
        st.info(person_memory.buffer)
    
    with st.expander("DOB"):
        st.info(dob_memory.buffer)