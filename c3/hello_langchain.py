from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model("gpt-5-nano", model_provider="openai", api_key=os.getenv("OPENAI_API_KEY"))
result = model.invoke("랭체인이 뭔가요?")
print(type(result))
print(result.content)