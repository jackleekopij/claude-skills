# Theme: Woodside Energy

**Source**: Woodside Energy Brand Guide — External & Internal, November 2024  
**Vibe**: Industrial authority meets digital precision. Navy depth, Woodside Red confidence, clean engineering aesthetic.

---

## Design Philosophy

This style embodies a **resource-sector technology leader** — the visual authority of a major energy company combined with the clarity and polish of a modern digital product. It rejects generic corporate blandness and SaaS sameness in favour of a distinct identity: clean white/grey canvas, sharp Woodside Red and navy accents, and a typographic system built for engineers and operators who need information fast.

**The default mode is light.** White cards on a cool-grey page, navy type, with Woodside Red and blue used as accent, not background. Reserve the full dark navy treatment for hero banners, CTA blocks, or sections where maximum brand punch is needed. Dark-mode-everything is a common mistake with this palette — resist it.

**Emotional keywords**: Authoritative, precise, engineered, confident, clean, trustworthy, bold.  
**Influences**: Woodside Energy brand system (Nov 2024), Linear/Stripe enterprise aesthetic, industrial operational clarity.

**Visual DNA** — the unmistakable signatures of this style:
1. **Light Canvas First**: `#f0f4f8` cool-grey page background, white card surface — Woodside brand bg token. Navy and red appear as accent, not as backdrop.
2. **Red as Active Signal**: Woodside Red `#d71638` marks the active/current state — the Now column, primary CTAs, key stat highlights, left-border accents on in-focus items. Never as large-area fill.
3. **Navy as Typography**: `#001543` for headings and strong labels — far more readable and premium on a white card than generic dark grey.
4. **Blue Accent Spectrum**: `#00aeef` (Blue 3) and `#0071bc` (Blue 2) for secondary accents, chips, badges, and "next" horizon signals. `#e1f4fd` (Blue 5) for light chip fills.
5. **Condensed Display Type**: Barlow Condensed for headlines, quarter labels, stat numbers — the industrial, engineered feel that distinguishes this from generic SaaS.
6. **Data-Forward Stats**: Large condensed numerals with tight tracking in navy or light-navy ghost — numbers are first-class visual elements.
7. **Operational Cards**: White cards with a 3px top accent line (red for active/now, blue for next, grey for later/done) — inspired by control room panel styling but clean and modern.

---

## Design Token System

### Colors (Light Mode)

```
background:        #f0f4f8   -- Cool grey-blue base (not pure white)
foreground:        #ffffff   -- White, for cards and raised elements
primary:           #d71638   -- Woodside Red — core brand, CTAs, key accents
secondary:         #00aeef   -- Blue 3 — highlights, interactive elements, step markers
textMain:          #001543   -- Navy — headings (stronger than generic dark gray)
textBody:          #4d4d4f   -- Dark Grey — body text, taglines, descriptions
textMuted:         #6b7a8d   -- Muted blue-grey — supporting text, captions
accent:            #51b848   -- Green — positive indicators, success states
warning:           #f58220   -- Orange — alerts, callouts, highlights
border:            #d9e2ec   -- Cool grey border
input:             #ffffff   -- White input backgrounds
ring:              #0071bc   -- Blue 2 — focus ring
destructive:       #d71638   -- Woodside Red doubles as destructive (contextual)
```

### Colors (Dark Mode — for hero sections, dark cards, CTA blocks)

```
darkBg:            #001543   -- Navy, primary dark background
darkCard:          #003369   -- Blue 1, card/panel on dark
darkBorder:        rgba(255,255,255,0.08)  -- Subtle white border on dark
darkTextPrimary:   #ffffff   -- White headings
darkTextBody:      #90d1f3   -- Blue 4, body text on dark
darkTextMuted:     rgba(255,255,255,0.45)  -- Low-contrast labels on dark
darkAccentBg:      rgba(0,174,239,0.10)    -- Blue ghost for chips/badges on dark
```

