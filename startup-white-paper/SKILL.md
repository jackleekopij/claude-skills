---
name: startup-white-paper
description: >
  Write authoritative white papers for startups — the kind that make investors lean forward,
  enterprise buyers circulate internally, and founders look like the domain expert they are.
  Produces structured, research-backed documents that build a case from first principles:
  defining the problem, analysing why existing solutions fail, presenting the startup's
  approach as the logical answer, and grounding everything in market evidence and technical
  depth. Use this skill whenever the user wants to write a white paper, produce a thought
  leadership document, create a market thesis paper, write a technical white paper, build
  an investor-facing research document, draft a solution brief, or mentions "white paper",
  "thought leadership", "market thesis", "position paper", "technical brief", "solution paper",
  "industry report", or wants to turn startup analysis into a persuasive, outward-facing
  document. Also trigger when the user says "write something that makes us look credible",
  "we need a document for enterprise buyers", "help me establish authority in our space",
  or wants a long-form document that positions their startup.
---

# Startup White Paper

Write white papers that establish a startup as the authoritative voice in their domain.
A white paper is not a pitch deck (visual, brief), not a blog post (casual, short), and
not an academic paper (peer-reviewed, neutral). It is a **persuasive, well-researched,
authoritative document** (3,000–8,000 words) that builds a case from first principles
and positions the startup's approach as the logical conclusion.

## When to Use

- Startup needs a thought leadership document for their market
- Founder wants to establish credibility with enterprise buyers or investors
- Converting internal analysis or evaluation findings into an outward-facing document
- Building a market thesis paper to support fundraising
- Creating a technical white paper to attract developer/partner adoption
- Producing a solution brief for enterprise sales enablement

## Relationship to Startup Evaluator

The `startup-evaluator` skill analyses startups from an *external, critical* perspective.
This skill takes many of the same frameworks and flips the lens — building the case *from
the startup's perspective*. The evaluator's eight dimensions (problem, market, business
model, defensibility, team, technical approach, competition, traction) are exactly what a
white paper needs to address, but reframed as a persuasive narrative rather than a
diagnostic report.

If a startup evaluation already exists, use it as source material — the evaluator's
findings about strengths become the white paper's central arguments, and the evaluator's
identified risks become objections the white paper should pre-emptively address.

## Reference Library

Load references on-demand based on the type of white paper being written.

| Reference File | When to Read | Contents |
|---|---|---|
| [`references/narrative-structures.md`](references/narrative-structures.md) | Always — before writing any white paper | Narrative arc patterns, argument-building techniques, section-by-section construction, tone calibration per audience |
| [`references/audience-calibration.md`](references/audience-calibration.md) | When tailoring for a specific reader (investor, enterprise buyer, developer, regulator) | Audience-specific language, evidence hierarchies, what each reader cares about, trust signals by audience type |

**Also draw from the startup-evaluator reference library** when you need deeper framework
support for specific sections:

| Evaluator Reference | When to Read in White Paper Context |
|---|---|
| `startup-evaluator/references/foundational-frameworks.md` | Building the "Why Now?" section or articulating the problem thesis |
| `startup-evaluator/references/moats-and-defensibility.md` | Writing the competitive advantage / defensibility narrative |
| `startup-evaluator/references/unit-economics-and-growth.md` | Presenting business model viability or market economics |
| `startup-evaluator/references/ai-era-dynamics.md` | Any AI-native startup; addressing AI moat questions proactively |
| `startup-evaluator/references/adtech-and-attention.md` | AdTech or attention-economy startups |

---

## Writing Philosophy

### The Inversion Principle

The startup evaluator asks: *"Is this company credible?"*
The white paper answers: *"Here is why this approach is inevitable."*

Every VC framework the evaluator uses to probe for weakness, the white paper uses to
demonstrate strength. Thiel's contrarian question becomes the paper's thesis statement.
Graham's "why hasn't this been built before?" becomes the "Why Now?" section. Helmer's
7 Powers become the structural advantages section.

