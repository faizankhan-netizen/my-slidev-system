from .schema import SlideContent

class RhythmEngine:
    def __init__(self):
        self.history = []
        
    def validate(self, slide: SlideContent) -> SlideContent:
        if len(self.history) > 0:
            prev = self.history[-1]
            if prev.content_type == slide.content_type:
                slide.content_type = self._suggest_alternative(slide.content_type)
                
        self.history.append(slide)
        return slide
        
    def _suggest_alternative(self, blocked_type: str) -> str:
        fallbacks = {
            "concept": ["feature_grid", "comparison"],
            "comparison": ["concept", "feature_grid"],
            "feature_grid": ["concept", "process"],
            "process": ["concept", "feature_grid"],
            "data_point": ["quote", "concept"],
            "quote": ["data_point", "concept"],
        }
        
        options = fallbacks.get(blocked_type, ["concept"])
        return options[0]
