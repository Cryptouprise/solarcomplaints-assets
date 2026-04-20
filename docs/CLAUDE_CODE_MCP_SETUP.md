# Claude Code MCP Setup — SolarComplaints.co Operations

**For:** Chase (and any AI agent using Claude Code to work on SolarComplaints.co)
**Purpose:** Get Claude Code connected to every MCP server and API we use, so it has the same powers as the Claude web/app version.

---

## 🚨 Why This Doc Exists

Claude Code CLI runs **fresh** — it doesn't inherit MCP connections from your Claude.ai account. You have to tell it what servers to connect to. This doc walks through every command.

⚠️ **Secrets handling:** This is a public repo, so actual API keys aren't in this doc. Get them from your Claude memory/1Password, or ask Claude to pull them from the userMemories in a chat session.

---

## ⚡ Quickest Path — Copy/Paste These Commands

Open your terminal (on laptop) or **Termux / Terminal app** (on mobile) and run these one at a time. They all use the `-s user` flag which means **"available everywhere, not just this project"** — so you set it up once and it's there forever.

### Step 1: Confirm Claude Code is installed

```bash
claude --version
```

If that fails, install it first:
```bash
# macOS / Linux
curl -fsSL https://claude.com/code/install.sh | bash

# On iOS/Android via Termux:
pkg install nodejs
npm install -g @anthropic-ai/claude-code
```

### Step 2: Connect ALL your MCP servers (one-shot)

Paste this entire block into your terminal. Each line is a separate MCP server.

```bash
# n8n workflow engine (hosted on Elestio)
# NOTE: replace N8N_MCP_TOKEN with your actual token
claude mcp add --transport http n8n -s user \
  "https://infiniten8n-u44853.vm.elestio.app/mcp/$N8N_MCP_TOKEN"

# n8n via webhook (backup endpoint)
claude mcp add --transport http n8n-webhook -s user \
  "https://infiniten8n-u44853.vm.elestio.app/webhook/mcp/$N8N_MCP_TOKEN"

# Google Workspace (Gmail, Calendar, Drive) — OAuth flow launches in browser
claude mcp add --transport http gmail -s user \
  "https://gmailmcp.googleapis.com/mcp/v1"
claude mcp add --transport http gcal -s user \
  "https://calendarmcp.googleapis.com/mcp/v1"
claude mcp add --transport http gdrive -s user \
  "https://drivemcp.googleapis.com/mcp/v1"

# ClickUp
claude mcp add --transport http clickup -s user \
  "https://mcp.clickup.com/mcp"

# Airtable
claude mcp add --transport http airtable -s user \
  "https://mcp.airtable.com/mcp"

# Supabase (FULL admin — for storage, DB, edge functions)
claude mcp add --transport http supabase -s user \
  "https://mcp.supabase.com/mcp"

# Vercel
claude mcp add --transport http vercel -s user \
  "https://mcp.vercel.com"

# Netlify
claude mcp add --transport http netlify -s user \
  "https://netlify-mcp.netlify.app/mcp"

# Stripe
claude mcp add --transport http stripe -s user \
  "https://mcp.stripe.com"

# Gamma (presentations)
claude mcp add --transport http gamma -s user \
  "https://mcp.gamma.app/mcp"

# Invideo (video generation, SSE transport)
claude mcp add --transport sse invideo -s user \
  "https://mcp.invideo.io/sse"

# Day AI
claude mcp add --transport http dayai -s user \
  "https://day.ai/api/mcp"

# Microsoft Learn
claude mcp add --transport http mslearn -s user \
  "https://learn.microsoft.com/api/mcp"

# FactSet (financial data)
claude mcp add --transport http factset -s user \
  "https://mcp.factset.com/content/v1"
```

### Step 3: Verify everything connected

```bash
claude mcp list
```

You should see every server listed. `✓` means healthy. `○` means pending OAuth.

### Step 4: Run `/mcp` inside a Claude Code session to trigger OAuth flows

Start Claude Code:
```bash
claude
```

Then type:
```
/mcp
```

