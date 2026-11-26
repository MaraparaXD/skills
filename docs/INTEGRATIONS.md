# Integration plan

The hub is a skill catalog, not a universal proxy. MCP servers are executable tools; SKILL.md files are instructions. This MVP only provides the latter. Keep project-specific tools local by default.

| MCP | Placement | Status |
|---|---|---|
| Context7 | local client or approved remote service | planned |
| Serena | local workspace | planned |
| PAL clink | local CLI authentication and sandbox | planned |
| Playwright | local isolated browser/test workspace | planned |
| GitHub | approved scoped local/remote access | planned |
| Semgrep | local source scan | planned |
| shadcn/ui | local project | planned |
| Postgres | development DB only, least privilege | planned |
| Hugging Face | approved remote or local | planned |
| Promptfoo | isolated test environment | planned |

Install from official upstreams, pin versions, verify permissions and review terms. No API keys required for the catalog; external models and providers have their own billing/quotas. Do not forward provider tokens to the VPS. Avoid exposing local file paths, terminals, browser sessions, Docker or production databases remotely. A future gateway must use explicit tool allowlists, per-project identities, bounded outputs, timeouts and policy checks; no arbitrary command execution or recursive delegation.

## Migration decisions
Legacy folders are moved intact to categories or optional plugin bundles. Archived skills are not in the active catalog. `learn-codebase` and `oneskill` are archived due to aggressive context use. `vercel-cli-with-tokens` is archived because it instructs printing an authentication token. `cloud-sync` and `omni-routes` require extra dependencies. Reporting and unrelated utility skills are archived to focus the engineering scope. Original git history remains available.

All imported skills are marked legacy-review because their full contents and dependency graphs have not been audited. Review individually for prompt injection, secrets, command execution, licensing, duplicate identifiers and hard-coded paths before enabling them. The new curated playbooks have no external runtime dependency; tool recommendations are conditional. For future adapters, retain local fallback when a provider is unavailable.
