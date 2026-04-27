# Cinematic Engine V5 — Topic Analyzer
# Hierarchical category system with audience + tone boosters.
# Returns the best archetype for a given topic string.
# RULE: keyword bag + audience/tone modifiers. LLM hook reserved for future.

# --- CATEGORY SIGNAL DATABASE ---
CATEGORIES = [
    {
        "archetype": "style-research",
        "signals": [
            "research", "dissertation", "thesis", "study", "paper",
            "journal", "hypothesis", "methodology", "findings", "analysis",
            "literature review", "abstract", "conclusion", "data", "survey",
            "experiment", "correlation", "psychology", "sociology", "statistics",
            "academic", "scholarly", "publish", "citation", "peer review",
            "qualitative", "quantitative", "sample", "respondents", "variable",
            "regression", "significant", "p-value", "mean", "median",
            "proposal", "defense", "chapter", "university", "faculty",
            "phd", "masters", "undergraduate", "department", "professor"
        ],
        "weight": 1.2
    },
    {
        "archetype": "style-editorial",
        "signals": [
            "fashion", "brand", "design", "portfolio", "magazine",
            "photography", "art", "typography", "aesthetic", "runway",
            "couture", "vogue", "style", "editorial", "graphic",
            "visual identity", "print", "layout", "90s", "trend"
        ],
        "weight": 1.0
    },
    {
        "archetype": "style-luxury",
        "signals": [
            "premium", "exclusive", "luxury", "wealth", "jewelry",
            "wine", "antimatter", "quantum", "heritage", "bespoke",
            "elite", "haute", "prestige", "high-end", "opulent",
            "invest", "fine dining", "yacht", "gold", "diamond",
            "khilafah", "caliphate", "civilization", "legacy", "sovereignty"
        ],
        "weight": 1.1
    },
    {
        "archetype": "style-eco",
        "signals": [
            "nature", "organic", "sustainable", "health", "wellness",
            "farming", "poultry", "agriculture", "green", "garden",
            "environment", "climate", "plant", "herbal", "eco",
            "biodiversity", "carbon", "renewable", "wudu", "hygiene",
            "forest", "wildlife", "nutrition", "food", "crop"
        ],
        "weight": 1.0
    },
    {
        "archetype": "style-school",
        "signals": [
            "learn", "student", "kids", "education", "school",
            "science", "fun", "teach", "class", "children",
            "quiz", "activity", "lesson", "math", "biology",
            "geography", "primary", "secondary", "young"
        ],
        "weight": 1.0
    },
    {
        "archetype": "style-cyber",
        "signals": [
            "code", "hack", "security", "blockchain", "crypto",
            "terminal", "devops", "api", "cyber", "network",
            "programming", "software", "algorithm", "database", "cloud",
            "linux", "docker", "kubernetes", "zero-day", "exploit"
        ],
        "weight": 1.0
    },
    {
        "archetype": "style-business",
        "signals": [
            "revenue", "strategy", "roi", "market", "growth",
            "pipeline", "quarterly", "kpi", "startup", "enterprise",
            "management", "leadership", "sales", "product", "stakeholder",
            "roadmap", "go-to-market", "business", "corporate", "executive"
        ],
        "weight": 1.0
    },
    {
        "archetype": "style-space",
        "signals": [
            "cosmos", "galaxy", "future", "vision", "exploration",
            "orbit", "space", "nasa", "rocket", "astronomy",
            "universe", "stellar", "nebula", "interstellar", "mars",
            "moon", "satellite", "telescope", "black hole", "photon"
        ],
        "weight": 1.0
    },
    {
        "archetype": "style-industrial",
        "signals": [
            "manufacturing", "construction", "infrastructure", "supply chain",
            "logistics", "engineering", "factory", "machinery", "blueprint",
            "structural", "architecture", "civil", "mechanical", "electrical",
            "plant", "refinery", "pipeline", "maintenance", "industrial"
        ],
        "weight": 1.0
    },
    {
        "archetype": "style-workshop",
        "signals": [
            "workshop", "training", "practical", "hands-on", "guide",
            "tutorial", "exercise", "how-to", "skills", "practice",
            "team", "collaborate", "brainstorm", "facilitation", "onboard",
            "diy", "prototype", "sprint", "agile", "retrospective"
        ],
        "weight": 1.0
    },
]

# Audience → archetype affinity (adds +3 to score)
AUDIENCE_BOOST = {
    "students":    "style-school",
    "children":    "style-school",
    "kids":        "style-school",
    "executives":  "style-business",
    "managers":    "style-business",
    "investors":   "style-luxury",
    "vip":         "style-luxury",
    "developers":  "style-cyber",
    "engineers":   "style-industrial",
    "creatives":   "style-editorial",
    "designers":   "style-editorial",
    "farmers":     "style-eco",
    "community":   "style-eco",
    "scientists":  "style-space",
    "visionaries": "style-space",
    "trainers":    "style-workshop",
    "scholars":    "style-luxury",
    "historians":  "style-luxury",
    "researchers": "style-research",
    "academics":   "style-research",
    "professors":  "style-research",
    "phd":         "style-research",
}

# Tone → archetype affinity (adds +2 to score)
TONE_BOOST = {
    "playful":      "style-school",
    "bold":         "style-editorial",
    "minimal":      "style-editorial",
    "elegant":      "style-luxury",
    "refined":      "style-luxury",
    "technical":    "style-cyber",
    "practical":    "style-workshop",
    "natural":      "style-eco",
    "professional": "style-business",
    "corporate":    "style-business",
    "cinematic":    "style-space",
    "epic":         "style-space",
    "structural":   "style-industrial",
    "academic":     "style-research",
    "analytical":   "style-research",
    "rigorous":     "style-research",
    "scholarly":    "style-research",
}


class TopicAnalyzer:
    """
    Resolves a topic string into the best matching archetype.
    Scoring: category signals (phrase-aware) + audience boost + tone boost.
    Falls back to 'style-business' when no signals match.
    """

    def resolve(self, topic: str, audience: str = "", tone: str = "") -> str:
        topic_lower = topic.lower()
        scores: dict[str, float] = {}

        # 1. Category signal matching
        for cat in CATEGORIES:
            arch = cat["archetype"]
            hits = sum(1 for signal in cat["signals"] if signal in topic_lower)
            scores[arch] = scores.get(arch, 0.0) + hits * cat["weight"]

        # 2. Audience boost (+3)
        if audience:
            boosted = AUDIENCE_BOOST.get(audience.lower())
            if boosted:
                scores[boosted] = scores.get(boosted, 0.0) + 3.0

        # 3. Tone boost (+2)
        if tone:
            boosted = TONE_BOOST.get(tone.lower())
            if boosted:
                scores[boosted] = scores.get(boosted, 0.0) + 2.0

        if not scores or max(scores.values()) == 0:
            return "style-business"  # Safe default

        return max(scores, key=scores.get)

    # LLM hook — reserved for future integration
    def resolve_with_llm(self, topic: str, audience: str = "", tone: str = "") -> str:
        raise NotImplementedError("LLM resolver not yet implemented. Use resolve().")
