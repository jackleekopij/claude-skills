# Claude Code Skills

A public collection of custom skills for [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Install any skill into your own Claude Code setup and start using it immediately.

## Available Skills

### [optimal-learning](./optimal-learning/)

A research-backed learning system grounded in cognitive psychology (seven peer-reviewed studies on the testing effect, retrieval practice, and pretesting). Two modes:

- **Study Mode** — Pre-test, source material processing, Obsidian study note generation, NotebookLM podcast prompts, and post-study quizzes.
- **Test Mode** — Retrieval practice at the edge of your knowledge with persistent gap tracking across sessions.

### [startup-evaluator](./startup-evaluator/)

Evaluate startups with the rigor of a top-tier VC — covering value proposition, market, team, defensibility, unit economics, technical approach, and website/content quality. Synthesises classic frameworks (Sequoia, Helmer's 7 Powers, Gurley, YC, a16z, NFX) with AI-era considerations into structured, actionable reports. Includes reference libraries on foundational frameworks, moats & defensibility, unit economics, adtech/attention economics, and AI-era dynamics.

### [agent-report-annotation](./agent-report-annotation/)

Annotate AI-assisted reports with authority tiers to signal which claims are the human author's own positions vs. agent-generated analysis. Three tiers: **Author** (human's direct experience or strong conviction), **Reviewed** (human engaged critically), **Deferred** (agent-generated, read but not independently verified). Useful for maintaining credibility and transparency in co-authored analysis.

## Installation

Copy a skill folder into your Claude Code skills directory:

```bash
cp -r <skill-folder> ~/.claude/skills/
```

Or install directly from this repo:

```bash
git clone https://github.com/jackleekopij/claude-skills.git
cp -r claude-skills/<skill-name> ~/.claude/skills/
```

## Contributing

Have a skill to share? PRs welcome. Each skill should live in its own folder with a `SKILL.md` file containing the skill definition (frontmatter + instructions).

## License

MIT
