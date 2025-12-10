"""Tool and skill connections for network visualization."""

from typing import List, Tuple

# Connections between tools, skills, and technologies
# Format: (source, target)
TOOL_CONNECTIONS: List[Tuple[str, str]] = [
    # Python ecosystem
    ("Python", "Pandas"),
    ("Python", "NLP"),
    ("Python", "SQL"),
    ("Python", "Data Engineering"),
    ("Python", "Machine Learning"),
    ("Python", "Matplotlib"),
    ("Python", "Plotly"),

    # SQL and databases
    ("SQL", "Snowflake"),
    ("SQL", "DBT"),
    ("SQL", "Tableau"),
    ("SQL", "Data Analysis"),

    # DBT connections
    ("DBT", "Snowflake"),
    ("DBT", "Tableau"),
    ("DBT", "Data Engineering"),

    # Data science stack
    ("Pandas", "NLP"),
    ("Pandas", "Machine Learning"),
    ("Pandas", "Data Analysis"),

    # NLP/ML tools
    ("NLP", "Hugging Face"),
    ("NLP", "OpenAI"),
    ("NLP", "WhisperX"),
    ("Machine Learning", "Hugging Face"),

    # Visualization tools
    ("Tableau", "Data Visualization"),
    ("Matplotlib", "Data Visualization"),
    ("Plotly", "Data Visualization"),
    ("Pandas", "Matplotlib"),
    ("Pandas", "Plotly"),

    # Data engineering
    ("Snowflake", "Data Engineering"),
    ("Data Engineering", "Data Pipelines"),
    ("Data Engineering", "Flyte"),
    ("Docker", "Flyte"),
    ("Flyte", "NLP"),
    ("Flyte", "Data Pipelines"),

    # Data analysis connections
    ("Data Analysis", "Data Visualization"),
    ("Data Analysis", "Machine Learning"),
]

# Node categories for coloring/grouping
NODE_CATEGORIES = {
    # Programming Languages
    "Python": "language",
    "SQL": "language",

    # Core Competencies
    "Data Analysis": "competency",
    "Data Visualization": "competency",
    "Data Engineering": "competency",
    "NLP": "competency",
    "Machine Learning": "competency",

    # Data Tools
    "Pandas": "data_tool",
    "Snowflake": "data_tool",
    "DBT": "data_tool",

    # Visualization Tools
    "Tableau": "viz_tool",
    "Matplotlib": "viz_tool",
    "Plotly": "viz_tool",

    # ML/AI Tools
    "Hugging Face": "ml_tool",
    "OpenAI": "ml_tool",
    "WhisperX": "ml_tool",

    # Infrastructure
    "Docker": "infrastructure",
    "Flyte": "infrastructure",
    "Data Pipelines": "infrastructure",
}

# Color scheme for node categories
CATEGORY_COLORS = {
    "language": "#FF6B6B",  # Red
    "competency": "#4ECDC4",  # Teal
    "data_tool": "#45B7D1",  # Blue
    "viz_tool": "#FFA07A",  # Light Orange
    "ml_tool": "#98D8C8",  # Mint
    "infrastructure": "#95E1D3",  # Light Green
}

# Node sizes based on importance/proficiency
# (could be derived from SKILLS_WITH_TOOLS scores)
NODE_SIZES = {
    "Python": 84,
    "SQL": 95,
    "Data Analysis": 95,
    "Data Visualization": 90,
    "Data Engineering": 70,
    "NLP": 79,
    "Machine Learning": 71,
    "Pandas": 80,
    "Tableau": 70,
    "Snowflake": 60,
    "DBT": 50,
    "Docker": 60,
    "Flyte": 50,
    "Hugging Face": 45,
    "OpenAI": 45,
    "WhisperX": 40,
    "Matplotlib": 70,
    "Plotly": 65,
    "Data Pipelines": 70,
}


def get_node_color(node: str) -> str:
    """Get color for a node based on its category."""
    category = NODE_CATEGORIES.get(node, "competency")
    return CATEGORY_COLORS.get(category, "#999999")


def get_node_size(node: str) -> int:
    """Get size for a node based on proficiency/importance."""
    return NODE_SIZES.get(node, 50)
