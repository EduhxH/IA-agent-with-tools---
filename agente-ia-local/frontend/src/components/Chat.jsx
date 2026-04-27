import { useState, useRef, useEffect } from "react"
import { ToolBadge } from "./ToolBadge"

const API = import.meta.env.VITE_API_URL || "http://localhost:8000"

const SUGGESTIONS = [
  "Search what is LangGraph",
  "How much is 15% of 847?",
  "What is the ReAct pattern in AI?",
]

export function Chat() {
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState("")
  const [loading, setLoading] = useState(false)
  const [sessionId] = useState(() => `session_${Date.now()}`)
  const [workspace, setWorkspace] = useState("")
  const [workspaceInput, setWorkspaceInput] = useState("")
  const [showWorkspace, setShowWorkspace] = useState(false)
  const [uploadedFiles, setUploadedFiles] = useState([])
  const bottomRef = useRef(null)
  const inputRef = useRef(null)
  const fileInputRef = useRef(null)

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" })
  }, [messages, loading])

  useEffect(() => {
    fetch(`${API}/workspace`)
      .then(r => r.json())
      .then(d => { setWorkspace(d.workspace); setWorkspaceInput(d.workspace) })
      .catch(() => {})

    fetch(`${API}/uploads`)
      .then(r => r.json())
      .then(d => setUploadedFiles(d.files || []))
      .catch(() => {})
  }, [])

  async function send(text) {
    const msg = (text || input).trim()
    if (!msg || loading) return
    setInput("")
    setMessages(prev => [...prev, { role: "user", content: msg }])
    setLoading(true)

    try {
      const res = await fetch(`${API}/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: msg, session_id: sessionId })
      })
      if (!res.ok) throw new Error(`HTTP ${res.status}`)
      const data = await res.json()
      setMessages(prev => [...prev, {
        role: "assistant",
        content: data.response,
        tool_calls: data.tool_calls
      }])
    } catch {
      setMessages(prev => [...prev, {
        role: "assistant",
        content: "⚠ Could not reach the agent. Is Ollama running?\n\nRun: `ollama serve` in a terminal.",
        isError: true
      }])
    } finally {
      setLoading(false)
      inputRef.current?.focus()
    }
  }

  async function clearChat() {
    await fetch(`${API}/chat/${sessionId}`, { method: "DELETE" }).catch(() => {})
    setMessages([])
  }

  async function handleUpload(e) {
    const file = e.target.files[0]
    if (!file) return
    const form = new FormData()
    form.append("file", file)
    try {
      const res = await fetch(`${API}/upload`, { method: "POST", body: form })
      const data = await res.json()
      setUploadedFiles(prev => [...new Set([...prev, data.filename])])
      setMessages(prev => [...prev, {
        role: "assistant",
        content: `File uploaded: ${data.filename}. You can now ask me to read it.`,
      }])
    } catch {
      setMessages(prev => [...prev, {
        role: "assistant",
        content: "Failed to upload file.",
        isError: true
      }])
    }
    e.target.value = ""
  }

  async function saveWorkspace() {
    if (!workspaceInput.trim()) return
    try {
      const res = await fetch(`${API}/workspace`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ path: workspaceInput.trim() })
      })
      const data = await res.json()
      if (!res.ok) {
        setMessages(prev => [...prev, {
          role: "assistant",
          content: `Invalid path: ${data.detail}`,
          isError: true
        }])
        return
      }
      setWorkspace(data.workspace)
      setShowWorkspace(false)
      setMessages(prev => [...prev, {
        role: "assistant",
        content: `Workspace set to: ${data.workspace}. You can now ask me to read files from this project.`,
      }])
    } catch {
      setMessages(prev => [...prev, {
        role: "assistant",
        content: "Failed to update workspace.",
        isError: true
      }])
    }
  }

  return (
    <div className="layout">
      <div className="bg-blob blob-1" />
      <div className="bg-blob blob-2" />
      <div className="bg-blob blob-3" />

      <div className="chat-container">
        {/* Header */}
        <header className="chat-header">
          <div className="header-left">
            <div className="agent-avatar">
              <span>AI</span>
            </div>
            <div>
              <h1 className="agent-name">Local Agent</h1>
              <p className="agent-status">
                <span className="status-dot" />
                powered by Ollama
              </p>
            </div>
          </div>
          <div className="header-actions">
            {/* Upload button */}
            <button
              className="btn-action"
              onClick={() => fileInputRef.current?.click()}
              title="Upload file for the agent to read"
            >
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
                <polyline points="17 8 12 3 7 8"/>
                <line x1="12" y1="3" x2="12" y2="15"/>
              </svg>
              Upload File
            </button>
            <input
              ref={fileInputRef}
              type="file"
              style={{ display: "none" }}
              onChange={handleUpload}
            />

            {/* Workspace button */}
            <button
              className="btn-action"
              onClick={() => setShowWorkspace(prev => !prev)}
              title="Set project workspace for the agent to read"
            >
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/>
              </svg>
              Set Project
            </button>

            {messages.length > 0 && (
              <button className="btn-clear" onClick={clearChat} title="Clear chat">
                ✕ Clear
              </button>
            )}
          </div>
        </header>

        {/* Workspace panel */}
        {showWorkspace && (
          <div className="workspace-panel">
            <p className="workspace-label">
              Current workspace: <code>{workspace || "not set"}</code>
            </p>
            <div className="workspace-input-row">
              <input
                className="workspace-input"
                value={workspaceInput}
                onChange={e => setWorkspaceInput(e.target.value)}
                placeholder="C:\Users\Yor\Documents\my-project"
                onKeyDown={e => e.key === "Enter" && saveWorkspace()}
              />
              <button className="btn-save" onClick={saveWorkspace}>
                Save
              </button>
            </div>
            {uploadedFiles.length > 0 && (
              <div className="uploaded-files">
                <p className="workspace-label">Uploaded files:</p>
                {uploadedFiles.map((f, i) => (
                  <span key={i} className="file-chip">{f}</span>
                ))}
              </div>
            )}
          </div>
        )}

        {/* Messages area */}
        <div className="messages-area">
          {messages.length === 0 ? (
            <div className="empty-state">
              <div className="empty-icon">◈</div>
              <h2>How can I help you?</h2>
              <p>Ask me anything. I can search the web, calculate, and read files.</p>
              <div className="suggestions">
                {SUGGESTIONS.map((s, i) => (
                  <button key={i} className="suggestion-chip" onClick={() => send(s)}>
                    {s}
                  </button>
                ))}
              </div>
            </div>
          ) : (
            messages.map((msg, i) => (
              <div key={i} className={`message-row ${msg.role}`}>
                {msg.role === "assistant" && (
                  <div className="msg-avatar">AI</div>
                )}
                <div className="message-content">
                  {msg.tool_calls?.length > 0 && (
                    <div className="tool-badges">
                      {msg.tool_calls.map((tc, j) => (
                        <ToolBadge key={j} toolCall={tc} />
                      ))}
                    </div>
                  )}
                  <div className={`bubble ${msg.role} ${msg.isError ? "error" : ""}`}>
                    {msg.content}
                  </div>
                </div>
                {msg.role === "user" && (
                  <div className="msg-avatar user-avatar">U</div>
                )}
              </div>
            ))
          )}

          {loading && (
            <div className="message-row assistant">
              <div className="msg-avatar">AI</div>
              <div className="bubble assistant thinking">
                <span className="dot" /><span className="dot" /><span className="dot" />
              </div>
            </div>
          )}
          <div ref={bottomRef} />
        </div>

        {/* Input area */}
        <div className="input-area">
          <div className="input-wrapper">
            <input
              ref={inputRef}
              value={input}
              onChange={e => setInput(e.target.value)}
              onKeyDown={e => e.key === "Enter" && !e.shiftKey && send()}
              placeholder="Ask the agent something..."
              disabled={loading}
              className="chat-input"
            />
            <button
              onClick={() => send()}
              disabled={loading || !input.trim()}
              className="send-btn"
            >
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                <line x1="22" y1="2" x2="11" y2="13" />
                <polygon points="22 2 15 22 11 13 2 9 22 2" />
              </svg>
            </button>
          </div>
          <p className="input-hint">Press Enter to send · Built with Ollama + FastAPI</p>
        </div>
      </div>
    </div>
  )
}