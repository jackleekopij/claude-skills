# Theme: Cyberpunk / Glitch

**Source**: designprompts.dev — Cyberpunk theme  
**Vibe**: High-Tech, Low-Life. Digital dystopia. Hacker noir. CRT grit.

---

## Design Philosophy

The aesthetic is a digital dystopia colliding with high-tech noir. Advanced technology meets societal decay — underground hackers, neon-drenched megacities, corrupted data streams. Every pixel should feel like it's being rendered on a malfunctioning CRT monitor in a rain-soaked alley or a rogue terminal in a subterranean bunker.

**Emotional keywords**: Dangerous, electric, rebellious, aggressively futuristic-retro.  
**Influences**: Blade Runner, Akira, Ghost in the Shell, The Matrix.

The interface should feel *alive* and volatile — buzzing with digital energy, glitching with data corruption, pulsing with raw power. It's not just a website; it's a hacked feed, a forbidden interface.

---

## Design Token System

### Colors (Dark Mode — Mandatory)

```
background:        #0a0a0f   -- Deep void black, slight blue undertone
foreground:        #e0e0e0   -- Primary text (not pure white — less harsh)
card:              #12121a   -- Card background, deep purple-black
muted:             #1c1c2e   -- UI chrome / elevated backgrounds
mutedForeground:   #6b7280   -- Secondary text, reduced contrast
accent:            #00ff88   -- PRIMARY NEON: Electric green (Matrix)
accentSecondary:   #ff00ff   -- SECONDARY NEON: Hot magenta/pink
accentTertiary:    #00d4ff   -- TERTIARY NEON: Cyan/electric blue
border:            #2a2a3a   -- Subtle borders
input:             #12121a   -- Deep input background
ring:              #00ff88   -- Focus ring matches accent
destructive:       #ff3366   -- Error/danger red-pink
```

**Absolute rule**: These are the only colors. No pastels, no warm tones, no grays besides `mutedForeground`.

### Typography

**Font Stack**:
- **Headings / Title**: `"Orbitron", "Share Tech Mono", monospace` — geometric, futuristic, robotic
- **Body / Monospace**: `"JetBrains Mono", "Fira Code", "Consolas", monospace` — terminal feel
- **Labels / Badges**: `"Share Tech Mono", monospace`

**Load from Google Fonts** (add to `<head>`):
```html
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Share+Tech+Mono&display=swap" rel="stylesheet">
```

**Scale & Styling**:
- H1: 6xl–8xl, font-black, uppercase, tracking-widest
- H2: 4xl–5xl, font-bold, uppercase, tracking-wide
- Body: base, tracking-wide, leading-relaxed
- Labels/Code: sm, monospace, uppercase, tracking-[0.2em]

### Borders & Radius

```
Default:      0px radius — sharp cuts are the norm
Chamfer:      Use clip-path, NOT border-radius
```

**Chamfered corner clip-path** (standard size — 10px cut):
```css
clip-path: polygon(
  0 10px, 10px 0,
  calc(100% - 10px) 0, 100% 10px,
  100% calc(100% - 10px), calc(100% - 10px) 100%,
  10px 100%, 0 calc(100% - 10px)
);
```

**Small chamfer** (6px cut, for buttons and inputs):
```css
clip-path: polygon(
  0 6px, 6px 0,
  calc(100% - 6px) 0, 100% 6px,
  100% calc(100% - 6px), calc(100% - 6px) 100%,
  6px 100%, 0 calc(100% - 6px)
);
```

### Neon Glow Shadows

```css
/* Primary accent glow (green) */
--glow-accent: 0 0 5px #00ff88, 0 0 10px #00ff8840;
--glow-accent-lg: 0 0 10px #00ff88, 0 0 20px #00ff8860, 0 0 40px #00ff8830;

/* Secondary glow (magenta) */
--glow-secondary: 0 0 5px #ff00ff, 0 0 20px #ff00ff60;

/* Tertiary glow (cyan) */
--glow-tertiary: 0 0 5px #00d4ff, 0 0 20px #00d4ff60;

/* Destructive glow (red-pink) */
--glow-destructive: 0 0 5px #ff3366, 0 0 20px #ff336660;
```

