import json
import asyncio
import threading
from .web_search import web_search
from .calculator import calculator
from .file_reader import read_file
from agent.mcp_client import call_mcp_tool

TOOLS_DESCRIPTION = """
You have access to the following tools. To use one, reply in EXACTLY this JSON format and nothing else:
{"tool": "tool_name", "input": "argument"}

Available tools:
- web_search: Searches for up-to-date information on the web. Input: a search query.
- calculator: Evaluates mathematical expressions. Input: an expression (e.g., "15 * 3 + 7").
- read_file: Reads a local file from the workspace. Input: relative file path (e.g., "backend/agent/agent.py").
- write_file: Writes content to a file in the workspace. Input: JSON string with {"path": "relative/path.py", "content": "file content"}.
- list_directory: Lists contents of a directory in the workspace. Input: relative directory path (e.g., "backend").
- query_pinecone: Searches the persistent knowledge base for relevant context. Input: a natural language query string.
- upsert_pinecone: Stores a fact or result in the knowledge base. Input: JSON string with a list of records, e.g. [{"id": "unique_id", "text": "fact to store"}].
- read_emails: Fetches emails from Gmail. Input: JSON string with optional fields: {"query": "is:unread", "max_results": 3}.
- get_email: Fetches the full content of a single email. Input: the Gmail message ID string.
- suggest_reply: Generates a reply prompt for a given email. Input: JSON string with {"email_id": "id", "tone": "professional"}.
- send_email: Sends an email via Gmail. Input: JSON string with {"to": "email", "subject": "subject", "body": "body"}.
- update_excel_live: Writes a value to the user's open Excel sheet. Input: JSON string with {"cell": "A1", "value": "data"}.
- register_goal: Registers a long-term goal for the agent to pursue. Input: JSON string with {"goal": "description", "priority": 1}.
- list_goals: Lists all registered goals and their status. Input: empty string.
- complete_goal: Marks a goal as completed. Input: the goal ID string.
- self_correction: Analyzes a task error and suggests a fix. Input: JSON string with {"task_id": "id", "error": "error description"}.
- respond: Use this when you have all the information needed to answer the user. Input: your final answer.

Rules:
1. ALWAYS use only one tool at a time.
2. Before answering any question, call query_pinecone to check for stored context.
3. After learning something relevant, call upsert_pinecone to store it.
4. If you need up-to-date information, use web_search before responding.
5. When the user asks about emails, always call read_emails first.
6. Never send an email without the user explicitly confirming the content first.
7. When you have everything you need, use respond with the final answer.
8. NEVER make up facts — if you don't know something, search for it.
9. When the user sets a goal, use register_goal to store it.
10. When a tool fails, use self_correction to suggest a recovery strategy.
"""


def _run_mcp(tool_name: str, arguments: dict) -> str:
    result_container = {}

    def run_in_thread():
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            result_container["result"] = loop.run_until_complete(
                call_mcp_tool(tool_name, arguments)
            )
        except Exception as e:
            result_container["result"] = f"MCP error: {e}"
        finally:
            loop.close()

    thread = threading.Thread(target=run_in_thread)
    thread.start()
    thread.join()
    return result_container.get("result", "MCP error: no result")


def _parse_json_input(tool_input, fallback: dict) -> dict:
    if isinstance(tool_input, dict):
        return tool_input
    try:
        return json.loads(tool_input)
    except Exception:
        return fallback


def execute_tool(tool_name: str, tool_input) -> str:
    if tool_name == "web_search":
        return web_search(tool_input)

    elif tool_name == "calculator":
        return calculator(tool_input)

    elif tool_name == "read_file":
        path = tool_input if isinstance(tool_input, str) else str(tool_input)
        return _run_mcp("read_file", {"path": path})

    elif tool_name == "write_file":
        args = _parse_json_input(tool_input, {})
        return _run_mcp("write_file", args)

    elif tool_name == "list_directory":
        path = tool_input if isinstance(tool_input, str) else "."
        return _run_mcp("list_directory", {"path": path})

    elif tool_name == "query_pinecone":
        query = tool_input if isinstance(tool_input, str) else str(tool_input)
        return _run_mcp("query_pinecone", {"text": query})

    elif tool_name == "upsert_pinecone":
        try:
            records = json.loads(tool_input) if isinstance(tool_input, str) else tool_input
        except Exception:
            records = [{"id": "auto", "text": str(tool_input)}]
        return _run_mcp("upsert_pinecone", {"records": records})

    elif tool_name == "read_emails":
        args = _parse_json_input(tool_input, {"query": "is:unread", "max_results": 3})
        if not args.get("query"):
            args["query"] = "is:unread"
        if not args.get("max_results"):
            args["max_results"] = 3
        return _run_mcp("read_emails", args)

    elif tool_name == "get_email":
        email_id = tool_input if isinstance(tool_input, str) else str(tool_input)
        return _run_mcp("get_email", {"email_id": email_id.strip()})

    elif tool_name == "suggest_reply":
        args = _parse_json_input(tool_input, {"email_id": str(tool_input), "tone": "professional"})
        return _run_mcp("suggest_reply", args)

    elif tool_name == "send_email":
        args = _parse_json_input(tool_input, {})
        return _run_mcp("send_email", args)

    elif tool_name == "update_excel_live":
        args = _parse_json_input(tool_input, {"cell": "A1", "value": str(tool_input)})
        return _run_mcp("update_excel_live", args)

    elif tool_name == "register_goal":
        args = _parse_json_input(tool_input, {"goal": str(tool_input), "priority": 1})
        return _run_mcp("register_autonomous_goal", args)

    elif tool_name == "list_goals":
        return _run_mcp("list_autonomous_goals", {})

    elif tool_name == "complete_goal":
        goal_id = tool_input if isinstance(tool_input, str) else str(tool_input)
        return _run_mcp("complete_goal", {"goal_id": goal_id.strip()})

    elif tool_name == "self_correction":
        args = _parse_json_input(tool_input, {"task_id": "unknown", "error": str(tool_input)})
        return _run_mcp("run_self_correction", args)

    else:
        return f"Tool not found: {tool_name}"