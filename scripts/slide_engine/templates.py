from .orchestrator import ComputedSlideState
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

def _pill(module: str, state: 'ComputedSlideState') -> str:
    """Renders module label using archetype CSS pill class."""
    if not module:
        return ""
    css_cls = state.pill_class
    if css_cls:
        return f'<div class="{css_cls}">{module}</div>'
    return f'<div style="display:inline-block;width:fit-content;padding:4px 12px;border-radius:30px;font-size:10px;font-weight:900;letter-spacing:2px;text-transform:uppercase;margin-bottom:0.8rem;border:1px solid rgba(255,255,255,0.2);background:rgba(255,255,255,0.1);">{module}</div>'

def _card(inner: str, state: 'ComputedSlideState', extra_style: str = "") -> str:
    """Renders a card using archetype CSS card class. extra_style = structural props only."""
    css_cls = state.card_class
    style_attr = f' style="{extra_style}"' if extra_style else ''
    if css_cls:
        return f'<div v-click class="{css_cls}"{style_attr}>{inner}</div>'
    return f'<div v-click style="background:rgba(255,255,255,0.07);padding:1rem;border-radius:12px;border:1px solid rgba(255,255,255,0.1);{extra_style}">{inner}</div>'

def _stat(value: str, state: 'ComputedSlideState') -> str:
    """Renders a stat number using archetype CSS stat class."""
    css_cls = state.stat_class
    if css_cls:
        return f'<div class="{css_cls}">{value}</div>'
    return f'<div style="font-size:8rem;font-weight:900;line-height:1;color:var(--accent-primary);margin:1rem 0;">{value}</div>'

def _wrapper(inner: str, state: 'ComputedSlideState', center: bool = False) -> str:
    """Renders content wrapper. Uses CSS class if archetype defines one, otherwise structural inline."""
    css_cls = state.wrapper_class
    structural = "display:flex;flex-direction:column;height:100%;"
    if center:
        structural += "justify-content:center;align-items:center;text-align:center;"
    if css_cls:
        return f'<div class="{css_cls}" style="{structural}">{inner}</div>'
    return f'<div style="position:relative;z-index:10;{structural}pointer-events:none;">{inner}</div>'

def _base_slide(content: SlideContent, archetype: str, inner_html: str, layout: str = "default", state: 'ComputedSlideState' = None) -> str:
    if state is None:
        from .orchestrator import orchestrate_slide
        state = orchestrate_slide(content, archetype)

    # Phase 0 fix: correct per-archetype font import
    font_import = getattr(state, 'font_import', 'Inter:wght@400;700')
    fonts = f'<link href="https://fonts.googleapis.com/css2?family={font_import}&display=swap" rel="stylesheet" />'
    
    bg_video_fm = f"\nbg_video_url: {content.bg_video_url}" if content.bg_video_url else ""
    css_vars = f"  --slide-bg: {state.slide_bg};\n  --slide-text: {state.slide_text};\n  --accent-primary: {state.accent_color};\n  --accent-secondary: {state.accent_secondary};\n  --accent-tertiary: {state.accent_tertiary};\n  --font-base: {state.font_family};\n"
    
    # Phase A: kinetic shapes driven by archetype DNA, not hardcoded list
    kinetic_shapes = ""
    if getattr(state, 'use_kinetic_shapes', True):
        kinetic_shapes = '<div class="absolute inset-0 z-0 opacity-10 pointer-events-none overflow-hidden"><div class="absolute top-10 left-10 w-20 h-20 border-2 border-[var(--slide-text)] rounded-full animate-pulse"></div><div class="absolute bottom-20 right-10 w-32 h-32 border-2 border-[var(--slide-text)] rotate-45 opacity-50"></div><div class="absolute top-1/2 left-1/4 w-4 h-4 bg-[var(--slide-text)] rounded-full"></div></div>'
    
    nav_dots = """<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="['w-1.5 h-1.5 rounded-full transition-all duration-300', i === $nav.currentPage ? 'bg-[var(--accent-primary)] w-4' : 'bg-[var(--slide-text)] opacity-50']"></div></div>"""
    backdrop_html = '<CinematicBackdrop v-model:url="$frontmatter.bg_video_url" :url="$frontmatter.bg_video_url" />' if content.bg_video_url else ''
    
    # Phase A: append variant class (e.g. 'variant-red') when energy threshold met
    variant = getattr(state, 'variant_class', '')
    slide_class = f"{archetype} {variant}".strip()
    
    clean_inner_html = "\n".join([line for line in inner_html.split("\n") if line.strip()])
    elements_str = "\n".join([e for e in [fonts, backdrop_html, kinetic_shapes, nav_dots, clean_inner_html] if e.strip()])
    
    return f"---\nlayout: {layout}\nclass: {slide_class}{bg_video_fm}\nstyle: |\n{css_vars}---\n{elements_str}\n"