The best white papers don't *claim* authority — they **demonstrate** it by showing
analytical depth the reader hasn't seen elsewhere.

### The Three Tests

Before writing, confirm the white paper passes three tests:

1. **The "So What?" Test**: Every section must answer "so what?" for the reader. Market
   is growing? So what — what does that mean for *their* decision? Technology is novel?
   So what — what problem does that solve that couldn't be solved before?

2. **The Non-Obvious Insight Test**: The paper must contain at least one insight the
   reader is unlikely to have encountered. Restating conventional wisdom doesn't establish
   authority. The insight can be a contrarian framing, a data point, a historical analogy,
   or a structural observation about the market.

3. **The Standalone Test**: A reader with no prior knowledge of the startup should be able
   to read the white paper and (a) understand the problem domain, (b) see why current
   solutions are inadequate, (c) grasp the proposed approach, and (d) find the argument
   persuasive — all without needing to visit the startup's website or see a demo.

---

## Part 1: White Paper Types

Choose the type based on the audience and goal. Most startup white papers are type 1 or 2.

### Type 1: Market Thesis / Thought Leadership

**Purpose**: Establish the startup as the authoritative voice on a market shift.
**Audience**: Investors, press, industry analysts, potential partners.
**Core move**: Define a problem or trend that others haven't articulated clearly, then
show why the startup's approach is the natural response.

This type spends 60% of its length on the problem and market context, 30% on the approach,
and 10% on the company. The company almost emerges as a footnote — "of course someone
would build this, and here's who."

**When to use**: Fundraising, PR, conference talks, analyst briefings.

### Type 2: Solution / Technical White Paper

**Purpose**: Convince technical buyers or partners that the approach is sound.
**Audience**: CTOs, engineering leads, technical evaluators, developers.
**Core move**: Demonstrate technical depth and architectural thinking that the reader
can verify. Show you understand the tradeoffs, not just the benefits.

This type spends 30% on the problem, 50% on the technical approach (architecture,
methodology, benchmarks), and 20% on results and implications.

**When to use**: Enterprise sales, developer adoption, technical partnerships.

### Type 3: Industry / Problem Analysis

**Purpose**: Educate the market about a problem they may not know they have.
**Audience**: Business decision-makers, department heads, procurement teams.
**Core move**: Quantify the cost of the status quo. Make the implicit explicit — show
the reader what their current approach is actually costing them in money, time, or risk.

This type spends 70% on problem analysis with data, 20% on solution requirements (not
*your* solution — the abstract requirements), and 10% on a call to action.

**When to use**: Category creation, market education, inbound content marketing.

### Type 4: Case Study / Results Paper

**Purpose**: Prove the approach works with real-world evidence.
**Audience**: Prospective customers, investors evaluating traction.
**Core move**: Let the results speak. Specific numbers, named customers (with permission),
before/after comparisons, and honest discussion of what didn't work initially.

This type spends 20% on context, 50% on the case study with specifics, and 30% on
generalised learnings and implications.

**When to use**: Sales enablement, investor updates, proof-of-concept proposals.

---

## Part 2: The Interview

Before writing, gather the information needed to produce a credible white paper. Don't
start writing with gaps — they show.

### Essential Information

1. **Who is the primary reader?** (Investor, enterprise buyer, developer, regulator, general
   audience) — this determines tone, evidence type, and structure.
2. **What should the reader do after reading?** (Book a demo, invest, adopt the API,
   share internally, change their mental model of the market) — this determines the
   call to action and where the argument lands.
3. **What is the startup's core thesis?** The single contrarian or non-obvious belief that
   the company is built on. (Thiel: "What important truth do few people agree with you on?")
4. **What evidence exists?** Data, case studies, benchmarks, customer testimonials, market
   research, published studies. The strength of the evidence determines the paper's
   assertiveness — don't make claims that outrun the evidence.
