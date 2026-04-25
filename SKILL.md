---
name: slidev-presentation
description: "Use this skill any time a Slidev presentation is involved — creating, editing, debugging, or styling slides.md files. Trigger when the user mentions 'slides', 'presentation', 'deck', 'Slidev', or any visual content that needs to be shown. Always run the Pre-Draft Protocol from AGENTS.md before generating content."
---

## Slidev Architecture & Design SOP

*This is the mandatory technical and visual architecture for ALL slides in this repository (Replications AND New Creations) to ensure pixel-perfect, responsive, and bug-free rendering.*

### 📂 Multi-Deck Management Workflow
To prevent overwriting work, we use the `presentations/` folder as a master archive.

1. **New Project Start**: Always create a master file first: `presentations/<topic_name>.md`.
2. **Active Development**: `slides.md` is our "Staging Area". Copy your master file content into `slides.md` for `npm run dev` to pick it up.
3. **Switching Decks**: To work on a different topic, use PowerShell:
   ```powershell
   # Archive current work
   Copy-Item slides.md presentations/current_topic.md
   # Load new work
   Copy-Item presentations/new_topic.md slides.md
   ```

### The Universal Hybrid Layout
We use a **Hybrid Layout** because it combines the precision of absolute graphics with the reliability of flexible text.

1. **Layout Sovereignty (The White Border Fix)**
   To definitively kill white borders, you MUST apply the background and padding directly to the **layout container** using the frontmatter `class` property.
   ```markdown
   ---
   layout: default
   class: bg-green
   ---
   ```
   In the `<style>` block:
   ```css
   /* Mandatory: Set background on layout class AND globally on body/app */
   body, #app, .slidev-layout.bg-green {
     background: #064E3B !important;
     padding: 3.5rem !important; /* The 'Safety Buffer' gap for headings */
   }
   ```

2. **The Global Background Reset**
   Always style the `body` and `#app` in your global `<style>` block to match the slide background. This ensures that the browser area outside the slide canvas (the "viewport gap") is never white, creating a seamless full-bleed experience.

3. **Custom Vue Layouts & Component-Driven Structure**
   Instead of writing raw HTML wrappers, use frontmatter to define the slide layout, and our custom Vue components for the content.
   
   *Available Layouts (set via `layout: name` in frontmatter):*
   - `default`: Automatically wraps content in the safe-zone wrapper.
   - `cards`: Requires `pill` and `title` in frontmatter. Automatically creates a balanced flex-grid for your cards.
   - `split`: Requires `pill`, `title`, and `subtitle`. Perfect for left-text and right-media (`::right::`) splits.

   *Theming & Dark Mode (CSS Variables):*
   - The entire engine is powered by CSS Variables (`--bg-primary`, `--text-main`, etc.).
   - Slidev's built-in Dark Mode toggle automatically switches these variables.
   - **Business** flips to a sleek Slate/Navy dark mode.
   - **School** remains a dark Neon cosmos.
   - **Workshop** flips from a warm "Paper" look to a stunning "Blueprint" aesthetic.

   *Example (The Cards Layout):*
   ```markdown
   ---
   layout: cards
   class: style-school
   pill: THE MISSION
   title: Main Title
   ---
   <SlideCard v-click title="Point 1" icon="🚀" borderTop="#22D3EE">
      Explanation text here.
   </SlideCard>
   ```
   *Available Components:*
   - `<CategoryPill>`: Wraps text in the styled pill format.
   - `<SlideCard>`: Accepts `title`, `icon`, `stat`, `titleColor`, and `borderTop` props.
   - `<LiveChart>`: Accepts `option` (JSON object of ECharts config), `width`, and `height`. Use for animated, dynamic data visualizations (especially in Business/Technical styles).

4. **Premium Typography Engine**
   We utilize imported Google Fonts to give each archetype a distinct, high-end feel. Do not override these unless instructed:
   - **Business:** `Inter` (Sharp, credible, corporate)
   - **School:** `Outfit` (Geometric, vibrant, accessible)
   - **Workshop:** `Space Grotesk` (Pragmatic, technical, instructional)

5. **HSL Color Engine (The Alpha Superpower)**
   All CSS variables store raw HSL *channel values* — NOT full hex codes or hsl() wrappers.
   This means you can dynamically apply any opacity to any themed color anywhere:
   ```css
   /* ✅ CORRECT — dynamic opacity composable */
   background: hsl(var(--bg-card) / 0.05);
   box-shadow: 0 4px 20px hsl(var(--text-main) / 0.12);

   /* ❌ WRONG — breaks the opacity system */
   background: var(--bg-card);
   ```
   UnoCSS shortcuts for common patterns (use these in slide content):
   - `slide-card-shadow` — Themed drop shadow auto-adapts to dark/light mode
   - `neon-glow`         — Coloured glow matching `--accent-secondary`
   - `subtle-border`     — 30% opacity border matching `--border-main`

