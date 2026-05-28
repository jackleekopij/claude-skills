# Theme: Obsidian Precision

**Source**: ausdata.ai — neo-classical data infrastructure aesthetic
**Reference sites**:
- Main site: https://www.ausdata.ai/en (hero globe, typography, obsidian palette)
- Console: https://console.ausdata.ai/ (bento cards, animated feature effects)
- Brand: https://www.ausdata.ai/en/brand

**Vibe**: Mathematical elegance. Classical typography meets dark obsidian depth. Swiss watchmaker builds a data platform. Golden ratio proportions. Refined technical authority.

---

## Design Philosophy

**Mathematical Precision as Visual Language.** Obsidian Precision uses the golden ratio (φ = 1.618) as its structural foundation — in spacing, gradient angles, opacity stops, and proportional hierarchies. Classical serif typography (Cormorant Garamond) delivers an editorial, almost academic gravitas, while near-black backgrounds create depth without harshness. The result is a system that feels both timeless and unmistakably technical.

**Emotional keywords**: Authoritative, precise, elegant, deep, mathematical, refined, structured, premium.
**Influences**: Scientific journals, Swiss typography, observatory interfaces, classical architecture, high-end API documentation (Stripe, Linear).

---

## Design Token System

### Colors — Dark Mode (Primary)

#### Obsidian Base Scale (Backgrounds)
```
obsidian:          #050505   -- Deepest background (body/page)
obsidianSurface:   #0a0a0a   -- Section backgrounds, footer
obsidianCard:      #101010   -- Card backgrounds, elevated panels
obsidianBorder:    #1e1e1e   -- Subtle structural borders
obsidianGhost:     #2a2a2a   -- Ghost borders, faint dividers
```

#### Gallery Scale (Text)
```
galleryFg:         #f5f5f5   -- Primary text (not pure white — warmer)
galleryMuted:      #cccccc   -- Secondary text, descriptions
galleryGhost:      #aaaaaa   -- Tertiary text, labels, timestamps
galleryLine:       #2a2a2a   -- Divider lines
```

#### Border & Glass
```
borderLine:        #ffffff52  -- Semi-transparent white borders (32% opacity)
navBg:             #08080826  -- Nav background with glass effect (15% opacity)
navSeparator:      #ffffff12  -- Very subtle nav dividers (7% opacity)
navChipBorder:     #ffffff26  -- Chip/badge borders (15% opacity)
navChipBg:         #ffffff0a  -- Chip backgrounds (4% opacity)
```

#### Neural Accent Scale (Blue — Primary)
```
neural500:         #477eeb   -- Standard blue
neural400:         #6e98ed   -- Lighter blue (primary accent)
neural300:         #8fafef   -- Lightest blue (text accent)
```

#### Quantum Accent Scale (Violet — Secondary)
```
quantum500:        #6347eb   -- Standard violet
quantum400:        #836eed   -- Lighter violet (secondary accent)
quantum300:        #9f8fef   -- Lightest violet
```

#### Violet Atmosphere (UI Effects)
```
violetDim:         #4f46e51f  -- Faint violet wash (12% opacity)
violetGlow:        #4f46e580  -- Violet glow for hover/focus (50% opacity)
violetPure:        #4f46e5    -- Pure violet for active states
violetLight:       #818cf8    -- Light violet for borders and accents
```

#### Signal Colors (Sparingly)
```
quantumCyan:       #25d1f4   -- Data flow, connectivity
quantumEmerald:    #1ae6a2   -- Success, operational status
quantumAmber:      #fab338   -- Warning, attention
```

**Rule**: Neural (blue) is the primary accent for interactive elements. Quantum (violet) is secondary for emphasis and gradients. Signal colors (cyan, emerald, amber) are used only for semantic states — never decoratively.

### Colors — Light Mode

```
obsidian:          #fafaf8   -- Warm parchment background (NOT pure white)
obsidianSurface:   #f4f2ee   -- Slightly warmer surface
obsidianCard:      #eceae5   -- Card backgrounds
obsidianBorder:    #d8d5ce   -- Warm grey borders
obsidianGhost:     #b8b5ad   -- Ghost borders
galleryFg:         #0a0a0a   -- Near-black text
galleryMuted:      #2e2e2e   -- Secondary text
galleryGhost:      #444444   -- Tertiary text
galleryLine:       #e0ded9   -- Warm dividers
```

**Rule**: Light mode uses warm parchment tones, never cold whites. The violet/blue accents darken slightly but retain their hue. Never just "invert" — the warmth of the paper is the distinguishing trait.

