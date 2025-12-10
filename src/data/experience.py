"""Professional experience data model."""

from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Role:
    """Represents a professional role/position."""

    company: str
    title: str
    start_year: int
    end_year: Optional[int]  # None for current role
    color: str
    responsibilities: list[str]

    @property
    def duration_years(self) -> float:
        """Calculate duration in years."""
        end = self.end_year or date.today().year
        return round(end - self.start_year, 1)

    @property
    def is_current(self) -> bool:
        """Check if this is a current role."""
        return self.end_year is None


# Professional experience timeline
EXPERIENCE = [
    Role(
        company="Blizzard Entertainment",
        title="Specialist Game Master",
        start_year=2006,
        end_year=2008,
        color="#4A90E2",  # Blue
        responsibilities=[
            "Customer support for World of Warcraft",
            "Community management and player relations",
            "Issue resolution and escalation handling",
            "Player behavior analysis and reporting",
        ],
    ),
    Role(
        company="Jolt Online Gaming",
        title="Community Manager",
        start_year=2008,
        end_year=2012,
        color="#FFD700",  # Gold
        responsibilities=[
            "Community engagement and content moderation",
            "Event planning and coordination",
            "Content creation and social media management",
            "Analytics reporting on community metrics",
        ],
    ),
    Role(
        company="Lionbridge",
        title="Consultant",
        start_year=2012,
        end_year=2018,
        color="#87CEEB",  # Sky blue
        responsibilities=[
            "Quality assurance testing",
            "Technical documentation",
            "Client communication and reporting",
            "Process improvement and automation",
        ],
    ),
    Role(
        company="HBO Max",
        title="Technical Support",
        start_year=2018,
        end_year=2021,
        color="#9B59B6",  # Purple
        responsibilities=[
            "Technical troubleshooting for streaming platform",
            "Data analysis of support tickets and user issues",
            "Cross-functional collaboration with engineering teams",
            "Performance metrics tracking and reporting",
        ],
    ),
    Role(
        company="HBO Max / WarnerBros",
        title="Data Analyst",
        start_year=2021,
        end_year=2023,
        color="#FF8C00",  # Orange
        responsibilities=[
            "Data pipeline development and maintenance",
            "Advanced analytics and reporting",
            "Stakeholder collaboration and insights delivery",
            "Machine learning model development",
        ],
    ),
    Role(
        company="Schibsted",
        title="Data Analyst",
        start_year=2023,
        end_year=2025,
        color="#32CD32",  # Green
        responsibilities=[
            "Analytics engineering with dbt",
            "Data pipeline orchestration with Flyte",
            "Advanced NLP and ML model development",
            "Cross-team data platform initiatives",
        ],
    ),
    Role(
        company="Schibsted",
        title="Data Scientist",
        start_year=2025,
        end_year=None, # Current role
        color="#FF69B4",  # Pink
        responsibilities=[
            "Sequential NLP model development",
            "Recommender systems engineering",
            "Real-time data processing pipelines",
        ],
    ),
]

# Data source metadata
DATA_METADATA = {
    "source": "LinkedIn profile + manual curation",
    "last_updated": "2025-12-10",
    "methodology": "Dates verified against employment records",
}
