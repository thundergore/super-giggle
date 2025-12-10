"""Interactive heatmap visualization using Plotly."""

import plotly.graph_objects as go
import pandas as pd
from typing import Dict
from ..data.skills import SKILLS_BY_ROLE


def create_heatmap(
    skills_by_role: Dict[str, Dict[str, int]] = SKILLS_BY_ROLE,
    output_path: str = "output/visualizations/heatmap.html",
    show: bool = False,
) -> go.Figure:
    """
    Create an interactive heatmap of skill usage across roles.

    Args:
        skills_by_role: Dictionary mapping role names to skill percentages
        output_path: Path to save HTML output
        show: Whether to display the figure immediately

    Returns:
        Plotly Figure object
    """
    # Convert to DataFrame for easier manipulation
    df = pd.DataFrame(skills_by_role).T

    # Get role names and skill names
    roles = df.index.tolist()
    skills = df.columns.tolist()

    # Create hover text
    hover_texts = []
    for role in roles:
        role_hover = []
        for skill in skills:
            value = df.loc[role, skill]
            hover_text = f"<b>{role}</b><br>"
            hover_text += f"Skill: {skill}<br>"
            hover_text += f"Responsibility: {value}%<br>"
            if value >= 80:
                hover_text += "<i>Primary focus area</i>"
            elif value >= 50:
                hover_text += "<i>Regular responsibility</i>"
            elif value >= 20:
                hover_text += "<i>Occasional work</i>"
            else:
                hover_text += "<i>Minimal involvement</i>"
            role_hover.append(hover_text)
        hover_texts.append(role_hover)

    # Create heatmap
    fig = go.Figure(
        data=go.Heatmap(
            z=df.values,
            x=skills,
            y=roles,
            colorscale=[
                [0.0, "#F8F9FA"],  # Very light gray for 0
                [0.2, "#E3D5F5"],  # Very light purple
                [0.4, "#C7ABE8"],  # Light purple
                [0.6, "#AB81DB"],  # Medium purple
                [0.8, "#8F57CE"],  # Dark purple
                [1.0, "#732DC1"],  # Very dark purple
            ],
            text=df.values,
            texttemplate="%{text}",
            textfont=dict(size=11, color="white"),
            hovertemplate="%{customdata}<extra></extra>",
            customdata=hover_texts,
            colorbar=dict(
                title="Responsibility<br>Weight (%)",
                titleside="right",
                tickmode="linear",
                tick0=0,
                dtick=20,
                thickness=20,
                len=0.7,
            ),
        )
    )

    # Update layout
    fig.update_layout(
        title=dict(
            text="Skills Usage Across Roles<br><sub>Percentage represents responsibility weight, not proficiency level</sub>",
            font=dict(size=22, color="#2C3E50"),
            x=0.5,
            xanchor="center",
        ),
        xaxis=dict(
            title="Skills & Competencies",
            side="bottom",
            tickangle=-45,
            tickfont=dict(size=12, color="#2C3E50"),
        ),
        yaxis=dict(
            title="Professional Roles",
            tickfont=dict(size=12, color="#2C3E50"),
            autorange="reversed",  # Show oldest role at top
        ),
        plot_bgcolor="white",
        paper_bgcolor="white",
        height=500,
        width=900,
        margin=dict(l=180, r=120, t=120, b=120),
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


if __name__ == "__main__":
    # Generate heatmap when run directly
    create_heatmap(show=True)
