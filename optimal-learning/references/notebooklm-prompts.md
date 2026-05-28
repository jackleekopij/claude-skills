# NotebookLM Audio Overview — Prompt Templates

When the skill generates NotebookLM prompts (Study Mode Step 6), use these templates.
The user pastes these into the "Customize" field of NotebookLM's Audio Overview feature
after uploading their source material.

Generate **four variants** so the user can pick the one that fits their needs — three
focused prompts plus one combined prompt that covers all angles in a single podcast:

---

## Variant 1: Conceptual Deep Dive

Focus on building deep understanding of the core concepts and their relationships.

```
Focus this conversation on building deep conceptual understanding. For each major concept
in the material:

1. Explain it in plain language first, then add precision
2. Give a concrete real-world analogy
3. Explain how it connects to the other key concepts
4. Identify the most common misconception about it and explain why it's wrong

Spend extra time on these specific topics: [INSERT 2-3 KEY CONCEPTS FROM THE MATERIAL]

Don't just summarize — I want to understand the *why* behind each concept. Challenge me
with "what would happen if..." scenarios. End with the 3 most important takeaways someone
studying this material should remember.
```

## Variant 2: Pre-Existing Knowledge Bridge

Focus on connecting new material to things the user already knows. Best when the skill
has identified relevant prior knowledge in Step 1.

```
I already have some background in [INSERT RELATED TOPICS THE USER KNOWS]. Help me
understand this new material by constantly connecting it to what I already know.

For each new concept, start with: "You know how [familiar concept] works? This is
similar because... but different because..."

Highlight where this material:
- Extends what I already know
- Contradicts or updates my existing understanding
- Fills gaps in my knowledge

Focus especially on: [INSERT 2-3 AREAS WHERE NEW MATERIAL CONNECTS TO PRIOR KNOWLEDGE]

End by summarizing the 3-5 biggest ways this material changes or deepens my existing
understanding.
```

## Variant 3: Application & Problem-Solving

Focus on practical application — how to use the knowledge, not just understand it.

```
I'm studying this material and I want to focus on practical application. Structure the
conversation around:

1. For each key concept, give me a concrete scenario where I'd need to apply it
2. Walk me through the thinking process for solving problems with this material
3. Identify the trickiest parts — where do people typically make mistakes when
   applying this knowledge?
4. Give me decision frameworks: "When you see X, think about Y because Z"

Focus especially on: [INSERT 2-3 CONCEPTS THAT HAVE PRACTICAL APPLICATIONS]

I'd rather deeply understand how to *use* 5 key ideas than superficially cover
everything. Prioritize depth over breadth.
```

## Variant 4: Combined (All Three Angles)

Covers conceptual understanding, prior-knowledge bridging, and practical application in
one podcast using a multi-pass structure. Best when the user wants comprehensive coverage
without listening to three separate podcasts.

```
I already have some background in [INSERT RELATED TOPICS THE USER KNOWS]. I'm studying
this material for a project involving [INSERT PROJECT CONTEXT]. Structure the conversation
in three passes:

PASS 1 — CONCEPTUAL FOUNDATIONS
For the core concepts ([INSERT 2-3 KEY CONCEPTS]), explain each in plain language with a
concrete analogy, then show how they connect. Identify the most common misconception about
each and explain why it's wrong.

PASS 2 — CONNECTING TO WHAT I KNOW
Bridge everything back to what I already understand. For each new idea, start with:
"You know how [familiar concept] works? This is similar because... but different
because..." Highlight where this material extends, contradicts, or fills gaps in my
existing understanding.

PASS 3 — PRACTICAL DECISIONS
Now help me make real choices. For each key method or framework, give a concrete scenario
where it's the right pick and where it'd fail. Focus on: [INSERT 2-3 PRACTICAL DECISIONS
THE USER FACES]. Give me decision frameworks: "When you see X, think about Y because Z."

End with the 5 most important things I should remember when applying this material to
my project.
```

---

## Customization Notes

When generating these prompts for the user:
- Replace all `[INSERT ...]` placeholders with actual content from the study material
- Adjust the tone based on the topic (technical vs. humanities vs. practical)
- If the user has specific learning goals mentioned in the session, weave those in
- Keep each prompt under ~200 words — NotebookLM works best with focused instructions

**What to upload as NotebookLM sources:**
Always instruct the user to upload BOTH the original source material (papers, docs, articles)
AND the study notes generated in Step 4. The study notes contain project context, prior
knowledge connections, and personalized framing that the prompts reference. Without them,
NotebookLM won't have the context to make the podcast personally relevant — the prompts
will reference "your project" or "what you already know" but the podcast hosts won't know
what those are.