6. **Mesh Gradients & Glassmorphism (Phase 3)**
   Each archetype's background is now a layered CSS mesh gradient using `radial-gradient()`. Cards and pills use **glassmorphism**: `backdrop-filter: blur()` with semi-transparent `hsl()` backgrounds and inset highlights.
   
   *Archetype Visual Signatures:*
   - **Business:** Faint orange + blue radial blobs over clean slate. Glass cards with subtle `inset 0 1px 0` highlight and hover lift.
   - **School:** Four-colour neon cosmos (Cyan + Pink + Gold + Purple). Cards are near-invisible frosted glass. Headings have a `text-shadow` neon glow.
   - **Workshop (Light):** Warm amber gradient blobs over cream paper. Sticky-note cards have a slight rotation and authentic dashed borders.
   - **Workshop (Dark):** Blueprint mode — cool blue mesh gradient. Same card structure recoloured to engineering blueprint aesthetic.
   
   **Critical Rule:** Do NOT add `background` inline styles to slides using these archetypes. The mesh gradient lives in the CSS and must not be overridden.

7. **Decorative Design Elements (Phase 2)**
   Each archetype now has animated background textures and micro-decorations powered by CSS `::before`/`::after` pseudo-elements. These are pure CSS — no JavaScript or extra DOM needed.
   
   *Shared Patterns:*
   - **Animated Blobs:** The mesh gradient blobs slowly "breathe" using a 15s CSS keyframe (`cosmos-breathe`). This prevents the background from feeling static.
   - **Background Textures:** Each archetype has a masked texture (dot grid or graph paper) that fades towards the edges. This adds depth without competing with content.
   - **Card Micro-accents:** Floating particles, diamond shapes, or tape strips appear near cards using `::before`/`::after` on `.card`.
   
   *Archetype-Specific Flourishes:*
   - **School:** Cyan/pink neon particles float near cards. The pill has a `neon-pulse` animation.
   - **Business:** A geometric corner accent (curved orange lines) pulses in the top-right. Small diamond shapes float on cards.
   - **Workshop:** A drafting ruler with tick marks lines the left edge. Cards have "tape strip" accents that gently sway.
   
   **Critical Rule:** All decorative pseudo-elements use `z-index: 0` and `pointer-events: none`. All content uses `z-index: 1`. Never change these values.

8. **Density-Aware Scaling (The Bleed Prevention Rule)**
   - **Titles:** Cap at `3rem` for dense slides (3+ cards/items).
   - **Padding:** Rely on the `default` layout padding. Do not add random padding hacks.
   - **Safe Zone:** All text must stay within the `3.5rem` padding buffer. If content approaches the bottom edge, downscale fonts or simplify descriptions immediately.
   - **Dense Grids (3×2):** Use `gap: 0.8rem` and shorten card descriptions to single lines.

9. **Graphic Positioning**
   - **Absolute Accents:** Use `top`, `left`, etc. for decorative dots. Note that they position relative to the *padded* layout, so `top:0` starts at the padding edge.
   - **Bleed Geometry:** Use `::before/::after` pseudo-elements for large edge-bleed shapes to keep the DOM clean.

### 🎨 Style Presets & Theming
We have pre-designed CSS contexts in the `styles/` folder. Apply them to match your audience:

1. **Importing Styles**: Add the import at the top of your global `<style>` block:
   ```css
   @import './styles/school.css';
   @import './styles/business.css';
   @import './styles/workshop.css';
   ```

2. **Applying to Slides**: Use the corresponding class in your frontmatter:
   - **`style-school`**: Vibrant, rounded, neon accents (For students).
   - **`style-business`**: Structured, Slate/Navy, trust-focused (For corporate).
   - **`style-workshop`**: Warm paper, dashed lines, action-oriented (For training).

   Example:
   ```markdown
   ---
   layout: default
   class: style-school
   ---
   ```

