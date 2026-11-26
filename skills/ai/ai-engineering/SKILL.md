---
name: ai-engineering
description: Build evaluated LLM applications, agents and RAG systems.
---

# ai-engineering

1. Define task, baseline, quality target, latency and cost budget. Choose RAG for retrieval, fine-tuning only when justified and deterministic code where possible.
2. Version prompts, models, embedding settings and datasets. Build ingestion with provenance, permissions, deduplication and chunking.
3. Separate retrieval from generation; test retrieval recall and grounded answers with representative held-out examples. Avoid exposing private data to external providers without approval.
4. Validate structured outputs and tool inputs; require approval for irreversible actions. Use bounded retries, timeouts and observability.
5. Compare quality, cost and failure modes against baseline; record limitations and fallback. No credentials in prompts.
