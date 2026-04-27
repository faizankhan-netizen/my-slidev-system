from .schema import SlideContent
from .topic_analyzer import TopicAnalyzer

# ACT_STYLES removed — it contradicted archetype sovereignty.
# Energy variation within a single archetype replaces cross-archetype switching.

class ArchetypeConductor:
    """
    Resolves the archetype for a deck.
    Priority: explicit global_theme > topic-based auto-resolution.
    Per-slide archetype switching (ACT_STYLES) is intentionally removed.
    """
    def __init__(self, global_theme: str = None, topic: str = "",
                 audience: str = "", tone: str = ""):
        self._analyzer = TopicAnalyzer()

        if global_theme:
            self.global_theme = global_theme  # Manual override always wins
        else:
            self.global_theme = self._analyzer.resolve(topic, audience, tone)

    def get_archetype(self, slide: SlideContent) -> str:
        """Returns the deck-level archetype. Consistent across all slides."""
        return self.global_theme
