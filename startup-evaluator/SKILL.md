---
name: startup-evaluator
description: >
  Evaluate startups with the rigor of a top-tier VC — covering value proposition, market,
  team, defensibility, unit economics, technical approach, and website/content quality.
  Synthesizes classic frameworks (Sequoia, YC, a16z, NFX) with AI-era considerations
  into structured, actionable reports. Use this skill whenever the user wants to evaluate
  a startup, review a pitch deck, analyze a company's website or positioning, assess a
  business model, do due diligence on a startup, review founder materials, critique an
  adtech/SaaS/marketplace/AI company, or mentions "startup review", "business analysis",
  "evaluate this company", "what do you think of this startup", "review this pitch",
  "due diligence", or shares a startup's website asking for feedback. Also trigger when
  the user wants to write a report for a founder, prepare investor notes, or compare
  a startup against its competitive landscape.
---

# Startup Evaluator

Evaluate startups using battle-tested VC frameworks, adapted for the AI era (2024–2026+).
This skill produces structured, actionable reports that are simultaneously human-readable
and agent-executable.

## When to Use

- Evaluating a startup idea, pitch deck, or website
- Writing a peer review or investor memo
- Assessing business model viability, unit economics, or defensibility
- Reviewing startup content/copy for clarity and persuasiveness
- Comparing a startup against competitive alternatives
- Any "what do you think of this company" request

## Reference Library

This skill includes deep reference files with extracted key concepts from canonical
sources. The SKILL.md body contains the evaluation framework — the references contain the
*why* behind each framework, with specific questions, application guides, and benchmarks.

**Read these on-demand, not upfront.** Load only the reference(s) relevant to the
dimension you're going deep on.

| Reference File | When to Read | Key Sources |
|---|---|---|
| [`references/foundational-frameworks.md`](references/foundational-frameworks.md) | Evaluating problem quality, idea validity, team, competition, PMF status | Paul Graham, Peter Thiel, Clayton Christensen, Eric Ries, Michael Porter, Marc Andreessen, Andy Rachleff |
| [`references/moats-and-defensibility.md`](references/moats-and-defensibility.md) | Deep-diving on Dimension 4 (Defensibility) or Dimension 7 (Competition) | Warren Buffett, Hamilton Helmer (7 Powers), NFX Network Effects Manual |
| [`references/unit-economics-and-growth.md`](references/unit-economics-and-growth.md) | Evaluating Dimension 3 (Business Model) or Dimension 8 (Traction); assessing revenue quality, marketplace economics, or SaaS metrics | Sam Altman, Bill Gurley, YC growth framework, Andrew Chen |
| [`references/ai-era-dynamics.md`](references/ai-era-dynamics.md) | Any startup using AI as a core product component; assessing AI moats, wrapper risk, or cost dynamics | a16z "Who Owns the Generative AI Platform", NFX 5-Layer Stack, AI cost curves |
| [`references/adtech-and-attention.md`](references/adtech-and-attention.md) | Any advertising, attention economy, or reward/incentive-based business | Herbert Simon, Tim Wu, Shoshana Zuboff, adtech business models, fraud analysis |

**Usage pattern:** When writing a dimension's analysis, check whether you need deeper
framework support. If so, read the relevant reference file *before* writing that section.
For instance, if you're evaluating a reward-based adtech startup's defensibility, read
both `moats-and-defensibility.md` AND `adtech-and-attention.md`.

## Evaluation Philosophy

Good startup evaluation is **not a checklist** — it's pattern recognition informed by
frameworks. The frameworks below are lenses, not scorecards. A startup can fail every
"rule" and still succeed (Airbnb looked insane on paper). The goal is to identify the
**specific risks and leverage points** for *this* company, not to grade it generically.

Two meta-principles from the best VCs:

1. **Paul Graham's Well Test**: Does a small number of people want this *a lot*, or do
   many people want it *a little*? Nearly all good startup ideas are narrow-and-deep
   wells, not broad-and-shallow puddles. A social network for pet owners sounds plausible
   but fails — nobody urgently needs it. Stripe succeeded because thousands of programmers
   were desperate for better payment processing.

