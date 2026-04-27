import sys
import os

sys.path.append(os.path.join(os.getcwd(), 'scripts'))

from slide_engine.schema import SlideContent
from slide_engine.renderer import Pipeline

def generate():
    """
    Sample Research/Dissertation Deck Generator.
    Topic: Relationship between Happiness and Gratitude
    Auto-resolves to: style-research
    """
    engine = Pipeline(
        topic="Dissertation: Happiness, Gratitude and Forgiveness — A Correlational Study",
        audience="researchers",
        tone="academic"
    )

    slides = [
        # 1. Cover Slide
        SlideContent(
            content_type="cover",
            module="DISSERTATION DEFENSE",
            title="Happiness, Gratitude & Forgiveness",
            subtitle="A Correlational Study Among University Students",
            energy="high"
        ),

        # 2. Abstract
        SlideContent(
            content_type="quote",
            title="\"What we measure defines what we pursue.\"",
            description="— Hadley Cantril | This study examines the empirical relationship between subjective happiness, dispositional gratitude, and heartland forgiveness across a sample of 120 undergraduate students.",
            module="ABSTRACT",
            energy="calm"
        ),

        # 3. Research Objectives
        SlideContent(
            content_type="concept",
            module="OBJECTIVES",
            title="Research Objectives",
            subtitle="Three Guiding Hypotheses",
            description="H₁: Gratitude significantly predicts Happiness. H₂: Forgiveness is positively correlated with Happiness. H₃: Gratitude mediates the relationship between Forgiveness and Happiness.",
            emoji="🎯",
            energy="standard"
        ),

        # 4. Methodology
        SlideContent(
            content_type="process",
            module="METHODOLOGY",
            title="Research Design",
            description="Quantitative correlational design. Three validated psychometric instruments were administered to a purposive sample.",
            items=[
                "Subjective Happiness Scale (SHS) — 4 items | Lyubomirsky & Lepper (1999)",
                "Gratitude Questionnaire-6 (GQ-6) — 6 items | McCullough et al. (2002)",
                "Heartland Forgiveness Scale (HFS) — 18 items | Thompson et al. (2005)"
            ],
            energy="standard"
        ),

        # 5. Sample Demographics
        SlideContent(
            content_type="data_point",
            module="SAMPLE",
            title="Study Demographics",
            description="University students across disciplines",
            stat_value="N = 120",
            stat_label="Participants",
            energy="high"
        ),

        # 6. Key Findings
        SlideContent(
            content_type="concept",
            module="FINDINGS",
            title="Key Findings",
            subtitle="Pearson Correlation Results",
            description="A statistically significant positive correlation was found between Gratitude and Happiness (r = 0.67, p < 0.01). Forgiveness showed a moderate positive correlation with Happiness (r = 0.48, p < 0.01). H₁, H₂ and H₃ were all supported at the 0.01 significance level.",
            emoji="📊",
            energy="high"
        ),

        # 7. Conclusion
        SlideContent(
            content_type="section_intro",
            module="CONCLUSION",
            title="Implications for Practice",
            description="Cultivating gratitude through structured interventions may serve as an effective psychological lever for improving subjective well-being in student populations.",
            emoji="🌿",
            energy="standard"
        ),

        # 8. References / Finale
        SlideContent(
            content_type="finale",
            module="THANK YOU",
            title="Open for Questions",
            subtitle="A Study Submitted in Partial Fulfillment of the Requirements for the Degree of Master of Science in Psychology",
            energy="high"
        )
    ]

    md = engine.render(slides)
    with open("presentations/dissertation_demo.md", "w", encoding="utf-8") as f:
        f.write(md)
    with open("slides.md", "w", encoding="utf-8") as f:
        f.write(md)

    # Print resolved archetype
    from slide_engine.topic_analyzer import TopicAnalyzer
    resolved = TopicAnalyzer().resolve(
        "Dissertation: Happiness, Gratitude and Forgiveness — A Correlational Study",
        audience="researchers",
        tone="academic"
    )
    print(f"Successfully generated Research dissertation demo.")
    print(f"Resolved Archetype: {resolved}")

if __name__ == "__main__":
    generate()
