"""TinyFn + Pydantic AI: Deterministic math tools for your AI agent."""

import asyncio
import os

from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStreamableHTTP

TINYFN_API_KEY = os.environ["TINYFN_API_KEY"]

server = MCPServerStreamableHTTP(
    "https://api.tinyfn.io/mcp/math/",
    headers={"X-API-Key": TINYFN_API_KEY},
)

agent = Agent(
    "anthropic:claude-sonnet-4-20250514",
    toolsets=[server],
    system_prompt="Use the MCP tools for all calculations. Do not compute anything yourself.",
)


async def main():
    async with agent:
        result = await agent.run("What is the factorial of 12?")
        print(result.output)

        result = await agent.run("Is 7919 a prime number?")
        print(result.output)

        result = await agent.run("What is the GCD of 48 and 18?")
        print(result.output)


if __name__ == "__main__":
    asyncio.run(main())
