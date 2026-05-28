# Research Base — Seven Studies Underlying the Optimal Learning Skill

This file contains concise summaries of the research papers that inform the skill's design.
Each entry explains: what was studied, key findings, and how it maps to the skill's workflow.

---

## 1. Chen et al. (2025) — Prediction Error–Driven Learning

**Title:** Testing effect arises from prediction error–driven learning

**Key finding:** The testing effect is best explained by prediction error learning theory.
When you take a test, your brain generates a prediction. If that prediction is wrong, the
error signal drives stronger encoding of the correct answer than passive study would. This
is why even failed test attempts improve later recall — the error itself is the learning
mechanism.

**Skill application:** This is the theoretical foundation for pre-testing (Study Mode Step 2).
Even when users guess wrong on pre-test questions, the prediction errors prime their brain
to encode correct answers more deeply when they encounter them in the study material.

---

## 2. Mera et al. (2025) — Pretesting as a Learning Strategy

**Title:** Pretesting as a more effective learning strategy than re-studying

**Key finding:** Attempting to answer questions about material *before* studying it produces
better long-term retention than studying the material twice. This holds even when pretests
are completely failed. Additionally, people consistently underestimate the effectiveness of
pretesting and overestimate re-reading — a metacognitive miscalibration.

**Skill application:** Directly informs the pre-test workflow (Study Mode Step 2) and the
metacognitive calibration component of Test Mode. The skill explicitly normalizes errors
and reminds users that difficulty during testing signals effective learning.

---

## 3. Yang et al. (2019) — Free Recall vs. Multiple Choice

**Title:** Enhancing learning and retrieval of new information: the role of test format

**Key finding:** Free recall (open-ended) testing produces the strongest memory traces for
well-learned material. However, multiple-choice testing has a unique benefit for "marginal
knowledge" — information that's stored in memory but temporarily inaccessible. MCQs provide
retrieval cues that help stabilize this fragile knowledge.

**Skill application:** Informs the question format strategy in Test Mode Step 2. The skill
uses free recall for core concepts (strongest encoding) and MCQs for peripheral/weak
knowledge (recovery of temporarily inaccessible memories).

---

## 4. Polack & Miller (2022) — The Testing Effect Mechanisms

**Title:** Testing improves long-term retention: a meta-analytic review

**Key finding:** Taking a test on previously studied material reliably improves subsequent
test performance across a wide variety of experimental conditions. The effect is robust
across different materials, delay intervals, and test formats. Testing is not merely
assessment — it actively modifies the memory trace.

**Skill application:** Provides the empirical foundation for Test Mode as a whole. The
skill frames testing as a *learning activity*, not evaluation, and encourages users to
view it as the primary mechanism of durable learning.

---

## 5. Jemstedt (2024) — Ineffectiveness of Passive Re-reading

**Title:** Re-reading and highlighting: ineffective but persistent study strategies

**Key finding:** Despite being the most commonly used study strategies, re-reading and
highlighting produce minimal learning gains compared to active strategies like testing.
They create an "illusion of competence" — students feel they've learned because the
material feels familiar, but familiarity doesn't equal retrievability.

**Skill application:** Informs the "What NOT to do" guidelines throughout the skill.
Study notes are designed with "desirable difficulties" rather than smooth summaries.
The skill never falls back to passive formats and warns about the illusion of competence.

---

## 6. Hazlett et al. (2024) — Self-Testing and Student Success

**Title:** Self-testing practice and learning strategy follow-through predict student success

**Key finding:** Students who actually follow through on self-testing practices perform
significantly better than those who only plan to test themselves. The key predictor of
success isn't knowing about effective strategies — it's consistently executing them.
Strategy follow-through matters more than strategy knowledge.

**Skill application:** This is why the skill includes a structured tracker with session
history and scheduled follow-ups. The system provides the scaffolding for consistent
practice rather than relying on the user to self-organize their retrieval practice.

---

## 7. Mayrhofer et al. (2023) — Concept Mapping vs. Retrieval Practice

**Title:** Retrieval practice vs. concept mapping: methodological considerations

**Key finding:** Some widely cited studies claiming retrieval practice is categorically
superior to concept mapping may have methodological artifacts. When controls are properly
matched, concept mapping can be comparably effective as an active learning strategy.
Both are legitimate — the important distinction is active vs. passive, not which active
strategy is "best."

**Skill application:** Informs the caveats section. The skill doesn't dogmatically push
one active strategy over another. It primarily uses retrieval practice (strongest evidence
base) but acknowledges that concept mapping and other active strategies contribute to
learning. The key principle: anything active beats anything passive.

---

## Summary: Design Principles Derived from the Research

1. **Test early, test often** — Testing is the learning mechanism, not just measurement
2. **Errors are features, not bugs** — Prediction errors drive encoding
3. **Pre-test before study** — Failed predictions prime deeper learning
4. **Free recall for strong material, MCQ for weak** — Match format to knowledge state
5. **Active over passive, always** — No re-reading, no highlighting, no passive summaries
6. **Track and scaffold** — Consistent practice matters more than knowing what works
7. **Calibrate metacognition** — Help users feel that difficulty = learning, not failure
