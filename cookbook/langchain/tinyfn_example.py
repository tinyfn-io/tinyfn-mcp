"""TinyFn + LangChain: Deterministic math tools for your AI agent."""

import asyncio
import os

from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_anthropic import ChatAnthropic

TINYFN_API_KEY = os.environ["TINYFN_API_KEY"]

model = ChatAnthropic(model="claude-sonnet-4-20250514")


async def main():
    client = MultiServerMCPClient(
        {
            "tinyfn-math": {
                "transport": "streamable_http",
                "url": "https://api.tinyfn.io/mcp/math/",
                "headers": {"X-API-Key": TINYFN_API_KEY},
            },
        }
    )

    tools = await client.get_tools()
    print(f"Loaded {len(tools)} tools")

    agent = create_agent(model, tools)

    response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What is the factorial of 12?"}]}
    )
    print(response["messages"][-1].content)

    response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "Is 7919 a prime number?"}]}
    )
    print(response["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
