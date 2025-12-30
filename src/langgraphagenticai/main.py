from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLM.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.disply_result import DisplayResultStreamlit
import json
import streamlit as st


def load_langgraph_agenticai_app():
    """
    Load LangGraph Agentic AI App
    """

    ui = LoadStreamlitUI()
    user_input = ui.load_streamlitui()

    if not user_input:
        st.error('Error: Failed to load user input')
        return

    # Capture user message separately from usecase_option
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe
    else:
        user_message = st.chat_input("Enter your message:")

    if user_message:
        try:
            obj_llm_config = GroqLLM(user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error('Error: LLM model cannot be initialized')
                return

            usecase = user_input.get('usecase_option')
            if not usecase:
                st.error('Error: Usecase not selected')
                return

            ### Graph Builder
            graph_builder = GraphBuilder(model)

            try:
                graph = graph_builder.setup_graph(usecase)
                if graph:
                    display_result = DisplayResultStreamlit(usecase, graph, user_message)
                    display_result.display_result_on_ui()
                else:
                    st.error(f"Error: Could not setup graph for usecase '{usecase}'")
            except Exception as e:
                st.error(f"Error occurred with exception: {str(e)}")
                return

        except Exception as e:
            st.error(f"Error occurred with exception: {str(e)}")