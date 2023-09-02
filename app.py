import streamlit as st
from langchain.llms import HuggingFaceHub
from dotenv import load_dotenv
load_dotenv()
import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HF_API_TOKEN")


#Function to return the response
def load_answer(question): 
    llm=HuggingFaceHub(repo_id="google/flan-t5-large")
    answer=llm(question)
    return answer


#App UI starts here
st.set_page_config(page_title="LangChain Demo")
st.header("LangChain Demo")

#Gets the user input
def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text


user_input=get_text()
response = str(load_answer(user_input))

submit = st.button('Generate')  

#If generate button is clicked
if submit:

    st.subheader("Answer:")

    st.write(response)