def render_cover(c: SlideContent, archetype: str, state: 'ComputedSlideState' = None) -> str:
    from .orchestrator import orchestrate_slide
    if state is None: state = orchestrate_slide(c, archetype)
    inner = f"""
  <div v-motion {get_motion_props(c.energy, 0)}>{_pill(c.module, state)}</div>
  <h1 v-motion {get_motion_props(c.energy, 1)} style="{get_dynamic_title_style(c.title, True)}">{c.title}</h1>
  <div v-motion {get_motion_props(c.energy, 2)} style="{get_dynamic_desc_style(c.subtitle, True)}">{c.subtitle}</div>
"""
    return _base_slide(c, archetype, _wrapper(inner, state, center=True), "center", state)

def render_section_intro(c: SlideContent, archetype: str, state: 'ComputedSlideState' = None) -> str:
    from .orchestrator import orchestrate_slide
    if state is None: state = orchestrate_slide(c, archetype)
    inner = f"""
  <div v-motion {get_motion_props(c.energy, 0)} style="font-size:4rem;margin-bottom:1rem;">{c.emoji}</div>
  <div v-motion {get_motion_props(c.energy, 1)}>{_pill(c.module, state)}</div>
  <h1 v-motion {get_motion_props(c.energy, 2)} style="{get_dynamic_title_style(c.title, True)}text-transform:uppercase;">{c.title}</h1>
  <div v-motion {get_motion_props(c.energy, 3)} style="{get_dynamic_desc_style(c.description, True)}">{c.description}</div>
"""
    return _base_slide(c, archetype, _wrapper(inner, state, center=True), "center", state)

def render_data_point(c: SlideContent, archetype: str, state: 'ComputedSlideState' = None) -> str:
    from .orchestrator import orchestrate_slide
    if state is None: state = orchestrate_slide(c, archetype)
    inner = f"""
  <div v-motion {get_motion_props(c.energy, 0)}>{_pill(c.module, state)}</div>
  <div v-motion {get_motion_props(c.energy, 1)}>{_stat(c.stat_value, state)}</div>
  <div v-motion {get_motion_props(c.energy, 2)} style="font-size:2rem;font-weight:900;text-transform:uppercase;letter-spacing:2px;">{c.stat_label}</div>
  <div v-motion {get_motion_props(c.energy, 3)} style="{get_dynamic_desc_style(c.description, True)}margin-top:1.5rem;">{c.description}</div>
"""
    return _base_slide(c, archetype, _wrapper(inner, state, center=True), "default", state)

def render_concept(c: SlideContent, archetype: str, state: 'ComputedSlideState' = None) -> str:
    from .orchestrator import orchestrate_slide
    if state is None: state = orchestrate_slide(c, archetype)
    footer_card = f"""
  <div v-click style="margin-top:auto;padding:1.5rem;background:color-mix(in srgb,var(--slide-text) 5%,transparent);border-left:4px solid var(--accent-primary);border-radius:8px;">
    <div style="font-size:2rem;margin-bottom:0.5rem;">{c.emoji}</div>
    <div style="font-weight:700;">{c.subtitle}</div>
  </div>""" if (c.emoji or c.subtitle) else ""

    inner = f"""
  {_pill(c.module, state)}
  <h1 style="{get_dynamic_title_style(c.title)}">{c.title}</h1>
  <div style="{get_dynamic_desc_style(c.description)}max-width:100%;">{c.description}</div>
  {footer_card}
"""
    return _base_slide(c, archetype, _wrapper(inner, state), "default", state)

