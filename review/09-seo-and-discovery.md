# SEO, discovery and product clarity review

Reviewed October 19, 2026. Contact: **Alex Nguyen**, support.mcp@trolypage.com. This document records the earlier public-page observations; changing repository language does not change the live website.

## Assessment

The earlier listing assumed readers already understood TrolyPage. Its broad subtitle and opening did not define the product clearly enough. The revised candidate names the actual jobs: AI customer support, CRM, social media scheduling and order management. The brand and verified publisher are unchanged. This candidate now uses English throughout, including example prompts and tool-reference descriptions.

The Features page has a useful on-page foundation: readable HTML describing concrete tasks. Clarity and consistency still need work. This inspection does not establish good rankings or demand; it used no Search Console data, keyword-volume research or Core Web Vitals report.

## Three separate discovery surfaces

| Surface | What matters |
| --- | --- |
| Google / Bing | Crawlable public pages addressing real needs, useful content and internal links |
| OpenAI / Claude / Muse directories | Name, subtitle, description, README and examples explaining benefits and prerequisites to unfamiliar readers |
| Tool selection after connection | Tool descriptions, input schemas, data scope and test prompts that help the host choose appropriate tools |

Keywords in a ZIP do not establish improved Google ranking or guaranteed directory recommendations. OpenAI recommends testing branded, unbranded and negative prompts. [Metadata guidance](https://developers.openai.com/plugins/guides/optimize-metadata).

## Revised candidate copy

| Field | Current draft |
| --- | --- |
| Contact | Alex Nguyen |
| Display name | TrolyPage |
| Subtitle | AI support, CRM & social posts — 30 characters |
| Opening | TrolyPage is AI customer support, CRM, social media scheduling and order management software for small businesses. |
| Next paragraph | Explains the business workspace and the integration with an existing account |
| Starter prompts | Summarize a conversation/draft a reply; find a SKU/prepare a reviewable order; compare sales |
| README | Product definition and Features link, with separate MCP setup guidance |
| Claude keywords | customer-support, crm, social-media-scheduling, order-management and brand; no ranking mechanism is assumed |

Role, plan, external-payment and approval-state limitations remain. No extra channels or tool capabilities have been claimed. WebsiteURL still points to MCP setup; the README links to Features for product context. Optional localized listing overrides are omitted from the English-only candidate.

## Features page observations

Source: `evidence/features-seo.json`. Public HTTP was inspected on the review date after browser navigation timed out. That timeout provides no visual or performance score. Non-English captured labels have been translated and labeled in the repository; original route and locale identifiers remain unchanged.

| Check | Observation | Assessment |
| --- | --- | --- |
| HTTP / content | /features and /vi/tinh-nang returned 200 with headings and content in HTML | Useful crawl foundation |
| Title | Scheduled posting and multichannel inbox appear before the brand | More specific than a slogan; avoid adding keywords without a reason |
| Description | Describes tasks and channels | Clear starting point; Google may choose another snippet |
| H1 | One H1 describes the workflow | More informative than the brand alone |
| Canonical / locales | English self-canonical; English, Vietnamese and x-default alternates; separate localized metadata | Multilingual structure exists; monitor Google's selected canonical |
| Robots / sitemap | No noindex found in inspected meta/X-Robots-Tag; Features not blocked; both locale URLs in sitemap-pages | No crawl blocker observed within scope; indexing is unverified |
| Sharing | OG/Twitter metadata present | Supports link previews |
| Structured data | No application/ld+json found in inspected Features HTML | Consider accurate WebPage/BreadcrumbList after copy and scope corrections |
| Image alt | All images had alt attributes; some empty | Empty alt may be valid for decoration; inspect visually before calling it an error |

Google recommends clear titles describing the page. Meta descriptions can be used for snippets but are not guaranteed to appear. [Title links](https://developers.google.com/search/docs/appearance/title-link), [snippets](https://developers.google.com/search/docs/appearance/snippet).

## Proposed website improvements: not deployed

### 1. Define the product immediately below the main message

Explain the audience and jobs before introducing automation terms:

> TrolyPage is customer support and social media management software for small business teams. Organize customer conversations, keep CRM records, schedule posts and turn conversations into orders—with AI assistance and human review where needed.

This is proposed copy only. Avoid unmeasured claims about revenue, time savings or automatically closing every order.

### 2. Align promises with actual capabilities

The reviewed Features text limits comment management to YouTube, while the broad heading may imply all channels. Use a heading that matches current coverage and expand it when support is verified.

Describe follow-up through configured rules/schedules rather than implying the system knows when a customer is free. Align broad footer automation claims with actual channel support and approval behavior. [Reviewed page](https://trolypage.com/features).

### 3. Explain first steps for new and existing users

- Solution seekers need examples, supported channels, plan requirements and a concrete first trial.
- Plugin users need to know whether an existing workspace is required, which role/plan is eligible and what they can try after connecting.

Use specific calls to action such as trying an inbox or watching a workflow demo. Reserve MCP, OAuth and entitlement detail for setup guidance.

### 4. Organize useful content around real needs

These are intent hypotheses, without measured volume or difficulty:

| Need | Query / content ideas |
| --- | --- |
| Customer support | AI customer support; AI chatbot for Messenger; customer service chatbot |
| Inbox / CRM | shared inbox; Messenger and Zalo OA inbox; multichannel inbox; customer CRM |
| Content | social media scheduling; Facebook post scheduling; social content management |
| Orders | order management from chat; create orders from conversations |
| AI integration | customer support tools for an AI assistant; CRM MCP connector; TrolyPage MCP |

Expand existing use-case pages with examples and links from relevant feature sections. Review untranslated anchors/navigation on the English website. Create separate English pages only with useful, accurate content; avoid repetitive keyword pages or competitor names used merely to attract searches.

## Measure after release

1. Search Console: non-brand queries, impressions, clicks and CTR by locale URL, country and device; indexing and selected canonical. Compare matched conditions before/after rather than attributing changes from one day of data.
2. Directory analytics where available: views, installs/connections and the first useful action. Installs alone do not prove successful use.
3. AI routing: run discovery-prompts.json on an actual host connected to the demo workspace; record correct selection and unnecessary activation. These supplement the five positive/three negative business cases.

Finalize the product definition, resolve scope claims and measure real queries. Server, policy and reviewer-access requirements remain in 07-readiness.md.
