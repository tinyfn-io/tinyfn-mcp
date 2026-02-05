<div align="center">
  <a href="https://tinyfn.io">
    <img src="assets/tinyfn-logo.svg" alt="TinyFn Logo" width="200">
  </a>

  <h1>TinyFn MCP Server</h1>

  <p>
    <strong>🧮 500+ deterministic tools for AI agents</strong><br/>
    <i>Eliminate hallucinations in math, conversions, and validations</i>
  </p>

  <p>
    <a href="https://github.com/tinyfn-io/tinyfn-mcp/blob/main/LICENSE">
      <img src="https://img.shields.io/badge/license-MIT-purple?style=for-the-badge" alt="License"/>
    </a>
    <a href="https://docs.tinyfn.io">
      <img src="https://img.shields.io/badge/docs-tinyfn.io-blue?style=for-the-badge" alt="Documentation"/>
    </a>
  </p>

  <p>
    <a href="#-quick-start">Quick Start</a> •
    <a href="#-available-mcp-servers">Servers</a> •
    <a href="#-tool-categories">Tools</a> •
    <a href="#-pricing">Pricing</a> •
    <a href="https://docs.tinyfn.io">Docs</a>
  </p>

  <div>
    <h3>🎉 <strong>Free Tier Available!</strong> 🎉</h3>
    <p><strong>100 requests/month FREE</strong> <br/>
    <sub>No credit card required</sub></p>
  </div>
</div>

---

## 🌟 Overview

**Your AI agent sucks at counting.** LLMs hallucinate on basic math, mess up unit conversions, and can't reliably validate emails. TinyFn fixes this with 500+ deterministic tools that always return the correct answer.

