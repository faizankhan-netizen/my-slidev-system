from dataclasses import dataclass, field
from typing import Optional
import re
from .schema import SlideContent
from .boundguard import get_cycle_bounds
from .context import ARCHETYPES

# --- COMPUTED STATE SCHEMA (V5) ---
@dataclass
class ComputedSlideState:
    """The final, locked-in design token payload. No logic allowed past this point."""

    # CSS Variable Payloads
    slide_bg: str
    slide_text: str
    accent_color: str
    accent_secondary: str
    accent_tertiary: str
    font_family: str

    # Phase 0 fix: correct font import URL per archetype
    font_import: str

    # Vue/Structural Flags
    show_nav: bool
    energy_level: str

    # Spatial Payloads (BoundGuard)
    cycle_radius: int = 0
    cycle_node_size: int = 0
    cycle_margin_top: int = 0

    # Phase A: Structural Sovereignty — CSS class names only, never style strings
    card_class: str = ""       # e.g. "card" — activates .style-X .card in CSS
    pill_class: str = ""       # e.g. "pill" — activates .style-X .pill in CSS
    stat_class: str = ""       # e.g. "stat", "stat-giant", "tech-stat"
    wrapper_class: str = ""    # e.g. "content-wrapper" for archetypes that define it
    variant_class: str = ""    # e.g. "variant-red" for high-energy editorial
    use_kinetic_shapes: bool = True


# --- LUMINANCE MATH ---
def _hex_to_luminance(hex_color: str) -> float:
    """Calculates perceived brightness. Returns 0.0 (Dark) to 1.0 (Light)."""
    if not hex_color:
        return 0.0

    # Extract first hex from gradient strings
    if "gradient" in hex_color:
        match = re.search(r'#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})', hex_color)
        if match:
            hex_color = match.group(0)
        else:
            return 0.0

    if not hex_color.startswith('#'):
        return 0.0

    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 3:
        hex_color = ''.join(c + c for c in hex_color)

    try:
        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        return (0.299 * r + 0.587 * g + 0.114 * b) / 255.0
    except Exception:
        return 0.0


# --- THE ORCHESTRATOR BRAIN (V5) ---
def orchestrate_slide(content: SlideContent, archetype: str, index: int = 0) -> ComputedSlideState:
    theme = ARCHETYPES.get(archetype, ARCHETYPES["default"])
    css = theme.get("css_classes", {})

    # 1. Intent Resolution — custom BG overrides archetype default
    bg_color = content.custom_bg
    if not bg_color:
        # Phase D: Auto-variety via bg_palette (if archetype defines it)
        palette = theme.get("bg_palette")
        if palette and len(palette) > 0:
            bg_color = palette[index % len(palette)]
        else:
            energy_key = content.energy if content.energy in theme["colors"] else "medium"
            bg_color = theme["colors"].get(energy_key, theme["colors"]["medium"])

    # 2. Luminance Math & Automatic Contrast Enforcement
    if content.custom_text == "dark":
        text_color = "#1A1A1A"
    elif content.custom_text == "light":
        text_color = "#FFFFFF"
    else:
        lum = _hex_to_luminance(bg_color)
        text_color = "#1A1A1A" if lum > 0.5 else "#FFFFFF"

    # 3. Spatial Resolution (BoundGuard)
    radius = node_size = margin_top = 0
    if content.content_type == "cycle" and hasattr(content, 'items'):
        bounds = get_cycle_bounds(len(content.items), content.title)
        radius    = bounds["radius"]
        node_size = bounds["node_size"]
        margin_top = bounds["margin_top_px"]

    # 4. Variant Resolution — auto-apply CSS variant class
    variant_class = ""
    
    # Skip variant logic if user has provided a custom background override
    if not content.custom_bg:
        # Phase D: Auto-texture rotation for variety
        texture_palette = theme.get("texture_palette")
        if texture_palette and len(texture_palette) > 0:
            variant_class = texture_palette[index % len(texture_palette)]
        else:
            threshold = theme.get("variant_energy_threshold")
            if threshold and content.energy == threshold and theme.get("variants"):
                variant_class = theme["variants"][0]

    # 5. Lock and return the State
    return ComputedSlideState(
        slide_bg         = bg_color,
        slide_text       = text_color,
        accent_color     = theme["colors"].get("accent_primary",   "#FFFFFF"),
        accent_secondary = theme["colors"].get("accent_secondary", "#FFFFFF"),
        accent_tertiary  = theme["colors"].get("accent_tertiary",  "#FFFFFF"),
        font_family      = theme["fonts"],
        font_import      = theme.get("font_import", "Inter:wght@400;700"),
        show_nav         = True,
        energy_level     = content.energy,
        cycle_radius     = radius,
        cycle_node_size  = node_size,
        cycle_margin_top = margin_top,
        # Phase A: CSS class names
        card_class       = css.get("card", ""),
        pill_class       = css.get("pill", ""),
        stat_class       = css.get("stat", ""),
        wrapper_class    = css.get("wrapper", ""),
        variant_class    = variant_class,
        use_kinetic_shapes = theme.get("kinetic_shapes", True),
    )