def render_comparison(c: SlideContent, archetype: str, state: 'ComputedSlideState' = None) -> str:
    from .orchestrator import orchestrate_slide
    if state is None: state = orchestrate_slide(c, archetype)
    if len(c.items) < 2: c.items = ["Item 1", "Item 2"]
    card_a = _card(f"<div style='font-size:3rem;margin-bottom:1rem;'>{c.items[0].split('|')[0] if '|' in c.items[0] else '❌'}</div><div style='font-size:1.2rem;font-weight:800;'>{c.items[0].split('|')[-1]}</div>", state, "display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;")
    card_b = _card(f"<div style='font-size:3rem;margin-bottom:1rem;'>{c.items[1].split('|')[0] if '|' in c.items[1] else '✅'}</div><div style='font-size:1.2rem;font-weight:800;'>{c.items[1].split('|')[-1]}</div>", state, "display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;")
    inner = f"""
  {_pill(c.module, state)}
  <h1 style="{get_dynamic_title_style(c.title, True)}">{c.title}</h1>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:2rem;width:100%;margin-top:2rem;flex:1;">
    {card_a}
    {card_b}
  </div>
"""
    return _base_slide(c, archetype, _wrapper(inner, state), "default", state)

def render_process(c: SlideContent, archetype: str, state: 'ComputedSlideState' = None) -> str:
    from .orchestrator import orchestrate_slide
    if state is None: state = orchestrate_slide(c, archetype)
    items_html = ""
    for i, item in enumerate(c.items):
        items_html += f'<div v-click style="display:flex;gap:1.5rem;align-items:flex-start;margin-bottom:1rem;"><div style="font-size:1.5rem;font-weight:900;color:var(--accent-primary);opacity:0.8;">{i+1:02d}</div>{_card(item, state, "padding:1rem;")}</div>'
    inner = f"""
  {_pill(c.module, state)}
  <h1 style="{get_dynamic_title_style(c.title)}">{c.title}</h1>
  <div style="{get_dynamic_desc_style(c.description)}">{c.description}</div>
  <div style="margin-top:1rem;width:100%;">{items_html}</div>
"""
    return _base_slide(c, archetype, _wrapper(inner, state), "default", state)

def render_feature_grid(c: SlideContent, archetype: str, state: 'ComputedSlideState' = None) -> str:
    from .orchestrator import orchestrate_slide
    if state is None: state = orchestrate_slide(c, archetype)
    items_html = ""
    for i, item in enumerate(c.items[:4]):
        parts = item.split('|')
        idx_label = f'<div style="font-size:0.8rem;color:var(--accent-primary);font-weight:900;">{i+1:02}</div>'
        text = parts[-1]
        items_html += _card(f'{idx_label}<div style="font-weight:700;font-size:1.1rem;">{text}</div>', state, "display:flex;flex-direction:column;gap:0.3rem;")
    inner = f"""
  {_pill(c.module, state)}
  <h1 style="{get_dynamic_title_style(c.title)}">{c.title}</h1>
  <div style="{get_dynamic_desc_style(c.description)}">{c.description}</div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;width:100%;margin-top:1rem;flex:1;">{items_html}</div>
"""
    return _base_slide(c, archetype, _wrapper(inner, state), "default", state)

def render_quote(c: SlideContent, archetype: str, state: 'ComputedSlideState' = None) -> str:
    from .orchestrator import orchestrate_slide
    if state is None: state = orchestrate_slide(c, archetype)
    inner = f"""
  <div style="font-size:5rem;color:var(--accent-primary);opacity:0.5;margin-bottom:-2rem;font-family:serif;">"</div>
  <div v-motion :initial="{{opacity:0}}" :enter="{{opacity:1}}" style="{get_dynamic_desc_style(c.quote_text, True)}font-size:2.5rem;font-weight:700;font-style:italic;line-height:1.3;max-width:80%;">{c.quote_text}</div>
  <div v-motion :initial="{{opacity:0,y:10}}" :enter="{{opacity:1,y:0}}" style="margin-top:2rem;font-size:1.2rem;font-weight:600;text-transform:uppercase;letter-spacing:2px;">— {c.quote_author}</div>
"""
    return _base_slide(c, archetype, _wrapper(inner, state, center=True), "center", state)

