import os
import xml.etree.ElementTree as ET
import sys

# Ensure UTF-8 output
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

def extract_text(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        text = []
        for t in root.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}t'):
            if t.text:
                text.append(t.text)
        return " ".join(text)
    except Exception as e:
        return f"Error reading {xml_file}: {e}"

slides_dir = 'temp_pptx/ppt/slides'
if not os.path.exists(slides_dir):
    print(f"Directory not found: {slides_dir}")
else:
    slides = [f for f in os.listdir(slides_dir) if f.endswith('.xml')]
    slides.sort(key=lambda x: int(x.replace('slide', '').replace('.xml', '')) if x.replace('slide', '').replace('.xml', '').isdigit() else 0)

    for slide in slides:
        slide_num = slide.replace('slide', '').replace('.xml', '')
        print(f"Slide {slide_num}:")
        content = extract_text(os.path.join(slides_dir, slide))
        print(content)
        print("-" * 20)
