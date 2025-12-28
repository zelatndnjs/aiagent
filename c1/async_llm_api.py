import asyncio
import os

from openai import AsyncOpenAI
from anthropic import AsyncAnthropic
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

openai_client = AsyncOpenAI(api_key=openai_api_key)
claude_client = AsyncAnthropic(api_key=anthropic_api_key)


async def call_async_openai(prompt: str, model: str = "gpt-5-nano") -> str:
    response = await openai_client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


async def call_async_claude(prompt: str, model: str = "claude-3-haiku-20240307") -> str:

    response = await claude_client.messages.create(
        model=model, max_tokens=1024, messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text

async def main():
    print("동시에 API 호출하기")
    prompt = "비동기 프로그래밍에 대해 두세 문장으로 설명해주세요."
    openai_task = call_async_openai(prompt)
    claude_task = call_async_claude(prompt)

    openai_result, claude_result = await asyncio.gather(openai_task, claude_task)
    print(f"OpenAI 응답: {openai_result}")
    print(f"Claude 응답: {claude_result}")

if __name__ == "__main__":
    asyncio.run(main())