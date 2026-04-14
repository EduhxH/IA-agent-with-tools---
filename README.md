<div align="center">

<img src="https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
<img src="https://img.shields.io/badge/React-Frontend-61DAFB?style=for-the-badge&logo=react&logoColor=black" />
<img src="https://img.shields.io/badge/Groq-LLM%20API-F55036?style=for-the-badge" />
<img src="https://img.shields.io/badge/Ollama-Local%20LLM-000000?style=for-the-badge" />
<img src="https://img.shields.io/badge/ReAct-Tool%20Use-7C3AED?style=for-the-badge" />
<img src="https://img.shields.io/badge/status-complete-brightgreen?style=for-the-badge" />

<br/>
<br/>

# 🤖 IA Agent with Tool Use

**An AI agent that reasons, searches, calculates and reads files.**  
Implements the ReAct pattern manually — no LangChain, no shortcuts.

> ⚠️ **Note:** The source code, including variables, functions, and comments, is written entirely in **American English**.

[How It Works](#-how-it-works) • [Features](#-features) • [Tech Stack](#-tech-stack) • [Getting Started](#-getting-started) • [Project Structure](#-project-structure) • [Deploy](#-deploy)

</div>

---

## 🧩 About the Project

This project is a hands-on exploration of **AI agents with tool use**, built without relying on high-level frameworks like LangChain or LlamaIndex.

The goal was to understand how agents work under the hood — by implementing the **ReAct (Reason + Act)** pattern manually:

- The LLM decides which tool to use and responds in structured JSON
- The backend parses that JSON, executes the real tool, and feeds the result back
- The loop continues until the model produces a final answer

Runs locally via **Ollama** or in the cloud via **Groq** (free tier).

---

## ⚡ How It Works

```
User sends a message
        ↓
Backend sends full conversation history to the LLM
        ↓
Model replies with JSON → {"tool": "web_search", "input": "..."}
        ↓
Backend parses JSON and executes the tool
        ↓
Result is injected back into the conversation
        ↓
Model replies again → {"tool": "respond", "input": "final answer"}
        ↓
Frontend displays the answer + tool badges
```

---

## ✨ Features

- 🔍 **Web search** — real-time DuckDuckGo search, no API key required
- ➗ **Safe calculator** — evaluates math expressions using AST parsing, never `eval()`
- 📄 **File reader** — reads local `.txt`, `.md`, `.py`, `.json`, `.csv` files securely
- 🔁 **ReAct loop** — iterative Reason → Act → Observe cycle, up to 6 steps
- 🧩 **Manual tool use** — no SDK abstractions, fully hand-rolled JSON parsing
- 🛡️ **Robust parsing** — handles markdown code blocks, surrounding text, malformed JSON
- 💬 **Session memory** — conversation history preserved per session (last 20 messages)
- 🏷️ **Tool badges** — frontend shows which tools were used for each response
- ⚡ **Thinking indicator** — animated dots while the agent is reasoning
- 💡 **Suggestion chips** — quick-start prompts on empty state
- 🎨 **Dark glassmorphism UI** — anime-inspired interface with animated background

---

## 🛠 Tech Stack

| Technology | Role |
|---|---|
| [Ollama](https://ollama.com/) — `llama3.2` | Local LLM (development) |
| [Groq](https://groq.com/) — `llama-3.1-8b-instant` | Cloud LLM (production, free tier) |
| [FastAPI](https://fastapi.tiangolo.com/) | REST API backend |
| [React](https://react.dev/) + [Vite](https://vitejs.dev/) | Frontend interface |
| [DuckDuckGo Search](https://pypi.org/project/duckduckgo-search/) | Free web search tool |
| [Railway](https://railway.app/) | Backend deployment |
| [Vercel](https://vercel.com/) | Frontend deployment |

---

## 📦 Prerequisites

- [Python 3.11+](https://www.python.org/)
- [Node.js 18+](https://nodejs.org/)
- [Ollama](https://ollama.com/) (for local development)
- [Groq API Key](https://console.groq.com/) (free, for production)

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/EduhxH/IA-agent-with-tools---.git
cd IA-agent-with-tools---/agente-ia-local
```

### 2. Backend setup

```bash
cd backend
pip install -r requirements.txt
```

Create a `.env` file inside `backend/`:

```env
# Local development
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2

# Production (Groq)
GROQ_API_KEY=your_key_here
OLLAMA_MODEL=llama-3.1-8b-instant
```

### 3. Start Ollama (local development only)

```bash
ollama pull llama3.2
ollama serve
```

### 4. Run the backend

```bash
uvicorn api.app:app --reload --port 8000
```

### 5. Run the frontend

```bash
cd ../frontend
npm install
npm run dev
```

> ✅ App running at `http://localhost:5173`

---

## 📁 Project Structure

```
agente-ia-local/
│
├── backend/
│   ├── agent/
│   │   ├── agent.py            # ReAct loop — reason, act, observe
│   │   └── ollama_client.py    # HTTP client for Ollama/Groq API
│   │
│   ├── tools/
│   │   ├── __init__.py         # Tool registry and dispatcher
│   │   ├── web_search.py       # DuckDuckGo search tool
│   │   ├── calculator.py       # AST-based safe math evaluator
│   │   └── file_reader.py      # Sandboxed local file reader
│   │
│   ├── api/
│   │   └── app.py              # FastAPI routes + CORS + session management
│   │
│   ├── Procfile                # Railway deployment config
│   ├── requirements.txt        # Python dependencies
│   └── .env                    # Environment variables (not committed)
│
└── frontend/
    └── src/
        ├── components/
        │   ├── Chat.jsx         # Main chat interface
        │   └── ToolBadge.jsx    # Visual badge for tool calls
        ├── App.jsx
        └── index.css            # Glassmorphism dark theme
```

---

## 🌐 Deploy

### Backend — Railway

1. Connect your GitHub repository on [railway.app](https://railway.app)
2. Set **Root Directory** to `agente-ia-local/backend`
3. Add environment variables:
   - `GROQ_API_KEY` = your Groq key
   - `OLLAMA_MODEL` = `llama-3.1-8b-instant`
4. Deploy — Railway detects the `Procfile` automatically

### Frontend — Vercel

1. Import your repository on [vercel.com](https://vercel.com)
2. Set **Root Directory** to `agente-ia-local/frontend`
3. Add environment variable:
   - `VITE_API_URL` = your Railway backend URL
4. Deploy

---

## ⚠️ Common Issues

**Agent not responding / 500 error**

Check Railway logs. Most common causes:
- `GROQ_API_KEY` missing or invalid
- Model name changed — check [Groq deprecations](https://console.groq.com/docs/deprecations)

**429 Too Many Requests**

Groq free tier has rate limits. Wait 1-2 minutes between requests during testing.

**CORS error on frontend**

Make sure `app.py` has `allow_credentials=False` and `allow_origins=["*"]`.

---

## 🧠 What I Learned

- How to implement the ReAct pattern from scratch without SDKs
- Why tool results are injected as `role: user` messages (no native `role: tool` in most APIs)
- How to build a robust JSON parser for LLM responses that don't always follow instructions
- How to switch between local LLMs (Ollama) and cloud APIs (Groq) with minimal code changes
- How to deploy a Python backend on Railway and a React frontend on Vercel
- Why API keys should never be committed to Git

---

## 🔮 Future Improvements

- [ ] ChromaDB integration for long-term memory
- [ ] Streaming responses token by token
- [ ] More tools (image generation, code execution)
- [ ] Authentication system

---

## 👤 Author

**Eduardo Carvalho** — Escola Secundária de Fesco  
Projeto desenvolvido no âmbito da disciplina de Informática · 2025/2026
