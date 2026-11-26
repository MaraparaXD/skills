---
name: multi-agent-orchestrator
description: Delegate independent engineering tasks to authorized local agents with bounded context.
---

# multi-agent-orchestrator

1. Define acceptance criteria and inspect the available agents/tools; use PAL clink only when configured and explicitly permitted.
2. Assign small independent read-only analyses (architecture, tests, security). Supply only relevant paths and sanitized context. Do not send client data or secrets to third parties without authorization.
3. Request evidence, assumptions, concrete file references and a short result. Cap parallelism at two and avoid recursive delegation.
4. For code changes, use isolated git worktrees and a single integrator. No bypass of approvals, no shared mutable working tree.
5. Validate results with local tests. If a provider quota is exhausted, report it and offer another authorized agent; never attempt to bypass limits.
