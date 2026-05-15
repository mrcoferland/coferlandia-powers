---
name: webapp-testing
description: Test local or authorized web applications with Playwright. Use when you need to inspect UI behavior, verify interactions, capture screenshots, or debug browser logs.
license: Apache-2.0
metadata:
  author: Diego Cofré
  project: coferlandia-powers
  version: "0.1.0"
---

# Web Application Testing

## Note
Adapted for Coferlandia from public browser-testing patterns; references and examples are original and brand-neutral.

## When to use this skill
Use this skill for:
- local web apps
- staging environments you are allowed to test
- UI regressions and interaction checks
- screenshots, console logs, and flow verification

## Procedure
1. Decide whether the page is static HTML or a dynamic app.
2. If the app is dynamic, wait for the server and the browser to finish loading before inspecting the DOM.
3. Use a short Playwright script with `sync_playwright()` unless async is clearly needed.
4. Prefer stable selectors such as role, text, label, or data-test attributes.
5. Inspect the rendered page before acting when the UI is not obvious.
6. Capture screenshots or logs when they help explain the result.
7. Verify the final state instead of assuming the click worked.

## Best practices
- launch Chromium headless for automation
- wait for `networkidle` on dynamic pages when appropriate
- keep scripts small and readable
- close the browser in a `finally` block if possible
- use the smallest set of interactions that proves the bug or success case

## Safety notes
- Only test applications you own or are explicitly authorized to test.
- Do not use this skill for credential theft, bypassing access controls, or any unauthorized probing.
