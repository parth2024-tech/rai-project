#!/usr/bin/env python3
"""
Unit tests for all-configurations comparator.
"""

from src.eval.all_configs_comparator import compare_all_configs
from src.eval.comparative_eval import load_synthetic_profiles


def test_compare_all_configs_returns_all_four() -> None:
    profiles = load_synthetic_profiles()
    assert len(profiles) > 0
    p = profiles[0]

    comparison = compare_all_configs(p)
    assert len(comparison) == 4
    assert "Config 1 (Monolithic Baseline)" in comparison
    assert "Config 2 (Multi-Perspective Prompting)" in comparison
    assert "Config 3 (Unmoderated Debate)" in comparison
    assert "Config 4 (Proposed Deliberation System)" in comparison


def test_config_verdicts() -> None:
    profiles = load_synthetic_profiles()
    p = profiles[0]
    comparison = compare_all_configs(p)

    c1 = comparison["Config 1 (Monolithic Baseline)"]
    c4 = comparison["Config 4 (Proposed Deliberation System)"]

    assert c1["verdict"] == "FAILED"
    assert len(c1["violations"]) > 0
    assert c4["verdict"] == "PASSED"
    assert len(c4["violations"]) == 0
    assert "0.00" in c4["cost"] or "Free" in c4["cost"]
