import os

filepath = r"d:\my-slides\slidev\scripts\slide_engine\templates.py"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Replace _base_slide to remove empty lines that break Slidev's markdown parser
import re

new_base_slide = """def _base_slide(content: SlideContent, archetype: str, inner_html: str, layout: str = "default", state: 'ComputedSlideState' = None) -> str:
    if state is None:
        from .orchestrator import orchestrate_slide
        state = orchestrate_slide(content, archetype)
    
    bg_video_fm = f"\\nbg_video_url: {content.bg_video_url}" if content.bg_video_url else ""
    
    css_vars = f"  --slide-bg: {state.slide_bg};\\n  --slide-text: {state.slide_text};\\n  --accent-primary: {state.accent_color};\\n  --accent-secondary: {state.accent_secondary};\\n  --accent-tertiary: {state.accent_tertiary};\\n  --font-base: {state.font_family};\\n"
    
    kinetic_shapes = ""
    if archetype in ["style-school", "style-business", "style-cyber", "default"]:
        kinetic_shapes = '<div class="absolute inset-0 z-0 opacity-10 pointer-events-none overflow-hidden"><div class="absolute top-10 left-10 w-20 h-20 border-2 border-[var(--slide-text)] rounded-full animate-pulse"></div><div class="absolute bottom-20 right-10 w-32 h-32 border-2 border-[var(--slide-text)] rotate-45 opacity-50"></div><div class="absolute top-1/2 left-1/4 w-4 h-4 bg-[var(--slide-text)] rounded-full"></div></div>'
    
    nav_dots = '<div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2 opacity-30 hover:opacity-100 transition-opacity duration-500 z-50"><div v-for="i in $nav.total" :key="i" :class="[\\'w-1.5 h-1.5 rounded-full transition-all duration-300\\', i === $nav.currentPage ? \\'bg-[var(--accent-primary)] w-4\\' : \\'bg-[var(--slide-text)] opacity-50\\']"></div></div>'
    
    fonts = '<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;700&family=Montserrat:wght@400;900&display=swap" rel="stylesheet" />'
    backdrop_html = '<CinematicBackdrop v-model:url="$frontmatter.bg_video_url" :url="$frontmatter.bg_video_url" />' if content.bg_video_url else ''
    
    # Strip blank lines from inner_html to prevent Slidev markdown parser from breaking HTML blocks
    clean_inner_html = "\\n".join([line for line in inner_html.split("\\n") if line.strip()])
    
    elements = [fonts, backdrop_html, kinetic_shapes, nav_dots, clean_inner_html]
    elements_str = "\\n".join([e for e in elements if e.strip()])
    
    return f"---\\nlayout: {layout}\\nclass: {archetype}{bg_video_fm}\\nstyle: |\\n{css_vars}---\\n{elements_str}\\n"
"""

# Extract everything before `def _base_slide` and everything after its return statement
# Use regex to replace the function
pattern = re.compile(r"def _base_slide\(.*?return f\"\"\"[^\"]*\"\"\"[ \n]*", re.DOTALL)
content = pattern.sub(new_base_slide + "\n", content)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully patched templates.py")
