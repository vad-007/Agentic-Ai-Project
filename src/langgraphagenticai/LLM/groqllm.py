import os
from langchain_groq import ChatGroq
import streamlit as st


class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        llm = None
        try:
            groq_api_key = self.user_controls_input.get("GROQ_API_KEY", "")
            selected_groq_model = self.user_controls_input.get("groq_model_option", "")

            if not groq_api_key:
                groq_api_key = os.environ.get("GROQ_API_KEY", "")

            if not groq_api_key:
                st.error("GROQ API key is required")
                return None

            if not selected_groq_model:
                st.error("Selected Groq model is required")
                return None

            llm = ChatGroq(model_name=selected_groq_model, api_key=groq_api_key)

        except Exception as e:
            st.error(f"Error: {str(e)}")
        return llm
