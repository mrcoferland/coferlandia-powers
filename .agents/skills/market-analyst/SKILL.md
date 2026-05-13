---
name: market-analyst
description: Evaluate demand, competition, timing, distribution, and go-to-market path for online business opportunities. Use after scouting to decide whether a real reachable market exists.
license: Apache-2.0
metadata:
  author: Diego Cofré
  project: coferlandia-powers
  version: "0.1.0"
---

# Market Analyst

## Purpose
Evaluate whether a candidate opportunity has real demand, reachable buyers, a plausible distribution path, and a sensible format.

## When to use this skill
Use after candidate discovery or during a deep dive when market structure, competition, or distribution risk needs analysis.

## Inputs expected
- Opportunity description and evidence links.
- Target geography and customer segment.
- Any known competitors or alternatives.

## Procedure
1. Identify who has the problem and who pays.
2. Describe current alternatives and workarounds.
3. Determine whether the pain is urgent, expensive, frequent, or compliance-driven.
4. Classify the market as broad, niche, or ultra-niche.
5. Assess competition as weak, fragmented, strong, or dominant.
6. Identify reachable distribution channels Diego can actually test.
7. Choose the best packaging: SaaS, API, dashboard, bot, service, data product, plugin, content, affiliate asset, or internal tool.
8. Recommend validation that avoids building too much.

## Output format
```text
Target customer:
Problem:
Current alternatives:
Market size signal:
Competition:
Distribution channels:
Timing:
Validation path:
Main bottleneck:
Market recommendation:
```

## Safety constraints
Separate facts from assumptions. Avoid claiming market size without evidence. Flag regulatory, privacy, scraping, or platform-terms issues for Skeptic review.
