# SolarComplaints.co Assets

Central repository for SolarComplaints.co media, documentation, and article backups.

## 📁 Folder Structure

| Folder | What's in it |
|--------|-------------|
| `/heroes/` | Hero images for blog articles (1400x788 JPG, served via jsDelivr CDN) |
| `/videos/` | Animated hero videos from Gemini and other generators |
| `/docs/` | Framework, playbooks, handoff docs for AI agents |
| `/articles/` | Markdown backups of published articles (for version control) |

## 🔗 CDN URLs

Images and videos in this repo are automatically served via jsDelivr global CDN:

- **Hero image:** `https://cdn.jsdelivr.net/gh/Cryptouprise/solarcomplaints-assets@main/heroes/{article-slug}.jpg`
- **Video:** `https://cdn.jsdelivr.net/gh/Cryptouprise/solarcomplaints-assets@main/videos/{filename}.mp4`
- **Doc (raw):** `https://raw.githubusercontent.com/Cryptouprise/solarcomplaints-assets/main/docs/HANDOFF_FRAMEWORK.md`

## 🚀 How to add a new asset

1. Drop the file in the right folder (name it after the article slug, e.g. `momentum-solar-complaints-2026.jpg`)
2. Commit and push — GitHub auto-updates
3. Within 1-2 minutes, the file is live at the CDN URL above
4. Reference it in the blog admin API `image1` field

## 🧠 Quick Links for AI Agents

- **Handoff Framework:** [`docs/HANDOFF_FRAMEWORK.md`](./docs/HANDOFF_FRAMEWORK.md)
- **Framework Python Helpers:** [`docs/framework_v2.py`](./docs/framework_v2.py)
- **Live article index:** [`articles/INDEX.md`](./articles/INDEX.md)

## ✉️ Contact

Chase Wyatt — Infinite AI / Gosunlite LLC
