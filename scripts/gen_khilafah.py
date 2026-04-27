import sys
import os

# Add scripts directory to path to find slide_engine
sys.path.append(os.path.join(os.getcwd(), 'scripts'))

from slide_engine.schema import SlideContent
from slide_engine.renderer import Pipeline

def generate():
    # Phase C: Let the engine auto-resolve the archetype based on topic
    # We use a broad topic description to provide more signals
    engine = Pipeline(
        topic="A Journey Through History: The Khilafah", 
        audience="students", 
        tone="playful"
    )
    
    slides = [
        # 1. The Hook - Cover
        SlideContent(
            content_type="cover",
            module="HISTORY",
            title="THE KHILAFAH",
            subtitle="A History Adventure for Young Explorers",
            energy="high"
        ),
        
        # 2. Quote - Core Principle
        SlideContent(
            content_type="quote",
            title="Divine Mandate",
            module="CORE VALUES",
            quote_text="The best of your leaders are those whom you love and who love you, who pray for you and you pray for them.",
            quote_author="Prophet Muhammad (ﷺ)",
            energy="calm"
        ),

        # 3. Media Focus - Expansion
        SlideContent(
            content_type="media_focus",
            module="ERA OF LIGHT",
            title="The Rashidun Caliphate",
            description="The 'Rightly Guided' era established the foundations of Shura (consultation) and absolute justice, spanning from the Arabian Peninsula to the Levant and beyond.",
            media_url="https://images.unsplash.com/photo-1542640244-7e672d6cef21?auto=format&fit=crop&w=1200&q=80",
            media_type="image",
            energy="standard"
        ),
        
        # 4. Process - Eras of Governance
        SlideContent(
            content_type="process",
            module="HISTORICAL TIMELINE",
            title="The Great Dynasties",
            items=[
                "Umayyad Era|Establishment of statehood and administration across three continents.",
                "Abbasid Golden Age|The zenith of science, culture, and theology in Baghdad.",
                "Ottoman Legacy|The final great Khilafah, bridging East and West for centuries."
            ],
            energy="high"
        ),
        
        # 5. Concept - Principles
        SlideContent(
            content_type="concept",
            module="GOVERNANCE",
            title="The Pillars of the State",
            description="Unlike secular models, the Khilafah is built upon the dual responsibility to the Creator and the creation.",
            subtitle="Justice, Shura, and Accountability",
            emoji="⚖️",
            energy="standard"
        ),
        
        # 6. Data Point - Impact
        SlideContent(
            content_type="data_point",
            module="GLOBAL REACH",
            title="A Lasting Impact",
            stat_value="1300",
            stat_label="YEARS OF CONTINUITY",
            description="From the 7th century until the early 20th, the model of the Khilafah remained the central political identity of the Muslim world.",
            energy="high"
        ),

        # 7. Comparison - Justice
        SlideContent(
            content_type="comparison",
            module="LEGAL SYSTEM",
            title="Justice for All",
            items=[
                "⚖️|Equity: Protection of rights for Muslims and non-Muslims alike.",
                "📜|Accountability: The Caliph is subject to the same law as the citizens."
            ],
            energy="calm"
        ),
        
        # 8. Finale
        SlideContent(
            content_type="finale",
            title="A Legacy Unfolding.",
            subtitle="Revisiting the history to inspire the future.",
            energy="high"
        )
    ]
    
    md = engine.render(slides)
    
    output_path = "presentations/khilafah_legacy.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md)
        
    # Stage to slides.md for preview
    with open("slides.md", "w", encoding="utf-8") as f:
        f.write(md)
        
    print(f"Successfully generated deck on 'The Khilafah' and staged to slides.md.")
    print(f"Resolved Archetype: {engine.conductor.global_theme}")

if __name__ == "__main__":
    generate()
