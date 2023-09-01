import streamlit as st
from langchain.llms import HuggingFaceHub
from dotenv import load_dotenv
load_dotenv()
import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")


#Function to return the response
def load_answer(question): 
    llm=HuggingFaceHub(repo_id="google/flan-t5-xl", model_kwargs={"temperature":1e-10})
    answer=llm(question)
    return answer


#App UI starts here
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("LangChain Demo")

#Gets the user input
def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text


user_input=get_text()
response = load_answer(str(user_input))

submit = st.button('Generate')  

#If generate button is clicked
if submit:

    st.subheader("Answer:")

    st.write(response)