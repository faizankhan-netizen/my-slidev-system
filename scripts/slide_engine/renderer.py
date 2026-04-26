from typing import List
from .schema import SlideContent
from .conductor import ArchetypeConductor
from .rhythm import RhythmEngine
from .templates import render_slide
from .boundguard import BoundGuard

class Pipeline:
    def __init__(self, global_theme: str = "style-business"):
        self.conductor = ArchetypeConductor(global_theme)
        self.rhythm = RhythmEngine()
        self.boundguard = BoundGuard()
        
    def render(self, script: List[SlideContent]) -> str:
        output = []
        for slide in script:
            validated_slide = self.rhythm.validate(slide)
            
            # Paginate if needed to prevent text bleed
            paginated_slides = self.boundguard.paginate(validated_slide)
            
            for pag_slide in paginated_slides:
                archetype = self.conductor.get_archetype(pag_slide)
                md = render_slide(pag_slide, archetype)
                output.append(md)
            
        return "\n".join(output)
