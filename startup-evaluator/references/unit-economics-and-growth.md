# Unit Economics & Growth — Deep Reference

Consult this file when evaluating Dimension 3 (Business Model & Unit Economics) and when
assessing Dimension 8 (Traction & Evidence) — particularly whether growth is healthy or
just burning cash.

## Table of Contents
1. [Sam Altman — Unit Economics Fundamentals](#altman)
2. [Bill Gurley — Revenue Quality](#gurley)
3. [YC — Growth & Metrics That Matter](#yc-growth)
4. [Marketplace Economics](#marketplace)
5. [SaaS Metrics & Benchmarks](#saas)

---

## Sam Altman — Unit Economics Fundamentals {#altman}

**Source**: "Unit Economics" (blog.samaltman.com), YC lectures, "How to Succeed with a
Startup" (YC talk)

### Core Concepts

**The Dollar-for-80-Cents Test**
- "It never makes sense to take 80 cents from a customer and hand them a dollar back."
- Yet this is what startups do when they subsidize growth with negative unit economics
- Every user acquired at a loss has to eventually become profitable, or the company dies
  when funding dries up
- The critical question: "Do you make money on each transaction/user, *excluding* fixed
  costs?" If not, growth accelerates death.

**Growth Is Not the Precursor — It's the Result**
- "Growth is the result of a great product, not the precursor"
- Startups that try to grow before achieving PMF waste money on users who won't stick
- Premature growth creates a false signal: metrics go up, but the underlying business
  isn't healthy
- YC test: look at the retention curve, not the acquisition curve

**When Negative Unit Economics Are Acceptable:**
- Marketplace chicken-and-egg: subsidizing one side to bootstrap liquidity (Uber subsidized
  drivers initially). Must have a clear plan to reach positive margins.
- Land-and-expand: acquiring a customer at a loss with a proven upsell path (Slack: free
  tier → paid → enterprise)
- Network effects: each user at a loss makes the product more valuable for others, and
  value eventually exceeds cost (but this has to be *proven*, not assumed)
- Temporary supply constraints: costs are high now but will fall (AI inference costs
  dropping ~50%/year)

**When Negative Unit Economics Are a Red Flag:**
- No plan to reach positive margins ("we'll figure out monetization later")
- Customer subsidies with no structural reason to believe behavior changes at scale
- Spending more on each marginal customer (inverse economies of scale)
- Marketplace take rate too low to sustain both sides

### Key Metrics to Evaluate

| Metric | What It Tells You | Healthy Range |
|---|---|---|
| CAC (Customer Acquisition Cost) | How much to get a customer | Depends on LTV |
| LTV (Lifetime Value) | How much a customer is worth over their lifetime | Must be > CAC |
| LTV:CAC ratio | Efficiency of growth | >3:1 for venture-scale businesses |
| CAC payback period | How long to recover acquisition cost | <18 months |
| Gross margin | Revenue minus direct costs of delivery | >60% for software, >40% for marketplace |
| Contribution margin | Gross margin minus variable sales/marketing | Must be positive |
| Burn multiple | Net burn / net new ARR | <2x is efficient, >3x is concerning |

---

## Bill Gurley — Revenue Quality {#gurley}

**Source**: "All Revenue is Not Created Equal" (Above the Crowd blog, 2011)

### Core Concepts

Gurley argues that Wall Street (and VCs) should not treat all revenue dollars the same.
A dollar of high-quality revenue is worth much more than a dollar of low-quality revenue
because of its sustainability, predictability, and margin characteristics.

**Revenue Quality Factors (ranked by importance):**

1. **Sustainable competitive advantage (moat)** — Revenue protected by a moat is worth
   more than revenue in a commodity market
2. **Presence of network effects** — Revenue that gets easier to generate over time
   (because the product improves with scale) is highest quality
3. **Visibility / predictability** — Recurring, contractual revenue > transactional
   revenue > one-time revenue. Subscription > usage-based > project-based
4. **Customer lock-in / high switching costs** — Revenue from embedded customers is more
   durable
5. **Gross margin levels** — High-margin revenue is worth more (software 80%+ vs services
   30-50%)
6. **Marginal profitability** — Each additional dollar of revenue should cost less to
   generate
7. **Customer concentration risk** — Revenue spread across many customers is safer than
   revenue concentrated in a few
8. **Partner dependency** — Revenue you control directly is worth more than revenue
   dependent on a platform (app store, marketplace, API provider)
9. **Organic demand vs. heavy sales dependence** — Organic/inbound revenue signals
   stronger PMF than outbound-driven revenue
10. **Growth** — High growth rate amplifies all other factors

### Revenue Quality Hierarchy

```
Most Valuable
│ Recurring + high margin + moat + network effects (SaaS with NE)
│ Recurring + high margin + moat (Enterprise SaaS)
│ Recurring + high margin (SaaS without clear moat)
│ Transactional + high margin (marketplace take rate)
│ Usage-based + decent margin (cloud/API)
│ Transactional + low margin (e-commerce, logistics)
│ Project-based / one-time
│ Revenue dependent on subsidies or promotional pricing
Least Valuable
```

### How to Apply

When evaluating a startup's revenue or revenue model:
1. Place their revenue in the hierarchy above
2. Ask: "As you scale, does revenue quality improve or degrade?"
3. Watch for revenue that *looks* like recurring but isn't (annual contracts with easy
   cancellation, month-to-month with high churn)
4. Check customer concentration: if one customer is >20% of revenue, that's risk

---

## YC — Growth & Metrics That Matter {#yc-growth}

**Source**: YC Essential Startup Advice, Michael Seibel's posts, Sam Altman's "Startup
Playbook"

### The Growth Framework

**Pre-PMF Metrics (What to Measure):**
- Retention rate (weekly/monthly cohort retention)
- Usage frequency and depth
- NPS / Sean Ellis survey (% "very disappointed" if product gone)
- Qualitative: are users recommending to others unprompted?
- Number of "can't live without" users (even 10 is a signal)

**Post-PMF Metrics (When to Scale):**
- Week-over-week or month-over-month growth rate
- Organic vs. paid acquisition mix
- Payback period on customer acquisition
- Gross margin trajectory
- Net revenue retention (for SaaS: >100% means existing customers spend more over time)

**Growth Rate Benchmarks (YC/a16z):**
- 5-7% week-over-week: Good for YC companies
- 10%+ week-over-week: Exceptional
- 2-3% week-over-week: Needs improvement
- Flat or declining: Reconsider everything

**Michael Seibel's "Real Product-Market Fit":**
- PMF is not a single moment — it's a spectrum
- Level 1: Users say they want it (weakest signal)
- Level 2: Users use a prototype (better)
- Level 3: Users retain without prompting (good)
- Level 4: Users pay money (strong)
- Level 5: Users would be devastated without it AND tell others (true PMF)

### Dangerous Growth Patterns

**The "growth solves everything" trap:**
- Growing 10% MoM while churning 8% MoM = a treadmill, not a business
- Always look at *net* growth: new customers minus churned customers
- If net retention is below 100%, the company is a leaky bucket

**The "we're growing but not monetizing yet" trap:**
- Acceptable only if: (a) there's a proven monetization model in the industry, AND
  (b) the company is deliberately deferring revenue to maximize network effects
- Unacceptable if: the company doesn't know how it will make money

**The "enterprise pipeline" trap:**
- "We have $2M in pipeline" means nothing — pipeline doesn't pay salaries
- Signed contracts > LOIs > verbal commitments > "pipeline"
- Ask: "How many of those deals have *closed*? What's your close rate?"

---

## Marketplace Economics {#marketplace}

**Source**: Bill Gurley "A Rake Too Far" (2013), a16z marketplace series, Andrew Chen
"The Cold Start Problem" (2021)

### Core Concepts

**Take Rate (Rake)**
- The percentage of GMV (gross merchandise value) the marketplace keeps
- Must be high enough to build a business but low enough that both sides feel it's fair
- If the take rate is too high, participants have strong incentive to disintermediate
  (go around the marketplace)

**Take Rate Benchmarks:**

| Category | Typical Take Rate | Examples |
|---|---|---|
| Digital goods/services | 20-30% | App Store (30%), Fiverr (20%) |
| Ride-sharing / delivery | 20-30% | Uber (25%), DoorDash (15-25%) |
| E-commerce marketplace | 10-15% | Amazon (15%), Etsy (6.5% + fees) |
| Real estate | 2-5% | Redfin, Zillow |
| Financial services | 1-3% | Payment processing |
| Advertising marketplace | 15-40% | Programmatic ad exchanges |

**Liquidity**
- A marketplace's core challenge: enough supply and demand that matches happen reliably
- Before liquidity: frustrating for both sides, negative word-of-mouth
- After liquidity: self-reinforcing, network effects kick in
- "Liquidity" is market-specific: for Uber it's "a car arrives in < 5 minutes"; for
  Airbnb it's "10+ good listings in any searched city"

**The Cold Start Problem (Andrew Chen)**
- How to get the first users on both sides when neither side has value without the other
- Classic solutions: start with one side (supply or demand), subsidize, go hyperlocal,
  piggyback on existing networks, have the founding team BE the supply

**Disintermediation Risk**
- Once buyer and seller connect, why not go direct?
- Defenses: ongoing value (quality assurance, payment processing, dispute resolution,
  discovery/matching), data and relationship ownership, contractual terms
- Ask: "After the first transaction, what keeps both sides on the platform?"

---

## SaaS Metrics & Benchmarks {#saas}

For B2B SaaS companies specifically:

| Metric | Benchmark | Source |
|---|---|---|
| Gross margin | >70% | Bessemer |
| LTV:CAC ratio | >3:1 | General VC consensus |
| CAC payback | <18 months | Bessemer |
| Net revenue retention | >110% | Best-in-class SaaS |
| Rule of 40 | Revenue growth % + profit margin % > 40 | Brad Feld |
| Magic Number | >0.75 (efficient growth) | Bessemer |
| Monthly churn | <2% | General benchmark |
| Annual churn | <10% | For enterprise |

**The Rule of 40**: A company's revenue growth rate plus its profit margin should exceed
40%. A company growing 60% YoY can afford -20% margins. A company growing 20% should be
at 20%+ margins. This balances growth against efficiency.

**Burn Multiple** (David Sacks): Net burn / net new ARR.
- <1x: Amazing efficiency (Incredible)
- 1-1.5x: Good
- 1.5-2x: Mediocre
- 2-3x: Bad
- >3x: Burning money

**AI-era SaaS adjustments:**
- Gross margins of 50-60% are acceptable *if* inference costs are the driver (costs
  falling rapidly)
- Usage-based pricing is becoming more common (aligns cost with value delivered)
- AI-native SaaS can often achieve higher net retention (product improves with usage data)
