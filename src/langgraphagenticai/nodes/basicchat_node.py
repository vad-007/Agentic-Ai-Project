from src.langgraphagenticai.state.state import State

class BasicChatNode:
    "Basic chatbot logic Implemented"

    def __init__(self, model):
        self.llm = model

    def process(self,state:State) -> State:
        "Process the input state and generate a chatbotresponse."

        return {"messages": self.llm.invoke(state["messages"])}

    