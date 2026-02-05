# TinyFn MCP Examples

This directory contains examples of using TinyFn MCP with various AI assistants and clients.

## Quick Examples

### Math Operations

Ask your AI assistant:
- "Is 17 a prime number?"
- "What's the factorial of 10?"
- "Calculate 15% of 847"

### Conversions

- "Convert 72°F to Celsius"
- "How many miles is 100 kilometers?"
- "Convert #3B82F6 to RGB"

### Validation

- "Is `user@example.com` a valid email?"
- "Validate this credit card: 4111111111111111"
- "Is this a valid UUID: 550e8400-e29b-41d4-a716-446655440000?"

### Encoding

- "Base64 encode 'Hello, World!'"
- "Generate a SHA-256 hash of 'password123'"
- "URL encode this string: 'hello world & goodbye'"

### Date/Time

- "How many days between January 1, 2024 and March 15, 2024?"
- "What's the current Unix timestamp?"
- "Convert 2:30 PM EST to PST"

### Generators

- "Generate a UUID"
- "Create a secure 16-character password"
- "Give me a random number between 1 and 100"

## Integration Examples

### Claude Desktop

```json
{
  "mcpServers": {
    "tinyfn": {
      "command": "npx",
      "args": ["-y", "@tinyfn/mcp"],
      "env": {
        "TINYFN_API_KEY": "your-api-key"
      }
    }
  }
}
```

### Cursor

Add to your MCP settings:

```json
{
  "mcpServers": {
    "tinyfn": {
      "command": "npx",
      "args": ["-y", "@tinyfn/mcp"],
      "env": {
        "TINYFN_API_KEY": "your-api-key"
      }
    }
  }
}
```

### REST API

```bash
# Check if prime
curl "https://api.tinyfn.io/v1/math/is-prime?number=17" \
  -H "X-API-Key: your-api-key"

# Convert temperature
curl "https://api.tinyfn.io/v1/conversions/celsius-to-fahrenheit?celsius=25" \
  -H "X-API-Key: your-api-key"

# Generate UUID
curl "https://api.tinyfn.io/v1/generators/uuid" \
  -H "X-API-Key: your-api-key"

# Validate email
curl "https://api.tinyfn.io/v1/validation/email?email=test@example.com" \
  -H "X-API-Key: your-api-key"
```

## Get Your API Key

Sign up for free at [tinyfn.io](https://tinyfn.io) to get your API key.

Free tier includes 100 requests/month - no credit card required.
