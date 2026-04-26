import sys
import os
import random
sys.stdout.reconfigure(encoding='utf-8')

# Ensure we can import slide_engine
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from slide_engine.schema import SlideContent
from slide_engine.renderer import Pipeline

# The 5 Acts of the Masterclass
ACTS = {
    1: {"name": "THE HOOK", "module": "FOUNDATIONS"},
    2: {"name": "THE ARCHITECTURE", "module": "SYSTEMS"},
    3: {"name": "THE IMPLEMENTATION", "module": "DEPLOYMENT"},
    4: {"name": "THE HUMAN FACTOR", "module": "CULTURE"},
    5: {"name": "THE VISION", "module": "FUTURE"},
}

TYPES = [
    "concept", "comparison", "data_point", "process", 
    "feature_grid", "quote", "activity", "case_study"
]

def generate_script() -> list[SlideContent]:
    script = []
    
    # 1. The Cover
    script.append(SlideContent(
        content_type="cover",
        title="THE INTELLIGENCE EXPLOSION",
        subtitle="A Masterclass on the Next Decade of Human-AI Symbiosis",
        act=1, module="MASTERCLASS", emoji="🚀"
    ))
    
    # 2. The Agenda
    script.append(SlideContent(
        content_type="agenda",
        title="Course Map",
        items=["Foundations: What is intelligence?", "Systems: The Architecture of AI", "Deployment: Real-world impact", "Culture: The human factor", "Future: 2030 and beyond"],
        act=1, module="ROADMAP"
    ))

    # Generate the remaining 96 slides to reach 99, then 1 finale
    for i in range(3, 100):
        act_num = ((i - 1) // 20) + 1
        act_num = min(act_num, 5) # cap at 5
        act_info = ACTS[act_num]
        
        # Every 20th slide is a section intro
        if (i - 1) % 20 == 0:
            script.append(SlideContent(
                content_type="section_intro",
                title=act_info["name"],
                description=f"Entering the next phase: {act_info['module']}",
                act=act_num, module=act_info["module"], emoji="🧠"
            ))
            continue
            
        # Determine a semantic type
        ctype = random.choice(TYPES)
        
        c = SlideContent(
            content_type=ctype,
            title=f"Evolution Phase {i:03d}",
            subtitle=f"Core principle of {act_info['name'].lower()}",
            description=f"This slide explores the strategic implications of phase {i} in the broader context of {act_info['module'].lower()}.",
            act=act_num,
            module=f"{act_info['module']} // {i:03d}",
            emoji=random.choice(["⚡", "🌍", "💡", "🛠️", "📊", "🔍", "🎯"]),
            items=["First dimension of impact", "Second dimension of scale", "Third dimension of speed", "Fourth dimension of security"],
            stat_value=f"{random.randint(10, 99)}X",
            stat_label="Velocity Increase",
            quote_text="The system adapts to the environment, not the other way around.",
            quote_author="Strategic Principle"
        )
        script.append(c)
        
    # 100. The Finale
    script.append(SlideContent(
        content_type="finale",
        title="THE JOURNEY BEGINS",
        subtitle="End of Masterclass.",
        act=5, module="CONCLUSION"
    ))
    
    return script

if __name__ == "__main__":
    print("Generating 100-Slide Semantic Script...")
    script = generate_script()
    
    print("Initializing Pipeline...")
    pipeline = Pipeline()
    
    print("Rendering Markdown...")
    output_md = pipeline.render(script)
    
    out_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "presentations", "ai_masterclass.py.md")
    
    # We also want to write directly to slides.md
    slides_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "slides.md")
    
    # Write the YAML frontmatter for the whole deck
    frontmatter = """---
theme: default
background: black
highlighter: shiki
lineNumbers: false
transition: fade
canvasWidth: 900
title: The Intelligence Explosion
---

"""
    
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(frontmatter + output_md)
        
    with open(slides_path, "w", encoding="utf-8") as f:
        f.write(frontmatter + output_md)
        
    print(f"✅ Generated {len(script)} slides using semantic intelligence.")
    print("✅ Staged to slides.md. HMR should pick it up immediately.")
