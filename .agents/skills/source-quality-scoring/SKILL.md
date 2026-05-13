---
name: source-quality-scoring
description: Score external evidence quality from 1 to 5 for opportunity reports. Use whenever research depends on web sources, public claims, market signals, crypto dashboards, reviews, or community posts.
license: Apache-2.0
metadata:
  author: Diego Cofré
  project: coferlandia-powers
  version: "0.1.0"
---

# Source Quality Scoring

## Purpose
Evaluate how trustworthy each external source is before it influences an opportunity recommendation.

## When to use this skill
Use whenever a report depends on web sources, public claims, reviews, market data, crypto dashboards, social posts, SEO articles, or community discussions.

## Inputs expected
- Source URL or citation.
- Claim extracted from the source.
- Publication date or observed freshness.
- Other corroborating or contradictory sources.

## Scoring rubric
Score 1-5:
- 5: primary source, fresh, reputable, verifiable, low bias, independently corroborated.
- 4: strong secondary source or high-quality dataset with minor limitations.
- 3: plausible source with moderate bias or limited corroboration.
- 2: weak source, stale, promotional, thinly verified, or likely SEO-driven.
- 1: unreliable, unverifiable, hype-heavy, AI filler, or contradicted by better sources.

## Procedure
1. Classify source type: primary, secondary, community, commercial, dataset, social, or unknown.
2. Assess freshness, reputation, verifiability, bias, corroboration, data quality, SEO-spam risk, AI-filler risk, and hype risk.
3. Explain how the source should or should not affect the decision.

## Output format
```text
Source:
Type:
Freshness:
Reputation:
Verifiability:
Bias risk:
Corroboration:
Evidence quality score:
Notes:
```

## Safety constraints
Do not treat a single weak source as confirmed. Label unverified claims clearly.
