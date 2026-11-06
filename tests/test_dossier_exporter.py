"""
Unit tests for Counselor Audit Dossier Exporter (JSON, Markdown, HTML, and file persistence).
"""

import json
import os
import tempfile
import pytest

from src.agents.multi_agent_harness import MultiAgentDebateHarness
from src.utils.dossier_exporter import (
    export_dossier_to_file,
    generate_html_dossier,
    generate_json_dossier,
    generate_markdown_dossier,
)


@pytest.fixture
def mock_debate_result():
    harness = MultiAgentDebateHarness()
    profile = {
        "candidate_name": "Test Student",
        "skills": ["Python_Basics"],
        "target": "Machine Learning Engineer",
        "timeline": "6 months",
        "budget": "Low (₹3,000 / month)",
        "college_tier": "Tier-3 Rural Engineering College",
        "background": "Aspiring ML engineer with strong motivation but budget constraints."
    }
    return harness.run_debate(profile)


def test_generate_json_dossier_structure(mock_debate_result):
    """Verify JSON dossier structure conformant with university advisor records."""
    dossier = generate_json_dossier(mock_debate_result)

    assert dossier["dossier_version"] == "1.0.0"
    assert "candidate" in dossier
    assert dossier["candidate"]["name"] == "Test Student"
    assert dossier["candidate"]["target_role"] == "Machine Learning Engineer"

    assert "deliberation_trace" in dossier
    assert "planner" in dossier["deliberation_trace"]
    assert "critic" in dossier["deliberation_trace"]
    assert "ethics_reviewer" in dossier["deliberation_trace"]
    assert "dispute_tree" in dossier["deliberation_trace"]

    assert "governance_and_safety" in dossier
    assert "calibrated_uncertainty" in dossier["governance_and_safety"]
    assert "gate_triggered" in dossier["governance_and_safety"]

    assert "verified_roadmap" in dossier
    assert "actionable_milestones" in dossier["verified_roadmap"]


def test_generate_markdown_dossier_content(mock_debate_result):
    """Verify Markdown dossier contains headers, dispute tree table, and uncertainty metrics."""
    md = generate_markdown_dossier(mock_debate_result)

    assert "# Responsible AI Career Guidance Audit Dossier" in md
    assert "Candidate Profile & Context" in md
    assert "Multi-Persona Deliberation Trace" in md
    assert "Dispute Tree & Resolved Contention Forks" in md
    assert "Prerequisite DAG Verification & Calibrated Uncertainty" in md
    assert "Actionable Roadmap & Grounded Evidence Citations" in md
    assert "Test Student" in md


def test_generate_html_dossier_styling(mock_debate_result):
    """Verify HTML dossier produces styled, accessible, sanitized markup."""
    html = generate_html_dossier(mock_debate_result)

    assert "<!DOCTYPE html>" in html
    assert "<html lang=\"en\">" in html
    assert "Test Student" in html
    assert "Responsible Artificial Intelligence Platform" in html
    assert "metric-card" in html


def test_export_dossier_to_file(mock_debate_result):
    """Verify file persistence across markdown, json, and html formats."""
    with tempfile.TemporaryDirectory() as tmpdir:
        md_path = os.path.join(tmpdir, "audit_dossier.md")
        json_path = os.path.join(tmpdir, "audit_dossier.json")
        html_path = os.path.join(tmpdir, "audit_dossier.html")

        # Test Markdown Export
        res_md = export_dossier_to_file(mock_debate_result, md_path, fmt="markdown")
        assert os.path.exists(res_md)
        with open(res_md, "r", encoding="utf-8") as f:
            assert "# Responsible AI Career Guidance Audit Dossier" in f.read()

        # Test JSON Export
        res_json = export_dossier_to_file(mock_debate_result, json_path, fmt="json")
        assert os.path.exists(res_json)
        with open(res_json, "r", encoding="utf-8") as f:
            data = json.load(f)
            assert data["dossier_version"] == "1.0.0"

        # Test HTML Export
        res_html = export_dossier_to_file(mock_debate_result, html_path, fmt="html")
        assert os.path.exists(res_html)
        with open(res_html, "r", encoding="utf-8") as f:
            assert "<!DOCTYPE html>" in f.read()