### 🚨 Critical Parser Rules (Do Not Break)
1. **Single Root Element:** Every slide must have exactly ONE root `<div>`.
2. **Zero Blank Lines:** Never leave a blank line between nested `<div>` tags. This breaks the markdown-it parser and leaks raw HTML text to the screen.
3. **Slide Numbering Safety:** Never place a `---` separator between a `<style>` block and the first slide's content. This creates a "Blank Slide 1". Keep the style block at the very top, within the global frontmatter or immediately attached to Slide 1.
4. **The Flex Stretch Trap:** In a `flex-direction: column` layout, children (like pills) will stretch to 100% width by default. Always use `align-items: flex-start` on the `.content-wrapper` to keep UI elements proportionate.
5. **Markdown-in-HTML Limitation:** Markdown syntax (like `**bold**`) does NOT render inside HTML tags. Always use HTML tags (`<b>`, `<strong>`) or `<span style="...">` for text highlighting within layout blocks.
6. **Icon Sibling Safety:** Never place a `<carbon:icon />` as a direct sibling of a `<div>` inside a flex container. Wrap icons in a `<span>` to prevent template parsing crashes.
7. **Safe Zone Discipline:** To respect the `3.5rem` safety buffer, cap main titles at `2.8rem` - `3.2rem` and use `width: 100%` on containers to ensure they wrap within the padding instead of overflowing.
8. **No Trailing Separator:** Never leave a `---` separator at the very end of the file. Slidev interprets this as the start of a new slide, resulting in an unintended blank slide at the end of your presentation.
9. **No Tailwind Arbitrary Values:** Avoid `w-[350px]` in Vue templates; use `style="width: 350px"` to prevent parser confusion.



# Slidev Presentation Skill

## Quick Reference

| Task | Action |
|------|--------|
| Create a new presentation | Run Pre-Draft Protocol → Write `slides.md` |
| Read a `.pptx` for style reference | Run `python extract_pptx.py <file.pptx>` |
| Preview slides | `npm run dev` → open `http://localhost:3030` |
| Verify an icon exists | `python -c "import json; data=json.load(open('node_modules/@iconify-json/carbon/icons.json')); print([k for k in data['icons'].keys() if 'keyword' in k])"` |
| Launch Remote Control | `npm run remote` → Press `Ctrl+R` in deck |
| Debug a broken slide | Check `slides.md__slidev_N.md` line numbers in Vite error → trace back to `slides.md` |

---

## Pre-Draft Protocol (MANDATORY)

Before writing a single line of `slides.md`, perform a **Contextual Audit** based on `PRINCIPLES.md`:

1. **Analyze the Topic** — Is it Technical, Business, Social, or Creative?
2. **Analyze the Audience** — What is their age, knowledge gap, and motivation? (Student vs. Executive vs. Developer)
3. **Analyze the Setting** — Large hall, remote screen, or self-paced?

**Output Requirement**: State your assumptions to the user and get confirmation before proceeding.

---

## Design Intelligence

### Don't Create Boring Slides

Every slide must have a **visual element** — background shape, icon, image, or decorative circle. Text-only slides kill engagement.

**Avoid these anti-patterns:**
- ❌ Plain white background on every slide
- ❌ Same layout repeated across all slides
- ❌ Centered body text (only center titles)
- ❌ Underline accent lines below titles (hallmark of lazy AI-generated slides)
- ❌ Low-contrast text or icons on similar-value backgrounds
- ❌ Placeholder text or unused frontmatter fields

---

## Audience → Design Mapping

| Audience | Palette Strategy | Layout Strategy | Energy |
|----------|-----------------|-----------------|--------|
| **School Students (6–10)** | Vibrant: Indigo + Orange + Teal + Yellow | Rounded cards, large emoji, massive type | Max energy, floating circles, animations |
| **School Students (11–12)** | Bold: Navy + Electric Blue + Coral | Two-col, fact, image-right | High energy, icons, `v-click` reveals |
| **Corporate/Government** | Deep: Navy + Gold + Off-white | `quote`, `fact`, data tables | Premium, no gimmicks |
| **Developers/Technical** | Dark: Charcoal + Accent + Code blocks | `two-cols` with code, terminal aesthetic | Clean, precise |
| **Awareness/Social** | Calm: Sage + Cream + Warm Accent | `center`, flowing text, imagery | Emotional, spacious |
| **Luxury** | Dark: Midnight Obsidian + Gold | `split` with cinematic images | Sophisticated, visionary |

---

## 📡 Mission Control: Remote Navigation

The engine features a built-in "Mission Control" portal for mobile remote control.

### How to use:
1. **Launch**: Run `npm run remote` in your terminal. This exposes the presentation to your local network.
2. **Access Portal**: Press `Ctrl+R` on your desktop browser while the presentation is open.
3. **Connect**: Scan the generated QR code with your mobile device.
4. **Command**: Once open on mobile, a **Tactile Remote Interface** (Luxury Style) will appear with large Next/Back buttons for seamless navigation.

