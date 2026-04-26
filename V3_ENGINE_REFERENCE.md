# Slidev Cinematic Engine V3: Technical Reference (Refactored)

## 🚀 Overview
Version 3.1 represents the professionalization of the engine. It is now a **Component-Driven, Config-First Architecture**.

## 🏗️ Core Components

### 🎬 CinematicBackdrop.vue
Located in `components/`. This is the single source of truth for all background media.
- **YouTube Support**: Robust Regex-based ID extraction.
- **Interactive GUI**: Built-in hover menu for live URL swapping.
- **State Management**: Handles `v-model` sync with Slidev frontmatter.

### 🧠 BoundGuard (Spatial Intelligence)
Located in `scripts/slide_engine/boundguard.py`. 
- **Steel-Wall Protocol**: Ensures 160px title clearance.
- **Auto-Scaling**: Dynamically adjusts font sizes based on text density.
- **Config-Driven**: Reads all bounds from `config.py`.

## ⚙️ Configuration Matrix
All engine tuning happens in **`scripts/slide_engine/config.py`**.
- `SPATIAL`: View heights, gaps, and radii.
- `STYLES`: Master CSS tokens for wrappers, pills, and grids.
- `ENERGY_PROPS`: Motion physics mapping (high, calm, standard).

## 🧩 Agent Rules (MANDATORY)

1. **Propagate Context**: When adding a new layout, add it to `templates.py` but move the complex HTML into a `.vue` component first.
2. **Respect the Config**: Never hardcode a pixel value in `templates.py`. Always add it to `config.py` first.
3. **Component-First**: If a UI element needs state (like a toggle or input), it belongs in a Vue component, not a Python f-string.

---

*"Clean Code. Cinematic Result. Constant Evolution."* ⚡ mosque
