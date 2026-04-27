import sys
import os

# Add scripts directory to path to find slide_engine
sys.path.append(os.path.join(os.getcwd(), 'scripts'))

from slide_engine.schema import SlideContent
from slide_engine.renderer import Pipeline

def generate():
    engine = Pipeline(global_theme="style-school")
    
    slides = [
        # 1. The Hook
        SlideContent(
            content_type="cover",
            module="DAILY SUPERPOWER",
            title="Sparkling Clean!",
            subtitle="The Amazing Secret Benefits of Wudu",
            energy="high",
            bg_video_url="https://assets.mixkit.co/videos/preview/mixkit-slow-motion-of-water-splashing-on-a-blue-background-34444-large.mp4"
        ),
        
        # 2. Section Intro
        SlideContent(
            content_type="section_intro",
            module="PART 01",
            title="Our Shield",
            description="How Wudu protects our body from tiny invisible monsters!",
            emoji="🛡️",
            energy="calm"
        ),
        
        # 3. Physical Benefit (Concept)
        SlideContent(
            content_type="concept",
            module="HYGIENE",
            title="Germ-Buster!",
            subtitle="Invisible Cleanliness",
            description="Wudu washes away germs and dust from our skin 5 times a day. It's like having a deep-clean car wash for your body!",
            emoji="🧼",
            energy="standard"
        ),
        
        # 4. The Healthy Flow (Cycle)
        SlideContent(
            content_type="cycle",
            module="THE FLOW",
            title="The Healthy Cycle",
            items=["Fresh Face", "Clean Hands", "Cool Head", "Happy Feet", "Bright Eyes"],
            energy="high"
        ),
        
        # 5. Focus Boost (Data Point)
        SlideContent(
            content_type="data_point",
            module="BRAIN POWER",
            title="Wake Up!",
            stat_value="100%",
            stat_label="Energy Boost",
            description="Cool water on our face tells our brain to wake up and focus! It's nature's energy drink without the sugar.",
            energy="high"
        ),
        
        # 6. The Wise Word (Quote)
        SlideContent(
            content_type="quote",
            title="The Wise Word",
            module="HADITH",
            quote_text="Cleanliness is half of Faith.",
            quote_author="Prophet Muhammad (PBUH)",
            energy="calm"
        ),
        
        # 7. Interactive Moment (Activity)
        SlideContent(
            content_type="activity",
            module="ACTION TIME",
            title="The Wudu Challenge",
            description="Can you name the 4 fard (mandatory) parts of Wudu? Discuss with your partner!",
            emoji="🎯",
            energy="high"
        ),
        
        # 8. Finale
        SlideContent(
            content_type="finale",
            title="Keep Sparkling!",
            subtitle="Wudu today, shine forever.",
            energy="high",
            bg_video_url="https://assets.mixkit.co/videos/preview/mixkit-sparkles-on-a-blue-background-34443-large.mp4"
        )
    ]
    
    md = engine.render(slides)
    with open("presentations/wudu_benefits_v3.md", "w", encoding="utf-8") as f:
        f.write(md)
    with open("slides.md", "w", encoding="utf-8") as f:
        f.write(md)
    print("Successfully generated 'Benefits of Wudu' V3 deck and staged to slides.md.")

if __name__ == "__main__":
    generate()
