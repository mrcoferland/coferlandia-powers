---
name: mcp-builder
description: Design and build MCP servers with clear tools, concise schemas, good error handling, and realistic evaluations. Use when integrating an external service through the Model Context Protocol.
license: Apache-2.0
metadata:
  author: Diego Cofré
  project: coferlandia-powers
  version: "0.1.0"
---

# MCP Server Development Guide

## Note
Adapted for Coferlandia from public MCP design patterns; wording and examples are original and brand-neutral.

## When to use this skill
Use this skill when you are building or reviewing an MCP server, especially if the server will expose external APIs, files, or workflow tools to agents.

## Core principles
- Prefer clear, action-oriented tool names.
- Keep each tool focused on one job.
- Return compact, relevant outputs.
- Use pagination or filtering when results can grow large.
- Make error messages actionable.
- Mark tools read-only or destructive when that distinction matters.

## Design workflow
1. Understand the target service and its API.
2. Decide whether the client needs a few workflow tools or broad endpoint coverage.
3. Choose transport based on deployment needs.
   - stdio for local use
   - HTTP for remote use
4. Define input schemas with strict, well-named fields.
5. Define output shapes that are easy for agents to consume.
6. Add pagination, retries, and good failure messages.
7. Review the server as an agent user, not only as a developer.
8. Create a small evaluation set with realistic questions and verifiable answers.

## Implementation checklist
- documented tools
- consistent naming
- authentication handled explicitly
- safe defaults
- structured responses where useful
- tests or sample calls that prove the tools work

## Verification
Before shipping, verify that a fresh agent can:
- discover the right tool quickly
- call it with minimal guesswork
- understand the response without extra prompting
- recover from common API errors
