"""Main script to generate all visualizations."""

import sys
from pathlib import Path
from datetime import datetime

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.visualizations.timeline import create_timeline
from src.visualizations.radar import create_radar_chart
from src.visualizations.heatmap import create_heatmap
from src.visualizations.wordcloud import create_wordcloud
from src.visualizations.network import create_network_diagram, get_network_stats


def ensure_output_directory() -> Path:
    """Ensure output directory exists."""
    output_dir = Path("output/visualizations")
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def generate_all_visualizations(show: bool = False) -> dict:
    """
    Generate all portfolio visualizations.

    Args:
        show: Whether to display visualizations after generation

    Returns:
        Dictionary with generation statistics
    """
    print("=" * 60)
    print("Craig Turner's Portfolio Visualization Generator")
    print("=" * 60)
    print()

    start_time = datetime.now()

    # Ensure output directory exists
    output_dir = ensure_output_directory()
    print(f"Output directory: {output_dir.absolute()}")
    print()

    visualizations = [
        ("Timeline", create_timeline),
        ("Radar Chart", create_radar_chart),
        ("Heatmap", create_heatmap),
        ("Skills Treemap", create_wordcloud),
        ("Network Diagram", create_network_diagram),
    ]

    results = {}

    for name, func in visualizations:
        print(f"Generating {name}...", end=" ")
        try:
            fig = func(show=show)
            print("✓ Done")
            results[name] = {"status": "success", "figure": fig}
        except Exception as e:
            print(f"✗ Error: {e}")
            results[name] = {"status": "error", "error": str(e)}

    # Generate network statistics
    print()
    print("=" * 60)
    print("Network Analysis")
    print("=" * 60)
    try:
        stats = get_network_stats()
        print(f"\nTotal Skills/Tools: {stats['num_nodes']}")
        print(f"Connections: {stats['num_edges']}")
        print(f"Network Density: {stats['density']:.3f}")
        print("\nMost Connected Skills:")
        for skill, centrality in stats["top_connected"][:3]:
            print(f"  • {skill}: {centrality:.3f}")
        print("\nKey Bridging Skills (connecting different domains):")
        for skill, centrality in stats["top_bridging"][:3]:
            print(f"  • {skill}: {centrality:.3f}")
        results["network_stats"] = stats
    except Exception as e:
        print(f"Error calculating network stats: {e}")

    # Summary
    print()
    print("=" * 60)
    print("Generation Summary")
    print("=" * 60)

    successful = sum(1 for r in results.values() if isinstance(r, dict) and r.get("status") == "success")
    total = len(visualizations)

    print(f"\nCompleted: {successful}/{total} visualizations")

    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    print(f"Duration: {duration:.2f} seconds")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    print(f"View visualizations in: {output_dir.absolute()}")
    print()

    return results


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate portfolio visualizations for Craig Turner"
    )
    parser.add_argument(
        "--show",
        action="store_true",
        help="Display visualizations in browser after generation",
    )
    parser.add_argument(
        "--viz",
        choices=["timeline", "radar", "heatmap", "wordcloud", "network", "all"],
        default="all",
        help="Generate specific visualization (default: all)",
    )

    args = parser.parse_args()

    if args.viz == "all":
        generate_all_visualizations(show=args.show)
    else:
        # Generate single visualization
        viz_map = {
            "timeline": ("Timeline", create_timeline),
            "radar": ("Radar Chart", create_radar_chart),
            "heatmap": ("Heatmap", create_heatmap),
            "wordcloud": ("Skills Treemap", create_wordcloud),
            "network": ("Network Diagram", create_network_diagram),
        }

        ensure_output_directory()
        name, func = viz_map[args.viz]
        print(f"Generating {name}...")
        func(show=args.show)
        print(f"✓ {name} generated successfully")


if __name__ == "__main__":
    main()
