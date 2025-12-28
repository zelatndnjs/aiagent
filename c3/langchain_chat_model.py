import random
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

if random.random() < 0.5:
    print("gpt-5-nano selected")
    model = init_chat_model("gpt-5-nano", model_provider="openai", api_key=os.getenv("OPENAI_API_KEY"))
else:
    print("claude-3-haiku-20240307 selected")
    model = init_chat_model("claude-3-haiku-20240307", model_provider="anthropic", api_key=os.getenv("ANTHROPIC_API_KEY"))

result = model.invoke("RAG이 뭔가요?")
print(result.content)