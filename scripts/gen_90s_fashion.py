import sys
import os

# Add scripts directory to path to find slide_engine
sys.path.append(os.path.join(os.getcwd(), 'scripts'))

from slide_engine.schema import SlideContent
from slide_engine.renderer import Pipeline

def generate():
    # Phase C: Using topic analysis to auto-select 'style-editorial'
    engine = Pipeline(topic="90s Fashion Trends", audience="creatives", tone="bold")
    
    slides = [
        # 1. The Hook - Cover
        SlideContent(
            content_type="cover",
            module="EDITORIAL",
            title="90s REBORN",
            subtitle="The Defining Decade of Modern Fashion",
            energy="high",
            bg_video_url="https://assets.mixkit.co/videos/preview/mixkit-fashion-model-posing-for-a-photoshoot-in-a-studio-39873-large.mp4"
        ),
        
        # 2. Bold Quote
        SlideContent(
            content_type="quote",
            title="The Shift",
            module="VISION",
            quote_text="I don't design clothes. I design dreams.",
            quote_author="Ralph Lauren",
            energy="calm"
        ),

        # 3. Media Focus - Grunge
        SlideContent(
            content_type="media_focus",
            module="THE AESTHETIC",
            title="The Grunge Movement",
            description="Anti-fashion became the highest fashion. Born in Seattle, distressed denim, flannel, and combat boots dominated the runways and the streets alike.",
            media_url="https://images.unsplash.com/photo-1542272201-b1ca555f8505?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
            media_type="image",
            energy="standard"
        ),
        
        # 4. Comparison - 80s vs 90s
        SlideContent(
            content_type="comparison",
            module="EVOLUTION",
            title="The Shift to Minimalism",
            items=[
                "👗|80s: Neon & Shoulder Pads", 
                "🖤|90s: Slip Dresses & Neutral Tones"
            ],
            energy="high"
        ),
        
        # 5. Feature Grid - Wardrobe Staples
        SlideContent(
            content_type="feature_grid",
            module="WARDROBE",
            title="Iconic Staples",
            description="The key pieces that defined the 90s silhouette and continue to influence modern wardrobes.",
            items=[
                "🧥|Leather Jackets", 
                "👖|Baggy Denim", 
                "👢|Combat Boots", 
                "📿|Choker Necklaces"
            ],
            energy="standard"
        ),
        
        # 6. Media Focus - Supermodels
        SlideContent(
            content_type="media_focus",
            module="ICONS",
            title="The Supermodel Era",
            description="Naomi, Cindy, Linda, Christy, and Tatjana. The 90s saw the birth of models who were bigger than the brands they walked for.",
            media_url="https://images.unsplash.com/photo-1492446845049-9c50cc313f00?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
            media_type="image",
            energy="calm"
        ),

        # 7. Case Study - Calvin Klein
        SlideContent(
            content_type="case_study",
            module="SPOTLIGHT",
            title="Calvin Klein",
            description="Defining the aesthetic of the 90s with stark, black-and-white campaigns and a controversial focus on 'heroin chic' and raw minimalism.",
            subtitle="The campaign that introduced Kate Moss to the world and changed fashion photography.",
            stat_value="CK",
            stat_label="MINIMALISM",
            emoji="📸",
            energy="standard"
        ),
        
        # 8. Finale
        SlideContent(
            content_type="finale",
            title="Timeless.",
            subtitle="The decade that never truly left.",
            energy="high",
            bg_video_url="https://assets.mixkit.co/videos/preview/mixkit-woman-walking-on-a-catwalk-with-a-fashion-dress-41808-large.mp4"
        )
    ]
    
    md = engine.render(slides)
    with open("presentations/90s_fashion_editorial.md", "w", encoding="utf-8") as f:
        f.write(md)
    with open("slides.md", "w", encoding="utf-8") as f:
        f.write(md)
    print("Successfully generated '90s Fashion' editorial deck and staged to slides.md.")

if __name__ == "__main__":
    generate()
