# AI-Era Dynamics — Deep Reference

Consult this file when evaluating any startup that uses AI as a core component of its
product, or when assessing how AI shifts the competitive landscape for a non-AI startup.
Especially relevant for Dimensions 4 (Defensibility), 6 (Technical Approach), and 2
(Market & Timing).

## Table of Contents
1. [a16z — Who Owns the Generative AI Platform?](#a16z-platform)
2. [NFX — 5-Layer Generative AI Tech Stack](#nfx-stack)
3. [The AI Wrapper Problem](#wrapper)
4. [AI-Era Moat Assessment Framework](#moat-framework)
5. [AI Startup Archetypes & Evaluation Patterns](#archetypes)
6. [AI Cost Dynamics & Margin Trajectories](#costs)

---

## a16z — Who Owns the Generative AI Platform? {#a16z-platform}

**Source**: Matt Bornstein, Guido Appenzeller, Martin Casado — a16z (January 2023, with
subsequent updates through 2025)

### Key Findings

**The three-layer stack:**
1. **Applications** — User-facing products using AI models
2. **Models** — Foundation models (proprietary APIs or open-source)
3. **Infrastructure** — Cloud/hardware running training and inference

**Where value is accruing (2023–2026):**
- Infrastructure captures the most dollars (10-20% of all revenue flows to cloud providers)
- Applications are growing fast but struggle with retention and differentiation
- Model providers have massive usage but unclear long-term business models

**The core insight: "No systemic moats in generative AI"**
- Applications use similar models → limited product differentiation
- Models train on similar data with similar architectures → unclear long-term
  differentiation
- Cloud providers run the same GPUs → limited technical differentiation
- Hardware is manufactured at the same fabs → limited hardware differentiation
- Standard moats (scale, supply chain, ecosystem, distribution) exist but aren't durable
  in the traditional sense

**What this means for startup evaluation:**
- Don't accept "we use AI" as a differentiator — *everyone* uses AI
- Ask: "If I strip out the AI, what's unique about your product?"
- Look for moats in: proprietary data flywheels, workflow embedding, vertical integration,
  domain expertise codified into the product
- AI-native apps have a window to establish position before incumbents integrate AI
  features, but the window is narrow (12-24 months)

### Application-Level Challenges (from a16z data)

| Challenge | Details |
|---|---|
| Retention | Top-of-funnel growth is strong, but many users are "AI tourists" who don't stick |
| Differentiation | Apps relying on same underlying models look/feel similar |
| Gross margins | 50-60% typical (inference costs), vs. 80-90% for traditional SaaS |
| Defensibility | No obvious network effects or data moats in most apps yet |

### The Vertical Integration Question

- Consuming AI models as a service: fast iteration, small team, can swap providers.
  But: limited differentiation, dependent on model provider.
- Training custom models: defensible (proprietary model), expensive ($M+), slower
  iteration, requires specialized talent.
- a16z's take: "If the primary differentiation is the AI itself, vertical integration
  (model + app) will likely win. If AI is part of a larger feature set, horizontal
  (API-based) will work."

---

## NFX — 5-Layer Generative AI Tech Stack {#nfx-stack}

**Source**: James Currier, NFX (December 2022, updated 2023)

### The Five Layers

```
Layer 5: Applications (workflow tools for humans + AI collaboration)
Layer 4: OS / API layer (interoperability, identity, payments, model switching)
Layer 3: Hyperlocal AI models (specialist, proprietary data — e.g., your company's style)
Layer 2: Specific AI models (domain-specific — e.g., tweet writing, e-commerce photos)
Layer 1: General AI models (GPT, Claude, Stable Diffusion — broad capabilities)
```

### Key Insights for Evaluation

**Where to build defensibility:**
- Layers 1-2 (General/Specific models): trending toward commoditization. Data advantages
  asymptote. Human perception limits cap the value of marginal improvements.
- Layer 3 (Hyperlocal models): strongest data moat position — proprietary, trusted data
  that competitors can't easily replicate
- Layer 4 (OS/API): strong network effects and embedding potential
- Layer 5 (Applications): network effects and embedding are the primary moat vectors

**The data asymptote principle:**
- More data improves models, but with diminishing returns
- The first million data points are transformative; the tenth million barely moves the needle
- Human perception has limits — once AI output exceeds human discrimination ability,
  further improvement doesn't create competitive advantage
- Timeline: NFX estimated 2-3 years (from 2022) for many models to reach human-perception
  limits in their domains — we're now past that timeline for text and images

**How to win (NFX's prescription):**
1. **Product speed** — ship fast, iterate, don't over-optimize models at the expense of
   product
2. **Sales speed** — aggressive go-to-market to embed before competitors
3. **Network effects** — build them into the product architecture from day one
4. **Embedding** — become part of the customer's daily workflow
5. **Sprint with capital** — move fast while the market is forming

---

## The AI Wrapper Problem {#wrapper}

### Definition

An "AI wrapper" is a product that provides a UI/UX layer on top of a foundation model API
(OpenAI, Anthropic, etc.) without substantial proprietary technology, data, or workflow
value.

### The Wrapper Test

Strip away the AI model. What remains?

| What Remains | Assessment |
|---|---|
| Nothing — just a chat interface or form | **Pure wrapper** — extremely vulnerable |
| A nice UI with templates and presets | **Thin wrapper** — easily replicable |
| Domain-specific data pipeline + custom prompting | **Value-add wrapper** — some defensibility |
| Proprietary data + custom model + workflow integration | **AI-native product** — defensible |
| Complete vertical solution (data → model → UX → distribution) | **Vertical AI company** — strong |

### When Wrappers Can Win

Not all wrappers are doomed. Wrappers succeed when:
1. **Distribution advantage**: they reach customers that the model provider can't/won't
   (vertical market, specific channel, regulatory compliance)
2. **Workflow integration**: they embed deeply into the customer's existing tools and
   processes (Cursor wrapped AI into the IDE workflow; GitHub Copilot couldn't be
   easily replicated by "just use the API")
3. **Domain data flywheel**: the wrapper generates proprietary training data through usage
   that improves results for their specific domain
4. **Curation and taste**: for consumer products, editorial judgment and UX polish can
   create brand loyalty (though this is a weak moat)

### Red Flags in AI Startup Claims

| Claim | What to Probe |
|---|---|
| "We have a proprietary AI model" | How much of it is fine-tuning vs. training from scratch? What's the data source? |
| "Our AI is better than competitors" | Better by what metric? Measured how? Compared to what baseline? |
| "We have a data moat" | Is the data truly proprietary? How much is needed? Have you asymptoted? |
| "AI is our core technology" | Could someone replicate the product in a weekend with the same API? |
| "We use [latest model] for [task]" | Why does this specific task need AI vs. rules/heuristics? |

---

## AI-Era Moat Assessment Framework {#moat-framework}

### Framework: Three Layers of AI Defensibility

**Layer 1: Model Layer (Weakest)**
- Custom model architecture → mostly commoditized
- Fine-tuned model on domain data → moderate, but fine-tuning is getting easier
- Proprietary training data → moderate, but data advantages asymptote
- Novel training methodology → rare, and quickly published/replicated

**Layer 2: Data Layer (Medium)**
- Proprietary data pipeline → moderate (hard to build, but not impossible to replicate)
- User-generated data flywheel → strong if active (each user creates data that improves
  the product for all users)
- Continuous learning from production → strong (the product improves from real-world usage)
- Domain-specific evaluation data → underrated (knowing how to measure if your AI works
  is its own expertise)

**Layer 3: Product/Distribution Layer (Strongest in AI era)**
- Workflow embedding → strong (once AI is woven into daily processes, switching is painful)
- Network effects → very strong (marketplace, platform, collaborative features)
- Distribution channels → strong (partnerships, integrations, community)
- Brand / trust → moderate-strong (especially in high-stakes domains: healthcare, legal,
  finance)
- Regulatory compliance → strong in regulated industries

### The 2025-2026 AI Landscape

Key dynamics to consider in any AI startup evaluation:
- **Foundation model capabilities are converging** — GPT-4/Claude/Gemini class models
  are roughly comparable for most tasks
- **Open-source is catching up** — Llama, Mistral, and others are viable for many
  applications, reducing API dependency
- **Inference costs are plummeting** — what cost $1 in 2023 costs ~$0.10 in 2026
- **Agentic AI is the frontier** — multi-step, tool-using agents are the current
  battleground
- **Incumbents are moving fast** — Microsoft (Copilot), Google (Gemini integration),
  Salesforce (Einstein), Adobe (Firefly) have all shipped AI features
- **Regulation is coming** — EU AI Act is in effect, US and others following;
  compliance is becoming a real factor

---

## AI Startup Archetypes & Evaluation Patterns {#archetypes}

### Archetype 1: AI-Native Application
- Builds a product where AI is the core value delivery mechanism
- Example: Cursor (AI code editor), Midjourney (AI image generation)
- Evaluate: Is the AI deeply integrated or a bolt-on? Does the product create a data
  flywheel? Is there workflow embedding?

### Archetype 2: AI-Enabled Vertical SaaS
- Takes a specific industry and rebuilds the workflow with AI at the center
- Example: Harvey (legal), Abridge (medical documentation)
- Evaluate: Does the team have deep domain expertise? Is the data proprietary to the
  vertical? Are there regulatory barriers that protect the position?

### Archetype 3: AI Infrastructure / Tooling
- Builds picks-and-shovels for other AI companies
- Example: LangChain, Weights & Biases, Scale AI
- Evaluate: Is this a feature or a product? Will the cloud providers absorb this? Is
  there a developer community/ecosystem forming?

### Archetype 4: AI Marketplace / Platform
- Connects AI capabilities with demand
- Example: Hugging Face, Replicate
- Evaluate: Are network effects forming? Is there liquidity? Can creators/suppliers be
  retained?

### Archetype 5: Data-Advantage AI Company
- Owns or generates unique data that creates a persistent AI advantage
- Example: Tesla (driving data), Spotify (listening data for recommendations)
- Evaluate: Is the data truly proprietary? Has the model asymptoted? Does data freshness
  matter (continuous advantage vs. one-time training benefit)?

---

## AI Cost Dynamics & Margin Trajectories {#costs}

### The Cost Curve

AI inference costs are declining rapidly, following a pattern similar to Moore's Law:

| Year | Approximate cost per million tokens (GPT-4 class) |
|---|---|
| 2023 | $30-60 |
| 2024 | $10-30 |
| 2025 | $3-10 |
| 2026 | $1-5 |

### Implications for Margin Analysis

- A company with 50% gross margins due to AI inference costs in 2024 might have 70%+
  margins by 2026 *without changing anything* — just from cost declines
- This means: don't over-penalize current margins if the company is API-dependent. Instead,
  model the margin trajectory.
- BUT: cost declines benefit everyone, including competitors. Lower costs don't create
  a moat — they lower the barrier to entry.

### The Compute Allocation Question

For companies training their own models:
- Training costs are one-time (per model version) but massive ($1M-$100M+)
- Inference costs are ongoing and scale with usage
- The ratio matters: a company spending 80% of revenue on training is in a very different
  position than one spending 80% on inference
- Training spend = investment in future capability. Inference spend = cost of current delivery.
