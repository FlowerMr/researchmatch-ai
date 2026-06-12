import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    print("❌ OPENROUTER_API_KEY not found in .env file")
    exit(1)

print("✅ KEY FOUND:", api_key[:10] + "...")

try:
    llm = ChatOpenAI(
        model="deepseek/deepseek-chat",
        openai_api_key=api_key,
        openai_api_base="https://openrouter.ai/api/v1",
        temperature=0.7,
        max_tokens=500
    )
    
    response = llm.invoke("Hello! Who are you?")
    print("📝 Response:", response.content)
    
except Exception as e:
    print(f"❌ Error: {e}")