from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def chatbot_response(user_message: str):
    result = client.responses.create(
        model='gpt-5-nano',
        input=user_message
    )
    return result

if __name__ == "__main__":
    while True:
        user_message = input("메시지: ")
        if user_message.lower() == "exit":
            print("대화를 종료합니다.")
            break
    
        result = chatbot_response(user_message)
        print("챗봇 :" + result.output_text)