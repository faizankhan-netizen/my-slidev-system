import json
import re
from .schema import SlideContent
from .config import STYLES, ENERGY_PROPS
from .boundguard import get_dynamic_title_style, get_dynamic_desc_style, get_cycle_bounds

def get_motion_props(energy: str, index: int = 0) -> str:
    delay = index * 100
    props = ENERGY_PROPS.get(energy, ENERGY_PROPS["standard"])
    initial = json.dumps(props["initial"])
    enter = props["enter"].copy()
    enter["transition"] = {**enter.get("transition", {}), "delay": delay}
    enter_str = json.dumps(enter)
    return f":initial='{initial}' :enter='{enter_str}'"

def _base_slide(content: SlideContent, archetype: str, inner_html: str, layout: str = "default") -> str:
    # Use the new CinematicBackdrop component for clean, reactive media handling
    bg_video_fm = f"\nbg_video_url: {content.bg_video_url}" if content.bg_video_url else ""
    
    # Navigation Dots (Vue-powered progress indicator)
    nav_dots = """
<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50">
  <div v-for="i in $nav.total" :key="i" 
       :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-cyan-400 w-4' : 'bg-white/20']">
  </div>
</div>
"""
    
    return f"""
---
layout: {layout}
class: {archetype}{bg_video_fm}
---
<CinematicBackdrop v-model:url="$frontmatter.bg_video_url" :url="$frontmatter.bg_video_url" />
{nav_dots}
{inner_html}
"""

def render_cover(c: SlideContent, archetype: str) -> str:
    html = f"""
<div style="{STYLES['wrapper_center']}">
  <div v-motion {get_motion_props(c.energy, 0)} style="{STYLES['pill']}">{c.module}</div>
  <h1 v-motion {get_motion_props(c.energy, 1)} style="{get_dynamic_title_style(c.title, True)}">{c.title}</h1>
  <div v-motion {get_motion_props(c.energy, 2)} style="{get_dynamic_desc_style(c.subtitle, True)}">{c.subtitle}</div>
</div>
"""
    return _base_slide(c, archetype, html, "center")

def render_section_intro(c: SlideContent, archetype: str) -> str:
    html = f"""
<div style="{STYLES['wrapper_center']}">
  <div v-motion {get_motion_props(c.energy, 0)} style="font-size: 4rem; margin-bottom: 1rem;">{c.emoji}</div>
  <div v-motion {get_motion_props(c.energy, 1)} style="{STYLES['pill']}">{c.module}</div>
  <h1 v-motion {get_motion_props(c.energy, 2)} style="{get_dynamic_title_style(c.title, True)} text-transform: uppercase;">{c.title}</h1>
  <div v-motion {get_motion_props(c.energy, 3)} style="{get_dynamic_desc_style(c.description, True)}">{c.description}</div>
</div>
"""
    return _base_slide(c, archetype, html, "center")

def render_data_point(c: SlideContent, archetype: str) -> str:
    html = f"""
<div style="{STYLES['wrapper_center']}">
  <div v-motion {get_motion_props(c.energy, 0)} style="{STYLES['pill']}">{c.module}</div>
  <div v-motion {get_motion_props(c.energy, 1)} style="font-size: 8rem; font-weight: 900; line-height: 1; color: var(--accent-primary, orange); text-shadow: 0 0 40px rgba(255,165,0,0.3); margin: 1rem 0;">{c.stat_value}</div>
  <div v-motion {get_motion_props(c.energy, 2)} style="font-size: 2rem; font-weight: 900; text-transform: uppercase; letter-spacing: 2px;">{c.stat_label}</div>
  <div v-motion {get_motion_props(c.energy, 3)} style="{get_dynamic_desc_style(c.description, True)} margin-top: 1.5rem;">{c.description}</div>
</div>
"""
    return _base_slide(c, archetype, html, "default")

