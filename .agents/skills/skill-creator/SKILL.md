---
name: skill-creator
description: Create or revise Agent Skills with clear triggers, compact instructions, and testable guidance. Use when turning a workflow into a new skill or auditing an existing skill for quality.
license: Apache-2.0
metadata:
  author: Diego Cofré
  project: coferlandia-powers
  version: "0.1.0"
---

# Skill Creator

## Note
Adapted for Coferlandia from the public Agent Skills pattern; wording and examples are original and brand-neutral.

## When to use this skill
Use this skill when you need to:
- draft a new skill from a stable workflow
- tighten an existing skill so it is shorter and clearer
- convert a repeated action into a reusable playbook
- review a skill for missing triggers, risks, or examples

## Procedure
1. Identify the real job the skill should solve.
2. Define clear trigger conditions in user language.
3. Keep the instructions compact and specific.
4. Include inputs, outputs, and safety limits.
5. Prefer concrete steps over motivational prose.
6. Add a brief note if the skill is adapted from an external pattern.
7. If the skill needs extra files, make their purpose explicit.
8. If the workflow has tests, include verification steps.

## Quality checklist
- Title matches the skill's purpose.
- Description explains when to use it in one sentence.
- Body is easy to scan.
- No filler, no brand copy, no hidden dependencies.
- The skill can be executed without asking for extra context in normal cases.

## Output shape
When drafting a skill, produce:
- name
- description
- trigger phrases
- when to use
- steps
- safety notes
- verification
