from .web_search import web_search
from .calculator import calculator
from .file_reader import read_file

TOOLS_DESCRIPTION = """
You have access to the following tools. To use one, reply in EXACTLY this JSON format and nothing else:
{"tool": "tool_name", "input": "argument"}

Available tools:
- web_search: Searches for up‑to‑date information on the web. Input: a search query.
- calculator: Evaluates mathematical expressions. Input: an expression (e.g., "15 * 3 + 7").
- read_file: Reads a local file. Input: the file path.
- respond: Use this when you have all the information needed to answer the user. Input: your final answer.

Rules:
1. ALWAYS use only one tool at a time.
2. If you need information, use web_search BEFORE responding.
3. When you have everything you need, use respond with the final answer.
4. NEVER make up facts — if you don’t know something, search for it.
"""


def execute_tool(tool_name: str, tool_input: str) -> str:
    if tool_name == "web_search":
        return web_search(tool_input)
    elif tool_name == "calculator":
        return calculator(tool_input)
    elif tool_name == "read_file":
        return read_file(tool_input)
    else:
        return f"Tool not found: {tool_name}"