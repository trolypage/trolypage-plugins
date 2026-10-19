# Claude directory profile release — October 19, 2026

The owner selected a dedicated Claude Directory catalog. The full MCP service retains its Gen AI functionality.

| Connection | Purpose |
| --- | --- |
| `https://trolypage.com/mcp/claude` | Business directory profile; 180 allowlisted tools before entitlement filtering |
| `https://trolypage.com/mcp/troly` | Full MCP catalog, including existing Gen AI capabilities |

The directory server restricts both discovery and execution. It excludes AI image/video/audio generation, agent execution and configuration, Automation Hub, and arbitrary Integration Hub operations. Text generation for captions, hashtags and business drafts remains available. No MCP resources or prompts are exposed by the directory profile. OAuth resource validation prevents a token issued for the directory endpoint from accessing the full endpoint.

Backend changes also complete tool annotations, provide English directory descriptions, synchronize broadcast creation's input schema with request validation, and add a read-only, tenant-scoped broadcast sender lookup.

Validation: 248 backend MCP feature/unit tests passed. After the final schema-prose correction, seven catalog/authorization tests passed again. PHP formatting and diff whitespace checks passed. These are automated local regressions, not evidence that every tool has completed an authenticated production business workflow.

Production deployment applied 14 explicitly listed files after comparing existing file hashes against the inspected baseline, checking payload hashes and PHP syntax, and creating a private rollback copy. Routes were cached, the MCP inspector cache was invalidated, and the running HTTP and stream Octane pools were gracefully reloaded. No environment variables or Gen AI handlers were changed.

Live Claude verification: OAuth completed for TrolyPage Reviewer against the directory resource. The connector submission Tools step read 180 tools live: 90 read-only and 90 write tools. It showed four advisory suggestions to reference target API documentation (asset imports, URL knowledge ingestion and social comment actions). The previous catch-all operation flag and missing annotation suggestions did not appear. This verifies discovery and portal metadata checks, not execution of all tools.

Claude bundle candidate 1.0.2 uses the dedicated endpoint and eight skills; the unsupported Automation skill was removed from this candidate. OpenAI remains connected to the full endpoint. This release note does not assert directory approval or completion of authenticated all-tool testing.
