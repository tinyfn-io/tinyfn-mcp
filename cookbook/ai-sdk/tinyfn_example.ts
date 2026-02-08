/**
 * TinyFn + Vercel AI SDK: Deterministic math tools for your AI agent.
 *
 * Install: npm install ai @ai-sdk/mcp @ai-sdk/openai
 * Run:     npx tsx tinyfn_example.ts
 */

import { createMCPClient } from "@ai-sdk/mcp";
import { generateText } from "ai";
import { openai } from "@ai-sdk/openai";

const TINYFN_API_KEY = process.env.TINYFN_API_KEY!;

async function main() {
  const client = await createMCPClient({
    transport: {
      type: "http",
      url: "https://api.tinyfn.io/mcp/math/",
      headers: {
        "X-API-Key": TINYFN_API_KEY,
      },
    },
  });

  try {
    const tools = await client.tools();

    const result = await generateText({
      model: openai("gpt-4o"),
      tools,
      maxSteps: 5,
      messages: [
        {
          role: "user",
          content: "What is the factorial of 12?",
        },
      ],
    });

    console.log(result.text);
  } finally {
    await client.close();
  }
}

main();
