# TinyFn MCP Examples

## Natural Language Queries

Once configured, just ask your AI assistant in plain language. TinyFn tools are invoked automatically.

### Math & Numbers
| You ask... | TinyFn tool | Result |
|-----------|-------------|--------|
| *"Is 7919 a prime number?"* | `is_prime(7919)` | `true` |
| *"What's 17% of 4,847?"* | `percentage(17, 4847)` | `823.99` |
| *"Calculate the factorial of 12"* | `factorial(12)` | `479001600` |
| *"What's the GCD of 48 and 18?"* | `gcd(48, 18)` | `6` |
| *"Square root of 144"* | `square_root(144)` | `12` |

### Conversions
| You ask... | TinyFn tool | Result |
|-----------|-------------|--------|
| *"Convert 72°F to Celsius"* | `fahrenheit_to_celsius(72)` | `22.22` |
| *"How many miles is 100 km?"* | `kilometers_to_miles(100)` | `62.14` |
| *"Convert #3B82F6 to RGB"* | `hex_to_rgb("#3B82F6")` | `{r:59, g:130, b:246}` |
| *"42 in binary?"* | `decimal_to_binary(42)` | `"101010"` |
| *"How many pounds is 70 kg?"* | `kilograms_to_pounds(70)` | `154.32` |

### Validation
| You ask... | TinyFn tool | Result |
|-----------|-------------|--------|
| *"Is user@example.com valid?"* | `validate_email("user@example.com")` | `true` |
| *"Validate 4111111111111111"* | `validate_credit_card("4111...")` | `true` (Visa test card) |
| *"Is this a valid UUID?"* | `validate_uuid("550e8400-...")` | `true` |
| *"Check if 192.168.1.1 is valid"* | `validate_ip("192.168.1.1")` | `true` |

### Encoding & Hashing
| You ask... | TinyFn tool | Result |
|-----------|-------------|--------|
| *"Base64 encode 'Hello, World!'"* | `base64_encode("Hello, World!")` | `"SGVsbG8sIFdvcmxkIQ=="` |
| *"SHA-256 hash of 'password123'"* | `hash_sha256("password123")` | `"ef92b778bafe..."` |
| *"URL encode 'hello world'"* | `url_encode("hello world")` | `"hello%20world"` |
| *"Decode this JWT"* | `jwt_decode("eyJhbG...")` | `{header, payload}` |

### Date & Time
| You ask... | TinyFn tool | Result |
|-----------|-------------|--------|
| *"Days between Jan 15 and Mar 22?"* | `date_diff("2024-01-15", "2024-03-22")` | `67 days` |
| *"Is 2024 a leap year?"* | `is_leap_year(2024)` | `true` |
| *"Current Unix timestamp?"* | `get_now()` | ISO 8601 timestamp |
| *"Convert 2:30 PM EST to PST"* | `convert_timezone(...)` | Timezone-adjusted time |

### Generators
| You ask... | TinyFn tool | Result |
|-----------|-------------|--------|
| *"Generate a UUID"* | `generate_uuid()` | `"a1b2c3d4-..."` |
| *"Create a 20-char password"* | `generate_password(20)` | `"kX9#mP2$vL..."` |
| *"Roll 3 six-sided dice"* | `roll_dice(3, 6)` | `[4, 2, 6]` |
| *"Random number 1-100"* | `random_number(1, 100)` | `42` |

### Statistics
| You ask... | TinyFn tool | Result |
|-----------|-------------|--------|
| *"Mean of [10, 20, 30, 40]"* | `calculate_mean([10,20,30,40])` | `25` |
| *"Standard deviation?"* | `calculate_stddev([10,20,30,40])` | `11.18` |
| *"95th percentile?"* | `calculate_percentile(data, 95)` | Percentile value |

### Finance
| You ask... | TinyFn tool | Result |
|-----------|-------------|--------|
| *"20% tip on $85.50"* | `calculate_tip(85.50, 20)` | `$17.10` |
| *"% change from 100 to 125?"* | `percentage_change(100, 125)` | `25%` |
| *"Monthly payment on $200k loan?"* | `loan_payment(200000, 6.5, 30)` | Monthly amount |

---

## Configuration Examples

### Claude Code (all 500+ tools)

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

### Claude Desktop (multi-server)

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
    },
    "tinyfn-hash": {
      "url": "https://api.tinyfn.io/mcp/hash/",
      "headers": {
        "X-API-Key": "tf_live_YOUR_KEY_HERE"
      }
    }
  }
}
```

### Cursor & Windsurf (~40 tool limit)

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

Recommended servers for Cursor/Windsurf (all under 40 tools):
- `validate` — 15 tools
- `hash` — 18 tools
- `encode` — 20 tools
- `generate` — 15 tools
- `finance` — 15 tools
- `stats` — 16 tools

### Continue.dev

```json
{
  "experimental": {
    "mcpServers": [
      {
        "name": "tinyfn-math",
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

| Server | Endpoint | Tools |
|--------|----------|-------|
| **All** | `https://api.tinyfn.io/mcp/all/` | 500+ |
| **Math** | `https://api.tinyfn.io/mcp/math/` | 52 |
| **Convert** | `https://api.tinyfn.io/mcp/convert/` | 42 |
| **String** | `https://api.tinyfn.io/mcp/string/` | 33 |
| **Datetime** | `https://api.tinyfn.io/mcp/datetime/` | 24 |
| **Encode** | `https://api.tinyfn.io/mcp/encode/` | 20 |
| **Hash** | `https://api.tinyfn.io/mcp/hash/` | 18 |
| **Color** | `https://api.tinyfn.io/mcp/color/` | 30 |
| **Stats** | `https://api.tinyfn.io/mcp/stats/` | 16 |
| **Validate** | `https://api.tinyfn.io/mcp/validate/` | 15 |
| **Finance** | `https://api.tinyfn.io/mcp/finance/` | 15 |
| **Generate** | `https://api.tinyfn.io/mcp/generate/` | 15 |

> **Important:** All URLs must end with a trailing `/`

---

## Get Your API Key

Sign up free at [tinyfn.io](https://tinyfn.io) — 100 requests/month, no credit card required.

Full documentation: [docs.tinyfn.io](https://docs.tinyfn.io)
