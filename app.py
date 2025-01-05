import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from config import Config, prompt

# Load environment variables
load_dotenv()

# Model class definition
class Model:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0.8,
            model="llama-3.1-8b-instant",
            api_key=os.getenv('GROQ_API_KEY'),
        )

    def chat(self, message: str) -> str:
        sequence_chain = prompt | self.llm.with_structured_output(Config)
        try:
            data = {"user_message": message}
            # Running the chain
            response = sequence_chain.invoke(data)
            return response.msg
        except Exception as e:
            return f"Error: {str(e)}"

# Streamlit app
st.title("ChatGroq Streamlit Application")
st.subheader("Chat with Severus SnAIpe")

# Instantiate the model
model = Model()

# Input message
user_input = st.text_input("Your message:", "", placeholder="Type your message here...")

# Button to send the message
if st.button("Send"):
    if user_input.strip():
        with st.spinner("Generating response..."):
            response = model.chat(message=user_input)
        st.text_area("Response:", response, height=200)
    else:
        st.warning("Please enter a message before clicking send.")

# Footer
st.write("\n---")
st.caption("Powered by Langchain Groq and Streamlit")
