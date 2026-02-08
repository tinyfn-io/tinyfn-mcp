"""TinyFn + CrewAI: Deterministic math tools for your AI agent."""

import os

from crewai import Agent, Task, Crew
from crewai.mcp import MCPServerHTTP

TINYFN_API_KEY = os.environ["TINYFN_API_KEY"]

agent = Agent(
    role="Math Assistant",
    goal="Solve math problems using remote tools",
    backstory="Expert mathematician with access to deterministic computation tools.",
    mcps=[
        MCPServerHTTP(
            url="https://api.tinyfn.io/mcp/math/",
            headers={"X-API-Key": TINYFN_API_KEY},
        ),
    ],
)

task = Task(
    description="What is the factorial of 12? Is 7919 a prime number?",
    expected_output="The factorial value and the primality result.",
    agent=agent,
)

crew = Crew(agents=[agent], tasks=[task])
result = crew.kickoff()
print(result)
