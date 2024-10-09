import streamlit as st
#from langchain.chat_models import ChatOpenAI
from langchain_openai.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

st.title("Langchain text gen")

user_prompt = st.text_area("Enter your prompt: ")

if st.button("Generate text"):
    if user_prompt:
        llm = ChatOpenAI(
            model = "gpt-3.5-turbo",
            temperature = 0,
        )

        messages = [
            SystemMessage(content = "You are a helpful assistant"),
            HumanMessage(content = user_prompt),
        ]

        response = llm(messages)

        st.subheader("Generated Text: ")
        st.write(response.content.strip())

    else:
        st.error("Please enter a prompt.")