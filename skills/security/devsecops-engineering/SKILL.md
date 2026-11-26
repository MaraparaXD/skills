---
name: devsecops-engineering
description: Build safe Docker and CI/CD pipelines with repeatable security controls.
---

# devsecops-engineering

1. Inventory build inputs, runtime permissions and deployment targets. Prefer immutable images, pinned versions/digests and non-root users.
2. Keep secrets outside source and build layers; use scoped CI identities and protected environments.
3. Run lint, tests, SAST, dependency and image scanning; document exceptions and expiry. Generate SBOM where useful.
4. Use staged deployments, health checks, resource limits, rollback and audit logs. Do not automatically deploy or modify infrastructure without authorization.
5. Verify failure paths, backup/restore and least privilege; never mount the Docker socket into an untrusted service.
