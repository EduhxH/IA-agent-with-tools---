<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![React](https://img.shields.io/badge/React-19-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-000000?style=for-the-badge)
![Vite](https://img.shields.io/badge/Vite-Frontend-646CFF?style=for-the-badge&logo=vite&logoColor=white)
![Status](https://img.shields.io/badge/status-in%20development-yellow?style=for-the-badge)

# 🤖 Local AI Agent with Tool Use

**An autonomous AI agent with tool use capabilities running 100% locally.**  
No cloud SDKs. **No LangChain.** Just pure ReAct pattern implementation.

> 🇺🇸 **Note:** The source code, including variables, functions, and comments, is written entirely in **American English**.

[How It Works](#-how-it-works) • [Features](#-features) • [Tech Stack](#-tech-stack) • [Getting Started](#-getting-started) • [Deployment](#-deployment) • [Project Structure](#-project-structure)

</div>

---

## 🧩 About the Project

<div align="center">

This project is a deep dive into the **ReAct (Reasoning and Acting)** pattern, built from scratch without relying on high-level AI frameworks like LangChain.

The goal was to create an agent that doesn't just talk, but actually **executes actions** to find information or perform tasks. It uses a manual implementation of the reasoning loop, where the LLM decides which tool to use, processes the output, and continues until it finds the final answer.

Everything runs locally via **Ollama**, ensuring privacy and a deep understanding of the agentic workflow:

</div>

- **Pure Implementation:** Manual ReAct loop without LangChain or similar abstractions.
- **Real-time Tools:** Execution of Web Search, Calculator, and File Reader.
- **Modern Stack:** FastAPI-based backend and React 19 + Vite frontend.
- **100% Local Inference:** Powered by Ollama — no API keys, no cloud, no data leaving your machine.

---

## ⚡ How It Works

<div align="center">

```
User question
     ↓
LLM Reason (Thought)
     ↓
Action Selection (Tool Call)
     ↓
Tool Execution (Web, Calc, etc.)
     ↓
Observation (Tool Output)
     ↓
LLM Final Answer (Result)
```

The backend exposes a `/chat` endpoint. On each request, the agent runs the full ReAct loop — reasoning, selecting a tool, executing it, and feeding the result back into the LLM — until a final answer is reached.

</div>

---

## ✨ Features

<div align="center">

| | Feature | Description |
|---|---|---|
| 🛠 | **Manual ReAct Pattern** | Reasoning loop implemented from scratch for full control |
| 🌐 | **Web Search Tool** | Integrated with DuckDuckGo to find real-time information |
| 🔢 | **Calculator Tool** | Accurate mathematical operations performed via code execution |
| 📂 | **File Reader** | Reads and processes local files for context injection |
| 🚀 | **FastAPI Backend** | Lightweight and fast API handling all agent logic |
| 💻 | **React UI** | Modern and responsive chat interface built with React 19 and Vite |
| 🔒 | **100% Local** | Powered by Ollama; your data never leaves your machine |
| ⚡ | **Real-time Interaction** | Seamless communication between frontend and the agentic backend |

</div>

---

## 🛠 Tech Stack

<div align="center">

| Technology | Role |
|---|---|
| [React 19](https://react.dev/) | Frontend UI (Vite) |
| [FastAPI](https://fastapi.tiangolo.com/) | Backend API |
| [Ollama](https://ollama.com/) | Local LLM Engine |
| [DuckDuckGo Search](https://pypi.org/project/duckduckgo-search/) | Web search capability |
| [Pydantic](https://docs.pydantic.dev/) | Data validation |
| [Uvicorn](https://www.uvicorn.org/) | ASGI Server |

</div>

---

## 📦 Prerequisites

<div align="center">

- [Python 3.11+](https://www.python.org/)
- [Node.js & npm](https://nodejs.org/)
- [Ollama](https://ollama.com/) installed and running locally

</div>

---

## 🚀 Getting Started

### 1. Pull the required model

```bash
ollama pull llama3.2  # Or your preferred model
```

### 2. Clone the repository

```bash
git clone https://github.com/EduhxH/IA-agent-with-tools---.git
cd IA-agent-with-tools---/agente-ia-local
```

### 3. Setup Backend

```bash
cd backend
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

### 4. Setup Frontend

```bash
cd ../frontend
npm install
```

### 5. Run the Project

**Start Backend** (make sure you're inside `backend/`):

```bash
uvicorn api.app:app --reload --port 8000
```

**Start Frontend:**

```bash
cd frontend
npm run dev
```

<div align="center">

The frontend will be available at `http://localhost:5173` and the backend at `http://localhost:8000`.

</div>

---

## ⚙️ Configuration

<div align="center">

The backend reads configuration from environment variables. Create a `.env` file inside `backend/`:

</div>

```env
OLLAMA_BASE_URL=http://localhost:11434   # Default Ollama address
OLLAMA_MODEL=llama3.2                    # Model to use for inference
```

<div align="center">

No API keys required — everything runs locally through Ollama.

</div>

---

## ☁️ Deployment

<div align="center">

This project is also deployed on:

| | Platform | URL |
|---|---|---|
| 🌐 | **Frontend (Vercel)** | [ia-agent-with-tools.vercel.app](https://ia-agent-with-tools.vercel.app) |
| 🚂 | **Backend (Railway)** | [ia-agent-with-tools-production.up.railway.app](https://ia-agent-with-tools-production.up.railway.app) |

> ⚠️ The deployed version connects to a remote LLM provider. Local setup uses Ollama for full privacy.

</div>

---

## 📁 Project Structure

```
agente-ia-local/
│
├── backend/
│   ├── agent/
│   │   ├── agent.py            # ReAct loop logic
│   │   └── ollama_client.py    # Ollama HTTP client
│   ├── api/
│   │   ├── __init__.py
│   │   └── app.py              # FastAPI routes & setup
│   ├── tools/                  # Tool implementations (search, calc, file reader)
│   ├── .env                    # Local configuration (not committed)
│   └── requirements.txt        # Python dependencies
│
├── frontend/
│   ├── src/                    # React components & logic
│   ├── public/                 # Static assets
│   ├── package.json            # JS dependencies
│   └── vite.config.js          # Vite configuration
│
└── .gitignore
```

---

## 🧠 What I Learned

<div align="center">

- Deep understanding of the **ReAct pattern** and agentic reasoning loops.
- How to implement a tool-calling loop manually using system prompts.
- Integrating local LLMs via **Ollama's HTTP API** without any SDK abstraction.
- Building a decoupled architecture with **FastAPI** and **React**.
- Handling asynchronous tool execution and state management in the UI.
- Prompt engineering for consistent structured outputs from local LLMs.

---

Made with 💜 by [EduhxH](https://github.com/EduhxH)

</div>
