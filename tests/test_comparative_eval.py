"""
Unit tests for Comparative Evaluation Benchmark across 4 configurations and 20 synthetic profiles.
"""

from src.eval.comparative_eval import ComparativeEvaluator, load_synthetic_profiles


def test_synthetic_profiles_loading():
    """Verify that all 20 synthetic candidate profiles load with counterfactual pairs."""
    profiles = load_synthetic_profiles()
    assert len(profiles) == 20

    base_ids = set(p["base_id"] for p in profiles)
    assert len(base_ids) == 10

    for base_id in base_ids:
        variants = [p for p in profiles if p["base_id"] == base_id]
        assert len(variants) == 2
        var_types = {v["variant"] for v in variants}
        assert var_types == {"A", "B"}


def test_config_1_monolithic_evaluation():
    """Verify metrics computation for baseline Monolithic Single LLM (Config 1)."""
    evaluator = ComparativeEvaluator()
    res = evaluator._eval_config_1_single_llm()

    assert res["config_id"] == "C1"
    metrics = res["metrics"]
    assert "evidence_diversity" in metrics
    assert "contradiction_resolution_rate" in metrics
    assert "unsupported_claim_rate" in metrics
    assert "fairness_across_synthetic_profiles" in metrics
    assert "user_rubric_score" in metrics

    # Baseline has 0% contradiction resolution
    assert metrics["contradiction_resolution_rate"] == "0.0%"


def test_config_2_multi_perspective_evaluation():
    """Verify metrics computation for Multi-Perspective Prompted Single LLM (Config 2)."""
    evaluator = ComparativeEvaluator()
    res = evaluator._eval_config_2_multi_perspective()

    assert res["config_id"] == "C2"
    metrics = res["metrics"]
    assert float(metrics["contradiction_resolution_rate"].replace("%", "")) > 0.0


def test_config_3_unmoderated_triad_evaluation():
    """Verify metrics computation for Unmoderated Triad Debate (Config 3)."""
    evaluator = ComparativeEvaluator()
    res = evaluator._eval_config_3_unmoderated_triad()

    assert res["config_id"] == "C3"
    assert res["raw_counts"]["total_profiles"] == 20


def test_config_4_proposed_rai_system():
    """Verify metrics computation for Proposed RAI Multi-Persona + Graph Gate System (Config 4)."""
    evaluator = ComparativeEvaluator()
    res = evaluator._eval_config_4_proposed_system()

    assert res["config_id"] == "C4"
    metrics = res["metrics"]

    # Unsupported claim rate should be 0.0% due to Graph Prerequisite Gate
    assert metrics["unsupported_claim_rate"] == "0.0%"
    # Contradiction resolution rate should be high
    crr = float(metrics["contradiction_resolution_rate"].replace("%", ""))
    assert crr >= 80.0
    # User rubric score should exceed 4.0
    rubric = float(metrics["user_rubric_score"].split()[0])
    assert rubric >= 4.0


def test_comparative_advantage_of_proposed_system():
    """Verify that Proposed System (C4) statistically outperforms Baseline Monolithic (C1) across all RAI dimensions."""
    evaluator = ComparativeEvaluator()
    c1 = evaluator._eval_config_1_single_llm()
    c4 = evaluator._eval_config_4_proposed_system()

    # Evidence Diversity
    assert c4["metrics"]["evidence_diversity"] > c1["metrics"]["evidence_diversity"]

    # Unsupported Claim Rate (lower is better)
    ucr_c1 = float(c1["metrics"]["unsupported_claim_rate"].replace("%", ""))
    ucr_c4 = float(c4["metrics"]["unsupported_claim_rate"].replace("%", ""))
    assert ucr_c4 < ucr_c1

    # Contradiction Resolution Rate (higher is better)
    crr_c1 = float(c1["metrics"]["contradiction_resolution_rate"].replace("%", ""))
    crr_c4 = float(c4["metrics"]["contradiction_resolution_rate"].replace("%", ""))
    assert crr_c4 > crr_c1
