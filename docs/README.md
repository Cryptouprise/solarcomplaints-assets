# Docs

Framework, playbooks, research, and content matrix for SolarComplaints.co.

## 🚀 For AI Agents — START HERE

### If you are picking up Batch 1 article slots 5-10:
👉 **[AGENT_DISPATCH_BATCH1.md](./AGENT_DISPATCH_BATCH1.md)** ← READ FIRST. Per-slot briefs, workflow, definition of done.

### Setup (do once)
1. **[CLAUDE_CODE_MCP_SETUP.md](./CLAUDE_CODE_MCP_SETUP.md)** — Connect Claude Code to MCP servers and APIs

### Operations playbook
2. **[HANDOFF_FRAMEWORK.md](./HANDOFF_FRAMEWORK.md)** — Voice, article template, API rules
3. **[framework_v2.py](./framework_v2.py)** — Reusable Python helpers (CTA cards, case studies, schema)

### Content research and planning
4. **[LEGAL_ARSENAL.md](./LEGAL_ARSENAL.md)** — 15 verified legal loopholes with primary source citations + case law
5. **[ARTICLE_MATRIX.md](./ARTICLE_MATRIX.md)** — 40+ article topics organized by tier and priority
6. **[MASTER_SLATE_APR_2026.md](./MASTER_SLATE_APR_2026.md)** — Active production slate (Batch 1 + 2 + 3)
7. **[AGENT_DISPATCH_BATCH1.md](./AGENT_DISPATCH_BATCH1.md)** — Specific briefs for current open slots

---

## ⚡ Quick Reference

- **SolarComplaints.co admin API:** `https://solarcomplaints.co/api/admin`
- **GitHub assets:** `github.com/Cryptouprise/solarcomplaints-assets`
- **Image CDN:** `https://cdn.jsdelivr.net/gh/Cryptouprise/solarcomplaints-assets@main/heroes/{slug}.jpg`
- **Bing IndexNow:** `https://api.indexnow.org/indexnow`
- **n8n:** `https://infiniten8n-u44853.vm.elestio.app/`

## 🎯 Core Workflow

1. Open `AGENT_DISPATCH_BATCH1.md` → claim a slot
2. Open `LEGAL_ARSENAL.md` → pull the exact legal citations for your slot's loophole
3. Open `HANDOFF_FRAMEWORK.md` → apply the 10/10 template and voice rules
4. Use `framework_v2.py` for Python helpers
5. Generate hero image via fal.ai Flux Pro (prompt formula in dispatch doc)
6. Publish + push to GitHub + submit to Bing IndexNow
7. Verify `seoWarnings: []` and update articles/INDEX.md

## ⚠️ Security

Public repo. Never commit API keys. Use environment variables from `~/.solarcomplaints-secrets.sh` (template in CLAUDE_CODE_MCP_SETUP.md).
