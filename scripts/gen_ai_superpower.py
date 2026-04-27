import sys
import os

sys.path.append(os.path.join(os.getcwd(), 'scripts'))

from slide_engine.schema import SlideContent
from slide_engine.renderer import Pipeline

def generate():
    engine = Pipeline(global_theme="style-ai-superpower")
    
    slides = [
        # --- OPENER: THE HOOK ---
        SlideContent(
            content_type="cover",
            title="AI SUPERPOWER",
            subtitle="The Paintbrush for your Imagination",
            module="ACTIVATE!",
            energy="high",
            custom_bg="#1A1F5E", # Audited Hex
            bg_video_url="https://assets.mixkit.co/videos/preview/mixkit-digital-network-of-moving-points-and-lines-41315-large.mp4"
        ),
        
        # --- MODULE 1: THE MAGIC (ORANGE POP) ---
        SlideContent(
            content_type="section_intro",
            title="Module 01: The Magic",
            description="How do machines actually 'grow a brain'?",
            emoji="🪄",
            module="THE START",
            energy="high",
            custom_bg="#FF6B35" # Audited Orange Pop
        ),
        SlideContent(
            content_type="concept",
            title="What is an Algorithm?",
            description="No computers needed. An algorithm is just a recipe. Think of it as a set of instructions for a robot with NO common sense.",
            subtitle="The Recipe Analogy",
            emoji="🍳",
            energy="calm",
            custom_bg="#12173A" # Audited Dark Blue
        ),
        SlideContent(
            content_type="activity",
            title="The Puppy Game",
            description="Reinforcement Learning in Action! One student is the Puppy. The class is the Training Data.",
            emoji="🐕",
            module="INTERACTIVE",
            energy="high",
            custom_bg="#12173A"
        ),

        # --- MODULE 2: AI AROUND YOU (MINT LIGHT RESET) ---
        SlideContent(
            content_type="section_intro",
            title="Module 02: AI Around You",
            description="Not in Silicon Valley. In your gaon, gali, aur ghar.",
            emoji="🇮🇳",
            module="LOCAL IMPACT",
            energy="standard",
            custom_bg="#ECFDF5", # Audited Mint Light
            custom_text="dark"  # Trigger inversion
        ),
        SlideContent(
            content_type="case_study",
            title="01: Kheti (Agriculture)",
            description="AI saves the crop before you can see the disease. Satellites scan the farm and send a WhatsApp alert.",
            subtitle="10-Day Early Warning",
            stat_value="10 Days",
            stat_label="Early Warning",
            emoji="🌾",
            energy="standard",
            custom_bg="#FFFBEB", # Audited Cream/Yellow
            custom_text="dark"
        ),
        SlideContent(
            content_type="media_focus",
            title="02: Bollywood Magic",
            description="The naale ki ladaai in RRR—98% of the waterfall battle was AI-composited VFX.",
            media_url="https://www.youtube.com/watch?v=VIs_L3D6qgE",
            media_type="video",
            module="CINEMA",
            energy="high",
            custom_bg="#1A1F5E"
        ),
        SlideContent(
            content_type="data_point",
            title="03: Health AI (Village Care)",
            description="Wadhwani AI detects Tuberculosis from a simple cough recording. Screening an entire village in one morning.",
            stat_value="3 Years",
            stat_label="Earlier Detection",
            module="SAVING LIVES",
            energy="high",
            custom_bg="#0F172A" # Audited Deep Navy
        ),

        # --- MODULE 3: YOU ARE THE ALGORITHM (MAROON INTENSITY) ---
        SlideContent(
            content_type="section_intro",
            title="Module 03: You are the AI",
            description="No computers. Just your brain.",
            emoji="🧠",
            energy="high",
            custom_bg="#4C0519" # Audited Maroon Intensity
        ),
        SlideContent(
            content_type="process",
            title="Program Your Robot",
            description="Mission: Make your teammate draw a house. But you can't use the words 'draw' or 'house'.",
            items=["Round 1: Write Instructions", "Round 2: Fix the Chaos", "Round 3: Iteration"],
            energy="high",
            custom_bg="#12173A"
        ),

        # --- THE GRAND FINALE ---
        SlideContent(
            content_type="finale",
            title="Superpower: ACTIVATED.",
            subtitle="The ideas were yours. AI was just the paintbrush.",
            energy="high",
            custom_bg="#1A1F5E",
            bg_video_url="https://assets.mixkit.co/videos/preview/mixkit-futuristic-technology-background-with-lines-and-dots-34445-large.mp4"
        )
    ]
    
    md = engine.render(slides)
    with open("presentations/ai_superpower_replica.md", "w", encoding="utf-8") as f:
        f.write(md)
    with open("slides.md", "w", encoding="utf-8") as f:
        f.write(md)
    print("Successfully generated Exact Replica AI Superpower deck.")

if __name__ == "__main__":
    generate()