This opens browser windows for each server that needs OAuth (Google Workspace, ClickUp, Airtable, Supabase, Vercel, Stripe, etc.). Log in to each and authorize. You only do this once.

---

## 🔑 Static API Keys — Environment Variables

Some things aren't MCP servers — they're plain HTTP APIs we call via `curl` or Python. Put these in your shell profile so Claude Code can see them.

### Create a secrets file (NOT in this repo)

```bash
# Create ~/.solarcomplaints-secrets.sh (outside of any repo)
touch ~/.solarcomplaints-secrets.sh
chmod 600 ~/.solarcomplaints-secrets.sh
nano ~/.solarcomplaints-secrets.sh
```

Paste this template and fill in the actual values (get them from your Claude chat memory or 1Password):

```bash
#!/bin/bash
# SolarComplaints.co operational secrets
# Load with: source ~/.solarcomplaints-secrets.sh

# SolarComplaints.co admin API
export SC_ADMIN_KEY="sc_admin_..."
export SC_BASE_URL="https://solarcomplaints.co/api/admin"

# GitHub (for pushing assets to solarcomplaints-assets repo)
export GITHUB_TOKEN="ghp_..."
export GITHUB_USER="Cryptouprise"

# fal.ai (image/video generation — Flux, Imagen, Veo)
export FAL_KEY="..."

# Bing IndexNow
export BING_INDEXNOW_KEY="..."

# n8n MCP token (used in the URLs above)
export N8N_MCP_TOKEN="..."

# Optional services
export LEONARDO_KEY="..."
export GEMINI_KEY="..."  # NOTE: blocked from Anthropic IPs, run from Supabase edge function
export TELNYX_KEY="..."
export FIRECRAWL_KEY="..."
export CREATIFY_API_ID="..."
export CREATIFY_API_KEY="..."
export HOSTINGER_API="..."
```

### Auto-load on every shell start

Add this line to `~/.zshrc` or `~/.bashrc`:

```bash
[ -f ~/.solarcomplaints-secrets.sh ] && source ~/.solarcomplaints-secrets.sh
```

Then reload:
```bash
source ~/.zshrc   # or ~/.bashrc
```

Verify they're set:
```bash
echo $SC_ADMIN_KEY   # should show your key
echo $FAL_KEY
```

---

## 📱 Mobile Setup (iOS / Android)

**⭐ Easiest mobile option:** Use the **Claude mobile app** (not Claude Code). You already have MCP connectors set up in the Claude.ai Settings > Connectors page — those work on mobile natively. No terminal required.

### If you really want Claude Code on mobile:

**Android (Termux):**
```bash
pkg update && pkg upgrade
pkg install nodejs git curl nano
npm install -g @anthropic-ai/claude-code
claude login  # OAuth flow opens browser
# Then run the MCP add commands above
```

**iOS:** Claude Code CLI doesn't have a first-class iOS experience. Options:
1. **SSH into your Hostinger VPS** (`187.77.5.39`) from **Termius** or **Blink Shell**, and run Claude Code there
2. **Use the Claude iOS app directly** — MCP connectors already work

---

## 🛠️ Task-Specific Quick Commands

### Publishing a new blog post to SolarComplaints.co

Inside Claude Code, tell it:

```
Publish a new article to SolarComplaints.co.

Pull the framework docs from:
- https://raw.githubusercontent.com/Cryptouprise/solarcomplaints-assets/main/docs/HANDOFF_FRAMEWORK.md
- https://raw.githubusercontent.com/Cryptouprise/solarcomplaints-assets/main/docs/framework_v2.py

My admin key is in $SC_ADMIN_KEY.
My GitHub token is in $GITHUB_TOKEN.
My fal.ai key is in $FAL_KEY.

The topic is: [TOPIC HERE]

Workflow:
1. Research via web search
2. Generate article HTML following the 10/10 template
3. POST to $SC_BASE_URL/blog
4. Generate hero image via fal.ai Flux Pro 1.1 (landscape 16:9, cinematic documentary style, no text)
5. Push hero to github.com/Cryptouprise/solarcomplaints-assets/heroes/{slug}.jpg
6. Update image1 on the post to https://cdn.jsdelivr.net/gh/Cryptouprise/solarcomplaints-assets@main/heroes/{slug}.jpg
7. Submit to Bing IndexNow with $BING_INDEXNOW_KEY
8. Push markdown backup to github.com/Cryptouprise/solarcomplaints-assets/articles/{slug}.md
9. Confirm seoWarnings is empty
```

