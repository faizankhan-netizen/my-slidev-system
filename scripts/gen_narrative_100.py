"""
gen_narrative_100.py — The 100-Slide AI Narrative Masterpiece
Focuses on meaningful flow, logical transitions, and presentation mechanism.
"""

import os

FRONTMATTER = """\
---
title: "THE INTELLIGENCE EXPLOSION"
transition: fade-out
canvasWidth: 900
highlighter: shiki
---
"""

GLOBAL_STYLE = ""

# The Sequential Narrative Script
NARRATIVE = [
    # --- ACT 1: THE HOOK (1-15) ---
    {"t": "The Intelligence Explosion", "d": "We are witnessing the most significant transition in human history.", "p": "MOMENT ZERO", "a": "style-space", "l": "center"},
    {"t": "Everything is Changing", "d": "From how we code to how we dream.", "p": "THE SHIFT", "a": "style-space", "l": "default"},
    {"t": "The 70-Year Wait", "d": "AI isn't new. But the 'Unlock' is.", "p": "HISTORY", "a": "style-school", "l": "default"},
    {"t": "Moores Law vs Scaling Laws", "d": "Hardware was the floor. Intelligence is the ceiling.", "p": "GROWTH", "a": "style-school", "l": "default"},
    {"t": "The First Billion Tokens", "d": "The day the internet became training data.", "p": "DATA", "a": "style-cyber", "l": "default"},
    {"t": "Emergent Properties", "d": "Models began to reason in ways we didn't program.", "p": "MYSTERY", "a": "style-cyber", "l": "default"},
    {"t": "The Turing Illusion", "d": "Is it thinking? Or just predicting?", "p": "PHILOSOPHY", "a": "style-cyber", "l": "default"},
    {"t": "The New Literacy", "d": "If you can't speak to the machine, you are behind.", "p": "SKILLS", "a": "style-school", "l": "default"},
    {"t": "The End of Search", "d": "Why find links when you can find answers?", "p": "UTILITY", "a": "style-business", "l": "default"},
    {"t": "The Rise of Answers", "d": "The fundamental shift from 'Search' to 'Generate'.", "p": "UTILITY", "a": "style-business", "l": "default"},
    {"t": "Economic Velocity", "d": "Intelligence is becoming too cheap to meter.", "p": "ROI", "a": "style-business", "l": "default"},
    {"t": "Market Disruption", "d": "Incumbents are vulnerable. The agile are winning.", "p": "ROI", "a": "style-business", "l": "default"},
    {"t": "Global AI GDP", "d": "A 15.7 Trillion dollar opportunity by 2030.", "p": "NUMBERS", "a": "style-business", "l": "fact"},
    {"t": "The AI Arms Race", "d": "Nations are investing billions to secure sovereignty.", "p": "GEOPOLITICS", "a": "style-industrial", "l": "default"},
    {"t": "Transitioning to Tech", "d": "Now, let's look under the hood.", "p": "ACT 2", "a": "style-cyber", "l": "center"},

    # --- ACT 2: ARCHITECTURE (16-40) ---
    {"t": "The Transformer", "d": "The architecture that changed everything.", "p": "ENGINE", "a": "style-cyber", "l": "default"},
    {"t": "Attention Mechanisms", "d": "Focusing on what matters in a sea of data.", "p": "LOGIC", "a": "style-cyber", "l": "default"},
    {"t": "Hidden Layers", "d": "Where the 'magic' happens inside the network.", "p": "LOGIC", "a": "style-cyber", "l": "default"},
    {"t": "Tokenization", "d": "Breaking the world into digestible pieces.", "p": "DATA", "a": "style-cyber", "l": "default"},
    {"t": "Latent Space", "d": "A universe of meaning beyond human vision.", "p": "DATA", "a": "style-cyber", "l": "default"},
    {"t": "Embeddings", "d": "Turning concepts into coordinates.", "p": "MATH", "a": "style-cyber", "l": "default"},
    {"t": "Cross-Attention", "d": "How vision meets language.", "p": "MATH", "a": "style-cyber", "l": "default"},
    {"t": "Diffusers", "d": "Creating art from static and noise.", "p": "CREATIVE", "a": "style-school", "l": "default"},
    {"t": "The Denoiser", "d": "The mechanism of visual creation.", "p": "CREATIVE", "a": "style-school", "l": "default"},
    {"t": "RLHF", "d": "Teaching the machine to be human-friendly.", "p": "ALIGNMENT", "a": "style-school", "l": "default"},
    {"t": "Reward Modeling", "d": "The carrot and the stick for silicon brains.", "p": "ALIGNMENT", "a": "style-school", "l": "default"},
    {"t": "Prompt Engineering", "d": "The art of the perfect instruction.", "p": "INTERFACE", "a": "style-school", "l": "default"},
    {"t": "Context Windows", "d": "The 'RAM' of our new digital assistants.", "p": "SPECS", "a": "style-cyber", "l": "default"},
    {"t": "Long-Term Memory", "d": "Solving the 'Forgetting' problem with RAG.", "p": "SPECS", "a": "style-cyber", "l": "default"},
    {"t": "Vector Retrieval", "d": "Instantly finding the needle in a 100-ton haystack.", "p": "MECHANISM", "a": "style-cyber", "l": "default"},
    {"t": "Agentic Loops", "d": "Moving from 'Chat' to 'Doing'.", "p": "EVOLUTION", "a": "style-cyber", "l": "default"},
    {"t": "The Action Layer", "d": "How AI uses browsers, APIs, and terminals.", "p": "EVOLUTION", "a": "style-cyber", "l": "default"},
    {"t": "Self-Correction", "d": "The machine that fixes its own mistakes.", "p": "EVOLUTION", "a": "style-cyber", "l": "default"},
    {"t": "Multi-Agent Swarms", "d": "Coordination at the speed of light.", "p": "EVOLUTION", "a": "style-cyber", "l": "default"},
    {"t": "Fine-Tuning", "d": "Building your own specialized intelligence.", "p": "CUSTOM", "a": "style-business", "l": "default"},
    {"t": "LoRA & Adapters", "d": "Personalizing models without the billion-dollar price tag.", "p": "CUSTOM", "a": "style-business", "l": "default"},
    {"t": "The Knowledge Silo", "d": "Bridging corporate data with global intelligence.", "p": "CUSTOM", "a": "style-business", "l": "default"},
    {"t": "Security in Training", "d": "Protecting your IP from the model.", "p": "SECURITY", "a": "style-business", "l": "default"},
    {"t": "The Data Moat", "d": "Proprietary data is the only real advantage.", "p": "STRATEGY", "a": "style-business", "l": "default"},
    {"t": "Architecture Summary", "d": "From neurons to agents. Ready for implementation?", "p": "ACT 3", "a": "style-industrial", "l": "center"},

    # --- ACT 3: IMPLEMENTATION (41-65) ---
    {"t": "AI in Healthcare", "d": "Curing diseases before they symptoms show.", "p": "BIO", "a": "style-eco", "l": "default"},
    {"t": "Drug Discovery", "d": "Simulating years of lab work in hours.", "p": "BIO", "a": "style-eco", "l": "default"},
    {"t": "Personalized Medicine", "d": "A doctor in your pocket, personalized to your DNA.", "p": "BIO", "a": "style-eco", "l": "default"},
    {"t": "Diagnostics", "d": "X-rays read with 99.9% accuracy.", "p": "BIO", "a": "style-eco", "l": "default"},
    {"t": "FinTech Revolution", "d": "High-frequency decision making without bias.", "p": "FINANCE", "a": "style-business", "l": "default"},
    {"t": "Fraud Detection", "d": "Stopping theft before the card is swiped.", "p": "FINANCE", "a": "style-business", "l": "default"},
    {"t": "Algorithmic Trading", "d": "When markets talk to markets.", "p": "FINANCE", "a": "style-business", "l": "default"},
    {"t": "Retail Hyper-Personalization", "d": "Stores that know what you want before you do.", "p": "COMMERCE", "a": "style-business", "l": "default"},
    {"t": "Supply Chain AI", "d": "Predictive logistics for a chaotic world.", "p": "LOGISTICS", "a": "style-industrial", "l": "default"},
    {"t": "Warehouse Robotics", "d": "The physical arm of digital intelligence.", "p": "LOGISTICS", "a": "style-industrial", "l": "default"},
    {"t": "The Smart Grid", "d": "Managing energy at a planetary scale.", "p": "ENERGY", "a": "style-eco", "l": "default"},
    {"t": "Climate Modeling", "d": "Finding the path to net-zero with AI.", "p": "ENERGY", "a": "style-eco", "l": "default"},
    {"t": "Manufacturing 5.0", "d": "Factories that design their own parts.", "p": "INFRA", "a": "style-industrial", "l": "default"},
    {"t": "Predictive Maintenance", "d": "Fixing the bridge before it cracks.", "p": "INFRA", "a": "style-industrial", "l": "default"},
    {"t": "Legal-Tech", "d": "Reviewing 10,000 contracts in 6 seconds.", "p": "LAW", "a": "style-business", "l": "default"},
    {"t": "Creative-Tech", "d": "Hollywood in a bedroom.", "p": "ART", "a": "style-school", "l": "default"},
    {"t": "Music Generation", "d": "The symphonies of the future are mathematical.", "p": "ART", "a": "style-school", "l": "default"},
    {"t": "Gaming & Worlds", "d": "NPCs that remember your name and your past.", "p": "GAMING", "a": "style-school", "l": "default"},
    {"t": "EdTech", "d": "Education adapted to the speed of the learner.", "p": "LEARN", "a": "style-school", "l": "default"},
    {"t": "The Tutor AI", "d": "Every child has a personalized mentor.", "p": "LEARN", "a": "style-school", "l": "default"},
    {"t": "Space Exploration", "d": "Navigating the stars with silicon captains.", "p": "SPACE", "a": "style-space", "l": "default"},
    {"t": "Materials Science", "d": "Inventing new metals for the next century.", "p": "SCIENCE", "a": "style-industrial", "l": "default"},
    {"t": "The Lab AI", "d": "Automating the scientific method.", "p": "SCIENCE", "a": "style-industrial", "l": "default"},
    {"t": "Public Service", "d": "Cities that work for the citizens.", "p": "GOV", "a": "style-eco", "l": "default"},
    {"t": "Impact Summary", "d": "Everything is being rewritten. But what about us?", "p": "ACT 4", "a": "style-luxury", "l": "center"},

    # --- ACT 4: THE HUMAN FACTOR (66-85) ---
    {"t": "The Centaur Workflow", "d": "Human intuition + AI speed.", "p": "HYBRID", "a": "style-school", "l": "default"},
    {"t": "Augmentation Not Replacement", "d": "The tools don't work without the pilot.", "p": "HYBRID", "a": "style-school", "l": "default"},
    {"t": "The Skill Floor", "d": "Average is over. Greatness is accessible.", "p": "PEOPLE", "a": "style-school", "l": "default"},
    {"t": "Job Displacement", "d": "The painful transition of the labor market.", "p": "PEOPLE", "a": "style-eco", "l": "default"},
    {"t": "New Occupations", "d": "Jobs that didn't exist 24 months ago.", "p": "PEOPLE", "a": "style-eco", "l": "default"},
    {"t": "Creative Sovereignty", "d": "Anyone can be a creator.", "p": "PEOPLE", "a": "style-school", "l": "default"},
    {"t": "Psychology of AI", "d": "Why we personify the machine.", "p": "MIND", "a": "style-eco", "l": "default"},
    {"t": "The Empathy Gap", "d": "What a model can never feel.", "p": "MIND", "a": "style-eco", "l": "default"},
    {"t": "Educational Reform", "d": "Stop testing memory. Start testing thinking.", "p": "LEARN", "a": "style-school", "l": "default"},
    {"t": "Critical Thinking", "d": "The most valuable skill in an automated world.", "p": "LEARN", "a": "style-school", "l": "default"},
    {"t": "Ethics of Truth", "d": "Deepfakes and the end of 'Seeing is Believing'.", "p": "ETHICS", "a": "style-eco", "l": "default"},
    {"t": "Data Privacy", "d": "Who owns your digital shadow?", "p": "ETHICS", "a": "style-eco", "l": "default"},
    {"t": "Bias in the Brain", "d": "Models inherit our prejudices. How to fix them?", "p": "ETHICS", "a": "style-eco", "l": "default"},
    {"t": "Hallucinations", "d": "The high cost of confident lies.", "p": "RISK", "a": "style-cyber", "l": "default"},
    {"t": "The Black Box", "d": "Can we ever truly trust what we don't understand?", "p": "RISK", "a": "style-cyber", "l": "default"},
    {"t": "Model Collapse", "d": "When AI trains on AI, the quality dies.", "p": "RISK", "a": "style-cyber", "l": "default"},
    {"t": "Compute Scarcity", "d": "The geopolitical war for GPUs.", "p": "RISK", "a": "style-industrial", "l": "default"},
    {"t": "The Power Draw", "d": "The carbon cost of a single prompt.", "p": "RISK", "a": "style-eco", "l": "default"},
    {"t": "Regulation Wars", "d": "The EU vs The US vs The East.", "p": "RISK", "a": "style-business", "l": "default"},
    {"t": "Human Factor Summary", "d": "The tools are ready. Are you?", "p": "ACT 5", "a": "style-space", "l": "center"},

    # --- ACT 5: THE FUTURE VISION (86-100) ---
    {"t": "2025: The Agentic Year", "d": "When your calendar starts taking meetings.", "p": "TIMELINE", "a": "style-luxury", "l": "default"},
    {"t": "2026: Multimodal Default", "d": "Voice, vision, and text as a single sense.", "p": "TIMELINE", "a": "style-luxury", "l": "default"},
    {"t": "2027: The Energy Pivot", "d": "AI-optimized fusion and fission.", "p": "TIMELINE", "a": "style-eco", "l": "default"},
    {"t": "2028: Embodied AI", "d": "The model gets a body.", "p": "TIMELINE", "a": "style-industrial", "l": "default"},
    {"t": "2029: AGI Horizon", "d": "Matching human level across all tasks.", "p": "TIMELINE", "a": "style-space", "l": "default"},
    {"t": "The Singularity?", "d": "Beyond human comprehension.", "p": "VISION", "a": "style-space", "l": "center"},
    {"t": "The Post-Labor Society", "d": "What do we do when we don't 'have' to work?", "p": "VISION", "a": "style-eco", "l": "default"},
    {"t": "Silicon Life", "d": "The second branch of the evolutionary tree.", "p": "VISION", "a": "style-space", "l": "default"},
    {"t": "Planetary Intelligence", "d": "A connected global brain.", "p": "VISION", "a": "style-space", "l": "default"},
    {"t": "The Final Challenge", "d": "Keeping humanity at the center.", "p": "VISION", "a": "style-luxury", "l": "default"},
    {"t": "Conclusion", "d": "It's time to build.", "p": "END", "a": "style-luxury", "l": "center"},
    {"t": "Thank You", "d": "Questions? Ideas? Let's connect.", "p": "CONTACT", "a": "style-luxury", "l": "default"},
    {"t": "Credits", "d": "Built with Slidev Cinematic Engine.", "p": "INFO", "a": "style-luxury", "l": "default"},
    {"t": "Resources", "d": "Links to research papers and datasets.", "p": "INFO", "a": "style-luxury", "l": "default"},
    {"t": "Fin.", "d": "The intelligence explosion is just beginning.", "p": "FIN", "a": "style-space", "l": "center"}
]

