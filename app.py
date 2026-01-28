##This is a basic chatbot using ollama that is already installed in my system so just i am creating a interface to conect my input to ollama model
##Model used- gemma3:4b
##We are using langsmith to track our ai response call 

import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate #To define what my chatbot used to do like what to think and give ans accordingly
from langchain_core.output_parsers import StrOutputParser #To display the output of ai response

load_dotenv()

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

## Prompt Template
prompts = ChatPromptTemplate.from_messages(
    [
        ("system","You are helpfull assistant. Please respond to the qution asked"),
        ("user","Quetion:{question}") 
    ]
)

## streamlit framework
st.title("Langchain Demo With Gemma3:4b Model")
input_text=st.text_input("What question you have in mind?")


## Ollama Llama2 model
llm = Ollama(model="gemma3:4b") #Calling my model
output_parser = StrOutputParser()
chain = prompts|llm|output_parser ##Take the response send into llm get the output

if input_text:
    st.write(chain.invoke({"question":input_text}))


