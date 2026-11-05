"""
Basic unit tests for RAI Project verification.
"""
from src.graph.career_graph import career_graph
from src.rag.vector_store import EvidenceVectorStore


def test_career_graph_structure():
    """Verify that the 42-node prerequisite graph is populated and valid."""
    assert len(career_graph.graph.nodes) >= 42
    assert len(career_graph.graph.edges) >= 40
    # Test prerequisite resolution
    prereqs = career_graph.get_prerequisites("Deep_Learning")
    assert "Linear_Algebra" in prereqs or "ML_Foundations" in prereqs


def test_vector_store_diversity():
    """Verify Shannon entropy calculation for evidence diversity."""
    items = [
        {"domain": "MIT OCW"},
        {"domain": "Berkeley CS61"},
        {"domain": "Stanford CS144"},
        {"domain": "O*NET"}
    ]
    diversity = EvidenceVectorStore.calculate_evidence_diversity(items)
    assert diversity > 0.8
    # Zero items
    assert EvidenceVectorStore.calculate_evidence_diversity([]) == 0.0
