from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLM.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
import json
import streamlit as st


def load_langgraph_agenticai_app():
    """
    Load LangGraph Agentic AI App
    """

    ui=LoadStreamlitUI()
    user_input=ui.load_streamlitui()

    if not user_input:
        st.error('Please select a use case')
        return

    if st.session_state.IsFetchButtonClicked:
        user_input['usecase_option']=st.session_state.timeframe
    else:
        user_input['usecase_option']= st.chat_input("Enter Use message:")

    if user_input:
        try:
            obj_llm_config=GroqLLM('user_controls_input=user_input')
            model=obj_llm_config.get_llm_model()

            if not model:
                st.error('Please provide a valid model name')
                return

            usecase=user_input['selected_usecase']
            if not usecase:
                st.error('Please select a use case')
                return

                ### Graph Builder

            graph_builder=GraphBuilder(model)

            try:
                graph=graph_builder.setup_graph(usecase)
            except Exception as e:
                st.error(f"Error occured with exception: {str(e)}")
                return
        
        except Exception as e:
            st.error(f"Error occured with exception: {str(e)}")

            
        


        
    

    