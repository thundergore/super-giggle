"""Interactive treemap visualization (replaces word cloud) using Plotly."""

import plotly.graph_objects as go
from typing import Dict
from ..data.skills import SKILLS_WITH_TOOLS
from ..data.connections import NODE_CATEGORIES, get_node_color


def create_wordcloud(
    skills_with_tools: Dict[str, int] = SKILLS_WITH_TOOLS,
    output_path: str = "output/visualizations/wordcloud.html",
    show: bool = False,
) -> go.Figure:
    """
    Create an interactive treemap of skills and tools (replaces traditional word cloud).

    Treemaps are more interactive and accessible than word clouds, while still
    showing relative importance through size.

    Args:
        skills_with_tools: Dictionary mapping skill/tool names to proficiency scores
        output_path: Path to save HTML output
        show: Whether to display the figure immediately

    Returns:
        Plotly Figure object
    """
    # Prepare data with categories
    labels = []
    parents = []
    values = []
    colors = []
    hover_texts = []

    # Add root
    labels.append("All Skills")
    parents.append("")
    values.append(0)  # Will be calculated automatically
    colors.append("#FFFFFF")
    hover_texts.append("All Technical Skills & Tools")

    # Group by category
    categories = {}
    for skill, score in skills_with_tools.items():
        category = NODE_CATEGORIES.get(skill, "competency")
        if category not in categories:
            categories[category] = []
        categories[category].append((skill, score))

    # Category names mapping
    category_names = {
        "language": "Programming Languages",
        "competency": "Core Competencies",
        "data_tool": "Data Tools",
        "viz_tool": "Visualization Tools",
        "ml_tool": "ML/AI Tools",
        "infrastructure": "Infrastructure & Orchestration",
    }

    # Add categories
    for category, items in categories.items():
        category_name = category_names.get(category, category.replace("_", " ").title())
        total_score = sum(score for _, score in items)

        labels.append(category_name)
        parents.append("All Skills")
        values.append(total_score)
        colors.append(get_node_color(items[0][0]) if items else "#CCCCCC")
        hover_texts.append(f"{category_name}<br>Total Proficiency: {total_score}")

        # Add individual skills
        for skill, score in items:
            labels.append(skill)
            parents.append(category_name)
            values.append(score)
            colors.append(get_node_color(skill))
            hover_text = f"<b>{skill}</b><br>"
            hover_text += f"Proficiency: {score}/100<br>"
            hover_text += f"Category: {category_name}"
            hover_texts.append(hover_text)

    # Create treemap
    fig = go.Figure(
        go.Treemap(
            labels=labels,
            parents=parents,
            values=values,
            marker=dict(
                colors=colors,
                line=dict(width=2, color="white"),
                colorscale=None,
            ),
            text=labels,
            textposition="middle center",
            hovertemplate="%{customdata}<extra></extra>",
            customdata=hover_texts,
            textfont=dict(size=14, color="white", family="Arial Black, sans-serif"),
        )
    )

    # Update layout
    fig.update_layout(
        title=dict(
            text="Skills & Tools Portfolio<br><sub>Interactive treemap showing proficiency across technologies</sub>",
            font=dict(size=22, color="#2C3E50"),
            x=0.5,
            xanchor="center",
        ),
        paper_bgcolor="white",
        height=600,
        width=900,
        margin=dict(l=20, r=20, t=100, b=20),
        font=dict(family="Arial, sans-serif"),
    )

    # Save to HTML
    fig.write_html(
        output_path,
        config={
            "displayModeBar": True,
            "displaylogo": False,
            "modeBarButtonsToRemove": ["pan2d", "lasso2d", "select2d"],
        },
    )

    if show:
        fig.show()

    return fig


def create_wordcloud_alternative(
    skills_with_tools: Dict[str, int] = SKILLS_WITH_TOOLS,
    output_path: str = "output/visualizations/wordcloud_sunburst.html",
    show: bool = False,
) -> go.Figure:
    """
    Alternative visualization: Sunburst chart (hierarchical pie chart).

    Args:
        skills_with_tools: Dictionary mapping skill/tool names to proficiency scores
        output_path: Path to save HTML output
        show: Whether to display the figure immediately

    Returns:
        Plotly Figure object
    """
    # Use same data preparation as treemap
    labels = []
    parents = []
    values = []
    colors = []

    labels.append("Skills")
    parents.append("")
    values.append(0)
    colors.append("#FFFFFF")

    categories = {}
    for skill, score in skills_with_tools.items():
        category = NODE_CATEGORIES.get(skill, "competency")
        if category not in categories:
            categories[category] = []
        categories[category].append((skill, score))

    category_names = {
        "language": "Languages",
        "competency": "Competencies",
        "data_tool": "Data Tools",
        "viz_tool": "Viz Tools",
        "ml_tool": "ML/AI",
        "infrastructure": "Infrastructure",
    }

    for category, items in categories.items():
        category_name = category_names.get(category, category.replace("_", " ").title())
        total_score = sum(score for _, score in items)

        labels.append(category_name)
        parents.append("Skills")
        values.append(total_score)
        colors.append(get_node_color(items[0][0]) if items else "#CCCCCC")

        for skill, score in items:
            labels.append(skill)
            parents.append(category_name)
            values.append(score)
            colors.append(get_node_color(skill))

    # Create sunburst
    fig = go.Figure(
        go.Sunburst(
            labels=labels,
            parents=parents,
            values=values,
            marker=dict(colors=colors, line=dict(width=2, color="white")),
            branchvalues="total",
        )
    )

    fig.update_layout(
        title="Skills & Tools Portfolio (Sunburst)",
        height=600,
        width=600,
        paper_bgcolor="white",
    )

    fig.write_html(output_path)

    if show:
        fig.show()

    return fig


if __name__ == "__main__":
    # Generate both visualizations when run directly
    create_wordcloud(show=True)
    # create_wordcloud_alternative(show=True)  # Optional alternative
