from langchain.tools import tool
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage
from typing import Literal
from langchain_core.messages import Message
from typing_extensions import TypedDict, Annotated
import operator
from langgraph.graph import StateGraph, START, END, add_messages
import datetime

class State (TypedDict):
    """Represent the state of the graph"""

    messages:Annotated[list, add_messages]