### Background Textures (REQUIRED — prevents flat look)

**1. Scanlines overlay** (on `body::after` or a fixed overlay div — STATIC, not animated):
```css
background: repeating-linear-gradient(
  0deg,
  transparent,
  transparent 2px,
  rgba(0, 0, 0, 0.3) 2px,
  rgba(0, 0, 0, 0.3) 4px
);
pointer-events: none;
z-index: 9999;
position: fixed;
inset: 0;
opacity: 0.12;
```

**Important**: Scanlines must be STATIC. Do NOT animate/scroll them — that causes a distracting wavering effect. The scanlines should be a fixed texture overlay, like a CRT screen.

**2. Circuit grid pattern** (on body or section backgrounds):
```css
background-image:
  linear-gradient(rgba(0, 255, 136, 0.03) 1px, transparent 1px),
  linear-gradient(90deg, rgba(0, 255, 136, 0.03) 1px, transparent 1px);
background-size: 50px 50px;
```

**3. Radial accent bleed** (large faint glow in corner — add to body):
```css
background: radial-gradient(ellipse at top left, rgba(0, 255, 136, 0.04) 0%, transparent 60%),
            radial-gradient(ellipse at bottom right, rgba(255, 0, 255, 0.03) 0%, transparent 60%);
```

---

## Component Patterns

### Buttons

All buttons share:
- Font: monospace, uppercase, letter-spacing: 0.15em
- Transition: all 150ms
- No rounded corners — use small chamfer clip-path

**Primary (green accent)**:
```css
background: transparent;
border: 2px solid #00ff88;
color: #00ff88;
clip-path: [small chamfer];
/* Hover: */
background: #00ff88;
color: #0a0a0f;
box-shadow: var(--glow-accent);
```

**Destructive / E-Stop (red)**:
```css
background: #ff3366;
color: #fff;
border: none;
box-shadow: var(--glow-destructive);
/* Hover: increases glow intensity */
```

**Secondary (magenta)**:
```css
border: 2px solid #ff00ff;
color: #ff00ff;
/* Hover: fills magenta, --glow-secondary */
```

**Ghost / Utility**:
```css
background: #1c1c2e;
border: 1px solid #2a2a3a;
color: #6b7280;
/* Hover: border → accent, color → accent */
```

### Cards / Panels

**Standard card**:
```css
background: #12121a;
border: 1px solid #2a2a3a;
clip-path: [standard chamfer 10px];
transition: all 300ms;
/* Hover (optional): border → accent, box-shadow: --glow-accent */
```

**Terminal variant** (event logs, data feeds):
```css
background: #0a0a0f;
border: 1px solid #2a2a3a;
/* Add decorative header bar: */
/* ::before with 3 dots (red/amber/green) or ">" prompt prefix */
font-family: "JetBrains Mono", monospace;
```

### Status Badges

Use accent color family mapped to state semantics:
```
idle        → border: #00d4ff (cyan) — neutral/ready
moving      → border: #00ff88 + glow, animate pulse
holding     → border: #00ff88, static glow
e_stopped   → background: #ff3366, glow-destructive + blink
disconnected → border: #2a2a3a, color: #6b7280 — dim/dead
boot        → border: #ff00ff, glow-secondary — loading
```

### Data Tables

```css
/* Header row */
th { color: #00ff88; text-transform: uppercase; letter-spacing: 0.15em; border-bottom: 1px solid #2a2a3a; }

/* Data cells */
td { font-family: "JetBrains Mono", monospace; font-variant-numeric: tabular-nums; }

/* Alternating rows */
tr:nth-child(even) { background: rgba(0, 255, 136, 0.02); }

/* Hover row */
tr:hover { background: rgba(0, 255, 136, 0.05); }
```

