# Theme: Minimalist Monochrome

**Source**: designprompts.dev — Minimalist Monochrome theme  
**Vibe**: Editorial luxury. High-end fashion magazine. Stark black/white. Typography as graphic design.

---

## Design Philosophy

**Reduction to Essence.** Minimalist Monochrome strips design to its most fundamental elements: black, white, and typography. No accent colors to hide behind, no gradients to soften edges, no shadows to create false depth. Every design decision must stand on its own merit. This is design as discipline — restraint as the ultimate expression.

**Emotional keywords**: Austere, authoritative, timeless, editorial, intellectual, dramatic, refined, stark.  
**Influences**: Vogue/Harper's Bazaar covers, architectural monographs, luxury brand identities (Chanel, Celine), Bauhaus.

---

## Design Token System

### Colors (Strictly Monochrome — No Exceptions)

```
background:       #FFFFFF   -- Pure white
foreground:       #000000   -- Pure black
muted:            #F5F5F5   -- Off-white for subtle backgrounds
mutedForeground:  #525252   -- Dark gray for secondary text
accent:           #000000   -- Black IS the accent
accentForeground: #FFFFFF   -- White on black
border:           #000000   -- Black borders
borderLight:      #E5E5E5   -- Light gray for subtle dividers
card:             #FFFFFF   -- White cards
cardForeground:   #000000   -- Black text
ring:             #000000   -- Black focus rings
```

**Rule**: No other colors. Ever. Not even "almost black" grays for primary elements.

### Typography

**Font Stack**:
- **Display/Headlines**: `"Playfair Display", Georgia, serif` — elegant, high-contrast with beautiful italics
- **Body**: `"Source Serif 4", Georgia, serif` — highly readable serif for long-form text
- **Mono/Labels**: `"JetBrains Mono", monospace` — for dates, metadata, technical details

**Load from Google Fonts** (add to `<head>`):
```html
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Source+Serif+4:wght@400;600&display=swap" rel="stylesheet">
```

**Scale**: Use oversized type — headlines should dominate space (7xl–9xl on desktop). Words become graphic elements.

**Tracking & Leading**:
- Headlines: tracking-tight (-0.025em) or tracking-tighter (-0.05em)
- Body: tracking-normal
- Labels/Small caps: tracking-widest (0.1em)

### Borders & Radius

```
ALL: 0px — zero border-radius everywhere, no exceptions
```

**Border weights**:
```
hairline: 1px solid #E5E5E5  -- subtle dividers
thin:     1px solid #000000  -- standard borders
medium:   2px solid #000000  -- emphasis
thick:    4px solid #000000  -- section dividers, heavy rules
ultra:    8px solid #000000  -- maximum impact
```

### Shadows

**NONE.** Zero drop shadows. Depth is created through:
- Color inversion (black/white swap)
- Border weight variation
- Scale contrast
- Negative space

### Background Textures (Subtle — Required for Paper Quality)

**Horizontal lines** (global, very subtle):
```css
background-image: repeating-linear-gradient(
  0deg,
  transparent, transparent 1px,
  #000 1px, #000 2px
);
background-size: 100% 4px;
opacity: 0.015;
```

**Grid** (for editorial sections):
```css
background-image:
  linear-gradient(#00000008 1px, transparent 1px),
  linear-gradient(90deg, #00000008 1px, transparent 1px);
background-size: 40px 40px;
```

---

## Component Patterns

### Buttons

**Primary**:
- Background: #000000, Text: #FFFFFF
- Padding: generous (px-8 py-4)
- Font: uppercase, tracking-widest, font-medium, text-sm
- Hover: invert to white bg, black text, black border
- Transition: 100ms max

**Outline**:
- Background: transparent, Text: #000000, Border: 2px solid #000000
- Hover: fill black, text white

**Shape**: Always rectangular, zero radius. Consider small arrow (→) for CTAs.

### Cards

**Standard**:
- Background: #FFFFFF, Border: 1px solid #000000
- No shadow, no radius

**Inverted** (for emphasis):
- Background: #000000, Text: #FFFFFF

### Status / Badges

Use inversion for emphasis — black pill for active/primary states, light border for neutral states. No color.

### Tables

```css
th { border-bottom: 2px solid #000000; text-transform: uppercase; letter-spacing: 0.1em; }
td { border-bottom: 1px solid #E5E5E5; }
tr:hover { background: #F5F5F5; }
```

---

## Hover & Animation

**Motion Philosophy**: Minimal and instant. Maximum 100ms. Binary on/off states.

**Card hover**: Full color inversion (bg, text, borders) — 100ms
**Button hover**: Color inversion — instant (0ms)
**Link hover**: Underline appears — instant

**No**: bouncy animations, parallax, slow easing, gradient animations.

---

## Bold Choices (All MANDATORY)

1. **Oversized hero typography** — at least one text element at 7xl or larger
2. **4px thick horizontal rules** between all major sections
3. **Heavy section dividers** — thick black lines as structural anchors
4. **Inverted elements** for emphasis — black background/white text panels (no accent colors)
5. **Sharp everything** — zero border-radius across all elements
6. **Editorial pull quote style** — large italic serif for highlighted content  
7. **Typography as graphic design** — headlines that function as visual elements
8. **Instant interactions** — hover states that snap, not ease

---

## What Success Looks Like

A successfully themed monochrome UI should feel like:
- Opening a high-end fashion magazine
- Walking through a modern art gallery
- Reading a luxury brand's annual report

It should NOT look like:
- A generic blog template
- Dark mode with colors removed
- Anything with border-radius
