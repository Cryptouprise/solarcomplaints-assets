# Agent Dispatch — Batch 1 Articles 5-10

**For:** Claude Code agents (or any AI agent with the MCP/API access)
**Goal:** Publish articles #5-10 from MASTER_SLATE_APR_2026.md using the established framework
**Pace:** As many as possible, in parallel where possible

---

## 🚨 READ THESE FIRST (in order, no exceptions)

1. **`docs/CLAUDE_CODE_MCP_SETUP.md`** — Connect to MCPs and load environment variables
2. **`docs/HANDOFF_FRAMEWORK.md`** — Voice, template, API rules
3. **`docs/LEGAL_ARSENAL.md`** — Verified legal citations (15 loopholes, all primary-source verified)
4. **`docs/MASTER_SLATE_APR_2026.md`** — The article slate
5. **`docs/framework_v2.py`** — Python helpers (use these, don't recreate)

If you skip these, your articles will not match the existing voice, will miss internal links, and will create SEO/style inconsistency across the site. Don't skip.

---

## 🎯 What to Pick Up

These slots are open. Each is independently buildable. You can claim one, work it to completion, then move to the next. Multiple agents can work different slots in parallel.

| Slot | Slug | Title | Tier | Words | Status |
|------|------|-------|------|-------|--------|
| #5 | `unlicensed-solar-contractor-california-bp-7031` | Unlicensed Solar Contractor? You May Owe $0 — The CA B&P 7031 Guide | 🏛️ PILLAR | 2,800 | OPEN |
| #6 | `tila-rescission-solar-loan-3-year-2026` | TILA Rescission for Solar Loans — The 3-Year Undo Button | 🏛️ PILLAR | 2,500 | OPEN |
| #7 | `solar-companies-going-bankrupt-2026-watchlist` | Which Solar Companies Are Going Bankrupt in 2026 — The Watch List | 🔥 NEWS | 2,200 | OPEN |
| #8 | `elder-abuse-solar-fraud-enhanced-damages-2026` | Elder Abuse + Solar Fraud — When Damages Get Doubled or Tripled | 🏛️ PILLAR | 2,200 | OPEN |
| #9 | `how-to-check-solar-loan-dealer-fee-2026` | How to Check If Your Solar Loan Has a Hidden Dealer Fee — 10-Minute Guide | 💰 COMMERCIAL | 1,800 | OPEN |
| #10 | `sell-house-with-solar-lease-legal-ways-out-2026` | Your Solar Lease Is Killing Your Home Sale — 5 Legal Ways Out | 💰 COMMERCIAL | 2,400 | OPEN |

**To claim a slot:** Just start working it. Update this file's status column to "IN PROGRESS — {agent name}" if you want to coordinate, but it's not required if you're working solo.

---

## 📋 Per-Slot Briefs

Each brief tells you the angle, primary legal arsenal entries to pull from, key facts to include, and required internal links. Treat these as the spec — don't deviate from the angle.

### Slot #5 — Unlicensed Solar Contractor? You May Owe $0 (CA B&P 7031)

**Primary loophole:** #7 in LEGAL_ARSENAL.md (Cal. Bus. & Prof. Code § 7031)

**Angle:** California-specific deep dive. The "nuke" framing — if installer's license was invalid for even one day, contract is unenforceable, all payments clawed back, all security interests void. Make it concrete and actionable.

**Key facts to include:**
- Exact statute text (quote (a), (b), (c) from LEGAL_ARSENAL.md)
- Required licenses: C-46 (Solar) or C-10 (Electrical)
- How to check at cslb.ca.gov/OnlineServices/CheckLicenseII
- "Substantial compliance" exception (subdivision (e)) and when it does NOT apply
- MW Erectors v. Niederhauser (2005) 36 Cal.4th 412, 435 — "prevents unlicensed entities from recovering compensation regardless of the balance of the equities"
- Similar statutes in TX (Tex. Occ. Code § 1302), FL (Fla. Stat. § 489.128), NV (NRS 624.320), AZ (A.R.S. § 32-1153)

**Required internal links:**
- 14 Legal Loopholes pillar
- Hidden Dealer Fee article
- FTC Holder Rule article
- California-relevant: Sunrun, Freedom Forever, Momentum Solar pages

**Voice notes:** This is the single most powerful tool for CA homeowners. Frame it as such without overstating. Equipment was never the problem. License was the gatekeeper. License was invalid → contract is unenforceable. That's it.

---

### Slot #6 — TILA Rescission Pillar (with Lankhorst caveat)

**Primary loophole:** #2 in LEGAL_ARSENAL.md

**Angle:** The 3-year undo button — but with the legal nuance most solar exit sites get wrong.

**Critical:** Frame the Lankhorst v. Independent Savings Plan Co., 787 F.3d 1100 (11th Cir. 2015) limitation correctly. UCC-1 fixture filing alone does NOT automatically trigger TILA — needs actual home security interest. DO NOT promise universal applicability. DO explain when it actually applies (deed lien, home improvement security interest, bundled roof work, state law extensions).

**Key facts:**
- 15 USC § 1635 — written notice (not lawsuit) suffices, per Jesinoski v. Countrywide, 574 U.S. 259 (2015)
- 3-year extended window when material disclosure defects exist (wrong APR, wrong amount financed, missing Notice of Right to Cancel)
- Hidden dealer fees create the disclosure defect that triggers the 3-year window
- Massachusetts 209 CMR 32.23 extends rescission rights more broadly than federal TILA
- Loans bundled with roof work, electrical panel upgrades, or rewiring more often qualify

**Required internal links:**
- 14 Loopholes pillar
- Hidden Dealer Fee article (this is the connection point)
- FTC Holder Rule article
- GoodLeap, Mosaic complaint articles

---

### Slot #7 — Solar Companies Going Bankrupt in 2026 (Watch List)

**Primary angle:** Tracker piece + predictive analysis. Evergreen content that gets updated.

**Companies to cover (verified from research):**
- ✅ Already filed: Sunnova (2024), SunPower (2024), Sunlight Financial (2024), Solar Mosaic (2025), Freedom Forever (April 15, 2026)
- 🟡 At risk based on financial signals: Vivint (acquired by Sunrun, customer service degraded), Pink Energy / Power Home Solar (already shut down 2022 — historical context), Vision Solar (multiple state AG actions), Trinity Solar (heavy NJ exposure), Lumio (formed from merger of struggling installers), Titan Solar Power (already bankrupt 2024)

**Key facts:**
- Industry context: residential installs declined 31% in 2024 (CFPB data)
- OBBBA (One Big Beautiful Bill Act) cut tax credits short by 7 years
- SEIA downgraded base case residential outlook 22%
- Pattern: when installer files, FTC Holder Rule + material breach claims against lender become powerful
- 90-day window after filing is when individual settlements get most favorable

**Required internal links:**
- 14 Loopholes pillar
- Cancel Freedom Forever article
- SunStrong warranty article
- Hidden Dealer Fee article

**Voice:** Sober reporting, not gossip. Cite financial signals (CFPB complaints, debt covenants, layoffs) where verifiable. Don't predict bankruptcies on speculation.

---

### Slot #8 — Elder Abuse + Solar Fraud (Enhanced Damages)

**Primary loophole:** #9 in LEGAL_ARSENAL.md

**Angle:** When the homeowner is 65+ (or dependent adult), damages get doubled or tripled. Most powerful in California (Welf. & Inst. Code § 15610.30), but 40+ states have similar statutes.

**Key facts:**
- CA W&I 15610.30: enhanced damages, attorney's fees mandatory, separate private right of action
- Pattern: salesperson targets 65+ homeowner specifically because they often have home equity, fixed income, less skeptical of door-to-door sales
- NY AG Attyx complaint emphasized targeting of elderly/low-income — that framing was strategic
- States with strong elder financial abuse statutes: CA, NY, FL, TX, NJ, MA, CT, PA, IL, AZ, NV, WA, OR (verify each before citing specific statute numbers)
- Enhancement typically: double or treble compensatory damages + attorney's fees + punitive damages available

**Required internal links:**
- 14 Loopholes pillar
- NY AG Attyx article
- Hidden Dealer Fee article
- FTC Holder Rule article

**Voice:** Protective. Outraged but professional. Frame the homeowner as the victim of a deliberate strategy, not as someone who should have known better. The law agrees with that framing — the statutes were written specifically because elders ARE targeted.

---

### Slot #9 — How to Check If Your Solar Loan Has a Hidden Dealer Fee (10-Minute Guide)

**Primary angle:** Practical, high-intent commercial query. Companion piece to the dealer fee pillar (#1 in batch).

**Structure:** Step-by-step. Less narrative, more action items. Should feel like a worksheet.

**Key steps:**
1. Pull your sales proposal AND your loan agreement (different documents — both needed)
2. Find the "system price" or "total project cost" on the sales proposal
3. Find the "Amount Financed" on the loan TILA disclosure
4. Calculate the difference — that's almost certainly the dealer fee
5. If the documents don't show a clear cash price, request it in writing from the installer (refusal = evidence)
6. Cross-reference your lender against the CFPB Issue Spotlight + Minnesota AG complaint
7. Calculate your dealer fee as a % of cash price — anything 10%+ matches the documented pattern
8. Document your findings + your salesperson's verbal promises about the loan terms

**Required internal links:**
- The Hidden Dealer Fee pillar (THE big one)
- 14 Loopholes pillar
- FTC Holder Rule article
- TILA Rescission article (slot #6)
- GoodLeap complaints article

**Voice:** Direct, useful, slightly aggressive. "You can find this in 10 minutes. Here's how."

---

### Slot #10 — Solar Lease Killing Your Home Sale (5 Legal Ways Out)

**Primary angle:** High commercial intent. Homeowners trying to sell a house with a solar lease are often blocked by buyer financing or refusal. This is the practical legal path.

**Structure:** 5 numbered options, each with mechanics + when it applies + outcome.

**The 5 paths:**
1. **Lease buyout via the lessor's stated formula** — typically expensive (often 20-50% above equipment value), but available
2. **Buyout via fraud/misrepresentation challenge** — if salesperson misrepresented buyout flexibility or transferability, the buyout amount is itself contestable
3. **Lease assumption by the buyer** — possible but often blocked by buyer's lender (Fannie Mae and Freddie Mac have specific guidelines)
4. **Material breach rescission** — if lessor failed to maintain system, honor production guarantee, or provide service, the lease may be voidable
5. **State UDAP attack on the lease itself** — particularly in CA (CLRA + UCL), NY (GBL 349), MA (93A) where lease terms can be unconscionable or deceptively disclosed

**Key facts:**
- Sunrun lease buyout calculator article already exists — link to it
- Freddie Mac and Fannie Mae solar lease guidelines (look up current versions)
- "UCC-1 fixture filing" issue — this can cloud title; how to clear it
- Some buyers' lenders refuse to fund any home with solar lease — this is leverage for unconscionability claim

**Required internal links:**
- Sunrun PPA & Lease Buyout Calculator (existing)
- 14 Loopholes pillar
- Is the Sunrun Lease Predatory (existing)
- Hidden Dealer Fee article
- FTC Holder Rule article

**Voice:** Practical. Sympathetic to the homeowner stuck in a contract that's now blocking their life decision. Multiple paths, each with honest tradeoffs.

---

## 🛠️ Workflow For Each Article

For every article, follow this exact sequence. The framework_v2.py handles most of it — use those helpers.

### Step 1: Build the Python publishing script

Use this template (mirror b1_01_dealer_fee.py through b1_04_holder_rule.py):

```python
import sys
sys.path.insert(0, '/path/to/articles')
from framework_v2 import *

SLUG = "your-slug-here"
SRC = "your-src-tag"
PUB_DATE = "2026-04-19"  # or current date
PUB_DATE_SCHEMA = "2026-04-19T21:00:00-05:00"

schema_news = newsarticle_schema(
    headline="...",
    description="...",
    publish_date=PUB_DATE_SCHEMA,
    slug=SLUG,
    keywords=[...]
)

CONTENT = f"""{schema_news}

[3 paragraph intro ending with "Stick with me..."]

{byline("Reviewed by the SolarComplaints.co editorial team — ...")}

<h2>...</h2>
[content with 8-10 internal links woven in naturally]

{case_study(name, city, state, year, company, amount, description, outcome)}

{mid_cta(SRC, "...")}

[more content]

{evidence_checklist([...5 items...])}

[more content]

{outcomes_section()}

<h2>The Bottom Line</h2>
[3-4 paragraph close]

{closing_cta(SRC)}

<h3>Related Reading</h3>
<ul>
<li>...</li>
</ul>
"""

payload = {
    "slug": SLUG,
    "title": "...",
    "content": CONTENT,
    "readTime": [calculated],
    "publishDate": PUB_DATE,
    "metaTitle": "..." # MUST be < 60 chars
    "metaDescription": "..." # MUST be < 160 chars
    "excerpt": "...",
    "keywords": [...],
    "category": "legal" or "news" or "company" or "commercial",
    "image1": f"https://cdn.jsdelivr.net/gh/Cryptouprise/solarcomplaints-assets@main/heroes/{SLUG}.jpg",
    "directAnswer": "...", # AEO-optimized 200-500 word answer
    "faqJson": [
        {"question": "...", "answer": "..."},
        # 5 FAQs minimum
    ],
    "published": True,
    "upsert": True
}

print(publish(payload, is_update=False))
print("Bing:", submit_bing(SLUG))
```

### Step 2: Publish via admin API

The `publish()` helper handles the POST. Watch for SEO warnings — fix them before moving on.

### Step 3: Generate hero image via fal.ai

Use Flux Pro 1.1 (`fal-ai/flux-pro/v1.1`). Prompt formula:
- Documentary realism + cinematic lighting
- Weighty props specific to the article (scales, books, hourglass, anchor, magnifying glass, etc.)
- 16:9 landscape, JPEG output
- ALWAYS include "no text visible, no readable writing, no logos, no signage anywhere" to avoid garbled text

### Step 4: Upload hero to GitHub repo

Path: `heroes/{slug}.jpg`. Use the GitHub Contents API (PUT with base64 content).

### Step 5: Submit to Bing IndexNow

```bash
curl -X POST "https://api.indexnow.org/indexnow" \
  -H "Content-Type: application/json" \
  -d '{
    "host": "solarcomplaints.co",
    "key": "a9dc40ec318d70ab0cee3b6b492b24ce76502dccd7b1b5e3e6e1abe8d1e97a5c",
    "urlList": ["https://solarcomplaints.co/blog/{slug}"]
  }'
```

Expect HTTP 202.

### Step 6: Push article markdown backup

Pull the live post via admin API GET, format as markdown with frontmatter, push to `articles/{slug}.md` in the repo.

### Step 7: Update articles/INDEX.md

Add the new article to the appropriate tier section.

---

## ✅ Definition of Done (per article)

A slot is "done" when ALL of these are true:
- [ ] Article published, returns `seoWarnings: []`
- [ ] Hero image generated, uploaded to `heroes/{slug}.jpg`, CDN URL returns HTTP 200
- [ ] Bing IndexNow returns 202
- [ ] Article markdown backup pushed to `articles/{slug}.md`
- [ ] articles/INDEX.md updated with link to new article
- [ ] Internal links from this article point to correct existing articles
- [ ] At least 2 previously-published articles link BACK to this one (update them via PUT)

---

## 🚫 Common Mistakes to Avoid

1. **Don't restate the angle differently.** The brief above IS the angle. If you change it you'll create internal contradictions across the site.
2. **Don't make up case citations.** If you reference a case, it must exist. Pull from LEGAL_ARSENAL.md only.
3. **Don't make up state-specific statutes.** Verify each one before publishing. State session laws change.
4. **Don't skip internal links.** Every article must link to (a) the 14 Loopholes pillar, (b) the relevant loophole pillar, (c) at least 2 other previously-published articles.
5. **Don't exceed metaTitle 60 chars or metaDescription 160 chars.** This is a hard limit — the API will warn but still publish, then you have to fix. Get it right the first time.
6. **Don't use emojis in body content.** OK in CTA labels, never in article prose.
7. **Don't promise legal advice.** "This is editorial analysis. For your specific situation, get a case review."
8. **Don't write more than 4-5 paragraphs without an H2 break.** Mobile readability matters.

---

## 📊 Live Status Dashboard

Check your work against the live site:
- Stats endpoint: `GET https://solarcomplaints.co/api/admin/stats`
- Single article: `GET https://solarcomplaints.co/api/admin/blog/{slug}`
- All published: count should go up by 1 per article

Current as of session close (April 19, 2026):
- 134 total posts
- Articles 1-4 of Batch 1 complete
- 6 slots open (5-10)

After all 10 done: 140 posts. After Batch 2 (10 more): 150 posts.

---

**Last updated:** April 19, 2026 (after Batch 1 articles 1-4 publish)
**Owner:** Chase Wyatt / Infinite AI
**Status if you need to update:** Edit this file in `docs/AGENT_DISPATCH_BATCH1.md`