**Gradient tokens**:
```
redGradient:       linear-gradient(135deg, #d71638, #a81028)     -- Red accent gradient (CTAs, banner)
blueGradient:      linear-gradient(135deg, #00aeef, #0071bc)     -- Blue accent gradient (step numbers, highlights)
navyGradient:      linear-gradient(135deg, #001543, #003369 40%, #004080)  -- Dark section backgrounds
lightCard:         linear-gradient(145deg, #ffffff, #f8fafc)     -- Subtle card gradient
ctaDark:           linear-gradient(135deg, #001543, #00152f)     -- Deep dark CTA section
```

### Typography

```
fontFamily:        'Barlow', system-ui, sans-serif
fontDisplay:       'Barlow Condensed', 'Barlow', sans-serif
googleFontsImport: @import url('https://fonts.googleapis.com/css2?family=Barlow:wght@300;400;500;600;700;800&family=Barlow+Condensed:wght@600;700;800&display=swap')
```

Barlow is the official web substitute for DIN 2014 (Woodside's corporate typeface). Barlow Condensed is used for display/headline roles where DIN 2014 Bold would appear in print.

| Role | Font | Weight | Size (desktop) | Size (mobile) | Line Height | Letter Spacing |
|------|------|--------|---------------|---------------|-------------|----------------|
| Hero headline | Barlow Condensed | 800 | text-5xl / text-6xl | text-3xl / text-4xl | 1.1 | -0.01em |
| Section heading | Barlow Condensed | 700 | text-3xl / text-4xl | text-2xl | 1.15 | -0.005em |
| Card title | Barlow | 600 (SemiBold) | text-lg / text-xl | text-lg | 1.3 | normal |
| Body | Barlow | 400 (Regular) | text-base | text-base | 1.6 | normal |
| Nav / Labels | Barlow | 500 (Medium) | text-sm | text-sm | 1.5 | normal |
| Stat numbers | Barlow Condensed | 800 | text-4xl / text-5xl | text-3xl | 1.0 | -0.02em |
| Section labels | Barlow | 700 | text-xs | text-xs | 1.4 | 0.12em (uppercase) |

### Radius & Border

```
cardRadius:        8px    -- rounded-lg (not overly rounded — engineered feel)
inputRadius:       6px    -- rounded-md
buttonRadius:      6px    -- rounded-md (primary), 9999px / rounded-full for pill variant
border:            1px solid #d9e2ec
darkBorder:        1px solid rgba(255,255,255,0.08)
```

Woodside's aesthetic is more squared-off than typical SaaS — 8px radius, not 12px+. This gives the industrial, engineered feel.

### Shadows & Effects

**Brand-colored shadows** using navy and blue tints — never neutral gray.

```
shadowDefault:     0 2px 12px -2px rgba(0, 21, 67, 0.08)
shadowHover:       0 8px 24px -4px rgba(0, 21, 67, 0.12), 0 4px 8px -2px rgba(0, 21, 67, 0.06)
shadowButton:      0 4px 14px 0 rgba(215, 22, 56, 0.25)
shadowButtonBlue:  0 4px 14px 0 rgba(0, 113, 188, 0.25)
shadowGlow:        0 0 20px rgba(0, 174, 239, 0.4)
shadowNavy:        0 4px 20px -4px rgba(0, 21, 67, 0.2)
```

**Key rule**: Elevated elements use navy-tinted shadows (`rgba(0, 21, 67, ...)`). Red buttons get red-tinted shadows. Blue interactive elements get blue-tinted shadows. Never `rgba(0,0,0,...)`.

### Spacing & Layout

```
maxWidth:          1280px  -- max-w-7xl
sectionPadding:    64px mobile / 80px tablet / 96px desktop
containerPadding:  16px mobile / 24px desktop
```

**Grid patterns**:
- Hero: Two-column `lg:grid-cols-2`, text-first on left, visual on right
- Features: Alternating zig-zag or 3-column `md:grid-cols-3` card grid
- Stats: Four-column `md:grid-cols-4` with large condensed numbers
- Dashboard/Data: Dense grids with tight 8px gaps — operational density
- Text width: `max-w-xl` or `max-w-2xl` for 60–75 char line lengths

---

## Component Stylings

### Buttons

**Primary (Red)**: Woodside Red with red gradient. Squared radius. White text. Red-tinted shadow. Hover: darken + lift.

```css
.btn-primary {
  background: linear-gradient(135deg, #d71638, #a81028);
  color: #fff;
  border-radius: 6px;
  padding: 12px 28px;
  font-family: 'Barlow', sans-serif;
  font-weight: 600;
  font-size: 14px;
  letter-spacing: 0.02em;
  box-shadow: 0 4px 14px 0 rgba(215, 22, 56, 0.25);
  transition: all 200ms ease-out;
  border: none;
}
.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px 0 rgba(215, 22, 56, 0.35);
  filter: brightness(1.05);
}
```

**Secondary (Blue outline)**: White background, blue border, navy text. Hover: blue tint fill.

```css
.btn-secondary {
  background: #fff;
  color: #001543;
  border: 1.5px solid #0071bc;
  border-radius: 6px;
  padding: 11px 28px;
  font-family: 'Barlow', sans-serif;
  font-weight: 600;
  font-size: 14px;
  transition: all 200ms ease-out;
}
.btn-secondary:hover {
  background: #e1f4fd;
  border-color: #00aeef;
  transform: translateY(-1px);
}
```

**Dark context button**: White text, transparent with white border. Hover: white fill with navy text.

```css
.btn-dark {
  background: transparent;
  color: #fff;
  border: 1.5px solid rgba(255,255,255,0.3);
  border-radius: 6px;
  padding: 11px 28px;
  font-weight: 600;
  transition: all 200ms ease-out;
}
.btn-dark:hover {
  background: #fff;
  color: #001543;
  border-color: #fff;
}
```

### Cards

**Light card**: White background, subtle navy shadow, 8px radius, colored top accent line.

```css
.card {
  background: linear-gradient(145deg, #fff, #f8fafc);
  border-radius: 8px;
  border: 1px solid rgba(0, 21, 67, 0.06);
  box-shadow: 0 2px 12px -2px rgba(0, 21, 67, 0.08);
  transition: all 200ms ease-out;
  position: relative;
  overflow: hidden;
}
.card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
  background: linear-gradient(135deg, #00aeef, #0071bc);
}
.card:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 24px -4px rgba(0, 21, 67, 0.12),
              0 4px 8px -2px rgba(0, 21, 67, 0.06);
}
```

**Dark card (navy)**: For stats, hero panels, data-dense sections.

```css
.card-dark {
  background: linear-gradient(135deg, #001543, #003369 40%, #004080);
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.08);
  color: #fff;
  position: relative;
  overflow: hidden;
}
.card-dark::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 2px;
  background: linear-gradient(135deg, #00aeef, #0071bc);
}
```

**Feature icon containers**: `width: 48px; height: 48px; border-radius: 8px; background: #e1f4fd; color: #0071bc;` (Blue 5 bg, Blue 2 icon).

### Section Labels

Uppercase micro-label with left accent line — a Woodside infographic signature.

```css
.section-label {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-family: 'Barlow', sans-serif;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #0071bc;
  margin-bottom: 8px;
}
.section-label::before {
  content: '';
  width: 14px;
  height: 2px;
  background: linear-gradient(135deg, #00aeef, #0071bc);
  border-radius: 2px;
}
```

### Stat Blocks

Large condensed numbers with supporting label — the "data-forward" signature.

```css
.stat-number {
  font-family: 'Barlow Condensed', 'Barlow', sans-serif;
  font-size: 48px;
  font-weight: 800;
  line-height: 1;
  letter-spacing: -0.02em;
  color: #90d1f3;
  margin-bottom: 4px;
}
.stat-label {
  font-size: 12px;
  font-weight: 500;
  color: rgba(255, 255, 255, 0.5);
  line-height: 1.3;
}
```

### Inputs

```css
input, select, textarea {
  background: #fff;
  border: 1px solid #d9e2ec;
  border-radius: 6px;
  padding: 10px 14px;
  font-family: 'Barlow', sans-serif;
  font-size: 14px;
  color: #001543;
  transition: all 150ms ease-out;
}
input:focus, select:focus, textarea:focus {
  outline: none;
  border-color: #0071bc;
  box-shadow: 0 0 0 3px rgba(0, 113, 188, 0.15);
}
```

### Tables

Header row: `background: #001543; color: #90d1f3; font-weight: 700; text-transform: uppercase; font-size: 11px; letter-spacing: 0.08em`. Row hover: `background: #e1f4fd`. Borders: bottom `1px solid #d9e2ec`.

### Badges / Status

Pill badges: `border-radius: 9999px; padding: 4px 12px; font-size: 12px; font-weight: 600`.
- Success: `background: rgba(81,184,72,0.12); color: #3a8a33`
- Primary (blue): `background: rgba(0,174,239,0.10); color: #0071bc`
- Alert: `background: rgba(245,130,32,0.12); color: #d06d15`
- Critical (red): `background: rgba(215,22,56,0.10); color: #d71638`
- Milestone (gold): `background: rgba(255,212,0,0.15); color: #b39400; border: 1px solid rgba(255,212,0,0.3)`

---

## Bold Choices (Mandatory)

These are **required** for authentic Woodside implementations. Skipping them produces a generic corporate result.

### 1. Navy-Tinted Shadows (Not Neutral Gray)

Every elevated element must use **navy-tinted shadows** (`rgba(0, 21, 67, ...)`). Red buttons get red-tinted shadows (`rgba(215, 22, 56, ...)`). Never `rgba(0,0,0,...)`.

### 2. Red Gradient Accent Text

At least one prominent headline uses Woodside Red gradient text:

```css
.gradient-text {
  background: linear-gradient(135deg, #d71638, #a81028);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
```

Use selectively — the key phrase in a hero headline, a stat number on light background, or a section title keyword. Never entire paragraphs.

### 3. Colored Top-Accent Lines on Cards

Every card has a thin (2–3px) gradient line at its top edge. Blue gradient (`#00aeef → #0071bc`) for standard cards. Red gradient (`#d71638 → #a81028`) for highlighted/featured cards. Implemented via `::before` pseudo-element.

### 4. Navy Hero/CTA Sections

At least one major section uses the deep navy gradient background (`#001543 → #003369 → #004080`). This is not optional dark mode — it's the Woodside signature. White text, blue-accent elements, red CTAs.

### 5. Condensed Display Numbers

All statistics, metrics, and large numbers use Barlow Condensed 800 with tight letter-spacing. Numbers are visual anchors — large, bold, and immediately scannable. On dark backgrounds: `color: #90d1f3`. On light backgrounds: `color: #001543`.

### 6. Section Label + Left Line Pattern

Section headings are preceded by an uppercase micro-label with a left accent line (blue gradient). This is borrowed from the Woodside infographic system and must appear on every content section.

### 7. Left Border Accent on Callouts

Important callout boxes, blockquotes, and challenge/opportunity sections use a 3px left border in Woodside Red (`#d71638`). This replaces generic box highlighting.

---

## Animation & Transitions

**Philosophy**: "Engineered Precision" — smooth, deliberate, confident. No playful bouncing.

```
baseTransition:    all 200ms ease-out
longTransition:    all 400ms ease-out
```

**Hover effects**:
- Cards: `translateY(-3px)` + shadow enhancement (subtle — not dramatic)
- Buttons: `translateY(-2px)` + shadow and brightness boost
- Arrow icons: `translateX(4px)` on group hover
- Table rows: background color transition, no lift

**No decorative motion**: No floating elements, no pulse animations, no blur orb animations. The Woodside brand is grounded and operational. Motion serves function — hover feedback, transitions, loading states — not decoration.

**Exception**: Data visualizations and charts may use entrance animations (fade + slide) for progressive disclosure.

---

## Iconography

**Library**: Lucide icons, or any consistent stroke icon set.

```
defaultSize:       16px inline, 20px featured, 24px prominent
strokeWidth:       2px
joins:             rounded
```

**Icon containers**:
- Standard: `48px × 48px, border-radius: 8px, background: #e1f4fd, color: #0071bc`
- On dark: `48px × 48px, border-radius: 8px, background: rgba(0,174,239,0.10), color: #00aeef`
- Red accent: `48px × 48px, border-radius: 8px, background: rgba(215,22,56,0.10), color: #d71638`

**Color treatment**: Icons match their container context — blue on light, cyan on dark, red for alerts/emphasis.

---

## Accessibility

- All text meets WCAG AA: Navy `#001543` on `#f0f4f8` background exceeds AAA. White on `#001543` exceeds AAA.
- Focus: `outline: none; box-shadow: 0 0 0 3px rgba(0, 113, 188, 0.3); outline-offset: 2px`
- Touch targets: minimum 44×44px
- `prefers-reduced-motion`: disable hover lifts, skip entrance animations
- Semantic HTML: proper heading hierarchy, native buttons, nav/footer landmarks

---

## CSS Variables (Copy-Paste Ready)

```css
@import url('https://fonts.googleapis.com/css2?family=Barlow:wght@300;400;500;600;700;800&family=Barlow+Condensed:wght@600;700;800&display=swap');

:root {
  /* Brand primary */
  --wd-red: #d71638;
  --wd-red-dark: #a81028;
  --wd-red-light: #ff3356;
  --wd-red-ghost: rgba(215, 22, 56, 0.10);

  /* Navy blues */
  --navy: #001543;
  --navy-mid: #003369;
  --blue: #0071bc;
  --blue-light: #00aeef;
  --blue-pale: #90d1f3;
  --blue-wash: #e1f4fd;
  --blue-ghost: rgba(0, 174, 239, 0.10);

  /* Accents */
  --green: #51b848;
  --orange: #f58220;
  --gold: #ffd400;

  /* Neutral */
  --bg: #f0f4f8;
  --surface: #ffffff;
  --text: #001543;
  --text-body: #4d4d4f;
  --text-muted: #6b7a8d;
  --border: #d9e2ec;

  /* Gradients */
  --gradient-red: linear-gradient(135deg, #d71638, #a81028);
  --gradient-blue: linear-gradient(135deg, #00aeef, #0071bc);
  --gradient-navy: linear-gradient(135deg, #001543, #003369 40%, #004080);
  --gradient-card: linear-gradient(145deg, #fff, #f8fafc);

  /* Shadows (navy-tinted) */
  --shadow-sm: 0 2px 12px -2px rgba(0, 21, 67, 0.08);
  --shadow-md: 0 8px 24px -4px rgba(0, 21, 67, 0.12), 0 4px 8px -2px rgba(0, 21, 67, 0.06);
  --shadow-btn-red: 0 4px 14px 0 rgba(215, 22, 56, 0.25);
  --shadow-btn-blue: 0 4px 14px 0 rgba(0, 113, 188, 0.25);
  --shadow-glow: 0 0 20px rgba(0, 174, 239, 0.4);

  /* Layout */
  --radius-sm: 6px;
  --radius-md: 8px;
  --radius-full: 9999px;
  --max-width: 1280px;

  /* Typography */
  --font: 'Barlow', system-ui, sans-serif;
  --font-display: 'Barlow Condensed', 'Barlow', sans-serif;
  --transition: all 200ms ease-out;
}
```