5. **Who are the competitors, and what do they get wrong?** Not for the purpose of
   attacking them — for the purpose of showing that the market's current approach has a
   structural flaw that the startup's approach resolves.
6. **What is the "Why Now?"** — the technology shift, regulatory change, behavioural change,
   or cost curve crossing that makes this approach newly viable. (Sequoia test)
7. **Are there existing evaluations or analyses?** If a startup-evaluator report exists,
   use it as source material.
8. **What is the target length and format?** Print-ready PDF? Web page? Both?

### Optional but Valuable

- Industry data or analyst reports the startup has access to
- Founder's own writing, talks, or interviews (for voice matching)
- Competitor white papers or marketing (to differentiate positioning)
- Regulatory or compliance context that shapes the market
- Technical architecture diagrams or methodology details (for Type 2)

---

## Part 3: Structure & Construction

### Universal Structure

Every white paper, regardless of type, follows this narrative arc. Section lengths vary
by type (see Part 1), but the sequence is fixed because it mirrors how persuasion works:
establish shared reality → reveal the gap → present the resolution.

```
1. Executive Summary (half-page)
2. The Problem / State of Play
3. Why Current Approaches Fall Short
4. Why Now — What Changed
5. The Approach / Framework / Solution
6. Evidence & Validation
7. Implications & Path Forward
8. About [Company]
```

### Section-by-Section Construction

#### 1. Executive Summary

Write this last. Half a page. Three elements:
- The core problem in one sentence
- The key insight (what everyone else is missing) in one sentence
- What this paper demonstrates in one sentence

Do not front-load the company or product. The executive summary is about the *thesis*,
not the company.

#### 2. The Problem / State of Play

This is where the evaluator's framework pays off. Apply Paul Graham's well/puddle test
but in reverse — instead of asking "is this a real problem?", *demonstrate* that it is by
showing the depth and urgency of the pain.

**Construction pattern:**
- Open with a concrete, specific scenario that illustrates the problem (a named persona,
  a real situation, a data point that lands)
- Zoom out to the systemic version of the problem
- Quantify the cost: money, time, risk, missed opportunity
- Establish that this isn't a niche complaint — anchor the problem's scope with credible
  data (industry reports, public filings, survey data)

**Common mistakes to avoid:**
- Starting with market size ("The global X market is $Y billion"). Boring and tells
  the reader nothing about the *problem*.
