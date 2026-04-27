import os
import sys
import json
import re

# Ensure we can import the slide_engine
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from slide_engine import Pipeline, SlideContent

CONTENT_TYPES = [
    "cover", "agenda", "section_intro", "concept", "comparison", 
    "data_point", "process", "feature_grid", "quote", "activity", 
    "case_study", "cycle", "chart", "table", "media_focus", "finale"
]

ARCHETYPES = [
    "style-school", "style-business", "style-editorial", "style-luxury",
    "style-eco", "style-cyber", "style-space", "style-industrial", "style-workshop"
]

def make_sample_slide(content_type: str) -> SlideContent:
    """Creates a sample SlideContent for testing."""
    s = SlideContent(
        title=f"Test {content_type.replace('_', ' ').title()}",
        module="V5 MATRIX TEST",
        content_type=content_type,
        description=f"This is a visual regression test for the '{content_type}' layout in the Cinematic Engine V5.",
        energy="standard"
    )
    
    # Add type-specific data
    if content_type == "cover":
        s.subtitle = "Ensuring Design Sovereignty"
    elif content_type == "data_point":
        s.stat_value = "99.9%"
        s.stat_label = "Uptime"
    elif content_type == "comparison":
        s.items = ["❌ Legacy Inline Styles|Hardcoded", "✅ V5 Design Sovereignty|Class-based"]
    elif content_type in ["process", "feature_grid", "agenda", "cycle"]:
        s.items = ["Step 1|Initial Setup", "Step 2|Refactor Logic", "Step 3|Inject Classes", "Step 4|Final Render"]
    elif content_type == "quote":
        s.quote_text = "Design is not just what it looks like and feels like. Design is how it works."
        s.quote_author = "Steve Jobs"
    elif content_type == "chart":
        s.chart_data = [{"name": "A", "value": 10}, {"name": "B", "value": 25}, {"name": "C", "value": 15}]
        s.chart_type = "bar"
    elif content_type == "table":
        s.table_headers = ["Feature", "Status", "Impact"]
        s.table_rows = [["Design DNA", "Passed", "High"], ["Class Mapping", "Passed", "Critical"], ["CSS Control", "Passed", "Total"]]
    elif content_type == "case_study":
        s.subtitle = "V5 Migration Success"
        s.stat_value = "10x"
        s.stat_label = "Cleanliness"
        s.emoji = "🚀"
    elif content_type == "media_focus":
        s.media_url = "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80"
        s.media_type = "image"
        s.cta_text = "Learn More"
        s.cta_link = "#"
        
    return s

def validate_md_output(md: str, archetype: str):
    """
    Smoke test for the generated markdown.
    Checks for unclosed tags and ensures every emitted class="X" 
    actually exists in the archetype's CSS file.
    """
    # 1. Frontmatter check
    assert f"class: {archetype}" in md, f"MISSING ARCHETYPE CLASS: {archetype} not found in output"
    
    # 2. Tag balance check
    opens = len(re.findall(r'<div', md))
    closes = len(re.findall(r'</div', md))
    if opens != closes:
        print(f"  [WARNING] Tag mismatch in {archetype}: {opens} opens vs {closes} closes")

    # 3. CSS Class Presence Check
    # Extract all class names from the markdown
    emitted_classes = set()
    for match in re.findall(r'class="([^"]*)"', md):
        for cls in match.split():
            if cls not in ["fixed", "absolute", "inset-0", "z-0", "z-50", "opacity-10", 
                           "pointer-events-none", "overflow-hidden", "top-10", "left-10",
                           "w-20", "h-20", "border-2", "rounded-full", "animate-pulse",
                           "bottom-20", "right-10", "w-32", "h-32", "rotate-45", "opacity-50",
                           "top-1/2", "left-1/4", "w-4", "h-4", "bg-[var(--slide-text)]",
                           "bottom-4", "left-1/2", "-translate-x-1/2", "flex", "gap-2",
                           "opacity-30", "hover:opacity-100", "transition-opacity", 
                           "duration-500", "w-1.5", "h-1.5", "transition-all", "duration-300",
                           "w-4", "bg-[var(--accent-primary)]"]:
                emitted_classes.add(cls)

    # Load CSS file
    css_name = archetype.replace("style-", "")
    css_path = f"styles/{css_name}.css"
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            css_content = f.read()
            for cls in emitted_classes:
                # Basic check for .classname in CSS
                if f".{cls}" not in css_content and cls != archetype:
                     print(f"  [ORPHAN CLASS] .{cls} not found in {css_path}")
    else:
        print(f"  [WARNING] CSS file not found: {css_path}")

def generate_matrix():
    print("Starting Cinematic Engine V5 Matrix Test...")
    
    output_dir = "presentations"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    total_slides = 0
    
    for archetype in ARCHETYPES:
        print(f"  Processing {archetype}...")
        engine = Pipeline(global_theme=archetype)
        
        slides = [make_sample_slide(ct) for ct in CONTENT_TYPES]
        md = engine.render(slides)
        
        # Validation
        validate_md_output(md, archetype)
        
        # Save output
        filename = f"test_{archetype.replace('style-', '')}.md"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(md)
            
        total_slides += len(slides)
        print(f"    - Generated {len(slides)} slides: {filename}")
        
    print(f"\nMatrix Test Complete! Generated {total_slides} slides across {len(ARCHETYPES)} archetypes.")
    print(f"Output located in /{output_dir}")

if __name__ == "__main__":
    generate_matrix()
