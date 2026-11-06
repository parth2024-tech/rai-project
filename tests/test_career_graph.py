"""
Unit tests for CareerSkillGraph ontology, DAG invariants, and Cypher generation.
"""

import networkx as nx
import pytest

from src.graph.career_graph import GRAPH_EDGES, GRAPH_NODES, career_graph


def test_graph_node_and_edge_counts():
    """Verify that the DAG ontology has at least 42 nodes and 40 directed edges."""
    assert len(GRAPH_NODES) >= 42
    assert len(GRAPH_EDGES) >= 40
    assert len(career_graph.graph.nodes) >= 42
    assert len(career_graph.graph.edges) >= 40


def test_graph_is_directed_acyclic():
    """Verify that the prerequisite ontology forms a strict Directed Acyclic Graph (no cyclic loops)."""
    assert nx.is_directed_acyclic_graph(career_graph.graph), "Career graph contains cyclic dependencies!"


def test_direct_prerequisites():
    """Verify direct prerequisite resolution for core tech skills."""
    dl_prereqs = career_graph.get_prerequisites("Deep_Learning")
    assert "ML_Foundations" in dl_prereqs

    algo_prereqs = career_graph.get_prerequisites("Advanced_Algorithms")
    assert "Algorithms_Basics" in algo_prereqs

    dist_prereqs = career_graph.get_prerequisites("Distributed_Systems")
    assert "Linux_Internals" in dist_prereqs or "Networking_Basics" in dist_prereqs

    # Unknown skill
    assert career_graph.get_prerequisites("Nonexistent_Skill_123") == []


def test_transitive_ancestor_prerequisites():
    """Verify topological ancestry resolution for advanced tier skills."""
    ancestors = career_graph.get_all_ancestor_prerequisites("LLM_Application_Dev")
    assert len(ancestors) > 0
    # Must include earlier math or programming fundamentals
    assert any(x in ancestors for x in ["Python_Basics", "Data_Analysis_Pandas", "Linear_Algebra", "Deep_Learning"])

    # Topological order: Python_Basics should appear before Deep_Learning if both present
    if "Python_Basics" in ancestors and "Deep_Learning" in ancestors:
        assert ancestors.index("Python_Basics") < ancestors.index("Deep_Learning")

    assert career_graph.get_all_ancestor_prerequisites("Unknown_Skill") == []


def test_check_prerequisites_detects_violations():
    """Verify that skipping prerequisite steps produces structured violation reports."""
    existing_skills = ["Python_Basics"]
    # Trying to jump straight into Deep Learning without Math or ML Foundations
    proposed = ["Deep_Learning", "LLM_Application_Dev"]

    violations = career_graph.check_prerequisites(existing_skills, proposed)
    assert len(violations) > 0

    violated_milestones = [v["milestone"] for v in violations]
    assert "Deep_Learning" in violated_milestones

    missing = [v["missing_prerequisite"] for v in violations]
    assert "ML_Foundations" in missing


def test_check_prerequisites_satisfied_sequence():
    """Verify that a correctly ordered curriculum produces zero violations."""
    existing = ["Python_Basics", "Linear_Algebra", "Probability_Stats"]
    proposed = [
        "Data_Analysis_Pandas",
        "ML_Foundations",
        "Deep_Learning"
    ]
    violations = career_graph.check_prerequisites(existing, proposed)
    assert len(violations) == 0


def test_topological_curriculum_generation():
    """Verify that topological sorting generates a valid ordered path from foundations to target."""
    target_skills = ["Deep_Learning"]
    existing = ["Python_Basics"]

    curriculum = career_graph.get_topological_curriculum(target_skills, existing)
    assert len(curriculum) > 0
    assert "Deep_Learning" in curriculum

    # Verify Deep_Learning appears at the end
    assert curriculum[-1] == "Deep_Learning"

    # Verify if ML_Foundations is included, it is before Deep_Learning
    if "ML_Foundations" in curriculum:
        assert curriculum.index("ML_Foundations") < curriculum.index("Deep_Learning")


def test_cypher_export():
    """Verify that the generated Cypher script contains valid MERGE statements."""
    cypher = career_graph.export_cypher_script()
    assert "MERGE (s:Skill" in cypher
    assert "PREREQUISITE_FOR" in cypher
    assert "Python_Basics" in cypher
    assert "Deep_Learning" in cypher


def test_sync_to_neo4j_fallback():
    """Verify graceful fallback when Neo4j instance is not running locally."""
    res = career_graph.sync_to_neo4j(uri="bolt://localhost:9999")
    assert res["status"] in ["success", "fallback"]
    assert "message" in res
