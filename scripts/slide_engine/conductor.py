from .schema import SlideContent

ACT_STYLES = {
    1: "style-space",      # Act 1: The Hook (Cinematic, Visionary)
    2: "style-cyber",      # Act 2: Architecture (Technical, Dark)
    3: "style-business",   # Act 3: Implementation (Corporate, Clean)
    4: "style-school",     # Act 4: Human Factor (Accessible, Energetic)
    5: "style-luxury",     # Act 5: Vision/Future (Premium, Minimalist)
}

class ArchetypeConductor:
    def __init__(self, global_theme: str = "style-business"):
        self.global_theme = global_theme

    def get_archetype(self, slide: SlideContent) -> str:
        return self.global_theme

