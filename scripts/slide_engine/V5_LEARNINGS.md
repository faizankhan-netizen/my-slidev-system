# Cinematic Engine V5: Refactor Learnings 🧠
*Date: 2026-04-27*

This document archives the critical technical and design shifts made during the migration from the hardcoded V3 pipeline to the intelligent V5 architecture.

## 1. The Death of Inline Styles (Design Sovereignty)
**Learning**: Hardcoding visual properties (hex colors, border-radii) in Python creates technical debt and prevents designers from skinning the deck.
**Solution**: Implemented a "Class-Only" interface. Python now only emits semantic classes like `.card` or `.pill`. 
*   **Result**: To change the look of every "School" card in every deck ever generated, we now only need to edit `school.css`. The Python code remains untouched.

## 2. Topic Intelligence vs. Manual Selection
**Learning**: Users often don't know which archetype fits their topic, leading to "Design Fatigue" where every deck looks the same.
**Solution**: Created a `TopicAnalyzer` with a hierarchical scoring system (Signals + Audience Boost + Tone Boost).
*   **Case Study**: "90s Fashion" automatically resolves to `style-editorial` (+10 signals). "Khilafah for Kids" resolves to `style-school` (+5 audience boost).

## 3. The "Vibrant Variety" Principle
**Learning**: Educational decks (School/Workshop) fail if they are static. A "single mix color bg" feels repetitive and drains audience attention.
**Solution**: 
*   **Background Palettes**: Archetypes can now define a `bg_palette` (e.g., the AI Superpower sophisticated vibrant palette). The engine rotates these colors per slide index.
*   **Texture Rotation**: Simultaneously rotating textures (Lined → Grid → Dots) prevents the "same slide" feeling and keeps the presentation alive.

## 4. Narrative Pacing (Arc Composer)
**Learning**: A presentation is a story, not a list. Every story has a rhythm.
**Solution**: Introduced the `ArcComposer`.
*   **The Arc**: Automatically assigns high energy to Hooks/Climaxes and calm energy to Reflection/Context slides. 
*   **Rhythm Rules**: Enforces a "Breather" slide after data-heavy content and limits consecutive text-heavy slides to prevent cognitive overload.

## 5. Luminance as a First-Class Citizen
**Learning**: Vibrant backgrounds are beautiful but dangerous for accessibility.
**Solution**: Integrated real-time `_hex_to_luminance` math into the `Orchestrator`. 
*   **Result**: As the background rotates from a deep Navy to a light Mint, the text color automatically flips between White and Dark Grey with zero user input.

---

## 🛠️ Technical Stack (V5)
- **Engine**: Python 3.11 (Logic) + Slidev (Rendering)
- **Intelligence**: `TopicAnalyzer` (Signal Bag) + `ArcComposer` (Position Mapping)
- **Styling**: CSS-Native (Design Sovereignty)
- **Validation**: `test_archetype_matrix.py` (Regression suite for 144+ combinations)

*"Architecture is the art of separating what changes from what stays the same."*
