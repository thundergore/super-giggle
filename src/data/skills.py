"""Skills proficiency and assessment data model."""

from dataclasses import dataclass
from enum import Enum


class ProficiencyLevel(Enum):
    """Proficiency level definitions with clear criteria."""

    AWARENESS = (0, 30, "Learning / Awareness")
    APPLIED = (31, 60, "Applied in Projects")
    PROFICIENT = (61, 85, "Proficient Daily Use")
    EXPERT = (86, 100, "Expert / Teaching Others")

    def __init__(self, min_score: int, max_score: int, description: str):
        self.min_score = min_score
        self.max_score = max_score
        self.description = description

    @classmethod
    def from_score(cls, score: int) -> "ProficiencyLevel":
        """Get proficiency level from a score."""
        for level in cls:
            if level.min_score <= score <= level.max_score:
                return level
        raise ValueError(f"Score {score} out of range (0-100)")


@dataclass
class SkillProficiency:
    """Represents proficiency in a specific skill."""

    name: str
    score: int  # 0-100
    years_experience: float
    last_used: str  # e.g., "2025-01" or "Current"
    context: str  # How/where the skill was applied

    @property
    def level(self) -> ProficiencyLevel:
        """Get the proficiency level."""
        return ProficiencyLevel.from_score(self.score)

    @property
    def level_description(self) -> str:
        """Get the level description."""
        return self.level.description


# Current technical skills (as of 2025-01-26)
SKILLS = {
    "Python": SkillProficiency(
        name="Python",
        score=84,
        years_experience=7.0,
        last_used="Current",
        context="Daily use for data pipelines, ML models, automation scripts",
    ),
    "SQL": SkillProficiency(
        name="SQL",
        score=95,
        years_experience=7.0,
        last_used="Current",
        context="Daily use for data analysis, dbt transformations, query optimization",
    ),
    "NLP": SkillProficiency(
        name="NLP",
        score=79,
        years_experience=3.0,
        last_used="Current",
        context="Production models using Hugging Face, OpenAI, WhisperX for transcription",
    ),
    "Data Visualization": SkillProficiency(
        name="Data Visualization",
        score=90,
        years_experience=6.0,
        last_used="Current",
        context="Tableau dashboards, Python (matplotlib, seaborn, plotly), executive reporting",
    ),
    "Machine Learning": SkillProficiency(
        name="Machine Learning",
        score=71,
        years_experience=3.0,
        last_used="Current",
        context="Classification models, NLP pipelines, scikit-learn, transformers",
    ),
    "Data Engineering": SkillProficiency(
        name="Data Engineering",
        score=70,
        years_experience=4.0,
        last_used="Current",
        context="Flyte orchestration, Docker, dbt, Snowflake, data pipeline design",
    ),
}

# Skills usage by role (percentage represents time spent / importance in role)
# This separates "proficiency" from "responsibility weight"
SKILLS_BY_ROLE = {
    "Blizzard Entertainment": {
        "Data Analysis": 65,  # Analyzed player behavior, issue patterns
        "Scripting": 5,  # Minimal automation
        "Big Data": 80,  # Dealt with massive player databases
        "Data Visualization": 10,  # Basic reporting
        "Creative/Communication": 100,  # Primary focus: player interaction
    },
    "Jolt Online Gaming": {
        "Data Analysis": 15,  # Basic community metrics
        "Scripting": 10,  # Simple automation
        "Big Data": 0,  # No large-scale data work
        "Data Visualization": 15,  # Social media metrics
        "Creative/Communication": 63,  # Content creation focus
    },
    "Lionbridge": {
        "Data Analysis": 45,  # QA metrics and reporting
        "Scripting": 40,  # Process automation
        "Big Data": 15,  # Limited data scale
        "Data Visualization": 50,  # Client reporting
        "Creative/Communication": 50,  # Documentation and client relations
    },
    "HBO Max": {
        "Data Analysis": 90,  # Primary responsibility
        "Scripting": 65,  # SQL + Python for automation
        "Big Data": 90,  # Large-scale streaming data
        "Data Visualization": 80,  # Dashboards and reporting
        "Creative/Communication": 90,  # Cross-functional collaboration
    },
    "HBO Max / WarnerBros": {
        "Data Analysis": 95,  # Advanced analytics
        "Scripting": 90,  # Daily Python/SQL work
        "Big Data": 85,  # Snowflake data warehouse
        "Data Visualization": 90,  # Executive dashboards
        "Creative/Communication": 85,  # Stakeholder management
    },
    "Schibsted": {
        "Data Analysis": 95,  # Core responsibility
        "Scripting": 90,  # Daily development
        "Big Data": 85,  # Analytics engineering
        "Data Visualization": 90,  # Tableau and Python viz
        "Creative/Communication": 75,  # Team collaboration
    },
}

# Expanded skills with tools (for word cloud / network visualization)
SKILLS_WITH_TOOLS = {
    # Programming Languages
    "Python": 84,
    "SQL": 95,
    # Data Tools
    "Tableau": 70,
    "Snowflake": 60,
    "DBT": 50,
    "Pandas": 80,
    # ML/AI Tools
    "NLP": 79,
    "Machine Learning": 75,
    "Hugging Face": 45,
    "OpenAI": 45,
    "WhisperX": 40,
    # Visualization
    "Matplotlib": 70,
    "Plotly": 65,
    "Data Visualization": 90,
    # Engineering
    "Docker": 60,
    "Flyte": 50,
    "Data Engineering": 65,
    "Data Pipelines": 70,
}

# Methodology documentation
SKILLS_METHODOLOGY = """
## Skills Assessment Methodology

### Proficiency Scoring (0-100)
- **0-30 (Awareness/Learning)**: Familiar with concepts, learning actively, not yet applied in production
- **31-60 (Applied in Projects)**: Used in real projects, comfortable with basics, need documentation for advanced features
- **61-85 (Proficient Daily Use)**: Daily usage, can solve complex problems, mentor others on basics
- **86-100 (Expert/Teaching Others)**: Deep expertise, teach others, contribute to community, optimize and architect

### Data Sources
- **Years Experience**: Based on employment records and project timelines
- **Proficiency Scores**: Self-assessment validated against:
  - Project complexity and outcomes
  - Peer feedback and code reviews
  - Frequency of use (daily, weekly, monthly)
  - Teaching/mentoring activities

### Skills by Role Percentages
These represent **responsibility weight** (% of time/importance), not proficiency:
- Based on role descriptions and actual work performed
- Validated against project portfolios and deliverables
- Updated periodically to reflect career progression

### Last Updated
2025-01-26

### Limitations
- Self-assessment inherently subjective
- Scores reflect practical application, not theoretical knowledge
- Some skills overlap (e.g., Data Engineering includes SQL, Python, Docker)
"""