def render_agenda(c: SlideContent, archetype: str, state: 'ComputedSlideState' = None) -> str:
    from .orchestrator import orchestrate_slide
    if state is None: state = orchestrate_slide(c, archetype)
    items_html = ""
    for idx, item in enumerate(c.items):
        items_html += f'<div v-click v-motion {get_motion_props(c.energy, idx+2)} @click="$nav.go($nav.currentPage + {idx+1})" style="background:color-mix(in srgb,var(--slide-text) 5%,transparent);border:1px solid color-mix(in srgb,var(--slide-text) 10%,transparent);padding:1.5rem;border-radius:16px;cursor:pointer;transition:all 0.3s ease;pointer-events:auto;"><div style="font-size:0.8rem;opacity:0.5;font-weight:900;margin-bottom:0.5rem;">0{idx+1}</div><div style="font-size:1.2rem;font-weight:900;">{item}</div></div>'
    inner = f"""
  <div v-motion {get_motion_props(c.energy, 0)}>{_pill(c.module, state)}</div>
  <h1 v-motion {get_motion_props(c.energy, 1)} style="{get_dynamic_title_style(c.title)}">{c.title}</h1>
  <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:1.5rem;margin-top:2rem;">{items_html}</div>
"""
    return _base_slide(c, archetype, _wrapper(inner, state), "default", state)

def render_cycle(c: SlideContent, archetype: str, state: 'ComputedSlideState' = None) -> str:
    from .orchestrator import orchestrate_slide
    if state is None: state = orchestrate_slide(c, archetype)
    bounds = get_cycle_bounds(len(c.items), c.title)
    count = min(len(c.items), 6) or 1
    radius, node_size = bounds["radius"], bounds["node_size"]
    items_html = ""
    for i, item in enumerate(c.items[:6]):
        angle = (i / count) * 360
        items_html += f'<div style="position:absolute;left:50%;top:50%;transform:rotate({angle}deg) translate({radius}px) rotate(-{angle}deg);pointer-events:none;z-index:10;"><div v-click v-motion {get_motion_props(c.energy, i+2)} style="width:{node_size}px;height:{node_size}px;margin-left:-{node_size/2}px;margin-top:-{node_size/2}px;background:color-mix(in srgb,var(--slide-bg) 90%,transparent);border:2px solid color-mix(in srgb,var(--accent-primary) {100 - i*15}%,transparent);border-radius:50%;display:flex;align-items:center;justify-content:center;text-align:center;padding:1rem;font-size:0.7rem;font-weight:800;box-shadow:0 0 20px color-mix(in srgb,var(--accent-primary) 30%,transparent);pointer-events:auto;backdrop-filter:blur(10px);">{item}</div></div>'
    inner = f"""
  <div v-motion {get_motion_props(c.energy, 0)}>{_pill(c.module, state)}</div>
  <h1 v-motion {get_motion_props(c.energy, 1)} style="{get_dynamic_title_style(c.title)}">{c.title}</h1>
  <div style="flex:1;position:relative;width:100%;display:flex;align-items:center;justify-content:center;margin-top:{bounds['margin_top_px']}px;margin-bottom:40px;">
    <div v-motion :initial="{{scale:0}}" :enter="{{scale:1,transition:{{type:'spring',delay:500}}}}" style="width:{node_size*0.7}px;height:{node_size*0.7}px;background:var(--accent-primary);border-radius:50%;z-index:20;display:flex;align-items:center;justify-content:center;box-shadow:0 0 40px var(--accent-primary);pointer-events:auto;"><div style="color:black;font-weight:900;font-size:0.5rem;text-transform:uppercase;letter-spacing:1px;text-align:center;">{c.module}</div></div>
    <div style="position:absolute;width:{radius*2}px;height:{radius*2}px;border:1px dashed color-mix(in srgb,var(--slide-text) 20%,transparent);border-radius:50%;pointer-events:none;z-index:1;"></div>
    {items_html}
  </div>
"""
    return _base_slide(c, archetype, _wrapper(inner, state), "default", state)

