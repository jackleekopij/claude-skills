---
name: agent-report-annotation
description: >
  Annotate AI-assisted reports with authority tiers to signal which claims are the human author's
  own positions vs. agent-generated analysis. Use this skill whenever the user wants to add
  credibility annotations to a report, document, or analysis that was co-authored with an AI agent.
  Also trigger when the user mentions "authority tiers", "claim annotation", "who wrote what",
  "author vs AI", "human vs agent claims", "confidence tags", "annotation system",
  "signal my involvement", "which parts did I write", or wants to distinguish their own expertise
  from AI-generated analysis in any document. Use this even if the user just says something like
  "I want to show which parts are mine" or "add credibility markers" or "tag the claims".
---

# Agent Report Annotation

A system for annotating AI-assisted documents with authority tiers — signaling which claims
represent the human author's direct expertise, which they've reviewed and engaged with, and
which they're deferring to the agent's analysis.

## Why This Matters

AI-assisted reports create an epistemic problem: the reader can't tell which claims the human
author would stake their reputation on vs. which ones the AI generated and the human simply
didn't object to. This skill solves that by making the authority gradient explicit and visible.

The system is designed for documents where a human expert and an AI agent collaborate — startup
evaluations, technical assessments, research reports, due diligence documents, policy analyses.
It's not meant for purely creative writing or fiction.

## The Three Tiers

The system uses exactly three tiers. Three is the right number because it maps to genuine
epistemic states without creating false precision:

| Tier | Tag | Meaning |
|---|---|---|
| **Author** | `«Author»` | The human's own position. They have direct experience, strong conviction, or personal expertise. They would defend this claim in debate. |
| **Reviewed** | `«Reviewed»` | The human has engaged with this claim — they have relevant background, have done some verification, or have applied critical thinking. It's not their core claim but they've meaningfully evaluated it. |
| **Deferred** | `«Deferred»` | The agent did the analysis. The human has read it and it makes sense, but they haven't independently verified the underlying claims. |

Do NOT add more tiers. The temptation to add "Partially Reviewed" or "Strongly Author" creates
false precision. If the user pushes for more granularity, guide them toward the principle system
instead (see below).

## Two-Layer Structure

The annotation system has two layers that work together:

### Layer 1: Principles

Top-level beliefs that span the entire document. These are the author's macro positions that
inform multiple specific claims. Each principle gets an ID (P1, P2, etc.) and its own tier tag.

Principles should be:
- **Spanning** — they affect multiple sections of the document, not just one paragraph
- **Substantive** — they represent genuine beliefs or analytical lenses, not truisms
- **Concise** — one sentence that captures the core belief
- **Evidenced** — where possible, cite supporting evidence (prediction markets, research, data)

Example:
```
- **P1: AI coding is compressing software replication costs** «Author» — Direct experience
  building software with AI tools. Informs all cost/moat assessments in this report.
- **P2: Network effects matter more than code** «Reviewed» — Industry observation, not
  personal conviction as strong as P1.
```

Aim for 3-5 principles per document. Fewer than 3 suggests the author hasn't thought about
their macro positions. More than 5 suggests the principles aren't truly spanning.

### Layer 2: Inline Claim Tags

Specific assertions in the document body, tagged with their tier and optionally linked to a
principle. Tags use guillemet notation: `«Author · P1»`, `«Reviewed»`, `«Deferred · P3»`.

Tags are placed inline, immediately after the claim they annotate — not at the end of
paragraphs or in footnotes. The reader should be able to see the authority level of each
claim as they encounter it.

## The Workflow

### Phase 1: Extract Claims

Read the document and extract key claims in batches of 6-8. A "claim" is an assertion that
could be true or false — not a structural element, definition, or question. Focus on:

- Evaluative judgments ("the moat is weak", "the team is strong")
- Factual assertions the author may or may not have verified ("CFAA applies here")
- Predictions or risk assessments ("platform risk increases with scale")
- Recommendations ("reframe the narrative around network effects")

Present each batch to the user as a numbered list with the claim text. Wait for them to assign
tiers before continuing to the next batch. Accept typos and shorthand gracefully (e.g.,
"reviwed" = Reviewed, "def" = Deferred, "mine" = Author).

