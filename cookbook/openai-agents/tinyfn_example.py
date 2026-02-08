"""TinyFn + OpenAI Agents SDK: Deterministic math tools for your AI agent."""

import asyncio
import os

from agents import Agent, Runner
from agents.mcp import MCPServerStreamableHttp

TINYFN_API_KEY = os.environ["TINYFN_API_KEY"]


async def main():
    async with MCPServerStreamableHttp(
        name="TinyFn Math",
        params={
            "url": "https://api.tinyfn.io/mcp/math/",
            "headers": {"X-API-Key": TINYFN_API_KEY},
        },
        cache_tools_list=True,
    ) as server:
        agent = Agent(
            name="Math Assistant",
            instructions="Use the MCP tools for all calculations. Do not compute anything yourself.",
            mcp_servers=[server],
        )

        result = await Runner.run(agent, "What is the factorial of 12?")
        print(result.final_output)

        result = await Runner.run(agent, "Is 7919 a prime number?")
        print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
