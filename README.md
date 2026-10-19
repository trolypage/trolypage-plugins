# TrolyPage plugins for OpenAI, Claude and Muse

TrolyPage provides AI customer support, CRM, social media scheduling and order management for small businesses. These plugins connect an AI assistant to an existing, authorized TrolyPage workspace.

[Product features](https://trolypage.com/features) · [MCP setup](https://trolypage.com/mcp) · [Support](https://trolypage.com/mcp#errors)

**Status: Claude connector and bundle submitted for review; OpenAI draft uploaded; Muse submitted with all 3/3 follow-up requirements complete. No approved directory release.** Updated on October 19, 2026. The repository, review materials and plugin packages are written in English.

## Packages

| Platform | Source | Review archive |
| --- | --- | --- |
| OpenAI | [Portable plugin](packages/openai/trolypage-mcp) | [OpenAI ZIP](archives/openai-trolypage-mcp-1.0.2-DRAFT.zip) |
| Claude | [Skills and MCP bundle](packages/claude/trolypage-mcp) | [Claude ZIP](archives/claude-trolypage-mcp-1.0.2-DRAFT.zip) |
| Muse | [Submission form draft](review/04-muse.md) | Uses the shared technical and review materials |

Both candidates retain the `trolypage-mcp` identity and original mobile app icon. OpenAI candidate 1.0.2 with nine skills and the full MCP endpoint. Claude candidate 1.0.2 has eight skills and uses the dedicated `https://trolypage.com/mcp/claude` directory catalog; the unsupported Automation skill is excluded. OpenAI includes listing metadata, five positive and three negative review cases, commerce disclosure and availability in all platform-permitted countries. Claude Directory uses the public GitHub source; its bundle license is Apache-2.0. This repository contains distribution materials, not the application backend.

## Review the materials

Open [review.html](review.html) for the complete preview, or read these documents:

1. [Listing and copy](review/01-listing-and-copy.md): product definition, publisher, contact, URLs and commerce.
2. [Readiness](review/07-readiness.md): unresolved requirements before submission.
3. Platform guides: [OpenAI](review/02-openai.md), [Claude](review/03-claude.md), [Muse](review/04-muse.md).
4. [Reviewer access, tests and demo](review/06-tests-demo-and-access.md): verified account access, real synthetic fixtures and walkthrough evidence.
5. [Technical and data processing](review/05-technical-and-data.md), [proposed policy corrections](review/08-policy-copy-to-review.md) and [SEO and discovery](review/09-seo-and-discovery.md).

Submission contact: **Alex Nguyen**, **support.mcp@trolypage.com**. Public support: **support@trolypage.com**. Verified OpenAI business publisher: **Trolypage**.

## Current verification

The reviewer workspace has an Owner role and Scale plan. Claude directory OAuth and 180-tool discovery succeeded. The owner attested prior execution of all tools through Inspector/Claude; this is recorded separately from independent representative calls. Real customer/product/order fixtures and an unpaid idempotent order retry were verified. OpenAI's scan account connected and discovered 271 full-endpoint tools; secure reviewer credentials are saved. See [current evidence](evidence/submission-progress-20261019.md).

Claude connector submission succeeded and bundle 1.0.2 is awaiting review. Local package validation, portal scans and business execution remain distinct. Muse's data questionnaire and secure integration requirements are submitted; the portal shows 3/3 complete. No platform approval or live release is claimed. Credentials and backend source are excluded from this distribution.

| Location | Contents |
| --- | --- |
| `packages/` | Reviewed distribution source |
| `review/` | Form drafts, tests, inventory, contracts and readiness findings |
| `evidence/` | Public observations and isolated source-schema extraction; translated descriptions are labeled |
| `assets/` | Original 1024 px mobile icon, 512 px listing icon, 64 px composer icon and inspection sheet |
| `validation-report.json` | Local checks and their limits |
| `archives/SHA256SUMS.txt` | Archive hashes |

## Rebuild

Edit the source in `packages/` and documents in `review/`, then run:

```powershell
python -X utf8 package.py
```

The command validates and rebuilds both archives and refreshes the HTML preview without overwriting reviewed documents or test results. Do not edit ZIP files directly. The two historical generator commands now delegate to this safe rebuild path so they cannot restore obsolete or non-English drafts.

The Agent Plugins schema checks use `jsonschema` from the temporary `trolypage-plugin-schema-validator` directory when available; other build dependencies are Pillow, PyYAML and Markdown. Portal scans and live tests remain separate.

Local directory: `D:/trolypage-plugins`. Public repository: [trolypage/trolypage-plugins](https://github.com/trolypage/trolypage-plugins). The owner selected [Apache-2.0](LICENSE) for original plugin skills and documentation. See NOTICE for scope; the separate application backend is excluded.
