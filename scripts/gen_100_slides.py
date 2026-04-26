"""
gen_100_slides.py — Stress Test Generator
Generates a 100-slide Slidev deck covering 5 modules × ~18 slides each.
Run: python scripts/gen_100_slides.py
Output: presentations/stress_test_100.md
"""

import textwrap

FRONTMATTER = """\
---
title: "Global AI Summit — 100-Slide Stress Test"
transition: fade
canvasWidth: 900
---
"""

GLOBAL_STYLE = """\
<style>
.slidev-layout { overflow:hidden; padding: 0 !important; }
body, #app { background: #0a0a0f; }
.pill {
  display:inline-block; padding:5px 16px; border-radius:9999px;
  font-size:10px; font-weight:900; letter-spacing:0.3em;
  text-transform:uppercase; color:white;
}
.content-wrapper {
  position:relative; z-index:10; height:100%;
  display:flex; flex-direction:column;
}
.dot { position:absolute; border-radius:50%; pointer-events:none; z-index:0; }
.stat-block {
  background:rgba(255,255,255,0.07); border-radius:16px;
  padding:1.2rem 1.5rem; border-top:4px solid currentColor;
}
</style>

"""

# ── Module definitions ──────────────────────────────────────────────────────
MODULES = [
    {
        "name": "The AI Revolution",
        "style": "style-school",
        "bg": "#0B0C2A",
        "accent": "#22D3EE",
        "pill_bg": "#22D3EE",
        "pill_text": "#0B0C2A",
        "slide_range": (4, 22),
    },
    {
        "name": "Business Impact",
        "style": "style-business",
        "bg": "#0F172A",
        "accent": "#F97316",
        "pill_bg": "#F97316",
        "pill_text": "#ffffff",
        "slide_range": (23, 41),
    },
    {
        "name": "Technical Architecture",
        "style": "style-cyber",
        "bg": "#050d05",
        "accent": "#22C55E",
        "pill_bg": "#22C55E",
        "pill_text": "#050d05",
        "slide_range": (42, 60),
    },
    {
        "name": "Sustainability & Ethics",
        "style": "style-eco",
        "bg": "#0d1f12",
        "accent": "#86EFAC",
        "pill_bg": "#86EFAC",
        "pill_text": "#0d1f12",
        "slide_range": (61, 79),
    },
    {
        "name": "The Future Roadmap",
        "style": "style-luxury",
        "bg": "#0a0508",
        "accent": "#D4AF37",
        "pill_bg": "#D4AF37",
        "pill_text": "#0a0508",
        "slide_range": (80, 98),
    },
]

LAYOUTS = ["center", "fact", "two-cols", "cards", "default"]

EMOJIS = ["🚀","🧠","⚡","🌍","🔬","💡","📊","🛰️","🌱","🏗️","🔐","💎","🤖","📡","🧬","⚙️","🌐","🏆"]

TOPICS = [
    "Attention Mechanisms","Neural Networks","Transformers","Embeddings","Inference Speed",
    "Model Alignment","Data Pipelines","Vector Databases","Edge Computing","Zero-Shot Learning",
    "Prompt Engineering","Fine-Tuning","RAG Systems","Multi-Modal AI","Safety Frameworks",
    "Carbon Footprint","AI Governance","Bias Detection","Synthetic Data","Autonomous Agents",
    "Supply Chain AI","Predictive Analytics","NLP Breakthroughs","Computer Vision","Robotics",
    "Quantum ML","Federated Learning","On-Device AI","AI in Healthcare","AI in Education",
]

STATS = [
    ("$15.7T","Global AI economic impact by 2030"),
    ("97M","New AI-related jobs created by 2025"),
    ("80%","Enterprises using AI in some capacity"),
    ("3.5×","Productivity gain with AI assistance"),
    ("500B","Parameters in the largest LLMs today"),
    ("40%","Reduction in energy via AI optimization"),
    ("$4.4T","Annual value AI could add to business"),
    ("72%","Of execs say AI is a top-3 priority"),
    ("10×","Faster drug discovery with AI models"),
    ("60%","Drop in ML model training costs since 2020"),
]

def pill(text, bg="#22D3EE", color="#0B0C2A"):
    return f'<span class="pill" style="background:{bg};color:{color};">{text}</span>'

def dot(size, top=None, bottom=None, left=None, right=None, color="#ffffff"):
    pos = ""
    if top is not None: pos += f"top:{top}px;"
    if bottom is not None: pos += f"bottom:{bottom}px;"
    if left is not None: pos += f"left:{left}px;"
    if right is not None: pos += f"right:{right}px;"
    return f'<div class="dot" style="width:{size}px;height:{size}px;{pos}background:{color};opacity:0.25;"></div>'

