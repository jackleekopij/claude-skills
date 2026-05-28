# Theme: Corporate Trust

**Source**: designprompts.dev — Enterprise / Corporate Trust theme  
**Vibe**: Modern enterprise SaaS. Trustworthy yet vibrant. Polished, dimensional, approachable.

---

## Design Philosophy

This style embodies the modern enterprise SaaS aesthetic — professional yet approachable, sophisticated yet friendly. It draws inspiration from tech unicorns and high-growth startups that have successfully humanized the corporate experience. The design rejects the cold, sterile formality of traditional corporate websites in favor of a warm, confident, and inviting presence.

**Emotional keywords**: Trustworthy, vibrant, polished, dimensional, modern, approachable, enterprise-ready, elegant.  
**Influences**: Linear, Vercel, Stripe, Notion — companies that made "corporate" feel premium.

**Visual DNA** — the unmistakable signatures of this style:
1. **Colored Shadows**: Soft shadows with blue/purple tints instead of neutral grays
2. **Isometric Elements**: Subtle 3D transforms (rotate-x, rotate-y) on decorative cards
3. **Gradient Text**: Strategic use of indigo→violet gradient text for headline emphasis
4. **Soft Blobs**: Large, blurred gradient orbs in the background for atmospheric depth
5. **Elevated Cards**: White cards that lift on hover with enhanced shadows
6. **Dual-Tone Palette**: Indigo (primary) + Violet (secondary) creating a cohesive gradient spectrum

---

## Design Token System

### Colors (Light Mode)

```
background:        #F8FAFC   -- Slate 50, very subtle cool grey/white base
foreground:        #FFFFFF   -- White, for cards and raised elements
primary:           #4F46E5   -- Indigo 600, core brand color
secondary:         #7C3AED   -- Violet 600, for gradients and accents
textMain:          #0F172A   -- Slate 900, high contrast
textMuted:         #64748B   -- Slate 500, supporting text
accent:            #10B981   -- Emerald 500, positive indicators / success
border:            #E2E8F0   -- Slate 200, subtle separation
input:             #FFFFFF   -- White input backgrounds
ring:              #4F46E5   -- Indigo 600, focus ring matches primary
destructive:       #EF4444   -- Red 500, error/danger
```

**Gradient tokens**:
```
primaryGradient:   from #4F46E5 to #7C3AED   -- Indigo→Violet, buttons & active states
textGradient:      from #4F46E5 to #7C3AED   -- Combined with bg-clip-text text-transparent
bgSubtle:          from #EEF2FF to #EDE9FE   -- Indigo-100 → Violet-100, container tints
ctaDark:           from #312E81 to #1E1B4B   -- Indigo-900 → Indigo-950, dark CTA section
```

### Typography

```
fontFamily:        'Plus Jakarta Sans', system-ui, sans-serif
googleFontsImport: @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap')
```

| Role | Weight | Size (desktop) | Size (mobile) | Line Height | Letter Spacing |
|------|--------|---------------|---------------|-------------|----------------|
| Hero headline | 800 (ExtraBold) | text-5xl / text-6xl | text-3xl / text-4xl | 1.1 | -0.02em |
| Section heading | 700 (Bold) | text-3xl / text-4xl | text-2xl | 1.2 | -0.01em |
| Card title | 600 (SemiBold) | text-lg / text-xl | text-lg | 1.3 | normal |
| Body | 400 (Regular) | text-base | text-base | 1.6–1.7 | normal |
| Nav / Labels | 500 (Medium) | text-sm | text-sm | 1.5 | normal |

**Scale**: Major Third (1.250). Tight tracking on headlines for modern polish.

### Radius & Border

```
cardRadius:        12px   -- rounded-xl
inputRadius:       8px    -- rounded-lg
buttonRadius:      9999px -- rounded-full (primary), 8px / rounded-lg (secondary)
border:            1px solid #E2E8F0
```

### Shadows & Effects

This is where the design truly shines. **Colored shadows** replace neutral grays.

```
shadowDefault:     0 4px 20px -2px rgba(79, 70, 229, 0.1)
shadowHover:       0 10px 25px -5px rgba(79, 70, 229, 0.15), 0 8px 10px -6px rgba(79, 70, 229, 0.1)
shadowButton:      0 4px 14px 0 rgba(79, 70, 229, 0.3)
shadowGlow:        0 0 20px rgba(79, 70, 229, 0.5)
```

