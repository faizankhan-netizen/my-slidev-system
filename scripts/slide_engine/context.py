# Universal Design Context (V5)
# Central registry for all archetype tokens.
# RULE: css_classes contains ONLY class name strings — no style values, ever.
# Visual properties live exclusively in the CSS files under /styles/*.css

ARCHETYPES = {
    "style-research": {
        "fonts": "'Source Serif 4', 'IBM Plex Sans', serif",
        "font_import": "Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,700;1,8..60,400&family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;600",
        "colors": {
            "calm":   "#FAFAF8", # Warm Ivory
            "medium": "#F0EDE6", # Aged Paper
            "high":   "#1B2333", # Deep Ink Navy
            "accent_primary":   "#1B5E4F", # Forest Teal
            "accent_secondary": "#B5451B", # Rust Red (citations)
            "accent_tertiary":  "#2C4A8C"  # Academic Blue
        },
        "css_classes": {
            "card":     "card",
            "pill":     "pill",
            "stat":     "stat",
            "citation": "citation",
            "finding":  "finding",
            "footnote": "footnote",
            "wrapper":  ""
        },
        "kinetic_shapes": False,
        "has_decorative_layer": True,
        "variants": ["variant-cover", "variant-chapter"],
        "variant_energy_threshold": "high"
    },

    "style-editorial": {
        "fonts": "'Playfair Display', serif",
        "font_import": "Playfair+Display:ital,wght@0,700;0,900;1,700&family=Inter:wght@400;700",
        "colors": {
            "calm":   "#FDFBF7",
            "medium": "#F3F0E6",
            "high":   "#E5E0D8",
            "accent_primary":   "#991B1B",
            "accent_secondary": "#1A1A1A",   # Black — for hard contrast
            "accent_tertiary":  "#F5F5DC"    # Beige — for warmth
        },
        "css_classes": {
            "card":    "card",
            "pill":    "pill",
            "stat":    "stat-giant",
            "caption": "caption",
            "wrapper": "content-wrapper"
        },
        "kinetic_shapes": False,
        "has_decorative_layer": True,
        "variants": ["variant-red"],
        "variant_energy_threshold": "high"
    },

    "style-luxury": {
        "fonts": "'Cinzel', serif",
        "font_import": "Cinzel:wght@400;700;900&family=Cormorant+Garamond:ital,wght@0,300;0,600;0,700;1,300",
        "colors": {
            "calm":   "#18181B",
            "medium": "#27272A",
            "high":   "#3F3F46",
            "accent_primary":   "#D4AF37",
            "accent_secondary": "#8B7355",
            "accent_tertiary":  "#FFD700"
        },
        "css_classes": {
            "card":    "card",
            "pill":    "pill",
            "stat":    "stat",
            "wrapper": ""
        },
        "kinetic_shapes": False,
        "has_decorative_layer": True,
        "variants": [],
        "variant_energy_threshold": None
    },

    "style-school": {
        "fonts": "'Outfit', 'Gochi Hand', sans-serif",
        "font_import": "Outfit:wght@400;700;900&family=Gochi+Hand&display=swap",
        "colors": {
            "calm":   "#F0F9FF", # Soft Blue
            "medium": "#FEF3C7", # Soft Yellow
            "high":   "#FCE7F3", # Soft Pink
            "accent_primary":   "#0EA5E9",
            "accent_secondary": "#EC4899",
            "accent_tertiary":  "#EAB308"
        },
        "bg_palette": [
            "#1A1F5E", # AI Deep Navy
            "#FF6B35", # AI Orange Pop
            "#12173A", # AI Midnight
            "#ECFDF5", # AI Mint Light
            "#FFFBEB", # AI Cream/Yellow
            "#4C0519", # AI Maroon Intensity
            "#0F172A"  # AI Deep Slate
        ],
        "texture_palette": [
            "variant-lined",
            "variant-grid",
            "variant-dots",
            "variant-notebook"
        ],
        "css_classes": {
            "card":    "card",
            "pill":    "pill",
            "stat":    "stat",
            "wrapper": "school-wrapper"
        },
        "kinetic_shapes": False,
        "has_decorative_layer": True,
        "variants": ["variant-grid", "variant-dots"],
        "variant_energy_threshold": "high"
    },

    "style-business": {
        "fonts": "'Inter', sans-serif",
        "font_import": "Inter:wght@400;600;700;800;900",
        "colors": {
            "calm":   "#FFFFFF",
            "medium": "#F8FAFC",
            "high":   "#E2E8F0",
            "accent_primary":   "#EA580C",
            "accent_secondary": "#1E3A5F",
            "accent_tertiary":  "#1D4ED8"
        },
        "css_classes": {
            "card":    "card",
            "pill":    "pill",
            "stat":    "stat",
            "wrapper": ""
        },
        "kinetic_shapes": True,
        "has_decorative_layer": True,
        "variants": [],
        "variant_energy_threshold": None
    },

    "style-workshop": {
        "fonts": "'Space Grotesk', sans-serif",
        "font_import": "Space+Grotesk:wght@400;600;700;800;900",
        "colors": {
            "calm":   "#FFFBF0",
            "medium": "#FFF8E8",
            "high":   "#FEF3C7",
            "accent_primary":   "#D97706",
            "accent_secondary": "#F59E0B",
            "accent_tertiary":  "#FCD34D"
        },
        "css_classes": {
            "card":         "card",
            "pill":         "pill",
            "activity_box": "activity-box",
            "wrapper":      ""
        },
        "kinetic_shapes": False,
        "has_decorative_layer": True,
        "variants": [],
        "variant_energy_threshold": None
    },

    "style-cyber": {
        "fonts": "'JetBrains Mono', monospace",
        "font_import": "JetBrains+Mono:wght@400;700;800",
        "colors": {
            "calm":   "#000000",
            "medium": "#050505",
            "high":   "#0A0A0A",
            "accent_primary":   "#00FF41",
            "accent_secondary": "#00CC33",
            "accent_tertiary":  "#88FF99"
        },
        "css_classes": {
            "card":    "card",
            "pill":    "pill",
            "stat":    "stat",
            "wrapper": ""
        },
        "kinetic_shapes": True,
        "has_decorative_layer": True,
        "variants": [],
        "variant_energy_threshold": None
    },

    "style-eco": {
        "fonts": "'Lora', serif",
        "font_import": "Lora:ital,wght@0,400;0,700;1,400",
        "colors": {
            "calm":   "#F0FDF4",
            "medium": "#DCFCE7",
            "high":   "#BBF7D0",
            "accent_primary":   "#16A34A",
            "accent_secondary": "#86EFAC",
            "accent_tertiary":  "#4ADE80"
        },
        "css_classes": {
            "card":    "card",
            "pill":    "pill",
            "stat":    "stat",
            "wrapper": ""
        },
        "kinetic_shapes": False,
        "has_decorative_layer": True,
        "variants": [],
        "variant_energy_threshold": None
    },

    "style-space": {
        "fonts": "'Outfit', sans-serif",
        "font_import": "Outfit:wght@300;700;900&family=Space+Mono",
        "colors": {
            "calm":   "#0B0F19",
            "medium": "#0F1629",
            "high":   "#1E1B4B",
            "accent_primary":   "#C084FC",
            "accent_secondary": "#22D3EE",
            "accent_tertiary":  "#D4AF37"
        },
        "css_classes": {
            "card":         "card",
            "pill":         "pill",
            "data_tag":     "data-tag",
            "card_content": "card-content",
            "wrapper":      "content-wrapper"
        },
        "kinetic_shapes": False,
        "has_decorative_layer": True,
        "variants": [],
        "variant_energy_threshold": None
    },

    "style-industrial": {
        "fonts": "'Roboto Mono', monospace",
        "font_import": "Roboto+Mono:wght@400;700&family=Inter:wght@400;900",
        "colors": {
            "calm":   "#1F2937",
            "medium": "#374151",
            "high":   "#4B5563",
            "accent_primary":   "#F59E0B",
            "accent_secondary": "#60A5FA",
            "accent_tertiary":  "#FCD34D"
        },
        "css_classes": {
            "card":        "card",
            "pill":        "pill",
            "stat":        "tech-stat",
            "measurement": "measurement",
            "wrapper":     "content-wrapper"
        },
        "kinetic_shapes": False,
        "has_decorative_layer": True,
        "variants": [],
        "variant_energy_threshold": None
    },

    "style-ai-superpower": {
        "fonts": "'Fredoka', 'Montserrat', sans-serif",
        "font_import": "Fredoka:wght@400;700&family=Montserrat:wght@400;900",
        "colors": {
            "calm":   "#1A1F5E",
            "medium": "linear-gradient(135deg, #1A1F5E 0%, #2D3A8C 100%)",
            "high":   "linear-gradient(135deg, #4c1d95 0%, #1e1b4b 100%)",
            "accent_primary":   "#06D6A0",
            "accent_secondary": "#06D6A0",
            "accent_tertiary":  "#06D6A0"
        },
        "css_classes": {
            "card":    "grid-box",
            "pill":    "pill",
            "stat":    "stat-value",
            "wrapper": ""
        },
        "kinetic_shapes": True,
        "has_decorative_layer": True,
        "variants": [],
        "variant_energy_threshold": None
    },

    "default": {
        "fonts": "'Inter', sans-serif",
        "font_import": "Inter:wght@400;700",
        "colors": {
            "calm":   "#FFFFFF",
            "medium": "#F3F4F6",
            "high":   "#E5E7EB",
            "accent_primary":   "#3B82F6",
            "accent_secondary": "#3B82F6",
            "accent_tertiary":  "#3B82F6"
        },
        "css_classes": {
            "card":    "",
            "pill":    "",
            "stat":    "",
            "wrapper": ""
        },
        "kinetic_shapes": True,
        "has_decorative_layer": False,
        "variants": [],
        "variant_energy_threshold": None
    }
}
