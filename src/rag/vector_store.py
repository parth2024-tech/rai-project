#!/usr/bin/env python3
"""
Vector Store & Retrieval Engine for Public Course & Role Data
Uses ChromaDB to index:
- Public Course Curriculum (ACM/IEEE CS2023, MIT OCW, Berkeley CS61, Stanford)
- Public Role Classifications (O*NET & BLS Standard Occupational Classifications)
Computes Evidence Diversity metric (Shannon Entropy of cited sources).
"""

import json
import math
import os
from typing import Any

import chromadb

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data")
COURSE_FILE = os.path.join(DATA_DIR, "public_courses.json")
ROLE_FILE = os.path.join(DATA_DIR, "public_roles.json")


class EvidenceVectorStore:
    """Manages ChromaDB vector indexing and retrieval for course and role evidence."""

    def __init__(self, persist_dir: str | None = None):
        if persist_dir:
            self.client = chromadb.PersistentClient(path=persist_dir)
        else:
            self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection(
            name="public_career_evidence",
            metadata={"description": "Public ACM course curricula and O*NET career roles"}
        )
        self._ensure_indexed()

    def _ensure_indexed(self):
        """Indexes public course and role data if collection is empty."""
        if self.collection.count() > 0:
            return

        documents = []
        metadatas = []
        ids = []

        # 1. Ingest Courses
        if os.path.exists(COURSE_FILE):
            with open(COURSE_FILE, "r", encoding="utf-8") as f:
                courses = json.load(f)
            for c in courses:
                doc_text = (
                    f"Course Title: {c['title']}. Source: {c['source']}. Domain: {c['domain']}. "
                    f"Level: {c['level']}. Competencies taught: {', '.join(c['competencies'])}. "
                    f"Prerequisites: {', '.join(c['prerequisites']) if c['prerequisites'] else 'None'}. "
                    f"Workload: {c['workload_hours']} hours. Cost: {c['cost']}."
                )
                documents.append(doc_text)
                metadatas.append({
                    "type": "course",
                    "id": c["course_id"],
                    "title": c["title"],
                    "source": c["source"],
                    "domain": c["domain"],
                    "level": c["level"],
                    "workload_hours": c["workload_hours"],
                    "cost": c["cost"],
                    "url": c["url"]
                })
                ids.append(f"course_{c['course_id']}")

        # 2. Ingest Roles
        if os.path.exists(ROLE_FILE):
            with open(ROLE_FILE, "r", encoding="utf-8") as f:
                roles = json.load(f)
            for r in roles:
                doc_text = (
                    f"Role: {r['role_title']} ({r['short_title']}). SOC Code: {r['soc_code']}. "
                    f"Domain: {r['domain']}. Description: {r['description']}. "
                    f"Core Skills: {', '.join(r['core_skills'])}. Market Growth: {r['market_growth_rate']}. "
                    f"Salary Band: {r['entry_salary_band_inr']}. Saturation Risk: {r['saturation_risk']}. "
                    f"Prerequisite Depth: {r['prerequisite_depth']}."
                )
                documents.append(doc_text)
                metadatas.append({
                    "type": "role",
                    "id": r["soc_code"],
                    "title": r["role_title"],
                    "source": r["source"],
                    "domain": r["domain"],
                    "salary_band": r["entry_salary_band_inr"],
                    "saturation_risk": r["saturation_risk"],
                    "timeline_months": r["typical_timeline_months"],
                    "url": f"https://www.onetonline.org/link/summary/{r['soc_code']}"
                })
                ids.append(f"role_{r['soc_code']}")

        if documents:
            self.collection.add(
                documents=documents,
                metadatas=metadatas,
                ids=ids
            )

    def retrieve_evidence(self, query: str, top_k: int = 5) -> list[dict[str, Any]]:
        """Retrieves top-k grounded evidence documents matching the query."""
        results = self.collection.query(
            query_texts=[query],
            n_results=min(top_k, self.collection.count())
        )
        evidence = []
        if results and "metadatas" in results and results["metadatas"]:
            for meta, doc, dist in zip(results["metadatas"][0], results["documents"][0], results["distances"][0] if results.get("distances") else [0.0]*len(results["metadatas"][0])):
                item = dict(meta)
                item["snippet"] = doc
                item["relevance_score"] = round(1.0 / (1.0 + float(dist)), 3) if dist is not None else 1.0
                evidence.append(item)
        return evidence

    @staticmethod
    def calculate_evidence_diversity(evidence_items: list[dict[str, Any]]) -> float:
        """
        Calculates Shannon Entropy (Evidence Diversity) across cited source domains.
        H_div = - sum(p * log2(p)). Returns a normalized score between 0.0 and 1.0.
        """
        if not evidence_items:
            return 0.0
        domain_counts: dict[str, int] = {}
        for item in evidence_items:
            dom = item.get("domain", "General")
            domain_counts[dom] = domain_counts.get(dom, 0) + 1

        total = len(evidence_items)
        entropy = 0.0
        for cnt in domain_counts.values():
            p = cnt / total
            if p > 0:
                entropy -= p * math.log2(p)

        # Normalize by maximum possible entropy log2(N)
        max_entropy = math.log2(total) if total > 1 else 1.0
        normalized_diversity = round(entropy / max_entropy, 3) if max_entropy > 0 else 0.0
        return normalized_diversity


# Global Singleton Instance
vector_store = EvidenceVectorStore()
