---
name: notion-second-brain
description: >
  Read from and write to Kyle's Notion Second Brain. Use this skill whenever the user wants
  to add a note, save an idea, log something, file something away, create a task, write a
  journal entry, update Notion, or mentions "second brain", "notion", "add to my notes",
  "save this", "log this", "file this", "add a task", "to do", "remind me", "journal entry",
  or asks what projects or topics exist. Also trigger when the user shares something worth
  capturing (research finding, meeting outcome, decision, idea) and asks you to save it.
  When in doubt, use this skill — it's better to trigger unnecessarily than to miss a capture.
---

# Notion Second Brain

Kyle's Second Brain lives in Notion and follows a PARA-adjacent structure. This skill
governs how to capture artefacts into it correctly.

## Setup

The token is stored at `~/.notion_token` (chmod 600). The script reads from there automatically.
The integration is named "AI MCP" in Kyle's Notion workspace.

Run all operations via the bundled script:

```bash
python3 ~/.agents/skills/notion-second-brain/scripts/notion.py <command>
```

Alternatively, set `NOTION_TOKEN` in the environment (overrides the file).

## Database IDs (hardcoded in notion.py, listed here for reference)

| Database          | ID                                     |
|-------------------|----------------------------------------|
| Notes             | `1f7fa8e2-920b-81a8-9522-cbe0f406e9ad` |
| Projects          | `1f7fa8e2-920b-815c-8048-fcfaca0a10b8` |
| Topics            | `1f7fa8e2-920b-81bd-93c9-ed9c9957a487` |
| Tasks             | `1f3fa8e2-920b-808e-9b74-f023a477d541` |
| Journal           | `1f4fa8e2-920b-814a-86d2-ed04dc37a029` |
| Areas             | `21afa8e2-920b-8014-b156-ea987d6a2b00` |

Second Brain root page: `1f9fa8e2-920b-8032-b444-f473da012765`

---

## Artefact Types

### Note → Notes DB
Used for: ideas, research findings, meeting notes, observations, reference material,
anything that doesn't have a deadline or checkbox.

**Required:**
- `Name` — a concise, descriptive title
- `Projects + Notebooks` — at least one, resolved dynamically (see below)
- `Topics` — at least one, resolved dynamically (see below)

**Optional:** `Due`, `Content` (paragraph body)

### Task → Tasks DB
Used for: anything actionable with a time horizon.

**Key fields:**
- `Name` — the action (start with a verb)
- `Time Horizon` — one of: `Today`, `Tomorrow`, `This Week`, `Next Week`, `This Month`, `Someday`
- `Work Style` — `Deep Work` or `Shallow Work`
- `Projects + Notebooks` — link to the relevant project (resolved dynamically)
- `Due` — ISO date (YYYY-MM-DD) if there's a specific deadline

### Journal Entry → Journal DB
Used for: daily/weekly reflections, mood logs, check-ins.

**Key fields:**
- `Name` — typically the date or a short description
- `Journal Type` — e.g. `Daily`, `Weekly`, `Reflection`, `Gratitude` (create new if needed)
- `Mood` — e.g. `Good`, `Great`, `Neutral`, `Low` (create new if needed)
- `Energy` — e.g. `High`, `Medium`, `Low` (create new if needed)
- `Content` — the actual journal text

---

## Dynamic Tag Resolution — ALWAYS DO THIS

Before creating any Note or Task, you must resolve which Projects and Topics to tag it with.
**Never guess or hardcode IDs.** The list changes over time as projects are created/archived.

### Step 1: Fetch available options

```bash
python3 ~/.agents/skills/notion-second-brain/scripts/notion.py list-projects
python3 ~/.agents/skills/notion-second-brain/scripts/notion.py list-topics
```

This gives you a live list of `ID → Name` pairs.

### Step 2: Match to context

- Read the content being captured.
- Find the best matching Project(s) and Topic(s) from the live list.
- If multiple are relevant, include all of them (Notes support multi-relation).

### Step 3: Handle missing options

If no existing Project or Topic is a good fit:
- **Propose the new name** to the user before creating it: *"I don't see a Project for X. Should I use Y instead, or create a new one called X?"*
- If the user confirms a new one: create it first in the relevant DB via the Notion API, then use its new ID.
- For Topics, creating a new entry is fine without asking if the intent is clear from context.

---

## Reading Page Content

To read the full content of any Notion page (note, task, journal entry), use `read-page` with the page ID
(obtained from `search` results):

```bash
python3 ~/.agents/skills/notion-second-brain/scripts/notion.py read-page <page-id>
```

This outputs the page title and all block content as plain text (headings, bullets, code blocks, etc.).
Use this to review existing notes, cross-reference content, or check what's already captured before
deciding whether to update or create new pages.

---

## IMPORTANT: Search Before Creating

Before creating any new Note or Task, **always search for existing pages** that cover the same topic.
Use the `search` command to check if a page already exists that should be updated/appended to:

