const toolMeta = {
  web_search: { icon: "◈", label: "web search" },
  calculator: { icon: "⊞", label: "calculator" },
  read_file:  { icon: "▤", label: "read file" },
}

export function ToolBadge({ toolCall }) {
  const meta = toolMeta[toolCall.tool] || { icon: "●", label: toolCall.tool }
  return (
    <div className="tool-badge">
      <span className="tool-icon">{meta.icon}</span>
      <span className="tool-label">{meta.label}</span>
      <span className="tool-sep">·</span>
      <span className="tool-input">
        {String(toolCall.input).slice(0, 40)}
      </span>
    </div>
  )
}
