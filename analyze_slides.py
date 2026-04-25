import sys, re, os
sys.stdout.reconfigure(encoding='utf-8')

# PPTX EMU conversion constants
# Slide: 9144000 EMU wide x 5143500 EMU tall = 10" x 5.625"
# Slidev canvas: 900px wide x ~506px tall (16:9)
W_EMU = 9144000
H_EMU = 5143500
W_PX = 900
H_PX = 506

def emu_to_px_x(v): return round(int(v) / W_EMU * W_PX)
def emu_to_px_y(v): return round(int(v) / H_EMU * H_PX)
def pt(sz): return round(int(sz) / 100)  # sz in hundredths of a point

for i in range(1, 6):
    path = f'temp_pptx/ppt/slides/slide{i}.xml'
    if not os.path.exists(path):
        print(f'slide{i}: NOT FOUND'); continue
    with open(path, encoding='utf-8') as f:
        xml = f.read()

    print(f'\n{"="*60}')
    print(f'SLIDE {i}')
    print(f'{"="*60}')

    # Extract all shapes with position, size, text, font info
    shapes = re.findall(r'<p:sp>(.*?)</p:sp>', xml, re.DOTALL)
    for sp in shapes:
        name_m = re.search(r'id="\d+" name="([^"]+)"', sp)
        name = name_m.group(1) if name_m else '?'
        off_m = re.search(r'<a:off x="(\d+)" y="(\d+)"', sp)
        ext_m = re.search(r'<a:ext cx="(\d+)" cy="(\d+)"', sp)
        texts = re.findall(r'<a:t>(.+?)</a:t>', sp)
        sz_m = re.findall(r'sz="(\d+)"', sp)
        bold_m = re.findall(r'b="(\d+)"', sp)
        color_m = re.findall(r'srgbClr val="([A-Fa-f0-9]{6})"', sp)
        if not off_m: continue
        x, y = emu_to_px_x(off_m.group(1)), emu_to_px_y(off_m.group(2))
        if ext_m:
            w, h = emu_to_px_x(ext_m.group(1)), emu_to_px_y(ext_m.group(2))
        else:
            w, h = 0, 0
        if texts:
            sizes_pt = [pt(s) for s in sz_m] if sz_m else []
            print(f'  [{name}] x={x}px y={y}px w={w}px h={h}px | font={sizes_pt}pt bold={bold_m} color={color_m}')
            print(f'    TEXT: {texts}')
