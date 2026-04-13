import { useState, useRef, useEffect } from "react"
import { ToolBadge } from "./ToolBadge"

const API = "http://localhost:8000"

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
  const bottomRef = useRef(null)
  const inputRef = useRef(null)

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" })
  }, [messages, loading])

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
    } catch (e) {
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

  return (
    <div className="layout">
      {/* Animated background blobs */}
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
          {messages.length > 0 && (
            <button className="btn-clear" onClick={clearChat} title="Clear chat">
              ✕ Clear
            </button>
          )}
        </header>

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
