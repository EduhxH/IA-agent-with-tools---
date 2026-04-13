import os
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL = os.getenv("OLLAMA_MODEL", "llama3-8b-8192")

def chat(messages: list, system_prompt: str = "") -> str:
    all_messages = []
    if system_prompt:
        all_messages.append({"role": "system", "content": system_prompt})
    all_messages.extend(messages)

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": MODEL,
            "messages": all_messages,
            "temperature": 0.1,
            "max_tokens": 2048
        },
        timeout=30
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]