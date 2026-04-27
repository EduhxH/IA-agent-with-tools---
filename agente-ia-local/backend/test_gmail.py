import asyncio
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from agent.mcp_client import call_mcp_tool

async def main():
    print("Testing Gmail read_emails...")
    result = await call_mcp_tool("read_emails", {
        "query": "is:unread",
        "max_results": 3
    })
    print("Result:", result)

asyncio.run(main())