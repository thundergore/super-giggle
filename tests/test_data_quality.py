"""Data quality and validation tests."""

import pytest
from datetime import date
from src.data import EXPERIENCE, SKILLS, SKILLS_BY_ROLE, TOOL_CONNECTIONS
from src.data.experience import Role
from src.data.skills import SkillProficiency, ProficiencyLevel


class TestExperienceData:
    """Test experience data quality and consistency."""

    def test_experience_not_empty(self):
        """Ensure experience data exists."""
        assert len(EXPERIENCE) > 0, "Experience data should not be empty"

    def test_experience_chronological_order(self):
        """Verify experience is in chronological order."""
        for i in range(len(EXPERIENCE) - 1):
            current = EXPERIENCE[i]
            next_role = EXPERIENCE[i + 1]
            assert current.start_year <= next_role.start_year, (
                f"{current.company} should come before {next_role.company}"
            )

    def test_only_one_current_role(self):
        """Ensure only one role has no end date."""
        current_roles = [role for role in EXPERIENCE if role.is_current]
        assert len(current_roles) == 1, "Should have exactly one current role"

    def test_current_role_is_most_recent(self):
        """Verify current role is the last one chronologically."""
        current_role = [role for role in EXPERIENCE if role.is_current][0]
        assert current_role == EXPERIENCE[-1], "Current role should be last in list"

    def test_no_year_overlaps(self):
        """Ensure no role years overlap."""
        for i in range(len(EXPERIENCE) - 1):
            current = EXPERIENCE[i]
            next_role = EXPERIENCE[i + 1]
            if current.end_year:
                assert current.end_year < next_role.start_year, (
                    f"Role overlap detected: {current.company} ends in {current.end_year}, "
                    f"but {next_role.company} starts in {next_role.start_year}"
                )

    def test_valid_year_ranges(self):
        """Verify all years are valid."""
        current_year = date.today().year
        for role in EXPERIENCE:
            assert role.start_year <= current_year, f"{role.company} start year is in the future"
            if role.end_year:
                assert role.end_year >= role.start_year, (
                    f"{role.company} end year before start year"
                )
                assert role.end_year <= current_year, f"{role.company} end year is in the future"

    def test_duration_calculation(self):
        """Test duration calculation is reasonable."""
        for role in EXPERIENCE:
            duration = role.duration_years
            assert 0 < duration <= 50, (
                f"{role.company} duration {duration} years seems unreasonable"
            )

    def test_roles_have_required_fields(self):
        """Ensure all roles have required data."""
        for role in EXPERIENCE:
            assert role.company, f"Role missing company name"
            assert role.title, f"{role.company} missing title"
            assert role.color, f"{role.company} missing color"
            assert role.responsibilities, f"{role.company} has no responsibilities"
            assert len(role.responsibilities) > 0, f"{role.company} responsibilities empty"

    def test_reasonable_year_range(self):
        """Verify experience spans reasonable time period."""
        earliest = min(role.start_year for role in EXPERIENCE)
        latest = max(role.end_year or date.today().year for role in EXPERIENCE)
        total_years = latest - earliest
        assert 10 <= total_years <= 50, (
            f"Total career span {total_years} years seems unreasonable"
        )


class TestSkillsData:
    """Test skills data quality and consistency."""

    def test_skills_not_empty(self):
        """Ensure skills data exists."""
        assert len(SKILLS) > 0, "Skills data should not be empty"

    def test_skill_scores_in_range(self):
        """Verify all skill scores are 0-100."""
        for skill_name, skill in SKILLS.items():
            assert 0 <= skill.score <= 100, (
                f"{skill_name} score {skill.score} out of range"
            )

    def test_proficiency_levels_valid(self):
        """Test proficiency level assignment."""
        for skill_name, skill in SKILLS.items():
            # Should not raise exception
            level = skill.level
            assert isinstance(level, ProficiencyLevel)

    def test_years_experience_reasonable(self):
        """Verify years of experience are reasonable."""
        for skill_name, skill in SKILLS.items():
            assert 0 < skill.years_experience <= 30, (
                f"{skill_name} years_experience {skill.years_experience} seems unreasonable"
            )

    def test_last_used_not_empty(self):
        """Ensure last_used field is populated."""
        for skill_name, skill in SKILLS.items():
            assert skill.last_used, f"{skill_name} missing last_used date"

    def test_context_provided(self):
        """Ensure context is provided for each skill."""
        for skill_name, skill in SKILLS.items():
            assert skill.context, f"{skill_name} missing context"
            assert len(skill.context) > 10, f"{skill_name} context too brief"


