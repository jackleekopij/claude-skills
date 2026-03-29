---
name: optimal-learning
description: >
  Research-backed learning system with two modes: Study (pre-test → material creation → NotebookLM podcast prompts)
  and Test (retrieval practice at the edge of your knowledge with gap tracking across sessions).
  Use this skill whenever the user wants to learn new material, study a topic, create study notes, review for exams,
  test their knowledge, do retrieval practice, track learning progress, or mentions "study mode", "test mode",
  "learning", "study", "review", "quiz me", "test me", "knowledge gaps", or "spaced practice".
  Also trigger when the user uploads PDFs, docs, or other content and says they want to learn or understand it.
  This skill should be used even for casual requests like "help me learn this" or "I need to study for..."
---

# Optimal Learning Skill

A research-backed learning system grounded in cognitive psychology. This skill implements an evidence-based
workflow derived from seven peer-reviewed studies on the testing effect, retrieval practice, prediction error
learning, and pretesting.

The core insight from the research: **testing is not just assessment — it is the primary mechanism of durable
learning.** Passive re-reading and highlighting feel effective but produce weak memory traces. Testing forces
your brain to generate predictions, and the errors from those predictions drive the encoding that makes
knowledge stick (Chen et al. 2025).

## Abstraction Levels: Strategic / Tactical / Technical

Not all knowledge within a topic deserves the same encoding depth. This skill uses three abstraction
levels to calibrate how deeply to learn each concept. These are **per-concept tags**, not mutually
exclusive operating modes — the user will typically operate at Strategic + Tactical simultaneously.

| Level | The user is... | They need to know... | Encoding depth |
|-------|---------------|---------------------|----------------|
| **Strategic** | Making strategic decisions, choosing approaches, designing experiments, evaluating tradeoffs | *What* X does, *when* it fails, *why* you'd choose it over Y. Causal reasoning about tradeoffs. | Deep conceptual. Rich mental models. Free recall expected. |
| **Tactical** | Orchestrating AI/tools, configuring systems, validating outputs, composing components, catching errors | Interfaces, what good output looks like, typical parameter ranges, red flags. Enough to prompt AI effectively and spot when it's wrong. | Working familiarity. Recognition and pattern-matching. |
| **Technical** | Doing low-level implementation — writing algorithms line-by-line, deriving equations, manual procedural work | Internal mechanics, mathematical derivations, step-by-step implementation detail | Comprehensive procedural. Derivations, proofs, implementation steps. |

The key question per concept: **"Am I deciding, configuring, or implementing?"**

**The levels are cumulative.** Operating at a lower level includes everything above it:
- Strategic only → deep treatment for Strategic; Tactical and Technical get lighter treatment
- Strategic + Tactical → deep treatment for both; Technical gets lighter treatment
- All three (Technical) → deep treatment at all levels (e.g., a student implementing algorithms
  from scratch also needs to understand the design tradeoffs and configuration interfaces)

Concepts **above** the user's operating level always get full depth. Concepts **below** it get
progressively lighter treatment — concise reference rather than deep encoding. The user's
declared operating level sets the **depth boundary**: everything at or above it is actively
learned and tested; everything below is reference-only.

This framework shapes everything: which pre-test questions to ask, how deep study notes go,
what the knowledge tracker tracks, and where test mode focuses retrieval practice.

## Two Modes

This skill operates in two modes. Ask the user which mode they want, or infer from context:

- **Study Mode** — First encounter with new material. Transforms raw content into connected, testable knowledge.
- **Test Mode** — Retrieval practice sessions that find and work the edges of the user's knowledge.

The user will typically alternate: study a topic, then test on it in a later session, then study new material
that builds on what they know, then test again.

---

## Study Mode

### Overview

Study mode transforms raw content (PDFs, docs, articles) into structured knowledge connected to what the user
already knows. It follows a specific sequence designed to maximize encoding depth.

### Step 0: Discover Vault Structure

The user will select their Obsidian vault folder through Cowork. On first use, explore the folder structure:

```bash
# Understand the vault organization
find [mounted-folder] -type d -maxdepth 3 | head -50
find [mounted-folder] -name "*.md" -maxdepth 3 | head -50
```

Look for:
- Folder hierarchy (by subject? by project? flat?)
- Existing note formats and conventions
- Any existing Maps of Content (MOC) files
- A `_knowledge-tracker/` directory (created by this skill in Test Mode)

