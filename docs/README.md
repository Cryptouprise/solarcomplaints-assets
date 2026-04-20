# Docs

Framework, playbooks, research, and content matrix for SolarComplaints.co.

## 🚀 Reading Order (Start Here)

### Setup
1. **[CLAUDE_CODE_MCP_SETUP.md](./CLAUDE_CODE_MCP_SETUP.md)** — Connect Claude Code to all MCP servers and APIs

### Operations playbook
2. **[HANDOFF_FRAMEWORK.md](./HANDOFF_FRAMEWORK.md)** — Voice, article template, API, SEO rules
3. **[framework_v2.py](./framework_v2.py)** — Reusable Python helpers (CTA cards, case studies, schema)

### Content research and planning (THE CORE)
4. **[LEGAL_ARSENAL.md](./LEGAL_ARSENAL.md)** ← THE GOLD — 14 verified legal loopholes with primary source citations, case law, and exact statutory language. Use this for every article.
5. **[ARTICLE_MATRIX.md](./ARTICLE_MATRIX.md)** ← THE ROADMAP — 40+ article topics organized by legal angle, tier, and priority. Claude Code picks any row and publishes.

---

## ⚡ Quick Reference

- **SolarComplaints.co admin API:** `https://solarcomplaints.co/api/admin`
- **GitHub assets:** `github.com/Cryptouprise/solarcomplaints-assets`
- **Image CDN:** `https://cdn.jsdelivr.net/gh/Cryptouprise/solarcomplaints-assets@main/heroes/{slug}.jpg`
- **Bing IndexNow:** `https://api.indexnow.org/indexnow`
- **n8n:** `https://infiniten8n-u44853.vm.elestio.app/`

## 🎯 Core Workflow

1. Open `ARTICLE_MATRIX.md` → pick the next article in publishing order
2. Open `LEGAL_ARSENAL.md` → pull the exact legal citations for that article
3. Open `HANDOFF_FRAMEWORK.md` → apply the 10/10 template and voice rules
4. Use `framework_v2.py` for Python helpers
5. Generate hero image via fal.ai Flux Pro
6. Publish + push to GitHub + submit to Bing IndexNow
7. Verify `seoWarnings: []` on API response

## ⚠️ Security

Public repo. Never commit API keys. Use environment variables from `~/.solarcomplaints-secrets.sh` (template in CLAUDE_CODE_MCP_SETUP.md). GitHub push protection will block commits containing detected secrets.
