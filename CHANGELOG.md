# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2025-01-26

### Added
- **Interactive Visualizations**: All charts now use Plotly with:
  - Hover tooltips showing detailed information
  - Zoom and pan capabilities
  - Responsive sizing for mobile devices
  - Better color schemes and accessibility

- **Modular Code Structure**:
  - `src/data/` - Type-safe data models using Python dataclasses
  - `src/visualizations/` - Modular visualization generation
  - `src/generate.py` - CLI tool for generating visualizations
  - `tests/` - Comprehensive data quality test suite

- **Data Quality & Methodology**:
  - Automated tests for chronological consistency
  - Score range validation (0-100)
  - Documented proficiency assessment criteria in METHODOLOGY.md
  - Clear separation of "proficiency" vs "responsibility weight"

- **Modern Web Design**:
  - Responsive Tailwind CSS layout
  - Mobile-first approach
  - SEO meta tags for social sharing
  - Metric summary cards
  - Enhanced storytelling with narrative sections

- **Project Deep Dives**:
  - Three detailed case studies with measurable impact
  - Technology stack for each project
  - Quantified achievements

- **Developer Experience**:
  - requirements.txt for dependency management
  - pyproject.toml for project configuration
  - Black, Ruff, and mypy for code quality
  - Comprehensive README with usage examples
  - CI/CD ready structure

### Changed
- **From**: Single Jupyter notebook (cv.ipynb, 415KB)
- **To**: Modular Python codebase with separation of concerns
- **Visualization Library**: matplotlib/seaborn → Plotly
- **Data Storage**: Inline dictionaries → Type-safe dataclasses
- **HTML**: Inline CSS → Tailwind CSS with responsive design
- **Documentation**: Brief README → Comprehensive docs with methodology

### Improved
- **Data Accuracy**: All dates cross-referenced with employment records
- **Transparency**: Clear methodology documentation
- **Maintainability**: Modular code easier to update and extend
- **Performance**: Faster regeneration with caching
- **Accessibility**: Better color contrast and alt text
- **Storytelling**: Added achievements, metrics, and narrative flow

### Technical Details

**New Dependencies**:
- plotly>=5.18.0 (interactive visualizations)
- networkx>=3.2 (graph analysis)
- pandas>=2.1.0 (data manipulation)
- pytest>=7.4.0 (testing)
- black>=23.12.0 (code formatting)
- ruff>=0.1.0 (linting)

**New Files**:
- `src/data/experience.py` - Professional experience data model
- `src/data/skills.py` - Skills proficiency with methodology
- `src/data/connections.py` - Tool/skill network relationships
- `src/visualizations/*.py` - Five visualization modules
- `src/generate.py` - Main generation script
- `tests/test_data_quality.py` - Data validation tests
- `METHODOLOGY.md` - Assessment criteria documentation
- `CHANGELOG.md` - This file

**File Structure**:
```
Before: 1 notebook (cv.ipynb)
After:  15 Python modules + docs + tests + config files
```

### Migration Notes

**For Users**:
1. Install dependencies: `pip install -r requirements.txt`
2. Generate visualizations: `python src/generate.py`
3. View portfolio: Open `output/index.html`

**For Developers**:
- Old notebook preserved in project root for reference
- Old static PNGs still in `Viz/` directory
- New interactive HTMLs generated in `output/visualizations/`
- Run tests before committing: `pytest tests/`

### Breaking Changes

- Visualization output location changed from `Viz/` to `output/visualizations/`
- Main portfolio page moved from root `index.html` to `output/index.html`
- File naming: `xp_timeline.png` → `timeline.html` (interactive)
- Data structure: Dictionaries → Dataclasses (not backward compatible)

### Deprecated

- Static matplotlib/seaborn visualizations (PNGs)
- Root `index.html` (replaced by `output/index.html`)
- Inline data definitions in notebook

### Security

- No sensitive data in repository
- .gitignore updated to exclude .env files
- Email address published intentionally for portfolio purposes

## [1.0.0] - 2025-01-26

### Initial Version
- Single Jupyter notebook with matplotlib visualizations
- Static PNG exports
- Basic HTML page with inline CSS
- Manual data updates

---

## Upcoming (Planned)

### [2.1.0] - TBD
- [ ] GitHub Actions CI/CD pipeline
- [ ] Automated deployment to GitHub Pages
- [ ] Dark mode toggle in UI
- [ ] Export visualizations to PDF

### [2.2.0] - TBD
- [ ] Skill proficiency timeline (track changes over time)
- [ ] Blog integration for extended case studies
- [ ] Certifications and education timeline
- [ ] Interactive filtering of skills by category

### [3.0.0] - TBD
- [ ] API endpoint for programmatic access to portfolio data
- [ ] Real-time GitHub activity integration
- [ ] LinkedIn profile sync
- [ ] Analytics dashboard (page views, engagement)

---

**Legend**:
- Added: New features
- Changed: Changes in existing functionality
- Deprecated: Soon-to-be removed features
- Removed: Removed features
- Fixed: Bug fixes
- Security: Security improvements
