---
name: secure-coding
description: Review and implement secure application code using threat modeling and OWASP practices.
---

# secure-coding

1. Identify assets, entry points, actors, trust boundaries and authorization assumptions.
2. Review authentication, object-level authorization, input validation, injection, SSRF, file uploads, output encoding, cryptographic configuration and secret handling.
3. Use Semgrep or equivalent local scanners when available; validate findings manually and avoid claiming coverage from a clean scan.
4. Report severity, affected code, evidence, impact and a practical remediation. Test with synthetic fixtures only in authorized environments.
5. Require regression tests, dependency checks and safe defaults before release. Never run destructive tests against real systems without approval.