Adapt all output to match the user's existing vault conventions. If no conventions exist, use a clean
folder-per-subject structure with atomic notes.

### Step 1: Read Existing Knowledge

Before touching the new material, read the user's existing notes on related topics from their vault.
This is essential because the research shows learning is strongest when new information connects to
and extends existing knowledge structures (prediction error is larger when there's a prior framework
to violate).

```
1. Search the vault for notes related to the new topic
2. Read any existing knowledge tracker files for this topic area
3. Build a mental model of what the user already knows and where the boundaries are
```

### Step 2: Calibrate Operating Level

Before generating the pre-test, establish what abstraction level the user will operate at for
this topic. This determines encoding depth for every downstream step.

Ask the user:

```
For this topic, what will you be doing with this knowledge? Describe your role
briefly — this determines how deep we go at each level.

Examples:
- "I'm designing experiments and choosing algorithms, not implementing them
   from scratch" → Strategic + Tactical depth, Technical is reference-only
- "I need to implement these algorithms for a university assignment and
   understand every step" → full depth at all three levels
- "I just need to make strategic decisions about which approach to fund"
   → Strategic depth only, Tactical and Technical are reference-only
```

From the user's answer, determine their **operating depth** — the lowest level they need
to actively learn (Strategic, Tactical, or Technical). Remember: the levels are cumulative, so
operating at Tactical means Strategic + Tactical both get full treatment, and operating at Technical
means all three levels get full treatment.

If the user's answer is ambiguous, err toward Strategic + Tactical (the most common pattern for
someone leveraging AI). Store the operating depth — it's used in every subsequent step.

The user's role description also helps infer which *concepts* within the topic sit at which
level. A concept's level is intrinsic ("CQL's alpha parameter" is inherently Tactical-level),
but whether it gets deep or light treatment depends on the user's operating depth.

### Step 3: Pre-Test (The Pretesting Effect)

**Before the user reads any new material**, generate a pre-test. This is one of the most powerful
techniques in the research:

> "Pretesting, which involves attempting and failing to guess unknown information before studying it,
> has emerged as a more effective strategy than mere re-studying." — Mera et al. 2025

> "The testing effect arises from prediction error–driven learning — testing forces predictions that
> generate errors, which strengthen memory more than passive study." — Chen et al. 2025

The pre-test primes the brain to notice and encode the answers when they appear in the study material.
Even wrong guesses are valuable — the prediction error they generate is the mechanism.

**Generate 8-12 pre-test questions, stratified by level.** The distribution depends on the
user's operating depth from Step 2. Levels at or above the operating depth get substantive
questions; levels below get at most 1 lightweight recognition question.

Example distributions:
- **Operating at Strategic only:** ~8-10 Strategic, ~1-2 Tactical (lightweight), 0 Technical
- **Operating at Strategic + Tactical:** ~5-7 Strategic, ~3-4 Tactical, 0-1 Technical (lightweight)
- **Operating at all three (Technical):** ~3-4 Strategic, ~3-4 Tactical, ~3-4 Technical

Question types by level:
- **Strategic:** Open-ended questions about tradeoffs, design decisions, when/why choices matter
- **Tactical:** MCQ or short-answer about configuration, interfaces, parameter ranges, red flags
- **Technical:** Procedural questions — derive, implement, step through an algorithm, write pseudocode

For levels **below** the user's operating depth, at most include 1 lightweight recognition
question ("would you notice if..."). Don't invest pre-test priming on knowledge the user
won't need to reconstruct.

Label each question with its level so the user can see the calibration:
```
## Pre-Test: [Topic Name]

Before you read the material, try answering these. Guessing is good — prediction errors
prime your brain to encode the answers more deeply.

**Strategic**
1. [Open-ended tradeoff/design question]
2. [Why-would-you-choose question]
...

**Tactical**
5. [MCQ about configuration/interface]
6. [What does a red flag look like?]

**Technical**
8. [Derive/implement/step-through question]
...
```

Wait for the user's responses. Record their answers — these become the baseline for understanding
their starting knowledge state. Don't correct them yet.

### Step 4: Process Source Material

Read and deeply analyze the provided content (PDFs, docs, etc.). For each concept identified,
tag it with an abstraction level (Strategic / Tactical / Technical) based on the user's operating
level from Step 2.

