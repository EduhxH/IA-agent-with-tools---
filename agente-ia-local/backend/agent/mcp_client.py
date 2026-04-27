import asyncio
import os
from contextlib import asynccontextmanager
from typing import Any

from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

_SERVER_PARAMS = StdioServerParameters(
    command="uv",
    args=["run", "mcp-server"],
    cwd=os.getenv("MCP_SERVER_PATH", ".")
)


@asynccontextmanager
async def _mcp_session():
    async with stdio_client(_SERVER_PARAMS) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            yield session


async def call_mcp_tool(tool_name: str, arguments: dict[str, Any]) -> str:
    async with _mcp_session() as session:
        result = await session.call_tool(tool_name, arguments)

    if not result.content:
        raise ValueError(f"Tool '{tool_name}' returned an empty response.")

    return result.content[0].text


async def list_available_tools() -> list[str]:
    async with _mcp_session() as session:
        tools = await session.list_tools()
    return [t.name for t in tools.tools]