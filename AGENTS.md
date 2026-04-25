# Agent Instructions: Slidev Presentation Engine 🤖
*Last Updated: 2026-04-25*

This repository is a high-performance presentation engine built on **Slidev**. It is designed for creating premium, Indocentric, and interactive slide decks for educational and business seminars.

---

## 🏗️ Repository Architecture

| File | Role | Priority |
|------|------|----------|
| **`slides.md`** | Primary source of truth. All slide content, styles, and metadata. | Always edit |
| **`SKILL.md`** | **START HERE.** Operational playbook — design intelligence, QA protocol, icon safety, workflow steps. | Read before any task |
| **`PRINCIPLES.md`** | Strategic methodology — audience analysis, context discovery, narrative engineering. | Read before any new deck |
| **`STYLE_GUIDE.md`** | Visual standards — typography, spacing, default palette, layout rules. | Read before styling |
| **`public/`** | Static assets. Always reference as `/filename.png` (absolute path from root). | |
| **`extract_pptx.py`** | Extracts text from legacy `.pptx` files. Also read slide XML in `temp_pptx/` for color/shape data. | For PPTX migrations |

---

## 🚦 Pre-Draft Protocol (MANDATORY — No Exceptions)

Before writing **any** slide content, execute this sequence in order:

### Step 1: Read SKILL.md
Open and read `SKILL.md`. It contains the active design intelligence, QA checklist, icon safety table, and workflow steps. Do not skip this.

### Step 2: Contextual Audit (from PRINCIPLES.md)
Answer these three questions explicitly:
1. **Topic** — Is it Technical, Business, Social, Creative? What is the emotional weight?
2. **Audience** — Age group, knowledge gap, motivation (Inspire / Learn / Decide)?
3. **Setting** — Large hall, remote screen, or self-paced?

### Step 3: State Assumptions
Present your audit to the user. Get confirmation before writing slides.

### Step 4: Design Mapping
From `SKILL.md`'s Audience → Design table, select:
- Color palette (topic-specific, NOT generic blue)
- Layout strategy (rounded cards vs. data-dense vs. calm)
- Energy level (max energy → moderate → premium quiet)

### Step 5: Build + QA
Write the slides. Then run the **QA Protocol** from `SKILL.md` before declaring done.

---

## 🎨 Core Design Principles

1. **Audience-First Contextuality**: Design is NOT a fixed mandate. Subject and audience dictate everything.
2. **Geometric Life**: Every slide needs non-text visual elements — background circles, icons, images, or decorative shapes. Text-only slides are unacceptable.
3. **Iconography as Language**: Use the **Carbon** icon set. Icons must provide instant visual shorthand, never decoration. **Always verify icon names** using the Icon Safety Protocol in `SKILL.md`.
4. **Subject Harmony**: Colors must feel designed for THIS topic specifically. If swapping the palette into a different topic still "works," the choices weren't specific enough.
5. **Dynamic Color Shifting**: Each module can have its own background gradient/color to signal a phase change and reset audience attention.

---

## 🚀 Development Workflow

- **Preview**: `npm run dev` → `http://localhost:3030`
- **Transitions**: `fade` or `slide-left` for premium feel
- **Interactivity**: `v-click` for sequential storytelling — never dump all content at once
- **Layouts**: Rotate through `fact`, `center`, `two-cols`, `image-right`, `end` — never repeat the same layout consecutively
- **Geometric Depth**: Use edge-bleed CSS circles on `.slidev-layout::before/::after` to break the rectangular frame

---

## 🧩 Content Strategy

- **Indocentricity**: Ground examples in Indian contexts (Agri-tech, Bollywood, Health, Rural infrastructure, Hinglish terms)
- **The Power Flow**: Hook → Modules (2–3) → Interactive Bridge → Finale. Module names adapt to the topic.
- **Minimalism**: If a slide has more than 3 bullet points, split it into two slides.
- **The Bridge**: Every module must end with an `ACTIVITY`, `VOTE TIME`, or `LIVE DEMO` moment.

---

## 🛠️ Environment (Windows/PowerShell)

- Use semicolons (`;`) not `&&` to chain PowerShell commands
- Use `Get-ChildItem -Recurse` instead of `dir /s`
- UTF-8 for Python scripts: `sys.stdout.reconfigure(encoding='utf-8')`

---

*"Maintain the DNA. Respect the Guide. Activate the Superpower."* ⚡