### Gradients (Golden Ratio Stops)

All gradients use golden ratio proportions — 0%, 38.2%, 61.8%, 100% for stops. Gradient angle is 137.5° (the golden angle).

```css
--gradient-neural: linear-gradient(137.5deg, #477eeb 0%, #175de8 38.2%, #0f49bd 61.8%, #093690 100%);
--gradient-quantum: linear-gradient(137.5deg, #6347eb 0%, #2e2eea 38.2%, #2b6cee 61.8%, #0f5af0 100%);
--gradient-data-flow: linear-gradient(90deg, #477eeb 0%, #25d1f4 38.2%, #1ae6a2 100%);
--gradient-ai-core: radial-gradient(circle at 38.2% 38.2%, #6e98ed 0%, #477eeb 38.2%, #0f49bd 61.8%, #062460 100%);
```

### Typography

**Font Stack** (three-tier hierarchy):
- **Display/Headlines**: `"Cormorant Garamond", Georgia, serif` — elegant, high-contrast classical serif. Used in **italic** at weight 300 (light) for hero headings. Weight 600 for emphasis contrast.
- **Body/UI**: `"Inter", -apple-system, sans-serif` — clean, highly legible geometric sans for body text and UI elements.
- **Mono/Meta**: `"Space Mono", monospace` — technical monospace for labels, status text, code blocks, and metadata.

**Load from Google Fonts** (add to `<head>`):
```html
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,600;1,300;1,600&family=Inter:wght@300;400;500;600&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
```

**Type Scale**:
```
h1 (Hero):     44px, weight 300, italic, letter-spacing -1.54px, line-height 0.92
h1 (Alt):      44px, weight 600, normal, letter-spacing -1.54px (for emphasis words)
h2:            32px, weight 300, italic, letter-spacing -0.8px, line-height 1.2
h2 (Bold):     32px, weight 600, normal, letter-spacing -0.96px, opacity 0.382
h3:            20px, weight 600, normal, letter-spacing -0.4px, line-height 1.27
h4:            12px, weight 500, uppercase, letter-spacing 1.56px (0.13em), line-height 1.2
Labels:        10-11px, weight 400, uppercase, letter-spacing 1.3-1.56px
Body:          17px, weight 500, letter-spacing 0.136px, line-height 1.618 (golden ratio!)
Body small:    14px, weight 400, letter-spacing 0.08px, line-height 1.75
```

**Key typographic moves**:
- H1 is Cormorant Garamond in *italic* at light weight — this gives the editorial personality
- H2 uses a dual-weight system: italic 300 for primary + normal 600 at 0.382 opacity for secondary (golden ratio opacity!)
- H4 and labels use uppercase + extreme letter-spacing (0.13em) — a different typographic register entirely
- Body line-height is exactly φ (1.618)

### Borders & Radius

```
ALL: 0px border-radius — zero radius everywhere, no exceptions
```

**Border styles**:
```
subtle:        1px solid #ffffff52   -- Semi-transparent white (buttons, cards)
structural:    1px solid #1e1e1e    -- Obsidian border for sections
ghost:         1px solid #2a2a2a    -- Very faint structural lines
inset-glow:    inset 0 1px 0 #ffffff0a  -- Subtle top-edge shine on glass elements
cta-border:    1px solid rgba(129, 140, 248, 0.28)  -- Violet-tinted for primary CTAs
```

### Shadows

Minimal. Glass and light effects rather than drop shadows.

```css
/* Glass shine — inner top edge */
box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.04), 0 0 0 1px rgba(255, 255, 255, 0.02);

/* Nav scrolled state */
box-shadow: 0 4px 32px rgba(0, 0, 0, 0.55), 0 0 0 1px rgba(79, 70, 229, 0.1);

/* Nav default */
box-shadow: 0 8px 40px rgba(0, 0, 0, 0.4);
```

### Background Textures

**Noise overlay** (required — gives paper/film grain quality):
```css
.noise-overlay::after {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: 1;
  opacity: 0.025;
  mix-blend-mode: overlay;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
  background-repeat: repeat;
  background-size: 200px 200px;
}
```

**Geometric grid background** (hero section — very subtle):
Use a faint geometric line pattern at ~3% opacity, suggesting a coordinate system or mathematical grid.

### Spacing (Golden Ratio)

Use φ-derived spacing throughout:
```
section-py:     clamp(3.5rem, 6vw, 7rem)      -- Vertical section padding
section-px:     clamp(1.5rem, 4.236vw, 4.236rem) -- Horizontal section padding (4.236 = φ³)
section-py-sm:  clamp(2rem, 4vw, 4rem)          -- Smaller section padding
card-padding:   40px (p-10)                      -- Generous card padding
```

