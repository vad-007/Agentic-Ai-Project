from configparser import ConfigParser

class Config:
    def __init__(self, config_file='src/langgraphagenticai/ui/uiconfigfile.ini'):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_llm_options(self):
        return self.config['DEFAULT'].get('LLM_SELECTION', 'Groq').split(',')

    def get_usecase_options(self):
        return self.config['DEFAULT'].get('USAGE_INSTRUCTIONS', 'Basic Chatbot,Chatbot with Tool,Travel Planner,AI News,SDCL Workflow,Custom Workflow').split(',')

    def get_page_title(self):
        return self.config['DEFAULT'].get('PAGE_TITLE', 'LangGraph Agentic AI')

    def get_welcome_message(self):
        return self.config['DEFAULT'].get('WELCOME_MESSAGE', 'Welcome to LangGraph Agentic AI!')

    def get_groq_model_options(self):
        return self.config['DEFAULT'].get('Groq_MODEL_OPTIONS', 'llama-3.1-8b-instant').split(',')
