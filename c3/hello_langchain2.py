import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

model = init_chat_model("claude-3-haiku-20240307", model_provider="anthropic", api_key=os.getenv("ANTHROPIC_API_KEY"))

result = model.invoke("랭체인이 뭔가요?")
print(result.content)