Built for the [Model Context Protocol (MCP)](https://modelcontextprotocol.io), TinyFn gives your AI assistant reliable utilities for the boring stuff—so it can focus on what it's actually good at.

<div align="center">
  <table>
    <tr>
      <td align="center">✅ <strong>500+ Tools</strong><br/><sub>Math, strings, dates, and more</sub></td>
      <td align="center">🎯 <strong>Zero Hallucinations</strong><br/><sub>Deterministic results every time</sub></td>
      <td align="center">⚡ <strong>Lightning Fast</strong><br/><sub>Edge-optimized responses</sub></td>
      <td align="center">🔌 <strong>Works Everywhere</strong><br/><sub>Claude, Cursor, any MCP client</sub></td>
    </tr>
  </table>
</div>

---

## 🎯 Why TinyFn?

LLMs are incredible at reasoning, creativity, and understanding context. But they're terrible at:

- ❌ Basic arithmetic (`What's 17% of 4,847?`)
- ❌ Unit conversions (`Convert 72°F to Celsius`)
- ❌ Date calculations (`How many days between Jan 15 and Mar 22?`)
- ❌ Regex validation (`Is this a valid email?`)
- ❌ Hash generation (`Generate a SHA-256 hash`)

**TinyFn handles the boring stuff, done right.**

---

## ⚡ Quick Start

> 💡 **Get your free API key at [tinyfn.io](https://tinyfn.io)**

### Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or `%APPDATA%\Claude\claude_desktop_config.json` (Windows):

```json
{
  "mcpServers": {
    "tinyfn-math": {
      "url": "https://api.tinyfn.io/mcp/math/",
      "headers": {
        "X-API-Key": "tf_live_YOUR_KEY_HERE"
      }
    }
  }
}
```

> **Note:** Claude Desktop supports ~100 tools, so add 2-3 category servers as needed.

### Cursor & Windsurf

These platforms have a ~40 tool limit. Add to your MCP config:

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

Recommended servers: `validate` (25 tools), `hash` (10 tools), `encode` (15 tools).

### Claude Code

Claude Code supports Tool Search, so you can use the full server with all 500+ tools:

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

> ⚠️ **Important:** URLs must end with `/` or requests will fail with 404 errors.

---

## 📡 Available MCP Servers

| Server | URL | Tools | Best For |
|--------|-----|-------|----------|
| **All** | `/mcp/all/` | 500+ | Claude Code (with Tool Search) |
| **Math** | `/mcp/math/` | 55+ | Arithmetic, trigonometry, comparisons |
| **Convert** | `/mcp/convert/` | 40+ | Temperature, length, weight conversions |
| **Validate** | `/mcp/validate/` | 25+ | Email, URL, phone, credit card validation |
| **String** | `/mcp/string/` | 30+ | Text manipulation, counting |
| **Hash** | `/mcp/hash/` | 10+ | MD5, SHA256, SHA512, bcrypt |
| **Encode** | `/mcp/encode/` | 15+ | Base64, URL, HTML encoding |
| **Datetime** | `/mcp/datetime/` | 30+ | Date parsing, formatting, timezones |
| **Color** | `/mcp/color/` | 30+ | Color conversion, manipulation |
| **Stats** | `/mcp/stats/` | 20+ | Mean, median, standard deviation |
| **Finance** | `/mcp/finance/` | 15+ | Interest, loans, ROI |
| **Generate** | `/mcp/generate/` | 15+ | UUIDs, passwords, random values |

All servers use base URL: `https://api.tinyfn.io`

---

## 🛠️ Tool Categories

TinyFn provides **500+ tools** organized into categories:

<details>
<summary><strong>🔢 Math & Numbers</strong> (50+ tools)</summary>

| Tool | Description |
|------|-------------|
| `is_even`, `is_odd` | Check number parity |
| `is_prime` | Primality testing |
| `factorial`, `fibonacci` | Sequence calculations |
| `gcd`, `lcm` | Greatest common divisor, least common multiple |
| `percentage`, `average` | Statistical basics |
| `power`, `square_root` | Exponentiation |
| `sin`, `cos`, `tan` | Trigonometric functions |
| `log`, `log10`, `exp` | Logarithmic functions |
| `floor`, `ceil`, `round` | Rounding operations |

</details>

<details>
<summary><strong>📝 String Operations</strong> (30+ tools)</summary>

| Tool | Description |
|------|-------------|
| `reverse_string` | Reverse text |
| `uppercase`, `lowercase` | Case conversion |
| `camel_case`, `snake_case`, `kebab_case` | Naming conventions |
| `slug` | URL-safe slugs |
| `trim`, `pad` | Whitespace handling |
| `word_count`, `string_length` | Text metrics |
| `contains`, `starts_with`, `ends_with` | String matching |
| `split`, `join` | Array operations |

</details>

<details>
<summary><strong>✅ Validation</strong> (20+ tools)</summary>

| Tool | Description |
|------|-------------|
| `validate_email` | Email format validation |
| `validate_url` | URL format validation |
| `validate_phone` | Phone number validation |
| `validate_credit_card` | Credit card number validation (Luhn) |
| `validate_uuid` | UUID format validation |
| `validate_ip` | IPv4/IPv6 validation |
| `validate_json` | JSON syntax validation |
| `validate_date` | Date format validation |

</details>

<details>
<summary><strong>🔄 Conversions</strong> (50+ tools)</summary>

| Tool | Description |
|------|-------------|
| `celsius_to_fahrenheit` | Temperature conversion |
| `kilometers_to_miles` | Distance conversion |
| `kilograms_to_pounds` | Weight conversion |
| `liters_to_gallons` | Volume conversion |
| `hex_to_rgb`, `rgb_to_hex` | Color conversion |
| `decimal_to_binary` | Base conversion |
| `bytes_to_human` | File size formatting |

</details>

<details>
<summary><strong>🔐 Encoding & Hashing</strong> (35+ tools)</summary>

| Tool | Description |
|------|-------------|
| `base64_encode`, `base64_decode` | Base64 encoding |
| `url_encode`, `url_decode` | URL encoding |
| `hash_md5`, `hash_sha256`, `hash_sha512` | Cryptographic hashes |
| `hmac_sha256` | HMAC signatures |
| `jwt_decode` | JWT parsing (no verification) |
| `rot13` | ROT13 cipher |

</details>

<details>
<summary><strong>📅 Date & Time</strong> (30+ tools)</summary>

| Tool | Description |
|------|-------------|
| `get_now` | Current timestamp |
| `format_date`, `parse_date` | Date formatting |
| `date_diff` | Days between dates |
| `add_time`, `subtract_time` | Date arithmetic |
| `convert_timezone` | Timezone conversion |
| `is_leap_year` | Leap year check |
| `calculate_age` | Age calculation |
| `relative_time` | "2 hours ago" formatting |

</details>

<details>
<summary><strong>🎲 Generators</strong> (15+ tools)</summary>

| Tool | Description |
|------|-------------|
| `generate_uuid` | UUID v4 generation |
| `generate_password` | Secure password generation |
| `random_number`, `random_string` | Random value generation |
| `generate_lorem` | Lorem ipsum text |
| `roll_dice`, `flip_coin` | Random games |

</details>

<details>
<summary><strong>🎨 Colors</strong> (30+ tools)</summary>

| Tool | Description |
|------|-------------|
| `hex_to_hsl`, `hsl_to_hex` | Color space conversion |
| `lighten_color`, `darken_color` | Color manipulation |
| `complement_color` | Complementary colors |
| `contrast_ratio` | WCAG contrast checking |
| `generate_gradient` | Gradient generation |

</details>

<details>
<summary><strong>📊 Statistics</strong> (20+ tools)</summary>

| Tool | Description |
|------|-------------|
| `calculate_mean`, `calculate_median`, `calculate_mode` | Central tendency |
| `calculate_variance`, `calculate_stddev` | Dispersion |
| `calculate_percentile` | Percentile calculation |
| `calculate_correlation` | Correlation coefficient |

</details>

<details>
<summary><strong>💰 Finance</strong> (15+ tools)</summary>

| Tool | Description |
|------|-------------|
| `compound_interest` | Interest calculations |
| `loan_payment` | Monthly payment calculator |
| `calculate_tip` | Tip calculator |
| `percentage_change` | Growth/decline calculation |
| `mortgage_calculator` | Mortgage payments |

</details>

<details>
<summary><strong>🏃 Health</strong> (10+ tools)</summary>

| Tool | Description |
|------|-------------|
| `calculate_bmi` | Body Mass Index |
| `calculate_bmr` | Basal Metabolic Rate |
| `heart_rate_zones` | Training zones |
| `calories_burned` | Exercise calories |

</details>

<details>
<summary><strong>🎭 Fun</strong> (10+ tools)</summary>

| Tool | Description |
|------|-------------|
| `magic_8_ball` | Magic 8-ball responses |
| `dad_joke` | Random dad jokes |
| `fortune_cookie` | Fortune messages |
| `random_compliment` | Compliment generator |

</details>

---

## 💰 Pricing

<div align="center">
  <table>
    <tr>
      <th width="25%">Free</th>
      <th width="25%">Starter</th>
      <th width="25%">Pro</th>
      <th width="25%">Enterprise</th>
    </tr>
    <tr>
      <td align="center">
        <h3>$0/month</h3>
        <p><strong>100 requests</strong></p>
        <hr/>
        <p>✅ All 500+ tools<br/>
        ✅ MCP & REST API<br/>
        ✅ Community support</p>
      </td>
      <td align="center">
        <h3>$9/month</h3>
        <p><strong>10,000 requests</strong></p>
        <hr/>
        <p>✅ Everything in Free<br/>
        ✅ Priority support<br/>
        ✅ Usage analytics</p>
      </td>
      <td align="center">
        <h3>$30/month</h3>
        <p><strong>100,000 requests</strong></p>
        <hr/>
        <p>✅ Everything in Starter<br/>
        ✅ Higher rate limits<br/>
        ✅ Dedicated support</p>
      </td>
      <td align="center">
        <h3>Custom</h3>
        <p><strong>Unlimited</strong></p>
        <hr/>
        <p>✅ Everything in Pro<br/>
        ✅ SLA guarantee<br/>
        ✅ Custom integrations</p>
      </td>
    </tr>
  </table>
</div>

---

## 📚 Documentation

<div align="center">
  <a href="https://docs.tinyfn.io">
    <img src="https://img.shields.io/badge/📖_Docs-blue?style=for-the-badge" alt="Docs"/>
  </a>
  <a href="https://docs.tinyfn.io/mcp/overview">
    <img src="https://img.shields.io/badge/🔌_MCP_Guide-green?style=for-the-badge" alt="MCP Guide"/>
  </a>
  <a href="https://docs.tinyfn.io/api">
    <img src="https://img.shields.io/badge/🛠️_API_Reference-orange?style=for-the-badge" alt="API Reference"/>
  </a>
</div>

---

## 🤝 Support

- 📧 Email: [support@tinyfn.io](mailto:support@tinyfn.io)
- 🐛 Issues: [GitHub Issues](https://github.com/tinyfn-io/tinyfn-mcp/issues)

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

<div align="center">
  <p>
    <strong>The boring stuff, done right.</strong>
  </p>
  <p>
    <a href="https://tinyfn.io">Website</a> •
    <a href="https://docs.tinyfn.io">Documentation</a> •
    <a href="https://twitter.com/tinyfn_io">Twitter</a>
  </p>
</div>