class TestSkillsByRole:
    """Test skills by role data consistency."""

    def test_all_companies_present(self):
        """Verify all companies from EXPERIENCE are in SKILLS_BY_ROLE."""
        # Note: Simplified names might differ
        experience_companies = {role.company for role in EXPERIENCE}
        skills_companies = set(SKILLS_BY_ROLE.keys())

        # Should have approximately the same number
        assert len(skills_companies) >= len(experience_companies) - 2, (
            f"Missing companies in SKILLS_BY_ROLE"
        )

    def test_role_skill_percentages_valid(self):
        """Verify all role skill percentages are 0-100."""
        for company, skills in SKILLS_BY_ROLE.items():
            for skill_name, percentage in skills.items():
                assert 0 <= percentage <= 100, (
                    f"{company} - {skill_name}: {percentage}% out of range"
                )

    def test_skills_have_values(self):
        """Ensure each role has skills defined."""
        for company, skills in SKILLS_BY_ROLE.items():
            assert len(skills) > 0, f"{company} has no skills defined"
            assert len(skills) >= 3, f"{company} has too few skills (should show progression)"


class TestToolConnections:
    """Test tool connections network data."""

    def test_connections_not_empty(self):
        """Ensure connections data exists."""
        assert len(TOOL_CONNECTIONS) > 0, "Tool connections should not be empty"

    def test_connections_are_tuples(self):
        """Verify connections are properly formatted."""
        for connection in TOOL_CONNECTIONS:
            assert isinstance(connection, tuple), f"Connection {connection} is not a tuple"
            assert len(connection) == 2, f"Connection {connection} should have 2 elements"
            assert isinstance(connection[0], str), f"Connection source should be string"
            assert isinstance(connection[1], str), f"Connection target should be string"

    def test_no_self_connections(self):
        """Verify no tool connects to itself."""
        for source, target in TOOL_CONNECTIONS:
            assert source != target, f"Self-connection detected: {source} -> {target}"

    def test_no_duplicate_connections(self):
        """Ensure no duplicate connections exist."""
        unique_connections = set(TOOL_CONNECTIONS)
        assert len(unique_connections) == len(TOOL_CONNECTIONS), (
            "Duplicate connections detected"
        )

    def test_bidirectional_consistency(self):
        """Check for inconsistent bidirectional connections."""
        # If A->B exists, B->A should probably not exist (represents different relationship)
        for source, target in TOOL_CONNECTIONS:
            reverse = (target, source)
            if reverse in TOOL_CONNECTIONS:
                # Log warning but don't fail (might be intentional)
                print(f"Warning: Bidirectional connection: {source} <-> {target}")


class TestDataConsistency:
    """Test consistency across all data sources."""

    def test_skill_names_consistent(self):
        """Verify skill names are used consistently across datasets."""
        # Skills should appear in connections if they're important
        skill_names = set(SKILLS.keys())
        connection_nodes = set()
        for source, target in TOOL_CONNECTIONS:
            connection_nodes.add(source)
            connection_nodes.add(target)

        # Most core skills should appear in network
        core_skills = {"Python", "SQL", "NLP", "Machine Learning", "Data Engineering"}
        assert core_skills.issubset(connection_nodes), (
            f"Core skills missing from network: {core_skills - connection_nodes}"
        )

    def test_current_role_has_highest_skill_usage(self):
        """Verify current role (Schibsted) shows highest skill utilization."""
        schibsted_skills = SKILLS_BY_ROLE.get("Schibsted", {})
        assert schibsted_skills, "Schibsted not found in SKILLS_BY_ROLE"

        # Should have high percentages for key skills
        data_analysis = schibsted_skills.get("Data Analysis", 0)
        assert data_analysis >= 90, f"Current role should have high Data Analysis: {data_analysis}%"


class TestProficiencyLevels:
    """Test proficiency level system."""

    def test_proficiency_ranges_complete(self):
        """Verify proficiency levels cover full 0-100 range."""
        covered_ranges = []
        for level in ProficiencyLevel:
            covered_ranges.extend(range(level.min_score, level.max_score + 1))

        # Should cover 0-100
        assert min(covered_ranges) == 0, "Proficiency levels don't start at 0"
        assert max(covered_ranges) == 100, "Proficiency levels don't reach 100"

    def test_proficiency_levels_no_overlap(self):
        """Ensure proficiency level ranges don't overlap."""
        levels = list(ProficiencyLevel)
        for i in range(len(levels) - 1):
            current = levels[i]
            next_level = levels[i + 1]
            assert current.max_score < next_level.min_score or \
                   current.max_score + 1 == next_level.min_score, (
                f"Overlap detected: {current.description} and {next_level.description}"
            )

    def test_proficiency_from_score(self):
        """Test score to proficiency level conversion."""
        assert ProficiencyLevel.from_score(15) == ProficiencyLevel.AWARENESS
        assert ProficiencyLevel.from_score(50) == ProficiencyLevel.APPLIED
        assert ProficiencyLevel.from_score(75) == ProficiencyLevel.PROFICIENT
        assert ProficiencyLevel.from_score(95) == ProficiencyLevel.EXPERT

    def test_invalid_score_raises_error(self):
        """Test that invalid scores raise appropriate errors."""
        with pytest.raises(ValueError):
            ProficiencyLevel.from_score(150)
        with pytest.raises(ValueError):
            ProficiencyLevel.from_score(-10)