def render_concept(c: SlideContent, archetype: str) -> str:
    html = f"""
<div style="{STYLES['wrapper']}">
  <div style="{STYLES['pill']}">{c.module}</div>
  <h1 style="{get_dynamic_title_style(c.title)}">{c.title}</h1>
  <div style="{get_dynamic_desc_style(c.description)} max-width: 60%;">{c.description}</div>
  <div v-click style="margin-top: auto; padding: 1.5rem; background: rgba(255,255,255,0.05); border-left: 4px solid var(--accent-primary, cyan); border-radius: 8px;">
    <div style="font-size: 2rem; margin-bottom: 0.5rem;">{c.emoji}</div>
    <div style="font-weight: 700;">{c.subtitle}</div>
  </div>
</div>
"""
    return _base_slide(c, archetype, html, "default")

def render_comparison(c: SlideContent, archetype: str) -> str:
    if len(c.items) < 2: c.items = ["Item 1", "Item 2"]
    html = f"""
<div style="{STYLES['wrapper']}">
  <div style="{STYLES['pill']}">{c.module}</div>
  <h1 style="{get_dynamic_title_style(c.title, True)}">{c.title}</h1>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; width: 100%; margin-top: 2rem; flex: 1;">
    <div v-click style="{STYLES['grid_box']} display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; border-color: rgba(255,0,0,0.3);">
      <div style="font-size: 3rem; margin-bottom: 1rem;">{c.items[0].split('|')[0] if '|' in c.items[0] else '❌'}</div>
      <div style="font-size: 1.2rem; font-weight: 800;">{c.items[0].split('|')[-1]}</div>
    </div>
    <div v-click style="{STYLES['grid_box']} display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; border-color: rgba(0,255,0,0.3);">
      <div style="font-size: 3rem; margin-bottom: 1rem;">{c.items[1].split('|')[0] if '|' in c.items[1] else '✅'}</div>
      <div style="font-size: 1.2rem; font-weight: 800;">{c.items[1].split('|')[-1]}</div>
    </div>
  </div>
</div>
"""
    return _base_slide(c, archetype, html, "default")

def render_process(c: SlideContent, archetype: str) -> str:
    items_html = ""
    for i, item in enumerate(c.items):
        items_html += f"""
<div v-click style="display: flex; gap: 1.5rem; align-items: flex-start; margin-bottom: 1rem;">
  <div style="font-size: 1.5rem; font-weight: 900; color: var(--accent-primary, cyan); opacity: 0.8;">{i+1:02d}</div>
  <div style="{STYLES['grid_box']} padding: 1rem;">{item}</div>
</div>
"""
    html = f"""
<div style="{STYLES['wrapper']}">
  <div style="{STYLES['pill']}">{c.module}</div>
  <h1 style="{get_dynamic_title_style(c.title)}">{c.title}</h1>
  <div style="{get_dynamic_desc_style(c.description)}">{c.description}</div>
  <div style="margin-top: 1rem; width: 100%;">
{items_html}
  </div>
</div>
"""
    return _base_slide(c, archetype, html, "default")

def render_feature_grid(c: SlideContent, archetype: str) -> str:
    items_html = ""
    for item in c.items[:4]:
        parts = item.split('|')
        icon = parts[0] if len(parts) > 1 else '✨'
        text = parts[-1]
        items_html += f"""
<div v-click style="{STYLES['grid_box']} display: flex; flex-direction: column; gap: 0.5rem;">
  <div style="font-size: 2rem;">{icon}</div>
  <div style="font-weight: 700; font-size: 1.1rem;">{text}</div>
</div>
"""
    html = f"""
<div style="{STYLES['wrapper']}">
  <div style="{STYLES['pill']}">{c.module}</div>
  <h1 style="{get_dynamic_title_style(c.title)}">{c.title}</h1>
  <div style="{get_dynamic_desc_style(c.description)}">{c.description}</div>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; width: 100%; margin-top: 1rem; flex: 1;">
{items_html}
  </div>
</div>
"""
    return _base_slide(c, archetype, html, "default")

def render_quote(c: SlideContent, archetype: str) -> str:
    html = f"""
<div style="{STYLES['wrapper_center']}">
  <div style="font-size: 5rem; color: var(--accent-primary, cyan); opacity: 0.5; margin-bottom: -2rem; font-family: serif;">"</div>
  <div v-motion :initial="{{opacity:0}}" :enter="{{opacity:1}}" style="{get_dynamic_desc_style(c.quote_text, True)} font-size: 2.5rem; font-weight: 700; font-style: italic; line-height: 1.3; max-width: 80%;">{c.quote_text}</div>
  <div v-motion :initial="{{opacity:0, y:10}}" :enter="{{opacity:1, y:0}}" style="margin-top: 2rem; font-size: 1.2rem; font-weight: 600; text-transform: uppercase; letter-spacing: 2px;">— {c.quote_author}</div>
</div>
"""
    return _base_slide(c, archetype, html, "center")