**Background blobs**: Large (400–600px) circular gradients with heavy blur, positioned absolutely, 20–50% opacity, `filter: blur(64px)` or Tailwind `blur-3xl`.

### Spacing & Layout

```
maxWidth:          1280px  -- max-w-7xl
sectionPadding:    64px mobile / 80px tablet / 96px desktop  -- py-16 / sm:py-20 / lg:py-24
containerPadding:  16px mobile / 24px desktop  -- px-4 / sm:px-6
```

**Grid patterns**:
- Hero: Two-column `lg:grid-cols-2`, text-first
- Features: Alternating zig-zag with `lg:flex-row` / `lg:flex-row-reverse`
- Pricing: Three-column `md:grid-cols-3` with center emphasis (`md:scale-105`)
- Stats: Four-column `md:grid-cols-4`
- Text width: `max-w-xl` or `max-w-2xl` for 60–75 char line lengths

---

## Component Stylings

### Buttons

**Primary**: Gradient background (Indigo→Violet). `rounded-full` or `rounded-lg`. White text. Shadow: `shadowButton`. Hover: lift `translateY(-2px)` and increase shadow.

```css
.btn-primary {
  background: linear-gradient(135deg, #4F46E5, #7C3AED);
  color: #fff;
  border-radius: 9999px;
  padding: 12px 28px;
  font-weight: 600;
  box-shadow: 0 4px 14px 0 rgba(79, 70, 229, 0.3);
  transition: all 200ms ease-out;
}
.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px 0 rgba(79, 70, 229, 0.4);
}
```

**Secondary**: White background, border `#E2E8F0`, text `#334155` (Slate 700). Hover: `background: #F8FAFC`, darker border.

```css
.btn-secondary {
  background: #fff;
  color: #334155;
  border: 1px solid #E2E8F0;
  border-radius: 9999px;
  padding: 12px 28px;
  font-weight: 600;
  transition: all 200ms ease-out;
}
.btn-secondary:hover {
  background: #F8FAFC;
  border-color: #CBD5E1;
  transform: translateY(-1px);
}
```

### Cards

**Base**: White background, `border-radius: 12px`, `border: 1px solid rgba(226,232,240,0.8)`, `box-shadow: shadowDefault`.

**Hover**: Lift `translateY(-4px)` + enhanced shadow.

```css
.card {
  background: #fff;
  border-radius: 12px;
  border: 1px solid rgba(226, 232, 240, 0.8);
  box-shadow: 0 4px 20px -2px rgba(79, 70, 229, 0.1);
  transition: all 200ms ease-out;
}
.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 25px -5px rgba(79, 70, 229, 0.15),
              0 8px 10px -6px rgba(79, 70, 229, 0.1);
}
```

**Feature icon containers**: `width: 48px; height: 48px; border-radius: 12px; background: #EEF2FF; color: #4F46E5;` (indigo-50 bg, indigo-600 icon).

### Inputs

```css
input, select, textarea {
  background: #fff;
  border: 1px solid #E2E8F0;
  border-radius: 8px;
  padding: 10px 14px;
  font-size: 14px;
  transition: all 150ms ease-out;
}
input:focus, select:focus, textarea:focus {
  outline: none;
  border-color: #4F46E5;
  box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.15);
}
```

### Tables

Header row: `background: #F8FAFC; font-weight: 600; color: #0F172A; text-transform: uppercase; font-size: 12px; letter-spacing: 0.05em`. Row hover: `background: #FAFAFE`. Borders: bottom `1px solid #E2E8F0`.

### Badges / Status

Small pill badges: `border-radius: 9999px; padding: 4px 12px; font-size: 12px; font-weight: 600`.
- Success: `background: #ECFDF5; color: #059669`
- Primary: `background: #EEF2FF; color: #4F46E5`
- Warning: `background: #FFFBEB; color: #D97706`

---

## Bold Choices (Mandatory)

These are **required** for authentic Corporate Trust implementations. Skipping them produces a generic result.

### 1. Colored Shadows (Not Neutral Gray)

Every elevated element (cards, buttons, dropdowns, modals) must use **indigo-tinted shadows**, never `rgba(0,0,0,...)`. This is the single most distinctive trait.

### 2. Gradient Text Headlines

