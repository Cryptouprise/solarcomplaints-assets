#!/usr/bin/env python3
"""Validate SEO requirements for article backups."""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTICLES = ROOT / "articles"
HEROES = ROOT / "heroes"
REQUIRED_FIELDS = (
    "slug",
    "title",
    "published",
    "read_time",
    "category",
    "live_url",
    "hero_image",
    "meta_title",
    "meta_description",
)


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    closing = text.find("\n---\n", 4)
    if closing == -1:
        return {}

    fields = {}
    for line in text[4:closing].splitlines():
        if ": " in line:
            key, value = line.split(": ", 1)
            fields[key] = value.strip()
    return fields


def audit_article(path: Path) -> tuple[list[str], dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    fields = parse_frontmatter(text)
    errors = []

    for field in REQUIRED_FIELDS:
        if not fields.get(field):
            errors.append(f"missing frontmatter field '{field}'")

    slug = fields.get("slug", "")
    expected_slug = path.stem
    if slug and slug != expected_slug:
        errors.append(f"slug '{slug}' does not match filename '{expected_slug}'")

    expected_url = f"https://solarcomplaints.co/blog/{slug}"
    if slug and fields.get("live_url") != expected_url:
        errors.append(f"live_url must be '{expected_url}'")

    expected_image = (
        "https://cdn.jsdelivr.net/gh/Cryptouprise/"
        f"solarcomplaints-assets@main/heroes/{slug}.jpg"
    )
    if slug and fields.get("hero_image") != expected_image:
        errors.append("hero_image does not match the canonical CDN URL")
    if slug and not (HEROES / f"{slug}.jpg").is_file():
        errors.append(f"missing local hero image 'heroes/{slug}.jpg'")

    meta_title = fields.get("meta_title", "")
    if len(meta_title) > 60:
        errors.append(f"meta_title is {len(meta_title)} characters (maximum 60)")
    meta_description = fields.get("meta_description", "")
    if len(meta_description) > 160:
        errors.append(
            f"meta_description is {len(meta_description)} characters (maximum 160)"
        )

    h1_count = len(re.findall(r"^# ", text, flags=re.MULTILINE))
    if h1_count != 1:
        errors.append(f"expected exactly one H1, found {h1_count}")
    if not re.search(r"\*\*Direct answer(?: \(AEO-ready\))?:\*\*", text):
        errors.append("missing direct answer")
    if "**Keywords:**" not in text:
        errors.append("missing keyword list")

    internal_links = re.findall(r'href=["\'](/[^"\']+)', text)
    if len(internal_links) < 3:
        errors.append(f"expected at least 3 internal links, found {len(internal_links)}")
    if not any("pos=mid" in link for link in internal_links):
        errors.append("missing mid-article CTA tracking link")
    if not any("pos=close" in link for link in internal_links):
        errors.append("missing closing CTA tracking link")

    schemas = re.findall(
        r'<script type="application/ld\+json">(.*?)</script>', text, flags=re.DOTALL
    )
    if not schemas:
        errors.append("missing JSON-LD schema")
    for index, raw_schema in enumerate(schemas, start=1):
        try:
            schema = json.loads(raw_schema)
        except json.JSONDecodeError as exc:
            errors.append(f"JSON-LD block {index} is invalid: {exc.msg}")
            continue
        if schema.get("@context") != "https://schema.org":
            errors.append(f"JSON-LD block {index} has an invalid @context")

    return errors, fields


def main() -> int:
    failures = 0
    article_count = 0
    duplicates: dict[str, dict[str, list[str]]] = {
        "meta_title": defaultdict(list),
        "meta_description": defaultdict(list),
    }

    for path in sorted(ARTICLES.glob("*.md")):
        if path.name == "INDEX.md":
            continue
        article_count += 1
        errors, fields = audit_article(path)
        for field, values in duplicates.items():
            value = fields.get(field)
            if value:
                values[value].append(path.name)
        if errors:
            failures += len(errors)
            for error in errors:
                print(f"ERROR {path.relative_to(ROOT)}: {error}")

    for field, values in duplicates.items():
        for value, filenames in values.items():
            if len(filenames) > 1:
                failures += 1
                print(f"ERROR duplicate {field} in {', '.join(filenames)}: {value}")

    if failures:
        print(f"\nSEO audit failed: {failures} issue(s) across {article_count} articles.")
        return 1

    print(f"SEO audit passed: {article_count} articles validated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