Track the claim registry as you go — a running table of all claims with their assigned tiers.

### Phase 2: Identify Principles

After 2-3 batches of claims, patterns will emerge — certain claims cluster around shared
beliefs. Propose 3-5 candidate principles to the user:

- Look for claims that share an underlying thesis
- Identify the author's strongest convictions (clusters of "Author" tier claims)
- Note analytical lenses the author applies repeatedly

Present the proposed principles and ask the user to:
1. Confirm, modify, or reject each principle
2. Assign a tier to each principle
3. Add any principles the agent missed

Then map existing claims to principles where applicable.

### Phase 3: Annotate the Document

Apply annotations in this order:

1. **Add the Authority Tiers section** — place it after the executive summary (or equivalent
   top-level summary). Include:
   - The three-tier legend table
   - The principles list with tier tags and evidence
   - A one-line explanation of the inline tag format

2. **Insert inline tags** — at each claim location in the document. Use `multi_replace_string_in_file`
   for efficiency. Place the tag immediately after the specific assertion, not at paragraph
   boundaries.

3. **Update any summary tables** — if the document has an evaluation matrix or summary table,
   add brief references to key annotated risks/claims where relevant.

Tag placement guidelines:
- Place after the **specific clause** that makes the claim, not at the end of the sentence
- For bold/emphasized claims, place the tag after the bold text: `**claim text** «Tier»`
- For bullet points, place after the first clause that asserts something
- Don't tag every sentence — tag the *claims*, not the connecting tissue

### Phase 4: User Review

After all annotations are applied, tell the user the document is ready for review. Provide
a summary:
- Total claims annotated
- Breakdown by tier (N × Author, N × Reviewed, N × Deferred)
- Number of principles
- List of any claims the user flagged for revision during extraction

## Output Format

### Authority Tiers Section (template)

```markdown
## Authority Tiers

This report was produced collaboratively between a human reviewer ([Author Name])
and an AI agent ([Agent Name]). To signal the level of human authority behind each
claim, key assertions are annotated with one of three tiers:

| Tier | Meaning |
|---|---|
| **Author** | My position. I have direct experience or strong conviction. I'd defend this. |
| **Reviewed** | I've engaged with this — relevant background, some verification, critical thinking applied. Not my core claim. |
| **Deferred** | Agent did the analysis. I've read it and it makes sense, but I haven't independently verified. |

### Guiding Principles

- **P1: [Principle text]** «[Tier]» — [Brief evidence or basis]
- **P2: [Principle text]** «[Tier]» — [Brief evidence or basis]
- **P3: [Principle text]** «[Tier]» — [Brief evidence or basis]

Inline tags appear as «Author», «Reviewed · P1», «Deferred», etc. throughout the document.
```

### Inline Tags

```markdown
The proof engine is not a durable moat «Author · P1» because...
Under CFAA and Van Buren «Deferred», EarnOS's approach...
Platform risk increases non-linearly with scale «Reviewed».
```

## Edge Cases

- **User disagrees with a claim during extraction**: Note it and offer to revise the claim
  in the document before annotating. Don't annotate claims the user has rejected.
- **Claim spans multiple sentences**: Tag the first sentence that makes the core assertion.
- **Author and agent agree strongly**: Use "Author" if the human would independently make
  the claim. The tier reflects the human's authority, not whether the agent also agrees.
- **User can't decide between Author and Reviewed**: Ask "Would you defend this in a room
  of skeptics, or would you defer to someone with deeper expertise?" Author = yes to the
  first; Reviewed = yes to the second.
- **Very long documents (50+ claims)**: Present claims in batches of 6-8, not all at once.
  The user's attention and judgment degrade with batch sizes above 8.
- **User wants to add new claims not in the document**: These should be added to the document
  first, then annotated. The annotation system reflects what's written, not what's implied.

## What This Skill Does NOT Do

- It does not evaluate the quality of the claims themselves
- It does not fact-check or verify assertions
- It does not rewrite the document (unless the user explicitly asks)
- It does not work for single-author documents with no AI involvement
- It does not replace proper citation or sourcing — it signals authority level, not evidence
