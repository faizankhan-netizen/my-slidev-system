from .schema import SlideContent
from .arc_composer import ArcComposer

class RhythmEngine:
    """
    Ensures visual variety and manages narrative pacing.
    V2 features: text-heavy slide limits, breather slides, and arc-aware suggestions.
    """
    TEXT_HEAVY = {"concept", "process", "feature_grid", "table", "chart"}
    DATA_INTENSE = {"data_point", "cycle", "chart", "table"}

    def __init__(self, arc_type: str = "narrative", total_slides: int = 10):
        self.history: list[SlideContent] = []
        self.arc = ArcComposer(arc_type)
        self.total_slides = total_slides

    def validate(self, slide: SlideContent, index: int) -> SlideContent:
        """
        Applies rhythm rules and arc-based energy/type defaults.
        """
        # 1. Arc-based Defaults (if not explicitly set)
        position = self.arc.assign_position(index, self.total_slides)
        
        # Auto-energy if not already forced
        if not hasattr(slide, '_energy_explicit') or not slide._energy_explicit:
             slide.energy = self.arc.get_energy(position)

        # 2. Sequential Variety Rules
        if len(self.history) > 0:
            prev = self.history[-1]
            
            # Rule A: No consecutive duplicates of same content type
            if prev.content_type == slide.content_type:
                slide.content_type = self._suggest_alternative(slide.content_type)
            
            # Rule B: Max 2 consecutive text-heavy slides
            if self._consecutive_count(self.TEXT_HEAVY) >= 2 and slide.content_type in self.TEXT_HEAVY:
                # Force a visual break
                slide.content_type = "media_focus" if slide.media_url else "quote"
            
            # Rule C: Breather slide after intense data/spatial slides
            if prev.content_type in self.DATA_INTENSE:
                if slide.energy == "high":
                    slide.energy = "calm" # Soften the transition

        self.history.append(slide)
        return slide

    def _consecutive_count(self, type_set: set[str]) -> int:
        count = 0
        for s in reversed(self.history):
            if s.content_type in type_set:
                count += 1
            else:
                break
        return count

    def _suggest_alternative(self, blocked_type: str) -> str:
        fallbacks = {
            "concept": ["feature_grid", "comparison", "media_focus"],
            "comparison": ["concept", "feature_grid"],
            "feature_grid": ["process", "concept"],
            "process": ["feature_grid", "concept"],
            "data_point": ["quote", "media_focus", "concept"],
            "quote": ["data_point", "concept"],
            "media_focus": ["concept", "feature_grid"],
        }
        
        options = fallbacks.get(blocked_type, ["concept"])
        return options[0]
