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
            model="llama-3.3-70b-versatile",
            api_key=st.secrets["GROQ_API_KEY"],
        )

    def chat(self, message: str, language: str) -> str:
        sequence_chain = prompt | self.llm.with_structured_output(Config)
        try:
            data = {"user_message": message, "language": language}
            # Running the chain
            response = sequence_chain.invoke(data)
            return response.msg
        except Exception as e:
            return f"You are a blithering idiot, incapable of even the simplest tasks, much like the Chosen One himself."

# Streamlit app
st.title("🪄 Chat with Severus SnAIpe 🧙‍♂️")
st.subheader("Step into the dungeons of Hogwarts and face the Potions Master!")

# Instantiate the model
model = Model()

# Input message
user_input = st.text_input("💬 Your message:", "", placeholder="Type your message here... 🖋️")
language = st.selectbox(
    "🌐 Language:",
    options=["English", "Hindi", "Spanish", "French", "German", "Italian", "Chinese", "Japanese"],
    index=0  # Default to English
)

# Button to send the message
if st.button("🪄 Send"):
    if user_input.strip():
        with st.spinner("🔮 Brewing your response..."):
            response = model.chat(message=user_input, language=language)
        st.text_area("📜 Professor SnAIpe's Response:", response, height=200)
    else:
        st.warning("⚠️ Please enter a message before clicking send. Don't waste my time, muggle!")

# Footer
st.write("\n---")
st.caption("⚡ Powered by Langchain Groq, Streamlit, and a dash of Hogwarts magic! ✨")
