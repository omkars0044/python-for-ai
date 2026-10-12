import langchain_openai 
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(api_key="your-api-key", model_name="gpt-4", temperature=0.7)

response = llm.invoke("Hello, how are you?")