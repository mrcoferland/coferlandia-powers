# Security Policy

## Secrets and sensitive material

Do not commit secrets, API keys, private keys, seed phrases, wallet files, passwords, `.env` files, credentials, or production database dumps.

Use environment variables or a dedicated secret manager. Grant least privilege to every token and review tool permissions before running automation.

## Sensitive actions

Keep human approval for sensitive actions, including spending money, sending messages at scale, changing infrastructure, contacting customers, executing contracts, or interacting with crypto wallets.

Avoid autonomous financial execution. This project is not a trading bot and must not sign transactions, move funds, initiate swaps, or place bets.

## Reporting vulnerabilities

Report vulnerabilities through GitHub issues or the contact listed in the README. Do not include live secrets in vulnerability reports.
