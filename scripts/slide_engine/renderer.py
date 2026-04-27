from typing import List
from .schema import SlideContent
from .conductor import ArchetypeConductor
from .rhythm import RhythmEngine
from .templates import render_slide
from .boundguard import BoundGuard

class Pipeline:
    """
    The main V5 rendering pipeline.
    Orchestrates topic analysis, narrative arcs, and design sovereignty.
    """
    def __init__(self, global_theme: str = None, topic: str = "", 
                 audience: str = "", tone: str = "", arc_type: str = "narrative"):
        # Phase C: Auto-resolve archetype if no global_theme provided
        self.conductor = ArchetypeConductor(global_theme, topic, audience, tone)
        self.arc_type = arc_type
        self.boundguard = BoundGuard()
        self.rhythm = None # Initialized during render to know total count

    def render(self, script: List[SlideContent]) -> str:
        # Initialize rhythm engine with knowledge of deck length
        self.rhythm = RhythmEngine(self.arc_type, len(script))
        output = []
        
        for idx, slide in enumerate(script):
            # Phase D: Validate rhythm and assign arc-based energy
            validated_slide = self.rhythm.validate(slide, idx)
            
            # Paginate if needed to prevent text bleed (Spatial Engine)
            paginated_slides = self.boundguard.paginate(validated_slide)
            
            for pag_slide in paginated_slides:
                # Phase A: Design Sovereignty — get class-mapped archetype
                archetype = self.conductor.get_archetype(pag_slide)
                md = render_slide(pag_slide, archetype, index=idx)
                output.append(md)
            
        return "\n".join(output)
