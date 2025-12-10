<p align="center">
    <img src="img/dall-e-logo.webp" alt="Craig Turner's Logo" width="300">
</p>

# Craig Turner's Data Analytics Portfolio

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Plotly](https://img.shields.io/badge/plotly-5.18+-purple.svg)](https://plotly.com/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**Version**: `2.0.0` | **Last Updated**: `2025-12-10`

Interactive data visualizations showcasing 19 years of professional experience in data analytics, from gaming communities to enterprise analytics engineering. Built with modern Python data stack and interactive Plotly visualizations.

## What's New in v2.0

- **Interactive Visualizations**: All charts now use Plotly with hover tooltips, zoom, and pan
- **Modular Codebase**: Refactored from single notebook to production-grade Python modules
- **Data Quality Tests**: Comprehensive test suite validates data integrity
- **Modern UI**: Responsive Tailwind CSS design with mobile support
- **Methodology Documentation**: Transparent proficiency assessment criteria
- **Case Studies**: Detailed project deep dives with measurable impact

## Live Demo

View the portfolio at: [\[Super-giggle\]](https://thundergore.github.io/super-giggle/)

## Features

### Interactive Visualizations

1. **Professional Timeline** - 19-year career journey with role details
2. **Skills Proficiency Radar** - Technical competencies with context
3. **Role-Skills Heatmap** - Evolution of responsibilities over time
4. **Skills Treemap** - Portfolio breakdown by technology category
5. **Technology Network** - How tools and skills interconnect

### Data-Driven Approach

- ✅ **Validated Data**: Automated tests ensure chronological consistency and score ranges
- ✅ **Transparent Methodology**: Clear criteria for proficiency levels (see [METHODOLOGY.md](METHODOLOGY.md))
- ✅ **Version Controlled**: All data changes tracked with rationale
- ✅ **Type Safe**: Python dataclasses with proper typing

## Quick Start

### Prerequisites

- Python 3.11 or higher
- pip or poetry for package management

### Installation

```bash
# Clone the repository
git clone https://github.com/thundergore/super-giggle.git
cd super-giggle

# Install dependencies
pip install -r requirements.txt

# Or with optional dev tools
pip install -r requirements.txt
pip install -e ".[dev]"
```

### Generate Visualizations

```bash
# Generate all visualizations
python src/generate.py

# Generate specific visualization
python src/generate.py --viz timeline

# Generate and display in browser
python src/generate.py --show
```

Output will be in `output/visualizations/` as interactive HTML files.

### Run Tests

```bash
# Run data quality tests
pytest tests/

# Run with coverage
pytest tests/ --cov=src --cov-report=html
```

### View Locally

```bash
# Open the portfolio page
open output/index.html

# Or serve with Python
python -m http.server 8000 --directory output
# Then visit http://localhost:8000
```

## Project Structure

```
super-giggle/
├── src/
│   ├── data/              # Data models and sources
│   │   ├── experience.py  # Professional roles with achievements
│   │   ├── skills.py      # Skills proficiency with methodology
│   │   └── connections.py # Tool/skill network relationships
│   ├── visualizations/    # Plotly visualization modules
│   │   ├── timeline.py
│   │   ├── radar.py
│   │   ├── heatmap.py
│   │   ├── wordcloud.py   # Actually a treemap
│   │   └── network.py
│   └── generate.py        # Main generation script
├── tests/
│   └── test_data_quality.py  # Comprehensive data validation
├── output/
│   ├── index.html         # Portfolio website
│   └── visualizations/    # Generated interactive charts
├── notebooks/
│   └── cv.ipynb           # Original exploration notebook (legacy)
├── METHODOLOGY.md         # Assessment criteria documentation
├── requirements.txt       # Python dependencies
├── pyproject.toml         # Project configuration
└── README.md             # This file
```

## Technology Stack

**Core:**
- Python 3.11+ (dataclasses, type hints)
- Plotly 5.18+ (interactive visualizations)
- NetworkX (graph analysis)
- Pandas (data manipulation)

**Development:**
- pytest (testing)
- black (code formatting)
- ruff (linting)
- mypy (type checking)

**Frontend:**
- Tailwind CSS (responsive design)
- Plotly.js (embedded in HTML exports)

## Data Methodology

All proficiency scores follow a standardized 0-100 scale:

- **0-30**: Awareness/Learning
- **31-60**: Applied in Projects
- **61-85**: Proficient Daily Use
- **86-100**: Expert/Teaching Others

For detailed criteria and data sources, see [METHODOLOGY.md](METHODOLOGY.md).

## Customization

### Adding New Experience

Edit `src/data/experience.py`:

```python
Role(
    company="Your Company",
    title="Your Title",
    start_date=date(2025, 1, 1),
    end_date=None,  # None for current role
    color="#FF6B6B",
    responsibilities=["..."],
    achievements=["..."],
)
```

### Updating Skills

Edit `src/data/skills.py`:

```python
"New Skill": SkillProficiency(
    name="New Skill",
    score=75,
    years_experience=2.0,
    last_used="Current",
    context="How you use this skill...",
)
```

### Regenerate

```bash
python src/generate.py
```

## Development

### Code Quality

```bash
# Format code
black src/ tests/

# Lint
ruff check src/ tests/

# Type check
mypy src/
```

### Running Tests

```bash
# All tests
pytest

# With coverage
pytest --cov=src --cov-report=term-missing

# Specific test file
pytest tests/test_data_quality.py -v
```

## CI/CD Recommendations

The project is ready for automation:

```yaml
# .github/workflows/generate.yml
name: Generate Visualizations
on:
  push:
    branches: [main]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: pytest tests/
      - run: python src/generate.py
      - uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./output
```

## Roadmap

- [ ] GitHub Actions CI/CD pipeline
- [ ] Automated deployment to GitHub Pages
- [ ] Skill proficiency timeline (track changes over time)
- [ ] Export to PDF for offline viewing
- [ ] Dark mode toggle
- [ ] Blog integration for case study details
- [ ] Certifications and education timeline

## FAQ

**Q: Why move from Jupyter notebook to modular code?**
A: Better maintainability, testability, and demonstrates production coding practices. Plus it's easier to automate regeneration.

**Q: Can I use this for my own portfolio?**
A: Absolutely! Fork the repo, update the data in `src/data/`, regenerate, and deploy. Attribution appreciated.

**Q: How do you ensure data accuracy?**
A: Comprehensive test suite validates chronological consistency, score ranges, and logical relationships. All changes are version controlled.

**Q: Why Plotly instead of matplotlib?**
A: Interactive visualizations provide better user experience with hover details, zoom, and pan. More engaging for portfolio showcase.

## Contributing

While this is a personal portfolio, suggestions for improvements are welcome:

1. Open an issue describing the improvement
2. Fork and create a feature branch
3. Submit a PR with tests if applicable

## License

This project is open source for educational purposes. Feel free to fork and adapt for your own portfolio.

## Contact

- **LinkedIn**: [Craig Turner](https://www.linkedin.com/in/craigianturner)
- **GitHub**: [@thundergore](https://github.com/thundergore)
- **Email**: craig.turner@schibsted.com

---

Built with ❤️ and data by Craig Turner | Last updated: 2025-01-26
