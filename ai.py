import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def ask_ai(prompt):
    response = client.chat.completions.create(
        model="qwen/qwen3-30b-a3b",
        messages=[
            {
                "role": "user",
                "content":prompt
            }       
        ]
    )

    return response.choices[0].message.content

# # Test
# answer = ask_ai("Create a one sentence motivation message for a teacher")
# print(answer)