def slide_cover():
    return '''\
<div style="position:relative;width:100%;height:100%;background:#03001a;padding:3.5rem;overflow:hidden;">
  <div class="dot" style="width:500px;height:500px;top:-150px;right:-150px;background:#6366F1;opacity:0.18;border-radius:50%;"></div>
  <div class="dot" style="width:300px;height:300px;bottom:-80px;left:-80px;background:#22D3EE;opacity:0.12;border-radius:50%;"></div>
  <div class="content-wrapper justify-center">
    <div>
      <span class="pill" style="background:#6366F1;color:white;">GLOBAL AI SUMMIT · STRESS TEST</span>
      <div style="font-size:5.5rem;font-weight:900;color:white;line-height:1;letter-spacing:-0.05em;margin-top:1rem;">AI at</div>
      <div style="font-size:5.5rem;font-weight:900;color:#22D3EE;line-height:1;letter-spacing:-0.05em;margin-bottom:1.5rem;">Scale.</div>
      <div style="color:#94A3B8;font-size:1.1rem;font-weight:600;">100 Slides · 5 Modules · Full Engine Stress Test</div>
    </div>
  </div>
</div>'''

def slide_agenda():
    items = [
        ("01","The AI Revolution","#22D3EE"),
        ("02","Business Impact","#F97316"),
        ("03","Technical Architecture","#22C55E"),
        ("04","Sustainability & Ethics","#86EFAC"),
        ("05","The Future Roadmap","#D4AF37"),
    ]
    rows = ""
    for num, name, color in items:
        rows += f'''
      <div v-click style="display:flex;align-items:center;gap:1.2rem;background:rgba(255,255,255,0.04);border-radius:12px;padding:0.8rem 1.2rem;border-left:4px solid {color};">
        <div style="font-size:1.8rem;font-weight:900;color:{color};font-family:monospace;">{num}</div>
        <div style="font-size:1.1rem;font-weight:700;color:white;">{name}</div>
      </div>'''
    return f'''\
<div style="position:relative;width:100%;height:100%;background:#03001a;padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:#6366F1;color:white;margin-bottom:1.2rem;">TODAY'S AGENDA</span>
    <div style="font-size:2.5rem;font-weight:900;color:white;margin-bottom:1.5rem;">5 Modules. 100 Slides.</div>
    <div style="display:flex;flex-direction:column;gap:0.6rem;">{rows}
    </div>
  </div>
</div>'''

def slide_module_intro(mod, slide_num):
    return f'''\
<div style="position:relative;width:100%;height:100%;background:{mod["bg"]};padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div class="dot" style="width:450px;height:450px;top:-150px;right:-150px;background:{mod["accent"]};opacity:0.12;border-radius:50%;"></div>
  <div style="position:relative;z-index:10;">
    <span class="pill" style="background:{mod["pill_bg"]};color:{mod["pill_text"]};">MODULE {slide_num // 20 + 1}</span>
    <div style="font-size:4rem;font-weight:900;color:white;line-height:1.1;letter-spacing:-0.04em;margin-top:1rem;">{mod["name"]}</div>
    <div style="font-size:1.2rem;color:{mod["accent"]};margin-top:1rem;font-weight:600;">{EMOJIS[slide_num % len(EMOJIS)]} Deep dive begins now.</div>
  </div>
</div>'''

def slide_stat(idx, mod):
    stat, label = STATS[idx % len(STATS)]
    return f'''\
<div style="position:relative;width:100%;height:100%;background:{mod["bg"]};padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div class="content-wrapper items-center justify-center">
    <span class="pill" style="background:{mod["pill_bg"]};color:{mod["pill_text"]};margin-bottom:1.5rem;">KEY METRIC</span>
    <div style="font-size:6rem;font-weight:900;color:{mod["accent"]};line-height:1;letter-spacing:-0.05em;">{stat}</div>
    <div style="font-size:1.4rem;color:white;margin-top:1rem;font-weight:700;max-width:500px;">{label}</div>
  </div>
</div>'''