Key φ values used: `0.618rem`, `1rem`, `1.618rem`, `2.618rem`, `4.236rem`, `6.854rem`

---

## Component Patterns

### Navigation (Frosted Glass)

```css
nav {
  background: rgba(8, 8, 8, 0.15);        /* --nav-bg */
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.32);
  box-shadow: 0 8px 40px rgba(0, 0, 0, 0.4);
  position: fixed;
  top: 0;
  z-index: 50;
}
```

**Nav features**:
- System status indicator: green pulsing dot with "System operational" label
- Theme toggle button (dark/light)
- Language selector
- Hamburger menu for mobile
- All nav items: uppercase, letter-spacing 0.13em, Space Mono or Inter

### Buttons / CTAs

**Primary CTA** (Explore Products style):
```css
.btn-primary {
  background: transparent;
  color: rgba(248, 250, 252, 0.96);
  border: 1px solid rgba(129, 140, 248, 0.28);  /* violet-tinted border */
  border-radius: 0;
  padding: 14.4px 19.2px;
  font-size: 12px;
  font-weight: 400;
  letter-spacing: 1.56px;
  text-transform: uppercase;
  backdrop-filter: blur(8px);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.04), 0 0 0 1px rgba(255, 255, 255, 0.02);
  transition: all 500ms cubic-bezier(0.4, 0, 0.2, 1);
}
```

**Secondary CTA** (Go to Console style):
```css
.btn-secondary {
  background: rgba(12, 12, 18, 0.42);
  color: rgba(226, 232, 240, 0.92);
  border: 1px solid rgba(255, 255, 255, 0.32);
  border-radius: 0;
  padding: 14.4px 19.2px;
  font-size: 12px;
  letter-spacing: 1.56px;
  text-transform: uppercase;
  backdrop-filter: blur(6px);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.03);
}
```

Both CTAs include a trailing arrow icon (→) that shifts on hover.

**Text links**:
```css
.text-link {
  position: relative;
  color: #cccccc;
  transition: color 500ms ease-out;
}
.text-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 1px;
  background: currentColor;
  transform: scaleX(0);
  transition: transform 500ms ease-out;
  transform-origin: right;
}
.text-link:hover { color: #f5f5f5; }
.text-link:hover::after {
  transform: scaleX(1);
  transform-origin: left;
}
```

### Cards — Product/Feature Cards

**Standard product card**:
```css
.product-card {
  background: #101010;      /* obsidianCard */
  border: none;
  border-radius: 0;
  padding: 40px;             /* generous p-10 */
  transition: all 500ms cubic-bezier(0.4, 0, 0.2, 1);
}
```

