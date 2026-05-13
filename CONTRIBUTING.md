# Contributing

Contributions are welcome if they improve safe, practical opportunity research and validation.

## Contributing skills

- Add skills under `.agents/skills/<skill-name>/SKILL.md`.
- Use short, stable, lowercase, hyphenated names.
- The `name` field must match the parent directory.
- Every `SKILL.md` must start with YAML frontmatter containing `name` and `description`.
- Descriptions should be concise, specific, and action-oriented.
- Keep skill bodies compact and operational. Put longer material in referenced files.

## Validate

Run:

```bash
python3 scripts/validate-skills.py
```

Fix hard errors before submitting.

## Examples

Example reports should be educational, realistic, safe, and explicit about assumptions. Do not make income promises or invent sources.

## Safety expectations

Do not contribute material that facilitates illegal activity, fraud, credential theft, credential stuffing, phishing, malware, unauthorized exploitation, market manipulation, money laundering, tax evasion, doxxing, private-data abuse, paywall bypassing, autonomous trading, wallet operations, or private-key handling.
