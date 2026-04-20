# SolarComplaints.co — AI Content Operations Playbook

**For:** Any AI agent (Claude Code, GPT, or new Claude chat session) continuing content operations for SolarComplaints.co
**Owner:** Chase Wyatt — Infinite AI / Gosunlite LLC
**Last updated:** April 19, 2026
**Site stats as of handoff:** 129 published blog posts, zero SEO warnings, all posts have image/directAnswer/faqJson

---

## 1. Mission & Business Context

SolarComplaints.co is a **consumer watchdog platform and lead-generation engine** for homeowners trapped in bad residential solar contracts. The business model is simple: rank on Google and AI search for homeowner pain-point queries → convert readers into leads via "Start Your Free Case Review" forms → route leads to specialist partners who pursue contract cancellation or loan reduction.

**What we do for homeowners:**
- **Outcome #1:** Contract completely canceled. Homeowner keeps the equipment. The $30K, $80K, $150K loan? Gone.
- **Outcome #2:** Loan massively reduced — typically 40-60% (e.g., $150K → $75K, $70K → $35K)
- **Guarantee:** If we take the case and cannot deliver either outcome after exhausting every angle, the homeowner gets 40% of their fee back. In writing.

**This is NOT a generic SEO site.** It is a faith-driven, homeowner's-corner advocacy brand that reads like it was written by someone who cares, not by lawyers pretending to care. Tone is direct, specific, and real.

---

## 2. Voice Rules (Non-Negotiable)

Every article must sound like a friend who knows the legal landscape explaining things over coffee — not a law firm brochure.

**DO:**
- Address the reader as "you" directly
- Use short, punchy sentences alongside longer explanatory ones
- Name the real dollar amounts ($30K, $80K, $150K loans; $25K-$40K buyouts; $275M lawsuit)
- Reference real cases, real company names, real dates
- Use the "stick with me" mid-intro hook to retain scrollers ("stick with me — toward the bottom, I'll show you...")
- Call the reader a homeowner, not a consumer or a client
- Say "exit specialist" when referring to who contacts them
- Use em-dashes liberally for rhythm