def render_agenda(c: SlideContent, archetype: str) -> str:
    items_html = ""
    for idx, item in enumerate(c.items):
        items_html += f"""
<div v-click v-motion {get_motion_props(c.energy, idx+2)} 
     @click="$nav.go($nav.currentPage + {idx+1})"
     style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 16px; cursor: pointer; transition: all 0.3s ease; pointer-events: auto;"
     onmouseover="this.style.background='rgba(255,255,255,0.1)'; this.style.borderColor='var(--accent-primary, cyan)';"
     onmouseout="this.style.background='rgba(255,255,255,0.05)'; this.style.borderColor='rgba(255,255,255,0.1)';"
>
  <div style="font-size: 0.8rem; opacity: 0.5; font-weight: 900; margin-bottom: 0.5rem;">0{idx+1}</div>
  <div style="font-size: 1.2rem; font-weight: 900; letter-spacing: 1px;">{item}</div>
</div>
"""
    html = f"""
<div style="{STYLES['wrapper']}">
  <div v-motion {get_motion_props(c.energy, 0)} style="{STYLES['pill']}">{c.module}</div>
  <h1 v-motion {get_motion_props(c.energy, 1)} style="{get_dynamic_title_style(c.title)}">{c.title}</h1>
  <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1.5rem; margin-top: 2rem;">
    {items_html}
  </div>
</div>
"""
    return _base_slide(c, archetype, html, "default")

def render_cycle(c: SlideContent, archetype: str) -> str:
    bounds = get_cycle_bounds(len(c.items), c.title)
    items_html = ""
    ring_colors = ["#00f2fe", "#4facfe", "#38f9d7", "#6a11cb", "#2575fc"]
    count = min(len(c.items), 6) or 1
    radius, node_size = bounds["radius"], bounds["node_size"]
    
    for i, item in enumerate(c.items[:6]):
        angle = (i / count) * 360
        items_html += f"""
<div style="position:absolute; left:50%; top:50%; transform:rotate({angle}deg) translate({radius}px) rotate(-{angle}deg); pointer-events:none; z-index:10;">
  <div v-click v-motion {get_motion_props(c.energy, i+2)} 
       style="width:{node_size}px; height:{node_size}px; margin-left:-{node_size/2}px; margin-top:-{node_size/2}px; background:rgba(0,0,0,0.8); border:2px solid {ring_colors[i%len(ring_colors)]}; border-radius:50%; display:flex; align-items:center; justify-content:center; text-align:center; padding:1rem; font-size:0.7rem; font-weight:800; box-shadow:0 0 20px {ring_colors[i%len(ring_colors)]}44; pointer-events:auto; backdrop-filter:blur(10px);">
    {item}
  </div>
</div>
"""
    html = f"""
<div style="{STYLES['wrapper']}">
  <div v-motion {get_motion_props(c.energy, 0)} style="{STYLES['pill']}">{c.module}</div>
  <h1 v-motion {get_motion_props(c.energy, 1)} style="{get_dynamic_title_style(c.title)}">{c.title}</h1>
  <div style="flex: 1; position: relative; width: 100%; display: flex; align-items: center; justify-content: center; margin-top: {bounds['margin_top_px']}px; margin-bottom: 40px;">
    <div v-motion :initial="{{scale:0}}" :enter="{{scale:1, transition:{{type:'spring', delay:500}}}}" 
         style="width:{node_size*0.7}px; height:{node_size*0.7}px; background:var(--accent-primary, #00f2fe); border-radius:50%; z-index:20; display:flex; align-items:center; justify-content:center; box-shadow:0 0 40px var(--accent-primary, #00f2fe); pointer-events:auto;">
      <div style="color:black; font-weight:900; font-size:0.5rem; text-transform:uppercase; letter-spacing:1px; text-align:center;">{c.module}</div>
    </div>
    <div style="position:absolute; width:{radius*2}px; height:{radius*2}px; border:1px dashed rgba(255,255,255,0.1); border-radius:50%; pointer-events:none; z-index:1;"></div>
    {items_html}
  </div>
</div>
"""
    return _base_slide(c, archetype, html, "default")

