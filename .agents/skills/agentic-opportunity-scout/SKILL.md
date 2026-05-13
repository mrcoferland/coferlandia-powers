---
name: agentic-opportunity-scout
description: Discover online opportunities that can be executed, assisted, or scaled by agents. Use when looking for candidate ideas from public signals across GitHub, forums, marketplaces, AI tools, crypto, SaaS changes, and repeated pain points.
license: Apache-2.0
metadata:
  author: Diego Cofré
  project: coferlandia-powers
  version: "0.1.0"
---

# Agentic Opportunity Scout

## Purpose
Surface candidate opportunities with evidence. Do not deeply evaluate economics; produce enough signal for downstream analysis.

## When to use this skill
Use during broad discovery, daily scouting, or when the user asks for new online business opportunities that can be automated by agents.

## Inputs expected
- Search theme, vertical, or constraints.
- Preferred opportunity types: micro-SaaS, data products, bots, dashboards, APIs, automation workflows, plugins, or productized services.
- Time window and geographic scope, if relevant.

## Procedure
1. Search across GitHub, Hacker News, Product Hunt, Reddit, X/Twitter, Indie Hackers, AppSumo, Chrome Web Store, WordPress plugins, freelance marketplaces, API launches, AI tooling, crypto/DeFi, prediction markets, pricing changes, and regulatory updates.
2. Look for repeated complaints, expensive manual processes, abandoned tools with demand, weak incumbents, new platforms, new compliance burdens, and tasks agents can automate.
3. Capture direct source links and timestamps when possible.
4. Prefer B2B pain with clear willingness to pay and cheap validation.
5. Produce 5-10 candidates, then filter to the strongest 3 when asked.

## Output format
```text
Opportunity:
Category:
Signal:
Evidence:
Source links:
Why now:
Who pays:
Automation potential:
First experiment:
Confidence:
```

## Safety constraints
Do not recommend opportunities based on illegal hacking, credential theft, phishing, fraud, market manipulation, scraping private data, bypassing access controls, or autonomous financial execution.

## Related resources
- `workflows/daily-scout.md`
- `templates/opportunity-card.md`
