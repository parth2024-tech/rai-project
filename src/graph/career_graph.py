#!/usr/bin/env python3
"""
Career-Skill Knowledge Graph & Prerequisite DAG
Implements:
- 42-node prerequisite DAG ontology across 9 technical tracks
- Prerequisite violation detection (Delta_prereq)
- Topological curriculum ordering
- Neo4j Cypher query generation & official neo4j driver synchronization
"""

from typing import Any

import networkx as nx

# Node Definitions: 42 Nodes
GRAPH_NODES = [
    # Programming Foundations
    {"id": "Python_Basics", "label": "Python Basics", "category": "Programming", "tier": 1},
    {"id": "Python_OOP", "label": "Python OOP", "category": "Programming", "tier": 2},
    {"id": "C_Basics", "label": "C Basics", "category": "Programming", "tier": 1},
    {"id": "Pointers_Memory", "label": "Pointers & Memory", "category": "Programming", "tier": 2},
    {"id": "Java_Basics", "label": "Java Basics", "category": "Programming", "tier": 1},

    # Mathematical Foundations
    {"id": "Discrete_Math", "label": "Discrete Mathematics", "category": "Mathematics", "tier": 1},
    {"id": "Linear_Algebra", "label": "Linear Algebra", "category": "Mathematics", "tier": 2},
    {"id": "Probability_Stats", "label": "Probability & Statistics", "category": "Mathematics", "tier": 2},

    # Data Structures & Algorithms
    {"id": "Data_Structures", "label": "Data Structures", "category": "Algorithms", "tier": 2},
    {"id": "Algorithms_Basics", "label": "Algorithms Basics", "category": "Algorithms", "tier": 2},
    {"id": "Advanced_Algorithms", "label": "Advanced Algorithms", "category": "Algorithms", "tier": 3},

    # Systems & Architecture
    {"id": "Computer_Architecture", "label": "Computer Architecture", "category": "Systems", "tier": 2},
    {"id": "OS_Basics", "label": "Operating Systems", "category": "Systems", "tier": 3},
    {"id": "Concurrency_Threads", "label": "Concurrency & Multithreading", "category": "Systems", "tier": 3},
    {"id": "Linux_Internals", "label": "Linux Internals & Kernel", "category": "Systems", "tier": 3},
    {"id": "Networking_Basics", "label": "Computer Networks", "category": "Systems", "tier": 3},
    {"id": "Distributed_Systems", "label": "Distributed Systems", "category": "Systems", "tier": 4},
    {"id": "System_Design", "label": "High-Level System Design", "category": "Systems", "tier": 4},

    # Databases
    {"id": "Relational_DB", "label": "Relational Databases", "category": "Databases", "tier": 1},
    {"id": "SQL_Queries", "label": "SQL & Query Tuning", "category": "Databases", "tier": 2},
    {"id": "DB_Indexing_Normalisation", "label": "Indexing & Normalization", "category": "Databases", "tier": 2},
    {"id": "NoSQL_DB", "label": "NoSQL & Document Stores", "category": "Databases", "tier": 3},

    # Web & Software Engineering
    {"id": "Web_Basics_HTML_CSS", "label": "HTML & CSS", "category": "Web", "tier": 1},
    {"id": "JavaScript_Basics", "label": "JavaScript Basics", "category": "Web", "tier": 1},
    {"id": "Backend_Frameworks", "label": "Backend Frameworks (FastAPI/Django)", "category": "Web", "tier": 2},
    {"id": "REST_APIs", "label": "RESTful API Architecture", "category": "Web", "tier": 2},

    # DevOps & Infrastructure
    {"id": "Git_Version_Control", "label": "Git Version Control", "category": "DevOps", "tier": 1},
    {"id": "Docker_Containers", "label": "Docker Containerization", "category": "DevOps", "tier": 2},
    {"id": "CI_CD_Pipelines", "label": "CI/CD & GitHub Actions", "category": "DevOps", "tier": 3},

    # Machine Learning & AI
    {"id": "Data_Analysis_Pandas", "label": "Pandas & Data Wrangling", "category": "AI", "tier": 2},
    {"id": "ML_Foundations", "label": "Machine Learning Foundations", "category": "AI", "tier": 3},
    {"id": "Deep_Learning", "label": "Deep Learning & Neural Nets", "category": "AI", "tier": 3},
    {"id": "NLP_Basics", "label": "NLP & Transformers", "category": "AI", "tier": 4},
    {"id": "LLM_Application_Dev", "label": "LLM Apps & RAG", "category": "AI", "tier": 4},
    {"id": "MLOps", "label": "MLOps & Model Deployment", "category": "AI", "tier": 4},

    # Cybersecurity
    {"id": "Security_Fundamentals", "label": "Security Fundamentals", "category": "Security", "tier": 2},
    {"id": "Cryptography_Basics", "label": "Applied Cryptography", "category": "Security", "tier": 3},

    # Cloud & Retrieval
    {"id": "Cloud_Architecture", "label": "Cloud Infrastructure & AWS/GCP", "category": "DevOps", "tier": 3},
    {"id": "Information_Retrieval", "label": "Information Retrieval & Vector DB", "category": "AI", "tier": 4},
    {"id": "Ethical_AI_Fairness", "label": "Ethical AI & Fairness Governance", "category": "AI", "tier": 4},

    # Mobile Development
    {"id": "Mobile_SDK", "label": "Android SDK / Kotlin", "category": "Mobile", "tier": 2},
    {"id": "Mobile_App_Dev", "label": "Full Mobile App Development", "category": "Mobile", "tier": 3}
]