### Event Log / Terminal Feed

```css
background: #0a0a0f;
border: 1px solid #2a2a3a;
font-family: "JetBrains Mono", monospace;
font-size: 0.78em;
color: #00ff88;
padding: 8px 12px;
/* Each line prefixed with > or timestamp in mutedForeground */
/* Newest entries appear brighter; fade older ones with opacity */
```

### Inputs

```css
background: #12121a;
border: 1px solid #2a2a3a;
color: #00ff88;
font-family: monospace;
clip-path: [small chamfer];
/* Focus: border → accent, box-shadow: --glow-accent-sm */
/* Placeholder: #6b7280, italic */
```

---

## Animations (REQUIRED Keyframes)

```css
@keyframes blink {
  50% { opacity: 0; }
}

/* Intermittent glitch — NOT continuous. Fires briefly every ~6s. */
@keyframes cyberGlitch {
  0%, 92%, 100% { text-shadow: none; transform: none; }
  93%  { text-shadow: -2px 0 #ff00ff, 2px 0 #00d4ff; transform: translate(-1px, 0); }
  94%  { text-shadow: 2px 0 #ff00ff, -2px 0 #00d4ff; transform: translate(1px, 0); }
  95%  { text-shadow: -1px 0 #ff00ff, 1px 0 #00d4ff; transform: translate(0, 1px); }
  96%  { text-shadow: none; transform: none; }
}

@keyframes neonPulse {
  0%, 100% { box-shadow: 0 0 5px #00ff88, 0 0 10px #00ff8840; }
  50%       { box-shadow: 0 0 10px #00ff88, 0 0 20px #00ff8870, 0 0 40px #00ff8830; }
}

@keyframes bootSequence {
  0%   { opacity: 0; transform: translateY(4px); }
  100% { opacity: 1; transform: translateY(0); }
}
```

**Important**: Glitch/chromatic effects must be INTERMITTENT, not continuous. A constant wobbling `rgbShift` looks cheap. The reference implementation uses a ~6s cycle where 92-96% of the time the text is clean, and the glitch fires for a brief 0.3s burst. This is much more cinematic.

**Usage**:
- Title: `animation: cyberGlitch 6s ease-in-out infinite` with 3s delay — intermittent burst
- Title text: use gradient (`linear-gradient(90deg, #e0e0e0, #ff00ff, #00ff88)`) with `background-clip: text`
- E-Stop badge: `animation: neonPulse 1s ease-in-out infinite`
- Cursor in terminal: `animation: blink 1s step-end infinite`
- Moving state badge: `animation: neonPulse 0.5s ease-in-out infinite`

---

## Bold Choices (All MANDATORY)

1. **Scanline overlay** — fixed position, full-screen, 0.08 opacity for content sites (0.12 for dashboards), STATIC (not scrolling) — creates CRT texture. Disable in light mode.
2. **Subtle radial bleed** — green top-left + magenta bottom-right at 0.03 opacity. NOT grid lines on content sites (too busy). Grid lines OK for dashboards.
3. **Intermittent glitch on title** — `cyberGlitch` animation, NOT continuous RGB shift. 6s in dark, 8s in light.
4. **Gradient text on hero title** — multi-color gradient (white → magenta → cyan → green) with `background-clip: text`. Dark gets neon, light gets muted tones.
5. **Dual accent system** — green/emerald for primary elements + magenta/purple for secondary. Never use just one accent color everywhere.
6. **Terminal-style subtitle** — monospace font, green `>` prompt prefix, left border
7. **Orbitron display font** — for hero title and section headings. Load from Google Fonts.
8. **Glowing dividers** — section transitions use accent-colored border with box-shadow glow
9. **Section labels as badges** — bordered inline-block badges, not plain text headings. Primary and alt variants.
10. **Neon glow on hover** — cards, social links, toggles get glow box-shadow or drop-shadow on hover. Light mode uses subtle colored shadows instead.
11. **Dark mode default** — always default to dark. Light mode is an adaptation, not the base.

