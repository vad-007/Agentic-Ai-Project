import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message
        
        # Normalize usecase for comparison
        normalized_usecase = usecase.lower().replace(" ", "_")
        
        if normalized_usecase == "basic_chatbot":
            # Display user message
            with st.chat_message("user"):
                st.write(user_message)
            
            # Stream response from graph
            try:
                for event in graph.stream({'messages': [HumanMessage(content=user_message)]}):
                    for value in event.values():
                        if 'messages' in value:
                            msg = value['messages']
                            # If it's a list, get the last message
                            if isinstance(msg, list):
                                msg = msg[-1]
                            
                            with st.chat_message("assistant"):
                                st.write(msg.content)
            except Exception as e:
                st.error(f"Error during graph execution: {str(e)}")