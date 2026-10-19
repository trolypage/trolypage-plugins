---
name: troly-analytics
description: Produce read-only TrolyPage business, sales, channel, activity, response, AI, employee, follow-up, social, source, and forecast reports. Use for metrics, comparisons, trends, diagnostics, or executive summaries.
---

# TrolyPage Analytics

Use only the `trolypage` MCP server. Metric retrieval tools are read-only; export-report queues a background export and is a write. Read [tool-catalog.md](references/tool-catalog.md) before choosing reports.

## Workflow

1. Call `report-options` when filters, ranges, or available report types are uncertain.
2. Use the smallest number of reports that directly answer the question and keep their date ranges and filters aligned.
3. Label forecast output as an estimate, distinguish counts from rates, and state the compared periods.
4. Do not infer missing causal relationships from correlations in the returned data.

For a weekly operating review, combine overview, sales, response, channel, and forecast only when each adds a decision-relevant signal.
