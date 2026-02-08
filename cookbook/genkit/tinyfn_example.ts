/**
 * TinyFn + Google GenKit: Deterministic math tools for your AI agent.
 *
 * Install: npm install genkit @genkit-ai/mcp @genkit-ai/google-genai
 * Run:     npx tsx tinyfn_example.ts
 */

import { createMcpClient } from "@genkit-ai/mcp";
import { googleAI } from "@genkit-ai/google-genai";
import { genkit } from "genkit";

const TINYFN_API_KEY = process.env.TINYFN_API_KEY!;

const ai = genkit({
  plugins: [googleAI()],
});

const mathClient = createMcpClient({
  name: "tinyfnMath",
  mcpServer: {
    url: "https://api.tinyfn.io/mcp/math/",
    requestInit: {
      headers: {
        "X-API-Key": TINYFN_API_KEY,
      },
    },
  },
});

async function main() {
  await mathClient.ready();

  const tools = await mathClient.getActiveTools(ai);

  const { text } = await ai.generate({
    model: googleAI.model("gemini-2.5-flash"),
    prompt: "What is the factorial of 12?",
    tools,
  });

  console.log(text);
  await mathClient.disable();
}

main();