def render_chart(c: SlideContent, archetype: str, state: 'ComputedSlideState' = None) -> str:
    from .orchestrator import orchestrate_slide
    if state is None: state = orchestrate_slide(c, archetype)
    option = {
        "backgroundColor": "transparent",
        "tooltip": {"trigger": "axis"},
        "xAxis": {"type": "category", "data": [d.get("name", "") for d in c.chart_data], "axisLabel": {"color": state.slide_text}},
        "yAxis": {"type": "value", "axisLabel": {"color": state.slide_text}, "splitLine": {"lineStyle": {"color": "rgba(128,128,128,0.2)"}}},
        "series": [{"data": [d.get("value", 0) for d in c.chart_data], "type": c.chart_type or "bar", "itemStyle": {"color": "var(--accent-primary)"}, "areaStyle": {"opacity": 0.3} if c.chart_type == "line" else None}]
    }
    inner = f"""
  {_pill(c.module, state)}
  <h1 style="{get_dynamic_title_style(c.title)}">{c.title}</h1>
  <div style="{get_dynamic_desc_style(c.description)}">{c.description}</div>
  <div style="flex:1;min-height:0;width:100%;margin-top:1rem;"><v-chart :option='{json.dumps(option)}' autoresize style="width:100%;height:100%;" /></div>
"""
    return _base_slide(c, archetype, _wrapper(inner, state), "default", state)

def render_table(c: SlideContent, archetype: str, state: 'ComputedSlideState' = None) -> str:
    from .orchestrator import orchestrate_slide
    if state is None: state = orchestrate_slide(c, archetype)
    headers = "".join([f"<th style='padding:1rem;text-align:left;border-bottom:2px solid color-mix(in srgb,var(--slide-text) 20%,transparent);text-transform:uppercase;font-size:0.8rem;'>{h}</th>" for h in c.table_headers])
    rows = "".join([f"<tr style='background:{'color-mix(in srgb,var(--slide-text) 3%,transparent)' if i%2==0 else 'transparent'};'>" + "".join([f"<td style='padding:1rem;border-bottom:1px solid color-mix(in srgb,var(--slide-text) 5%,transparent);'>{cell}</td>" for cell in row]) + "</tr>" for i, row in enumerate(c.table_rows)])
    inner = f"""
  {_pill(c.module, state)}
  <h1 style="{get_dynamic_title_style(c.title)}">{c.title}</h1>
  <div style="margin-top:1.5rem;width:100%;overflow:hidden;border-radius:12px;border:1px solid color-mix(in srgb,var(--slide-text) 10%,transparent);background:rgba(0,0,0,0.2);"><table style="width:100%;border-collapse:collapse;font-size:1.1rem;"><thead><tr style="background:color-mix(in srgb,var(--slide-text) 5%,transparent);">{headers}</tr></thead><tbody>{rows}</tbody></table></div>
"""
    return _base_slide(c, archetype, _wrapper(inner, state), "default", state)

def render_media_focus(c: SlideContent, archetype: str, state: 'ComputedSlideState' = None) -> str:
    from .orchestrator import orchestrate_slide
    if state is None: state = orchestrate_slide(c, archetype)
    yt_reg = r'^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*'
    match = re.match(yt_reg, c.media_url) if c.media_url else None
    yt_id = match.group(2) if match and len(match.group(2)) == 11 else None
    media_tag = f"<iframe src='https://www.youtube.com/embed/{yt_id}?controls=1&rel=0' style='width:100%;height:100%;border:none;border-radius:12px;'></iframe>" if yt_id else f"<video src='{c.media_url}' controls autoplay loop muted style='width:100%;height:100%;object-fit:cover;border-radius:12px;'></video>" if c.media_type == "video" else f"<img src='{c.media_url}' style='width:100%;height:100%;object-fit:cover;border-radius:12px;' />"
    cta = f'<a href="{c.cta_link}" v-motion {get_motion_props(c.energy, 3)} style="margin-top:2rem;padding:1rem 2rem;background:var(--accent-primary);color:var(--slide-bg);font-weight:900;text-decoration:none;border-radius:50px;width:fit-content;">{c.cta_text}</a>' if c.cta_text else ""
    inner = f"""
  <div style="display:flex;width:100%;height:100%;gap:3rem;">
    <div style="flex:1;display:flex;flex-direction:column;justify-content:center;">
      <div v-motion {get_motion_props(c.energy, 0)}>{_pill(c.module, state)}</div>
      <h1 v-motion {get_motion_props(c.energy, 1)} style="{get_dynamic_title_style(c.title)}">{c.title}</h1>
      <div v-motion {get_motion_props(c.energy, 2)} style="{get_dynamic_desc_style(c.description)}">{c.description}</div>
      {cta}
    </div>
    <div v-motion :initial="{{opacity:0,x:50}}" :enter="{{opacity:1,x:0}}" style="flex:1.2;padding:1rem;">{media_tag}</div>
  </div>
"""
    return _base_slide(c, archetype, _wrapper(inner, state), "default", state)

