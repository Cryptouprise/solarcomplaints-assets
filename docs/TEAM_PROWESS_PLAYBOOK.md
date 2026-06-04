# Team Prowess Playbook

This playbook turns "improve our prowess" into a measurable operating system for delivery, quality, reliability, security, and growth.

## 1) Prowess Definition + Measurable Targets

Track these five targets monthly:

1. **Delivery speed:** Median cycle time (issue start → merged) under **5 days**.
2. **Quality:** Escaped defect rate under **2 defects per release**.
3. **Reliability:** Publishing workflow success rate at or above **98%**.
4. **Security:** High/critical dependency and code scanning alerts remediated within **7 days**.
5. **Growth:** At least **2 content experiments per month** with outcome tracking (traffic, engagement, or conversion lift).

## 2) Execution Basics

- Keep one visible weekly priority list with owners and due dates.
- Break work into small, independently shippable tasks.
- Enforce consistent reviews with a shared checklist:
  - scope matches ticket
  - facts/citations verified
  - assets and indexes updated
  - rollback path is clear
- Run a **weekly retro** with exactly three outputs:
  - one thing to keep
  - one thing to improve
  - one named owner + deadline for follow-up

## 3) Engineering Quality System

- Maintain stronger coverage on critical paths:
  - article publishing flow
  - asset references (hero/video links)
  - index integrity for `/articles/INDEX.md`
- Require automated checks in CI for:
  - markdown/link integrity
  - schema/format validation where applicable
  - security scans for dependencies and code alerts
- Perform a dependency/security hygiene pass every two weeks and document completed remediations.

## 4) Product Feedback Loop

- Collect customer signals from comments, support notes, and search query patterns every week.
- Triages happen on a fixed cadence with labels: `urgent`, `high-impact`, `backlog`.
- Ship in short cycles and capture outcomes per release:
  - what changed
  - expected outcome
  - actual outcome after 7 and 30 days

## 5) Team Capability Building

- Run monthly skill-gap review and pick top 1–2 skill areas to close.
- Schedule pair sessions for hard legal/content/automation tasks.
- Maintain shared playbooks for recurring tasks (research, drafting, publishing, QA).
- Rotate ownership of tricky areas to reduce single points of failure.

## 6) Monthly Review Cadence

At month-end:

1. Review target metrics and trend lines.
2. Keep practices that produced measurable gains.
3. Remove low-impact steps that add overhead.
4. Re-baseline next month targets based on outcomes.

## Suggested Owners

- **Lead/Owner:** sets targets and resolves blockers.
- **Ops/Editor:** enforces intake, triage, and release cadence.
- **Quality/Security owner:** tracks scans, defects, and remediation SLAs.
- **Analyst:** reports growth experiment outcomes.
