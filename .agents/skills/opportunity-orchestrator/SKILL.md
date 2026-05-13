---
name: opportunity-orchestrator
description: Coordinate multi-skill opportunity research workflows for agentic online businesses. Use when a broad opportunity request needs scouting, market analysis, economics, MVP design, risk review, and a BUILD/TEST/WAIT/KILL recommendation.
license: Apache-2.0
metadata:
  author: Diego Cofré
  project: coferlandia-powers
  version: "0.1.0"
---

# Opportunity Orchestrator

## Purpose
Coordinate the complete research workflow for agentic online business opportunities and produce a ranked recommendation.

## When to use this skill
Use when the user gives a broad opportunity request, a business hypothesis, or a list of candidate ideas that needs structured research across multiple specialist skills.

## Inputs expected
- User goal or hypothesis.
- Scope, geography, budget, timeline, and constraints.
- Known candidate opportunities, if any.
- Diego-specific fit constraints: strong backend, APIs, Python, .NET, automation, bots, databases, and low-cost validation.

## Procedure
1. Restate the request and define the decision needed.
2. Choose specialist skills: Scout, Source Quality Scorer, Market Analyst, CFO, Builder, Skeptic, and Reporter. Add Crypto/DeFi, Prediction Markets, or Online Business OSINT when relevant.
3. If delegating to subagents, pass complete context because subagents may have isolated context.
4. Ask Scout for candidates, not final economics.
5. Ask Source Quality Scorer to grade external evidence.
6. Ask Market Analyst to assess demand and distribution.
7. Ask CFO to estimate ranges and assumptions.
8. Ask Builder to design the smallest validation experiment.
9. Ask Skeptic to attack assumptions and select BUILD, TEST, WAIT, or KILL.
10. Resolve contradictions and rank opportunities with the standard scoring model.
11. Ask Reporter to create the final report when a candidate deserves a full write-up.

## Output format
```text
Research plan:
Delegated tasks:
Key findings:
Top opportunities:
Rejected opportunities:
Open questions:
Recommended next action:
```

## Safety constraints
Never execute financial transactions, sign blockchain transactions, move funds, initiate swaps, commit to business agreements, handle private keys, or assist fraud, phishing, illegal hacking, market manipulation, laundering, tax evasion, or unauthorized exploitation. Mark unsafe opportunities as KILL or require human review.

## Related resources
- `workflows/deep-dive.md`
- `templates/final-report.md`