---

## What Success Looks Like

A successfully themed cyberpunk UI should feel like:
- A hacker's terminal in a sci-fi film
- The UI from Blade Runner or Ghost in the Shell
- A military HUD overlaid on reality

It should NOT look like:
- A generic dark mode app (dark ≠ cyberpunk)
- Bootstrap dark theme
- Anything with rounded corners

---

## Content Site Recipes

The patterns above cover dashboards and apps. For **blogs, portfolios, landing pages**, use these recipes. They show how the tokens compose into full page sections.

### Hero Section

The hero is the statement piece. It must feel like a system booting up.

```html
<section class="hero">
  <h1 class="hero-title">SITE NAME</h1>
  <p class="hero-subtitle">Tagline or description here.</p>
  <p class="hero-meta">A site by <strong>Author Name</strong></p>
</section>
<div class="hero-divider"></div>
```

```css
.hero-title {
  font-family: var(--font-display); /* Orbitron */
  font-weight: 900;
  font-size: clamp(2.5rem, 6vw, 5rem);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  /* Multi-color gradient text — ties all accent colors together */
  background: linear-gradient(90deg, #e0e0e0, #ff00ff, #00d4ff, #00ff88);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: cyberGlitch 6s ease-in-out infinite 3s;
}
/* Light mode: use darker, muted version of same gradient */
[data-theme="light"] .hero-title {
  background: linear-gradient(90deg, #1a1a2e, #7b1fa2, #0077aa, #00805a);
  -webkit-background-clip: text;
  background-clip: text;
  animation-duration: 8s; /* slower, subtler */
}

/* Terminal-style subtitle with green prompt */
.hero-subtitle {
  font-family: var(--font-mono); /* JetBrains Mono */
  font-size: 0.95rem;
  color: var(--color-muted-fg);
  padding-left: 16px;
  border-left: 2px solid var(--color-accent); /* green */
}
.hero-subtitle::before {
  content: "> ";
  color: var(--color-accent);
  font-weight: bold;
}

/* Author name in secondary accent */
.hero-meta strong {
  color: var(--color-accent-secondary); /* magenta dark, purple light */
}

/* Glowing divider line */
.hero-divider {
  border: none;
  border-bottom: 1px solid var(--color-accent);
  position: relative;
}
.hero-divider::after {
  content: "";
  position: absolute;
  bottom: -1px;
  left: 0;
  right: 0;
  height: 1px;
  box-shadow: var(--glow-accent);
}
```

### Dual Accent System

Don't use green for everything — it flattens the hierarchy. Use two accent tones:

| Role | Dark Mode | Light Mode | Usage |
|------|-----------|------------|-------|
| Primary | `#00ff88` (neon green) | `#00805a` (emerald) | Main headings, badges, borders, prompts, primary hover |
| Secondary | `#ff00ff` (magenta) | `#7b1fa2` (purple) | Author name, dates, alt badges, section dividers, secondary hover |
| Tertiary | `#00d4ff` (cyan) | `#0077aa` (teal) | Links, minor accents |

**Where to use secondary accent:**
- Card dates / timestamps
- Author name in hero
- Section dividers between content areas
- Alternate section labels (e.g. "Podcast" vs "Blog")
- Theme toggle hover state
- Social link hover state (with drop-shadow glow)
- Nav text hover

### Section Labels (Badge Style)

```css
.section-label {
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  padding: 4px 12px;
  border: 1px solid var(--color-accent);
  color: var(--color-accent);
}
/* Alternate label for secondary sections */
.section-label--alt {
  border-color: var(--color-accent-secondary);
  color: var(--color-accent-secondary);
}
```

### Section Dividers

Use the secondary accent for dividers between major content areas — creates visual rhythm.

