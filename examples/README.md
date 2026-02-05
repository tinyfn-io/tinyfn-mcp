# TinyFn MCP Examples

## Quick Examples

Once configured, ask your AI assistant:

### Math Operations
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

---

## Configuration Examples

### Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "tinyfn-math": {
      "url": "https://api.tinyfn.io/mcp/math/",
      "headers": {
        "X-API-Key": "tf_live_YOUR_KEY_HERE"
      }
    },
    "tinyfn-validate": {
      "url": "https://api.tinyfn.io/mcp/validate/",
      "headers": {
        "X-API-Key": "tf_live_YOUR_KEY_HERE"
      }
    }
  }
}
```

### Claude Code

Add to `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "tinyfn": {
      "url": "https://api.tinyfn.io/mcp/all/",
      "headers": {
        "X-API-Key": "tf_live_YOUR_KEY_HERE"
      }
    }
  }
}
```

### Cursor & Windsurf

Add to your MCP config:

```json
{
  "mcpServers": {
    "tinyfn-validate": {
      "url": "https://api.tinyfn.io/mcp/validate/",
      "headers": {
        "X-API-Key": "tf_live_YOUR_KEY_HERE"
      }
    }
  }
}
```

### Continue.dev

```json
{
  "experimental": {
    "mcpServers": [
      {
        "name": "tinyfn",
        "url": "https://api.tinyfn.io/mcp/math/",
        "headers": {
          "X-API-Key": "tf_live_YOUR_KEY_HERE"
        }
      }
    ]
  }
}
```

---

## Available Servers

| Server | URL | Tools |
|--------|-----|-------|
| All | `https://api.tinyfn.io/mcp/all/` | 500+ |
| Math | `https://api.tinyfn.io/mcp/math/` | 55+ |
| Convert | `https://api.tinyfn.io/mcp/convert/` | 40+ |
| Validate | `https://api.tinyfn.io/mcp/validate/` | 25+ |
| String | `https://api.tinyfn.io/mcp/string/` | 30+ |
| Hash | `https://api.tinyfn.io/mcp/hash/` | 10+ |
| Encode | `https://api.tinyfn.io/mcp/encode/` | 15+ |

> ⚠️ **Important:** URLs must end with `/`

---

## Get Your API Key

Sign up for free at [tinyfn.io](https://tinyfn.io) to get your API key.

Free tier includes 100 requests/month - no credit card required.

Full documentation: [docs.tinyfn.io](https://docs.tinyfn.io)
