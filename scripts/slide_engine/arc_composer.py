# Cinematic Engine V5 — Arc Composer
# Orchestrates narrative energy and pacing across a deck.
# Supports multiple templates: narrative, modular, gallery.
# RULE: Proportional mapping from slide index to template position.

ARC_TEMPLATES = {
    "narrative": {
        # Classic story arc: Hook -> Context -> Body -> Climax -> Reflection -> Closer
        "positions": ["hook", "context", "body", "body", "climax", "reflection", "closer"],
        "energy_map": {
            "hook": "high",
            "context": "calm",
            "body": "standard",
            "climax": "high",
            "reflection": "calm",
            "closer": "high"
        },
        "type_suggestions": {
            "hook": ["cover"],
            "context": ["quote", "section_intro"],
            "body": ["concept", "feature_grid", "comparison", "media_focus", "case_study", "process"],
            "climax": ["data_point", "cycle"],
            "reflection": ["quote"],
            "closer": ["finale"]
        }
    },
    "modular": {
        # Section-based: Hook -> Intro -> Content -> Content -> Activity -> Intro ...
        "positions": ["hook", "module_intro", "content", "content", "activity", 
                       "module_intro", "content", "content", "activity", "closer"],
        "energy_map": {
            "hook": "high",
            "module_intro": "standard",
            "content": "calm",
            "activity": "high",
            "closer": "high"
        },
        "type_suggestions": {
            "hook": ["cover"],
            "module_intro": ["section_intro", "agenda"],
            "content": ["concept", "feature_grid", "chart", "table", "process"],
            "activity": ["activity", "data_point"],
            "closer": ["finale"]
        }
    },
    "gallery": {
        # Flat showcase: Cover -> Showcase -> Showcase -> Showcase -> Closer
        "positions": ["cover", "showcase", "showcase", "showcase", "showcase", "closer"],
        "energy_map": {
            "cover": "high",
            "showcase": "calm",
            "closer": "calm"
        },
        "type_suggestions": {
            "cover": ["cover"],
            "showcase": ["media_focus", "concept"],
            "closer": ["finale"]
        }
    }
}

class ArcComposer:
    """
    Assigns energy and role to slides based on their position in a deck.
    """
    def __init__(self, arc_type: str = "narrative"):
        self.template = ARC_TEMPLATES.get(arc_type, ARC_TEMPLATES["narrative"])
    
    def assign_position(self, index: int, total: int) -> str:
        """Maps slide index to template position using proportional scaling."""
        positions = self.template["positions"]
        if total <= 1:
            return positions[0]
        # Scale template to actual count
        ratio = index / (total - 1)
        template_idx = min(int(ratio * (len(positions) - 1)), len(positions) - 1)
        return positions[template_idx]
    
    def get_energy(self, position: str) -> str:
        """Returns the energy level for a given position."""
        return self.template["energy_map"].get(position, "standard")

    def get_suggested_types(self, position: str) -> list[str]:
        """Returns suggested content types for a given position."""
        return self.template["type_suggestions"].get(position, ["concept"])
