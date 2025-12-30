import streamlit as st
import os
from datetime import datetime

from langchain_core.messages import AIMessage, HumanMessage
from src.langgraphagenticai.ui.uiconfigfile import Config
        
class LoadStreamlitUI:    
    def __init__(self):
        self.config = Config()
        self.user_control = {}

    def initialize_session(self):
        return {
            "current_step": "requirements",
            "requirements": "",
            "user_stories": "",
            "po_feedback": "",
            "generated_code": "",
            "review_feedback": "",
            "decision": None
        }

    def render_requirements(self):
        st.markdown("## Requirements")
        st.session_state.state["requirements"] = st.text_area(
            "Enter Requirements",
            height=200,
            key="req_input"
        )
        if st.button("Submit Requirements"):
            st.session_state.state["current_step"] = "generate_user_stories"
            st.session_state.IsSDLC = True
    
    def render_user_stories(self):
        st.markdown("## User Stories")
        st.session_state.user_stories = st.text_area("Enter User Stories", value=st.session_state.user_stories)
    
    def render_po_feedback(self):
        st.markdown("## PO Feedback")
        st.session_state.po_feedback = st.text_area("Enter PO Feedback", value=st.session_state.po_feedback)
    
    def render_generated_code(self):
        st.markdown("## Generated Code")
        st.session_state.generated_code = st.text_area("Enter Generated Code", value=st.session_state.generated_code)
    
    def render_review_feedback(self):
        st.markdown("## Review Feedback")
        st.session_state.review_feedback = st.text_area("Enter Review Feedback", value=st.session_state.review_feedback)
    
    def render_decision(self):
        st.markdown("## Decision")
        st.session_state.decision = st.text_area("Enter Decision", value=st.session_state.decision)
        
    def load_streamlitui(self):
        st.set_page_config(
            page_title=self.config.get_page_title(),
            layout="wide"
        )
        st.header(self.config.get_page_title())
        
        if "timeframe" not in st.session_state:
            st.session_state.timeframe = ""
        if "IsFetchButtonClicked" not in st.session_state:
            st.session_state.IsFetchButtonClicked = False
        if "IsSDLC" not in st.session_state:
            st.session_state.IsSDLC = False

        with st.sidebar:
            llm_option = st.selectbox("Select LLM", self.config.get_llm_options())  
            usecase_option = st.selectbox("Select Use Case", self.config.get_usecase_options())

            self.user_control['llm_option'] = llm_option
    
            if self.user_control['llm_option'] == 'Groq':
                model_option = st.selectbox("Select Model", self.config.get_groq_model_options())
                self.user_control['groq_model_option'] = model_option  

                self.user_control['GROQ_API_KEY'] = st.text_input("GROQ API Key", type="password", key="GROQ_API_KEY")

                if not self.user_control['GROQ_API_KEY']:
                    st.warning("GROQ API Key is required")

            self.user_control['usecase_option'] = usecase_option

            if "state" not in st.session_state:
                st.session_state.state = self.initialize_session()
        
        return self.user_control