```bash
# Search across notes, tasks, and journal by title
python3 ~/.agents/skills/notion-second-brain/scripts/notion.py search "search terms"

# Search only a specific database
python3 ~/.agents/skills/notion-second-brain/scripts/notion.py search "search terms" --db notes
python3 ~/.agents/skills/notion-second-brain/scripts/notion.py search "search terms" --db tasks
```

**Search with multiple relevant terms** — try the project name, key nouns, abbreviations, and synonyms.
Do at least 2-3 searches with different terms before concluding no page exists.

If a matching page exists:
- Use `append` to add new content to it rather than creating a duplicate.
- If the user explicitly says "update the note", find and append to the existing page.

Only create a new note if no existing page covers the topic.

---

## Workflow: Adding a Note

```bash
# 1. Fetch projects and topics
python3 ~/.agents/skills/notion-second-brain/scripts/notion.py list-projects
python3 ~/.agents/skills/notion-second-brain/scripts/notion.py list-topics

# 2. Pick best matches, then create the note
python3 ~/.agents/skills/notion-second-brain/scripts/notion.py add-note \
  "Your Note Title" \
  --project-id <matched-project-id> \
  --topic-id <matched-topic-id> \
  --content "Optional body text"
```

## Workflow: Adding a Task

```bash
# 1. Fetch projects
python3 ~/.agents/skills/notion-second-brain/scripts/notion.py list-projects

# 2. Create the task
python3 ~/.agents/skills/notion-second-brain/scripts/notion.py add-task \
  "Verb-led task name" \
  --project-id <matched-project-id> \
  --horizon "Today" \
  --work-style "Deep Work" \
  --due "2026-04-20"
```

## Workflow: Adding a Journal Entry

```bash
python3 ~/.agents/skills/notion-second-brain/scripts/notion.py add-journal \
  "Daily Journal 2026-04-19" \
  --journal-type "Daily" \
  --mood "Good" \
  --energy "High" \
  --content "Today I..."
```

## Workflow: Uploading a full markdown file

Use this when the content is a full document (report, long note, research), not just a snippet.
It creates a new Note page and uploads the full content as structured Notion blocks.

```bash
python3 ~/.agents/skills/notion-second-brain/scripts/notion.py upload-md \
  "Note Title" \
  /path/to/file.md \
  --project-id <matched-project-id> \
  --topic-id <matched-topic-id>
```

After uploading, delete the source file if it was a loose desktop/tmp file — Notion is now the source of truth.

If the upload fails mid-way (e.g. ISP drop), the page will have been created. Use `resume-upload` to
append the full block set to the existing page rather than creating a duplicate:

```bash
python3 ~/.agents/skills/notion-second-brain/scripts/notion.py resume-upload \
  <existing-page-id> /path/to/file.md
```

Note: `resume-upload` re-uploads all blocks, so only use it on an empty page.

## Workflow: Appending to an existing page

```bash
python3 ~/.agents/skills/notion-second-brain/scripts/notion.py append \
  <page-id> "Text to append"
```

## Workflow: Archiving a page

```bash
python3 ~/.agents/skills/notion-second-brain/scripts/notion.py archive \
  <page-id>
```

---

## API notes (important for future changes)

- **Block appends use `PATCH`**, not `POST`. The endpoint is `PATCH /blocks/{id}/children`.
  `POST /blocks/{id}/children` returns 400. This applies to both `append` and `upload-md`.
- **Page creation uses `POST /pages`** and can include `children` inline (up to ~100 blocks).
  For large documents, create the page first then upload blocks separately via `resume-upload`.
- **Archiving uses `PATCH /pages/{id}`** with `{"archived": true}`.

---

## Confirming with the user

After creating any entry, always:
1. Show the Notion URL returned by the script so the user can click through and verify.
2. Briefly summarise what was filed and which Project/Topic tags were applied.

Example response:
> Filed to Notes DB: **"ISP fault diagnosis notes"**
> Tagged: Project → *GILT*, Topic → *Networking*
> [Open in Notion](https://www.notion.so/...)

---

## Error handling

The `notion.py` script retries up to 15 times with 3s delays (handles the current ISP fault).
If it still fails, tell the user the connection is down and suggest they retry later.

---

## Notes on the Second Brain structure

- **Projects** are time-bounded efforts with a clear outcome (e.g. "GILT Whitepaper", "AGSM Application").
- **Areas** are ongoing responsibilities (e.g. "Health", "Home", "Work"). Notes don't link directly to Areas — they link to Projects, which link to Areas.
- **Topics** are the taxonomy layer — cross-cutting themes like "AI", "Nutrition", "Leadership". A note can have multiple Topics.
- **Resources** DB is for reference material (books, links, tools) — distinct from Notes.
- Archived Projects/Topics are filtered out from `list-projects` and `list-topics` automatically.
