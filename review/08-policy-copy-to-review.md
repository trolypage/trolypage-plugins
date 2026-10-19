# Proposed policy and MCP guide corrections — unpublished

These are editorial drafts and items for factual confirmation, not approved legal commitments. Source inspection alone does not establish a completed security audit or full policy compliance.

## Publisher identity

Privacy section 13 still names SkyNet Solution and a Boulder, US address, while the footer names TROLYPAGE COMPANY LIMITED in Hanoi. Mobile support also names SkyNet Solution. The owner must confirm the legal/brand/service-provider relationship or replace the stale block. Current public information for comparison:

```text
TROLYPAGE COMPANY LIMITED
Enterprise registration number: 0111551901
Registered office: No. 72, Alley 318 De La Thanh, O Cho Dua Ward, Hanoi, Vietnam
Support: support@trolypage.com
MCP submission contact: support.mcp@trolypage.com
```

The owner confirmed Alex Nguyen as the submitter. Keep Trolypage as the verified business identity.

## MCP policy coverage: proposed wording to verify

When you connect an AI assistant to TrolyPage through MCP, the assistant sends the arguments for the tools you request and receives their results. Depending on the selected tools, those results can contain workspace customer information, conversations, internal notes, orders, products, reports, social content, knowledge, agent configuration or managed assets. Access is limited by the account, workspace role, plan and connection permissions.

Write tools may change internal records or request actions in connected services. Drafts and pending approvals are distinct from completed sends, publication, payment and delivery. You can disconnect the connector in the host and revoke the TrolyPage authorization to stop further access. Disconnecting does not remove data already returned to the AI host or content already sent to third-party services; consult each provider's controls and TrolyPage's published deletion instructions.

Payment associated with a merchant order takes place outside the assistant through the merchant's supported flow. TrolyPage may return a payment QR or payment status. A QR or submitted request does not itself establish receipt of money.

**Verify before publication:** exact processors and AI-use conditions, retention/deletion of connector logs and results, international transfers, model-training/secondary-use restrictions, encrypted storage and incident contact. Do not introduce unconfirmed guarantees or retention periods.

## Guide copy corrections

- Catalog: “One unified connection plus focused module endpoints. Available tools depend on workspace permissions and plan.” Avoid hardcoded counts.
- Analytics: “Metrics are read-only. Report exports queue a job and are write operations.”
- Approval: “TrolyPage supports Auto, Hybrid and Strict modes. Some writes can execute directly in Auto/Hybrid; inspect the actual returned state. Strict queues writes. Shop order approval, broadcast approval and the AI host's confirmation rules are separate controls.”

A source edit does not prove production has changed, especially with translation strings or cached content. Reopen the public URLs and verify the affected sections after deployment.
