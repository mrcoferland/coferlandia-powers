# coferlandia-powers

A Hermes Agent skill pack for discovering, evaluating, and validating agentic online business opportunities.

## Short description

`coferlandia-powers` is an Agent Skills-compatible skill pack that helps an agent discover online opportunities, evaluate them with market, financial, technical, and risk criteria, and turn the best ones into small validation experiments.

## What this is

- A public-ready Agent Skills skill pack.
- A structured opportunity research and validation system.
- A multi-skill workflow for scouting, evaluating, and testing online business ideas.
- A Diego Cofré-optimized operating system for practical agentic business experiments.

## What this is not

- Not a trading bot.
- Not a money-making promise.
- Not financial, legal, investment, or tax advice.
- Not a wallet automation system.
- Not a system for illegal hacking, fraud, spam, phishing, market manipulation, or unauthorized exploitation.

## Why it exists

Many online business ideas sound exciting but fail because evidence, distribution, unit economics, risk, and validation are not separated. This repository gives an agent a repeatable way to find opportunities, attack assumptions, and design cheap tests before committing to larger builds.

## Primary use cases

- Scout agentic online business opportunities.
- Evaluate micro-SaaS, automation, data products, APIs, dashboards, bots, and productized services.
- Research crypto/DeFi as a source of non-trading product opportunities.
- Use prediction markets as intelligence sources.
- Convert promising ideas into 48-hour and 7-day validation plans.
- Produce opportunity reports with risks and kill criteria.

## Architecture overview

```text
Broad opportunity request
        ↓
Opportunity Orchestrator
        ↓
Scout finds candidate opportunities
        ↓
Source Quality Scorer evaluates evidence
        ↓
Market Analyst evaluates demand and distribution
        ↓
CFO evaluates economics
        ↓
Builder designs MVP / validation experiment
        ↓
Skeptic attacks assumptions and risks
        ↓
Reporter creates final report
        ↓
Decision: BUILD / TEST / WAIT / KILL
```

## Agent layers

1. Opportunity Orchestrator
2. Agentic Opportunity Scout
3. Market Analyst
4. CFO / Unit Economics Analyst
5. Builder / MVP Designer
6. Skeptic / Risk Analyst
7. Source Quality Scorer
8. Crypto / DeFi Researcher
9. Prediction Markets Researcher
10. Online Business OSINT Researcher
11. Opportunity Reporter

## Skills list

Skills live under `.agents/skills/`:

- `opportunity-orchestrator`
- `agentic-opportunity-scout`
- `market-analyst`
- `cfo-unit-economics`
- `builder-mvp`
- `skeptic-risk`
- `source-quality-scoring`
- `crypto-defi-research`
- `prediction-markets-research`
- `online-business-osint`
- `opportunity-reporting`

## Workflows list

- `workflows/daily-scout.md`
- `workflows/weekly-opportunity-review.md`
- `workflows/deep-dive.md`
- `workflows/validate-mvp.md`
- `workflows/kill-or-build.md`

## Repository structure

```text
coferlandia-powers/
├── .agents/skills/       # canonical Agent Skills source
├── workflows/            # operating workflows
├── templates/            # report and experiment templates
├── examples/             # safe educational example reports
├── reports/              # generated reports, ignored except .gitkeep
├── dist/                 # exports, ignored except .gitkeep
└── scripts/              # install, validation, and export helpers
```

## Agent Skills compatibility

This project follows the Agent Skills protocol and the progressive disclosure model described at:

https://agentskills.io/client-implementation/adding-skills-support

Compatibility choices:

- Skills live under `.agents/skills/` for cross-client interoperability.
- Each skill is a directory containing `SKILL.md`.
- Each `SKILL.md` starts with YAML frontmatter.
- Every skill exposes at least `name` and `description`.
- The `name` matches the parent directory.
- Skill descriptions are lightweight catalog metadata.
- Full instructions live in each skill body and should be loaded only when relevant.
- Supporting resources should be loaded only when referenced and needed.

## Hermes usage

Install the skills into a Hermes-compatible local directory:

```bash
bash scripts/install-skills.sh
```

By default this copies `.agents/skills/` into:

```text
~/.hermes/skills/coferlandia-powers/
```

Use symlinks during active development:

```bash
bash scripts/install-skills.sh --symlink --force
```

Then start Hermes and ask it to use the relevant skills. Depending on your Hermes configuration, you may also load skills explicitly with the CLI or session commands.

## Installation

```bash
git clone https://github.com/mrcoferland/coferlandia-powers.git
cd coferlandia-powers
python3 scripts/validate-skills.py
bash scripts/install-skills.sh
```

## Validation

Run:

```bash
python3 scripts/validate-skills.py
```

The validator checks required Agent Skills fields, directory/name consistency, frontmatter presence, vague descriptions, long names, and unresolved placeholders.

## Example prompts

```text
Use coferlandia-powers to scout 10 agentic online opportunities around AI developer tools and rank the top 3.
```

```text
Run a deep-dive on this opportunity: a public API pricing monitor that detects pricing changes and turns them into affiliate/content opportunities.
```

```text
Evaluate this crypto idea as a non-trading product: a DeFi risk dashboard that monitors TVL drops, hacks, stablecoin depegs, and protocol revenue changes.
```

```text
Take this opportunity and produce a 48-hour MVP validation plan optimized for Diego Cofré.
```

## Safety model

The project rejects or flags opportunities involving illegal hacking, unauthorized exploitation, credential theft, credential stuffing, phishing, malware, fraud, pump-and-dump, market manipulation, money laundering, tax evasion, private-data abuse, doxxing, paywall bypassing, autonomous trading, wallet operations, or private-key handling.

When in doubt, the agent should downgrade the opportunity, ask for human review, or mark it as KILL.

## Financial/legal disclaimer

This project is for research, education, and software experimentation. It is not financial advice, investment advice, legal advice, or tax advice. It does not guarantee income. Users are responsible for validating outputs and complying with laws, platform terms, and regulations.

## Roadmap

- Add real-world evaluation datasets for opportunity reports.
- Add optional reference files for source-quality scoring.
- Add report scoring automation.
- Add safe integrations for public data APIs.
- Add more examples for Latin American and Spanish-language markets.

## Contributing

See `CONTRIBUTING.md`. Contributions must preserve the Agent Skills format and the safety model.

## License

Apache License 2.0. See `LICENSE` and `NOTICE`.
