from langchain.tools import tool
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage
from typing import Literal
from langchain_core.messages import AnyMessage
from typing_extensions import TypedDict, Annotated
import operator
from langgraph.graph import StateGraph, START, END
import datetime
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basicchat_node import BasicChatNode

class GraphBuilder:
    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(State)



    def basic_chatbot_build_graph(self):
        """
        Build a basic chatbot graph using langgraph.
        the method initializes the graph builder and adds the basic chat node to the graph.the Chatbot node is set as the start node and the end node.
        """
        self.basic_chatbot_node = BasicChatNode(self.llm)
        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)
        

    def setup_graph(self,usecase:str):
        """
        Setup the graph by adding the basic chat node to the graph.
        """
        if usecase == "basic_chatbot":
            self.basic_chatbot_build_graph()
            return self.graph_builder.compile()
        

    