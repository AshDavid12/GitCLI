import openai
from openai import OpenAI 
import os
from langchain_core.prompts.chat import ChatPromptTemplate

openai.api_key = os.getenv("OPENAI_API_KEY")


client = OpenAI()
def get_git_command(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    command = response.choices[0].message.content.strip()
    if '```' in command:
        command = command.split('```')[1].strip()
    return command