# Directed Prerequisite Edges (source -> target means source is PREREQUISITE_FOR target)
GRAPH_EDGES = [
    # Math & CS Core
    ("Discrete_Math", "Data_Structures"),
    ("Python_Basics", "Python_OOP"),
    ("Python_Basics", "Data_Structures"),
    ("Data_Structures", "Algorithms_Basics"),
    ("Algorithms_Basics", "Advanced_Algorithms"),

    # Systems Track
    ("C_Basics", "Pointers_Memory"),
    ("Pointers_Memory", "Computer_Architecture"),
    ("Computer_Architecture", "OS_Basics"),
    ("OS_Basics", "Concurrency_Threads"),
    ("Concurrency_Threads", "Linux_Internals"),
    ("OS_Basics", "Networking_Basics"),
    ("Linux_Internals", "Distributed_Systems"),
    ("Networking_Basics", "Distributed_Systems"),

    # Databases Track
    ("Relational_DB", "SQL_Queries"),
    ("SQL_Queries", "DB_Indexing_Normalisation"),
    ("DB_Indexing_Normalisation", "NoSQL_DB"),

    # Web & Backend Track
    ("Web_Basics_HTML_CSS", "JavaScript_Basics"),
    ("Python_OOP", "Backend_Frameworks"),
    ("SQL_Queries", "Backend_Frameworks"),
    ("JavaScript_Basics", "REST_APIs"),
    ("Backend_Frameworks", "REST_APIs"),
    ("REST_APIs", "System_Design"),
    ("Distributed_Systems", "System_Design"),

    # DevOps Track
    ("Git_Version_Control", "CI_CD_Pipelines"),
    ("OS_Basics", "Docker_Containers"),
    ("Docker_Containers", "CI_CD_Pipelines"),

    # Machine Learning Track
    ("Python_Basics", "Data_Analysis_Pandas"),
    ("Linear_Algebra", "ML_Foundations"),
    ("Probability_Stats", "ML_Foundations"),
    ("Data_Analysis_Pandas", "ML_Foundations"),
    ("ML_Foundations", "Deep_Learning"),
    ("Deep_Learning", "NLP_Basics"),
    ("NLP_Basics", "LLM_Application_Dev"),
    ("REST_APIs", "LLM_Application_Dev"),
    ("Deep_Learning", "MLOps"),
    ("Docker_Containers", "MLOps"),

    # Security Track
    ("Networking_Basics", "Security_Fundamentals"),
    ("Discrete_Math", "Cryptography_Basics"),
    ("Security_Fundamentals", "Cryptography_Basics"),

    # Cloud, Retrieval & Ethics Tracks
    ("Docker_Containers", "Cloud_Architecture"),
    ("Cloud_Architecture", "Distributed_Systems"),
    ("Data_Structures", "Information_Retrieval"),
    ("Information_Retrieval", "LLM_Application_Dev"),
    ("ML_Foundations", "Ethical_AI_Fairness"),

    # Mobile Track
    ("Java_Basics", "Mobile_SDK"),
    ("Mobile_SDK", "Mobile_App_Dev"),
    ("REST_APIs", "Mobile_App_Dev")
]


