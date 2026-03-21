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

### Step 2: Pre-Test (The Pretesting Effect)

**Before the user reads any new material**, generate a pre-test. This is one of the most powerful
techniques in the research:

> "Pretesting, which involves attempting and failing to guess unknown information before studying it,
> has emerged as a more effective strategy than mere re-studying." — Mera et al. 2025

> "The testing effect arises from prediction error–driven learning — testing forces predictions that
> generate errors, which strengthen memory more than passive study." — Chen et al. 2025

The pre-test primes the brain to notice and encode the answers when they appear in the study material.
Even wrong guesses are valuable — the prediction error they generate is the mechanism.

**Generate 8-12 pre-test questions:**
- Mix of free-recall (open-ended) and multiple-choice
- Target the key concepts from the new material
- Frame them as genuine questions the user might wonder about
- Include some that connect to the user's existing knowledge

**Present to the user:**
```
## Pre-Test: [Topic Name]

Before you read the material, try answering these questions. It's completely fine to guess
or say "I don't know" — the act of trying to predict the answer is what primes your brain
to learn it more deeply.

1. [Open-ended question about a core concept]
2. [MCQ about a key distinction]
3. [Question connecting to something the user already knows]
...
```

Wait for the user's responses. Record their answers — these become the baseline for understanding
their starting knowledge state. Don't correct them yet.

### Step 3: Process Source Material

Read and deeply analyze the provided content (PDFs, docs, etc.). Identify:
- Core concepts and their relationships
- Key facts, principles, and frameworks
- Areas that directly connect to the user's existing knowledge
- Areas that contradict or extend the user's existing understanding
- Common misconceptions in the field

### Step 4: Generate Study Notes

Create markdown study notes and save them to the user's vault. The notes should:

**Structure:**
- Start with a brief orientation paragraph connecting to what the user already knows
- Use the user's existing vault conventions (headings, tags, link style)
- Include internal links (`[[existing-note]]`) where concepts connect to prior knowledge
- End with "open questions" — things the material raises but doesn't fully answer

**Content principles (from the research):**
- Emphasize conceptual understanding over isolated facts
- Highlight where the new material extends, connects to, or conflicts with prior knowledge
- Include "elaborative interrogation" prompts throughout — "Why does this work this way?"
  and "How does this relate to [prior concept]?" — these deepen encoding
- Embed "desirable difficulties" — don't make notes too smooth or complete; leave small gaps
  that require the reader to actively reconstruct meaning

**What NOT to do:**
- Don't create a verbatim summary — the research shows passive re-reading is one of the least
  effective strategies (Jemstedt 2024)
- Don't over-highlight or bold everything — this creates an illusion of learning without
  actual encoding

### Step 5: Generate Pre-Test Feedback

Now reveal how the user's pre-test answers compare to what the material actually says:
- Which predictions were correct (reinforce these)
- Which were wrong and why (the prediction error here is valuable)
- Which they couldn't answer — flag these as priority items

### Step 6: Generate NotebookLM Podcast Prompts

Create prompts the user can paste into NotebookLM's Audio Overview "Customize" field. Generate
three variants so the user can choose based on their needs:

Read `references/notebooklm-prompts.md` for the prompt templates and customization details.

**Important:** The user will need to upload the source material to NotebookLM themselves.
The prompts you generate should be ready to paste into the Audio Overview customization field.

### Step 7: Generate Post-Study Quiz

After the study notes are created, generate a quiz that the user can use for immediate
self-testing. This differs from the pre-test — now we want to check encoding:

- 10-15 questions
- Mix of free recall and MCQ (see Test Mode for format rationale)
- Include questions that require connecting multiple concepts
- Include questions that require applying knowledge to new scenarios
- Save as a separate markdown file in the vault

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
- Overall mastery estimate: [percentage]

## Concept Map

| Concept | Mastery | Last Tested | Notes |
|---------|---------|-------------|-------|
| [concept-1] | strong | 2025-01-15 | Consistently correct on free recall |
| [concept-2] | partial | 2025-01-15 | Gets MCQ right but struggles with free recall |
| [concept-3] | weak | 2025-01-15 | Confused with [related concept] |
| [concept-4] | not-tested | — | Covered in study notes but not yet assessed |

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
find the current edge of the user's knowledge:

- 1-2 questions on previously "strong" concepts (verify retention)
- 1-2 questions on previously "partial" or "weak" concepts (check for improvement)
- 1 question on a "not-tested" concept (expand coverage)

The goal is to quickly locate where to focus the session. Don't spend 20 minutes on things
the user already knows well.

### Step 2: Edge-of-Knowledge Testing

Based on the diagnostic, focus the session on the boundary between what the user knows and
doesn't know. This is where learning happens most efficiently.

**Question format strategy (research-backed):**

Use **free recall (open-ended) for core concepts.** This produces the strongest memory traces:
> "Retrieval practice is superior to re-study for promoting long-term retention. The benefits
> of testing can be seen with open-ended responses (eg, cued or free recall)." — Yang et al. 2019

Use **multiple-choice for peripheral/marginal knowledge.** MCQs help recover knowledge that's
stored but temporarily inaccessible:
> "The use of multiple-choice questions during testing may have an additional benefit as it may
> stabilize information that is stored in memory but temporarily inaccessible due to disuse
> (eg, marginal knowledge)." — Yang et al. 2019

**Testing principles:**
- Ask one question at a time and wait for the user's answer
- After the user answers, provide immediate feedback with explanation (the research shows
  feedback after testing enhances the benefit)
- If the user gets it wrong, don't just give the answer — ask a simpler related question
  to help them reconstruct the path to the correct answer
- Mix question types: definitions, applications, comparisons, "what would happen if...",
  "explain why...", "how does X relate to Y..."
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
