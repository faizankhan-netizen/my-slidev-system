from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class SlideContent:
    # Identity
    content_type: str
    title: str
    subtitle: str = ""
    
    # Narrative Position
    act: int = 1
    module: str = ""
    position: str = "body" # opener, body, closer, bridge
    
    # Content Payload
    description: str = ""
    items: List[str] = field(default_factory=list)
    stat_value: str = ""
    stat_label: str = ""
    quote_text: str = ""
    quote_author: str = ""
    emoji: str = "✨"
    
    # NEW V3: Multi-Modal Payloads
    chart_type: str = "" # bar, line, pie, radar
    chart_data: List[dict] = field(default_factory=list)
    table_headers: List[str] = field(default_factory=list)
    table_rows: List[List[str]] = field(default_factory=list)
    media_url: str = ""
    media_type: str = "image" # image, video, iframe
    flow_type: str = "" # cycle, process, hierarchy
    cta_text: str = ""
    cta_link: str = ""
    bg_video_url: str = ""
    
    # Design Hints
    energy: str = "medium" # calm, medium, high
    bg_tone: str = "dark" # dark, light
