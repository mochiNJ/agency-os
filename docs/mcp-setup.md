# MCP Server Setup

Create `.mcp.json` in your `AI Agency` folder. Choose free or paid setup below.

---

## FREE SETUP ($0/month)

```json
{
  "mcpServers": {
    "mcp-image": {
      "command": "npx",
      "args": ["-y", "mcp-image"],
      "env": {
        "GEMINI_API_KEY": "GET_FREE_AT_AISTUDIO.GOOGLE.COM",
        "IMAGE_OUTPUT_DIR": "./clients"
      }
    },
    "postiz": {
      "command": "npx",
      "args": ["-y", "postiz-mcp"],
      "env": {
        "POSTIZ_URL": "http://localhost:5000"
      }
    }
  }
}
```

---

## PAID SETUP (Professional — ~$90-190/month total)

```json
{
  "mcpServers": {
    "higgsfield": {
      "type": "streamable-http",
      "url": "https://api.higgsfield.ai/mcp"
    },
    "claid": {
      "command": "npx",
      "args": ["-y", "claid-mcp"],
      "env": {
        "CLAID_API_KEY": "GET_FROM_CLAID.AI"
      }
    },
    "ayrshare": {
      "command": "npx",
      "args": ["-y", "ayrshare-mcp"],
      "env": {
        "AYRSHARE_API_KEY": "GET_FROM_AYRSHARE.COM"
      }
    },
    "meta-ads": {
      "type": "streamable-http",
      "url": "https://mcp.facebook.com/ads"
    },
    "composio": {
      "command": "npx",
      "args": ["-y", "composio-mcp"],
      "env": {
        "COMPOSIO_API_KEY": "GET_FROM_DASHBOARD.COMPOSIO.DEV"
      }
    },
    "mcp-image": {
      "command": "npx",
      "args": ["-y", "mcp-image"],
      "env": {
        "GEMINI_API_KEY": "GET_FREE_AT_AISTUDIO.GOOGLE.COM",
        "IMAGE_OUTPUT_DIR": "./clients"
      }
    }
  }
}
```

---

## Key MCP Notes

**Meta Ads MCP** (`mcp.facebook.com/ads`):
Official Meta MCP released April 2026. Free to use. 29 tools.
Requires: Facebook Business account + OAuth authorization per client.
START IN READ-ONLY MODE. Enable write permissions only after reviewing.
Tool families: Campaign Creation | Catalog Management | Insights | Audience | Tracking

**Composio MCP** (`dashboard.composio.dev`):
Single connection to 1,000+ tools including: Google Analytics, Google Search Console,
Ahrefs, TikTok, YouTube, LinkedIn, Reddit, X, Google Ads, Meta Ads, HubSpot,
Mailchimp, WhatsApp Business, Slack, Notion, Gmail, Outlook.
Free tier available. Most powerful single MCP addition.

**WhatsApp Business MCP** (via Composio):
After connecting Composio, add WhatsApp Business from their toolkit.
Requires: WhatsApp Business account (separate from personal WhatsApp).
Only message users who have opted in. Include opt-out in every marketing message.

**GoHighLevel MCP** (optional CRM):
Connect GHL via Composio or direct API for contact management, pipeline workflows,
and automated follow-up sequences.

**Postiz** (free publisher):
Self-hosted social media scheduler. Run locally at http://localhost:5000.
Used by the Publisher agent when Ayrshare is not configured.

**Ayrshare MCP** (paid publisher):
Posts to 13+ platforms simultaneously with scheduling.
Used by Publisher agent for production deployments.
