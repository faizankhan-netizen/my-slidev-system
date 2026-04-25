# Slidev Presentation Style Guide 🎨
*Version 1.0 — Inspired by "AI Superpower" & Modern Startup Keynotes*

This guide defines the aesthetic and structural DNA for high-impact, educational presentations created using Slidev. Follow these rules to maintain a **Premium, High-Energy, and Indocentric** brand identity.

---

## 1. Core Principles: Audience & Context
Design is a conversation between the speaker and the audience. Every visual choice must be justified by the context:
- **Audience Empathy**: Is this for a 12-year-old student or a CEO? For students, use vibrant imagery and relatable terms (*Murga-Murgi*). For executives, use data-dense layouts and industry terminology.
- **Subject-Matter Harmony**: The visuals must match the mood. **Slate Navy & Safety Orange** was chosen as our current baseline because it evokes the "Industrial-meets-Modern" spirit of Agri-Tech and startups.
- **Functional Minimalism**: Whitespace is not empty space; it is "focus space." Every element on a slide must earn its right to be there.
- **Narrative Pacing**: Use `v-click` to control the "dose" of information. High-energy storytelling requires revealing one surprise at a time.


---

## 2. Color Palette & Typography
| Element | Style | Value / Hex |
| :--- | :--- | :--- |
| **Primary** | Deep Navy / Slate | `#1E293B` |
| **Accent** | Safety Orange | `#F97316` |
| **Background** | Off-White / Light Grey | `#F8FAFC` |
| **Headings** | Extra Bold / Black | `text-7xl font-black tracking-tight` |
| **Subheadings** | Bold / All Caps | `text-sm font-bold tracking-widest opacity-50` |

---

## 3. Structural Framework: The "Power" Flow
Break presentations into a 4-part narrative structure:
1.  **The Hook**: High-impact visual or a "Superpower" promise.
2.  **The Modules**: Segment content into 3-4 logical blocks (e.g., "MODULE 1: The Brain").
3.  **The Interactive Bridge**: Every module must have an activity or a "Live Demo."
4.  **The Finale**: A collaborative "Big Build" or a call to action.

---

## 4. Writing & Tone of Voice
- **Direct Address**: Use "You," "We," and "Let's." (e.g., "Your superpower: ACTIVATED.")
- **Indocentricity**: Ground examples in Indian reality (Agriculture, Bollywood, Local languages). Use Hinglish terms naturally (e.g., "Kheti," "Bharat ka AI").
- **Power Words**: Use short, punchy labels: `ACTIVITY`, `LIVE DEMO`, `VOTE TIME`, `MISSION`.

---

## 5. Slidev-Specific Implementation
### Layout Selection
- **`fact`**: For big statistics (e.g., "3rd Largest").
- **`center`**: For thematic titles and core definitions.
- **`two-cols`**: For side-by-side comparisons or career matrices.
- **`quote`**: For powerful industry statements.

### Motion & Interactivity
- **`v-click`**: Mandatory for progressive storytelling. Reveal one point at a time.
- **`v-motion`**: Use sparingly for "Wow" moments (e.g., T-Rex to Chicken transition).
- **Icons**: Use Carbon icons (`<carbon:xxx/>`) for all functional labels (e.g., `<carbon:robot>` for tech).

---

## 6. Image Standards
- **Source**: High-quality, cinematic AI-generated or professional photography.
- **Style**: Warm lighting, rural-meets-modern aesthetics.
- **Placement**: Full-bleed backgrounds or clean `image-right/left` splits.

---

## 7. Example Header (Global Style)
```markdown
<style>
h1 { @apply text-7xl font-black uppercase tracking-tight mb-4; color: #1e293b; }
h2 { @apply text-4xl font-bold mb-4; color: #1e293b; }
.accent { color: #f97316; }
.bg-accent { background-color: #f97316; }
</style>
```

## 8. Adaptability & Content Flow
While the **Aesthetic DNA** (colors, type, labels) is fixed, the **Narrative Arc** must adapt to the subject:
- **Technical Subjects**: Focus on "The Loop" and "Smart Tech" modules.
- **Business Subjects**: Focus on "Market Matrix" and "Rapid ROI" modules.
- **Social/Humanitarian**: Focus on "Definition" and "Mission" modules.

**Rule of Thumb**: Maintain the *Module -> Activity -> Mission* pattern, but feel free to rename modules (e.g., "The Lab" instead of "The Foundation") to fit the topic's personality.

---

*“The ideas are yours. AI is just the paintbrush.”* ⚡

