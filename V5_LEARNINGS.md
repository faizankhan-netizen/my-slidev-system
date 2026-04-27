# Cinematic Engine V5: Design Sovereignty & Scholarly Intelligence
**Date**: April 27, 2026
**Version**: 5.1 (Research Update)

## 1. Technical Breakthroughs

### Design Sovereignty vs. Archetype Overrides
We discovered that high-energy archetype "Variants" (e.g., `variant-cover`) often contain `!important` CSS rules for backgrounds. This was overriding the user's `custom_bg` intent. 
*   **Fix**: Updated `orchestrator.py` to disable variant resolution if a manual background override is detected.
*   **Learning**: The "Design Sovereignty" principle must ensure that user-specified tokens always sit at the top of the specificity hierarchy.

### Structural Intelligence (Hypothesis Flow)
Generic list-cards fail to represent the logical structure of research. 
*   **Pattern**: Replaced horizontal grids with **Vertical Stacks** for complex academic sentences.
*   **Component**: Created the `.hypothesis-box` — a high-contrast, structural element that signals academic authority through thick borders and monospaced tagging.

### The "Default Sparkle" Anti-Pattern
Default values in `schema.py` (like `emoji: "✨"`) act as "ghost baggage" that degrades the professional tone of a deck.
*   **Fix**: Moved to "Opt-In Visuals." All default icons were removed to ensure a clean, minimalist canvas for serious topics like dissertations.

## 2. Archetype Specification: `style-research`

| Feature | Specification |
|---|---|
| **Primary Palette** | Forest Teal (#1B5E4F), Ink Navy (#1B2333), Warm Ivory (#FAFAF8) |
| **Typography** | Source Serif 4 (Body/Headings) + IBM Plex Mono (Data/Labels) |
| **Structural Rule** | 12px accent-border-left for high-level research claims |
| **Pacing** | Vertical stacks for methodology; High-contrast ivory for data density |

## 3. Best Practices for Dissertation Defense
1.  **Split the Load**: Never put more than 2 high-level hypotheses on a single slide. Vertical height is the most precious resource in fixed-aspect presentations.
2.  **Data Grounding**: Use `.stat-giant` for sample sizes (N=100) and `.finding` callouts for p-values.
3.  **No Filler**: Academic audiences value density over decoration. Remove abstract quotes if they don't contain primary study goals.

## 4. Known Issues & Resolved Debt
*   **Vertical Bleed**: Resolved by removing the hardcoded "footer card" from the `render_concept` template.
*   **Text Ghosting**: Resolved by forcing `color: black !important` inside scholarly components to survive dark-mode transitions.
