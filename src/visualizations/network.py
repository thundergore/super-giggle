"""Interactive network diagram visualization using Plotly."""

import plotly.graph_objects as go
import networkx as nx
from typing import List, Tuple
from ..data.connections import (
    TOOL_CONNECTIONS,
    NODE_CATEGORIES,
    get_node_color,
    get_node_size,
)


def create_network_diagram(
    connections: List[Tuple[str, str]] = TOOL_CONNECTIONS,
    output_path: str = "output/visualizations/network.html",
    show: bool = False,
) -> go.Figure:
    """
    Create an interactive network diagram of tools and skills connections.

    Args:
        connections: List of (source, target) tuples representing connections
        output_path: Path to save HTML output
        show: Whether to display the figure immediately

    Returns:
        Plotly Figure object
    """
    # Create network graph
    G = nx.Graph()
    G.add_edges_from(connections)

    # Calculate layout
    pos = nx.spring_layout(G, seed=42, k=1.5, iterations=50)

    # Prepare edge traces
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        line=dict(width=1, color="#BDC3C7"),
        hoverinfo="none",
        mode="lines",
        showlegend=False,
    )

    # Prepare node traces (one per category for legend)
    node_traces = {}

    for node in G.nodes():
        category = NODE_CATEGORIES.get(node, "competency")
        if category not in node_traces:
            node_traces[category] = {
                "x": [],
                "y": [],
                "text": [],
                "marker_size": [],
                "marker_color": get_node_color(node),
                "hover_text": [],
            }

        x, y = pos[node]
        node_traces[category]["x"].append(x)
        node_traces[category]["y"].append(y)
        node_traces[category]["text"].append(node)

        size = get_node_size(node)
        # Scale size for better visualization
        node_traces[category]["marker_size"].append(size * 0.8 + 20)

        # Build hover text
        connections_count = len(list(G.neighbors(node)))
        hover = f"<b>{node}</b><br>"
        hover += f"Category: {category.replace('_', ' ').title()}<br>"
        hover += f"Connections: {connections_count}<br>"
        hover += f"Connected to: {', '.join(list(G.neighbors(node))[:5])}"
        if connections_count > 5:
            hover += f"... (+{connections_count - 5} more)"
        node_traces[category]["hover_text"].append(hover)

    # Create figure
    fig = go.Figure()

    # Add edge trace first (so it's behind nodes)
    fig.add_trace(edge_trace)

    # Add node traces with legend
    category_names = {
        "language": "Programming Languages",
        "competency": "Core Competencies",
        "data_tool": "Data Tools",
        "viz_tool": "Visualization Tools",
        "ml_tool": "ML/AI Tools",
        "infrastructure": "Infrastructure",
    }

    for category, data in node_traces.items():
        fig.add_trace(
            go.Scatter(
                x=data["x"],
                y=data["y"],
                mode="markers+text",
                name=category_names.get(category, category.replace("_", " ").title()),
                marker=dict(
                    size=data["marker_size"],
                    color=data["marker_color"],
                    line=dict(width=2, color="white"),
                ),
                text=data["text"],
                textposition="top center",
                textfont=dict(size=10, color="#2C3E50", family="Arial Black"),
                hovertemplate="%{customdata}<extra></extra>",
                customdata=data["hover_text"],
            )
        )

    # Update layout
    fig.update_layout(
        title=dict(
            text="Skills & Tools Network<br><sub>Connections show how technologies relate in practice</sub>",
            font=dict(size=22, color="#2C3E50"),
            x=0.5,
            xanchor="center",
        ),
        showlegend=True,
        legend=dict(
            orientation="v",
            yanchor="top",
            y=1,
            xanchor="left",
            x=1.02,
            bgcolor="rgba(255, 255, 255, 0.8)",
            bordercolor="#BDC3C7",
            borderwidth=1,
        ),
        hovermode="closest",
        paper_bgcolor="white",
        plot_bgcolor="white",
        height=800,
        width=1100,
        margin=dict(l=20, r=200, t=100, b=20),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
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


def get_network_stats(connections: List[Tuple[str, str]] = TOOL_CONNECTIONS) -> dict:
    """
    Calculate network statistics for analysis.

    Args:
        connections: List of (source, target) tuples

    Returns:
        Dictionary of network statistics
    """
    G = nx.Graph()
    G.add_edges_from(connections)

    # Calculate various metrics
    degree_centrality = nx.degree_centrality(G)
    betweenness_centrality = nx.betweenness_centrality(G)

    # Get top nodes by centrality
    top_degree = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:5]
    top_betweenness = sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)[
        :5
    ]

    return {
        "num_nodes": G.number_of_nodes(),
        "num_edges": G.number_of_edges(),
        "density": nx.density(G),
        "top_connected": top_degree,
        "top_bridging": top_betweenness,
    }


if __name__ == "__main__":
    # Generate network diagram when run directly
    create_network_diagram(show=True)

    # Print network statistics
    stats = get_network_stats()
    print("\n=== Network Statistics ===")
    print(f"Nodes: {stats['num_nodes']}")
    print(f"Edges: {stats['num_edges']}")
    print(f"Density: {stats['density']:.3f}")
    print("\nTop Connected Skills:")
    for skill, centrality in stats["top_connected"]:
        print(f"  {skill}: {centrality:.3f}")
    print("\nTop Bridging Skills (connecting different areas):")
    for skill, centrality in stats["top_bridging"]:
        print(f"  {skill}: {centrality:.3f}")
