import os
import requests

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")

def chat(messages: list, system_prompt: str = "") -> str:
    all_messages = []
    if system_prompt:
        all_messages.append({"role": "system", "content": system_prompt})
    all_messages.extend(messages)

    response = requests.post(
        f"{OLLAMA_BASE_URL}/api/chat",
        json={
            "model": MODEL,
            "messages": all_messages,
            "stream": False,
            "options": {
                "temperature": 0.1,
                "num_predict": 2048
            }
        },
        timeout=900 # Ollama local pode ser mais lento
    )
    response.raise_for_status()
    return response.json()["message"]["content"]