**Card layout** (numbered):
- Number badge: large `01`, `02`, `03` in top corner — Inter or mono, oversized, low opacity
- Product icon: small icon/logo
- Title: H3 weight 600
- Description: body small (#cccccc)
- Stats block: large metric value (e.g. "5M+") + label underneath

Cards are laid out in a grid separated by 1px divider lines (obsidianBorder).

### Feature Badges (Pillars)

Three-column feature grid with icon + heading + description:
```
h4: uppercase, letter-spacing 0.13em, weight 500, 12px
p:  14px body text in galleryMuted
```
Each badge has a small icon (SVG) above the heading.

### Code Block

```css
.code-block {
  background: #0a0a0a;       /* obsidianSurface */
  border: 1px solid #1e1e1e; /* obsidianBorder */
  border-radius: 0;
  padding: 24px 32px;
  font-family: "Space Mono", monospace;
  font-size: 13px;
  line-height: 1.7;
  color: #818cf8;            /* violetLight — code is tinted violet */
}
.code-block .filename {
  font-size: 11px;
  text-transform: lowercase;
  letter-spacing: 0.5px;
  color: #aaaaaa;
  margin-bottom: 16px;
}
.code-block .comment {
  color: #666666;
  font-style: italic;
}
```

### Status Indicator (Heartbeat)

Green pulsing dot in the nav:
```css
.status-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;  /* exception: dots are round */
  background: #1ae6a2; /* quantumEmerald */
  animation: heartbeat 2s ease-in-out infinite;
}

@keyframes heartbeat {
  0%, 60%, 100% { opacity: 0.3; transform: scaleY(1); }
  10% { opacity: 1; transform: scaleY(1.6); }
  25% { opacity: 0.5; transform: scaleY(0.85); }
  35% { opacity: 0.85; transform: scaleY(1.3); }
}
```

### Section Headers

Pattern: uppercase label (Space Mono, 10-11px, tracking-widest, galleryGhost) above a Cormorant Garamond italic heading.

```html
<div class="section-header">
  <span class="section-label">PRODUCT SUITE</span>
  <h2>The Ausdata Matrix Family</h2>
</div>
```

### Footer

```css
footer {
  background: #0a0a0a;
  border-top: 1px solid rgba(255, 255, 255, 0.32);
  padding: var(--section-px);
  color: #cccccc;
  font-size: 14px;
}
```

Minimal footer with logo, copyright, and navigation links.

---

## Hover & Animation

**Motion Philosophy**: Smooth and deliberate. 500ms transitions for color/background changes. Cubic-bezier(0.4, 0, 0.2, 1) easing. No bouncy or playful motion — everything moves with intent.

**Entry animations**:
```css
@keyframes fadeUpBlur {
  0%   { opacity: 0; filter: blur(14px); transform: translateY(28px); }
  100% { opacity: 1; filter: blur(0);    transform: translateY(0); }
}
```

**Ambient motion**:
```css
@keyframes spotlightDrift {
  0%, 100% { transform: translate(0%) scale(1); }
  33%      { transform: translate(8%, -6%) scale(1.05); }
  66%      { transform: translate(-5%, 8%) scale(0.97); }
}

@keyframes neuralPulse {
  0%, 100% { opacity: 1; transform: scale(1); }
  50%      { opacity: 0.8; transform: scale(1.05); }
}

@keyframes glowPulse {
  0%, 100% { opacity: 0.35; }
  50%      { opacity: 0.8; }
}
```

**Card hover**: Background color transition, 500ms duration.
**Button hover**: Border and shadow intensify, arrow shifts right.
**Link hover**: Underline scales in from right to left, color brightens.

---

## Bold Choices (All MANDATORY)

1. **Cormorant Garamond italic for hero headings** — this is the personality of the theme. A classical serif in italic at light weight. Do not substitute with a sans-serif or a different serif.
2. **Golden ratio spacing** — use φ-derived values (0.618, 1.618, 2.618, 4.236) for padding, margins, and proportions. Gradient stops at 38.2% and 61.8%. Gradient angle at 137.5°.
3. **Obsidian depth** — three-level dark scale (#050505, #0a0a0a, #101010). Not just "dark mode" — intentionally deep near-black that reads as solid material.
4. **Noise texture overlay** on hero/main sections — SVG fractalNoise at 0.025 opacity with overlay blend mode. This gives tactile paper/film grain quality.
5. **Zero border-radius** on all rectangular elements (dots and circular indicators excepted). Sharp architectural edges define the style.
6. **Dual-weight heading system** — italic 300 paired with normal 600 at reduced opacity (0.382 = 1/φ) for typographic drama.
7. **Frosted glass navigation** — translucent bg, backdrop-filter blur, subtle inset glow, fixed position.
8. **500ms deliberate transitions** — no instant snaps, no 100ms. Everything moves at a considered, luxurious pace with cubic-bezier(0.4, 0, 0.2, 1).
9. **Violet-tinted CTA borders** — primary buttons have a faint indigo border (rgba(129, 140, 248, 0.28)) that gives them a subtle luminous quality without being loud.
10. **Uppercase + extreme tracking for labels** — H4, section labels, and meta text use uppercase with 0.13em letter-spacing. This creates a distinct typographic register that separates structural text from content text.

---

## Light Mode Adaptation

Light mode is NOT an inversion. It is a **warm parchment** variant:

- Background shifts to #fafaf8 (warm off-white, slightly yellow)
- Surfaces use #f4f2ee (warm cream)
- Cards use #eceae5 (light warm grey)
- Borders warm to #d8d5ce
- Text darkens to #0a0a0a / #2e2e2e
- Violet accents remain but darken slightly
- CTAs invert: dark background (#0a0a0a) with light text
- Noise overlay opacity can reduce to 0.015
- Geometric grid pattern becomes more visible

The overall feeling should be "reading a beautifully typeset paper journal" — warm, textured, refined.

---

## Signature Effect: Particle Globe (Three.js)

The hero section features a stunning interactive 3D particle globe built with **React Three Fiber** (R3F) + **Three.js r183**. This is the centrepiece visual and is worth recreating for hero sections in this theme.

### Architecture

The globe is composed of 4 layered components rendered inside an R3F `<Canvas>`:

1. **Particle Cloud** — ~2800 points distributed uniformly on a sphere using the **Fibonacci spiral** (golden angle = π(3−√5))
2. **Logo Mask** — An SVG logo rendered to a 2D canvas, sampled, and projected as particles onto the front hemisphere
3. **Node Markers** — 4 interactive product nodes at specific lat/long positions with glow halos
4. **Camera Drift** — Subtle mouse-following parallax on the camera position

### Canvas Setup

```jsx
<Canvas
  camera={{ position: [0, 0, 5.5], fov: 45 }}
  gl={{
    antialias: true,
    alpha: true,
    powerPreference: "high-performance",
    failIfMajorPerformanceCaveat: true,
  }}
  style={{ background: "transparent" }}
  dpr={[1, 2]}
>
  <Suspense fallback={null}>
    <CameraDrift />
    <ambientLight intensity={0.18} />          {/* dark mode: 0.18, light: 0.35 */}
    <directionalLight position={[4, 6, 5]} intensity={2.2} />
    <directionalLight position={[-3, -2, -3]} intensity={0.25} color="#8888ff" />
    <ParticleCloud count={2800} radius={1.8} isDark />
    <LogoMask radius={1.8} isDark fixed maxParticles={1200} maskResolution={320} />
    <NodeMarkers radius={1.8} isDark />
  </Suspense>
</Canvas>
```

### Component 1: Particle Cloud (Fibonacci Sphere)

Distributes points uniformly on a sphere using the golden angle, then renders as `<points>`:

```jsx
function ParticleCloud({ count = 2800, radius = 1.8, isDark }) {
  const positions = useMemo(() => {
    const pos = new Float32Array(count * 3);
    const sizes = new Float32Array(count);
    const goldenAngle = Math.PI * (3 - Math.sqrt(5));

    for (let i = 0; i < count; i++) {
      const y = 1 - (i / (count - 1)) * 2;            // -1 to 1
      const radiusAtY = Math.sqrt(1 - y * y);
      const theta = goldenAngle * i;

      pos[i * 3]     = Math.cos(theta) * radiusAtY * radius;
      pos[i * 3 + 1] = y * radius;
      pos[i * 3 + 2] = Math.sin(theta) * radiusAtY * radius;
      sizes[i] = 0.012 + 0.018 * Math.random();
    }
    return { positions: pos, sizes };
  }, [count, radius]);

  // Quaternion-based rotation with inertia (auto-rotate + drag)
  useFrame((_, delta) => {
    // Apply auto-rotation around Y axis
    // Apply drag quaternion if dragging
    // Apply mouse velocity for momentum
  });

  return (
    <points>
      <bufferGeometry>
        <bufferAttribute attach="attributes-position" args={[positions.positions, 3]} />
        <bufferAttribute attach="attributes-size" args={[positions.sizes, 1]} />
      </bufferGeometry>
      <pointsMaterial
        color={isDark ? "#ffffff" : "#111111"}
        size={0.022}
        sizeAttenuation
        transparent
        opacity={isDark ? 0.82 : 0.75}
        depthWrite={false}
      />
    </points>
  );
}
```

### Component 2: Logo Mask (SVG → Particle Projection)

Renders an SVG logo to a 2D canvas, samples white pixels, and projects them onto the sphere front hemisphere:

```jsx
function LogoMask({ radius = 1.8, isDark, maxParticles = 1200, maskResolution = 320, sampleStep = 2 }) {
  const [points, setPoints] = useState(null);

  useEffect(() => {
    // 1. Create an Image from SVG data URI
    // 2. Draw to a canvas at maskResolution × maskResolution
    // 3. Get imageData, scan pixels in sampleStep increments
    // 4. For white pixels (data > 128), project (x, y) → sphere surface:
    //    u = (col / (res-1)) * 2 - 1, scaled by logoScale
    //    v = -(row / (res-1)) * 2 - 1, scaled by logoScale
    //    z = sqrt(1 - u² - v²) if inside unit circle
    //    point = [u * radius, v * radius, z * radius]
    // 5. Randomly subsample to maxParticles if needed
    setPoints(new Float32Array(sampledPositions));
  }, [radius, maskResolution, sampleStep, maxParticles]);

  if (!points) return null;

  return (
    <group>
      {/* Spokes: line segments from each point to origin */}
      <lineSegments>
        <bufferGeometry>
          <bufferAttribute attach="attributes-position" args={[spokePositions, 3]} />
        </bufferGeometry>
        <lineBasicMaterial color={isDark ? "#22d3ee" : "#6366f1"} transparent opacity={0.02} depthWrite={false} />
      </lineSegments>

      {/* Logo particles */}
      <points>
        <bufferGeometry>
          <bufferAttribute attach="attributes-position" args={[points, 3]} />
        </bufferGeometry>
        <pointsMaterial
          color={isDark ? "#22d3ee" : "#6366f1"}
          size={0.016}
          sizeAttenuation
          transparent
          opacity={0.9}
          depthWrite={false}
        />
      </points>
    </group>
  );
}
```

### Component 3: Node Markers (Interactive Orbiting Nodes)

Four product nodes positioned at specific points on the sphere, with multi-layer glow effects:

```jsx
// Node definitions with positioned on sphere surface
const NODES = [
  { key: "matrix",   color: "#6366f1", size: 0.072, y: 0.65,  azimuth: 0.12 },
  { key: "blogflow", color: "#22d3ee", size: 0.064, y: 0.26,  azimuth: 0.60 },
  { key: "alpha",    color: "#f59e0b", size: 0.076, y: -0.30, azimuth: 0.88 },
  { key: "property", color: "#a525e0", size: 0.068, y: -0.70, azimuth: 0.26 },
];

// Each node renders 3 concentric spheres:
// 1. Outer glow:  SphereGeometry(2.8 * size), MeshBasicMaterial, opacity 0.055
// 2. Inner glow:  SphereGeometry(1.55 * size), MeshBasicMaterial, opacity 0.14
// 3. Solid core:  SphereGeometry(size, 48, 48), MeshStandardMaterial:
//                 roughness=0.3, metalness=0.55, emissive=color, emissiveIntensity=0.12

// Spoke lines from each node to origin
// Raycaster for hover detection → tooltip overlay (HTML positioned above canvas)
// Click opens product URL in new tab
```

### Component 4: Camera Drift

Subtle mouse-following camera with 0.04 lerp:

```jsx
function CameraDrift() {
  const { mouse } = useThree();
  useFrame(({ camera }) => {
    camera.position.x += (0.5 * mouse.x - camera.position.x) * 0.04;
    camera.position.y += (0.2 * mouse.y - camera.position.y) * 0.04;
    camera.lookAt(0, 0, 0);
  });
  return null;
}
```

### Interaction: Virtual Trackball Drag

The globe responds to pointer drag with quaternion-based rotation:

```javascript
// On pointer down: project mouse to virtual sphere surface
function projectToSphere(mx, my) {
  const r = Math.sqrt(mx * mx + my * my);
  const z = r < 0.8 ? Math.sqrt(0.64 - r * r) : 0.64 / (2 * r);
  return new Vector3(mx, my, z).normalize();
}

// On pointer move: compute quaternion between last and current projected vectors
deltaQ.setFromUnitVectors(lastVec, currentVec);

// On release: apply inertial decay via slerp toward identity quaternion
deltaQ.slerp(identityQ, 0.08);  // 8% decay per frame

// Auto-rotation: multiply by small Y-axis rotation each frame
autoRotQ.setFromAxisAngle(yAxis, 0.09 * delta);
rotation.premultiply(autoRotQ);

// Subtle pitch oscillation:
const pitchCorrection = (0.18 * Math.sin(0.12 * elapsed) - euler.x) * 0.02;
```

### Performance Adaptation

The component detects hardware capability and adjusts:

| Setting | Full | Lite | Fallback |
|---------|------|------|----------|
| Particle count | 2800 | 1400 | CSS circles only |
| Logo particles | 1200 | 420 | — |
| Mask resolution | 320 | 220 | — |
| DPR | [1, 2] | [1, 1.25] | — |
| Antialias | true | false | — |
| Fill light | yes | no | — |
| Sample step | 2 | 3 | — |

Detection checks: `hardwareConcurrency`, `deviceMemory`, `connection.saveData`, `prefers-reduced-motion`, WebGL context availability, software renderer detection.

### CSS Fallback (No WebGL)

When WebGL is unavailable, render concentric CSS circles with dashed borders:

```css
.sphere-fallback {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  border: 1px solid rgba(129, 140, 248, 0.25);
  background: radial-gradient(
    circle at 40% 35%,
    rgba(56, 189, 248, 0.2),
    rgba(15, 23, 42, 0.12) 48%,
    transparent 75%
  );
  box-shadow: 0 0 54px rgba(99, 102, 241, 0.2),
              inset 0 0 36px rgba(59, 130, 246, 0.1);
}
.sphere-fallback .ring-inner {
  position: absolute;
  inset: 14%;
  border-radius: 50%;
  border: 1px dashed rgba(165, 180, 252, 0.28);
  opacity: 0.72;
}
.sphere-fallback .ring-innermost {
  position: absolute;
  inset: 30%;
  border-radius: 50%;
  border: 1px solid rgba(148, 163, 184, 0.22);
  opacity: 0.8;
}
```

### Dependencies

```
@react-three/fiber   (R3F — React reconciler for Three.js)
@react-three/drei    (optional — helpers like OrbitControls, though this globe uses custom drag)
three                (r183+)
framer-motion        (for scroll-linked parallax: scale, rotateZ, translateY)
```

### Key Principles for Reuse

1. **Fibonacci spiral** for uniform sphere point distribution — creates the characteristic "star field" look
2. **Logo masking via canvas sampling** — any SVG/image can be projected onto the hemisphere
3. **Multi-layer glow** on nodes (3 concentric spheres with decreasing opacity) for volumetric feel
4. **Quaternion rotation with inertia** — drag feels physical and continues after release
5. **Mouse velocity tracking** on the surrounding page area — the sphere responds to distant mouse movement
6. **Graceful degradation** — hardware detection with 3 quality tiers down to pure CSS fallback

---

## Signature Effect: Animated Feature Bento Cards (CSS + Framer Motion)

The console site (console.ausdata.ai) uses animated bento-grid feature cards with two particularly striking effects: an **orbiting pulse ring** (Edge Network) and **rotating dashed security rings** (Enterprise Security). These are pure CSS/SVG + Framer Motion — no Three.js needed.

### Card Container Pattern

All cards share a common wrapper with glassmorphism and lift-on-hover:

```jsx
<motion.div
  whileHover={{ y: -5 }}
  className="group relative overflow-hidden rounded-3xl border p-8 transition-colors
             border-white/10 bg-white/5 hover:bg-white/10"
>
  {/* Ghost background: visual repeated at 20% opacity behind content */}
  <div className="absolute inset-0 flex items-center justify-center z-0 opacity-20 pointer-events-none">
    {children}
  </div>

  {/* Foreground content */}
  <div className="relative z-10">
    <h3>{title}</h3>
    <p>{description}</p>
  </div>

  {/* Hover glow: blurred circle that intensifies */}
  <div className="absolute -right-10 -top-10 h-40 w-40 rounded-full blur-[50px]
                  transition-all bg-cyan-500/10 group-hover:bg-cyan-500/20" />
</motion.div>
```

**Key design moves:**
- `rounded-3xl` (24px radius) — these cards soften to circles, unlike the main site's sharp edges
- `bg-white/5` with `hover:bg-white/10` — 5% white glass, doubles on hover
- `whileHover={{ y: -5 }}` — lifts 5px toward viewer
- Ghost layer: the animated visual is duplicated behind at 20% opacity for depth
- Corner glow: blurred 160×160px circle that intensifies on hover

### Grid Layout

```html
<div class="grid grid-cols-1 gap-4 md:grid-cols-3 md:grid-rows-2 h-auto md:h-[600px]">
  <!-- Business Intelligence: col-span-2, row-span-1 -->
  <!-- Type-safe SDK:         col-span-1, row-span-2 (tall) -->
  <!-- Edge Network:          col-span-1, row-span-1 -->
  <!-- Enterprise Security:   col-span-1, row-span-1 -->
</div>
```

### Effect 1: Edge Network — Orbiting Dot with Pulse Rings

A Lucide Globe icon centered in a translucent circle, with expanding ripple rings and an orbiting dot:

```jsx
function EdgeNetworkVisual() {
  return (
    <div className="relative flex h-72 w-72 items-center justify-center">
      {/* Center icon disc */}
      <div className="relative z-10 flex h-[144px] w-[144px] items-center justify-center
                      rounded-full bg-cyan-500/20 border border-cyan-500/50 text-cyan-300">
        <Globe size={72} strokeWidth={1.5} />
      </div>

      {/* Pulse ring 1: expands from 0.5× to 1.5× and fades out */}
      <motion.div
        className="absolute inset-0 rounded-full border border-cyan-500/50"
        initial={{ scale: 0.5, opacity: 0 }}
        animate={{ scale: 1.5, opacity: 0 }}
        transition={{ duration: 2, repeat: Infinity, ease: "easeOut" }}
      />

      {/* Pulse ring 2: same but 0.5s delayed for staggered ripple */}
      <motion.div
        className="absolute inset-0 rounded-full border border-cyan-500/40"
        initial={{ scale: 0.5, opacity: 0 }}
        animate={{ scale: 1.5, opacity: 0 }}
        transition={{ duration: 2, repeat: Infinity, ease: "easeOut", delay: 0.5 }}
      />

      {/* Orbiting dot: full rotation in 10 seconds */}
      <motion.div
        className="absolute h-full w-full rounded-full"
        animate={{ rotate: 360 }}
        transition={{ duration: 10, repeat: Infinity, ease: "linear" }}
      >
        <div className="absolute top-0 left-1/2 h-5 w-5
                        -translate-x-1/2 -translate-y-1/2 rounded-full bg-cyan-300" />
      </motion.div>
    </div>
  );
}
```

**How it works:**
- The 288×288px container holds a 144×144px center disc
- Two concentric ripple rings pulse outward (scale 0.5→1.5) and fade to 0 opacity, looping every 2s
- The second ring is delayed by 0.5s for a staggered sonar effect
- A full-size invisible disc rotates continuously (10s per revolution) carrying a 20×20px cyan dot along the edge
- Color system: cyan-500/20 background, cyan-500/50 borders, cyan-300 for the orbiting dot

### Effect 2: Enterprise Security — Counter-Rotating Dashed SVG Rings

A Lucide Shield icon with a Lock badge, surrounded by two dashed SVG circles rotating in opposite directions:

```jsx
function SecurityVisual() {
  return (
    <div className="relative flex h-72 w-72 items-center justify-center">
      {/* Center icon disc with lock badge */}
      <div className="relative z-10 flex h-[144px] w-[144px] items-center justify-center
                      rounded-full bg-emerald-500/20 border border-emerald-500/50 text-emerald-300">
        <Shield size={72} strokeWidth={1.5} />

        {/* Lock badge: anchored to bottom-right of the disc */}
        <div className="absolute -bottom-1 -right-1 bg-black rounded-full p-0.5
                        border border-emerald-500/70">
          <Lock size={30} className="text-emerald-300" />
        </div>
      </div>

      {/* Rotating dashed rings (SVG) */}
      <svg className="absolute inset-0 h-full w-full" viewBox="0 0 100 100">
        {/* Outer ring: fine dash, clockwise, 8s per revolution */}
        <motion.circle
          cx="50" cy="50" r="40"
          stroke="currentColor" strokeWidth="1"
          className="text-emerald-500/50"
          fill="none"
          strokeDasharray="4 4"
          animate={{ rotate: 360 }}
          transition={{ duration: 8, repeat: Infinity, ease: "linear" }}
          style={{ transformOrigin: "center" }}
        />

        {/* Inner ring: wider dash, counter-clockwise, 12s per revolution */}
        <motion.circle
          cx="50" cy="50" r="30"
          stroke="currentColor" strokeWidth="1"
          className="text-emerald-500/70"
          fill="none"
          strokeDasharray="10 10"
          animate={{ rotate: -360 }}
          transition={{ duration: 12, repeat: Infinity, ease: "linear" }}
          style={{ transformOrigin: "center" }}
        />
      </svg>
    </div>
  );
}
```

**How it works:**
- Two SVG circles with different `strokeDasharray` patterns (4/4 and 10/10) spin in opposite directions
- Outer ring (r=40) rotates clockwise at 8s/revolution — faster, fine dashes
- Inner ring (r=30) rotates counter-clockwise at 12s/revolution — slower, wider dashes
- The opposing motion creates a mechanical "gears turning" or "radar sweep" effect
- Lock badge uses a black background pill anchored bottom-right of the icon disc
- Color system: emerald-500/20 background, emerald-500/50 borders, emerald-300 text

### Adapting These Effects

Both effects follow the same structural pattern:
1. **288×288px container** (h-72 w-72)
2. **144×144px center disc** with icon (50% of container)
3. **Animated ring elements** occupying the full container (absolute inset-0)
4. **Color theming** via Tailwind opacity variants of a single hue

To change the accent color, swap `cyan` → `violet` or `emerald` → `amber`. To change the icon, swap in any Lucide icon at 72px.

### Dependencies

```
framer-motion    (motion.div, motion.circle with animate/transition)
lucide-react     (Globe, Shield, Lock icons)
tailwindcss      (utility classes, opacity variants)
```

---

## What Success Looks Like

A successfully themed Obsidian Precision UI should feel like:
- Opening a premium API documentation site (Stripe-tier)
- Walking through a mathematical exhibition at a science museum
- Reading a beautifully typeset scientific paper or journal
- Interacting with the interface of a high-end Swiss instrument

It should NOT look like:
- A generic dark mode SaaS dashboard
- A cyberpunk/neon aesthetic (too loud)
- A brutalist design (too raw — this is refined)
- Anything with rounded corners or playful animations
- A cold, sterile dark theme (this has warmth through typography and texture)
