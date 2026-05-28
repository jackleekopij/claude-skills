---
name: research-paper-analysis
description: >
  Skill for analyzing research papers in the context of an active research project. Extracts structured
  information (contribution, method, results, limitations), assesses relevance to project goals, identifies
  actionable items, and logs findings to the research log. Use this skill whenever the user shares a paper
  (PDF, markdown, or link), mentions "analyze this paper", "review this paper", "what's relevant from this",
  "extract from this paper", "literature review", "paper summary", "how does this relate to our project",
  "add this to the literature", or provides a research paper with project-related context. Also trigger
  when the user asks to compare methods across papers, identify gaps relative to existing literature, or
  update the literature review. Do NOT use for studying/learning a topic (use optimal-learning instead) —
  this skill is for project-oriented extraction, not personal knowledge building.
---

# Research Paper Analysis

A skill for extracting structured, project-relevant information from research papers. The key difference
from general paper summarization: this skill reads your project context first, so every extraction is
filtered through "what matters for THIS project."

## When This Skill Applies vs. Optimal Learning

These two skills serve different purposes and should not be confused:

| | Research Paper Analysis (this skill) | Optimal Learning |
|---|---|---|
| **Goal** | Extract what the project needs from a paper | Build personal understanding of a topic |
| **Question** | "What should we take from this paper?" | "Do I understand this topic deeply enough?" |
| **Output** | Structured analysis file + research log entry | Study notes, quizzes, knowledge tracker |
| **Storage** | `research/literature/` | `research/learning/` |
| **Tests the user?** | No | Yes (pre-tests, post-quizzes, test mode) |

Sometimes both apply: the user might want to analyze a paper AND learn from it. In that case, run this
skill first (extraction), then suggest optimal-learning for deeper study if the paper introduces concepts
the user needs to internalize.

---

## Workflow

### Step 0: Bootstrap Project Structure

Check whether the project has the expected research infrastructure. If any piece is missing,
create it — don't ask, just create with sensible defaults. This makes the skill portable
across projects.

**Check for and create if missing:**

```
research/                      # Research directory
  literature/                  # Paper analyses go here
    papers/                    # PDF storage (mention to user)
  log.md                       # Research log (append findings here)
```

If `research/log.md` doesn't exist, create it with this starter:

```markdown
# Research Log

A running record of key insights, technical learnings, and experimental findings.
Organized by category with dates. Intended to feed directly into the paper write-up.

---

## Research: Literature Connections
```

If the user specifies a different output location, use that instead and remember it for
future invocations in the same session.

### Step 1: Load Project Context

Before touching the paper, understand what the project cares about. Auto-discover by
searching for these files (in priority order):