### Testing connectivity

Inside a Claude Code session:

```
Test every MCP server I have connected. Report which ones are healthy.
```

### Quick health check for SolarComplaints.co

```bash
curl -s "$SC_BASE_URL/stats" -H "X-Admin-Key: $SC_ADMIN_KEY" | python3 -m json.tool
```

Expected output:
```json
{
    "totalBlogPosts": 129,
    "publishedBlogPosts": 129,
    "seoHealth": {"postsWithoutImage": 0, "postsWithoutDirectAnswer": 0, "postsWithoutFaq": 0}
}
```

---

## 🔍 Troubleshooting

### "Connection closed" errors on Windows
Use `cmd /c` wrapper:
```bash
claude mcp add --transport stdio my-server -- cmd /c npx -y @some/package
```

### MCP server shows as "pending" or "failed"
Run `/mcp` inside a Claude Code session to trigger the OAuth flow.

### "Command not found: claude"
Add npm global bin to your PATH:
```bash
export PATH="$(npm config get prefix)/bin:$PATH"
# Then add that line to ~/.zshrc to persist
```

### Want to remove a server
```bash
claude mcp remove <server-name> -s user
```

### See the config file
```bash
cat ~/.claude.json
```

### A secret got committed to GitHub by mistake
GitHub push protection will block secrets automatically. If one does slip through:
1. Rotate the secret immediately (generate a new one)
2. Revoke the old one
3. Use `git filter-branch` or BFG Repo-Cleaner to remove from history
4. Force-push

**Never put real keys in a public repo file.** Always use environment variables loaded from a secrets file outside the repo.

---

## 📋 Full List of Connected Services

| Service | Transport | Purpose |
|---------|-----------|---------|
| n8n | HTTP | Workflow automation |
| Gmail | HTTP + OAuth | Email |
| Google Calendar | HTTP + OAuth | Calendar |
| Google Drive | HTTP + OAuth | File storage |
| ClickUp | HTTP + OAuth | Task management |
| Airtable | HTTP + OAuth | Database |
| Supabase | HTTP + OAuth | DB + storage + edge functions |
| Vercel | HTTP + OAuth | Deployments |
| Netlify | HTTP + OAuth | Deployments |
| Stripe | HTTP + OAuth | Payments |
| Gamma | HTTP + OAuth | Presentations |
| Invideo | SSE | Video generation |
| Day AI | HTTP | Daily AI ops |
| Microsoft Learn | HTTP | MS/Azure docs |
| FactSet | HTTP | Financial data |

Plus static API keys for:
- **SolarComplaints.co admin** (custom REST)
- **GitHub** (REST via `gh` CLI or curl)
- **fal.ai** (image/video generation)
- **Bing IndexNow** (SEO submission)
- **Telnyx, Firecrawl, Creatify, Leonardo, Hostinger** (as needed)

---

## 🚀 First Task to Run (Smoke Test)

After setup, verify the full stack by running this inside Claude Code:

```
Smoke test. Run these 4 checks and report results:

1. Call $SC_BASE_URL/stats with X-Admin-Key: $SC_ADMIN_KEY — report totalBlogPosts
2. Supabase MCP: list projects — should include kievjwzrvjcielbsegkg and emonjusymdripmkvtttc
3. ClickUp MCP: get workspace hierarchy — confirm I can see my workspace
4. GitHub: GET https://api.github.com/repos/Cryptouprise/solarcomplaints-assets with Bearer $GITHUB_TOKEN — confirm repo access

If any fail, report the error.
```

If all 4 pass, you're fully operational.

---

**Last updated:** April 20, 2026
**Owner:** Chase Wyatt / Infinite AI
**Related:** [HANDOFF_FRAMEWORK.md](./HANDOFF_FRAMEWORK.md) (content operations playbook)