- Using jargon before establishing the problem in plain language
- Describing the problem in terms of the solution ("The problem is that companies don't
  have an AI-powered X") — the problem exists independently of the solution

#### 3. Why Current Approaches Fall Short

This is not a competitor teardown. It is a structural analysis of *why the category's
current paradigm fails*. The most persuasive white papers don't name competitors — they
describe the *approach* that competitors share and show why that approach has inherent
limitations.

**Construction pattern:**
- Identify the dominant paradigm (how the industry currently solves this problem)
- Show the structural limitation of that paradigm — not "their product is bad" but
  "this approach *cannot* scale / adapt / deliver X because of [architectural reason]"
- Use Christensen's disruption lens if applicable: is the incumbent approach over-serving
  some customers while under-serving others?
- Acknowledge what current approaches get right — this builds credibility and prevents
  the reader from dismissing the analysis as biased

#### 4. Why Now — What Changed

Directly apply the Sequoia "Why Now?" framework. The reader needs to understand why this
paper is relevant *today* and not five years ago or five years from now.

**Valid "Why Now?" catalysts:**
- Technology shift (new capabilities, cost curves crossing thresholds)
- Regulatory change (new requirements, old barriers removed)
- Behavioural change (how users/buyers/industries have shifted)
- Market structure change (consolidation, unbundling, platform shifts)
- Data availability (new data sources, new ways to collect/process data)

Each catalyst should be specific and verifiable. "AI is changing everything" is not a
Why Now. "GPT-4-class models reduced the cost of document analysis from $12/page
(human analyst) to $0.03/page (AI), crossing the threshold where automated compliance
review becomes cheaper than manual" — that's a Why Now.

#### 5. The Approach / Framework / Solution

Now — and only now — introduce the startup's approach. The preceding sections have built
the case; this section delivers the resolution.

**Construction pattern:**
- State the core insight or principle that the approach is built on (Thiel's "secret" —
  what does the startup believe that others don't?)
- Explain the approach at the conceptual level before going to implementation
- For Type 2 (technical): include architecture, methodology, key design decisions and
  *why* those decisions were made (trade-offs acknowledged, not hidden)
- For Type 1 (market thesis): focus on the framework or model that explains the market
  shift, with the product as an embodiment of that model
- Connect each feature/capability back to a problem identified in Section 2 — every
  capability should resolve a previously established pain point

**Tone calibration:**
- Authoritative, not promotional. "Our platform does X" reads as marketing. "This
  approach enables X because of [structural reason]" reads as expertise.
- Acknowledge trade-offs. "This approach optimises for X at the cost of Y, which is the
  right trade-off because [reason]" is more credible than "this approach is better in
  every way."
- Use the evaluator's defensibility frameworks (Helmer's 7 Powers, NFX network effects)
  to explain *why* the approach has structural advantages — but weave them into the
  narrative naturally, not as academic citations.

#### 6. Evidence & Validation

Match evidence type to audience (read `references/audience-calibration.md` for details):

- **Investors**: Market data, growth metrics, comparable exits, unit economics trajectory
- **Enterprise buyers**: Case studies, ROI calculations, integration evidence, security/
  compliance certifications
- **Developers**: Benchmarks, architectural transparency, code samples, API documentation
  quality
- **General audience**: Customer stories, before/after comparisons, industry endorsements

**Evidence hierarchy (strongest to weakest):**
1. Named customer results with specific numbers
2. Aggregate anonymised data across multiple deployments
3. Independent benchmark or third-party validation
4. Internal benchmarks with transparent methodology
5. Analyst/expert endorsement
6. Logical argument from first principles

Don't stretch evidence. If the startup is pre-revenue, say so and lean on
first-principles arguments and prototype results. Overstating evidence destroys
credibility faster than admitting early stage.

#### 7. Implications & Path Forward

Where is this going? What does the future look like if the thesis is correct?

**Construction pattern:**
- Restate the thesis in light of the evidence presented
- Describe the near-term implications (12-18 months) — concrete and specific
- Describe the medium-term implications (3-5 years) — directionally correct, more speculative
- End with a clear call to action appropriate to the audience

#### 8. About [Company]

Keep this short — three to four sentences. The white paper has already demonstrated
the company's depth. This section exists for readers who want to know who's behind it.
Include founding year, team background (one sentence), stage/funding if relevant, and
how to get in touch.

---

## Part 4: Tone & Voice

### The Expertise Spectrum

White paper tone sits between two poles:

| Too Academic | Sweet Spot | Too Promotional |
|---|---|---|
| "Our research indicates a statistically significant correlation between..." | "We found that companies using approach X see 3x faster deployment — here's why." | "Our revolutionary AI-powered platform transforms..." |

The sweet spot is **confident expertise**: the voice of someone who has deep knowledge,
shares it generously, and doesn't need to oversell because the analysis speaks for itself.

### Voice Principles

1. **Declarative over hedging.** "This approach works because..." not "We believe this
   approach may potentially work because..." Hedging signals uncertainty. If you're
   uncertain, either find more evidence or explicitly flag the uncertainty ("This is early
   data, but the signal is clear").

2. **Specific over general.** "Processing time dropped from 4.2 hours to 11 minutes" not
   "dramatically reduced processing time." Numbers, names, specifics — these are what
   separate a white paper from a blog post.

3. **Structural over anecdotal.** Don't just say "our approach is better" — show *why it's
   structurally better*. Use the evaluator's frameworks: is it a counter-positioning
   advantage (Helmer)? A network effect (NFX)? A cost curve crossing?

4. **Generous over gatekeeping.** Share genuine insight, not teasers. "Our methodology
   uses X, Y, Z approach and here's why each matters" builds trust. "Contact us to learn
   about our proprietary methodology" feels like marketing.

5. **Match the founder's voice.** If you have access to the founder's writing or speaking
   style, calibrate. A technical founder's white paper should feel technical. A
   business-focused founder's paper should feel strategic. Don't impose a voice that
   doesn't match who would credibly have written this.

---

## Part 5: Pre-Flight Checklist

Before delivering the final draft, verify:

### Structural Checks
- [ ] Executive summary can be read standalone and the thesis is clear
- [ ] Each section answers "so what?" for the target reader
- [ ] Problem section does not mention the solution
- [ ] "Why Now?" is specific and verifiable, not generic
- [ ] Solution section connects each capability to a previously identified problem
- [ ] Evidence matches the audience type (see audience calibration)
- [ ] Call to action is clear and appropriate

### Credibility Checks
- [ ] No claims without supporting evidence or explicit flagging as thesis
- [ ] Trade-offs acknowledged, not hidden
- [ ] Competitors addressed structurally, not by name (unless there's a specific reason)
- [ ] Technical claims are precise and verifiable
- [ ] Data sources cited or citable
- [ ] Consistent terminology throughout (no "platform" in one place and "solution" in
      another for the same thing)

### Tone Checks
- [ ] No promotional language ("revolutionary", "game-changing", "best-in-class")
- [ ] No unnecessary hedging ("we believe", "we think", "potentially")
- [ ] Jargon defined on first use or avoided
- [ ] Active voice throughout (passive voice is a sign of hedging)
- [ ] The paper could be read aloud at a conference without embarrassment

### Format Checks
- [ ] 3,000–8,000 words (shorter papers lack depth; longer papers lose readers)
- [ ] Clear visual hierarchy (headings, subheadings, callout boxes for key data)
- [ ] Figures/tables have titles and source citations
- [ ] Page/section breaks fall at natural transition points

---

## Part 6: Post-Draft Refinement

Follow the same refinement workflow as the startup evaluator, adapted for white papers:

### Step 1: Author Review

Present the draft to the human author. They will correct factual errors, add insider
context, adjust tone, and flag where the argument is weak. Apply corrections before
continuing.

### Step 2: Framework Gap Analysis

Re-read the draft against the evaluator's framework library. For each major claim, ask:
"Did I ground this in a recognised framework, or is it floating as unsupported assertion?"

Common gaps:
- "Why Now?" section without a specific catalyst tied to a verifiable shift
- Defensibility claims without structural reasoning (Helmer/NFX)
- Market sizing without bottom-up validation
- Technical claims without architectural specifics
- Competitive positioning without structural analysis of why the incumbent paradigm fails

### Step 3: The Hostile Reader Pass

Read the paper as someone who *wants* to poke holes. For every claim, ask:
- "How would a sceptical CTO respond to this?"
- "What would a competitive analyst highlight as weak?"
- "Where would an investor push back?"

Strengthen or pre-empt the weakest points. The goal isn't to eliminate all objections —
it's to show that the author has already considered them.

### Step 4: Authority Tier Annotation

If the white paper is co-authored with an AI agent and will be published externally,
apply the `agent-report-annotation` skill to tag claims by authority level. The founder
assigns tiers; the agent applies them. This maintains intellectual honesty about which
analysis is the founder's own and which is agent-generated.

### Step 5: Brevity Pass

White papers accumulate padding across editing rounds. Cut ruthlessly:
- Sentences that restate the previous sentence in different words
- Qualifiers that add no information ("very", "really", "quite")
- Sections that exist because "a white paper should have X" but don't serve the argument
- Data points that are interesting but don't advance the thesis