class CareerSkillGraph:
    """Encapsulates the 42-node Prerequisite Knowledge Graph."""

    def __init__(self):
        self.graph = nx.DiGraph()
        for node in GRAPH_NODES:
            self.graph.add_node(node["id"], **node)
        self.graph.add_edges_from(GRAPH_EDGES)

    def get_prerequisites(self, skill: str) -> list[str]:
        """Returns direct prerequisites for a given skill."""
        if skill not in self.graph:
            return []
        return list(self.graph.predecessors(skill))

    def get_all_ancestor_prerequisites(self, skill: str) -> list[str]:
        """Returns all transitive prerequisite skills in topological order."""
        if skill not in self.graph:
            return []
        ancestors = nx.ancestors(self.graph, skill)
        # Sort in topological order
        sub = self.graph.subgraph(ancestors | {skill})
        ordered = [n for n in nx.topological_sort(sub) if n != skill]
        return ordered

    def check_prerequisites(self, existing_skills: list[str], proposed_milestones: list[str]) -> list[dict[str, Any]]:
        """
        Detects missing prerequisite violations.
        A violation occurs if a milestone M requires P, but P is neither in existing_skills
        nor appears before M in proposed_milestones.
        """
        known = set(existing_skills)
        violations = []
        for idx, milestone in enumerate(proposed_milestones):
            if milestone not in self.graph:
                continue
            prereqs = self.get_prerequisites(milestone)
            for p in prereqs:
                if p not in known:
                    violations.append({
                        "milestone": milestone,
                        "missing_prerequisite": p,
                        "milestone_index": idx,
                        "rule": f"Cannot learn '{milestone}' before completing prerequisite '{p}'."
                    })
            known.add(milestone)
        return violations

    def get_topological_curriculum(self, target_skills: list[str], existing_skills: list[str]) -> list[str]:
        """Generates a strictly valid prerequisite-respecting curriculum sequence."""
        needed_nodes = set()
        for t in target_skills:
            if t in self.graph:
                needed_nodes.add(t)
                needed_nodes.update(nx.ancestors(self.graph, t))
        needed_nodes = needed_nodes - set(existing_skills)
        if not needed_nodes:
            return []
        sub = self.graph.subgraph(needed_nodes)
        return list(nx.topological_sort(sub))

    def export_cypher_script(self) -> str:
        """Generates ready-to-run Neo4j Cypher queries for creating the career-skill graph."""
        lines = [
            "// Neo4j Career-Skill Prerequisite Graph Schema",
            "// Clear existing graph",
            "// MATCH (n) DETACH DELETE n;",
            ""
        ]
        # Nodes
        for n in GRAPH_NODES:
            cat = n["category"]
            lbl = str(n["label"]).replace("'", "\\'")
            nid = n["id"]
            tier = n["tier"]
            lines.append(f"MERGE (s:Skill {{id: '{nid}'}}) SET s.name = '{lbl}', s.category = '{cat}', s.tier = {tier};")
        
        lines.append("\n// Prerequisite Relationships")
        for src, dst in GRAPH_EDGES:
            lines.append(
                f"MATCH (p:Skill {{id: '{src}'}}), (s:Skill {{id: '{dst}'}}) "
                f"MERGE (p)-[:PREREQUISITE_FOR]->(s);"
            )
        return "\n".join(lines)

    def sync_to_neo4j(self, uri: str = "bolt://localhost:7687", auth: tuple[str, str] = ("neo4j", "password")) -> dict[str, Any]:
        """Attempts connection to Neo4j database using official driver."""
        try:
            from neo4j import GraphDatabase
            driver = GraphDatabase.driver(uri, auth=auth)
            with driver.session() as session:
                for n in GRAPH_NODES:
                    session.run(
                        "MERGE (s:Skill {id: $id}) SET s.name = $name, s.category = $cat, s.tier = $tier",
                        id=n["id"], name=n["label"], cat=n["category"], tier=n["tier"]
                    )
                for src, dst in GRAPH_EDGES:
                    session.run(
                        "MATCH (p:Skill {id: $src}), (s:Skill {id: $dst}) MERGE (p)-[:PREREQUISITE_FOR]->(s)",
                        src=src, dst=dst
                    )
            driver.close()
            return {"status": "success", "message": f"Successfully synced 42 nodes and {len(GRAPH_EDGES)} edges to Neo4j at {uri}."}
        except Exception as e:
            return {"status": "fallback", "message": f"Neo4j server not connected ({e}). Running via embedded NetworkX in-memory DAG."}


# Global Singleton Instance
career_graph = CareerSkillGraph()
