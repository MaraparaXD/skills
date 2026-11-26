---
name: backend-engineering
description: Design and implement maintainable Python/FastAPI services and REST APIs.
---

# backend-engineering

1. Identify contracts, actors, trust boundaries, business invariants and existing architecture before editing.
2. Use typed request/response models, clear service boundaries, dependency injection only when useful, consistent errors and pagination. Validate data server-side.
3. Enforce authorization at each resource and tenant boundary. Use parameterized queries, timeouts, bounded retries and idempotency for side effects.
4. Keep secrets in environment or secret store; avoid logging sensitive payloads. Add structured logs with correlation IDs.
5. Implement smallest vertical slice; add unit/integration tests for success, validation, permissions and failures. Verify migrations and API compatibility.
