"""Interactive radar chart visualization using Plotly."""

import plotly.graph_objects as go
from typing import Dict
from ..data.skills import SKILLS, SkillProficiency


def create_radar_chart(
    skills: Dict[str, SkillProficiency] = SKILLS,
    output_path: str = "output/visualizations/radar.html",
    show: bool = False,
) -> go.Figure:
    """
    Create an interactive radar chart of skill proficiencies.

    Args:
        skills: Dictionary of skill name to SkillProficiency objects
        output_path: Path to save HTML output
        show: Whether to display the figure immediately

    Returns:
        Plotly Figure object
    """
    # Extract skill names and scores
    skill_names = list(skills.keys())
    skill_scores = [skill.score for skill in skills.values()]

    # Build hover text with detailed information
    hover_texts = []
    for name, skill in skills.items():
        hover_text = f"<b>{name}</b><br>"
        hover_text += f"Score: {skill.score}/100<br>"
        hover_text += f"Level: {skill.level_description}<br>"
        hover_text += f"Experience: {skill.years_experience} years<br>"
        hover_text += f"Last Used: {skill.last_used}<br>"
        hover_text += f"<i>{skill.context[:80]}...</i>"
        hover_texts.append(hover_text)

    # Create radar chart
    fig = go.Figure()

    fig.add_trace(
        go.Scatterpolar(
            r=skill_scores,
            theta=skill_names,
            fill="toself",
            fillcolor="rgba(138, 43, 226, 0.25)",  # Purple with transparency
            line=dict(color="rgb(138, 43, 226)", width=3),  # Purple line
            marker=dict(size=8, color="rgb(255, 140, 0)"),  # Orange markers
            hovertemplate="%{text}<extra></extra>",
            text=hover_texts,
            name="Proficiency",
        )
    )

    # Update layout
    fig.update_layout(
        title=dict(
            text="Technical Skill Proficiency",
            font=dict(size=24, color="#2C3E50"),
            x=0.5,
            xanchor="center",
        ),
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickmode="linear",
                tick0=0,
                dtick=20,
                tickfont=dict(size=10, color="#7F8C8D"),
                gridcolor="#E8E8E8",
            ),
            angularaxis=dict(
                tickfont=dict(size=12, color="#2C3E50"),
                gridcolor="#E8E8E8",
            ),
            bgcolor="white",
        ),
        paper_bgcolor="white",
        height=600,
        width=700,
        margin=dict(l=100, r=100, t=100, b=50),
        showlegend=False,
        font=dict(family="Arial, sans-serif"),
    )

    # Add reference circles for proficiency levels
    fig.add_trace(
        go.Scatterpolar(
            r=[30] * len(skill_names),
            theta=skill_names,
            mode="lines",
            line=dict(color="rgba(255, 0, 0, 0.2)", width=1, dash="dot"),
            hoverinfo="skip",
            showlegend=False,
            name="Awareness (30)",
        )
    )

    fig.add_trace(
        go.Scatterpolar(
            r=[60] * len(skill_names),
            theta=skill_names,
            mode="lines",
            line=dict(color="rgba(255, 165, 0, 0.2)", width=1, dash="dot"),
            hoverinfo="skip",
            showlegend=False,
            name="Applied (60)",
        )
    )

    fig.add_trace(
        go.Scatterpolar(
            r=[85] * len(skill_names),
            theta=skill_names,
            mode="lines",
            line=dict(color="rgba(0, 128, 0, 0.2)", width=1, dash="dot"),
            hoverinfo="skip",
            showlegend=False,
            name="Proficient (85)",
        )
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
    # Generate radar chart when run directly
    create_radar_chart(show=True)
