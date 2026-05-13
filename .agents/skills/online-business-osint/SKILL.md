---
name: online-business-osint
description: Investigate online business opportunities through public OSINT signals. Use to find repeated complaints, bad reviews, abandoned tools, marketplace demand, API opportunities, compliance burdens, and manual B2B workflows suitable for automation.
license: Apache-2.0
metadata:
  author: Diego Cofré
  project: coferlandia-powers
  version: "0.1.0"
---

# Online Business OSINT

## Purpose
Find online business opportunities from public signals that indicate pain, budget, and automation potential.

## When to use this skill
Use when the user wants practical opportunity discovery through complaints, reviews, forums, marketplaces, GitHub issues, product changes, API announcements, or regulatory shifts.

## Inputs expected
- Vertical, platform, persona, or problem space.
- Preferred product types and exclusions.
- Geographic or language constraints, if any.

## Procedure
1. Search public sources: GitHub issues, app reviews, marketplace posts, forums, Reddit, Hacker News, Product Hunt, Indie Hackers, SaaS changelogs, public docs, API announcements, and compliance updates.
2. Look for repeated complaints, expensive manual processes, bad reviews, abandoned plugins, broken workflows, repeated job posts, high-value manual B2B problems, and niches with willingness to pay.
3. Record observed signal, audience, pain, workaround, automation angle, validation path, risks, and confidence.
4. Prefer lawful, terms-aware, privacy-respecting opportunities.

## Output format
```text
Observed signal:
Audience:
Pain:
Current workaround:
Why automation helps:
Possible product/service:
Validation path:
Risks:
Confidence:
```

## Safety constraints
Do not collect private data, bypass access controls, scrape in violation of clear restrictions, dox people, or enable fraud, credential abuse, spam, or unauthorized exploitation.