**DON'T:**
- Write in legalese or corporate HR-speak
- Use vague phrases like "many homeowners find..." when you can say "you"
- Hide the actionable advice. It goes in bold, in blocks, early and often.
- Say "file a lawsuit." Say "get a free case review" or "fight back."
- Over-promise. The 40% refund guarantee is the backstop, not a sales gimmick.
- Use emojis in body copy (they're fine in CTA card labels)
- Sound like ChatGPT

**Example of voice — bad:**
> "Many homeowners who have entered into solar agreements with companies such as Sunrun may experience buyer's remorse. It is important to consult with a legal professional to understand your options."

**Example of voice — good:**
> "You signed a Sunrun lease, the panels are on the roof, and the first payment already hit your bank account. And now you are searching 'how to cancel a Sunrun contract after installation' because something has gone sideways. Here is the truth Sunrun's customer service team will never volunteer: a Sunrun contract IS cancellable after installation."

---

## 3. API Access & Publishing Mechanics

**Admin Base URL:** `https://solarcomplaints.co/api/admin`
**Admin Key:** `sc_admin_Q55em5eWnehqzM2cuEjFmc5x9q_ZjLQ2yn1iUnMyVqk`
**Header:** `X-Admin-Key: sc_admin_Q55em5eWnehqzM2cuEjFmc5x9q_ZjLQ2yn1iUnMyVqk`

**Create a new post:** `POST /blog` with full payload (see Section 5)
**Update existing post:** `PUT /blog/{slug}` with any subset of fields
**List posts:** `GET /blog?limit=100&published=true&offset=0`
**Get single post:** `GET /blog/{slug}`
**Site stats:** `GET /stats`

**Required fields for publish:** `slug`, `title`, `content`, `image1`, `directAnswer`, `faqJson`, `metaTitle`, `metaDescription`
**Recommended fields:** `readTime` (int), `publishDate` (YYYY-MM-DD only — NOT full ISO), `excerpt`, `keywords` (array), `category`

**Field quirks (learned the hard way):**
- `publishDate` MUST be `YYYY-MM-DD` format. ISO 8601 (`2026-04-19T08:00:00-05:00`) fails SQL query.
- `metaTitle` must be under 60 chars or you get an SEO warning.
- `metaDescription` must be under 160 chars or you get an SEO warning.
- `readTime` is an integer (number of minutes). String works too but int is cleaner.
- `image1` accepts any absolute URL (Unsplash, Supabase storage, etc). External URLs render fine.
- `content` is HTML. JSON-LD `<script type="application/ld+json">...` blocks can be embedded at the top.
- Categories used on this site: `news`, `company`, `city-company`, `aeo`, `emotional`, `foundation`, `legal`, `state`.

**After publishing, submit to Bing IndexNow:**
```
POST https://api.indexnow.org/indexnow
Content-Type: application/json
{"host":"solarcomplaints.co","key":"a9dc40ec318d70ab0cee3b6b492b24ce76502dccd7b1b5e3e6e1abe8d1e97a5c","keyLocation":"https://solarcomplaints.co/a9dc40ec318d70ab0cee3b6b492b24ce76502dccd7b1b5e3e6e1abe8d1e97a5c.txt","urlList":["https://solarcomplaints.co/blog/{slug}"]}
```
Returns 202 on success.

**Google Indexing API:** Requires service account JSON not available in the Claude chat environment. Manus has `python3 /home/ubuntu/run_bulk_index.py` or the Tuesday cron handles it.

---

## 4. Topic Selection Strategy

### Priority 1: Breaking news with high search demand

Monitor these categories weekly:
- **State AG actions** against solar companies (Texas, NY, CT, CA, CO, MN especially)
- **Solar company bankruptcies** (Chapter 11 filings, liquidations)
- **Major lawsuits** (class actions, state enforcement, private litigation)
- **Regulatory changes** (NEM policy updates, tax credit changes, licensing actions)

When these happen, publish within 48 hours to catch the search spike. Examples published so far:
- Texas AG Paxton CIDs to Sunrun/Freedom Forever/Lone Star/CAM Solar (April 6, 2026)
- Freedom Forever Chapter 11 bankruptcy (April 15, 2026)
- CT AG William Tong investigation of SunStrong (March 26, 2026)
- NY AG Letitia James $275M lawsuit vs. Attyx/SUNco/Mosaic/WebBank (March 17, 2026)

### Priority 2: High-intent homeowner pain points

Query patterns with high commercial intent:
- "how to cancel [company] contract" / "how to cancel [company] contract after installation"
- "[company] lawsuit" / "[company] complaints [state]"
- "is [company] lease predatory" / "is [company] PPA a ripoff"
- "solar salesman lied to me" / "solar salesman promised [x]"
- "[company] warranty not honored"
- "[lender] solar loan complaints" / "cancel [lender] loan"
- "solar contract forged signature"
- "solar company went out of business what happens"
- "solar panels stopped working [state]"

### Priority 3: Legal education content (evergreen)

Covers the underlying legal theories that support individual cases:
- FTC Holder Rule explained
- State Deceptive Trade Practices Acts
- TILA rescission rights
- Cooling-off period rules (federal + state)
- Successor liability in solar bankruptcies
- Statute of limitations + the "discovery rule"

### Priority 4: Geographic/company matrix

Combinations of (state × company) and (city × company) for long-tail SEO:
- "sunrun complaints [state]" — already have 15+ of these
- "freedom forever complaints [state]" — partial coverage
- "cancel solar contract [state]"
- "[city] solar complaints"

### What NOT to publish:
- Generic "benefits of solar" content (wrong audience)
- Pro-solar-industry content (off-brand)
- Content about solar-adjacent topics (batteries, EVs, etc) unless they tie to a homeowner contract issue
- Thin content under 1,500 words

---

## 5. Article Template (The 10/10 Framework)

Every article should follow this structure. A reusable Python helper library exists at `/home/claude/articles/framework_v2.py` from the previous session — Claude Code can rebuild this or import it.

### Article structure (in order):

1. **JSON-LD Schema blocks** — `NewsArticle` for news pieces, `HowTo` for action-step guides. Both can coexist. Embedded at top of `content` HTML before any text.

2. **Opening — VARIED STRUCTURE** (do not use the same pattern twice in a row):
   - **Story-led:** "Frances Holt opened her door in Houston in 2023..."
   - **Stat-shock:** "$500 million in debt. 50,000 to 100,000 creditors."
   - **Math-shock:** "A $150/month Sunrun lease, signed today, will cost you roughly $65,000 over 25 years."
   - **Direct question:** "Did a solar salesperson promise your electric bill would be zero — and now it isn't?"
   - **Scene-based:** "The letter arrives in a plain envelope. You almost miss it."

3. **3-paragraph intro** ending with the "stick with me" hook teasing the outcomes section toward the bottom.

4. **E-E-A-T byline block** — "Reviewed by the SolarComplaints.co editorial team" with a credibility line (e.g., "100+ cases reviewed across 25 states").

5. **Main content in H2/H3 sections** — 1,500-2,500 words total. Real dates, real dollar amounts, real company names. Interlinks to already-indexed articles throughout (not just at the bottom).

6. **At least one Case Study card** before the mid-CTA, and ideally a second one after the mid-CTA. Anonymized but concrete: "Marcus R., Plano, TX — signed a Sunrun contract in 2022 for a $72,000 loan..." Include dollar amounts, timeline, and what happened to the case.

7. **5-Minute Evidence Checklist (blue box)** — 5 specific actions the reader can take in the next 5 minutes to build their case. This is a conversion driver. It makes the abstract concrete.

8. **Mid-article CTA card (amber)** — Headline: "⚡ Don't Read Any Further Without Knowing This" → Two outcomes → 40% refund guarantee → "See If You Qualify → (60 seconds)" button with UTM tracking `?src={src}&pos=mid`.

9. **Main content continues** — typically the "what to do right now" action section, legal theory, or deeper case analysis.

10. **Outcomes section** — Always the same three subsections: Outcome #1 (canceled + keep system), Outcome #2 (40-60% reduction), and the 40% refund guarantee. Do not vary this language across articles.

11. **Bottom Line paragraph** — Summary, 90-day window urgency, call to action.

12. **Closing CTA card (dark)** — "Sixty seconds. That's all this takes." + "exit specialist" language + button with UTM tracking `?src={src}&pos=close`.

13. **Related Reading list** — 8-10 internal links to already-indexed articles. Mix of news, how-to, and state/company pages.

### Reusable component snippets (Python):

```python
# Amber mid-article CTA card
def mid_cta(src, custom_headline=None):
    headline = custom_headline or "Most homeowners we review end up in one of two outcomes:"
    return f"""
<div style="background:linear-gradient(135deg,#fff4e6 0%,#ffe4cc 100%);border:2px solid #f59e0b;border-radius:12px;padding:24px;margin:32px 0;">
<p style="margin:0 0 12px 0;font-size:14px;font-weight:700;color:#92400e;text-transform:uppercase;letter-spacing:0.05em;">⚡ Don't Read Any Further Without Knowing This</p>
<p style="margin:0 0 16px 0;font-size:18px;font-weight:700;color:#1a1a1a;line-height:1.4;">{headline}</p>
<p style="margin:0 0 8px 0;font-size:16px;color:#1a1a1a;"><strong>1.</strong> Contract completely canceled. You keep the system. That $30K, $80K, $150K loan? Gone.</p>
<p style="margin:0 0 16px 0;font-size:16px;color:#1a1a1a;"><strong>2.</strong> Loan slashed 40–60%. $150K down to $75K. $70K down to $35K. Real numbers.</p>
<p style="margin:0 0 16px 0;font-size:15px;color:#4a4a4a;font-style:italic;">If we take your case and can't deliver either outcome after exhausting every angle — you get 40% of your fee back. In writing.</p>
<p style="margin:0;"><a href="/file-a-complaint?src={src}&amp;pos=mid" style="display:inline-block;background:#dc2626;color:#fff;padding:14px 28px;border-radius:8px;font-size:17px;font-weight:700;text-decoration:none;">See If You Qualify → (60 seconds)</a></p>
</div>
"""

# Dark closing CTA card
def closing_cta(src):
    return f"""
<div style="background:linear-gradient(135deg,#1a1a1a 0%,#2d2d2d 100%);color:#fff;border-radius:12px;padding:32px;margin:32px 0;">
<p style="margin:0 0 16px 0;font-size:13px;font-weight:700;color:#fbbf24;text-transform:uppercase;letter-spacing:0.1em;">Your Next Move</p>
<h3 style="margin:0 0 16px 0;font-size:26px;font-weight:800;line-height:1.2;color:#fff;">Sixty seconds. That's all this takes.</h3>
<p style="margin:0 0 12px 0;font-size:16px;line-height:1.6;color:#e5e5e5;">No phone tree. No "someone will get back to you in 3–5 business days." You fill out the form and one of our <strong style="color:#fff;">exit specialists</strong> reaches out directly to walk you through whether we can help and what outcome is realistic for your specific case.</p>
<p style="margin:0 0 24px 0;font-size:16px;line-height:1.6;color:#e5e5e5;">Worst case: you find out you don't have a case and you got peace of mind. Best case: in a year, you're sitting on a free system and a loan that no longer exists.</p>
<p style="margin:0;"><a href="/file-a-complaint?src={src}&amp;pos=close" style="display:inline-block;background:#dc2626;color:#fff;padding:16px 32px;border-radius:8px;font-size:18px;font-weight:700;text-decoration:none;">Start Your Free Case Review →</a></p>
</div>
"""

# Yellow case study card
def case_study(name, city, state, year, company, loan_amount, outcome, timeline):
    return f"""
<div style="background:#fefce8;border:1px solid #eab308;border-radius:10px;padding:20px 24px;margin:28px 0;">
<p style="margin:0 0 8px 0;font-size:12px;font-weight:700;color:#854d0e;text-transform:uppercase;letter-spacing:0.08em;">⚡ Case File</p>
<p style="margin:0 0 10px 0;font-size:15px;line-height:1.6;color:#1a1a1a;"><strong>{name}, {city}, {state}</strong> — signed a {company} contract in {year} for a ${loan_amount:,} {'loan' if loan_amount > 20000 else 'lease'}. {outcome}</p>
<p style="margin:0;font-size:13px;color:#666;font-style:italic;">Timeline: {timeline}. Case details anonymized; dollar amounts and patterns reflect actual reviewed files.</p>
</div>
"""

# Blue evidence checklist
def evidence_checklist(items):
    items_html = "\n".join([f'<li style="margin:0 0 10px 0;padding-left:8px;">{item}</li>' for item in items])
    return f"""
<div style="background:#eff6ff;border:2px solid #3b82f6;border-radius:10px;padding:22px 26px;margin:28px 0;">
<p style="margin:0 0 4px 0;font-size:12px;font-weight:700;color:#1e40af;text-transform:uppercase;letter-spacing:0.08em;">📋 5-Minute Evidence Checklist</p>
<p style="margin:0 0 14px 0;font-size:17px;font-weight:700;color:#1a1a1a;">Do these in the next 5 minutes — before you do anything else:</p>
<ul style="margin:0;padding-left:22px;font-size:15px;line-height:1.6;color:#1a1a1a;">
{items_html}
</ul>
</div>
"""

# E-E-A-T byline
def byline(author_note="Reviewed by the SolarComplaints.co editorial team"):
    return f"""
<div style="display:flex;align-items:center;gap:12px;padding:14px 18px;background:#f8f7f4;border-left:4px solid #dc2626;border-radius:6px;margin:20px 0 28px 0;font-size:14px;color:#4a4a4a;">
<div style="flex:1;">
<p style="margin:0 0 4px 0;font-weight:600;color:#1a1a1a;">{author_note}</p>
<p style="margin:0;font-size:13px;">Based on 100+ homeowner cases reviewed. Updated with the latest state AG actions and federal enforcement developments.</p>
</div>
</div>
"""
```

### Standard outcomes section (use verbatim):

```html
<h2>Here Is What Actually Happens When We Take Your Case</h2>

<p>We are not a referral mill. We review every case before we take it. If you meet the criteria — and most homeowners reading an article like this one do — here is what typically happens:</p>

<h3>Outcome #1: Your contract gets completely canceled. You keep the system.</h3>

<p>Read that again. That $30,000 loan, that $80,000 loan, that $150,000 loan — <strong>gone.</strong> Wiped. And the equipment on your roof? <strong>You keep it.</strong> It is yours. Hire a local electrician or solar tech to clean it up and tie it in properly, and you have got a functioning solar system for the cost of a service call.</p>

<p>Not a typo. That is the best-case outcome, and it is what we push for on every case we accept.</p>

<h3>Outcome #2: Your loan gets massively reduced. Typically 40% to 60%.</h3>

<p>Every case is different, but the pattern is consistent:</p>

<ul>
<li>A $150,000 loan knocked down to around $75,000</li>
<li>A $70,000 loan cut to $35,000</li>
<li>A $175,000 loan restructured to something you can actually live with</li>
</ul>

<p>If we cannot completely kill the contract, we fight like hell to get the principal slashed — and we have a track record of doing it.</p>

<h3>If we take your case and cannot deliver either outcome?</h3>

<p>You get 40% of your fee back after we have exhausted every angle. That is our guarantee, in writing. Nobody else in this space puts that on paper. We do — because we only take cases we believe in.</p>
```

---

## 6. SEO & AEO Rules

- **Target keyword density:** Natural language. Put the primary keyword in the H1, early in paragraph 1, and in at least one H2. Do not keyword-stuff.
- **Internal linking:** Every article needs 8-10 contextual internal links. Mix of: (1) related company/state pages already indexed, (2) related legal theory articles, (3) related news pieces. Do not link every article to every other article — be contextually relevant.
- **External linking:** Minimal. Only to state AG offices, court records, or regulatory bodies when directly relevant. Do not link to competitors or law firms.
- **Schema markup:** Every article should have at least `NewsArticle` schema. News/bankruptcy/AG articles should add `HowTo` schema. FAQ schema is automatically generated from the `faqJson` field by the site.
- **Meta title:** Under 60 characters. Lead with keyword. Include "2026" for freshness signal.
- **Meta description:** Under 160 characters. Answer the query. Include a call to action.
- **Images:** Every article must have `image1` populated. External CDN URLs work (Unsplash, Pexels, Supabase storage). Chase is generating custom Gemini images that replace placeholders.
- **Related reading list:** 8-10 links at the bottom. These create the internal link graph that boosts page authority across the site.

### Keyword research approach:

1. Check Google Search Console for current impressions and CTR data (Chase or Manus has access)
2. Look for queries with high impressions + low CTR — those are ranking opportunities
3. Cross-reference with breaking news and AG actions
4. Validate with a Google search: if the top 10 results are generic, there is opportunity
5. Always include the year (2026) in at least the title and one H2 for freshness

---

## 7. Research Process for News Articles

1. **Web search for the original sources** — state AG press releases, court filings on Justia or PACER, primary news reporting (NYT, CBS, Bloomberg, pv-magazine, Law360, Reuters)
2. **Extract the primary facts:** dates, case numbers, dollar amounts, named parties, specific allegations
3. **Cross-reference at least 3 sources** to verify facts before publishing
4. **Quote sparingly** — use one direct quote per source maximum, and keep it under 15 words (copyright compliance). Paraphrase the rest.
5. **Never fabricate facts.** If the search result says "between $500M and $1B in debt," write that exactly — not "$750M."
6. **Always include:** filing date, case number or lawsuit number, jurisdiction, named parties, specific legal claims, dollar amounts at issue.

---

## 8. Lead Tracking (UTM Structure)

Every CTA in every article uses UTM tracking so Chase can see which article and which CTA position converts:

- Mid-article CTA: `/file-a-complaint?src={slug-short}&pos=mid`
- Closing CTA: `/file-a-complaint?src={slug-short}&pos=close`

The `src` parameter is a short slug identifier (examples):
- `texas-ag-2026`, `freedom-forever-bk-2026`, `sunrun-lease-predatory`, `zero-electric-bill-lie`, `sunstrong-warranty-ct-ag`, `ny-ag-attyx-275m`, `cancel-sunrun-after-install`, `goodleap-complaints-2026`, `forged-signature-2026`, `sunrun-buyout-calculator`

When creating a new article, pick a short unique `src` identifier and use it consistently in both CTAs.

---

## 9. Current Article Inventory (129 posts as of April 19, 2026)

Pulled via `GET /api/admin/blog?limit=200&published=true`. Categories:

- **News (7):** texas-ag-sunrun-solar-investigation-2026, freedom-forever-bankruptcy-2026, sunstrong-warranty-not-honored-sunnova-sunpower-2026, ny-ag-attyx-sunco-275-million-lawsuit-2026, sunpower-bankruptcy-what-homeowners-need-to-know, adt-solar-sunpro-abandoned-customers, solar-company-out-of-business-now-what
- **Company (62):** sunrun-complaints-[state] x 15+, freedom-forever-complaints-[state] x 8+, sunnova-complaints-[state] x 3, goodleap-complaints-[state] x 3, city-solar-complaints x 10, cancel-[company]-contract x 4, is-sunrun-solar-lease-predatory, sunrun-ppa-lease-buyout-calculator-2026
- **Legal (15):** solar-contract-forged-signature-what-to-do-2026, goodleap-solar-loan-complaints-2026, cancel-mosaic-solar-loan, cancel-goodleap-loan, cancel-dividend-finance-solar-loan, mosaic-solar-loan-complaints, solar-loan-balloon-payment-trap, solar-misrepresentation-lawsuit-guide, solar-contract-escalator-clause-explained, solar-monitoring-not-working, goodleap-dealer-fees-explained, solar-contract-rescission-guide, sunnova-bankruptcy-what-happens, solar-loan-problems, solar-lien-on-my-house
- **Emotional (8):** signed-solar-contract-without-reading-it, trapped-in-solar-lease-selling-house, solar-savings-were-a-lie, solar-damaged-my-roof-what-to-do, solar-company-stopped-responding, solar-panels-stopped-working-now-what, solar-door-to-door-scam-what-to-do, solar-savings-not-as-promised, paying-two-bills-solar-electric, solar-salesman-lied-to-me, solar-company-ruined-my-roof, solar-salesman-promised-zero-electric-bill
- **Foundation (7):** solar-salesman-tricks-to-watch-for, solar-company-went-out-of-business, solar-cooling-off-period-missed, how-to-get-out-of-solar-contract-legally, buyer-wont-assume-solar-lease, solar-panels-not-working-what-to-do, selling-house-with-solar-panels, solar-contract-red-flags, how-to-cancel-solar-contract, how-to-cancel-sunrun-contract-after-installation
- **State (5):** cancel-solar-contract-[state] x 4, texas/california/nj/il/ga/florida-solar-consumer-rights/laws-2026 (6 AEO pages)
- **AEO (6):** state-level consumer rights pages
- **City-company (1+):** orlando-solar-complaints etc

Check the current list before writing anything new: `curl -s "https://solarcomplaints.co/api/admin/blog?limit=200&published=true" -H "X-Admin-Key: sc_admin_Q55em5eWnehqzM2cuEjFmc5x9q_ZjLQ2yn1iUnMyVqk"` — avoid duplicating topics.

---

## 10. Next Recommended Topics (Priority Queue)

If Claude Code is picking up, these are the highest-value next targets (ordered):

1. **Momentum Solar complaints 2026** — operational chaos in late 2025, similar trajectory to Freedom Forever. High demand.
2. **Sunrun complaints [remaining states]** — fill in the grid for states not yet covered (Oregon, Washington, Colorado, Virginia, North Carolina).
3. **FTC Holder Rule explained for solar homeowners** — foundational legal education. Drives traffic to every loan cancellation page.
4. **Solar loan default consequences** — homeowners Googling this are in crisis mode. High-intent.
5. **Which solar companies are going bankrupt in 2026** — news-style landing page, updated weekly.
6. **How long does a solar contract cancellation take** — practical timeline question. Low CPC, high intent.
7. **NY AG Attyx lawsuit what it means for you** — follow-up to the main Attyx article, broader "if you have any solar contract, here's why this matters."
8. **Solar loan refinancing after installer bankruptcy** — specific Mosaic/GoodLeap refinance question given Freedom Forever BK.
9. **Cancel Freedom Forever contract 2026** — the bankruptcy creates specific cancellation opportunities this article should capture.
10. **Sunrun lease vs own solar comparison** — targets "is Sunrun lease worth it" queries.

Monitor continuously for new AG actions, bankruptcy filings, and class action lawsuits. Publish within 48 hours of the news breaking to catch the search spike.

---

## 11. Things That Must Be True in Every Article

- [ ] Intro hook varies from the last article published (story / stat / math / question / scene)
- [ ] "Stick with me" hook in the intro tells the reader what they get toward the bottom
- [ ] Byline block appears after the intro
- [ ] At least 1 case study card (ideally 2) with specific names/cities/dollar amounts/timelines
- [ ] 1 evidence checklist block (blue, 5 items)
- [ ] 1 mid-article CTA card (amber) with UTM tracking `pos=mid`
- [ ] Standard 3-outcome section appears (Outcome #1 / Outcome #2 / 40% refund guarantee)
- [ ] 1 closing CTA card (dark) with UTM tracking `pos=close`
- [ ] 8-10 related reading links at the bottom
- [ ] At least 1 `NewsArticle` JSON-LD schema block at the top
- [ ] `directAnswer` field populated (2-4 sentences, AEO-ready)
- [ ] `faqJson` field populated (5 Q&As)
- [ ] `metaTitle` under 60 chars
- [ ] `metaDescription` under 160 chars
- [ ] `readTime` populated (integer, minutes)
- [ ] `publishDate` populated in `YYYY-MM-DD` format (NOT full ISO)
- [ ] `image1` populated with an absolute URL — **and verified to return HTTP 200 before publish** (Unsplash occasionally removes photo IDs). Test with: `curl -sI "{url}" | head -1`
- [ ] `category` set to one of: news, company, legal, emotional, foundation, state, aeo, city-company
- [ ] Article submitted to Bing IndexNow after publish
- [ ] Response confirms `seoWarnings: []` (fix anything listed)

---

## 12. Failure Modes to Avoid

1. **Publishing without Bing IndexNow submission** — this delays indexing by weeks.
2. **Using full ISO dates in `publishDate`** — breaks the SQL query silently. Always use `YYYY-MM-DD`.
3. **Letting `metaDescription` exceed 160 chars** — triggers SEO warning. Fix immediately via PUT.
4. **Fabricating case numbers or dollar amounts** — damages trust and could trigger legal liability. Always cite verified sources.
5. **Linking to non-existent pages** — check the 129-post inventory before adding an internal link. Or use `/file-a-complaint` as the safe default.
6. **Writing in the same opening pattern twice in a row** — makes the whole site feel templated. Rotate: story / stat / math / question / scene.
7. **Getting too lawyerly** — if the reader has to re-read a paragraph, rewrite it. Direct, short, real.
8. **Missing the `upsert: true` flag** when updating — if you're not sure whether the post exists, set `upsert: true` in the payload.

---

## 13. Contact and Escalation

**Chase Wyatt** — owner, Infinite AI / Gosunlite LLC — reachable via the Claude chat interface. He makes the calls on voice changes, new topic priorities, and major business pivots.

**Manus** — secondary agent with direct sandbox access (`python3 /home/ubuntu/run_bulk_index.py` for Google Indexing, image swap workflows). Handoff via shared API key.

**When in doubt:** Default to the voice and template rules above. Publishing nothing is worse than publishing a 9/10 article — volume + consistency compounds on this site. But never publish below the checklist bar in Section 11.

---

## 14. Acknowledgment

Welcome to the team. This site is how Chase and his team give homeowners a fighting chance against an industry that has hurt a lot of people. Every article you publish that helps someone understand their options, file the right complaint, or get a case review is potentially tens of thousands of dollars back in a family's pocket — and in many cases, a faith-restoring experience that someone finally told them the truth.

Work with care. Write like it matters. Publish like their family depends on it — because for thousands of homeowners right now, it does.
