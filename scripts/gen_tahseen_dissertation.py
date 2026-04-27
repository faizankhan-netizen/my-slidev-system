import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.getcwd(), 'scripts'))

from slide_engine.schema import SlideContent
from slide_engine.renderer import Pipeline

def generate():
    engine = Pipeline(
        topic="Dissertation: Forgiveness, Gratitude, Psychological Well-Being and Happiness among College Students",
        audience="researchers",
        tone="academic"
    )

    slides = [
        # 1. Cover
        SlideContent(
            content_type="cover",
            module="DISSERTATION DEFENSE",
            title="Forgiveness, Gratitude & Happiness",
            subtitle="A Correlational Study on Psychological Well-Being Among College Students\n\nTahseen Fatima (24039000098) · Dept. of Psychology · 2024–2025",
            energy="high",
            custom_bg="#1B2333"
        ),

        # 2. Introduction
        SlideContent(
            content_type="concept",
            module="INTRODUCTION",
            title="Resilience & Well-Being",
            subtitle="Study Rationale",
            description="Investigating how trait forgiveness acts as a psychological lever to enhance well-being and happiness during the high-stress transition of college life.",
            emoji="🎓",
            energy="standard"
        ),

        # 3. Construct Definitions
        SlideContent(
            content_type="feature_grid",
            module="CONSTRUCTS",
            title="The Four Study Variables",
            description="Standardized psychological constructs used in the analysis.",
            items=[
                "Forgiveness|Letting go of resentment toward offenders (HFS).",
                "Well-Being|Ryff's 6 dimensions of optimal functioning.",
                "Happiness|Subjective satisfaction and positive affect.",
                "Gratitude|Recognition and appreciation of life's positives."
            ],
            energy="standard"
        ),

        # 4. Hypotheses Part 1 (SPLIT TO PREVENT BLEED)
        SlideContent(
            content_type="custom",
            module="HYPOTHESES (1/2)",
            title="Core Research Hypotheses",
            description="""
<div class="smart-art-stack">
  <div class="hypothesis-box" v-click>
    <div class="hypothesis-tag">Hypothesis 1</div>
    <div class="hypothesis-text">Forgiveness is positively and significantly correlated with psychological well-being.</div>
  </div>
  <div class="hypothesis-box" v-click>
    <div class="hypothesis-tag">Hypothesis 2</div>
    <div class="hypothesis-text">Forgiveness is positively and significantly correlated with happiness.</div>
  </div>
</div>
""",
            energy="high",
            custom_bg="#FAFAF8"
        ),

        # 5. Hypotheses Part 2
        SlideContent(
            content_type="custom",
            module="HYPOTHESES (2/2)",
            title="Core Research Hypotheses",
            description="""
<div class="smart-art-stack">
  <div class="hypothesis-box" v-click>
    <div class="hypothesis-tag">Hypothesis 3</div>
    <div class="hypothesis-text">Forgiveness is positively correlated with gratitude.</div>
  </div>
  <div class="hypothesis-box" v-click>
    <div class="hypothesis-tag">Hypothesis 4</div>
    <div class="hypothesis-text">PWB, happiness, and gratitude will be significantly intercorrelated.</div>
  </div>
</div>
""",
            energy="high",
            custom_bg="#FAFAF8"
        ),

        # 6. Methodology
        SlideContent(
            content_type="process",
            module="METHODOLOGY",
            title="Method & Participants",
            description="Cross-sectional correlational approach.",
            items=[
                "Sample: 100 college students.",
                "Sampling: Purposive Sampling technique.",
                "Design: Correlational quantitative study.",
                "Platform: Google Forms online survey."
            ],
            energy="standard"
        ),

        # 7. Measures
        SlideContent(
            content_type="feature_grid",
            module="MEASURES",
            title="Psychometric Tools",
            description="Validated scales for reliable data collection.",
            items=[
                "HFS|Heartland Forgiveness Scale (α=0.87).",
                "Ryff's PWB|6-dimension well-being scale.",
                "SHS|Subjective Happiness Scale (α=0.86).",
                "GQ-6|Gratitude Questionnaire (α=0.82)."
            ],
            energy="standard"
        ),

        # 8. Key Findings
        SlideContent(
            content_type="case_study",
            module="FINDINGS",
            title="Statistical Analysis",
            subtitle="Results Overview",
            description="Significant positive correlations found across all variables (p < 0.05). Forgiveness is a key predictor of student well-being.",
            stat_value="p < 0.05",
            stat_label="Significant",
            emoji="📊",
            energy="high",
            custom_bg="#1B5E4F"
        ),

        # 9. Finale
        SlideContent(
            content_type="finale",
            module="CONCLUSION",
            title="Thank You",
            subtitle="Tahseen Fatima · Psychology Dissertation 2025",
            energy="high",
            custom_bg="#1B2333"
        )
    ]

    md = engine.render(slides)
    with open("presentations/tahseen_dissertation_v4.md", "w", encoding="utf-8") as f:
        f.write(md)
    with open("slides.md", "w", encoding="utf-8") as f:
        f.write(md)

    print(f"Successfully generated Tahseen's dissertation (V4 - Correct Layout).")

if __name__ == "__main__":
    generate()