1. **`project-spec.md`** (or similar) — experimental design, research questions, hypotheses
2. **`copilot-instructions.md`** or `.github/copilot-instructions.md` — project overview, themes
3. **`README.md`** — project description
4. **`research/literature/review.md`** — existing literature review (what's already covered)
5. **`research/log.md`** — recent entries (what the team is currently working on)

Read the most relevant 2-3 files. Extract:
- **Research questions** — what the project is trying to answer
- **Current approach** — what methods/tools are in use
- **Known gaps** — what the project hasn't solved yet
- **Hardware/software constraints** — what's feasible to implement

**Present a brief summary to the user for verification:**
> "Based on your project context, I see you're working on [X] with [Y] hardware,
> exploring [Z] research themes. I'll filter the paper analysis through these lenses.
> Anything to adjust?"

Don't block on this — if the user doesn't respond or says "looks good," proceed.
Only pause if the user corrects the context.

### Step 2: Read and Analyze the Paper

Read the full paper (or the provided markdown/text). For each section, actively filter
through the project context: "Does this matter for our project? How?"

**What to look for specifically:**
- Methods that could be applied to the project's task/hardware
- Results that validate or challenge the project's approach
- Hyperparameters, architectures, or design choices that are directly reusable
- Failure modes or limitations that the project should avoid
- Baselines or comparisons that the project should include
- Datasets, environments, or evaluation protocols worth adopting

### Step 3: Generate Structured Analysis

Create a markdown file with the analysis. The filename should follow the pattern:
`{first_author_lastname}{year}-{short-descriptor}.md`

Examples: `silver2018-residual-rl.md`, `kumar2020-cql.md`, `kalashnikov2018-qt-opt.md`

Use this template — every section is mandatory, but sections can be brief if the paper
doesn't have much to say for that category:

```markdown
# {Paper Title}

**Authors:** {author list}
**Venue:** {conference/journal, year}
**PDF:** `research/literature/papers/{filename}.pdf` (if stored locally)
**ArXiv:** {link if available}

---

## One-Line Summary

{A single sentence capturing the core contribution — what they did and why it matters.}

## Core Contribution

{2-3 paragraphs. What is genuinely new here? Distinguish the actual contribution from
the engineering/experimental wrapper around it. What problem did it solve that wasn't
solved before?}

## Method

{How they did it. Focus on the parts that differ from standard approaches. Include:
- Architecture/algorithm (with key equations if they're central)
- Key design decisions and their stated rationale
- Hyperparameters that are non-obvious or differ from defaults}

## Key Results

{What worked and how well. Include specific numbers where they matter:
- Main performance metrics
- Ablation results that reveal what actually matters
- Comparison to baselines (which baselines, by how much)}

## Limitations & Failure Modes

{What the authors acknowledge AND what you notice they don't acknowledge:
- Experimental scope (sim only? single task? specific robot?)
- Assumptions that may not hold in other settings
- Missing baselines or comparisons
- Scalability concerns}

## Relevance to Our Project

{THIS IS THE MOST IMPORTANT SECTION. Be specific and concrete:

### What we can use
- {Specific method/technique and how it maps to our setup}
- {Hyperparameter or design choice we should adopt}
- {Evaluation protocol we should follow}

### What doesn't apply
- {Aspects that don't transfer and why — hardware differences, task differences, scale}

### Open questions this raises
- {Things to investigate further based on this paper}
- {Experiments this suggests we should run}}

## Connections to Other Work

{How this paper relates to others we've already reviewed:
- Builds on: {papers it extends}
- Competes with: {alternative approaches}
- Complements: {papers that address different aspects of the same problem}}

## Actionable Items

{Concrete next steps, if any. Be specific:
- [ ] {Something to implement, try, or investigate}
- [ ] {A comparison to add to our experiment plan}
- [ ] {A reference to cite in related work}}
```

### Step 4: Update the Literature Review (if it exists)

If `research/literature/review.md` (or similar) exists, check whether this paper fits
into an existing section or opens a new category. Suggest where it should be added, but
don't modify the review file without confirmation — the review file is a curated document,
not an auto-generated one.

### Step 5: Auto-Log to Research Log

Append an entry to `research/log.md` under the `## Research: Literature Connections`
heading (create this heading if it doesn't exist). Use this format:

```markdown
### {YYYY-MM-DD} — {Paper short reference}: {one-line insight}

{2-4 sentences: what the paper contributes and specifically how it connects to our project.
This should be dense enough that reading it 3 months later reconstructs why we cared about
this paper, without re-reading the full analysis.}
See: `research/literature/{analysis-filename}.md`
```

### Step 6: Offer Follow-Up Options

After delivering the analysis, offer:

1. **Deep-dive** — "Want me to go deeper on the method? I can extract the full algorithm
   or recreate their key equations."
2. **Compare** — "Want me to compare this against [other paper already reviewed]?"
3. **Study** — "Want to study this topic more deeply? I can switch to study mode
   (optimal-learning skill) for the concepts this paper introduces."
4. **Implement** — "Want me to implement any of the actionable items?"

---

## Multi-Paper Analysis

When the user provides multiple papers or asks to compare across papers, extend the
workflow:

1. Analyze each paper individually (Steps 2-5)
2. Generate a **comparison table** across papers covering:
   - Method type (on-policy/off-policy, model-free/model-based)
   - Data requirements (online interactions, demonstrations, dataset size)
   - Task scope (what tasks, what robots, sim/real)
   - Key results on comparable metrics
   - Applicability to our project (high/medium/low with reasoning)
3. Identify **consensus patterns** (what do multiple papers agree on?)
4. Identify **open debates** (where do papers disagree or take different approaches?)

---

## Quality Principles

**Be specific, not generic.** "This paper uses SAC" is not useful — everyone knows that from
the abstract. "This paper modifies SAC by adding a BC regularization term weighted by α=2.5,
which they show prevents policy collapse when fine-tuning from small offline datasets" is useful.

**Distinguish contribution from wrapper.** Many papers wrap a modest contribution in extensive
engineering. Identify what's actually new versus what's standard practice in a new context.

**Don't oversell relevance.** If a paper is tangentially related, say so. "Interesting but not
directly applicable because..." is more useful than stretching connections. The user's time is
better spent on highly relevant papers.

**Flag when you're uncertain.** If you can't tell whether a method would work on the project's
hardware, or whether a result is statistically significant, say so explicitly rather than
guessing.

**Preserve the paper's own caveats.** If the authors say "this only works for X," don't silently
generalize to Y. Repeat their stated limitations and add your own assessment of unstated ones.
