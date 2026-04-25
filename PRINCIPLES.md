# Strategic Presentation Principles 🧠
*A Framework for Context-Aware Design & Storytelling — v2.0*

This document defines the methodology for transforming a raw topic into a premium, audience-resonant Slidev presentation. Use this to decode the "Why" and "How" before writing a single line of Markdown.

---

## 1. Phase 1: Context Discovery
Before designing, you must define the **Triad of Context**:

### A. The Audience (Who is watching?)
- **The Knowledge Gap**: What do they already know vs. what do they *need* to know?
- **The Motivation**: Are they here to be inspired, to learn a skill, or to make a decision?
- **The Vibe**: 
  - *School Students*: High energy, tactile metaphors, gaming/superpower themes → **`style-school`**
  - *Corporate/Gov*: High density, data-driven, ROI-focused → **`style-business`**
  - *Field Operators*: Practical, instructional, hands-on → **`style-workshop`**

### B. The Subject (What is the core?)
- **Complexity**: Is it a "Simple Concept" (Poultry) or a "Complex System" (AI)?
- **Emotional Weight**: Is it "Future/Optimistic" or "Critical/Problem-Solving"?
- **The "Hero"**: Is the hero a product, a person, or a community?

### C. The Setting (Where is it happening?)
- **Physical Room**: Needs high contrast and large text.
- **Remote/Screen**: Can handle more detail and subtle animations.
- **Self-Paced**: Needs clear navigation and more explanatory text.

---

## 2. Phase 2: Decoding User Input
When a user provides a brief, translate it into a **Strategy Matrix**:

| User Request | Design Implication | Archetype Hint |
|---|---|---|
| "Make it simple" | Increase whitespace, reduce bullet points. | `style-school` with fewer cards |
| "Make it premium" | Cinematic imagery, glassmorphism, dark mode. | `style-school` or `style-business` (dark) |
| "Make it engaging" | Add `v-click` reveals and `ACTIVITY` slides. | Any archetype + `v-click` on every card |
| "Make it local" | Use Indocentric terms and familiar imagery. | Any archetype + Hinglish + rural examples |
| "Make it data-heavy" | Use `LiveChart`, stat cards, split layouts. | `style-business` with stat-focused slides |
| "Make it practical" | Step-by-step cards, activity boxes. | `style-workshop` |

---

## 3. Phase 3: The Design Mapping
Map the discovery insights to the engine's configuration:

| Insight | Archetype | Layout Strategy |
|---|---|---|
| **Trust/Authority** | `style-business` | `split` + `LiveChart`, stat cards |
| **Energy/Innovation** | `style-school` | `cards` with staggered v-click, `split` with images |
| **Calm/Education** | `style-school` (light) | `default`, balanced layouts |
| **Hands-On Training** | `style-workshop` | `cards` with activity boxes, dashed borders |

### Archetype → Slide Template Mapping
1. Select archetype from `STYLES.md`
2. Copy the matching template from `templates/<archetype>.md`
3. Create your master file in `presentations/<topic>.md`
4. Stage it: `Copy-Item presentations/<topic>.md slides.md`

---

## 4. Phase 4: Narrative Engineering (The "Power Flow")
Apply the structure based on the audience's attention span:

1. **The Hook (0-5 mins)**: Unlock curiosity. Use a cinematic cover slide (`split` layout with a generated cover image).
2. **The Modules (15-40 mins)**: Chunk the information into 3 labelled blocks. Use the `CategoryPill` component to signpost progress. Each module uses `cards` or `split` layouts.
3. **The Bridge (Every 10 mins)**: Break the "Fourth Wall." Use a `VOTE TIME` or `LIVE DEMO` to bring the audience back into the room.
4. **The Finale (Final 5 mins)**: Transition from "Thinking" to "Doing." Use `default` layout with centered spring-animated text and stat dividers.

---

## 5. The Visual Quality Checklist
- [ ] **No Hardcoded Colors**: Every `color`, `background`, `border`, and `box-shadow` uses `hsl(var(--token) / opacity)`.
- [ ] **Archetype Applied**: Every slide has `class: style-<archetype>` in frontmatter.
- [ ] **No Text-Only Slides**: Every slide has at least one icon, image, card, or decorative element.
- [ ] **Density Safe**: No more than 3 cards per row, 6 cards max per slide. Grid gap ≤ `0.8rem` for dense grids.
- [ ] **v-click Active**: Content is revealed sequentially, not dumped at once.
- [ ] **Images Optimized**: All images are `.webp` format in `public/`.
- [ ] **Dark Mode Tested**: Press `d` to verify both modes look premium.

---

*"Design is not just what it looks like and feels like. Design is how it works."* — Steve Jobs