**Safety Note**: Both devices must be connected to the same local WiFi network for the portal to bridge.

---

## Color System (Archetype-Driven)

> **Do NOT pick colors manually.** Select an archetype, and the CSS engine handles all colors via HSL tokens.

| Archetype | Accent Primary | Accent Secondary | Accent Tertiary | Best For |
|---|---|---|---|---|
| **`style-school`** | Cyan (`188 86% 53%`) | Pink (`330 81% 60%`) | Gold (`48 96% 53%`) | Student seminars, history, science, tech |
| **`style-business`** | Orange (`25 95% 53%`) | Navy (`217 33% 17%`) | Blue (`226 71% 40%`) | Corporate, ROI, procurement, strategy |
| **`style-workshop`** | Amber (`32 94% 44%`) | Yellow (`46 97% 65%`) | Bronze (`38 92% 50%`) | Training, field guides, how-to |

**If you need a topic-specific colour not covered above**, add a new archetype CSS file in `styles/` following the established HSL variable pattern.

---

## "Geometric Life" — The Visual Layer System

The engine's visual depth comes from **4 automated CSS layers**, not from manual inline styles. You do NOT need to write any `::before`/`::after` CSS in your markdown.

| Layer | What It Does | Source |
|---|---|---|
| **1. Mesh Gradient** | Atmospheric radial-gradient blobs | Archetype CSS (`background` on `.slidev-layout`) |
| **2. Background Texture** | Dot grid / graph paper | Archetype CSS (`::after` on `.slidev-layout`) |
| **3. Decorative Accents** | Particles, corner lines, tape strips | Archetype CSS (`::before` on `.slidev-layout` / `.card`) |
| **4. Content** | Cards, pills, titles, charts | Your markdown + Vue components |

**All layers are automatic.** Simply set `class: style-school` in frontmatter and the entire visual system activates.

---

## Slide Architecture: The Power Flow

Structure every deck as a **4-Act journey**. Module names adapt to the topic:

| Act | Purpose | Duration | Slidev Pattern |
|-----|---------|----------|---------------|
| **The Hook** | Unlock curiosity, promise the superpower | 1–2 slides | `layout: center`, dark background, big type |
| **The Modules (2-3)** | Deliver the learning in labelled chunks | 3–5 slides each | Mix `two-cols`, `fact`, `image-right` |
| **The Bridge** | Break the fourth wall, interactive moment | 1 slide per module | `ACTIVITY` / `VOTE TIME` callout |
| **The Finale** | Mission, call to action, end energy high | 1–2 slides | `layout: end` or `layout: center`, dark background |

**Label every module** with a `.module-label` pill:
```html
<div class="module-label">Module 1 · The Brain</div>
```

---

## Slide-by-Slide Layout Variation

**Never repeat the same layout twice in a row.** Rotate through these:

| Layout | Best For |
|--------|---------|
| `layout: center` | Thematic titles, hooks, big quotes |
| `layout: fact` | Single powerful statistic |
| `layout: two-cols` | Comparisons, before/after, dual concepts |
| `layout: image-right` | Story + supporting visual |
| `layout: end` | Finale slide |

---

## Icon Safety Protocol

**Always verify icons before writing them into slides.** The Carbon set uses non-obvious names.

```bash
# Verify an icon exists
python -c "import json; data=json.load(open('node_modules/@iconify-json/carbon/icons.json')); print([k for k in data['icons'].keys() if 'keyword' in k])"
```

**Known Name Traps:**
| You might write | Actual Carbon ID |
|----------------|-----------------|
| `carbon:brain` | ❌ Does NOT exist → use `carbon:cognitive` |
| `carbon:robot` | ❌ Does NOT exist → use `carbon:bot` |
| `carbon:agriculture` | ❌ Does NOT exist → use `carbon:agriculture-analytics` |
| `carbon:pill` | ❌ Does NOT exist → use `carbon:pills` |
| `carbon:noise-selective` | ❌ Does NOT exist → use `carbon:error-filled` |

---

## QA Protocol

**Assume there are problems. Your job is to find them.**

### Step 1: Icon Check
Run a verification search on every icon used before saving the file.

### Step 2: Syntax Check
Every `v-click`, `v-motion`, `<div>`, `<ul>`, and `<li>` that opens must close. Unclosed tags cause Vite's "Invalid end tag" errors.

**Common pitfall**: `<v-click class="...">` wrapping block-level elements can cause Vue parser issues. Prefer wrapping in a `<div v-click>`.

