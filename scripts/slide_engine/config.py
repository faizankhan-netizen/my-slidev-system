# Cinematic Engine V5 — Configuration Matrix
# RULE: STYLES contains only STRUCTURAL layout properties.
# Visual properties (color, border, shadow, backdrop, radius) live in CSS files.

# --- Spatial Intelligence (BoundGuard) ---
SPATIAL = {
    "view_height": 540,
    "footer_gap": 60,
    "title_clearance_default": 140,
    "title_clearance_aggressive": 160,
    "cycle_radius_max": 120,
    "cycle_node_default": 90,
    "limits": {
        "default": 4,
        "cycle": 6,
        "agenda": 6,
        "feature_grid": 4
    }
}

# --- Structural Layout Tokens (NO visual properties) ---
# Only: display, flex, grid, gap, width, height, margin, padding, align, justify
STYLES = {
    # Wrappers — structural only; visual comes from .content-wrapper CSS class
    "flex_col":         "display:flex; flex-direction:column; height:100%;",
    "flex_col_center":  "display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; height:100%;",
    "flex_row":         "display:flex; flex-direction:row; width:100%; height:100%; gap:3rem;",
    "flex_col_left":    "display:flex; flex-direction:column; justify-content:center;",
    # Grids
    "grid_2col":        "display:grid; grid-template-columns:1fr 1fr; gap:1.5rem; width:100%;",
    "grid_2col_asym":   "display:grid; grid-template-columns:1.2fr 0.8fr; gap:3rem; width:100%; height:100%;",
    "grid_fill":        "display:grid; grid-template-columns:1fr 1fr; gap:1.5rem; width:100%; margin-top:1rem; flex:1;",
    # Misc structural
    "media_col":        "flex:1.2; padding:1rem;",
    "text_col":         "flex:1; display:flex; flex-direction:column; justify-content:center;",
}

# --- Motion Physics ---
ENERGY_PROPS = {
    "high":     {"initial": {"opacity": 0, "y": 50, "scale": 0.9}, "enter": {"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15}}},
    "calm":     {"initial": {"opacity": 0, "y": 20},               "enter": {"opacity": 1, "y": 0, "transition": {"duration": 800}}},
    "standard": {"initial": {"opacity": 0, "x": -30},              "enter": {"opacity": 1, "x": 0, "transition": {"duration": 500}}},
    "medium":   {"initial": {"opacity": 0, "y": 20},               "enter": {"opacity": 1, "y": 0, "transition": {"duration": 600}}},
}