def slide_two_col(idx, mod):
    topic_a = TOPICS[(idx * 2) % len(TOPICS)]
    topic_b = TOPICS[(idx * 2 + 1) % len(TOPICS)]
    emoji_a = EMOJIS[idx % len(EMOJIS)]
    emoji_b = EMOJIS[(idx + 5) % len(EMOJIS)]
    return f'''\
<div style="position:relative;width:100%;height:100%;background:{mod["bg"]};padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:{mod["pill_bg"]};color:{mod["pill_text"]};margin-bottom:1rem;">COMPARISON</span>
    <div style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;">{topic_a} vs {topic_b}</div>
    <div style="display:flex;gap:1.5rem;flex:1;">
      <div v-click style="flex:1;background:rgba(255,255,255,0.05);border-radius:16px;padding:1.5rem;border-top:4px solid {mod["accent"]};">
        <div style="font-size:2rem;margin-bottom:0.8rem;">{emoji_a}</div>
        <div style="font-size:1.2rem;font-weight:900;color:white;margin-bottom:0.5rem;">{topic_a}</div>
        <div style="font-size:0.9rem;color:#94A3B8;line-height:1.6;">Foundational layer enabling scalable, adaptive intelligence across distributed systems and real-time data pipelines.</div>
      </div>
      <div v-click style="flex:1;background:rgba(255,255,255,0.05);border-radius:16px;padding:1.5rem;border-top:4px solid {mod["accent"]};">
        <div style="font-size:2rem;margin-bottom:0.8rem;">{emoji_b}</div>
        <div style="font-size:1.2rem;font-weight:900;color:white;margin-bottom:0.5rem;">{topic_b}</div>
        <div style="font-size:0.9rem;color:#94A3B8;line-height:1.6;">Next-generation paradigm shifting how organizations architect decision-making at the edge and in the cloud.</div>
      </div>
    </div>
  </div>
</div>'''

def slide_cards(idx, mod):
    topic = TOPICS[idx % len(TOPICS)]
    cards = []
    for i in range(3):
        e = EMOJIS[(idx + i) % len(EMOJIS)]
        t = TOPICS[(idx + i + 1) % len(TOPICS)]
        cards.append(f'''
      <div v-click style="background:rgba(255,255,255,0.05);border-radius:14px;padding:1.2rem;border-left:3px solid {mod["accent"]};">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">{e}</div>
        <div style="font-size:1rem;font-weight:800;color:white;margin-bottom:0.3rem;">{t}</div>
        <div style="font-size:0.8rem;color:#94A3B8;">Enabling robust, scalable AI workflows across enterprise infrastructure with real-time feedback loops.</div>
      </div>''')
    cards_html = "".join(cards)
    return f'''\
<div style="position:relative;width:100%;height:100%;background:{mod["bg"]};padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:{mod["pill_bg"]};color:{mod["pill_text"]};margin-bottom:1rem;">KEY CONCEPTS</span>
    <div style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;">{topic}</div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;flex:1;">{cards_html}
    </div>
  </div>
</div>'''

def slide_quote(idx, mod):
    quotes = [
        ("AI is the new electricity.", "Andrew Ng"),
        ("The question is not whether AI will change the world, but how fast.", "Demis Hassabis"),
        ("Every company will be an AI company.", "Jensen Huang"),
        ("AI will be the defining technology of the 21st century.", "Sundar Pichai"),
        ("We're at the iPhone moment for AI.", "Sam Altman"),
    ]
    q, author = quotes[idx % len(quotes)]
    return f'''\
<div style="position:relative;width:100%;height:100%;background:{mod["bg"]};padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;">
  <div class="dot" style="width:350px;height:350px;top:-100px;left:-100px;background:{mod["accent"]};opacity:0.08;border-radius:50%;"></div>
  <div style="position:relative;z-index:10;text-align:center;max-width:700px;">
    <div style="font-size:3rem;color:{mod["accent"]};margin-bottom:1rem;font-weight:900;">"</div>
    <div v-click style="font-size:2rem;font-weight:800;color:white;line-height:1.3;margin-bottom:1.5rem;">{q}</div>
    <div v-click style="font-size:1rem;color:{mod["accent"]};font-weight:700;letter-spacing:0.1em;text-transform:uppercase;">— {author}</div>
  </div>
</div>'''

def slide_list(idx, mod):
    topic = TOPICS[idx % len(TOPICS)]
    points = [
        "Scalable infrastructure enabling real-time inference at the network edge",
        "Self-supervised learning reducing labeled data requirements by 10×",
        "Constitutional AI frameworks ensuring model safety and alignment",
        "Multimodal pipelines unifying vision, audio, and language understanding",
        "Federated architectures preserving data privacy across jurisdictions",
    ]
    items_html = ""
    for i, pt in enumerate(points[:4]):
        items_html += f'''
      <div v-click style="display:flex;gap:1rem;align-items:flex-start;padding:0.8rem 0;border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-size:1rem;font-weight:900;color:{mod["accent"]};font-family:monospace;min-width:32px;">{str(i+1).zfill(2)}</div>
        <div style="font-size:0.95rem;color:#CBD5E1;line-height:1.5;">{pt}</div>
      </div>'''
    return f'''\
<div style="position:relative;width:100%;height:100%;background:{mod["bg"]};padding:3.5rem;overflow:hidden;">
  <div class="content-wrapper">
    <span class="pill" style="background:{mod["pill_bg"]};color:{mod["pill_text"]};margin-bottom:1rem;">KEY POINTS</span>
    <div style="font-size:2.2rem;font-weight:900;color:white;margin-bottom:1.5rem;">{topic}</div>
    <div style="flex:1;">{items_html}
    </div>
  </div>
</div>'''

