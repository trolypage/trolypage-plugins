---
name: troly-knowledge
description: Search TrolyPage agent knowledge, nodes, approved facts, and documents, or propose governed facts for review. Use for source-grounded answers, knowledge audits, FAQ preparation, or fact updates.
---

# TrolyPage Knowledge

Use only the `trolypage` MCP server. Read [tool-catalog.md](references/tool-catalog.md) to select the tools available for this workflow.

## Workflow

1. Resolve the real AI Agent ID before searching its knowledge.
2. Prefer `search-knowledge` for answer retrieval, `search-facts` for approved structured facts, and `search-documents` for source discovery.
3. Use `list-knowledge-nodes` or `list-facts` for audits and inventory.
4. Use `propose-fact` only to submit a candidate; clearly state that it remains unavailable to customer answers until approved.

Never present an unapproved fact as authoritative, merge knowledge across agents without permission, or fill gaps with invented business policy.
