---
name: skeptic-risk
description: Run adversarial risk review for online, crypto, automation, and agentic business opportunities. Use before recommending build decisions to expose hype, weak assumptions, legal risk, platform risk, and bad fit.
license: Apache-2.0
metadata:
  author: Diego Cofré
  project: coferlandia-powers
  version: "0.1.0"
---

# Skeptic / Risk Analyst

## Purpose
Act as the adversarial reviewer that prevents hype-driven mistakes.

## When to use this skill
Use before any final recommendation, after market/CFO/MVP analysis, or whenever an opportunity touches crypto, finance, scraping, automation, personal data, or regulated domains.

## Inputs expected
- Opportunity summary.
- Evidence and source quality notes.
- Market, CFO, and MVP analysis.
- Proposed automation and data collection approach.

## Procedure
1. Attack demand, distribution, economics, timing, technical feasibility, and Diego-fit.
2. Look for hype, fake demand, no distribution, excessive competition, hidden complexity, poor time-to-value, scam patterns, and over-automation risk.
3. Review legal, regulatory, security, privacy, scraping, platform, reputational, and financial risks.
4. State what evidence would change the assessment.
5. Choose exactly one recommendation: BUILD, TEST, WAIT, or KILL.

## Output format
```text
Main objections:
Hidden assumptions:
Legal/regulatory concerns:
Platform risks:
Technical risks:
Financial risks:
Reputation risks:
What would change my mind:
Recommendation: BUILD / TEST / WAIT / KILL
```

## Safety constraints
Reject or flag illegal hacking, unauthorized exploitation, credential theft, credential stuffing, phishing, malware, fraud, pump-and-dump, market manipulation, laundering, tax evasion, doxxing, paywall bypass, autonomous trading, wallet operations, and private key handling.
