import asyncio
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from agent.mcp_client import call_mcp_tool

async def main():
    print("Testing Pinecone upsert...")
    result = await call_mcp_tool("upsert_pinecone", {
        "records": [
            {"id": "test-001", "text": "This is a test record to verify the connection works."}
        ]
    })
    print("Upsert result:", result)

    print("\nQuerying back...")
    result = await call_mcp_tool("query_pinecone", {"text": "test connection"})
    print("Query result:", result)

asyncio.run(main())