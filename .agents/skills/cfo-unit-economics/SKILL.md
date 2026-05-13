---
name: cfo-unit-economics
description: Estimate practical unit economics for an online opportunity using ranges and explicit assumptions. Use when revenue model, pricing, costs, margin, break-even, and opportunity cost need evaluation.
license: Apache-2.0
metadata:
  author: Diego Cofré
  project: coferlandia-powers
  version: "0.1.0"
---

# CFO / Unit Economics

## Purpose
Translate an opportunity into practical numbers without false precision.

## When to use this skill
Use once a candidate opportunity has enough market signal to estimate revenue, costs, pricing, and break-even scenarios.

## Inputs expected
- Candidate opportunity and target customer.
- Proposed product format.
- Estimated acquisition channel and delivery model.
- Known tools, APIs, hosting, data, or labor costs.

## Procedure
1. State assumptions before numbers.
2. Estimate revenue model and expected customer.
3. Use ranges for pricing, setup cost, monthly operating cost, gross margin, time to first dollar, and break-even.
4. Create conservative, base, and optimistic scenarios.
5. Include opportunity cost for Diego's time.
6. Identify financial risks and sensitivity drivers.
7. Recommend BUILD, TEST, WAIT, or KILL only from a financial perspective.

## Output format
```text
Revenue model:
Expected customer:
Possible pricing:
Setup cost:
Monthly operating cost:
Gross margin:
Time to first dollar:
Break-even:
Conservative scenario:
Base scenario:
Optimistic scenario:
Financial risks:
Opportunity cost:
CFO recommendation:
```

## Safety constraints
This is not financial, investment, tax, or legal advice. Do not recommend trades, swaps, token purchases, or fund movement. Require human approval for any money movement.
