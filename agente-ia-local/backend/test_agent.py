import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from dotenv import load_dotenv
load_dotenv()

from agent.agent import run_agent

result = run_agent("What is 25 multiplied by 4?", [])
print("Response:", result["response"])
print("Tool calls:", result["tool_calls"])