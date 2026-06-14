from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

print("KEY FOUND:", os.getenv("OPENROUTER_API_KEY") is not None)

llm = ChatOpenAI(
    model="deepseek/deepseek-chat-v3-0324",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    temperature=0
)

response = llm.invoke("hello")

print(response.content)