# TinyFn Cookbook

Working examples of TinyFn MCP integrated with every mainstream AI agent framework.

Each example connects to TinyFn's remote MCP server and uses deterministic math tools to answer questions — no local server or Docker required.

## Prerequisites

1. **Get a free API key** at [tinyfn.io](https://tinyfn.io)
2. Set it as an environment variable:
   ```bash
   export TINYFN_API_KEY="tf_live_YOUR_KEY_HERE"
   ```
3. Set your LLM provider key (Anthropic, OpenAI, or Google):
   ```bash
   export ANTHROPIC_API_KEY="sk-ant-..."
   # or
   export OPENAI_API_KEY="sk-proj-..."
   ```

---

## Python Frameworks

### Pydantic AI

The recommended Python framework for building AI agents with type safety.

```bash
pip install pydantic-ai anthropic
```

```python
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStreamableHTTP

server = MCPServerStreamableHTTP(
    "https://api.tinyfn.io/mcp/math/",
    headers={"X-API-Key": os.environ["TINYFN_API_KEY"]},
)

agent = Agent("anthropic:claude-sonnet-4-20250514", toolsets=[server])

async with agent:
    result = await agent.run("What is the factorial of 12?")
    print(result.output)
```

**[Full example →](pydantic-ai/tinyfn_example.py)**

---

### LangChain

The most popular Python framework for building LLM applications.

```bash
pip install langchain langchain-mcp-adapters langchain-anthropic
```

```python
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent

client = MultiServerMCPClient({
    "tinyfn-math": {
        "transport": "streamable_http",
        "url": "https://api.tinyfn.io/mcp/math/",
        "headers": {"X-API-Key": os.environ["TINYFN_API_KEY"]},
    },
})

tools = await client.get_tools()
agent = create_agent("anthropic:claude-sonnet-4-20250514", tools)
response = await agent.ainvoke({"messages": [{"role": "user", "content": "Is 7919 prime?"}]})
```

**[Full example →](langchain/tinyfn_example.py)**

---

### OpenAI Agents SDK

OpenAI's official Python framework for building multi-agent workflows.

```bash
pip install openai-agents
```

```python
from agents import Agent, Runner
from agents.mcp import MCPServerStreamableHttp

async with MCPServerStreamableHttp(
    name="TinyFn Math",
    params={
        "url": "https://api.tinyfn.io/mcp/math/",
        "headers": {"X-API-Key": os.environ["TINYFN_API_KEY"]},
    },
) as server:
    agent = Agent(name="Math Assistant", mcp_servers=[server])
    result = await Runner.run(agent, "What is the factorial of 12?")
    print(result.final_output)
```

**[Full example →](openai-agents/tinyfn_example.py)**

---

### CrewAI

Python framework for orchestrating multi-agent teams.

```bash
pip install crewai mcp
```

```python
from crewai import Agent, Task, Crew
from crewai.mcp import MCPServerHTTP

agent = Agent(
    role="Math Assistant",
    goal="Solve math problems using remote tools",
    backstory="Expert mathematician.",
    mcps=[
        MCPServerHTTP(
            url="https://api.tinyfn.io/mcp/math/",
            headers={"X-API-Key": os.environ["TINYFN_API_KEY"]},
        ),
    ],
)

task = Task(description="What is the factorial of 12?", expected_output="The result.", agent=agent)
crew = Crew(agents=[agent], tasks=[task])
result = crew.kickoff()
```

**[Full example →](crewai/tinyfn_example.py)**

---

## TypeScript / JavaScript Frameworks

### Vercel AI SDK

The most popular TypeScript framework for building AI applications.

```bash
npm install ai @ai-sdk/mcp @ai-sdk/openai
```

```typescript
import { createMCPClient } from "@ai-sdk/mcp";
import { generateText } from "ai";
import { openai } from "@ai-sdk/openai";

const client = await createMCPClient({
  transport: {
    type: "http",
    url: "https://api.tinyfn.io/mcp/math/",
    headers: { "X-API-Key": process.env.TINYFN_API_KEY! },
  },
});

const tools = await client.tools();

const result = await generateText({
  model: openai("gpt-4o"),
  tools,
  maxSteps: 5,
  messages: [{ role: "user", content: "What is the factorial of 12?" }],
});

console.log(result.text);
await client.close();
```

**[Full example →](ai-sdk/tinyfn_example.ts)**

---

### Google GenKit

Google's TypeScript framework for building AI-powered applications.

```bash
npm install genkit @genkit-ai/mcp @genkit-ai/google-genai
```

```typescript
import { createMcpClient } from "@genkit-ai/mcp";
import { googleAI } from "@genkit-ai/google-genai";
import { genkit } from "genkit";

const ai = genkit({ plugins: [googleAI()] });

const mathClient = createMcpClient({
  name: "tinyfnMath",
  mcpServer: {
    url: "https://api.tinyfn.io/mcp/math/",
    requestInit: {
      headers: { "X-API-Key": process.env.TINYFN_API_KEY! },
    },
  },
});

await mathClient.ready();
const tools = await mathClient.getActiveTools(ai);

const { text } = await ai.generate({
  model: googleAI.model("gemini-2.5-flash"),
  prompt: "What is the factorial of 12?",
  tools,
});
```

**[Full example →](genkit/tinyfn_example.ts)**

---

### Mastra

TypeScript framework for building AI agents and workflows.

```bash
npm install @mastra/mcp @mastra/core
```

```typescript
import { MCPClient } from "@mastra/mcp";

const mcpClient = new MCPClient({
  servers: {
    tinyfnMath: {
      url: new URL("https://api.tinyfn.io/mcp/math/"),
      requestInit: {
        headers: { "X-API-Key": process.env.TINYFN_API_KEY! },
      },
      eventSourceInit: {
        fetch(input, init) {
          const headers = new Headers(init?.headers || {});
          headers.set("X-API-Key", process.env.TINYFN_API_KEY!);
          return fetch(input, { ...init, headers });
        },
      },
    },
  },
});

const tools = await mcpClient.listTools();
```

> **Note:** Mastra requires both `requestInit` and `eventSourceInit` for custom headers because the SSE fallback transport doesn't natively support custom headers.

**[Full example →](mastra/tinyfn_example.ts)**

---

## Which framework should I use?

| Framework | Language | Best for |
|-----------|----------|----------|
| **Pydantic AI** | Python | Type-safe agents, structured outputs |
| **LangChain** | Python | Complex chains, RAG, large ecosystem |
| **OpenAI Agents SDK** | Python | Multi-agent orchestration with OpenAI models |
| **CrewAI** | Python | Multi-agent teams with roles and goals |
| **Vercel AI SDK** | TypeScript | Next.js apps, streaming UI |
| **Google GenKit** | TypeScript | Firebase/Google Cloud integration |
| **Mastra** | TypeScript | Agent workflows, tool orchestration |

## Using other MCP servers

These examples use `/mcp/math/` but TinyFn has [12 category servers](../README.md#-available-mcp-servers). Just change the URL:

```python
# Validation tools
"https://api.tinyfn.io/mcp/validate/"

# Hash & crypto tools
"https://api.tinyfn.io/mcp/hash/"

# All 500+ tools (best for Claude Code)
"https://api.tinyfn.io/mcp/all/"
```

> **Important:** All URLs must end with a trailing `/`.

---

## Troubleshooting

**"404 Not Found"** — Make sure the URL ends with `/`

**"401 Unauthorized"** — Check your API key starts with `tf_live_` and use the `X-API-Key` header

**"Transport error"** — TinyFn uses Streamable HTTP (not legacy SSE). Use `type: "http"` in AI SDK, `MCPServerStreamableHTTP` in Pydantic AI, and `transport: "streamable_http"` in LangChain

**Rate limits** — Free tier is 100 requests/month. [Upgrade at tinyfn.io](https://tinyfn.io)
