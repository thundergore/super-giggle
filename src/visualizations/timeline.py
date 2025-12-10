"""Interactive timeline visualization using Plotly."""

import plotly.graph_objects as go
from datetime import date
from typing import List
from ..data.experience import Role, EXPERIENCE


def create_timeline(
    roles: List[Role] = EXPERIENCE,
    output_path: str = "output/visualizations/timeline.html",
    show: bool = False,
) -> go.Figure:
    """
    Create an interactive timeline visualization of professional experience.

    Args:
        roles: List of Role objects to visualize
        output_path: Path to save HTML output
        show: Whether to display the figure immediately

    Returns:
        Plotly Figure object
    """
    fig = go.Figure()

    # Create hover text with detailed information
    for i, role in enumerate(roles):
        # Format dates for display
        start_year = role.start_year
        end_year = role.end_year if role.end_year else date.today().year
        duration = role.duration_years

        # Build hover text
        hover_text = f"<b>{role.company}</b><br>"
        hover_text += f"{role.title}<br>"
        hover_text += f"{start_year} - {'Present' if role.is_current else role.end_year}<br>"
        hover_text += f"Duration: {duration} years<br><br>"
        hover_text += "<b>Key Responsibilities:</b><br>"
        for resp in role.responsibilities[:3]:  # Show top 3
            hover_text += f"• {resp}<br>"

        # Add bar for this role
        # For roles that start in current year, show at least 0.5 year width so they're visible
        bar_width = max(end_year - start_year, 0.5)

        fig.add_trace(
            go.Bar(
                name=role.company,
                x=[bar_width],
                y=[i],
                base=start_year,
                orientation="h",
                marker=dict(color=role.color, line=dict(color="white", width=1)),
                hovertemplate=hover_text + "<extra></extra>",
                text=f"{role.title}",
                textposition="inside",
                textfont=dict(color="white", size=11),
                insidetextanchor="middle",
            )
        )

    # Update layout
    fig.update_layout(
        title=dict(
            text="Professional Experience Timeline",
            font=dict(size=24, color="#2C3E50"),
            x=0.5,
            xanchor="center",
        ),
        xaxis=dict(
            title="Year",
            range=[2005, date.today().year + 1],
            tickmode="linear",
            tick0=2006,
            dtick=2,
            gridcolor="#E8E8E8",
        ),
        yaxis=dict(
            title="",
            ticktext=[role.company for role in roles],
            tickvals=list(range(len(roles))),
            autorange="reversed",
        ),
        plot_bgcolor="white",
        paper_bgcolor="white",
        height=500,
        margin=dict(l=150, r=50, t=80, b=80),
        showlegend=False,
        hovermode="closest",
        font=dict(family="Arial, sans-serif", size=12, color="#34495E"),
    )

    # Add vertical line for current year
    current_year = date.today().year
    fig.add_vline(
        x=current_year,
        line_dash="dash",
        line_color="gray",
        opacity=0.5,
        annotation_text=f"Today ({current_year})",
        annotation_position="top",
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
    # Generate timeline when run directly
    create_timeline(show=True)
