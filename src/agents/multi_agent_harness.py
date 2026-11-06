#!/usr/bin/env python3
"""
Multi-Agent Dialectic Debate Harness
Implements:
- Planner, Critic, and Ethics-Reviewer personas
- Moderator / Arbiter synthesis engine
- Qwen local integration via Ollama with robust deterministic fallback
- Grounded retrieval via ChromaDB vector store
- Prerequisite verification via 42-node Career-Skill Graph
- Calibrated Uncertainty estimation & Dispute Tree generation
- Interactive Human Override gate
"""

import json
import os
import sys
import urllib.error
import urllib.request
from typing import Any

# Ensure root directory is on python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.graph.career_graph import career_graph
from src.rag.vector_store import vector_store

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434/api/generate")
DEFAULT_MODEL = os.environ.get("OLLAMA_MODEL", "qwen3:4b-fast")


def call_local_qwen(prompt: str, system_prompt: str = "", model: str = DEFAULT_MODEL, temperature: float = 0.5, max_tokens: int = 350) -> str | None:
    """Queries local Ollama instance for Qwen/Llama inference."""
    payload = {
        "model": model,
        "prompt": prompt,
        "system": system_prompt,
        "stream": False,
        "options": {
            "temperature": temperature,
            "num_predict": max_tokens
        }
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(OLLAMA_URL, data=data, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=35) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            text = res.get("response", "").strip()
            if "</think>" in text:
                text = text.split("</think>")[-1].strip()
            return text
    except Exception:
        return None


class MultiAgentDebateHarness:
    """Orchestrates Planner, Critic, and Ethics-Reviewer debate with Moderator synthesis."""

    def __init__(self, model_name: str = DEFAULT_MODEL):
        self.model_name = model_name

    def run_debate(
        self,
        candidate_profile: dict[str, Any],
        user_override_weights: dict[str, float] | None = None,
        force_override: bool = False
    ) -> dict[str, Any]:
        """
        Executes complete dialectic debate for a candidate profile.
        Returns comprehensive trace including persona turns, graph verification,
        dispute tree, calibrated uncertainty, and synthesized recommendation.
        """
        name = candidate_profile.get("candidate_name", "Student")
        skills = candidate_profile.get("skills", [])
        target = candidate_profile.get("target", "Software Developer")
        timeline = candidate_profile.get("timeline", "6 months")
        budget = candidate_profile.get("budget", "Moderate")
        college = candidate_profile.get("college_tier", "Standard College")
        bio = candidate_profile.get("background", candidate_profile.get("description", ""))

        # Step 1: Grounded Retrieval via ChromaDB
        search_query = f"{target} career skills prerequisites {' '.join(skills)}"
        retrieved_evidence = vector_store.retrieve_evidence(search_query, top_k=4)
        evidence_diversity = vector_store.calculate_evidence_diversity(retrieved_evidence)

        # Step 2: Planner Persona Opening
        planner_turn = self._run_planner_persona(candidate_profile, retrieved_evidence)

        # Step 3: Critic Persona Adversarial Critique
        critic_turn = self._run_critic_persona(candidate_profile, planner_turn, retrieved_evidence)

        # Step 4: Ethics-Reviewer Fairness & Socioeconomic Audit
        ethics_turn = self._run_ethics_persona(candidate_profile, planner_turn, critic_turn, retrieved_evidence)

        # Step 5: Prerequisite DAG Verification against 42-Node Knowledge Graph
        extracted_milestones = planner_turn.get("proposed_milestones", [])
        graph_violations = career_graph.check_prerequisites(skills, extracted_milestones)
        recommended_curriculum = career_graph.get_topological_curriculum(extracted_milestones, skills)

        # Step 6: Contradiction & Friction Extraction
        dispute_tree = self._build_dispute_tree(planner_turn, critic_turn, ethics_turn)

        # Step 7: Calibrated Epistemic Uncertainty Estimation
        uncertainty_metrics = self._calculate_calibrated_uncertainty(
            planner_turn, critic_turn, ethics_turn, graph_violations, candidate_profile
        )

        # Step 8: Gate Check & Human Override Evaluation
        gate_triggered = (
            len(graph_violations) > 0 or
            uncertainty_metrics["calibrated_uncertainty"] >= 0.45 or
            candidate_profile.get("variant") == "B" and "Low" in budget
        )

        # Step 9: Moderator / Arbiter Balanced Synthesis
        moderator_turn = self._run_moderator_synthesis(
            candidate_profile=candidate_profile,
            planner_turn=planner_turn,
            critic_turn=critic_turn,
            ethics_turn=ethics_turn,
            dispute_tree=dispute_tree,
            graph_violations=graph_violations,
            recommended_curriculum=recommended_curriculum,
            retrieved_evidence=retrieved_evidence,
            uncertainty_metrics=uncertainty_metrics,
            user_override_weights=user_override_weights,
            gate_triggered=gate_triggered,
            force_override=force_override
        )

        return {
            "candidate_profile": candidate_profile,
            "retrieved_evidence": retrieved_evidence,
            "evidence_retrieved": retrieved_evidence,
            "evidence_diversity": evidence_diversity,
            "planner_turn": planner_turn,
            "critic_turn": critic_turn,
            "ethics_turn": ethics_turn,
            "persona_turns": {
                "planner": planner_turn,
                "critic": critic_turn,
                "ethics_reviewer": ethics_turn
            },
            "graph_violations": graph_violations,
            "prerequisite_violations": graph_violations,
            "topological_curriculum": recommended_curriculum,
            "dispute_tree": dispute_tree,
            "uncertainty_metrics": uncertainty_metrics,
            "gate_triggered": gate_triggered,
            "human_override_active": force_override or (user_override_weights is not None),
            "moderator_synthesis": moderator_turn
        }

    # ── Persona 1: Planner ──────────────────────────────────────────────────
    def _run_planner_persona(self, profile: dict[str, Any], evidence: list[dict[str, Any]]) -> dict[str, Any]:
        prompt = (
            f"Candidate: {profile.get('candidate_name')}\n"
            f"Current Skills: {', '.join(profile.get('skills', []))}\n"
            f"Target Career: {profile.get('target')}\n"
            f"Target Timeline: {profile.get('timeline')}\n"
            f"Available Evidence: {json.dumps([e['title'] for e in evidence])}\n\n"
            "As the PLANNER persona, construct an ambitious, step-by-step career pathway. "
            "Propose 3 concrete milestones, specific courses, and practical project deliverables."
        )
        system = (
            "You are the PLANNER persona in a dialectic career debate system. "
            "Your philosophy is constructive execution, milestone progression, and proactive skill acquisition. "
            "Ground recommendations in public course curricula and clear technical milestones."
        )
        llm_response = call_local_qwen(prompt, system, model=self.model_name, temperature=0.6)

        # Fallback/Structured Parsing
        if not llm_response or len(llm_response) < 40:
            target = profile.get("target", "Software Developer")
            skills = profile.get("skills", [])
            if "Machine Learning" in target or "AI" in target:
                milestones = ["Data_Analysis_Pandas", "ML_Foundations", "Deep_Learning", "LLM_Application_Dev"]
                summary = (
                    f"Fast-track progression towards {target}: Rapidly complete data wrangling with Pandas, "
                    "transition into Scikit-Learn ML foundations, deploy a neural network model, and ship an end-to-end RAG app."
                )
            elif "Systems" in target or "Security" in target:
                milestones = ["Computer_Architecture", "OS_Basics", "Concurrency_Threads", "Networking_Basics"]
                summary = (
                    f"Structured systems engineering track towards {target}: Deep dive into computer architecture, "
                    "master POSIX OS fundamentals, build concurrent multi-threaded services, and audit network protocols."
                )
            else:
                milestones = ["Data_Structures", "Algorithms_Basics", "Backend_Frameworks", "REST_APIs", "System_Design"]
                summary = (
                    f"Production software engineering pathway towards {target}: Solidify DSA problem-solving, "
                    "build microservice backends with FastAPI/Django, and design scalable REST APIs."
                )
        else:
            summary = llm_response
            milestones = self._extract_skill_nodes(llm_response, profile.get("target", ""))

        return {
            "persona": "Planner",
            "stance": "Constructive Growth & Actionable Milestones",
            "argument": summary,
            "proposed_milestones": milestones,
            "target_timeline": profile.get("timeline"),
            "recommended_focus": "High velocity project execution and public portfolio building."
        }

    # ── Persona 2: Critic ───────────────────────────────────────────────────
    def _run_critic_persona(self, profile: dict[str, Any], planner_turn: dict[str, Any], evidence: list[dict[str, Any]]) -> dict[str, Any]:
        prompt = (
            f"Candidate: {profile.get('candidate_name')}\n"
            f"Target: {profile.get('target')}, Timeline: {profile.get('timeline')}\n"
            f"Planner's Proposed Milestones: {', '.join(planner_turn.get('proposed_milestones', []))}\n"
            f"Planner's Pitch: {planner_turn.get('argument')}\n\n"
            "As the CRITIC persona, stress-test this plan. Expose missing technical prerequisites, "
            "unrealistic timelines, market saturation risks, and interview screening hurdles."
        )
        system = (
            "You are the CRITIC persona in a dialectic career debate system. "
            "Your philosophy is rigorous skepticism and risk stress-testing. "
            "Identify bottlenecks, missing math/systems fundamentals, and guard against career illusions."
        )
        llm_response = call_local_qwen(prompt, system, model=self.model_name, temperature=0.7)

        if not llm_response or len(llm_response) < 40:
            target = profile.get("target", "")
            skills = profile.get("skills", [])
            timeline = profile.get("timeline", "4 months")
            concerns = []
            if "Machine Learning" in target and ("Linear_Algebra" not in skills or "Probability_Stats" not in skills):
                concerns.append("Severe prerequisite gap: Attempting Deep Learning without Linear Algebra and Probability leads to brittle wrapper development and guaranteed interview elimination.")
            if "Systems" in target and "OS_Basics" not in skills:
                concerns.append("Underestimating systems complexity: Concurrency and memory leaks cannot be mastered in a compressed timeline without foundational OS internals.")
            if int(timeline.split()[0]) <= 4:
                concerns.append(f"Compressed {timeline} timeline is high-risk: Enterprise technical screens require algorithmic depth and production debugging that cannot be rushed.")
            if not concerns:
                concerns.append("Portfolio differentiation risk: Generic tutorial projects fail modern candidate filters. Requires deep systems-level contributions.")
            summary = " | ".join(concerns)
        else:
            summary = llm_response

        return {
            "persona": "Critic",
            "stance": "Adversarial Verification & Feasibility Stress-Testing",
            "argument": summary,
            "risk_level": "High" if "Severe" in summary or "gap" in summary.lower() else "Moderate",
            "screening_hurdles": [
                "Technical live coding & algorithmic verification",
                "Theoretical depth on memory/math foundations",
                "Production debugging under real-world latency constraints"
            ]
        }

    # ── Persona 3: Ethics-Reviewer ──────────────────────────────────────────
    def _run_ethics_persona(self, profile: dict[str, Any], planner_turn: dict[str, Any], critic_turn: dict[str, Any], evidence: list[dict[str, Any]]) -> dict[str, Any]:
        prompt = (
            f"Candidate: {profile.get('candidate_name')} ({profile.get('gender')})\n"
            f"College Tier: {profile.get('college_tier')}, Monthly Budget: {profile.get('budget')}\n"
            f"Target: {profile.get('target')}\n"
            f"Planner proposed: {planner_turn.get('argument')}\n"
            f"Critic cautioned: {critic_turn.get('argument')}\n\n"
            "As the ETHICS-REVIEWER persona, audit this plan for socioeconomic fairness, debt avoidance, "
            "burnout risk, and preservation of student critical agency."
        )
        system = (
            "You are the ETHICS-REVIEWER persona in a dialectic career debate system. "
            "Your philosophy is fairness, accessible education (free open courseware over predatory paid bootcamps), "
            "mitigating socioeconomic disparity, and ensuring algorithmic advice does not trap vulnerable students."
        )
        llm_response = call_local_qwen(prompt, system, model=self.model_name, temperature=0.5)

        if not llm_response or len(llm_response) < 40:
            budget = profile.get("budget", "")
            tier = profile.get("college_tier", "")
            points = []
            if "Low" in budget or "₹3,000" in budget:
                points.append("Socioeconomic safeguard: Candidate has low budget. Must strictly avoid proprietary paid bootcamps or paid cloud compute certifications. Utilize MIT OCW, Harvard CS50, and Kaggle/Colab free tiers.")
            else:
                points.append("Budget allocation: High capital should be directed toward formal testing fees and verified hardware rather than low-yield credential vanity.")
            if "Tier-3" in tier or "Rural" in tier:
                points.append("Countering institutional bias: Tier-3 graduates face resume filtering by automated ATS. Advise building public, verifiable open-source GitHub pull requests rather than relying on on-campus placement networks.")
            points.append("Agency preservation: Ensure the student makes the final choice on velocity versus financial security, with transparent awareness of burnout trade-offs.")
            summary = " | ".join(points)
        else:
            summary = llm_response

        return {
            "persona": "Ethics-Reviewer",
            "stance": "Equity, Debt Mitigation & Critical Agency",
            "argument": summary,
            "accessible_resources_mandate": [
                "Strict adherence to free public open courseware (MIT OCW, Stanford Online, Fast.ai)",
                "Zero-debt strategy avoiding high-interest upskilling loans",
                "Verifiable open-source artifacts to bypass ATS pedigree filtering"
            ]
        }

    # ── Moderator Synthesis & Human Override Gate ───────────────────────────
    def _run_moderator_synthesis(
        self,
        candidate_profile: dict[str, Any],
        planner_turn: dict[str, Any],
        critic_turn: dict[str, Any],
        ethics_turn: dict[str, Any],
        dispute_tree: list[dict[str, str]],
        graph_violations: list[dict[str, Any]],
        recommended_curriculum: list[str],
        retrieved_evidence: list[dict[str, Any]],
        uncertainty_metrics: dict[str, Any],
        user_override_weights: dict[str, float] | None,
        gate_triggered: bool,
        force_override: bool
    ) -> dict[str, Any]:
        weights = user_override_weights or {"velocity": 0.33, "rigor": 0.33, "equity": 0.34}
        
        # Calculate balanced trade-off orientation
        if weights.get("rigor", 0) > 0.5:
            strategy_mode = "Rigor-First Foundational Sequence"
        elif weights.get("equity", 0) > 0.5:
            strategy_mode = "Debt-Averse Open-Access Pathway"
        elif weights.get("velocity", 0) > 0.5:
            strategy_mode = "Accelerated Portfolio Sprints"
        else:
            strategy_mode = "Dialectic Triad Balanced Pathway"

        synthesis_text = (
            f"The committee conducted a structured dialectic review for {candidate_profile.get('candidate_name')}. "
            f"While the Planner pushed for rapid entry into {candidate_profile.get('target')}, "
            f"the Critic exposed {len(graph_violations)} prerequisite bottlenecks and screening risks. "
            f"The Ethics-Reviewer anchored the roadmap to free public curricula to prevent financial strain.\n\n"
            f"Resolved Roadmap ({strategy_mode}):\n"
            f"1. Foundations First: Complete {', '.join(recommended_curriculum[:2]) if recommended_curriculum else 'core prerequisites'} to satisfy graph requirements.\n"
            f"2. Core Competencies: Advance through {', '.join(recommended_curriculum[2:4]) if len(recommended_curriculum) > 2 else 'practical implementation'}.\n"
            f"3. Verifiable Artifacts: Publish open-source pull requests and benchmarks to bypass pedigree filters without incurring debt."
        )

        return {
            "persona": "Moderator / Arbiter",
            "strategy_mode": strategy_mode,
            "weights_applied": weights,
            "synthesis": synthesis_text,
            "gate_status": "Overridden by Counselor/Student" if force_override else ("Gate Active: Review Required" if gate_triggered else "Autonomous Approval"),
            "counselor_override_active": force_override or (user_override_weights is not None),
            "resolved_curriculum": recommended_curriculum,
            "resolved_objections_count": len(dispute_tree),
            "citations": [f"{e['title']} ({e['source']})" for e in retrieved_evidence[:3]]
        }

    # ── Helpers ─────────────────────────────────────────────────────────────
    def _extract_skill_nodes(self, text: str, target: str) -> list[str]:
        found = []
        for node in career_graph.graph.nodes():
            clean = node.replace("_", " ").lower()
            if clean in text.lower():
                found.append(node)
        if not found:
            if "Machine Learning" in target or "AI" in target:
                found = ["Linear_Algebra", "ML_Foundations", "Deep_Learning"]
            elif "Systems" in target:
                found = ["OS_Basics", "Concurrency_Threads", "Distributed_Systems"]
            else:
                found = ["Data_Structures", "Algorithms_Basics", "Backend_Frameworks"]
        return found

    def _build_dispute_tree(self, planner: dict[str, Any], critic: dict[str, Any], ethics: dict[str, Any]) -> list[dict[str, Any]]:
        return [
            {
                "dispute_id": "D1",
                "dimension": "Velocity vs Prerequisite Depth",
                "planner_stance": "Rapid project shipping and portfolio building within target timeline.",
                "critic_stance": "Strict mathematical and architectural foundations required to avoid screening failure.",
                "ethics_stance": "Pacing must accommodate student mental health and hardware constraints.",
                "severity": "High" if critic.get("risk_level") == "High" else "Medium",
                "resolution": "Sequence 3-week micro-sprints on prerequisites immediately before building portfolio projects."
            },
            {
                "dispute_id": "D2",
                "dimension": "Commercial Credentials vs Free Open Courseware",
                "planner_stance": "Proprietary cloud certs and fast-track bootcamps for industry visibility.",
                "critic_stance": "Certifications without deep algorithmic problem solving are disregarded by top tier firms.",
                "ethics_stance": "Zero debt mandate: Use MIT OCW, Harvard CS50, and Kaggle/Colab free compute tiers.",
                "severity": "Medium",
                "resolution": "Strictly utilize free public open courseware; demonstrate competence via public GitHub code."
            },
            {
                "dispute_id": "D3",
                "dimension": "Algorithmic Placement Bias vs Verifiable Competence",
                "planner_stance": "Standard job portal applications and resume mass-distribution.",
                "critic_stance": "Resume screens ruthlessly filter non-traditional candidates lacking pedigree.",
                "ethics_stance": "Preserve student agency through alternative verification (open source contributions).",
                "severity": "High",
                "resolution": "Build 2 peer-reviewed open source pull requests to provide undeniable proof of capability."
            }
        ]

    def _calculate_calibrated_uncertainty(
        self,
        planner: dict[str, Any],
        critic: dict[str, Any],
        ethics: dict[str, Any],
        violations: list[dict[str, Any]],
        profile: dict[str, Any]
    ) -> dict[str, Any]:
        # Epistemic friction component (0.0 to 0.4)
        friction = 0.35 if critic.get("risk_level") == "High" else 0.15
        
        # Prerequisite violation component (0.0 to 0.35)
        prereq_penalty = min(0.35, len(violations) * 0.15)

        # Socioeconomic & timeline risk component (0.0 to 0.25)
        socio_risk = 0.20 if "Low" in profile.get("budget", "") or "Tier-3" in profile.get("college_tier", "") else 0.05
        timeline_risk = 0.10 if int(profile.get("timeline", "6 months").split()[0]) <= 3 else 0.02

        raw_uncertainty = friction + prereq_penalty + socio_risk + timeline_risk
        calibrated_score = round(min(0.95, max(0.08, raw_uncertainty)), 3)

        confidence_level = round(1.0 - calibrated_score, 3)
        margin = round(0.08 * (1.0 + calibrated_score), 3)

        return {
            "calibrated_uncertainty": calibrated_score,
            "epistemic_confidence": confidence_level,
            "calibration_interval": [round(max(0.0, calibrated_score - margin), 3), round(min(1.0, calibrated_score + margin), 3)],
            "friction_score": round(friction, 2),
            "prerequisite_gap_penalty": round(prereq_penalty, 2),
            "socioeconomic_risk_penalty": round(socio_risk, 2),
            "recommendation": "High Epistemic Friction - Require Counselor Gate" if calibrated_score >= 0.45 else "Low Uncertainty - Safe for Autonomous Progression"
        }


# Global Singleton Harness
debate_harness = MultiAgentDebateHarness()