2. **Sequoia's "Why Now?" Test**: The best companies have a clear answer to "why hasn't
   this been built before?" — a technology shift, regulatory change, behavioral change,
   or cost curve crossing that makes the solution newly viable. If there's no why-now,
   either it's been tried and failed, or the market doesn't need it yet.

---

## Part 1: The Eight Evaluation Dimensions

For each dimension, assess the startup and assign a qualitative signal:
**Strong**, **Promising**, **Uncertain**, or **Concerning**. Not every dimension matters
equally for every company — call out which 2-3 are make-or-break for this specific startup.

### 1. Problem & Value Proposition

The foundation. If this is wrong, nothing else matters.

**Questions to answer:**
- Does the problem genuinely exist, or is it a "made-up" / "sitcom" idea? (PG: "Would you
  use this yourself if you hadn't built it?")
- Who has this problem *right now*, and how urgently?
- How are they solving it today? What's broken about current solutions?
- Can you state the value prop in one declarative sentence? (Sequoia test)
- Is the value prop **unique and compelling**, or is it "we do X but slightly better"?

**Red flags:**
- The problem description is about the solution, not the pain
- "Everyone" is the target customer (broad-shallow puddle)
- The current solution is "nothing" — sometimes this means there's no real pain
- Value prop requires lengthy explanation

**For adtech/marketplace startups specifically:**
- Two-sided value props must be compelling on BOTH sides
- Advertiser side: what proof of ROI do they get that they can't get elsewhere?
- Consumer side: is the value exchange fair and sustainable? Does the user genuinely
  benefit, or is this attention extraction dressed up as a reward?

### 2. Market & Timing

**Questions to answer:**
- TAM/SAM/SOM — but more importantly, is the market growing, and why?
- **Why now?** What changed to make this possible/necessary? (Technology, regulation,
  behavior, cost curve)
- Is this a market the startup can *credibly* enter and grow within?
- Is the market big enough to build a venture-scale business ($1B+ outcome)?
- Are there adjacent markets to expand into (path out of the initial niche)?

**AI-era considerations (2024–2026):**
- AI is compressing timelines — markets that took 5 years to develop now mature in 18 months
- AI-enabled companies can operate with 10x smaller teams, changing the economics of
  market entry
- "AI wrapper" risk: if the core product is a thin UI over an LLM API, the moat is paper-thin
- Data advantages still matter but asymptote faster than expected — a model that's 10%
  better often isn't distinguishable to users (NFX insight)
- Incumbents are integrating AI features fast — the window for AI-native startups to
  establish position is narrow

**For adtech specifically:**
- Global digital ad spend is ~$700B+ and growing, but highly concentrated (Google, Meta)
- Attention economy dynamics: human attention is finite and increasingly contested
- Privacy regulation (GDPR, CCPA, cookie deprecation) is reshaping targeting — this
  creates "why now?" for privacy-respecting alternatives
- Reward/incentive-based advertising is a growing niche but has historical challenges
  (fraud, quality of engagement)

### 3. Business Model & Unit Economics

**Questions to answer:**
- How does the company make money? Is the revenue model clear?
- What are the unit economics? (CAC, LTV, LTV:CAC ratio, payback period)
- At what scale do the economics become attractive?
- Gross margins — software (70-90%) vs services (30-50%) vs marketplace (10-20% take rate)?
- Is there a path to profitability, or is this a "grow now, monetize later" bet?

**Key frameworks:**
- **Sam Altman's Unit Economics Test**: "It never makes sense to take 80 cents from a
  customer and hand them a dollar back." If unit economics are negative, growth just
  accelerates cash burn.
- **Marketplace rake analysis**: For two-sided businesses, the take rate must be high enough
  to build a business but low enough that both sides feel the value exchange is fair.
- **Revenue quality**: Recurring > transactional > one-time. Contractual > voluntary churn.
- **Revenue quality position (Gurley)**: Place the startup's revenue in Gurley's quality
  hierarchy — recurring vs transactional, moat-protected vs exposed, diversified vs
  concentrated, organic vs subsidized. Revenue in the lower half of the hierarchy needs
  a credible path to structural improvement, not just growth. See
  `references/unit-economics-and-growth.md` for the full hierarchy.

**AI-era considerations:**
- AI inference costs are a real COGS item — margins of 50-60% are common in AI apps
  (vs 80-90% for traditional SaaS)
- Inference costs are falling ~50% per year — today's margin pressure may resolve naturally
- AI enables much smaller teams → lower operating costs → potentially faster path to
  profitability

### 4. Defensibility & Moat

The hardest dimension to assess for early-stage companies, but the most important for
long-term value.

**The four classic moats (NFX/Buffett):**
1. **Network effects**: Does the product get better as more people use it? (Strongest moat)
2. **Switching costs / Embedding**: Once adopted, is it painful to leave?
3. **Scale economies**: Does the company get cheaper to operate at scale?
4. **Brand**: Does the company own mindshare in its category?

**Additional moats:**
- **Data flywheel**: Does usage generate proprietary data that improves the product?
- **Regulatory / compliance**: Is there a licensing or compliance barrier?
- **Ecosystem / platform**: Does the company sit at a nexus that others build on?

**AI-era moat assessment (critical):**
- a16z's finding: "There don't appear, today, to be any systemic moats in generative AI."
  Apps use similar models, models train on similar data, clouds run similar GPUs.
- **Standard moats still apply**: Scale (capital), supply chain (GPU access), ecosystem,
  distribution, algorithmic cleverness. But none are inherently durable.
- The strongest AI-era moats come from: **proprietary data flywheels**, **workflow embedding**
  (becoming part of the customer's daily process), and **vertical integration** (owning the
  model + the app).
- Hyperlocal/proprietary data at NFX's "Layer 3" is the most defensible data position
- Human perception limits matter: once AI output quality exceeds human discrimination
  thresholds, further quality improvements don't create moat

**Red flags:**
- "Our moat is our technology" (technology alone is rarely a durable moat)
- "First mover advantage" (often a myth — Google wasn't the first search engine)
- No answer to "what stops Google/Meta from building this?"
- **Disintermediation at high take rates:** For marketplace or intermediary businesses,
  per Gurley's "A Rake Too Far," take rates above 20-25% create strong economic incentive
  for participants to route around the platform. Ask: "At your take rate, what stops the
  two sides from going direct once they've been introduced?" If the platform's primary
  value is the initial match (not ongoing services), disintermediation risk is high.

### 5. Team

**Questions to answer:**
- Do the founders have domain expertise relevant to the problem?
- Have they built and shipped products before?
- Is the team technically capable of executing their vision?
- Founder-market fit: are they the right people to solve *this* problem?
- Do they seem honest, clear-thinking, and resilient?

**What to look for:**
- **Organic idea**: Did the idea grow from the founders' own experience, or was it
  manufactured? (PG: "The verb you want to be using with respect to startup ideas is not
  'think up' but 'notice.'")
- **Speed of iteration**: How fast are they learning and shipping?
- **Intellectual honesty**: Do they acknowledge weaknesses, or do they spin everything?

**What you can assess from public materials:**
- Clarity of communication (if they can't explain it clearly, they may not understand it)
- Technical depth (do they understand their own stack, or is it buzzword soup?)
- Vision coherence (do the pieces fit together into a logical whole?)

### 6. Technical Approach & Novelty

**Questions to answer:**
- Is the technical approach sound? Does it solve the stated problem?
- What's genuinely novel vs. off-the-shelf technology?
- Is the technology appropriately scoped, or is it over-engineered for the current stage?
- Are there technical risks that could block execution?
- How does the architecture support scalability?

**AI-era technical assessment:**
- **Build vs. buy for AI**: Are they training custom models (expensive, slow, but defensible)
  or using APIs (fast, cheap, but commoditized)?
- **Data pipeline quality**: The boring data engineering is often more important than the
  flashy model
- **Evaluation methodology**: How do they measure whether their AI actually works? Startups
  that can't articulate their eval approach are flying blind
- **AI safety and alignment considerations**: For consumer-facing AI, what are the failure
  modes and how are they handled?

**For adtech/engagement platforms:**
- How is engagement/attention measured? Is it gameable?
- What fraud prevention mechanisms exist?
- How is user data handled? Privacy architecture matters.
- Is the matching/targeting approach actually better than incumbent solutions?

### 7. Competition & Positioning

**Questions to answer:**
- Who are the direct competitors? Indirect competitors?
- What's the startup's thesis about what everyone else is overlooking? (PG: "You have to
  be able to phrase it in terms of something the incumbents are overlooking.")
- Is the market crowded (good — means demand exists) or empty (could mean no demand)?
- Can the startup win a beachhead that expands into the broader market?

**How to frame competition analysis:**
- YC: "Startup companies always die of suicide not murder." Competitors matter less than
  most founders think.
- BUT: "What stops the incumbent from adding this as a feature?" is a legitimate question
  for AI-era startups specifically
- Look for **asymmetric advantages**: things the startup can do that incumbents structurally
  can't (or won't, due to incentive misalignment)

### 8. Traction & Evidence

**Questions to answer:**
- What evidence exists that this works? (Users, revenue, LOIs, pilots, waitlist)
- Is growth organic or paid? (Organic > paid for signal quality)
- Retention: are users coming back? (Retention > acquisition for signal quality)
- What stage is the company at, and is the evidence appropriate for that stage?

**For marketplace/platform startups — split-signal PMF:**
Assess PMF separately for each side using Seibel's spectrum. A marketplace at Level 4 on
the paying side (customers spending real money) but Level 2 on the supply side (early
usage, retention unknown) has a fragile foundation — the paying side's PMF depends on
the supply side retaining. Call out the split explicitly rather than blending it into a
single signal.

**Calibrating expectations by stage:**
- Pre-seed: An idea, maybe a prototype. Evidence = founder credibility + market signal
- Seed: MVP with early users. Evidence = usage data, qualitative user feedback
- Series A: Product-market fit signals. Evidence = retention curves, unit economics
- Beyond: Scaling what works. Evidence = growth rate, margin improvement

---

## Part 2: Website & Content Review

When reviewing a startup's website or marketing materials, evaluate through three reader
lenses simultaneously:

### The Customer Lens
- Can I understand what this product does within 10 seconds?
- Is the benefit to me (the customer) immediately clear?
- Do I trust this company? (Social proof, credibility signals, design quality)
- Is there a clear call to action? Do I know what to do next?
- Does the language speak to my pain, or is it generic marketing speak?

### The Investor Lens
- Is the market opportunity clear?
- Does the team seem credible?
- Is there evidence of traction?
- Is the business model understandable?
- Does the messaging signal a big outcome?

### The Advertiser/Partner Lens (for B2B2C or marketplace models)
- Is the value prop for *my* business clear?
- What proof of ROI is offered?
- How does this integrate with my existing workflows?
- What's the pricing model?
- Are there case studies or testimonials from companies like mine?

### Content Quality Checklist
- [ ] Hero section communicates the core value prop in ≤10 words
- [ ] No jargon without explanation on first use
- [ ] Social proof present and credible (logos, numbers, testimonials)
- [ ] Clear information hierarchy (most important → least important)
- [ ] No redundant/overlapping sections (common on startup sites)
- [ ] Mobile-responsive and performant
- [ ] CTA is prominent and repeated at natural decision points
- [ ] Consistent tone and messaging across pages
- [ ] Technical claims are substantiated, not hand-wavy
- [ ] Pricing/business model is transparent (or there's a clear reason it's not)

---

## Part 3: Report Format

Structure the output as a single Markdown document that serves three audiences:
the founder (strategic insights), a human reviewer (readable narrative), and an AI agent
(parseable, actionable).

### Report Template

```markdown
# [Company Name] — Startup Evaluation Report
> Prepared by [Author] · [Date]
> **Overall Signal: [Strong / Promising / Mixed / Concerning]**

## Executive Summary
<!-- 3-5 sentences. The single most important insight first. -->

## Evaluation Matrix

| Dimension | Signal | Key Insight |
|---|---|---|
| Problem & Value Prop | [signal] | [one line] |
| Market & Timing | [signal] | [one line] |
| Business Model & Unit Economics | [signal] | [one line] |
| Defensibility & Moat | [signal] | [one line] |
| Team | [signal] | [one line] |
| Technical Approach | [signal] | [one line] |
| Competition & Positioning | [signal] | [one line] |
| Traction & Evidence | [signal] | [one line] |

## Detailed Analysis

### 1. Problem & Value Proposition
<!-- Analysis using framework from Part 1 -->

### 2. Market & Timing
<!-- ... -->

### 3. Business Model & Unit Economics
### 4. Defensibility & Moat
### 5. Team
### 6. Technical Approach & Novelty
### 7. Competition & Positioning
### 8. Traction & Evidence

## Website & Content Review
<!-- Analysis using Part 2 framework -->

### What Works
### What Needs Improvement
### Specific Content Issues
<!-- List redundancies, unclear sections, missing elements -->

## Paths to Success
<!-- 2-4 plausible scenarios where this company wins big -->

## Paths to Failure
<!-- 2-4 realistic failure modes with leading indicators -->

## Appendix: Actionable Recommendations

<!-- Each recommendation is a standalone, agent-executable task -->

### Recommendation 1: [Title]
- **Problem:** [What's wrong / what's missing]
- **Impact:** [High / Medium / Low]
- **Effort:** [High / Medium / Low]
- **Suggested fix:** [Human-readable description]
- **Agent instruction:** |
  [Precise, self-contained instruction that an AI agent can execute directly.
   Include context, constraints, and acceptance criteria.
   Reference specific files, pages, or sections where applicable.]

### Recommendation 2: [Title]
...
```

### Writing the Report

**Tone**: Candid but constructive. This is a friend reviewing a friend's company — be
honest about weaknesses but frame them as opportunities. Assume the founder is smart and
receptive.

**Concreteness over generality**: "Your hero section says 'Revolutionizing advertising'
which tells me nothing — consider 'Brands pay you to try products you'll actually like'"
is 10x more useful than "Your messaging could be clearer."

**Agent instructions should be**:
- Self-contained (an agent reading only that block should be able to execute)
- Specific about inputs, outputs, and acceptance criteria
- Scoped to a single task (one instruction = one PR / one change)
- Include relevant context the agent would need (e.g., "The website is built with Next.js
  and deployed on Vercel" if known)

---

## Part 4: Special Considerations by Vertical

### AdTech / Attention Economy Startups

The advertising industry has specific dynamics worth calling out:

**The fundamental tension**: Advertisers want proof of ROI. Users want to not be annoyed.
Platforms want engagement. Any adtech startup must resolve this three-way tension.

**Reward-based / incentive advertising models**:
- Historical challenge: users game the system for rewards without genuine engagement
- The quality-of-attention problem: did the user actually absorb the message, or did they
  click through mindlessly to get the reward?
- Regulatory considerations: FTC guidelines on endorsements, sweepstakes law, money
  transmission (if paying users)
- Fraud vectors: bot farms, click fraud, fake accounts, collusion
- Success hinges on proving that reward-driven engagement converts to actual purchases
  at a rate that justifies the advertiser's spend

**Unit economics for reward-based advertising**:
- The math: Advertiser pays X per engagement → Platform takes Y cut → User receives Z reward
- For this to work: X > Y + Z AND the advertiser's conversion rate from this engagement
  must exceed their alternative channels (Google/Meta ads)
- Key question: is the per-user value high enough to fund meaningful rewards while leaving
  margin for the platform?

### AI-Native Startups

**The wrapper test**: Strip away the AI. What's left? If the answer is "a nice UI," the
company is vulnerable to both the underlying model provider adding that UI and to any
competitor building the same wrapper.

**Vertical > horizontal in AI apps**: Companies that deeply understand one domain and
embed AI into a complete workflow (data pipeline + model + UX + domain logic) tend to
outperform generic AI tools.

### Marketplace / Platform Startups

**Chicken-and-egg**: Which side do you get first? The answer is almost always: manually
recruit the supply side, then let demand follow.

**Liquidity**: A marketplace is only valuable when there's enough supply and demand that
matches happen reliably. Before liquidity, the experience is frustrating for both sides.

**Disintermediation risk**: Once buyer and seller connect, what stops them from going
direct? The platform must provide ongoing value (trust, convenience, quality assurance,
payment processing).

---

## Research Methodology

When evaluating a startup, gather information in this order:

1. **Website deep-read**: Every page, not just the homepage. Look for consistency,
   completeness, and clarity.
2. **Product demo/trial**: If available. Nothing beats hands-on experience.
3. **Competitive landscape**: Search for direct and indirect competitors. Check Crunchbase,
   PitchBook, or public databases for funding data.
4. **Market data**: Industry reports, market size estimates, growth trends.
5. **Team research**: LinkedIn, prior companies, public talks/interviews.
6. **Technical claims verification**: Can the claimed technology actually do what they say?
   Check for patents, published research, open-source contributions.
7. **User/customer feedback**: Reviews, social media mentions, community forums.
8. **Structural precedent search**: For every high-risk dimension, actively search for a
   historical company that faced the same structural dynamic — even if it's in a different
   industry. The goal isn't exact comparison but structural analogy: "Company X also sat
   as an intermediary between users and platforms without platform consent — what happened?"
   One well-chosen precedent (with specific outcomes: user loss, lawsuits, policy changes)
   is worth more than three paragraphs of abstract risk analysis.

Not all of this will be available for every evaluation. Work with what you have and
flag what's missing.

---

## Part 5: Post-Draft Refinement Workflow

The initial draft is never the final report. The following sequence has been validated
across multiple evaluations and produces materially better output than a single-pass draft.

### Step 1: Author Review & Corrections

Present the draft to the human author. They will flag factual errors, missing context
(they often know the founder, the industry, or the competitive landscape better than
publicly available materials reveal), tone issues, and areas where the analysis overstates
or understates risk. Apply corrections before proceeding.

### Step 2: Framework Gap Analysis

Re-read the completed draft against the reference library for each dimension. For each
dimension, ask: "Did I apply the relevant framework, or did I rely on generic analysis?"

Common gaps that surface on second pass:
- Defensibility section that doesn't reference Helmer's 7 Powers or NFX network effects
- Unit economics section that doesn't place revenue in Gurley's quality hierarchy
- Traction section that doesn't assess PMF using Seibel's spectrum (especially split-signal
  for marketplace/platform startups)
- Competition section that lacks a structural precedent for the highest-risk dynamic
- Market section without a concrete "why now?" tied to a technology/regulatory/behavioral
  shift

For each gap found, draft a specific addition with the framework citation integrated
naturally — not as an academic reference but as an analytical lens that sharpens the insight.
Propose additions to the author before applying.

### Step 3: Key Assumptions

Extract the 3-5 critical assumptions the analysis rests on — things that, if wrong, would
materially change the conclusions. Present only assumptions that are:
- **Non-obvious** — the reader might not realise they're assumed
- **Testable** — the founder could verify or refute them with data they have
- **Material** — if wrong, at least one dimension's signal would change

Place these after the Executive Summary in a "Key Assumptions" section. Each assumption
should state: what we assumed, where it affects the analysis, and what changes if it's wrong.

### Step 4: Authority Tier Annotation (if co-authoring)

If the report is co-authored with an AI agent, apply the `agent-report-annotation` skill
to tag claims by authority level (Author / Reviewed / Deferred) and extract guiding
principles. This step is the author's responsibility — they assign tiers, the agent applies
them. Do not skip this for reports that will be shared externally.

### Step 5: Brevity & Consistency Pass

After multiple editing rounds, reports accumulate repetition. Search for:
- Key phrases or arguments restated in multiple sections
- Framework names or data points repeated more than 3 times
- Sections that substantially duplicate analysis from other sections

The fix is cross-referencing ("as analysed in Section 7") rather than deletion — the first
full telling stays, subsequent mentions become brief references.
