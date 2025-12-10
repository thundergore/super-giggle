# Data Methodology & Assessment Criteria

This document explains how the data in this portfolio is collected, assessed, and maintained to ensure accuracy and transparency.

## Data Sources

### Experience Timeline
- **Source**: LinkedIn employment history + manual verification
- **Last Updated**: 2025-01-26
- **Update Frequency**: Updated when changing roles or significant milestones occur

### Skills Proficiency
- **Source**: Self-assessment validated against project outcomes
- **Validation Method**:
  - Project complexity and deliverables
  - Peer feedback and code reviews
  - Frequency of use (daily, weekly, monthly, rarely)
  - Teaching/mentoring activities
  - Contributions to documentation or open source

### Skills by Role
- **Source**: Job descriptions + actual work performed
- **Validation**: Project portfolios, deliverables, and documented achievements
- **Note**: Percentages represent **responsibility weight** (time/importance), not skill proficiency

## Proficiency Scoring System (0-100)

The proficiency scores use a standardized 0-100 scale with four distinct levels:

### Level 1: Awareness / Learning (0-30)
**Criteria:**
- Familiar with concepts and terminology
- Currently learning or have limited hands-on experience
- Can understand documentation with effort
- Not yet applied in production environments
- Would need significant support to use independently

**Example:** Just completed an online course; read documentation but haven't built anything substantial.

### Level 2: Applied in Projects (31-60)
**Criteria:**
- Used in real projects with successful outcomes
- Comfortable with fundamental concepts and common patterns
- Can solve standard problems with occasional documentation reference
- Applied in production but not the primary technology expert
- Can complete tasks with minimal guidance

**Example:** Built 2-3 production features; comfortable for routine tasks but consult docs for advanced scenarios.

### Level 3: Proficient Daily Use (61-85)
**Criteria:**
- Daily or weekly usage in professional capacity
- Can solve complex problems and debug difficult issues
- Rarely need documentation for common tasks
- Can mentor others on fundamentals and some advanced topics
- Contribute to best practices and standards
- Make architectural decisions involving this skill

**Example:** Primary technology in current role; go-to person for questions; write internal documentation.

### Level 4: Expert / Teaching Others (86-100)
**Criteria:**
- Deep expertise across most aspects of the technology
- Regularly teach workshops, write tutorials, or mentor others
- Contribute to open-source projects or community knowledge
- Can architect complex systems and optimize performance
- Stay current with latest developments and best practices
- Recognized expertise by peers or community

**Example:** Give conference talks; write blog posts; contribute to official docs; architect systems at scale.

## Limitations & Caveats

### Self-Assessment Bias
- All proficiency scores are self-assessed, which inherently carries subjective bias
- Scores reflect practical application ability, not theoretical knowledge
- Individual perception of expertise varies; these scores represent honest self-evaluation

### Context Dependency
- Proficiency is context-dependent (e.g., "expert in Python for data analysis" ≠ "expert in all Python")
- Scores reflect the specific context mentioned in the "context" field
- Some skills overlap significantly (e.g., Data Engineering includes SQL, Python, Docker)

### Time Decay
- Skills not used recently may decrease in proficiency
- Last updated date critical for interpreting current ability
- "Last Used" field indicates recency

### Scope Limitations
- Not all skills are included (focus on most relevant for data analytics roles)
- Soft skills (communication, leadership) not quantified here
- Domain knowledge (e.g., media industry) not captured in skill scores

## Skills by Role Methodology

The "Skills by Role" data uses a different metric than proficiency:

### What It Measures
- **Responsibility Weight**: Percentage of time or importance in that role
- **Not Proficiency**: A high percentage doesn't mean expert-level, just that it was a major responsibility
- **Role Context**: What the job required, not what you could do

### Interpretation Examples
- **Blizzard (Big Data: 80%)**: Worked with large databases daily, even if not as an expert
- **Schibsted (Data Analysis: 95%)**: Primary job function, most of time spent on this

### Why Separate from Proficiency?
- You can spend 90% of time on something while still learning (high responsibility, medium proficiency)
- Conversely, you can be an expert in something rarely used in a role (low responsibility, high proficiency)
- This separation provides clearer career narrative

## Data Quality Assurance

### Automated Validation
- Comprehensive test suite (`tests/test_data_quality.py`) validates:
  - Date consistency (no overlaps, chronological order)
  - Score ranges (0-100)
  - Required fields present
  - Logical consistency across datasets

### Manual Review Process
1. Annual review of all proficiency scores
2. Update "last used" dates quarterly
3. Add new skills as they become relevant (50+ hours of usage)
4. Archive skills no longer used for 2+ years

### Version Control
- All data changes tracked in git history
- Rationale for major score changes documented in commit messages
- Transparency in methodology evolution

## Changelog

### 2025-01-26 (v2.0.0)
- Complete restructure to modular Python codebase
- Added explicit methodology documentation
- Implemented automated data quality tests
- Added ProficiencyLevel enum with clear criteria
- Separated "skills by role" from skill proficiency
- Added achievements and context to all experience entries

### Future Improvements
- [ ] Track skill proficiency over time (trend data)
- [ ] Add external validation (certifications, peer reviews)
- [ ] Include project portfolio links as evidence
- [ ] Add difficulty/complexity ratings to achievements
- [ ] Incorporate objective metrics (lines of code, projects completed)

## Questions or Feedback?

If you have questions about this methodology or suggestions for improvement:
- LinkedIn: [Craig Turner](https://www.linkedin.com/in/craigianturner)
- GitHub Issues: [super-giggle repository](https://github.com/thundergore/super-giggle/issues)

## References

This methodology draws inspiration from:
- Dreyfus Model of Skill Acquisition
- Software Engineering Competency Matrix
- Data science skill assessment frameworks (Kaggle, DataCamp)
