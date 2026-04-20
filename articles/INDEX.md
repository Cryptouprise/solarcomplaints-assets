# Article Index

All currently-prioritized SolarComplaints.co articles, with live URLs and backups.

## 🔥 The Flagship 10 (April 2026 Batch)

| # | Title | Category | Live URL | Backup |
|---|-------|----------|----------|--------|
| 1 | Texas AG Paxton Investigates Sunrun and Freedom Forever for Solar Fraud | `news` | [View live](https://solarcomplaints.co/blog/texas-ag-sunrun-solar-investigation-2026) | [Backup](./texas-ag-sunrun-solar-investigation-2026.md) |
| 2 | Freedom Forever Files Chapter 11 Bankruptcy | `news` | [View live](https://solarcomplaints.co/blog/freedom-forever-bankruptcy-2026) | [Backup](./freedom-forever-bankruptcy-2026.md) |
| 3 | Is the Sunrun Solar Lease Predatory? | `company` | [View live](https://solarcomplaints.co/blog/is-sunrun-solar-lease-predatory) | [Backup](./is-sunrun-solar-lease-predatory.md) |
| 4 | Solar Salesman Promised a Zero Electric Bill — Now What? | `emotional` | [View live](https://solarcomplaints.co/blog/solar-salesman-promised-zero-electric-bill) | [Backup](./solar-salesman-promised-zero-electric-bill.md) |
| 5 | SunStrong Won't Honor Sunnova & SunPower Warranties — CT AG Investigates | `news` | [View live](https://solarcomplaints.co/blog/sunstrong-warranty-not-honored-sunnova-sunpower-2026) | [Backup](./sunstrong-warranty-not-honored-sunnova-sunpower-2026.md) |
| 6 | NY AG Sues Attyx (SUNco) for $275 Million | `news` | [View live](https://solarcomplaints.co/blog/ny-ag-attyx-sunco-275-million-lawsuit-2026) | [Backup](./ny-ag-attyx-sunco-275-million-lawsuit-2026.md) |
| 7 | How to Cancel a Sunrun Contract After Installation | `foundation` | [View live](https://solarcomplaints.co/blog/how-to-cancel-sunrun-contract-after-installation) | [Backup](./how-to-cancel-sunrun-contract-after-installation.md) |
| 8 | GoodLeap Solar Loan Complaints — The Complete 2026 Guide | `legal` | [View live](https://solarcomplaints.co/blog/goodleap-solar-loan-complaints-2026) | [Backup](./goodleap-solar-loan-complaints-2026.md) |
| 9 | Solar Contract Forged Signature — What to Do in 2026 | `legal` | [View live](https://solarcomplaints.co/blog/solar-contract-forged-signature-what-to-do-2026) | [Backup](./solar-contract-forged-signature-what-to-do-2026.md) |
| 10 | Sunrun PPA & Lease Buyout Calculator — How the Formula Actually Works | `company` | [View live](https://solarcomplaints.co/blog/sunrun-ppa-lease-buyout-calculator-2026) | [Backup](./sunrun-ppa-lease-buyout-calculator-2026.md) |


## 📊 Site Stats

- **Total published posts:** 129
- **SEO warnings:** 0
- **Images missing:** 0
- **Live admin stats:** `GET https://solarcomplaints.co/api/admin/stats`

## 🎨 Visual Standard

Every article uses the **documentary-realism + cinematic lighting** visual style. Hero images are stored at `heroes/{slug}.jpg` in this repo and served via jsDelivr CDN:

```
https://cdn.jsdelivr.net/gh/Cryptouprise/solarcomplaints-assets@main/heroes/{slug}.jpg
```

## 📝 Adding a New Article

1. Generate + publish via the admin API (see `/docs/HANDOFF_FRAMEWORK.md`)
2. Generate hero image via fal.ai Flux Pro (same style)
3. Upload hero to `/heroes/{slug}.jpg` in this repo
4. Set `image1` in the admin API to the CDN URL above
5. Pull a markdown backup to `/articles/{slug}.md`
6. Update this index

## 🤖 For AI Agents

See [`../docs/HANDOFF_FRAMEWORK.md`](../docs/HANDOFF_FRAMEWORK.md) for the master playbook covering voice, API, SEO, topic selection, and the 10/10 article template.
