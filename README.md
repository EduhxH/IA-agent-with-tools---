<div align="center">

<br>

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![React](https://img.shields.io/badge/React-19-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-000000?style=for-the-badge)
![Pinecone](https://img.shields.io/badge/Pinecone-Vector%20DB-000000?style=for-the-badge&logo=pinecone&logoColor=white)
![Google Cloud](https://img.shields.io/badge/Google%20Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)
![Vite](https://img.shields.io/badge/Vite-Frontend-646CFF?style=for-the-badge&logo=vite&logoColor=white)
![Status](https://img.shields.io/badge/status-in%20development-yellow?style=for-the-badge)

<br>

# 🤖 Local AI Agent with Tool Use

### An autonomous AI agent with tool use capabilities running 100% locally.
### Enhanced with [MCP-SERVER-PRO](https://github.com/EduhxH/MCP-SERVER-PRO) for professional tool integration.

<br>

> 🇺🇸 The source code — variables, functions, and comments — is written entirely in **American English**.

<br>

**[How It Works](#%EF%B8%8F-how-it-works)** &nbsp;•&nbsp; **[Features](#-features)** &nbsp;•&nbsp; **[Tech Stack](#%EF%B8%8F-tech-stack)** &nbsp;•&nbsp; **[Getting Started](#-getting-started)** &nbsp;•&nbsp; **[Configuration](#%EF%B8%8F-configuration)** &nbsp;•&nbsp; **[Deployment](#%EF%B8%8F-deployment)**

<br>

</div>

---

<br>

## 🧩 &nbsp;About the Project

This project is a deep dive into the **ReAct (Reasoning and Acting)** pattern — built from scratch, without relying on high-level AI frameworks like LangChain.

The goal was to create an agent that doesn't just talk, but actually **executes actions** to find information and perform tasks. It uses a manual implementation of the reasoning loop, where the LLM decides which tool to invoke, processes the output, and continues reasoning until it reaches a final answer.

Now integrated with the **Model Context Protocol (MCP)**, the agent can leverage professional-grade tools via [MCP-SERVER-PRO](https://github.com/EduhxH/MCP-SERVER-PRO) for database management, spreadsheet manipulation, and more.

<br>

---

<br>

## ⚡ &nbsp;How It Works

<div align="center">

<br>

```
         User Question
               ↓
      LLM Reasons (Thought)
               ↓
   Action Selection (Tool Call)
               ↓
  Tool Execution (Local / MCP)
               ↓
     Observation (Tool Output)
               ↓
      LLM Final Answer (Result)
```

<br>

*The backend exposes a `/chat` endpoint. On each request, the agent runs the full ReAct loop —*
*reasoning, selecting a tool, executing it, and feeding the result back — until a final answer is reached.*

<br>

</div>

---

<br>

## ✨ &nbsp;Features

<br>

<div align="center">

| Icon | Feature | Description |
|:---:|:---|:---|
| 🛠 | **Manual ReAct Pattern** | Reasoning loop implemented from scratch — no abstractions |
| 📂 | **Smart File Upload** | New frontend button to upload files directly; agent reads them using `file_reader.py` |
| 💻 | **IDE Project Reader** | Advanced feature to read any local project by setting the `workspace_root` path |
| 🌐 | **Web Search Tool** | Real-time search powered by DuckDuckGo |
| 🔢 | **Calculator Tool** | Accurate math operations executed via code |
| 🔌 | **MCP Integration** | Professional tools via [MCP-SERVER-PRO](https://github.com/EduhxH/MCP-SERVER-PRO) |
| 🚀 | **FastAPI Backend** | Lightweight, async API handling all agent logic |
| 🔒 | **100% Local** | Powered by Ollama — data never leaves your machine |

</div>

<br>

---

<br>

## 🛠️ &nbsp;Tech Stack

<br>

<div align="center">

| Technology | Role |
|:---:|:---|
| [React 19](https://react.dev/) | Frontend UI with new File/IDE integration buttons |
| [Vite](https://vitejs.dev/) | Frontend build tool |
| [FastAPI](https://fastapi.tiangolo.com/) | Backend API framework |
| [Ollama](https://ollama.com/) | Local LLM engine |
| [MCP](https://modelcontextprotocol.io/) | Model Context Protocol integration |
| [DuckDuckGo Search](https://pypi.org/project/duckduckgo-search/) | Web search capability |
| [Pydantic](https://docs.pydantic.dev/) | Data validation |

</div>

<br>

---

<br>

## 📦 &nbsp;Prerequisites

Before getting started, make sure you have the following installed:

- [Python 3.11+](https://www.python.org/)
- [Node.js & npm](https://nodejs.org/)
- [Ollama](https://ollama.com/) — running locally on your machine

<br>

---

<br>

## 🚀 &nbsp;Getting Started

<br>

**1 — Pull the required model**

```bash
ollama pull llama3.2   # or your preferred model
```

<br>

**2 — Clone the repository**

```bash
git clone https://github.com/EduhxH/IA-agent-with-tools---.git
cd IA-agent-with-tools---/agente-ia-local
```

<br>

**3 — Set up the backend**

```bash
cd backend
python -m venv .venv

# Activate the virtual environment
source .venv/bin/activate    # Linux / Mac
.venv\Scripts\activate       # Windows

pip install -r requirements.txt
```

<br>

**4 — Set up the frontend**

```bash
cd ../frontend
npm install
```

<br>

**5 — Run the project**

```bash
# Terminal 1 — Backend (inside /backend)
uvicorn api.app:app --reload --port 8000

# Terminal 2 — Frontend (inside /frontend)
npm run dev
```

<br>

<div align="center">

| Service | URL |
|:---:|:---:|
| Frontend | `http://localhost:5173` |
| Backend | `http://localhost:8000` |

</div>

<br>

---

<br>

## ⚙️ &nbsp;Configuration

The backend is configured via environment variables. Create a `.env` file inside `backend/`:

```env
OLLAMA_BASE_URL=http://localhost:11434   # default Ollama address
OLLAMA_MODEL=llama3.2                    # model used for inference
WORKSPACE_ROOT=C:/your/project/path      # configurable path for IDE reader
```

> No API keys required. Everything runs locally through Ollama.

<br>

---

<br>

## ☁️ &nbsp;Deployment

<div align="center">

This project is also deployed in the cloud:

<br>

| Platform | URL |
|:---:|:---|
| 🌐 &nbsp;**Vercel** (Frontend) | [ia-agent-with-tools.vercel.app](https://ia-agent-with-tools.vercel.app) |
| 🚂 &nbsp;**Railway** (Backend) | [ia-agent-with-tools-production.up.railway.app](https://ia-agent-with-tools-production.up.railway.app) |

<br>

> ⚠️ The deployed version uses a remote LLM provider. For full privacy, run the project locally with Ollama.

</div>

<br>

---

<br>

## 📁 &nbsp;Project Structure

```
agente-ia-local/
│
├── backend/
│   ├── agent/
│   │   ├── agent.py            # ReAct loop logic
│   │   └── ollama_client.py    # Ollama HTTP client
│   ├── api/
│   │   └── app.py              # FastAPI routes & app setup
│   ├── tools/                  # Core tool implementations (file_reader.py, etc.)
│   └── requirements.txt
│
├── frontend/
│   ├── src/                    # React components with Upload/IDE UI
│   └── vite.config.js
│
└── .gitignore
```

<br>

---

<br>

## 🧠 &nbsp;What I Learned

- The inner workings of the **ReAct pattern** and how agentic reasoning loops are structured.
- Manual tool-calling implementation using structured system prompts.
- Integration with the **Model Context Protocol (MCP)** for professional toolsets.
- Implementing **File Upload** logic to allow agents to process user-provided data.
- Creating a **Dynamic IDE Reader** to allow AI interaction with any local workspace.
- Designing a clean, decoupled architecture with **FastAPI** and **React 19**.

<br>

---

<br>

<div align="center">

Made with 💜 by [EduhxH](https://github.com/EduhxH)

</div>

