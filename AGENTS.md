# Agent Instructions: Slidev Presentation Engine 🤖
*Last Updated: 2026-04-26*

This repository is a **cinematic presentation engine** built on Slidev. It produces premium, Indocentric, and interactive slide decks for educational and business seminars — powered by a tokenized HSL color architecture, glassmorphism, and animated design elements.

---

## 🏗️ Repository Architecture

| File / Folder | Role | Priority |
|---|---|---|
| **`slides.md`** | Staging area. `npm run dev` reads this file. | Always edit |
| **`presentations/`** | Master archive. Each deck lives here as `<topic>.md`. | Source of truth for decks |
| **`SKILL.md`** | **START HERE.** Operational playbook — design intelligence, QA protocol, icon safety, workflow steps. | Read before any task |
| **`templates/`** | Starter boilerplate files for each archetype (`school`, `business`, `workshop`). | Copy to start a new deck |
| **`PRINCIPLES.md`** | Strategic methodology — audience analysis, context discovery, narrative engineering. | Read before any new deck |
| **`STYLES.md`** | Visual catalog & decision matrix for selecting the correct archetype. | Read during Step 4 |
| **`STYLE_GUIDE.md`** | Foundational visual standards — typography, spacing, palette philosophy. | Reference during styling |
| **`styles/`** | **The CSS Engine.** HSL tokens, mesh gradients, glassmorphism, animations per archetype. | Never hardcode colours |
| **`style.css`** | Global entry point. Imports all archetype CSS and clears Slidev theme defaults. | Do not delete |
| **`components/`** | Vue components: `SlideCard`, `CategoryPill`, `LiveChart`. | Use in all decks |
| **`layouts/`** | Custom Vue layouts: `default`, `cards`, `split`. | Set via frontmatter |
| **`uno.config.ts`** | UnoCSS configuration with HSL token shortcuts. | Reference for utility classes |
| **`public/`** | Static assets. Always reference as `/filename.webp`. | |
| **`scripts/`** | Asset pipeline (`optimize-assets.js` for PNG→WebP conversion). | Run `npm run optimize` |
| **`extract_pptx.py`** | Extracts text from legacy `.pptx` files. | For PPTX migrations |

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

### Step 4: Design Mapping & Template Loading
1. Consult **`STYLES.md`** to select the archetype that matches your Step 2 audit.
2. **Load Template**: Read the corresponding file from `templates/` (e.g., `templates/school.md`) to use as your structural foundation.
3. **Initialize Master**: Create `presentations/<topic>.md` with the template content.
4. **Stage Dev**: Copy that content into `slides.md`.

*Note: Always ensure the `class: style-<archetype>` frontmatter is present on every slide.*

### Step 5: Build + QA
Write the slides using the component-driven system. Then run the **QA Protocol** from `SKILL.md` before declaring done.

---

## 🎨 Core Design & Color System

1. **HSL Token Architecture**: All colors are stored as raw HSL channel values in CSS variables. Use `hsl(var(--token) / opacity)` — never hardcode hex values.
2. **Mesh Gradients**: Each archetype has atmospheric `radial-gradient()` blobs layered behind content. These are animated with CSS keyframes.
3. **Glassmorphism**: Cards use `backdrop-filter: blur()` with translucent backgrounds and inset highlights.
4. **Decorative Elements**: Dot grids, geometric corner accents, floating particles, and tape-strip accents are rendered via `::before`/`::after` pseudo-elements.
5. **Multi-layered Shadows**: Cards use 3-tier shadow stacks for realistic depth grounding.
6. **Iconography**: Carbon icon set (`<carbon:icon-name />`). Always verify names exist — see SKILL.md Icon Safety Protocol.

---

## 🚀 Development Workflow

- **Preview**: `npm run dev` → `http://localhost:3030` (run from `slidev/` directory)
- **Optimize Assets**: `npm run optimize` (converts PNG→WebP, ~75% size reduction)
- **Switch Decks**: `Copy-Item presentations/<topic>.md slides.md`
- **Transitions**: `fade` or `slide-left` for premium feel
- **Interactivity**: `v-click` for sequential storytelling — never dump all content at once
- **Dark Mode**: Press `d` in the browser to toggle

---

## 🧩 Content Strategy

- **Indocentricity**: Ground examples in Indian contexts (Agri-tech, Bollywood, Health, Rural infrastructure, Hinglish terms)
- **The Power Flow**: Hook → Modules (2–3) → Interactive Bridge → Finale. Module names adapt to the topic.
- **Minimalism**: If a slide has more than 3 bullet points, split it into two slides.
- **The Bridge**: Every module must end with an `ACTIVITY`, `VOTE TIME`, or `LIVE DEMO` moment.

---

## 🛠️ Environment (Windows/PowerShell)

- Run `npm run dev` from the `slidev/` subdirectory, **not** from `my-slides/`
- Use semicolons (`;`) not `&&` to chain PowerShell commands
- Use `Get-ChildItem -Recurse` instead of `dir /s`
- UTF-8 for Python scripts: `sys.stdout.reconfigure(encoding='utf-8')`

---

*"Maintain the DNA. Respect the Guide. Activate the Superpower."* ⚡
