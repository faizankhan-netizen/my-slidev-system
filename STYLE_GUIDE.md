# Slidev Presentation Style Guide 🎨
*Version 2.0 — Cinematic Engine with HSL Token Architecture*

This guide defines the aesthetic and structural DNA for high-impact, educational presentations created using Slidev. Follow these rules to maintain a **Premium, Cinematic, and Indocentric** brand identity.

---

## 1. Core Principles: Audience & Context
Design is a conversation between the speaker and the audience. Every visual choice must be justified by the context:
- **Audience Empathy**: Is this for a 12-year-old student or a CEO? For students, use vibrant imagery and relatable terms (*Murga-Murgi*). For executives, use data-dense layouts and industry terminology.
- **Subject-Matter Harmony**: The visuals must match the mood. Choose the archetype (`school`, `business`, `workshop`) that fits the audience — never force a single palette.
- **Functional Minimalism**: Whitespace is not empty space; it is "focus space." Every element on a slide must earn its right to be there.
- **Narrative Pacing**: Use `v-click` to control the "dose" of information. High-energy storytelling requires revealing one surprise at a time.

---

## 2. The HSL Color Architecture

> **The Golden Rule: NEVER hardcode hex colors. Use `hsl(var(--token) / opacity)` everywhere.**

All colors are stored as raw HSL channel values in CSS variables. This unlocks dynamic opacity composition — a single token can be used at 100%, 50%, 5%, or any opacity without defining new variables.

### Available Tokens
| Token | Purpose |
|---|---|
| `--bg-primary` | Slide background |
| `--bg-card` | Card/container background |
| `--text-main` | Primary text color |
| `--border-main` | Borders and dividers |
| `--accent-primary` | Primary action color |
| `--accent-secondary` | Secondary color / pill backgrounds |
| `--accent-tertiary` | Stat numbers, highlights |

### Usage
```css
/* ✅ CORRECT — Dynamic opacity */
color: hsl(var(--text-main));
background: hsl(var(--bg-card) / 0.08);
box-shadow: 0 4px 20px hsl(var(--text-main) / 0.12);

/* ❌ WRONG — Breaks the system */
color: #1E293B;
background: var(--bg-card);
```

---

## 3. Typography Engine
Each archetype imports a premium Google Font. Never override unless instructed:

| Archetype | Font | Character |
|---|---|---|
| **Business** | `Inter` | Sharp, credible, corporate |
| **School** | `Outfit` | Geometric, vibrant, accessible |
| **Workshop** | `Space Grotesk` | Pragmatic, technical, instructional |
| **Cyber** | `JetBrains Mono` | High-tech, logical, terminal |
| **Eco** | `Lora` | Organic, calm, established |
| **Luxury** | `Cormorant Garamond`| Sophisticated, editorial, premium |
| **Editorial** | `Playfair Display` | High-fashion, minimalist, Swiss |
| **Industrial** | `Roboto Mono` | Structural, precise, architectural |
| **Space** | `Outfit` / `Space Mono`| Epic, futuristic, visionary |

### Sizing Rules
| Element | Size | Weight |
|---|---|---|
| Title (hero) | `3.5rem` | `900` (Black) |
| Title (dense slides) | `2.4–2.8rem` | `900` |
| Subtitle | `1.6rem` | `700` |
| Body | `1.05rem` | `400` |
| Pill label | `10px` | `800–900` |

---

## 4. Structural Framework: The "Power" Flow
Break presentations into a 4-part narrative structure:
1. **The Hook**: High-impact visual — a cinematic cover slide with generated imagery.
2. **The Modules**: Segment content into 3-4 logical blocks using the `cards` or `split` layout.
3. **The Interactive Bridge**: Every module must have an activity or a "Live Demo."
4. **The Finale**: A centered conclusion slide with animated stats and a call to action.

---

## 5. The Visual Layer System

### Layer 1: Background Atmosphere
Each archetype has atmospheric gradients or animated stars:
- **School/Business**: Breathing mesh gradients.
- **Eco**: Soft sage/cream organic blobs.
- **Space**: Animated starfields and pulsing nebulas.

### Layer 2: Surface Texture
- **School/Business**: Masked dot-grids.
- **Workshop**: Graph-paper grid.
- **Cyber**: CRT scanlines.
- **Editorial**: "Stardust" paper grain.
- **Industrial**: Blueprint-style 40px grids.

### Layer 3: Structural Flavour
Pseudo-elements (`::before`/`::after`) create:
- **Cyber**: Bracket accents `[...]` and terminal cursor `_`
- **Eco**: Floating leaf accents `🍃`
- **Luxury**: Animated gold-trim shimmers
- **Editorial**: Asymmetric color blocks (Swiss Red)
- **Industrial**: Coordinate markers and architectural rulers
- **Space**: Orbital rings and light-flare shimmers

### Layer 4: Content
All content sits at `z-index: 1` above decorative layers. Cards use multi-layered `box-shadow` or glass blurs.

---

## 6. Glassmorphism Standards

