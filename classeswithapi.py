import requests
from langchain_openai import ChatOpenAI
class APIomkar:
    def __init__(self,api_key,model="gpt-3.5-turbo",token_limit=4096):
        self.api_key = api_key
        self.model = model
        self.token_limit = token_limit
        self.base_url = "https://api.openai.com/v1/chat/completions"

chatbot = APIomkar("your_api_key_here")
