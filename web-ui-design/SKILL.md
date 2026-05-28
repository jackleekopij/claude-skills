---
name: web-ui-design
description: Apply a visual design theme to a web UI (HTML/CSS/JS, React, Vue, or any frontend). Loads themed design tokens, component patterns, typography, effects, and animation rules from bundled theme files. Use this skill whenever the user wants to restyle, redesign, or improve the visual appearance of a web app or page — especially when they mention a specific aesthetic ("cyberpunk", "minimalist", "noir", "brutalist", "glassmorphism", etc.), share a design system prompt, say a UI looks "ugly", "boring", or "like a kid made it", or ask to apply a theme. Also trigger when the user attaches an HTML/JS/CSS file and wants it re-skinned, or when they want a control panel, dashboard, or tool to look more polished.
---

# Web UI Design Skill

This skill helps apply a coherent visual design theme to any web UI. It is theme-driven: each theme lives as a standalone markdown file in `themes/` and contains its full design token system, component patterns, effects, and bold mandatory choices.

## Available Themes

| Theme | File | Vibe |
|-------|------|-------|
| Cyberpunk / Glitch | `themes/cyberpunk.md` | Neon-drenched, gritty, CRT scanlines, hacker aesthetic |
| Minimalist Monochrome | `themes/minimalist-monochrome.md` | Editorial luxury, stark black/white, serif typography |
| Corporate Trust | `themes/corporate-trust.md` | Modern enterprise SaaS, indigo→violet gradients, colored shadows, isometric depth |
| Woodside Energy | `themes/woodside-energy.md` | Industrial authority, navy depth, Woodside Red accents, condensed display type, operational cards |
| Obsidian Precision | `themes/obsidian-precision.md` | Neo-classical data platform, Cormorant Garamond italic, obsidian depth, golden ratio spacing, violet accents |

> **To add a new theme**: create a new file in `themes/` following the same structure. Add a row to this table.

---

## Workflow

### Step 1 — Load the right theme

Read the relevant `themes/*.md` file immediately. Never apply a theme from memory — always load from the file so the exact tokens and rules are in context.

### Step 2 — Identify the page type

Determine what kind of UI this is — it changes which patterns to apply:

| Page Type | Key Patterns |
|-----------|-------------|
| **Dashboard / Control Panel** | Status badges, data tables, event logs, terminal feeds, metric cards |
| **Content Site / Blog / Portfolio** | Hero section, blog cards, section dividers, navigation, social links, footer |
| **Landing Page / Marketing** | Hero with CTA, feature grid, pricing cards, testimonials, FAQ accordion |
| **Tool / Utility** | Input forms, output panels, progress indicators, action buttons |

Load the appropriate recipe sections from the theme file. Most themes have both dashboard and content site patterns.

### Step 3 — Audit the current UI

Before changing anything, identify:
- **Tech stack**: vanilla HTML/CSS/JS, React, Vue, embedded template string, etc.
- **Existing design tokens**: what CSS variables or classes are already defined?
- **Component inventory**: what elements exist — buttons, cards, tables, status badges, inputs, progress bars?- **Dark/light mode**: does the UI need both? Default to dark for cyberpunk themes.- **Constraints**: is this a self-contained HTML string (like a Python template)? Are external fonts/CDNs allowed? Any performance constraints?

### Step 3 — Map theme to components

Walk through each component in the existing UI and map the theme's patterns to it:
- Replace color values with theme palette
- Replace typography with theme font stack (load from Google Fonts if CDN is available)
- Apply theme's border/radius/shadow rules
- Add theme's mandatory background textures and effects
- Add theme's signature animations

### Step 4 — Apply systematically

Work section by section:
1. **CSS variables & global styles** — reset the palette, global typography, body background, scanlines/textures
2. **Layout containers** — grid, max-width, section spacing
3. **Cards & panels** — background, borders, radius/chamfer, shadows
4. **Interactive elements** — buttons, status badges, inputs
5. **Data displays** — tables, event logs, terminal output
6. **Animations & effects** — keyframes, hover states, glows
7. **Typography hierarchy** — headings, labels, monospace content

### Step 5 — Bold choices (mandatory)

Every theme has a "Bold Choices" or "Non-Genericness" section. These are **required** — they are what separates a real themed implementation from a generic reskin. Apply all of them.

### Step 6 — Transformation depth check

After applying the theme, verify you've gone deep enough. A common failure mode is "just applying colors" — swapping the palette but leaving the visual language untransformed. Check each item:

- [ ] **Hero/header is a statement piece** — not just colored text. Gradient text, terminal prompt, glowing divider, or animated title.
- [ ] **Multiple accent colors in use** — not just one primary color everywhere. Use a dual accent system (e.g., green primary + magenta secondary) with clear hierarchy.
- [ ] **Hover states are distinctive** — not just color change. Add glow, shadow, scale, or border transitions.
- [ ] **Section transitions are styled** — dividers, borders, or spacing changes between content areas. Not just margin.
- [ ] **Typography has personality** — display font for headings (Orbitron), monospace for meta content (JetBrains Mono), not just the body font everywhere.
- [ ] **Background has atmosphere** — radial bleed, subtle texture, scanlines — not flat solid color.
- [ ] **Interactive elements feel alive** — buttons, toggles, links respond with energy (glow, color shift, shadow).
- [ ] **Light mode is a real adaptation** — not just "invert colors". Muted accent tones, disabled effects, different shadows.

If any of these are unchecked, go back and add them before presenting to the user.

---

## Inline HTML Templates (Common Case)

When the UI is embedded as a Python (or other language) template string:
- Edit the string in-place; do not extract to a separate file
- Google Fonts `<link>` tags go inside `<head>`
- CSS keyframes and custom properties go in the `<style>` block
- No build step — everything must be self-contained

---

## Quality Check

Before finishing, verify:
- [ ] All theme colors used (no old palette remnants)
- [ ] All "Bold Choices" from the theme applied
- [ ] Existing functionality unchanged (JS logic, API calls, state updates)
- [ ] Accessibility maintained (contrast ratios, focus states)
- [ ] Syntax compiles clean (run `python -m py_compile` for Python files)
