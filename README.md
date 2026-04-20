# SolarComplaints.co Assets

Central repository for SolarComplaints.co media, documentation, and article backups.

## 🚨 Using Claude Code? Start Here

👉 **[docs/CLAUDE_CODE_MCP_SETUP.md](./docs/CLAUDE_CODE_MCP_SETUP.md)** — Copy-paste terminal commands to connect every MCP server and API.

## 📁 Folder Structure

| Folder | What's in it |
|--------|-------------|
| `/heroes/` | Hero images for blog articles (served via jsDelivr CDN) |
| `/videos/` | Animated hero videos |
| `/docs/` | Framework, playbooks, and setup docs for AI agents |
| `/articles/` | Markdown backups of published articles |

## 🔗 CDN URLs (served via jsDelivr)

- **Hero image:** `https://cdn.jsdelivr.net/gh/Cryptouprise/solarcomplaints-assets@main/heroes/{article-slug}.jpg`
- **Video:** `https://cdn.jsdelivr.net/gh/Cryptouprise/solarcomplaints-assets@main/videos/{filename}.mp4`
- **Doc (raw markdown):** `https://raw.githubusercontent.com/Cryptouprise/solarcomplaints-assets/main/docs/HANDOFF_FRAMEWORK.md`

## 📚 Key Documents

1. **[docs/CLAUDE_CODE_MCP_SETUP.md](./docs/CLAUDE_CODE_MCP_SETUP.md)** — How to connect Claude Code to the full MCP/API stack
2. **[docs/HANDOFF_FRAMEWORK.md](./docs/HANDOFF_FRAMEWORK.md)** — Master playbook for content operations
3. **[docs/framework_v2.py](./docs/framework_v2.py)** — Python helpers for article generation
4. **[articles/INDEX.md](./articles/INDEX.md)** — Index of published articles with live URLs

## 🚀 How to Add a New Asset

1. Drop the file in the right folder (name it `{article-slug}.jpg` for heroes)
2. Commit and push to main
3. Within 1-2 minutes, the file is live at the CDN URL above
4. Reference it in the blog admin API `image1` field

## ✉️ Contact

Chase Wyatt — Infinite AI / Gosunlite LLC