def slide_activity(idx, mod):
    activities = [
        ("🎯 Quick Poll", "Raise your hand if you've used AI in the last 24 hours."),
        ("💬 Think-Pair-Share", "What industry will AI disrupt most in the next 5 years?"),
        ("🧠 Kahoot Round", "Test your knowledge — open Kahoot on your device."),
        ("✍️ 60-Second Write", "Name 3 AI tools you use without thinking about it."),
        ("🗳️ Live Vote", "Which AI risk concerns you most? Cast your vote now."),
    ]
    title, prompt = activities[idx % len(activities)]
    return f'''\
<div style="position:relative;width:100%;height:100%;background:{mod["bg"]};padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div style="position:relative;z-index:10;max-width:650px;">
    <span class="pill" style="background:{mod["pill_bg"]};color:{mod["pill_text"]};margin-bottom:1.5rem;">ACTIVITY BREAK</span>
    <div style="font-size:3rem;font-weight:900;color:white;margin:1rem 0;">{title}</div>
    <div v-click style="background:rgba(255,255,255,0.06);border-radius:16px;padding:1.5rem 2rem;border:1px solid rgba(255,255,255,0.1);">
      <div style="font-size:1.3rem;color:{mod["accent"]};font-weight:700;">{prompt}</div>
    </div>
  </div>
</div>'''

def slide_finale():
    return '''\
<div style="position:relative;width:100%;height:100%;background:#03001a;padding:3.5rem;overflow:hidden;display:flex;align-items:center;justify-content:center;text-align:center;">
  <div class="dot" style="width:500px;height:500px;top:-200px;right:-200px;background:#6366F1;opacity:0.15;border-radius:50%;"></div>
  <div class="dot" style="width:400px;height:400px;bottom:-150px;left:-150px;background:#22D3EE;opacity:0.10;border-radius:50%;"></div>
  <div style="position:relative;z-index:10;">
    <span class="pill" style="background:#6366F1;color:white;">STRESS TEST COMPLETE</span>
    <div style="font-size:5rem;font-weight:900;color:white;line-height:1;letter-spacing:-0.05em;margin:1rem 0;">100 Slides.</div>
    <div style="font-size:5rem;font-weight:900;color:#22D3EE;line-height:1;letter-spacing:-0.05em;margin-bottom:1.5rem;">Engine Holds.</div>
    <div v-click style="font-size:1.2rem;color:#94A3B8;font-weight:600;">All archetypes · All layouts · All components — verified at scale.</div>
  </div>
</div>'''

# ── Generator ──────────────────────────────────────────────────────────────

def get_slide_content(n, mod, local_idx):
    """Return HTML for slide n (1-indexed), local_idx = position within module."""
    pattern = local_idx % 6
    stat_idx = (n + local_idx) % len(STATS)
    if pattern == 0:
        return slide_stat(stat_idx, mod)
    elif pattern == 1:
        return slide_two_col(n, mod)
    elif pattern == 2:
        return slide_cards(n, mod)
    elif pattern == 3:
        return slide_quote(n, mod)
    elif pattern == 4:
        return slide_list(n, mod)
    else:
        return slide_activity(n, mod)

def generate():
    slides = []

    # Slide 1 — Cover
    slides.append(slide_cover())
    # Slide 2 — Agenda
    slides.append(slide_agenda())
    # Slide 3 — Opening quote (space style)
    space_mod = {"bg":"#03001a","accent":"#A78BFA","pill_bg":"#A78BFA","pill_text":"#03001a"}
    slides.append(slide_quote(0, space_mod))

    for mod in MODULES:
        start, end = mod["slide_range"]
        # Module intro slide
        slides.append(slide_module_intro(mod, start))
        # Content slides
        count = end - start  # remaining slides in this module
        for local_idx in range(count):
            n = start + local_idx + 1
            slides.append(get_slide_content(n, mod, local_idx))

    # Slides 99–100 — Finale
    while len(slides) < 99:
        # pad to 99 if needed
        last_mod = MODULES[-1]
        slides.append(slide_list(len(slides), last_mod))

    slides.append(slide_finale())

    # Trim to exactly 100
    slides = slides[:100]

    separator = "\n\n---\n\n"
    body = separator.join(slides)
    output = FRONTMATTER + GLOBAL_STYLE + body

    out_path = "presentations/stress_test_100.md"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"[OK] Generated {len(slides)} slides -> {out_path}")
    print(f"   File size: {len(output) / 1024:.1f} KB")

if __name__ == "__main__":
    generate()
