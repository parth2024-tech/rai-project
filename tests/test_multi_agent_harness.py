"""
Unit tests for dialectic Multi-Agent Debate Harness, dispute trees, and uncertainty estimation.
"""

import pytest

from src.agents.multi_agent_harness import MultiAgentDebateHarness


@pytest.fixture
def sample_profile():
    return {
        "profile_id": "TEST_01",
        "candidate_name": "Test Candidate",
        "skills": ["Python_Basics"],
        "target": "Machine Learning Engineer",
        "timeline": "3 months",
        "budget": "Low (₹2,000 / month)",
        "college_tier": "Tier-3 Rural Engineering College",
        "background": "Self-taught student wanting to transition into ML engineering with limited budget."
    }


def test_harness_initialization():
    harness = MultiAgentDebateHarness(model_name="qwen3:4b-fast")
    assert harness.model_name == "qwen3:4b-fast"


def test_debate_execution_structure(sample_profile):
    """Verify that run_debate returns all required debate, governance, and synthesis components."""
    harness = MultiAgentDebateHarness()
    result = harness.run_debate(sample_profile)

    # Core top-level keys
    assert "candidate_profile" in result
    assert "evidence_retrieved" in result
    assert "persona_turns" in result
    assert "dispute_tree" in result
    assert "uncertainty_metrics" in result
    assert "gate_triggered" in result
    assert "moderator_synthesis" in result

    # Check persona turns
    turns = result["persona_turns"]
    assert "planner" in turns
    assert "critic" in turns
    assert "ethics_reviewer" in turns

    assert "stance" in turns["planner"]
    assert "proposed_milestones" in turns["planner"]
    assert "stance" in turns["critic"]
    assert "screening_hurdles" in turns["critic"]
    assert "stance" in turns["ethics_reviewer"]
    assert "accessible_resources_mandate" in turns["ethics_reviewer"]


def test_dispute_tree_generation(sample_profile):
    """Verify that dispute tree extracts dialectic contradictions and friction between personas."""
    harness = MultiAgentDebateHarness()
    result = harness.run_debate(sample_profile)
    dispute_tree = result["dispute_tree"]

    assert isinstance(dispute_tree, list)
    assert len(dispute_tree) >= 1

    first_dispute = dispute_tree[0]
    assert "dispute_id" in first_dispute
    assert "dimension" in first_dispute
    assert "planner_stance" in first_dispute
    assert "critic_stance" in first_dispute
    assert "ethics_stance" in first_dispute
    assert "severity" in first_dispute
    assert "resolution" in first_dispute


def test_epistemic_uncertainty_bounds(sample_profile):
    """Verify that calibrated epistemic uncertainty respects mathematical boundaries [0, 1]."""
    harness = MultiAgentDebateHarness()
    result = harness.run_debate(sample_profile)
    metrics = result["uncertainty_metrics"]

    u = metrics["calibrated_uncertainty"]
    conf = metrics["epistemic_confidence"]
    interval = metrics["calibration_interval"]

    assert 0.0 <= u <= 1.0, f"Uncertainty {u} is outside [0.0, 1.0]"
    assert 0.0 <= conf <= 1.0, f"Confidence {conf} is outside [0.0, 1.0]"
    assert len(interval) == 2
    assert 0.0 <= interval[0] <= interval[1] <= 1.0


def test_human_override_interaction(sample_profile):
    """Verify that counselor override weights adjust synthesizer behavior and flag active override."""
    harness = MultiAgentDebateHarness()
    override_weights = {
        "planner": 0.2,
        "critic": 0.5,
        "ethics": 0.3
    }
    result = harness.run_debate(
        sample_profile,
        user_override_weights=override_weights,
        force_override=True
    )

    assert result["human_override_active"] is True
    synthesis = result["moderator_synthesis"]
    assert "counselor_override_active" in synthesis
    assert synthesis["counselor_override_active"] is True
    assert synthesis["weights_applied"] == override_weights


def test_evidence_retrieval_and_diversity(sample_profile):
    """Verify that vector evidence retrieval yields diverse academic and industry resources."""
    harness = MultiAgentDebateHarness()
    result = harness.run_debate(sample_profile)
    evidence = result["evidence_retrieved"]

    assert len(evidence) > 0
    domains = [e.get("domain") for e in evidence if "domain" in e]
    assert len(domains) > 0
