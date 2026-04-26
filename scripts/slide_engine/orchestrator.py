from dataclasses import dataclass
from typing import Optional
import re
from .schema import SlideContent
from .boundguard import get_cycle_bounds # Absorbing the Spatial Engine
from .context import ARCHETYPES

# --- COMPUTED STATE SCHEMA ---
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
    
    # Vue/Structural Flags
    show_nav: bool
    energy_level: str
    
    # Spatial Payloads (From BoundGuard)
    cycle_radius: int = 0
    cycle_node_size: int = 0
    cycle_margin_top: int = 0

# --- PHASE 3: THE ORCHESTRATOR BRAIN ---
def _hex_to_luminance(hex_color: str) -> float:
    """Calculates perceived brightness. Returns 0.0 (Dark) to 1.0 (Light)."""
    if not hex_color:
        return 0.0
        
    # GRADIENT BLINDNESS FIX: Extract the first hex color from a gradient string
    if "gradient" in hex_color:
        import re
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
    except:
        return 0.0

def orchestrate_slide(content: SlideContent, archetype: str) -> ComputedSlideState:
    theme = ARCHETYPES.get(archetype, ARCHETYPES["default"])
    
    # 1. Intent Resolution (Custom BG overrides Archetype default)
    bg_color = content.custom_bg
    if not bg_color:
        bg_color = theme["colors"].get(content.energy, theme["colors"]["medium"])
        
    # 2. Luminance Math & Contrast Enforcement
    text_color = "#FFFFFF" # Default Light Text for Dark BGs
    
    if content.custom_text == "dark":
        text_color = "#1A1F5E"
    elif content.custom_text == "light":
        text_color = "#FFFFFF"
    else:
        # The Engine calculates it automatically
        lum = _hex_to_luminance(bg_color)
        if lum > 0.5:
            text_color = "#1A1F5E" # Dark text for light bg
            
    # 3. Spatial Resolution (Calling BoundGuard)
    radius = 0
    node_size = 0
    margin_top = 0
    if content.content_type == "cycle" and hasattr(content, 'items'):
        bounds = get_cycle_bounds(len(content.items), content.title)
        radius = bounds["radius"]
        node_size = bounds["node_size"]
        margin_top = bounds["margin_top_px"]
            
    # 4. Lock and return the State
    return ComputedSlideState(
        slide_bg=bg_color,
        slide_text=text_color,
        accent_color=theme["colors"].get("accent_primary", theme["colors"].get("accent", "#FFFFFF")),
        accent_secondary=theme["colors"].get("accent_secondary", "#FFFFFF"),
        accent_tertiary=theme["colors"].get("accent_tertiary", "#FFFFFF"),
        font_family=theme["fonts"],
        show_nav=True,
        energy_level=content.energy,
        cycle_radius=radius,
        cycle_node_size=node_size,
        cycle_margin_top=margin_top
    )
