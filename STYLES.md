# Style Selection Matrix 🎨
*The Visual Decision-Making Core of the Slidev Engine — v2.0*

This document is used by agents to select the correct visual archetype based on the audience audit. **Mandatory Step 4 in the Pre-Draft Protocol.**

---

## 🏛️ Style Archetypes

### 1. `style-school` — The Neon Cosmos
*   **Target**: Students (K-12), Youth, Gaming Communities, History/Science enthusiasts.
*   **Vibe**: Cinematic, Vibrant, Immersive.
*   **Background**: Deep space navy (`229 84% 5%`) with 4-colour mesh gradient blobs (Cyan + Pink + Gold + Purple) that slowly breathe via CSS animation.
*   **Texture**: Masked dot-grid pattern (32px spacing) fading to edges.
*   **Cards**: Near-invisible frosted glass (`backdrop-filter: blur(18px)`). Floating neon particles (cyan/pink) orbit near card corners.
*   **Typography**: `Outfit` — geometric, accessible. Headings have `text-shadow` neon glow.
*   **Pill**: Neon pink with `neon-pulse` glow animation.
*   **Best For**: History, science, AI, tech — topics that benefit from cinematic depth.

### 2. `style-business` — The Executive
*   **Target**: Corporate Management, Government Officials, Investors.
*   **Vibe**: Credible, Structured, High-Density.
*   **Background (Light)**: Off-white (`210 40% 98%`) with subtle orange + blue radial blobs.
*   **Background (Dark)**: Slate Navy (`222 47% 11%`) with blue + orange corporate mesh.
*   **Texture**: Dot-grid (40px spacing) on a diagonal mask.
*   **Cards**: Semi-opaque glass (`68%` opacity). Gradient top-border (orange → navy). Geometric corner accent pulses in top-right.
*   **Typography**: `Inter` — sharp, corporate. Left-accent bar on headings.
*   **Pill**: Dark navy frosted label.
*   **Best For**: ROI analysis, strategic updates, procurement lifecycle, investor decks.

### 3. `style-workshop` — The Practical
*   **Target**: Field Operators, Workshop Participants, Small Business Owners.
*   **Vibe**: Instructional, Action-Oriented, Grounded.
*   **Background (Light)**: Warm cream paper (`48 100% 96%`) with amber gradient blobs.
*   **Background (Dark)**: Blueprint mode — navy with blue mesh gradients.
*   **Texture**: Graph-paper grid (48px, lines not dots) masked to fade at edges.
*   **Cards**: Sticky-note style — slight rotation, dashed borders, tape-strip accent on top.
*   **Typography**: `Space Grotesk` — pragmatic, technical. Underline headings.
*   **Pill**: Amber label with square corners.
*   **Best For**: How-to guides, field training, mushroom farming, manual workflows.

### 4. `style-cyber` — The Terminal
*   **Target**: Developers, AI Researchers, Technical Visionaries.
*   **Vibe**: High-Tech, Logic-First, Retro-Futuristic.
*   **Background**: Absolute black (`222 10% 2%`) with Matrix-green mesh gradients.
*   **Texture**: Animated vertical scanlines + CRT monitor flicker.
*   **Cards**: Minimalist terminal blocks with bracket accents `[...]` and glow effects.
*   **Typography**: `JetBrains Mono` — high-fidelity mono-space. Headings have `> ` prompts.
*   **Pill**: Outlined label with a flashing terminal cursor `_`.
*   **Best For**: Technical demos, software architecture, AI research, cybersecurity.

### 5. `style-eco` — The Sustainable
*   **Target**: Environmentalists, Wellness Coaches, Organic Brands, Agriculturalists.
*   **Vibe**: Grounded, Calm, Organic.
*   **Background**: Soft Sage (`120 15% 95%`) with cream & forest-green mesh gradients.
*   **Texture**: Recycled-paper grain + masked organic dot textures.
*   **Cards**: Large-radius tactile cards (24px) with floating leaf accents `🍃`.
*   **Typography**: `Lora` — elegant serif for an organic, established tone.
*   **Pill**: Rounded stadium label with a soft green background tint.
*   **Best For**: Sustainability reports, nature docs, wellness guides, organic farming.

### 6. `style-luxury` — The Visionary
*   **Target**: Luxury Brands, High-End Product Launches, Visionary Keynotes.
*   **Vibe**: Premium, Editorial, Sophisticated.
*   **Background**: Midnight Obsidian (`0 0% 5%`) with gold-dust mesh gradients.
*   **Texture**: Vertical silk-line texture + animated light-leak shimmers.
*   **Cards**: Sharp-edged glass blocks with animated gold-trim top borders.
*   **Typography**: `Cormorant Garamond` — light-weight serif for an editorial feel.
*   **Pill**: Minimalist underline label with high letter-spacing.
*   **Best For**: Product reveals, investor keynotes, premium vision statements.

---

## 🧭 Decision Quick-Reference

| Audience Signal | → Archetype |
|---|---|
| "Make it fun / engaging / for kids" | `style-school` |
| "Make it professional / for investors" | `style-business` |
| "Make it practical / training / how-to" | `style-workshop` |
| "It's about history / science / tech" | `style-school` |
| "It's about finance / strategy / ROI" | `style-business` |
| "It's a hands-on workshop / field guide" | `style-workshop` |

---

## 🛠️ Implementation Guide

### Step 1: Style Loading (Automatic)
The global `style.css` auto-imports all three archetypes. **You do NOT need a `<style>` block in your slides.md.**

### Step 2: Slide-Level Activation
Apply the archetype class in the slide's frontmatter:
```markdown
---
layout: cards
class: style-school
pill: MODULE TITLE
title: "The Main Heading"
---
```

### Step 3: Component Usage
Use standard class names within your HTML blocks to inherit the style:
- **`.card`**: Primary content container (via `<SlideCard>` component).
- **`.pill`**: Category label (via `<CategoryPill>` component).
- **`.stat`**: Large stat number styling.
- **`.formula`**: Code/formula display block.
- **`.activity-box`**: Workshop-specific interactive prompt.

### Step 4: Dark Mode
All three archetypes support Slidev's dark mode toggle (press `d`):
- **Business**: Light corporate → Dark slate
- **School**: Neon cosmos (same dark feel in both modes)
- **Workshop**: Warm paper → Blueprint mode