**Known Parser Trap — Icon as Flex Sibling**: Never place a self-closing icon tag (e.g. `<carbon:arrow-right/>`) as a *direct sibling* between flex or grid children. The Vue template parser loses context and renders all subsequent HTML as raw escaped text. Use a plain text character (`→`) or wrap the icon in a `<div>` container instead.

**Known Parser Trap — Multiple Root Elements**: Each Slidev slide can only have **one root-level HTML element**. If a slide has geo-circle `<div>`s AND a main content `<div>` as siblings at the top level, Vue's SFC parser throws "Invalid end tag." Always wrap everything in a single `<div class="relative w-full h-full">`.



### Step 3: Live Preview Check
After saving, check the terminal running `npm run dev` for:
- `Icon not found` → verify the icon name
- `Invalid end tag` → find unclosed HTML in the problem slide number
- `Pre-transform error` → usually a syntax issue in the slide indicated

### Step 4: Visual Rhythm Check
Mentally scroll through your slides and check:
- [ ] No two consecutive slides share the same background color
- [ ] Every slide has at least one non-text visual element (icon, image, shape, or decorative circle)
- [ ] Text does not overflow its container
- [ ] Module labels and headings are present and correctly capitalized

---

## File Structure

```
slidev/
├── slides.md              # Staging area — npm run dev reads this
├── presentations/         # Master archive for all decks
│   ├── mughal_empire.md
│   ├── history_of_islam.md
│   └── ...
├── style.css              # Global entry point — imports all archetype CSS
├── styles/                # The CSS Engine (HSL tokens, mesh gradients, glassmorphism)
│   ├── school.css         # Neon Cosmos archetype
│   ├── business.css       # Corporate Executive archetype
│   └── workshop.css       # Warm Paper / Blueprint archetype
├── components/            # Vue components
│   ├── SlideCard.vue      # Primary card with glassmorphism
│   ├── CategoryPill.vue   # Inline label with archetype styling
│   └── LiveChart.vue      # ECharts wrapper for animated data viz
├── layouts/               # Custom Slidev layouts
│   ├── default.vue        # Base layout with safe-zone padding
│   ├── cards.vue          # Auto-grid card layout with pill/title
│   └── split.vue          # Left text + right media layout
├── templates/             # Starter boilerplate for each archetype
│   ├── school.md
│   ├── business.md
│   └── workshop.md
├── scripts/               # Automation
│   └── optimize-assets.js # PNG→WebP asset pipeline
├── uno.config.ts          # UnoCSS with HSL token shortcuts
├── AGENTS.md              # Agent operational rules
├── SKILL.md               # This file — operational intelligence
├── STYLE_GUIDE.md         # Visual standards & color architecture
├── STYLES.md              # Archetype selection matrix
├── PRINCIPLES.md          # Strategic methodology
├── public/                # Static assets (images, logos)
│   └── *.webp             # Always referenced as /filename.webp
├── package.json           # Dependencies (Slidev, ECharts, Sharp, Vue)
└── extract_pptx.py        # Extract text from legacy .pptx files
```

---

## Common Workflows

### Create a new presentation from a topic

1. Run the **Pre-Draft Protocol** — state audience, topic, setting
2. Select the **Archetype** from `STYLES.md` based on your audience audit
3. Copy the matching **Template**: `Copy-Item templates/school.md presentations/<topic>.md`
4. Design the **Power Flow** — 3 module names specific to this topic
5. Generate **Cover Image** using the AI image tool
6. Run `npm run optimize` to convert to WebP
7. Write the slides in `presentations/<topic>.md` using Vue components
8. Stage for preview: `Copy-Item presentations/<topic>.md slides.md`
9. Verify all icons before saving
10. Check terminal for errors, test dark mode (`d` key)

### Switch between decks

```powershell
# Save current work
Copy-Item slides.md presentations/current_topic.md
# Load different deck
Copy-Item presentations/new_topic.md slides.md
```

### Migrate from a `.pptx` file

1. Run `python extract_pptx.py <file.pptx>` to extract text
2. Open `temp_pptx/ppt/slides/slide1.xml` to extract content structure
3. Select the closest archetype from `STYLES.md`
4. Rebuild the content in Slidev with `v-click`, `v-motion`, and Vue components

### Debug a Vite error

1. Note the **slide number** in the error (e.g., `slides.md__slidev_5.md:12`)
2. Count to that slide in `slides.md` (slides separated by `---`)
3. Check for: unclosed tags, invalid icon names, malformed frontmatter
4. Do a **full file overwrite** (not a patch) to flush Vite's virtual file cache

