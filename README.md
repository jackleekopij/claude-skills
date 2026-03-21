# Claude Code Skills

A public collection of custom skills for [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Install any skill into your own Claude Code setup and start using it immediately.

## Available Skills

### [optimal-learning](./optimal-learning/)

A research-backed learning system grounded in cognitive psychology (seven peer-reviewed studies on the testing effect, retrieval practice, and pretesting). Two modes:

- **Study Mode** — Pre-test, source material processing, Obsidian study note generation, NotebookLM podcast prompts, and post-study quizzes.
- **Test Mode** — Retrieval practice at the edge of your knowledge with persistent gap tracking across sessions.

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