At least one prominent headline per page uses gradient text:

```css
.gradient-text {
  background: linear-gradient(135deg, #4F46E5, #7C3AED);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
```

Apply selectively — typically to the second half of a hero headline or a section title keyword.

### 3. Isometric 3D Transforms

At least one decorative element (hero visual, feature card, dashboard preview) uses subtle 3D perspective:

```css
.isometric-container { perspective: 2000px; }
.isometric-card {
  transform: rotateX(5deg) rotateY(-12deg);
  transition: transform 300ms ease-out;
}
.isometric-card:hover {
  transform: rotateX(2deg) rotateY(-8deg);
}
```

### 4. Background Blur Orbs

At least one section has atmospheric gradient blobs behind the content:

```css
.blob {
  position: absolute;
  width: 500px;
  height: 500px;
  border-radius: 50%;
  filter: blur(80px);
  opacity: 0.25;
  pointer-events: none;
}
.blob-indigo { background: #818CF8; top: -100px; right: -100px; }
.blob-violet { background: #A78BFA; bottom: -100px; left: -100px; }
```

### 5. Card Hover Lift

All interactive cards must lift on hover with enhanced shadow. No flat hover states.

### 6. Split Headline Pattern

Hero headlines split styling: first words in `textMain` (#0F172A), key phrase in gradient text. Creates visual hierarchy without additional markup weight.

---

## Animation & Transitions

**Philosophy**: "Refined Motion" — smooth, professional, never jarring.

```
baseTransition:    all 200ms ease-out
longTransition:    all 500ms ease-out   -- image zooms, complex animations
```

**Hover effects**:
- Cards: `translateY(-4px)` + shadow enhancement
- Buttons: `translateY(-2px)` + shadow enhancement
- Arrow icons: `translateX(4px)` on group hover
- Images: `scale(1.05)` on group hover with overlay fade-in

**Decorative motion**: `animation: pulse 4s ease-in-out infinite` on floating elements for gentle breathing effect. Respect `prefers-reduced-motion`.

---

## Iconography

**Library**: Lucide icons (or any consistent stroke icon set).

```
defaultSize:       16px (h-4 w-4) inline, 20px (h-5 w-5) featured, 24px (h-6 w-6) prominent
strokeWidth:       2px
joins:             rounded
```

**Icon containers**:
- Small: `48px × 48px, border-radius: 12px, background: #EEF2FF, color: #4F46E5`
- Large: `56px × 56px, border-radius: 12px` for prominent features
- Circular: `border-radius: 50%` for avatars / status

**Color treatment**: Icons in `#4F46E5` (indigo) on `#EEF2FF` (indigo-50) container. Social icons: `#94A3B8` default, `#818CF8` on hover.

---

## Accessibility

- All text meets WCAG AA (Slate 900 on Slate 50 = AAA compliant)
- Focus: `outline: none; box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.3); outline-offset: 2px`
- Touch targets: minimum 44×44px
- `prefers-reduced-motion`: disable hover lifts and pulse animations
- Semantic HTML: proper heading hierarchy, native `<button>`, `<nav>`, `<details>`/`<summary>`

---

## CSS Variables (Copy-Paste Ready)

```css
:root {
  --bg: #F8FAFC;
  --surface: #FFFFFF;
  --primary: #4F46E5;
  --secondary: #7C3AED;
  --text: #0F172A;
  --text-muted: #64748B;
  --accent: #10B981;
  --border: #E2E8F0;
  --destructive: #EF4444;

  --gradient-primary: linear-gradient(135deg, #4F46E5, #7C3AED);
  --gradient-bg: linear-gradient(135deg, #EEF2FF, #EDE9FE);
  --gradient-cta: linear-gradient(135deg, #312E81, #1E1B4B);

  --shadow-sm: 0 4px 20px -2px rgba(79, 70, 229, 0.1);
  --shadow-md: 0 10px 25px -5px rgba(79, 70, 229, 0.15), 0 8px 10px -6px rgba(79, 70, 229, 0.1);
  --shadow-btn: 0 4px 14px 0 rgba(79, 70, 229, 0.3);
  --shadow-glow: 0 0 20px rgba(79, 70, 229, 0.5);

  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-full: 9999px;

  --font: 'Plus Jakarta Sans', system-ui, sans-serif;
  --transition: all 200ms ease-out;
}
```
