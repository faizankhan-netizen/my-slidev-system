import os
import sys

# Ensure Python can find the slide_engine module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from slide_engine.schema import SlideContent
from slide_engine.renderer import Pipeline

# ==============================================================================
# PRESENTATION: Cloud Computing for 5th Graders
# ARCHETYPE: style-school (Neon Cosmos, Friendly Typography)
# ==============================================================================

slides = [
    # SLIDE 1: Cover
    SlideContent(
        content_type="cover",
        module="INTRO",
        title="The Magic Cloud ☁️",
        description="Where do all your games, photos, and videos actually live? Let's find out!",
        energy="high"
    ),
    
    # SLIDE 2: The Big Secret
    SlideContent(
        content_type="concept",
        module="THE SECRET",
        title="It's Not Actually in the Sky!",
        description="When we say 'The Cloud', we aren't talking about rain clouds. The Cloud is actually just a bunch of really powerful computers sitting in giant warehouses on Earth.",
        energy="medium"
    ),
    
    # SLIDE 3: Comparison - Backpack vs Cloud
    SlideContent(
        content_type="comparison",
        module="HOW IT HELPS",
        title="Your Backpack vs. The Cloud",
        description="Why do we need the Cloud? Imagine trying to carry every book in the world.",
        items=[
            "Your Backpack (Computer) | Can only hold a few books. Gets heavy and full quickly.",
            "The Cloud (Internet) | A giant magical library. You don't have to carry anything, just borrow it when you need it!"
        ],
        energy="high"
    ),
    
    # SLIDE 4: Cycle of the Cloud
    SlideContent(
        content_type="cycle",
        module="HOW IT WORKS",
        title="The Cloud Cycle",
        description="How does a video get to your iPad?",
        items=[
            "1. You click 'Play'", 
            "2. Signal flies to space!", 
            "3. Lands in the Cloud", 
            "4. Cloud finds the video", 
            "5. Beams it back to you"
        ],
        energy="calm"
    ),
    
    # SLIDE 5: Data Point
    SlideContent(
        content_type="case_study",
        module="FUN FACT",
        title="Giant Data Centers",
        description="These warehouses are called Data Centers. They are so big that people ride scooters inside them!",
        subtitle="Size of the Cloud",
        stat_value="10,000+",
        stat_label="Servers in one building",
        emoji="🏢",
        energy="high"
    ),
    
    # SLIDE 6: Activity Break
    SlideContent(
        content_type="activity",
        module="BRAIN BREAK",
        title="Rent-a-Supercomputer",
        description="If you could rent a supercomputer for 1 hour, what game would you play or what world would you build?",
        emoji="🎮",
        energy="medium"
    ),
    
    # SLIDE 7: Media Focus
    SlideContent(
        content_type="media_focus",
        module="INSIDE LOOK",
        title="Inside a Data Center",
        description="This is what the 'Cloud' actually looks like. Thousands of blinking lights and giant cooling fans!",
        media_url="https://www.youtube.com/watch?v=XZmGGAbHqa0", # Google Data Center 360
        cta_text="Look around!",
        cta_link="#",
        energy="calm"
    ),
    
    # SLIDE 8: Finale
    SlideContent(
        content_type="finale",
        module="CONCLUSION",
        title="You Are A Cloud Master! ⚡",
        subtitle="Next time you watch YouTube, remember the giant warehouses doing all the hard work.",
        energy="high"
    )
]

def generate():
    print("Generating Cloud Computing Presentation...")
    engine = Pipeline(global_theme="style-school")
    
    # Using the School Archetype for the neon cosmos / 5th grade friendly vibe
    md = engine.render(slides)
    
    # Write to slides.md (Slidev will auto-reload)
    out_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "slides.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(md)
    print("Successfully generated Cloud Computing deck!")

if __name__ == "__main__":
    generate()
