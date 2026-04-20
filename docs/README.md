# Docs

Framework, playbooks, and handoff documentation for AI agents working on SolarComplaints.co content.

## 🚀 Start Here

**New to the stack?** Read these in order:

1. **[CLAUDE_CODE_MCP_SETUP.md](./CLAUDE_CODE_MCP_SETUP.md)** ← START HERE — How to connect Claude Code to every MCP server and API
2. **[HANDOFF_FRAMEWORK.md](./HANDOFF_FRAMEWORK.md)** — Master playbook for content operations (voice, API, SEO, topic selection, 10/10 article template)
3. **[framework_v2.py](./framework_v2.py)** — Reusable Python helpers (CTA cards, case studies, evidence checklists, schema generators)

## 🔗 Quick Reference

- **SolarComplaints.co admin API base:** `https://solarcomplaints.co/api/admin`
- **GitHub assets repo:** `github.com/Cryptouprise/solarcomplaints-assets`
- **Image CDN pattern:** `https://cdn.jsdelivr.net/gh/Cryptouprise/solarcomplaints-assets@main/heroes/{slug}.jpg`
- **Bing IndexNow:** `https://api.indexnow.org/indexnow`
- **n8n:** `https://infiniten8n-u44853.vm.elestio.app/`

## ⚡ Claude Code 30-second setup

```bash
# 1. Load your secrets file (see CLAUDE_CODE_MCP_SETUP.md for template)
source ~/.solarcomplaints-secrets.sh

# 2. Connect the critical MCP servers
claude mcp add --transport http supabase -s user https://mcp.supabase.com/mcp
claude mcp add --transport http clickup -s user https://mcp.clickup.com/mcp
claude mcp add --transport http n8n -s user "https://infiniten8n-u44853.vm.elestio.app/mcp/$N8N_MCP_TOKEN"
claude mcp add --transport http airtable -s user https://mcp.airtable.com/mcp
# ... see CLAUDE_CODE_MCP_SETUP.md for the full list

# 3. Verify
claude mcp list

# 4. Inside a Claude Code session, run /mcp to complete OAuth flows
```

## ⚠️ Security

This is a public repo. Never commit API keys or secrets directly. Use environment variables loaded from a local secrets file outside the repo (see CLAUDE_CODE_MCP_SETUP.md for the template). GitHub push protection is enabled and will block commits that contain detected secrets.
