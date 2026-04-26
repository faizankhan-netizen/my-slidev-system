import sys
import os

# Ensure we can import slide_engine
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from slide_engine.schema import SlideContent
from slide_engine.renderer import Pipeline

def generate_script() -> list[SlideContent]:
    script = [
        SlideContent(
            content_type="cover",
            title="AL-ANDALUS",
            subtitle="The Golden Age of Islam in Spain (711–1492)",
            act=1, module="HISTORY", emoji="🕌"
        ),
        SlideContent(
            content_type="agenda",
            title="The Andalusian Journey",
            items=["The Conquest (711 AD)", "Convivencia: The Golden Age", "Science, Art & Architecture", "The Reconquista (1492)"],
            act=1, module="ROADMAP"
        ),
        SlideContent(
            content_type="section_intro",
            title="THE CONQUEST",
            description="Crossing the Strait of Gibraltar.",
            act=2, module="711 AD", emoji="⚔️"
        ),
        SlideContent(
            content_type="data_point",
            title="Tariq ibn Ziyad",
            stat_value="711",
            stat_label="Year of the Arrival",
            description="The Umayyad conquest of Hispania begins.",
            act=2, module="ARRIVAL"
        ),
        SlideContent(
            content_type="concept",
            title="Convivencia",
            subtitle="The Era of Coexistence",
            description="A period where Muslims, Christians, and Jews lived together, sparking a renaissance of translation, philosophy, and trade.",
            act=3, module="GOLDEN AGE", emoji="🤝"
        ),
        SlideContent(
            content_type="feature_grid",
            title="Pillars of Progress",
            description="Al-Andalus became the intellectual beacon of Europe.",
            items=["📐|Mathematics", "🔬|Medicine", "🌾|Agriculture", "📚|Philosophy"],
            act=3, module="INNOVATION"
        ),
        SlideContent(
            content_type="section_intro",
            title="ARCHITECTURAL MARVELS",
            description="Symmetry, Water, and Light.",
            act=4, module="DESIGN", emoji="🏛️"
        ),
        SlideContent(
            content_type="comparison",
            title="The Great Monuments",
            items=["Mosque of Cordoba|Red & white horseshoe arches, a symbol of early Umayyad power.", "Alhambra of Granada|Intricate stucco, courtyards, and the peak of Nasrid art."],
            act=4, module="MONUMENTS"
        ),
        SlideContent(
            content_type="quote",
            title="",
            quote_text="Ignorance leads to fear, fear leads to hate, and hate leads to violence. This is the equation.",
            quote_author="Averroes (Ibn Rushd), Andalusian Philosopher",
            act=4, module="WISDOM"
        ),
        SlideContent(
            content_type="section_intro",
            title="THE RECONQUISTA",
            description="The slow decline and the fall of Granada.",
            act=5, module="DECLINE", emoji="🛡️"
        ),
        SlideContent(
            content_type="data_point",
            title="The Fall of Granada",
            stat_value="1492",
            stat_label="End of Al-Andalus",
            description="King Ferdinand and Queen Isabella receive the keys to the city.",
            act=5, module="THE END"
        ),
        SlideContent(
            content_type="finale",
            title="THE LEGACY LIVES ON",
            subtitle="In language, architecture, and the roots of the Renaissance.",
            act=5, module="CONCLUSION"
        )
    ]
    return script

if __name__ == "__main__":
    print("Generating Al-Andalus Semantic Script...")
    script = generate_script()
    pipeline = Pipeline(global_theme="style-luxury")
    output_md = pipeline.render(script)
    
    out_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "presentations", "islam_in_spain.md")
    slides_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "slides.md")
    
    frontmatter = """---
theme: default
background: black
highlighter: shiki
lineNumbers: false
transition: fade
canvasWidth: 900
title: Al-Andalus - Islam in Spain
---

"""
    
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(frontmatter + output_md)
        
    with open(slides_path, "w", encoding="utf-8") as f:
        f.write(frontmatter + output_md)
        
    print("✅ Staged to slides.md.")
