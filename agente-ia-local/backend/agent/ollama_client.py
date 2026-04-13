import requests
import os

OLLAMA_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")

def chat(messages: list, system_prompt: str = "") -> str:
    payload = {
        "model": MODEL,
        "messages": messages,
        "stream": False,
        "options": {
            "temperature": 0.1,
            "num_predict": 2048
        }
    }
    if system_prompt:
        payload["system"] = system_prompt

    response = requests.post(
        f"{OLLAMA_URL}/api/chat",
        json=payload,
        timeout=120
    )
    response.raise_for_status()
    return response.json()["message"]["content"]