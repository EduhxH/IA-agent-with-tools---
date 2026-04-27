import os
import shutil
from fastapi import FastAPI, UploadFile, File, HTTPException
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

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "..", "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

MCP_ENV_PATH = r"C:\Users\Yor\Documents\mcp-server-pro\mcp-server-pro\.env"


class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"


class WorkspaceRequest(BaseModel):
    path: str


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


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    dest = os.path.join(UPLOAD_DIR, file.filename)
    with open(dest, "wb") as f:
        shutil.copyfileobj(file.file, f)
    return {"filename": file.filename, "path": dest}


@app.get("/uploads")
async def list_uploads():
    files = os.listdir(UPLOAD_DIR)
    return {"files": files}


@app.post("/workspace")
async def set_workspace(req: WorkspaceRequest):
    path = req.path.strip()
    if not os.path.isdir(path):
        raise HTTPException(status_code=400, detail=f"Path does not exist: {path}")

    lines = []
    with open(MCP_ENV_PATH, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("WORKSPACE_ROOT="):
                lines.append(f"WORKSPACE_ROOT={path}\n")
            else:
                lines.append(line)

    with open(MCP_ENV_PATH, "w", encoding="utf-8") as f:
        f.writelines(lines)

    return {"ok": True, "workspace": path}


@app.get("/workspace")
async def get_workspace():
    with open(MCP_ENV_PATH, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("WORKSPACE_ROOT="):
                return {"workspace": line.split("=", 1)[1].strip()}
    return {"workspace": ""}