def render_activity(c: SlideContent, archetype: str, state: 'ComputedSlideState' = None) -> str:
    from .orchestrator import orchestrate_slide
    if state is None: state = orchestrate_slide(c, archetype)
    inner = f"""
  <div style="display:inline-block;padding:4px 16px;border-radius:4px;font-size:10px;font-weight:900;letter-spacing:2px;text-transform:uppercase;margin-bottom:0.8rem;background:rgba(255,0,0,0.2);border:1px solid rgba(255,0,0,0.5);color:#ff9999;">ACTIVITY BREAK</div>
  <div style="font-size:4rem;margin-bottom:1rem;">{c.emoji}</div>
  <h1 style="{get_dynamic_title_style(c.title, True)}">{c.title}</h1>
  {_card(c.description, state, "max-width:70%;margin:2rem auto;font-size:1.5rem;font-weight:700;")}
"""
    return _base_slide(c, archetype, _wrapper(inner, state, center=True), "center", state)

def render_case_study(c: SlideContent, archetype: str, state: 'ComputedSlideState' = None) -> str:
    from .orchestrator import orchestrate_slide
    if state is None: state = orchestrate_slide(c, archetype)
    inner = f"""
  <div style="display:flex;width:100%;height:100%;gap:3rem;">
    <div style="flex:1.2;display:flex;flex-direction:column;">
      {_pill(c.module, state)}
      <h1 style="{get_dynamic_title_style(c.title)}">{c.title}</h1>
      <div style="{get_dynamic_desc_style(c.description)}">{c.description}</div>
      <div v-click style="margin-top:auto;padding:1.5rem;background:color-mix(in srgb,var(--slide-text) 5%,transparent);border-radius:8px;border-left:4px solid var(--accent-primary);">
        <span style="font-weight:900;font-size:0.8rem;opacity:0.5;">CASE HIGHLIGHT</span><br/>
        <div style="font-size:1.1rem;font-weight:700;margin-top:0.5rem;">{c.subtitle}</div>
      </div>
    </div>
    <div v-click style="flex:0.8;background:color-mix(in srgb,var(--slide-text) 3%,transparent);border-radius:12px;border:1px dashed color-mix(in srgb,var(--slide-text) 10%,transparent);display:flex;align-items:center;justify-content:center;padding:2rem;">
      <div style="text-align:center;"><div style="font-size:5rem;margin-bottom:1rem;">{c.emoji}</div><div style="font-weight:900;letter-spacing:2px;">{_stat(c.stat_value, state)}</div><div style="opacity:0.6;font-size:0.9rem;">{c.stat_label}</div></div>
    </div>
  </div>
"""
    return _base_slide(c, archetype, _wrapper(inner, state), "default", state)

def render_finale(c: SlideContent, archetype: str, state: 'ComputedSlideState' = None) -> str:
    from .orchestrator import orchestrate_slide
    if state is None: state = orchestrate_slide(c, archetype)
    inner = f"""
  <h1 v-motion {get_motion_props(c.energy, 0)} style="{get_dynamic_title_style(c.title, True)}">{c.title}</h1>
  <div v-motion {get_motion_props(c.energy, 1)} style="font-size:1.5rem;opacity:0.8;">{c.subtitle}</div>
"""
    return _base_slide(c, archetype, _wrapper(inner, state, center=True), "center", state)

TEMPLATE_REGISTRY = {
    "cover": render_cover, "agenda": render_agenda, "section_intro": render_section_intro,
    "concept": render_concept, "comparison": render_comparison, "data_point": render_data_point,
    "process": render_process, "feature_grid": render_feature_grid, "quote": render_quote,
    "activity": render_activity, "case_study": render_case_study, "cycle": render_cycle,
    "chart": render_chart, "table": render_table, "media_focus": render_media_focus, "finale": render_finale
}

def render_slide(c: SlideContent, archetype: str, state: 'ComputedSlideState' = None, index: int = 0) -> str:
    from .orchestrator import orchestrate_slide
    state = orchestrate_slide(c, archetype, index)
    return TEMPLATE_REGISTRY.get(c.content_type, render_concept)(c, archetype, state)
