import asyncio
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from agent.mcp_client import call_mcp_tool

async def main():
    print("Testing Pinecone query...")
    result = await call_mcp_tool("query_pinecone", {"text": "test connection"})
    print("Result:", result)

asyncio.run(main())