### Card Properties
| Property | School | Business | Workshop | Cyber |
|---|---|---|---|---|
| `backdrop-filter` | `blur(18px) saturate(160%)` | `blur(16px) saturate(150%)` | `blur(14px) saturate(140%)` | `blur(12px) saturate(180%)` |
| Background | `hsl(--bg-card / 0.08)` | `hsl(--bg-card / 0.68)` | `hsl(--bg-card / 0.72)` | `hsl(--bg-card / 0.85)` |
| Border | Transparent + outline glow | Gradient top border | Dashed border | Thin green + glow |
| Shadow | 3-tier + cyan inner glow | 3-tier corporate | 3-tier angled tactile | Glow-pulse + inset |
| Hover | Scale 1.015 + glow | Lift -2px | Rotate to 0° + lift | Border-glow + lift |

---

## 7. Slidev-Specific Implementation
### Available Layouts
- `default`: Auto safe-zone padding, flexible content flow.
- `cards`: Frontmatter: `pill`, `title`. Auto-creates a balanced flex grid.
- `split`: Frontmatter: `pill`, `title`, `subtitle`. Left text + right media (`::right::`).

### Available Components
- `<CategoryPill>`: Inline-block styled label. Colors inherited from archetype.
- `<SlideCard>`: Props: `title`, `icon`, `stat`, `titleColor`, `borderTop`, `delay`.
- `<LiveChart>`: Props: `option` (ECharts JSON), `width`, `height`.

---

## 8. Image Standards
- **Source**: AI-generated cinematic imagery or professional photography.
- **Format**: Always `.webp` — run `npm run optimize` to convert PNGs.
- **Placement**: Full-bleed in `split` layout right slot, or as card backgrounds.
- **Shadows**: `box-shadow: 0 25px 60px hsl(0 0% 0% / 0.5)` for floating effect.

---

## 9. Writing & Tone of Voice
- **Direct Address**: Use "You," "We," and "Let's."
- **Indocentricity**: Ground examples in Indian reality (Agriculture, Bollywood, local languages).
- **Power Words**: Use short, punchy labels: `ACTIVITY`, `LIVE DEMO`, `VOTE TIME`, `MISSION`.

---

## 📐 10. Archetype Engineering Rules (Crucial)

### 10.1 Aesthetic Sovereignty (The "Structure" Rule)
*   **Principle**: Never sacrifice a structural archetype (like the Editorial asymmetry) for a technical fix.
*   **Action**: If text is illegible, fix the *color* or *contrast*, not the *positioning*. The asymmetry is the soul of the design.

### 10.2 High-Contrast Dominance (The "Overlap" Rule)
When text overlaps two backgrounds (e.g., Red Sidebar & White Main):
*   **The Law**: Use a single "Dominance Color" that works on both. For Editorial, **Stark Black** font is the default for halfway overlaps.
*   **The Constraint**: Do not use `mix-blend-mode`, gradients, or outlines. These often look "unclean" for modern standards.
*   **Contextual Shift**: If a slide is 100% one color (e.g., `.variant-red`), switch to **White** text for main headings and **Black** for secondary indicators (pills) to ensure 100% contrast.

### 10.3 Vertical Viewport Safety (The "Bleeding" Rule)
Slidev viewports are finite. To prevent "bleeding" off the bottom:
*   **Stat-Giant Cap**: Max size for giant numbers is **5rem** when headings/captions are present. Use **6rem** ONLY on empty focus slides.
*   **Heading Density**: Headlines with more than 3 words must use `line-height: 1` or smaller to reclaim vertical space.
*   **Layout Logic**: Prefer `justify-content: center` with a controlled `gap` over `space-between` to keep content within the safe zone.

### 10.4 Technical Rendering Pitfalls
*   **Markdown in HTML**: Standard markdown (`**bold**`) fails inside raw `<div>` tags in Slidev. Use `<b>` or `<strong>` for highlights within architectural components (like `.caption`).
*   **Z-Index Hygiene**: Background blocks (like `::before`) must stay at `z-index: 0`. All content must be `position: relative; z-index: 10;` to prevent physical obstruction.

---

## 🏗️ 11. Cinematic Engine V3: Advanced Layouts & Intelligence

### 11.1 BoundGuard Spatial Intelligence
The engine is now "Viewport Aware." It automatically adjusts layouts to prevent text bleeding:
- **Auto-Scaling**: Titles and descriptions shrink dynamically based on character count.
- **Title Clearance**: Infographics (Cycles/Charts) maintain a strict **160px buffer** from the top.
- **Auto-Pagination**: Large lists (Process/Agenda) are automatically split into multiple slides with "(1/n)" pagination suffixes.

### 11.2 Interactive Infrastructure
- **Guerrilla GUI**: Slides with video backgrounds feature a hidden hover-reveal input in the bottom-right for live media swapping.
- **YouTube-Embed Logic**: Pasting a YouTube link into the GUI or the Python API automatically converts it into a cinematic, muted background.
- **Module Hub**: The `agenda` template is now a clickable "Module Hub." Use `@click="$nav.go(N)"` to create jump-links between presentation acts.

### 11.3 New High-Fidelity Archetypes
| Type | Usage | Intelligence |
| :--- | :--- | :--- |
| `cycle` | Circular flows | Auto-calculates orbital math for 1-6 nodes. |
| `chart` | Data Trends | Uses theme-aware HSL palettes to match the deck's archetype. |
| `media_focus` | Product Demos | Auto-detects YouTube/Video and enables playback controls. |
| `table` | Data Sheets | Glassmorphic striped rows with automated HSL contrast. |

---

*"The ideas are yours. AI is just the paintbrush. The structure is sacred."* ⚡
