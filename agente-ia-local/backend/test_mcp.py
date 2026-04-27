import asyncio
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from agent.mcp_client import list_available_tools

async def main():
    print("Testing MCP connection...")
    tools = await list_available_tools()
    print("Available tools:", tools)

asyncio.run(main())