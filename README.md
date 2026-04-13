[🤖 Local AI Agent with Tool Use.md](https://github.com/user-attachments/files/26689456/Local.AI.Agent.with.Tool.Use.md)
<div align="center">

<img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/React-19-61DAFB?style=for-the-badge&logo=react&logoColor=black" />
<img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
<img src="https://img.shields.io/badge/Ollama-Local%20LLM-000000?style=for-the-badge" />
<img src="https://img.shields.io/badge/Vite-Frontend-646CFF?style=for-the-badge&logo=vite&logoColor=white" />
<img src="https://img.shields.io/badge/status-in%20development-yellow?style=for-the-badge" />

<br/>
<br/>

# 🤖 Local AI Agent with Tool Use

**An autonomous AI agent with tool use capabilities running 100% locally.**  
No cloud SDKs. No LangChain. Just pure ReAct pattern implementation.

> 🇺🇸 **Note:** The source code, including variables, functions, and comments, is written entirely in **American English**.

[How It Works](#-how-it-works) • [Features](#-features) • [Tech Stack](#-tech-stack) • [Getting Started](#-getting-started) • [Project Structure](#-project-structure)

</div>

---

## 🧩 About the Project

This project is a deep dive into the **ReAct (Reasoning and Acting)** pattern, built from scratch without relying on high-level AI frameworks.

The goal was to create an agent that doesn't just talk, but actually **executes actions** to find information or perform tasks. It uses a manual implementation of the reasoning loop, where the LLM decides which tool to use, processes the output, and continues until it finds the final answer.

Everything runs locally, ensuring privacy and a deep understanding of the agentic workflow:

- Manual ReAct loop implementation
- Real-time tool execution (Web Search, Calculator, etc.)
- FastAPI-based backend for high performance
- Modern React + Vite frontend for a smooth experience

---

## ⚡ How It Works

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

---

## ✨ Features

- 🛠 **Manual ReAct Pattern** — Implementation of the reasoning loop without LangChain or similar SDKs
- 🌐 **Web Search Tool** — Integrated with DuckDuckGo to find real-time information
- 🔢 **Calculator Tool** — Accurate mathematical operations performed via code execution
- 📂 **File Reader** — Capability to read and process local files for context
- 🚀 **FastAPI Backend** — Lightweight and fast API to handle agent logic
- 💻 **React UI** — Modern and responsive chat interface built with React 19 and Vite
- 🔒 **100% Local** — Powered by Ollama, ensuring your data never leaves your machine
- ⚡ **Real-time Interaction** — Seamless communication between the frontend and the agentic backend

---

## 🛠 Tech Stack

| Technology | Role |
|---|---|
| [React](https://react.dev/) | Frontend UI (Vite) |
| [FastAPI](https://fastapi.tiangolo.com/) | Backend API |
| [Ollama](https://ollama.com/) | Local LLM Engine |
| [DuckDuckGo Search](https://pypi.org/project/duckduckgo-search/) | Web search capability |
| [Pydantic](https://docs.pydantic.dev/) | Data validation |
| [Uvicorn](https://www.uvicorn.org/) | ASGI Server |

---

## 📦 Prerequisites

- [Python 3.11+](https://www.python.org/)
- [Node.js & npm](https://nodejs.org/)
- [Ollama](https://ollama.com/) installed and running locally

---

## 🚀 Getting Started

### 1. Pull the required model

```bash
ollama pull llama3.2 # Or your preferred model
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
source .venv/bin/activate # Linux/Mac
# .venv\Scripts\activate # Windows
pip install -r requirements.txt
```

### 4. Setup Frontend

```bash
cd ../frontend
npm install
```

### 5. Run the Project

**Start Backend:**
```bash
cd backend
uvicorn api.main:app --reload
```

**Start Frontend:**
```bash
cd frontend
npm run dev
```

---

## 📁 Project Structure

```
agente-ia-local/
│
├── backend/
│   ├── agent/              # ReAct loop logic
│   ├── api/                # FastAPI routes & setup
│   ├── tools/              # Tool implementations (search, calc, etc.)
│   ├── .env                # Configuration
│   └── requirements.txt    # Python dependencies
│
├── frontend/
│   ├── src/                # React components & logic
│   ├── public/             # Static assets
│   ├── package.json        # JS dependencies
│   └── vite.config.js      # Vite configuration
│
└── .gitignore
```

---

## 🧠 What I Learned

- Deep understanding of the **ReAct pattern** and agentic reasoning
- How to implement a tool-calling loop manually using system prompts
- Integrating local LLMs (Ollama) with a web application
- Building a decoupled architecture with **FastAPI** and **React**
- Handling asynchronous tool execution and state management in the UI
- Prompt engineering for consistent JSON/Structured outputs from LLMs

---

## 🔮 Future Improvements

- [ ] Support for multi-turn tool execution in a single turn
- [ ] Integration with more specialized tools (Database, API connectors)
- [ ] Dockerization for easier deployment
- [ ] Support for streaming agent thoughts to the UI

---

<div align="center">

Made with 💜 by [EduhxH](https://github.com/EduhxH)

</div>
