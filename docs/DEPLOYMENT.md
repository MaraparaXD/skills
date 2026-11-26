# VPS deployment (MVP)

Use a separate unprivileged service account and a versioned read-only checkout. This design uses MCP stdio over SSH; it requires no new public HTTP port, no API key and no persistent MCP daemon. Each client opens its own SSH subprocess. Do not use root, share SSH credentials, forward agents, or grant Docker/sudo access.

## Server setup
As an administrator, create a dedicated account and install Python 3.11+ with venv support. Provision an SSH key from your client; verify the host key via an independent trusted channel. Keep the checkout and venv owned by a separate deployment identity, readable/executable but not writable by the MCP runtime account. Example deployment directory: /opt/engineering-skills-hub. Clone this repository at an approved commit and run:
```sh
cd /opt/engineering-skills-hub
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python -m unittest discover -s tests -v
```
Before production, resolve and pin the SDK and transitive dependencies, review existing skill licenses and run a real MCP client smoke test. No deploy has been performed by this PR.

Use a dedicated SSH key with a forced command in authorized_keys (replace PUBLIC_KEY):
```text
restrict,command="cd /opt/engineering-skills-hub && exec .venv/bin/python -m hub.server" ssh-ed25519 PUBLIC_KEY
```
The key cannot request an arbitrary command or forwarding. Confirm file permissions, account restrictions and existing sshd policies before testing; do not alter existing SSH access. Never paste private keys into a chat or the repo.

## Clients
Create an SSH alias `engineering-hub` in ~/.ssh/config with HostName, User, IdentityFile, IdentitiesOnly yes, StrictHostKeyChecking yes, BatchMode yes, ForwardAgent no. Test host identity out of band. Example Codex registration:
```sh
codex mcp add engineering-hub -- ssh -T engineering-hub
codex mcp list
```
Claude Code:
```sh
claude mcp add --transport stdio --scope user engineering-hub -- ssh -T engineering-hub
claude mcp list
```
Gemini CLI settings.json (merge, do not overwrite other configuration):
```json
{"mcpServers":{"engineering-hub":{"command":"ssh","args":["-T","engineering-hub"]}}}
```
Use the client's MCP UI to call list_skills then read_skill with id backend-engineering. Confirm missing IDs fail and legacy entries require explicit opt-in. SSH and stdio examples must be tested against installed client versions.

## Updates
Review a PR, deploy a pinned commit to a new release directory, run tests, then switch the deployment path atomically. Keep the previous release for rollback. Restart clients to pick up the new version. No auto-pull from untrusted branches.

## Future HTTPS
If remote HTTP is needed, implement Streamable HTTP with authenticated requests, TLS, request limits, origin validation, per-client access, no public unauthenticated endpoint and auditable metadata-only logs. Prefer a private network. Do not expose the stdio server directly to the internet.