Identify:
- Core concepts and their relationships, **tagged by level**
- Key facts, principles, and frameworks
- Areas that directly connect to the user's existing knowledge
- Areas that contradict or extend the user's existing understanding
- Common misconceptions in the field

The level tagging drives everything downstream — study note depth, quiz focus, tracker entries.

### Step 5: Generate Study Notes

Create markdown study notes and save them to the user's vault. The notes
use a **depth gradient** based on abstraction level:

Each level has a **full-depth** treatment (when at or above the user's operating depth) and a
**reference** treatment (when below it). Apply the appropriate treatment based on Step 2.

**Strategic-level content:**
- *Full depth:* Full causal chains. *Why* something works, *when* it fails, *what* changes if
  assumptions break. Multiple paragraphs with worked reasoning and tradeoff analysis. Elaborative
  interrogation prompts: "Why does this work this way?" Desirable difficulties — leave gaps that
  force active reconstruction.
- *Reference (if below operating depth):* Brief summary of the tradeoff or decision point.
  Unlikely to be below operating depth since Strategic is the top level.

**Tactical-level content:**
- *Full depth:* Tables and quick-reference formats: parameter → what it controls → typical range
  → red flags. Interface descriptions: inputs, outputs, what to configure. Cross-references to
  Strategic-level content. Enough to configure, prompt AI correctly, and catch errors.
- *Reference (if below operating depth):* Collapsed/toggle section. "These parameters exist;
  here's a one-liner on each. You don't need to memorize ranges."

**Technical-level content:**
- *Full depth:* Derivations, step-by-step algorithms, worked examples, pseudocode. Procedural
  detail sufficient to implement from scratch. Elaborative prompts: "What happens at step 3
  if the input is negative?"
- *Reference (if below operating depth):* Collapsed/toggle sections labeled "Reference —
  implementation detail." One-liners or equations for recognition, not reconstruction.
  Explicitly marked: *"You don't need to memorize this. You need to recognize it."*

**Structure:**
- Start with a brief orientation paragraph connecting to what the user already knows
- Organize sections by Strategic → Tactical → Technical (most important first)
- Use the user's existing vault conventions (headings, tags, link style)
- Include internal links (`[[existing-note]]`) where concepts connect to prior knowledge
- End with "open questions" — things the material raises but doesn't fully answer

**Content principles (from the research):**
- Emphasize conceptual understanding over isolated facts
- Highlight where the new material extends, connects to, or conflicts with prior knowledge
- Embed desirable difficulties — don't make notes too smooth or complete

**What NOT to do:**
- Don't create a verbatim summary — the research shows passive re-reading is one of the least
  effective strategies (Jemstedt 2024)
- Don't over-highlight or bold everything — this creates an illusion of learning without
  actual encoding
- Don't give deep treatment to concepts below the user's operating depth — this wastes encoding
  effort on knowledge they won't actively use

### Step 6: Generate Pre-Test Feedback

Now reveal how the user's pre-test answers compare to what the material actually says:
- Which predictions were correct (reinforce these)
- Which were wrong and why (the prediction error here is valuable)
- Which they couldn't answer — flag these as priority items

### Step 7: Generate NotebookLM Podcast Prompts

Create prompts the user can paste into NotebookLM's Audio Overview "Customize" field. Generate
three variants so the user can choose based on their needs:

Read `references/notebooklm-prompts.md` for the prompt templates and customization details.

**Important:** The user will need to upload the source material to NotebookLM themselves.
The prompts you generate should be ready to paste into the Audio Overview customization field.

### Step 8: Generate Post-Study Quiz

After the study notes are created, generate a quiz for immediate self-testing. This differs from
the pre-test — now we want to check encoding. Stratify by level:

Distribute questions based on the user's operating depth (same logic as the pre-test):

- **Levels at or above operating depth:** Substantive questions. Strategic → free recall and
  application ("Explain why...", "Compare X and Y..."). Tactical → MCQ and short-answer
  ("What parameter controls X?"). Technical → procedural ("Derive...", "Implement...",
  "Step through this algorithm for input X").
- **Levels below operating depth:** 0-1 lightweight recognition questions ("spot the error").

Example for Strategic+Tactical operating depth: ~7-10 Strategic+Tactical questions, 0-1 Technical.
Example for Technical operating depth: ~4-5 Strategic, ~4-5 Tactical, ~4-5 Technical.

Label questions with their level. Save as a separate markdown file in the vault:
`[topic]-post-study-quiz.md`

### Study Mode File Outputs

Save all outputs to the user's vault in the appropriate location:

```
[vault]/[topic-folder]/
├── [topic]-study-notes.md          # Main study notes
├── [topic]-pre-test.md             # Pre-test questions and user's responses
├── [topic]-post-study-quiz.md      # Immediate self-test quiz
├── [topic]-notebooklm-prompts.md   # Prompts for Audio Overview
```

---

## Test Mode

### Overview

Test mode is for retrieval practice — the single most effective learning technique in the
research literature. It's designed for follow-up sessions after the user has studied material.

> "Taking a test of previously studied material has been shown to improve long-term subsequent
> test performance in a large variety of well controlled experiments." — Polack & Miller 2022

> "Self-testing practice and learning strategy follow-through predict student success."
> — Hazlett et al. 2024

### Step 0: Read Knowledge State

On entering test mode, read the user's knowledge tracker for the topic:

```
[vault]/_knowledge-tracker/
├── [topic]-tracker.md     # Mastery levels, gap history, session log
```

If no tracker exists yet, create one from the study notes and any previous quiz results.

The tracker format (create this on first test session):

```markdown
# Knowledge Tracker: [Topic]

## Metadata
- First studied: [date]
- Last tested: [date]
- Sessions completed: [n]
- Operating depth: [Strategic / Strategic+Tactical / Technical (all)]
- Overall mastery estimate: [percentage]

## Concept Map

| Concept | Level | Mastery | Last Tested | Notes |
|---------|-------|---------|-------------|-------|
| [concept-1] | Strategic | strong | 2025-01-15 | Consistently correct on free recall |
| [concept-2] | Strategic | partial | 2025-01-15 | Gets tradeoff right but misses edge case |
| [concept-3] | Tactical | partial | 2025-01-15 | Knows parameter exists, unsure of range |
| [concept-4] | Tactical | weak | 2025-01-15 | Confused with [related config] |
| [concept-5] | Technical | — | — | Below operating depth, reference only |

## Knowledge Gaps (Active)
- [Gap description with context about what the user confuses or misses]

## Knowledge Gaps (Resolved)
- [Previously identified gap] — resolved [date]

## Session History
### Session 1 — [date]
- Focus: [what was tested]
- Result: [brief summary]
- New gaps identified: [list]
- Gaps resolved: [list]
```

### Step 1: Diagnostic Scan

Start each test session with a quick diagnostic — 3-5 questions that span the topic to
find the current edge of the user's knowledge. **Prioritize by level:**

Prioritize levels at or above the user's operating depth (from the knowledge tracker metadata).
For levels below operating depth, skip entirely — they're reference knowledge, not retrieval-worthy.

Example for Strategic+Tactical operating depth:
- 2-3 questions on **Strategic-level** concepts
- 1-2 questions on **Tactical-level** concepts
- Skip Technical-level

Example for Technical operating depth (all levels active):
- 1-2 questions on **Strategic-level** concepts
- 1-2 questions on **Tactical-level** concepts
- 1-2 questions on **Technical-level** concepts

Within each level, mix retention checks (previously strong) with improvement checks (previously weak).
The goal is to quickly locate where to focus the session.

### Step 2: Edge-of-Knowledge Testing

Based on the diagnostic, focus the session on the boundary between what the user knows and
doesn't know. This is where learning happens most efficiently.

**Question format strategy — calibrated by level:**

**Strategic-level concepts → free recall (open-ended).** This produces the strongest memory traces
and is worth the investment because these are decision-making concepts:
> "Retrieval practice is superior to re-study for promoting long-term retention. The benefits
> of testing can be seen with open-ended responses (eg, cued or free recall)." — Yang et al. 2019

Examples: "Explain why...", "What would you change if...", "Compare X and Y for this scenario.",
"Walk me through the tradeoff between..."

**Tactical-level concepts → MCQ and short-answer.** MCQs are appropriate here because the user
needs recognition and pattern-matching, not deep reconstruction:
> "The use of multiple-choice questions during testing may have an additional benefit as it may
> stabilize information that is stored in memory but temporarily inaccessible due to disuse
> (eg, marginal knowledge)." — Yang et al. 2019

Examples: "What parameter controls X? (a/b/c/d)", "This config value looks wrong — what's the issue?"

**Technical-level concepts:**
- *If at operating depth:* Free recall and procedural questions. "Derive...", "Implement...",
  "Step through this algorithm." Full retrieval practice — these are core to the user's work.
- *If below operating depth:* Rarely tested. Only occasional "spot the error" questions.
  Never free recall — that's wasted encoding effort.

**Testing principles:**
- Ask one question at a time and wait for the user's answer
- After the user answers, provide immediate feedback with explanation
- If the user gets it wrong, don't just give the answer — ask a simpler related question
  to help them reconstruct the path to the correct answer
- Spend most of the session on levels at or above the operating depth
- For levels below operating depth, only occasional recognition checks
- Periodically re-test previously missed items within the same session (spaced within-session)

**Metacognitive calibration:**
The research consistently shows people underestimate how effective testing is and overestimate
how well they've learned from passive study (Mera et al. 2025). Periodically ask the user
to rate their confidence before revealing whether they're correct. This builds metacognitive
awareness over time.

### Step 3: Update Knowledge Tracker

After the testing session, update the tracker file in the vault:

1. Update mastery levels for all tested concepts
2. Move resolved gaps to the "Resolved" section
3. Add newly identified gaps to the "Active" section
4. Log the session in Session History
5. Update the overall mastery estimate

**Mastery level definitions:**
- **strong**: Correct on free recall across multiple sessions
- **partial**: Gets MCQ right but struggles with free recall, or correct once but not retested
- **weak**: Incorrect or unable to answer, or consistently confuses with related concepts
- **not-tested**: Present in study material but never assessed
- **—** (dash): Concept is below the user's operating depth — reference-only, not actively tested

Note: Mastery expectations are calibrated by level AND operating depth:
- A concept **at or above** operating depth should progress toward "strong" (free recall) or
  at minimum "partial" (MCQ-correct), depending on its level.
- A concept **below** operating depth is marked "—". It's tracked in the table for completeness
  but not actively tested unless the user's operating depth changes.

### Step 4: Recommend Next Steps

Based on the session results, suggest:
- When to test again (longer intervals for strong items, shorter for weak)
- Whether new study material would help (if gaps suggest missing foundational knowledge)
- Specific concepts to focus on next session
- Whether to revisit NotebookLM audio on specific subtopics

---

## Cross-Session Continuity

The knowledge tracker is the bridge between sessions. Each new Test Mode session should:

1. Read the tracker first
2. Note how long it's been since last session (longer gaps = expect some forgetting, which is normal and actually beneficial for learning when followed by successful retrieval)
3. Start with the diagnostic scan targeting previously weak areas + time-based retention checks
4. Build on the trajectory from previous sessions

This creates a spaced retrieval practice schedule that naturally adapts to the user's learning pace.

---

## Important Caveats from the Research

Keep these in mind throughout both modes:

1. **Testing is not just assessment** — it actively changes the memory trace (Polack & Miller 2022).
   Frame testing as a learning activity, not an evaluation. The user should feel safe getting
   things wrong.

2. **Errors are productive** — Wrong answers during pre-tests and tests drive prediction error
   learning (Chen et al. 2025, Mera et al. 2025). Never make the user feel bad about errors.
   Explicitly normalize them: "Getting this wrong actually helps your brain encode the correct
   answer more deeply."

3. **Illusion of competence** — Re-reading and highlighting feel effective but aren't
   (Jemstedt 2024, Hazlett et al. 2024). The skill should never fall back to passive formats.

4. **Metacognitive miscalibration** — People consistently underestimate testing effectiveness
   (Mera et al. 2025). Periodically remind the user that the difficulty they feel during
   testing is a sign of effective learning, not failure.

5. **Concept mapping caveat** — While concept mapping can be useful, Mayrhofer et al. (2023)
   showed that some claimed advantages of retrieval practice over concept mapping may be
   methodological artifacts. Both are legitimate active learning strategies.

---

## Reference Files

- `references/notebooklm-prompts.md` — Templates for generating NotebookLM Audio Overview prompts
- `references/research-base.md` — Detailed summaries of the seven research papers underlying this skill
