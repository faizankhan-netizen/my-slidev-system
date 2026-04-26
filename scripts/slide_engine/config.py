# Cinematic Engine V3 Configuration Matrix

# --- Spatial Intelligence (BoundGuard) ---
SPATIAL = {
    "view_height": 540,
    "footer_gap": 60,
    "title_clearance_default": 140,
    "title_clearance_aggressive": 160,
    "cycle_radius_max": 120,
    "cycle_node_default": 90,
    "pagination_limit": 4,
}

# --- Visual Tokens ---
STYLES = {
    "wrapper": "position:relative; z-index:10; height:100%; display:flex; flex-direction:column; pointer-events:none;",
    "wrapper_center": "position:relative; z-index:10; height:100%; display:flex; flex-direction:column; justify-content: center; align-items: center; text-align: center; pointer-events:none;",
    "pill": "display:inline-block; width: fit-content; padding:4px 12px; border-radius:30px; font-size:10px; font-weight:900; letter-spacing:2px; text-transform:uppercase; margin-bottom: 0.8rem; border: 1px solid rgba(255,255,255,0.2); white-space: nowrap; background: rgba(255,255,255,0.1); pointer-events:auto;",
    "grid_box": "background: rgba(255,255,255,0.07); padding: 1rem; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1); width: 100%; overflow: hidden; pointer-events: auto;"
}

# --- Motion Physics ---
ENERGY_PROPS = {
    "high": {"initial": {"opacity": 0, "y": 50, "scale": 0.9}, "enter": {"opacity": 1, "y": 0, "scale": 1, "transition": {"type": "spring", "stiffness": 250, "damping": 15}}},
    "calm": {"initial": {"opacity": 0, "y": 20}, "enter": {"opacity": 1, "y": 0, "transition": {"duration": 800}}},
    "standard": {"initial": {"opacity": 0, "x": -30}, "enter": {"opacity": 1, "x": 0, "transition": {"duration": 500}}}
}