```css
.section-divider {
  border: none;
  border-top: 1px solid var(--color-accent-secondary);
  box-shadow: var(--glow-secondary);
  margin: 3rem 0;
}
[data-theme="light"] .section-divider {
  border-color: #7b1fa2;
  opacity: 0.3;
  box-shadow: none;
}
```

### Blog / Content Cards

```css
.card {
  background: var(--color-card);
  border: 1px solid var(--color-border);
  transition: all 300ms;
}
.card:hover {
  border-color: var(--color-accent);
  box-shadow: var(--glow-accent-lg);
}
/* Card date in secondary accent */
.card-date {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: var(--color-accent-secondary);
  opacity: 0.7;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
/* Card image with consistent aspect ratio */
.card-image {
  aspect-ratio: 11/10;
  background-color: var(--color-card);
  overflow: hidden;
}
.card-image img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}
```

### Navigation

```css
.nav-brand {
  font-family: var(--font-display);
  font-weight: 700;
  text-transform: lowercase;
  letter-spacing: 0.05em;
  color: var(--color-accent);
}
.nav-brand:hover {
  color: var(--color-accent-secondary); /* magenta/purple on hover */
}
```

### Social Links

```css
.social-link {
  color: var(--color-muted-fg);
  transition: all 200ms;
}
.social-link:hover {
  color: var(--color-accent-secondary);
  filter: drop-shadow(0 0 6px var(--color-accent-secondary));
}
[data-theme="light"] .social-link:hover {
  color: #7b1fa2;
  filter: none; /* no glow in light mode */
}
```

### Dark/Light Mode Toggle

Support both modes. Dark is default.

```css
.theme-toggle {
  background: transparent;
  border: 1px solid var(--color-border);
  color: var(--color-muted-fg);
  cursor: pointer;
  transition: all 200ms;
}
.theme-toggle:hover {
  border-color: var(--color-accent-secondary);
  color: var(--color-accent-secondary);
}
```

**Flash prevention script** (put in `<head>` before stylesheets):
```html
<script>
(function() {
  var theme = localStorage.getItem('theme') || 'dark';
  if (theme === 'light') {
    document.documentElement.setAttribute('data-theme', 'light');
  }
})();
</script>
```

### Background Atmosphere

Keep it subtle. The background should feel alive but not distract.

```css
body {
  background-color: var(--color-bg);
  background-image:
    radial-gradient(ellipse at top left, rgba(0, 255, 136, 0.03) 0%, transparent 50%),
    radial-gradient(ellipse at bottom right, rgba(255, 0, 255, 0.03) 0%, transparent 50%);
}
```

**Dial**: The radial bleed opacity (0.03) is the sweet spot. Higher (0.06) makes the background feel tinted/muddy. Lower (0.01) is invisible. Circuit grid lines are optional — they can feel busy on content sites.

**Scanlines**: Keep at 0.08 opacity for content sites (vs 0.12 for dashboards). Disable entirely in light mode.

---

## Light Mode Token Overrides

When supporting light mode, override these tokens under `[data-theme="light"]`:

```css
[data-theme="light"] {
  --color-bg: #fafafa;
  --color-surface: #ffffff;
  --color-card: #ffffff;
  --color-text: #1a1a2e;
  --color-heading: #0d0d0d;
  --color-muted-fg: #6b7280;
  --color-border: #e0e0e0;
  --color-accent: #00805a;          /* emerald (muted green) */
  --color-accent-secondary: #7b1fa2; /* purple (muted magenta) */
  --color-accent-tertiary: #0077aa;  /* teal (muted cyan) */
  --color-link: #0077aa;
}
```

**Key light mode rules:**
- No scanlines (opacity: 0)
- No radial bleed (background-image: none)
- No neon glow shadows — use subtle colored box-shadows instead
- Glitch animation duration 8s (slower, less aggressive)
- Card hover: subtle colored shadow instead of neon glow
