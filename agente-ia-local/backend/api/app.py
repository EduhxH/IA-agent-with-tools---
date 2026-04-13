from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agent.agent import run_agent
from pydantic import BaseModel

app = FastAPI(title="IA Agent Local")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

sessions: dict[str, list] = {}

class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"

@app.post("/chat")
async def chat(req: ChatRequest):
    history = sessions.get(req.session_id, [])
    result = run_agent(req.message, history)
    sessions[req.session_id] = result["history"][-20:]
    return {
        "response": result["response"],
        "tool_calls": result["tool_calls"]
    }

@app.delete("/chat/{session_id}")
async def clear(session_id: str):
    sessions.pop(session_id, None)
    return {"ok": True}

@app.get("/health")
async def health():
    return {"status": "online"}