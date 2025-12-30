from typing import Literal, Annotated
import operator
from typing_extensions import TypedDict
from langgraph.graph import add_messages
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

class State(TypedDict):
    """Represent the state of the graph"""
    messages: Annotated[list, add_messages]