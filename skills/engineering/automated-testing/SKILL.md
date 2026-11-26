---
name: automated-testing
description: Create effective unit, integration and browser end-to-end tests.
---

# automated-testing

1. Map acceptance criteria and high-risk behaviors to tests; prefer deterministic fixtures and small tests.
2. Use pytest for Python, appropriate JS test runner for React and Playwright for critical browser flows when available.
3. Cover negative cases, authorization, validation, boundary conditions, retries and failure recovery. Use disposable services and synthetic records.
4. Avoid arbitrary sleeps and brittle selectors; isolate state, mock external systems selectively and retain reproducible commands.
5. Run targeted then full tests, report exact outcomes and skipped tests. Never fabricate results or change tests merely to hide regressions.
