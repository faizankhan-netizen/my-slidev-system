import sys
import os

# Ensure we can import slide_engine
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from slide_engine.schema import SlideContent
from slide_engine.renderer import Pipeline

def generate_test_script() -> list[SlideContent]:
    script = [
        SlideContent(
            content_type="cover",
            title="AL-ANDALUS V3",
            subtitle="Testing the Cinematic Multi-Element Engine",
            act=1, module="CORE", emoji="🕌"
        ),
        SlideContent(
            content_type="cover",
            title="VIDEO BG TEST",
            subtitle="The background video is reactive to GUI edits.",
            bg_video_url="https://v3.cdnpk.net/videvo_files/video/free/2019-11/large_watermarked/190828_27_SuperTrees_16_preview.mp4",
            act=1, module="VIDEO", energy="high"
        ),
        SlideContent(
            content_type="cycle",
            title="The Andalusian Cycle",
            description="The distinct phases of social and political evolution in Al-Andalus.",
            items=["Conquest (711)", "Emirate (756)", "Caliphate (929)", "Taifas (1031)", "Almoravids (1086)", "Nasrids (1230)"],
            act=1, module="LIFECYCLE", energy="high"
        ),
        SlideContent(
            content_type="chart",
            title="Population Growth",
            description="The rapid urbanization of the Iberian Peninsula under the Caliphate of Cordoba.",
            chart_type="line",
            chart_data=[
                {"name": "750 AD", "value": 4.5},
                {"name": "850 AD", "value": 6.2},
                {"name": "950 AD", "value": 8.8},
                {"name": "1050 AD", "value": 9.5}
            ],
            act=1, module="DEMOGRAPHICS"
        ),
        SlideContent(
            content_type="table",
            title="Urban Superiority",
            description="Comparing the scale of major cities in the 10th Century.",
            table_headers=["City", "Region", "Population", "Library Count"],
            table_rows=[
                ["Cordoba", "Al-Andalus", "500,000+", "70+"],
                ["London", "England", "~20,000", "0"],
                ["Paris", "France", "~30,000", "1"],
                ["Rome", "Italy", "~40,000", "5"]
            ],
            act=1, module="CITIES"
        ),
        SlideContent(
            content_type="media_focus",
            title="Architectural Zenith",
            description="The intricate details of the Alhambra represent the pinnacle of Nasrid craftsmanship and geometric precision.",
            media_url="/alhambra.png",
            media_type="image",
            cta_text="EXPLORE THE PALACE",
            cta_link="https://www.alhambra-patronato.es/",
            act=1, module="VISUALS"
        ),
        SlideContent(
            content_type="finale",
            title="V3 VALIDATED",
            subtitle="Multi-modal engine is now operational.",
            act=1, module="TEST"
        )
    ]
    return script

if __name__ == "__main__":
    print("Generating Al-Andalus V3 Demo...")
    script = generate_test_script()
    pipeline = Pipeline(global_theme="style-luxury")
    output_md = pipeline.render(script)
    
    slides_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "slides.md")
    
    frontmatter = """---
theme: default
background: black
highlighter: shiki
lineNumbers: false
transition: fade
canvasWidth: 900
title: Al-Andalus V3 Test
---

"""
    
    with open(slides_path, "w", encoding="utf-8") as f:
        f.write(frontmatter + output_md)
        
    print("✅ V3 Demo staged to slides.md.")