def generate_slide(idx, item):
    num = idx + 1
    # Global Style Tokens
    wrapper_style = "position:relative; z-index:10; height:100%; display:flex; flex-direction:column; padding: 2.5rem 3.5rem; overflow: hidden;"
    pill_style = "display:inline-block; width: fit-content; padding:4px 12px; border-radius:30px; font-size:9px; font-weight:900; letter-spacing:2px; text-transform:uppercase; margin-bottom: 0.8rem; border: 1px solid rgba(255,255,255,0.2); white-space: nowrap; background: rgba(255,255,255,0.1);"
    h1_style = "font-size: 2.8rem; font-weight: 900; line-height: 1.1; letter-spacing: -1.2px; margin-bottom: 0.5rem; width: 100%; word-wrap: break-word; text-transform: uppercase;"
    desc_style = "font-size: 1rem; line-height: 1.4; max-width: 100%; opacity: 0.7; margin-bottom: 1rem;"
    grid_box_style = "background: rgba(255,255,255,0.07); padding: 1rem; border-radius: 10px; border: 1px solid rgba(255,255,255,0.1); width: 100%;"

    # Layout Mechanism Logic
    pattern = (idx // 2) % 4  # Change layout every 2 slides
    
    if item['l'] == 'center':
        return f"""
---
layout: center
class: {item['a']}
---
<div style="{wrapper_style} align-items: center; text-center: center; justify-content: center; padding: 4rem;">
  <div v-motion :initial="{{opacity:0, y:20}}" :enter="{{opacity:1, y:0}}" style="{pill_style}">{item['p']}</div>
  <h1 v-motion :initial="{{opacity:0, scale:0.9}}" :enter="{{opacity:1, scale:1}}" style="{h1_style} text-align: center; font-size: 3.5rem; margin-top: 1rem;">{item['t']}</h1>
  <p style="{desc_style} text-align: center; max-width: 80%; margin-left: auto; margin-right: auto; font-size: 1.2rem;">{item['d']}</p>
</div>
"""
    elif item['l'] == 'fact':
        return f"""
---
layout: default
class: {item['a']}
---
<div style="{wrapper_style} align-items: center; justify-content: center; text-align: center;">
  <div style="{pill_style}">{item['p']}</div>
  <div v-motion :initial="{{opacity:0, y:50}}" :enter="{{opacity:1, y:0}}" style="font-size: 8rem; font-weight: 900; color: orange; line-height: 1; filter: drop-shadow(0 0 20px rgba(255,165,0,0.3));">15.7T</div>
  <div style="font-size: 2.2rem; font-weight: 900; text-transform: uppercase; letter-spacing: 2px; margin-top: 1rem;">{item['t']}</div>
  <div style="{desc_style} margin-top: 1rem; margin-left: auto; margin-right: auto;">{item['d']}</div>
</div>
"""
    
    # Narrative Layout Patterns
    if pattern == 0: # Standard (Grid Bottom)
        return f"""
---
layout: default
class: {item['a']}
---
<div style="{wrapper_style}">
  <div style="{pill_style}">{item['p']} · {num:03}</div>
  <div style="font-size: 1rem; font-weight: 400; opacity: 0.5; margin-bottom: 0.2rem;">PART { (idx // 20) + 1 }</div>
  <h1 style="{h1_style}">{item['t']}</h1>
  <div style="{desc_style}">{item['d']}</div>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.2rem; width: 100%; margin-top: 0.5rem;">
     <div v-click style="{grid_box_style}">
        <div style="font-size: 0.9rem; font-weight: 800; margin-bottom: 0.4rem; color: #6366f1;">Primary Impact</div>
        <div style="font-size: 0.8rem; opacity: 0.6;">Reshaping {item['t'].lower()} workflows with integrated intelligence.</div>
     </div>
     <div v-click style="{grid_box_style}">
        <div style="font-size: 0.9rem; font-weight: 800; margin-bottom: 0.4rem; color: #10b981;">Key Metric</div>
        <div style="font-size: 0.8rem; opacity: 0.6;">Achieving 10x velocity increase through architectural shift.</div>
     </div>
  </div>
</div>
"""
    elif pattern == 1: # Vertical Split (Focus Highlight)
        return f"""
---
layout: default
class: {item['a']}
---
<div style="{wrapper_style}">
  <div style="display: flex; width: 100%; height: 100%; gap: 3rem;">
    <div style="flex: 1.2; display: flex; flex-direction: column;">
      <div style="{pill_style}">{item['p']} · {num:03}</div>
      <h1 style="{h1_style} font-size: 3rem;">{item['t']}</h1>
      <div style="{desc_style} font-size: 1.1rem; line-height: 1.6;">{item['d']}</div>
      <div v-click style="margin-top: auto; padding: 1rem; background: rgba(255,255,255,0.05); border-radius: 8px; border-left: 4px solid cyan;">
        <span style="font-weight: 900; font-size: 0.8rem; opacity: 0.5;">STRATEGIC NOTE</span><br/>
        The implementation of {item['t']} requires a shift in core organizational logic.
      </div>
    </div>
    <div v-click style="flex: 0.8; background: rgba(255,255,255,0.03); border-radius: 12px; border: 1px dashed rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: center; padding: 2rem;">
      <div style="text-align: center;">
         <div style="font-size: 4rem; margin-bottom: 1rem;">🚀</div>
         <div style="font-weight: 900; letter-spacing: 2px;">ACTIVE PHASE</div>
         <div style="opacity: 0.4; font-size: 0.8rem;">Chapter { (idx // 20) + 1 } Deployment</div>
      </div>
    </div>
  </div>
</div>
"""
    elif pattern == 2: # Three Card Feature
        return f"""
---
layout: default
class: {item['a']}
---
<div style="{wrapper_style}">
  <div style="{pill_style}">{item['p']} · {num:03}</div>
  <h1 style="{h1_style} text-align: center; margin-bottom: 2rem;">{item['t']}</h1>
  <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; width: 100%;">
    <div v-click style="{grid_box_style} text-align: center; padding: 1.5rem 1rem;">
      <div style="font-size: 2rem; margin-bottom: 0.5rem;">🧠</div>
      <div style="font-weight: 800; font-size: 0.8rem;">ARCHITECTURE</div>
    </div>
    <div v-click style="{grid_box_style} text-align: center; padding: 1.5rem 1rem;">
      <div style="font-size: 2rem; margin-bottom: 0.5rem;">⚡</div>
      <div style="font-weight: 800; font-size: 0.8rem;">SPEED</div>
    </div>
    <div v-click style="{grid_box_style} text-align: center; padding: 1.5rem 1rem;">
      <div style="font-size: 2rem; margin-bottom: 0.5rem;">🌍</div>
      <div style="font-weight: 800; font-size: 0.8rem;">SCALE</div>
    </div>
  </div>
  <div style="{desc_style} margin-top: 2rem; text-align: center; max-width: 80%; margin-left: auto; margin-right: auto;">{item['d']}</div>
</div>
"""
    else: # Large Statement (Atmospheric)
        return f"""
---
layout: default
class: {item['a']}
---
<div style="{wrapper_style} justify-content: space-between; padding: 4rem;">
  <div style="display: flex; justify-content: space-between; width: 100%; align-items: flex-start;">
    <div style="{pill_style}">{item['p']} · {num:03}</div>
    <div style="font-weight: 900; opacity: 0.2; letter-spacing: 5px;">0{ (idx // 20) + 1 }</div>
  </div>
  <div style="max-width: 80%;">
    <h1 style="{h1_style} font-size: 4rem; line-height: 0.9;">{item['t']}</h1>
    <div style="height: 4px; width: 60px; background: orange; margin: 1.5rem 0;"></div>
    <div style="{desc_style} font-size: 1.4rem; opacity: 0.9;">{item['d']}</div>
  </div>
  <div v-click style="width: 100%; padding-top: 2rem; border-top: 1px solid rgba(255,255,255,0.1); font-size: 0.8rem; letter-spacing: 1px; opacity: 0.5;">
    RESEARCHED PERSPECTIVE · 2024-2030 STRATEGY DECK
  </div>
</div>
"""

def main():
    slides = []
    
    # Fill remaining to hit exactly 100 if narrative is shorter
    # (The narrative script above is already ~100 but let's be safe)
    
    for i, item in enumerate(NARRATIVE):
        slides.append(generate_slide(i, item))
    
    # Padding to 100 if needed (it shouldn't be, I wrote 100 entries)
    while len(slides) < 100:
        slides.append(generate_slide(len(slides), NARRATIVE[-1]))

    output = FRONTMATTER + GLOBAL_STYLE + "".join(slides)
    
    with open("presentations/narrative_100.md", "w", encoding="utf-8") as f:
        f.write(output)
    
    print(f"Generated 100-slide Narrative Masterpiece.")

if __name__ == "__main__":
    main()
