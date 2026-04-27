import copy
from .schema import SlideContent
from .config import SPATIAL

class BoundGuard:
    def paginate(self, slide: SlideContent) -> list[SlideContent]:
        limit = SPATIAL["limits"].get(slide.content_type, SPATIAL["limits"]["default"])
        if not slide.items or len(slide.items) <= limit:
            return [slide]
            
        paginated = []
        chunks = [slide.items[i:i + limit] for i in range(0, len(slide.items), limit)]
        
        for idx, chunk in enumerate(chunks):
            new_slide = copy.deepcopy(slide)
            new_slide.items = chunk
            new_slide.title = f"{slide.title} ({idx+1}/{len(chunks)})"
            paginated.append(new_slide)
            
        return paginated

def get_dynamic_title_style(title: str, is_center: bool = False) -> str:
    char_count = len(title)
    base_rem = 3.5 if is_center else 2.8
    
    if char_count <= 20:
        size = base_rem
    elif char_count <= 40:
        size = base_rem * 0.8
    elif char_count <= 60:
        size = base_rem * 0.6
    else:
        size = base_rem * 0.5
        
    align = "text-align: center;" if is_center else ""
    return f"font-size: {size:.1f}rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; overflow-wrap: break-word; word-break: keep-all; pointer-events: auto; {align}"

def get_dynamic_desc_style(desc: str, is_center: bool = False) -> str:
    align = "text-align: center; margin: 0 auto;" if is_center else ""
    return f"font-size: 1.1rem; line-height: 1.5; max-width: 100%; opacity: 0.8; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; pointer-events: auto; {align}"

def get_dynamic_grid_box_style() -> str:
    return "background: rgba(255,255,255,0.07); padding: 1rem; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1); width: 100%; overflow: hidden;"

def get_cycle_bounds(item_count: int, title: str):
    # Enforce strict title clearance
    title_height = SPATIAL["title_clearance_aggressive"] if len(title) > 20 else SPATIAL["title_clearance_default"]
    available_y = SPATIAL["view_height"] - title_height - SPATIAL["footer_gap"]
    
    node_size = SPATIAL["cycle_node_default"]
    radius = min(SPATIAL["cycle_radius_max"], (available_y - node_size) / 2 - 10)
    
    return {
        "radius": radius,
        "node_size": node_size,
        "margin_top_px": 20 
    }