def render_chart(c: SlideContent, archetype: str) -> str:
    option = {
        "backgroundColor": "transparent",
        "tooltip": {"trigger": "axis"},
        "xAxis": {"type": "category", "data": [d.get("name", "") for d in c.chart_data], "axisLabel": {"color": "rgba(255,255,255,0.6)"}},
        "yAxis": {"type": "value", "axisLabel": {"color": "rgba(255,255,255,0.6)"}, "splitLine": {"lineStyle": {"color": "rgba(255,255,255,0.1)"}}},
        "series": [{"data": [d.get("value", 0) for d in c.chart_data], "type": c.chart_type or "bar", "itemStyle": {"color": "var(--accent-primary, #00f2fe)"}, "areaStyle": {"opacity": 0.3} if c.chart_type == "line" else None}]
    }
    html = f"""
<div style="{STYLES['wrapper']}">
  <div style="{STYLES['pill']}">{c.module}</div>
  <h1 style="{get_dynamic_title_style(c.title)}">{c.title}</h1>
  <div style="{get_dynamic_desc_style(c.description)}">{c.description}</div>
  <div style="flex: 1; min-height: 0; width: 100%; margin-top: 1rem;">
    <v-chart :option='{json.dumps(option)}' autoresize style="width: 100%; height: 100%;" />
  </div>
</div>
"""
    return _base_slide(c, archetype, html, "default")

def render_table(c: SlideContent, archetype: str) -> str:
    headers = "".join([f"<th style='padding: 1rem; text-align: left; border-bottom: 2px solid rgba(255,255,255,0.2); text-transform: uppercase; font-size: 0.8rem;'>{h}</th>" for h in c.table_headers])
    rows = "".join([f"<tr style='background: {'rgba(255,255,255,0.03)' if i%2==0 else 'transparent'};'>" + "".join([f"<td style='padding: 1rem; border-bottom: 1px solid rgba(255,255,255,0.05);'>{cell}</td>" for cell in row]) + "</tr>" for i, row in enumerate(c.table_rows)])
    html = f"""
<div style="{STYLES['wrapper']}">
  <div style="{STYLES['pill']}">{c.module}</div>
  <h1 style="{get_dynamic_title_style(c.title)}">{c.title}</h1>
  <div style="margin-top: 1.5rem; width: 100%; overflow: hidden; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1); background: rgba(0,0,0,0.2);">
    <table style="width: 100%; border-collapse: collapse; font-size: 1.1rem;">
      <thead><tr style="background: rgba(255,255,255,0.05);">{headers}</tr></thead>
      <tbody>{rows}</tbody>
    </table>
  </div>
</div>
"""
    return _base_slide(c, archetype, html, "default")

def render_media_focus(c: SlideContent, archetype: str) -> str:
    # Use robust regex for YT
    yt_reg = r'^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*'
    match = re.match(yt_reg, c.media_url) if c.media_url else None
    yt_id = match.group(2) if match and len(match.group(2)) == 11 else None
    
    media_tag = f"<iframe src='https://www.youtube.com/embed/{yt_id}?controls=1&rel=0' style='width: 100%; height: 100%; border: none; border-radius: 12px;' />" if yt_id else f"<video src='{c.media_url}' controls autoplay loop muted style='width: 100%; height: 100%; object-fit: cover; border-radius: 12px;' />" if c.media_type == "video" else f"<img src='{c.media_url}' style='width: 100%; height: 100%; object-fit: cover; border-radius: 12px;' />"
    
    html = f"""
<div style="{STYLES['wrapper']}">
  <div style="display: flex; width: 100%; height: 100%; gap: 3rem;">
    <div style="flex: 1; display: flex; flex-direction: column; justify-content: center;">
      <div v-motion {get_motion_props(c.energy, 0)} style="{STYLES['pill']}">{c.module}</div>
      <h1 v-motion {get_motion_props(c.energy, 1)} style="{get_dynamic_title_style(c.title)}">{c.title}</h1>
      <div v-motion {get_motion_props(c.energy, 2)} style="{get_dynamic_desc_style(c.description)}">{c.description}</div>
      {f'<a href="{c.cta_link}" v-motion {get_motion_props(c.energy, 3)} style="margin-top: 2rem; padding: 1rem 2rem; background: var(--accent-primary, cyan); color: black; font-weight: 900; text-decoration: none; border-radius: 50px; width: fit-content;">{c.cta_text}</a>' if c.cta_text else ""}
    </div>
    <div v-motion :initial="{{opacity:0, x:50}}" :enter="{{opacity:1, x:0}}" style="flex: 1.2; padding: 1rem;">{media_tag}</div>
  </div>
</div>
"""
    return _base_slide(c, archetype, html, "default")

