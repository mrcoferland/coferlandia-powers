---
name: builder-mvp
description: Convert an online opportunity into a low-cost MVP and validation experiment optimized for Diego Cofré. Use when an idea needs a 48-hour and 7-day technical build plan with success and kill criteria.
license: Apache-2.0
metadata:
  author: Diego Cofré
  project: coferlandia-powers
  version: "0.1.0"
---

# Builder / MVP Designer

## Purpose
Turn an opportunity into the smallest technical experiment that can validate demand cheaply.

## When to use this skill
Use after a promising opportunity has preliminary evidence and needs an MVP, script, dashboard, bot, API, cron workflow, or concierge test.

## Inputs expected
- Opportunity and target customer.
- Main hypothesis to validate.
- Available data sources and APIs.
- Constraints on time, budget, hosting, and stack.

## Procedure
1. Define the MVP in one sentence.
2. Pick one core feature that tests the main hypothesis.
3. Explicitly list what not to build yet.
4. Favor Diego's fit: Python, .NET, APIs, backend automation, bots, GitHub, SQLite/PostgreSQL, Oracle/AWS/VPS, simple dashboards, scripts, cron jobs, and lightweight services.
5. Define 48-hour and 7-day plans.
6. Define one main metric, success criteria, and kill criteria.
7. Identify technical risks, platform dependencies, and data/API limits.

## Output format
```text
MVP:
Core feature:
Do not build yet:
Suggested stack:
Data/APIs:
Implementation steps:
48-hour plan:
7-day plan:
Success criteria:
Kill criteria:
Technical risks:
```

## Safety constraints
Do not build tools that facilitate fraud, phishing, credential theft, unauthorized exploitation, private-data abuse, paywall bypassing, or autonomous financial execution.
