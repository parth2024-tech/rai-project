"""
Unit tests for Plagiarism & Academic Originality Auditor.
"""

import os
import tempfile
import pytest

from src.utils.plagiarism_auditor import (
    analyze_burstiness_and_readability,
    audit_research_paper,
    calculate_lexical_diversity,
    clean_typst_prose,
    generate_plagiarism_report,
    scan_for_ai_cliches,
    shingle_overlap_check,
)


def test_clean_typst_prose():
    """Verify that Typst markup, directives, and math symbols are stripped to clean prose."""
    with tempfile.NamedTemporaryFile("w", suffix=".typ", delete=False) as f:
        f.write(
            "// Comment line\n"
            "#set page(paper: \"us-letter\")\n"
            "= Section Heading\n"
            "This is a substantive sentence evaluating student career advising.\n"
            "Here is another valid academic statement with math $Delta > 0$ and code `test`.\n"
        )
        temp_path = f.name

    try:
        full_text, sentences = clean_typst_prose(temp_path)
        assert "Comment line" not in full_text
        assert "#set" not in full_text
        assert len(sentences) >= 2
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)


def test_calculate_lexical_diversity():
    """Verify computation of TTR, Hapax ratio, and Yule's K metric."""
    sample = "The dialectic triad evaluates career pathways using topological graphs and calibrated uncertainty."
    metrics = calculate_lexical_diversity(sample)

    assert metrics["total_word_count"] > 5
    assert metrics["vocabulary_size"] > 5
    assert 0.0 < metrics["type_token_ratio"] <= 1.0
    assert 0.0 <= metrics["hapax_legomena_ratio"] <= 1.0


def test_burstiness_and_readability():
    """Verify sentence length standard deviation and Flesch-Kincaid grade computation."""
    sentences = [
        "Language models frequently exhibit sycophancy when advising students on technical careers.",
        "We enforce prerequisite graph constraints deterministically.",
        "This architectural intervention prevents sequence failure while preserving critical student agency throughout deliberation."
    ]
    res = analyze_burstiness_and_readability(sentences)

    assert res["sentence_count"] == 3
    assert res["mean_sentence_length"] > 5
    assert res["sentence_length_std_dev"] > 0
    assert res["flesch_kincaid_grade"] > 8.0


def test_scan_for_ai_cliches():
    """Verify that synthetic AI clichés are detected when present and ignored when absent."""
    clean_text = "We evaluate counterfactual pairs across five empirical metrics using paired bootstrap tests."
    assert len(scan_for_ai_cliches(clean_text)) == 0

    cliche_text = "In today's fast-paced digital world, this system serves as a testament to AI synergy and delves into data."
    matches = scan_for_ai_cliches(cliche_text)
    assert len(matches) >= 2


def test_shingle_overlap_check():
    """Verify that rolling 8-word shingles detect identical multi-word phrases."""
    sentences = [
        "This is an exact verbatim phrase that should be flagged as repeated text.",
        "This is an exact verbatim phrase that should be flagged as repeated text in another sentence."
    ]
    res = shingle_overlap_check(sentences, shingle_size=8)
    assert res["duplicate_shingles_found"] >= 1


def test_audit_research_paper_and_report():
    """Verify that paper.typ passes the end-to-end academic integrity audit."""
    if not os.path.exists("paper.typ"):
        pytest.skip("paper.typ not found in current directory")

    result = audit_research_paper("paper.typ")
    assert result["verdict"] == "PASSED - ZERO PLAGIARISM DETECTED"
    assert result["plagiarism_rate"] == "0.00%"
    assert float(result["academic_originality_index"].replace("%", "")) >= 95.0

    with tempfile.TemporaryDirectory() as tmpdir:
        report_path = os.path.join(tmpdir, "test_report.md")
        report = generate_plagiarism_report(result, output_path=report_path)
        assert os.path.exists(report_path)
        assert "Academic Integrity & Plagiarism Audit Certificate" in report
        assert "0.00%" in report
