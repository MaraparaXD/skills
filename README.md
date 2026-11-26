# Engineering Skills Hub MCP

Personal skill catalog and read-only MCP server for engineering agents. Original third-party skill folders retain their contents and licenses; new playbooks are in `skills/`. The optional Claude marketplace remains available under `plugins/`.

## Structure
- `skills/frontend`, `skills/engineering`, `skills/ai`, `skills/security`, `skills/devops`, `skills/orchestration`, `skills/knowledge`: categorized skills.
- `plugins/`: optional Claude design marketplace bundles.
- `archive/`: removed from the active catalog; historical content only. Do not install automatically.
- `catalog.json`: explicit allowlist, with curated and legacy-review status.
- `hub/`: read-only MCP catalog implementation.
- `docs/DEPLOYMENT.md`: VPS installation and client examples.
- `docs/INTEGRATIONS.md`: local/remote tooling roadmap.

The server exposes list_skills, search_skills and read_skill. It does not execute skills, commands, model calls or other MCPs. Clients use the returned text as optional reference material and perform work in their own permission boundary. No model API keys are required. Legacy skills are hidden by default until reviewed; some require Claude-specific plugins or tools.

## Run locally
```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python -m hub.server
```
The last command uses MCP stdio (not an interactive shell). Configure your client to launch it. See deployment guide for SSH transport.

## Claude plugin compatibility
`/plugin marketplace add MaraparaXD/skills` then install the desired plugin from `local-design-skillstack`. Existing standalone skill install paths have changed; use an explicitly selected skill folder under `skills/`, not a recursive copy of the entire repo. Marketplace behavior must be verified before merging.

## License
Original third-party licenses/attributions remain in their source folders where supplied. Check each upstream license before redistribution. No blanket license asserted over imported content.
