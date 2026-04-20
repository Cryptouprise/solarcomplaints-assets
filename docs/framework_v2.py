"""v2 framework - 10/10 article components for SolarComplaints.co"""

def byline(author_note="Reviewed by the SolarComplaints.co editorial team"):
    """E-E-A-T byline at top of every article. Critical for Google's helpful content updates on legal topics."""
    return f"""
<div style="display:flex;align-items:center;gap:12px;padding:14px 18px;background:#f8f7f4;border-left:4px solid #dc2626;border-radius:6px;margin:20px 0 28px 0;font-size:14px;color:#4a4a4a;">
<div style="flex:1;">
<p style="margin:0 0 4px 0;font-weight:600;color:#1a1a1a;">{author_note}</p>
<p style="margin:0;font-size:13px;">Based on 100+ homeowner cases reviewed. Updated with the latest state AG actions and federal enforcement developments.</p>
</div>
</div>
"""

def case_study(name, city, state, year, company, loan_amount, outcome, timeline):
    """Anonymized case study card. Use 1-2 per article. Makes content human and builds credibility."""
    return f"""
<div style="background:#fefce8;border:1px solid #eab308;border-radius:10px;padding:20px 24px;margin:28px 0;">
<p style="margin:0 0 8px 0;font-size:12px;font-weight:700;color:#854d0e;text-transform:uppercase;letter-spacing:0.08em;">⚡ Case File</p>
<p style="margin:0 0 10px 0;font-size:15px;line-height:1.6;color:#1a1a1a;"><strong>{name}, {city}, {state}</strong> — signed a {company} contract in {year} for a ${loan_amount:,} {'loan' if loan_amount > 20000 else 'lease'}. {outcome}</p>
<p style="margin:0;font-size:13px;color:#666;font-style:italic;">Timeline: {timeline}. Case details anonymized; dollar amounts and patterns reflect actual reviewed files.</p>
</div>
"""

def evidence_checklist(items):
    """5-minute evidence checklist block. Converts lurkers by giving them a concrete next step."""
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

def mid_cta(src, custom_headline=None):
    """Mid-article amber CTA. Optional custom headline for article-specific framing."""
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

def outcomes_section():
    """Standard outcomes section — anchor content for the CTA narrative."""
    return """
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
"""

def newsarticle_schema(headline, description, publish_date, slug, keywords):
    """JSON-LD NewsArticle schema for news-angle articles. Boosts AEO and featured snippets."""
    import json
    schema = {
        "@context": "https://schema.org",
        "@type": "NewsArticle",
        "headline": headline,
        "description": description,
        "datePublished": publish_date,
        "dateModified": publish_date,
        "author": {
            "@type": "Organization",
            "name": "SolarComplaints.co Editorial Team",
            "url": "https://solarcomplaints.co"
        },
        "publisher": {
            "@type": "Organization",
            "name": "SolarComplaints.co",
            "logo": {
                "@type": "ImageObject",
                "url": "https://solarcomplaints.co/logo.png"
            }
        },
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": f"https://solarcomplaints.co/blog/{slug}"
        },
        "keywords": keywords
    }
    return f'<script type="application/ld+json">{json.dumps(schema)}</script>\n'

def howto_schema(name, description, steps):
    """JSON-LD HowTo schema for action-step articles. Wins the featured snippet."""
    import json
    step_items = [{"@type": "HowToStep", "position": i+1, "name": s["name"], "text": s["text"]} for i, s in enumerate(steps)]
    schema = {
        "@context": "https://schema.org",
        "@type": "HowTo",
        "name": name,
        "description": description,
        "step": step_items
    }
    return f'<script type="application/ld+json">{json.dumps(schema)}</script>\n'


ADMIN_KEY = "sc_admin_Q55em5eWnehqzM2cuEjFmc5x9q_ZjLQ2yn1iUnMyVqk"
API_POST = "https://solarcomplaints.co/api/admin/blog"

def publish(payload, is_update=False, slug=None):
    import json, subprocess
    if is_update and slug:
        url = f"{API_POST}/{slug}"
        method = "PUT"
    else:
        url = API_POST
        method = "POST"
    result = subprocess.run([
        "curl", "-s", "-X", method, url,
        "-H", f"X-Admin-Key: {ADMIN_KEY}",
        "-H", "Content-Type: application/json",
        "-d", json.dumps(payload)
    ], capture_output=True, text=True)
    return result.stdout

def submit_bing(slug):
    import subprocess
    result = subprocess.run([
        "curl", "-s", "-o", "/dev/null", "-w", "%{http_code}",
        "-X", "POST", "https://api.indexnow.org/indexnow",
        "-H", "Content-Type: application/json; charset=utf-8",
        "-d", f'{{"host":"solarcomplaints.co","key":"a9dc40ec318d70ab0cee3b6b492b24ce76502dccd7b1b5e3e6e1abe8d1e97a5c","keyLocation":"https://solarcomplaints.co/a9dc40ec318d70ab0cee3b6b492b24ce76502dccd7b1b5e3e6e1abe8d1e97a5c.txt","urlList":["https://solarcomplaints.co/blog/{slug}"]}}'
    ], capture_output=True, text=True)
    return result.stdout
