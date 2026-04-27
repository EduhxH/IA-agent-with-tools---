import json
import re
from agent.ollama_client import chat
from tools import TOOLS_DESCRIPTION, execute_tool

SYSTEM_PROMPT = f"""You are a helpful and honest AI agent with a persistent knowledge base.

{TOOLS_DESCRIPTION}

Follow these rules:
1. Before answering any question, call query_pinecone to check for relevant stored context.
2. After receiving new information from the user or producing a useful result, call upsert_pinecone to store it.
3. Think step by step. Be concise and direct in your final answers."""


def parse_tool_call(text: str) -> dict | None:
    text = text.strip()
    text = re.sub(r'```json\s*', '', text)
    text = re.sub(r'```\s*', '', text)
    text = text.strip()
    try:
        data = json.loads(text)
        if "tool" in data and "input" in data:
            return data
    except json.JSONDecodeError:
        match = re.search(r'\{[^{}]*"tool"[^{}]*"input"[^{}]*\}', text)
        if match:
            try:
                return json.loads(match.group())
            except Exception:
                pass
    return None


def run_agent(user_message: str, history: list) -> dict:
    messages = history.copy()
    messages.append({"role": "user", "content": user_message})

    tool_calls_log = []
    max_iterations = 6

    for iteration in range(max_iterations):
        response = chat(messages, SYSTEM_PROMPT)
        print(f"[Iteration {iteration+1}] Model: {response[:100]}...")

        tool_call = parse_tool_call(response)

        if tool_call is None:
            messages.append({"role": "assistant", "content": response})
            return {
                "response": response,
                "tool_calls": tool_calls_log,
                "history": messages
            }

        tool_name = tool_call.get("tool")
        tool_input = tool_call.get("input", "")

        if tool_name == "respond":
            messages.append({"role": "assistant", "content": tool_input})
            return {
                "response": tool_input,
                "tool_calls": tool_calls_log,
                "history": messages
            }

        print(f"[tool] {tool_name}({str(tool_input)[:50]})")
        result = execute_tool(tool_name, tool_input)

        tool_calls_log.append({
            "tool": tool_name,
            "input": tool_input,
            "result_preview": result[:150]
        })

        messages.append({"role": "assistant", "content": response})
        messages.append({
            "role": "user",
            "content": f"[Tool result - {tool_name}]: {result[:2000]}"
        })

    final = "Reached the step limit. Summary of what I found: " + \
            ". ".join([f"{t['tool']}: {t['result_preview'][:80]}" for t in tool_calls_log])
    return {"response": final, "tool_calls": tool_calls_log, "history": messages}