def render_activity(c: SlideContent, archetype: str) -> str:
    html = f"""
<div style="{STYLES['wrapper_center']}">
  <div style="{STYLES['pill']} background: rgba(255,0,0,0.2); border-color: rgba(255,0,0,0.5); color: #ff9999;">ACTIVITY BREAK</div>
  <div style="font-size: 4rem; margin-bottom: 1rem;">{c.emoji}</div>
  <h1 style="{get_dynamic_title_style(c.title, True)}">{c.title}</h1>
  <div v-click style="{STYLES['grid_box']} max-width: 70%; margin: 2rem auto; font-size: 1.5rem; font-weight: 700;">
    {c.description}
  </div>
</div>
"""
    return _base_slide(c, archetype, html, "center")

def render_case_study(c: SlideContent, archetype: str) -> str:
    html = f"""
<div style="{STYLES['wrapper']}">
  <div style="display: flex; width: 100%; height: 100%; gap: 3rem;">
    <div style="flex: 1.2; display: flex; flex-direction: column;">
      <div style="{STYLES['pill']}">{c.module}</div>
      <h1 style="{get_dynamic_title_style(c.title)}">{c.title}</h1>
      <div style="{get_dynamic_desc_style(c.description)}">{c.description}</div>
      <div v-click style="margin-top: auto; padding: 1.5rem; background: rgba(255,255,255,0.05); border-radius: 8px; border-left: 4px solid var(--accent-primary, cyan);">
        <span style="font-weight: 900; font-size: 0.8rem; opacity: 0.5;">CASE HIGHLIGHT</span><br/>
        <div style="font-size: 1.1rem; font-weight: 700; margin-top: 0.5rem;">{c.subtitle}</div>
      </div>
    </div>
    <div v-click style="flex: 0.8; background: rgba(255,255,255,0.03); border-radius: 12px; border: 1px dashed rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: center; padding: 2rem;">
      <div style="text-align: center;">
         <div style="font-size: 5rem; margin-bottom: 1rem;">{c.emoji}</div>
         <div style="font-weight: 900; letter-spacing: 2px;">{c.stat_value}</div>
         <div style="opacity: 0.6; font-size: 0.9rem;">{c.stat_label}</div>
      </div>
    </div>
  </div>
</div>
"""
    return _base_slide(c, archetype, html, "default")

def render_finale(c: SlideContent, archetype: str) -> str:
    html = f"""
<div style="{STYLES['wrapper_center']}">
  <h1 v-motion {get_motion_props(c.energy, 0)} style="{get_dynamic_title_style(c.title, True)}">{c.title}</h1>
  <div v-motion {get_motion_props(c.energy, 1)} style="font-size: 1.5rem; opacity: 0.8;">{c.subtitle}</div>
</div>
"""
    return _base_slide(c, archetype, html, "center")

TEMPLATE_REGISTRY = {
    "cover": render_cover, "agenda": render_agenda, "section_intro": render_section_intro,
    "concept": render_concept, "comparison": render_comparison, "data_point": render_data_point,
    "process": render_process, "feature_grid": render_feature_grid, "quote": render_quote,
    "activity": render_activity, "case_study": render_case_study, "cycle": render_cycle,
    "chart": render_chart, "table": render_table, "media_focus": render_media_focus, "finale": render_finale
}

def render_slide(c: SlideContent, archetype: str) -> str:
    return TEMPLATE_REGISTRY.get(c.content_type, render_concept)(c, archetype)
