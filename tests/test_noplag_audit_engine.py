"""
Unit tests for Noplag Engine Plagiarism & AI Integrity Audit Suite.
Validates:
- Schleimer Winnowing fingerprint computation
- BLAST-adapted Seed-and-Extend alignment
- Sliding chunking
- AI stylometry and cliché detection
- End-to-end audit execution on paper.typ
"""

from __future__ import annotations

import os
from src.utils.noplag_audit_engine import (
    analyze_ai_vs_human_stylometry,
    chunk_document,
    compute_winnowing_fingerprint,
    extract_clean_typst_prose,
    hash_kgram,
    normalize_text,
    run_noplag_audit,
    seed_and_extend_align,
)


def test_normalize_text_and_citation_stripping():
    """Verify that normalization strips brackets and citation markers while preserving text."""
    sample = "According to ACM guidelines [12], curriculum design requires foundational math."
    norm = normalize_text(sample)
    assert "[12]" not in norm
    assert "acm guidelines" in norm
    assert "curriculum design" in norm


def test_hash_kgram_signed_64bit():
    """Verify that keyless Blake2b hashes fit within signed 64-bit integer range."""
    h = hash_kgram("hello")
    assert isinstance(h, int)
    assert -(2**63) <= h < 2**63


def test_compute_winnowing_fingerprint():
    """Verify that winnowing produces sorted, deduplicated fingerprints."""
    sample = "Large Language Models often exhibit sycophancy in career advisory tasks."
    fps = compute_winnowing_fingerprint(sample, k=5, w=8)
    assert len(fps) > 0
    assert sorted(fps) == fps
    assert len(fps) == len(set(fps))


def test_chunk_document_sliding():
    """Verify that sliding document chunking produces overlapping windows."""
    long_text = "Computer science education requires structured prerequisite validation. " * 30
    chunks = chunk_document(long_text, chunk_size=300, chunk_overlap=50)
    assert len(chunks) >= 2
    assert chunks[0].char_start == 0
    assert chunks[0].char_end == 300
    assert len(chunks[0].fingerprints) > 0


def test_seed_and_extend_alignment():
    """Verify BLAST seed-and-extend detects identical passages and rejects disjoint text."""
    q = "This is an exact verbatim passage of sufficient length to trigger seed extraction and extension."
    c = "Prefix words before. This is an exact verbatim passage of sufficient length to trigger seed extraction and extension. Suffix."
    passages = seed_and_extend_align(q, c, "candidate_1", min_seed_len=20, min_passage_len=30)
    assert len(passages) >= 1
    assert "verbatim passage" in passages[0].matched_text

    # Disjoint text should produce 0 passages
    disjoint = "Completely unrelated words about cooking recipes and gardening."
    no_passages = seed_and_extend_align(q, disjoint, "candidate_2", min_seed_len=20, min_passage_len=30)
    assert len(no_passages) == 0


def test_analyze_ai_vs_human_stylometry():
    """Verify human stylometric classification on rich academic prose."""
    text = (
        "Engineering students face hurdles. "
        "Chatbots frequently advise learners to skip foundational mathematics and enroll in expensive commercial bootcamps without prerequisite checks. "
        "Our deterministic graph prevents these sequence violations through rigorous topological verification executed in Python on consumer hardware."
    )
    sentences = [
        "Engineering students face hurdles.",
        "Chatbots frequently advise learners to skip foundational mathematics and enroll in expensive commercial bootcamps without prerequisite checks.",
        "Our deterministic graph prevents these sequence violations through rigorous topological verification executed in Python on consumer hardware.",
    ]
    metrics = analyze_ai_vs_human_stylometry(text, sentences)
    assert metrics["type_token_ratio"] > 0.30
    assert metrics["burstiness_cv"] >= 0.35
    assert metrics["ai_probability"] == 0.0
    assert len(metrics["matched_cliches"]) == 0


def test_run_noplag_audit_on_paper():
    """Verify that paper.typ passes the full Noplag Engine audit with 0.00% plagiarism."""
    if not os.path.exists("paper.typ"):
        return
    res = run_noplag_audit("paper.typ")
    assert res["plagiarism_rate"] == 0.00
    assert res["originality_index"] == 100.00
    assert res["ai_probability"] == 0.0
    assert res["stylometry"]["burstiness_cv"] >= 0.35
    assert len(res["stylometry"]["matched_cliches"]) == 0
