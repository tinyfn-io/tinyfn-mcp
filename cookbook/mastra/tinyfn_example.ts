/**
 * TinyFn + Mastra: Deterministic math tools for your AI agent.
 *
 * Install: npm install @mastra/mcp @mastra/core
 * Run:     npx tsx tinyfn_example.ts
 */

import { MCPClient } from "@mastra/mcp";

const TINYFN_API_KEY = process.env.TINYFN_API_KEY!;

async function main() {
  const mcpClient = new MCPClient({
    servers: {
      tinyfnMath: {
        url: new URL("https://api.tinyfn.io/mcp/math/"),
        requestInit: {
          headers: {
            "X-API-Key": TINYFN_API_KEY,
          },
        },
        eventSourceInit: {
          fetch(input: RequestInfo | URL, init?: RequestInit) {
            const headers = new Headers(init?.headers || {});
            headers.set("X-API-Key", TINYFN_API_KEY);
            return fetch(input, { ...init, headers });
          },
        },
      },
    },
  });

  const tools = await mcpClient.listTools();
  console.log(`Loaded ${Object.keys(tools).length} tools`);
  console.log("Tool names:", Object.keys(tools).slice(0, 10).join(", "), "...");

  await mcpClient.disconnect();
}

main();
