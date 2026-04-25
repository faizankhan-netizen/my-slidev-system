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

3. **The 2-Layer Content Structure**
   Now that the background and safe-zone padding are on the layout, slides use a simplified structure:
   ```html
   <div class="content-wrapper" style="position:relative; z-index:10; width:100%;">
      <!-- Text and interactive elements go here -->
   </div>
   ```

4. **Density-Aware Scaling (The Bleed Prevention Rule)**
   - **Titles:** Cap at `3rem` for dense slides (3+ cards/items).
   - **Gaps:** Use `gap: 15px` for horizontal card layouts.
   - **Safe Zone:** All text must stay within the `3.5rem` padding buffer. If content approaches the bottom edge, downscale fonts or simplify descriptions immediately.

5. **Graphic Positioning**
   - **Absolute Accents:** Use `top`, `left`, etc. for decorative dots. Note that they position relative to the *padded* layout, so `top:0` starts at the padding edge.
   - **Bleed Geometry:** Use `::before/::after` pseudo-elements for large edge-bleed shapes to keep the DOM clean.

### 🚨 Critical Parser Rules (Do Not Break)
1. **Single Root Element:** Every slide must have exactly ONE root `<div>`.
2. **Zero Blank Lines:** Never leave a blank line between nested `<div>` tags. This breaks the markdown-it parser and leaks raw HTML text to the screen.
3. **Slide Numbering Safety:** Never place a `---` separator between a `<style>` block and the first slide's content. This creates a "Blank Slide 1". Keep the style block at the very top, within the global frontmatter or immediately attached to Slide 1.
4. **The Flex Stretch Trap:** In a `flex-direction: column` layout, children (like pills) will stretch to 100% width by default. Always use `align-items: flex-start` on the `.content-wrapper` to keep UI elements proportionate.
5. **Markdown-in-HTML Limitation:** Markdown syntax (like `**bold**`) does NOT render inside HTML tags. Always use HTML tags (`<b>`, `<strong>`) or `<span style="...">` for text highlighting within layout blocks.
6. **Icon Sibling Safety:** Never place a `<carbon:icon />` as a direct sibling of a `<div>` inside a flex container. Wrap icons in a `<span>` to prevent template parsing crashes.
7. **Safe Zone Discipline:** To respect the `3.5rem` safety buffer, cap main titles at `2.8rem` - `3.2rem` and use `width: 100%` on containers to ensure they wrap within the padding instead of overflowing.
8. **No Tailwind Arbitrary Values:** Avoid `w-[350px]` in Vue templates; use `style="width: 350px"` to prevent parser confusion.



# Slidev Presentation Skill

## Quick Reference

| Task | Action |
|------|--------|
| Create a new presentation | Run Pre-Draft Protocol → Write `slides.md` |
| Read a `.pptx` for style reference | Run `python extract_pptx.py <file.pptx>` |
| Preview slides | `npm run dev` → open `http://localhost:3030` |
| Verify an icon exists | `python -c "import json; data=json.load(open('node_modules/@iconify-json/carbon/icons.json')); print([k for k in data['icons'].keys() if 'keyword' in k])"` |
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

---

## Color Palette Library

Choose colors specific to the topic — never default to generic blue.

| Theme | Background | Primary | Accent | Use For |
|-------|-----------|---------|--------|---------|
| **AI Superpower** | `#1A1F5E` deep navy | `#FF6B35` orange | `#06D6A0` teal | High-energy student seminars |
| **Poultry / Agri** | `#1E293B` slate | `#F97316` orange | `#22C55E` green | Agricultural / rural topics |
| **Health / Medical** | `#0D9488` teal | `#FB7185` coral | `#F8FAFC` off-white | Health awareness for students |
| **Corporate** | `#1E2761` navy | `#CADCFC` ice blue | `#FFFFFF` white | Executive presentations |
| **Nature / Environment** | `#2C5F2D` forest | `#97BC62` moss | `#F5F5F5` cream | Ecology, sustainability |
| **Finance / Business** | `#36454F` charcoal | `#F2F2F2` off-white | `#FFD700` gold | Finance, strategy decks |

**Rule of Dominance**: One color carries 60-70% visual weight. Max 3 colors per deck.

---

## "Geometric Life" — The Core Visual System

The original AI Superpower deck's secret weapon: **circles and blobs that bleed off the slide edges**, creating depth and breaking the "rectangular prison."

Replicate this in Slidev using CSS on `.slidev-layout`:

```css
/* Edge-bleed geometric circles */
.slidev-layout::before {
  content: "";
  position: absolute;
  width: 500px;
  height: 500px;
  background: rgba(255, 107, 53, 0.15); /* Use topic accent color */
  border-radius: 50%;
  top: -200px;
  right: -200px;
  z-index: 0;
  animation: float 12s infinite alternate ease-in-out;
}

@keyframes float {
  from { transform: translate(0, 0); }
  to { transform: translate(40px, 40px); }
}
```

**Small "Confetti" Dots**: Use inline `<div>` elements with varying sizes and topic colors to scatter across the slide background.

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
├── slides.md          # Source of truth — ALL content lives here
├── AGENTS.md          # Operational rules for AI agents
├── STYLE_GUIDE.md     # Default visual standards and color tokens
├── PRINCIPLES.md      # Strategic methodology: audience → design mapping
├── SKILL.md           # This file — operational intelligence for presentations
├── extract_pptx.py    # Extract text from legacy .pptx files
└── public/            # Static assets (images, logos)
    └── *.png          # Always referenced as /filename.png in slides.md
```

---

## Common Workflows

### Create a new presentation from a topic

1. Run the **Pre-Draft Protocol** — state audience, topic, setting
2. Pick a **Color Palette** from the library above that fits the topic
3. Design the **Power Flow** — 3 module names specific to this topic
4. Write `slides.md` with a `<style>` block at the top defining the palette
5. Verify all icons before saving
6. Check terminal for errors

### Migrate from a `.pptx` file

1. Run `python extract_pptx.py <file.pptx>` to extract text
2. Open `temp_pptx/ppt/slides/slide1.xml` to extract hex color codes and shape types
3. Use those exact colors in the `<style>` block of the new `slides.md`
4. Rebuild the content in Slidev with enhanced interactivity (`v-click`, `v-motion`)

### Debug a Vite error

1. Note the **slide number** in the error (e.g., `slides.md__slidev_5.md:12`)
2. Count to that slide in `slides.md` (slides separated by `---`)
3. Check for: unclosed tags, invalid icon names, malformed frontmatter
4. Do a **full file overwrite** (not a patch) to flush Vite's virtual file cache
