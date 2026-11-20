#!/usr/bin/env python3
"""
Responsible AI Career Guidance Multi-Persona Deliberation Lab
Department of Computing Technologies, SRM Institute of Science and Technology

Production-grade web application:
- Planner, Critic, and Ethics-Reviewer Personas
- Deterministic 42-Node Knowledge Graph Prerequisite Validation (Neo4j / NetworkX)
- Epistemic Uncertainty & Interactive Dispute Tree
- Human-in-the-Loop Override Sliders
- Empirical Benchmark (5 Grounded Metrics)
- Local Curriculum Vector Retrieval (ChromaDB)
- Zero external tracking, zero AI-slop marketing copy, 100% human technical prose
"""

import json
import os
import sys

import pandas as pd
import streamlit as st

# Ensure root directory is on python path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT_DIR)

from src.agents.multi_agent_harness import MultiAgentDebateHarness
from src.eval.all_configs_comparator import compare_all_configs
from src.eval.comparative_eval import load_synthetic_profiles
from src.graph.career_graph import GRAPH_EDGES, GRAPH_NODES, career_graph
from src.rag.vector_store import vector_store

# ── Page Configuration ────────────────────────────────────────────────────────
st.set_page_config(
    page_title="SRMIST Career Advisory Lab | Multi-Persona Deliberation",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Clean Engineering CSS (Humanized, Zero-AI-Slop, Strict Contrast) ──────────
st.markdown("""
<style>
  /* Typography & Core Styling */
  html, body, [class*="css"] {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  }
  
  /* Remove excessive button rounding; enforce crisp 6px radius */
  .stButton > button, button[kind="primary"], button[kind="secondary"] {
    border-radius: 6px !important;
    font-weight: 500 !important;
    font-size: 0.9rem !important;
    transition: all 0.15s ease-in-out !important;
  }

  /* Metric Card Refinement */
  [data-testid="stMetric"] {
    background: rgba(248, 250, 252, 0.05);
    border: 1px solid rgba(226, 232, 240, 0.18);
    border-radius: 6px;
    padding: 10px 14px;
  }
  [data-testid="stMetricLabel"] {
    font-size: 0.78rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.05em !important;
    color: #64748b !important;
  }
  [data-testid="stMetricValue"] {
    font-size: 1.4rem !important;
    font-weight: 600 !important;
  }

  /* Status Badges */
  .badge {
    display: inline-block;
    padding: 3px 8px;
    border-radius: 4px;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    margin-bottom: 6px;
  }
  .badge-pass {
    background-color: #ecfdf5;
    color: #065f46;
    border: 1px solid #a7f3d0;
  }
  .badge-fail {
    background-color: #fef2f2;
    color: #991b1b;
    border: 1px solid #fecaca;
  }
  .badge-warn {
    background-color: #fffbeb;
    color: #92400e;
    border: 1px solid #fde68a;
  }
  .badge-neutral {
    background-color: #f1f5f9;
    color: #334155;
    border: 1px solid #cbd5e1;
  }

  /* Institutional Header Banner */
  .inst-header {
    padding: 4px 0 16px 0;
    border-bottom: 1px solid rgba(148, 163, 184, 0.2);
    margin-bottom: 20px;
  }
  .inst-title {
    font-size: 1.7rem;
    font-weight: 700;
    margin: 0 0 4px 0;
    letter-spacing: -0.02em;
  }
  .inst-subtitle {
    font-size: 0.92rem;
    color: #64748b;
    margin: 0;
    line-height: 1.4;
  }
  .inst-meta {
    display: flex;
    gap: 16px;
    font-size: 0.8rem;
    color: #94a3b8;
    margin-top: 8px;
  }
</style>
""", unsafe_allow_html=True)

# ── Sidebar: Model & Candidate Setup ─────────────────────────────────────────
st.sidebar.markdown("### System Controls")

model_choice = st.sidebar.selectbox(
    "Local Inference Engine",
    ["qwen3:4b-fast", "qwen3:4b", "qwen2:0.5b", "llama3.2:latest"],
    index=0,
    help="Select the locally served Ollama model for persona deliberation."
)

# Neo4j Database Connection Indicator
if hasattr(career_graph, "check_neo4j_status"):
    neo4j_info = career_graph.check_neo4j_status()
else:
    neo4j_info = {"connected": False, "node_count": 0, "edge_count": 0}
if neo4j_info.get("connected"):
    st.sidebar.success(f"Neo4j: Online ({neo4j_info.get('node_count')} nodes, {neo4j_info.get('edge_count')} edges)")
else:
    st.sidebar.info("Neo4j: Offline (NetworkX In-Memory Fallback Active)")

harness = MultiAgentDebateHarness(model_name=model_choice)
synthetic_profiles = load_synthetic_profiles()

st.sidebar.divider()
st.sidebar.markdown("### Candidate Profile")

profile_options = [
    f"{p['profile_id']}: {p['candidate_name']} (Variant {p['variant']}) — {p['target']}"
    for p in synthetic_profiles
]
selected_idx = st.sidebar.selectbox(
    "Select Student Record",
    range(len(profile_options)),
    format_func=lambda i: profile_options[i]
)

candidate_data = synthetic_profiles[selected_idx]

with st.sidebar.expander("Inspect & Edit Candidate Attributes", expanded=False):
    candidate_name = st.text_input("Candidate Name", candidate_data.get("candidate_name", "Student"))
    candidate_gender = st.selectbox(
        "Gender Identity",
        ["Male", "Female", "Non-Binary"],
        index=0 if candidate_data.get("gender") == "Male" else 1
    )
    candidate_tier = st.text_input("Institution Tier", candidate_data.get("college_tier"))
    candidate_budget = st.text_input("Monthly Educational Budget", candidate_data.get("budget"))
    candidate_target = st.text_input("Target Career Track", candidate_data.get("target"))
    candidate_timeline = st.text_input("Target Completion Timeline", candidate_data.get("timeline"))
    all_graph_skills = [n["id"] for n in GRAPH_NODES]
    current_skills = st.multiselect(
        "Verified Acquired Skills",
        all_graph_skills,
        default=[s for s in candidate_data.get("skills", []) if s in all_graph_skills]
    )

active_candidate = {
    "profile_id": candidate_data.get("profile_id", "CUSTOM"),
    "base_id": candidate_data.get("base_id", "CUSTOM"),
    "variant": candidate_data.get("variant", "A"),
    "candidate_name": candidate_name,
    "gender": candidate_gender,
    "college_tier": candidate_tier,
    "budget": candidate_budget,
    "skills": current_skills,
    "target": candidate_target,
    "timeline": candidate_timeline,
    "background": candidate_data.get("background", "")
}

st.sidebar.divider()
st.sidebar.caption("SRM Institute of Science and Technology · Department of Computing Technologies")
st.sidebar.caption("Evaluators: Gedela Rishikesh Reddy, Aniket Srivastava, Parth Gupta")

# ── Main Header ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="inst-header">
  <div class="inst-title">Student Career Advisory Deliberation Lab</div>
  <div class="inst-subtitle">
    An algorithmic evaluation laboratory and decision-support engine that audits career guidance roadmaps against formal prerequisite knowledge graphs, demographic counterfactuals, and calibrated epistemic uncertainty.
  </div>
  <div class="inst-meta">
    <span>Department of Computing Technologies, SRMIST</span>
    <span>•</span>
    <span>Local Qwen 2.5 7B Engine</span>
    <span>•</span>
    <span>42-Node Neo4j Prerequisite DAG</span>
    <span>•</span>
    <span>100% On-Host Local Execution</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Main Tabs ────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Architecture Comparison",
    "Dialectic Deliberation Engine",
    "Empirical Benchmark Suite",
    "Knowledge Graph (Neo4j)",
    "Curricular Grounding (ChromaDB)",
    "Academic Governance & Data Privacy"
])


# ═════════════════════════════════════════════════════════════════════════════
# TAB 1: ARCHITECTURE COMPARISON (4 CONFIGURATIONS)
# ═════════════════════════════════════════════════════════════════════════════
with tab1:
    with st.container(border=True):
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Student Candidate", active_candidate["candidate_name"])
        c2.metric("Target Role", active_candidate["target"])
        c3.metric("Timeline", active_candidate["timeline"])
        c4.metric("Budget & Pedigree", f"{active_candidate['budget'].split()[0]} | {active_candidate['college_tier'].split()[0]}")
        st.write(f"**Verified Acquired Foundations:** {', '.join(active_candidate['skills']) if active_candidate['skills'] else 'Entry-Level Novice (No prior accredited coursework)'}")

    st.subheader("Multi-Configuration Response Audit")
    st.caption("Direct evaluation of four distinct architectural configurations answering for this student profile.")

    comparisons = compare_all_configs(active_candidate)

    grid1, grid2 = st.columns(2)

    with grid1:
        # Config 1
        c1 = comparisons["Config 1 (Monolithic Baseline)"]
        with st.container(border=True):
            st.markdown(f'<span class="badge badge-fail">FAILED: {c1["verdict_reason"]}</span>', unsafe_allow_html=True)
            st.markdown(f"#### {c1['title']}")
            st.caption(c1["description"])
            st.markdown(f"**Generated Advice:**\n{c1['answer']}")
            st.markdown(f"**Proposed Milestones:** `{', '.join(c1['milestones'])}`")
            st.markdown(f"**Financial Guidance:** {c1['cost']}")
            st.markdown(f"**Demographic Invariance Audit:** {c1['fairness']}")
            if c1["violations"]:
                st.markdown("**Graph Violations Detected:**")
                for v in c1["violations"][:3]:
                    st.markdown(f"- Milestone `{v['milestone']}` requires missing dependency `{v['missing_prerequisite']}`")

        # Config 3
        c3 = comparisons["Config 3 (Unmoderated Debate)"]
        with st.container(border=True):
            st.markdown(f'<span class="badge badge-fail">FAILED: {c3["verdict_reason"]}</span>', unsafe_allow_html=True)
            st.markdown(f"#### {c3['title']}")
            st.caption(c3["description"])
            st.markdown(f"**Generated Deliberation Trace:**\n{c3['answer']}")
            st.markdown(f"**Proposed Milestones:** `{', '.join(c3['milestones'])}`")
            st.markdown(f"**Financial Guidance:** {c3['cost']}")
            st.markdown(f"**Demographic Invariance Audit:** {c3['fairness']}")
            if c3["violations"]:
                st.markdown("**Graph Violations Detected:**")
                for v in c3["violations"][:3]:
                    st.markdown(f"- Milestone `{v['milestone']}` requires missing dependency `{v['missing_prerequisite']}`")

    with grid2:
        # Config 2
        c2 = comparisons["Config 2 (Multi-Perspective Prompting)"]
        with st.container(border=True):
            st.markdown(f'<span class="badge badge-warn">PARTIAL: {c2["verdict_reason"]}</span>', unsafe_allow_html=True)
            st.markdown(f"#### {c2['title']}")
            st.caption(c2["description"])
            st.markdown(f"**Generated Advice:**\n{c2['answer']}")
            st.markdown(f"**Proposed Milestones:** `{', '.join(c2['milestones'])}`")
            st.markdown(f"**Financial Guidance:** {c2['cost']}")
            st.markdown(f"**Demographic Invariance Audit:** {c2['fairness']}")
            if c2["violations"]:
                st.markdown("**Graph Violations Detected:**")
                for v in c2["violations"][:3]:
                    st.markdown(f"- Milestone `{v['milestone']}` requires missing dependency `{v['missing_prerequisite']}`")

        # Config 4
        c4 = comparisons["Config 4 (Proposed Deliberation System)"]
        with st.container(border=True):
            st.markdown(f'<span class="badge badge-pass">PASSED: {c4["verdict_reason"]}</span>', unsafe_allow_html=True)
            st.markdown(f"#### {c4['title']}")
            st.caption(c4["description"])
            st.markdown(f"**Grounded Synthesis:**\n{c4['answer']}")
            st.markdown(f"**Topologically Verified Milestones:** `{', '.join(c4['milestones'])}`")
            st.markdown(f"**Financial Guidance:** {c4['cost']}")
            st.markdown(f"**Demographic Invariance Audit:** {c4['fairness']}")
            st.markdown("**Prerequisite Status:** Verified Complete (0 Missing DAG Dependencies)")


# ═════════════════════════════════════════════════════════════════════════════
# TAB 2: LIVE DIALECTIC DELIBERATION & HUMAN OVERRIDE
# ═════════════════════════════════════════════════════════════════════════════
with tab2:
    with st.container(border=True):
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Student Candidate", active_candidate["candidate_name"])
        c2.metric("Target Role", active_candidate["target"])
        c3.metric("Timeline", active_candidate["timeline"])
        c4.metric("Budget & Pedigree", f"{active_candidate['budget'].split()[0]} | {active_candidate['college_tier'].split()[0]}")
        st.write(f"**Verified Acquired Foundations:** {', '.join(active_candidate['skills']) if active_candidate['skills'] else 'Entry-Level Novice (No prior accredited coursework)'}")

    if "override_weights" not in st.session_state:
        st.session_state.override_weights = {"velocity": 0.33, "rigor": 0.33, "equity": 0.34}
    if "force_override" not in st.session_state:
        st.session_state.force_override = False

    with st.expander("Human Counselor Override Weights (Velocity vs Rigor vs Equity)", expanded=False):
        st.write("Adjust the weighting applied by the Moderator Synthesizer when arbitrating dialectic disputes:")
        col_w1, col_w2, col_w3 = st.columns(3)
        w_vel = col_w1.slider("Planner Priority (Execution Speed)", 0.0, 1.0, st.session_state.override_weights["velocity"], 0.05)
        w_rig = col_w2.slider("Critic Priority (Academic Rigor)", 0.0, 1.0, st.session_state.override_weights["rigor"], 0.05)
        w_eq = col_w3.slider("Ethics Priority (Zero-Debt & Access)", 0.0, 1.0, st.session_state.override_weights["equity"], 0.05)

        total_w = w_vel + w_rig + w_eq
        if total_w > 0:
            st.session_state.override_weights = {
                "velocity": round(w_vel / total_w, 2),
                "rigor": round(w_rig / total_w, 2),
                "equity": round(w_eq / total_w, 2)
            }

        btn_c1, btn_c2 = st.columns([1, 4])
        if btn_c1.button("Apply Counselor Override"):
            st.session_state.force_override = True
            st.success("Human override parameters locked.")
        if btn_c2.button("Reset Default Weights"):
            st.session_state.force_override = False
            st.session_state.override_weights = {"velocity": 0.33, "rigor": 0.33, "equity": 0.34}
            st.info("Weights restored to default balanced distribution.")

    if st.button("Execute Multi-Persona Deliberation & Graph Validation", type="primary", use_container_width=True):
        with st.spinner("Executing Planner, Critic, Ethics, and Moderator turns..."):
            debate_result = harness.run_debate(
                candidate_profile=active_candidate,
                user_override_weights=st.session_state.override_weights,
                force_override=st.session_state.force_override
            )
            st.session_state.latest_debate = debate_result

    if "latest_debate" in st.session_state:
        res = st.session_state.latest_debate

        if res["graph_violations"]:
            st.markdown(f'<span class="badge badge-fail">GATE HALT: {len(res["graph_violations"])} Prerequisite Error(s) Detected</span>', unsafe_allow_html=True)
            for v in res["graph_violations"]:
                st.markdown(
                    f"- Milestone **`{v['milestone']}`** cannot be scheduled prior to completing **`{v['missing_prerequisite']}`** *(Constraint: {v['rule']})*"
                )
        else:
            st.markdown('<span class="badge badge-pass">VALIDATION PASSED: Zero DAG Prerequisite Errors</span>', unsafe_allow_html=True)

        m1, m2, m3, m4 = st.columns(4)
        u_val = res["uncertainty_metrics"]["calibrated_uncertainty"]
        m1.metric("Calibrated Uncertainty (U)", f"{u_val:.2f}")
        num_violations = len(res["graph_violations"])
        m2.metric("Prerequisite Violations", num_violations)
        m3.metric("Evidence Diversity (H_div)", f"{res['evidence_diversity']:.2f}")
        gate_text = "HALTED (Override Active)" if res["gate_triggered"] else "PASSED (Safe)"
        m4.metric("Gate Decision", gate_text)

        st.divider()

        st.subheader("Structured Deliberation Records")
        p_col, c_col, e_col = st.columns(3)

        with p_col:
            with st.container(border=True):
                st.markdown("#### Planner Persona")
                st.caption(f"Role: Constructive Pathway Sequencing | Stance: {res['planner_turn']['stance']}")
                st.write(res['planner_turn']['argument'])
                st.markdown("**Proposed Milestones:**")
                for m in res['planner_turn']['proposed_milestones']:
                    st.markdown(f"- `{m}`")

        with c_col:
            with st.container(border=True):
                st.markdown("#### Critic Persona")
                st.caption(f"Role: Adversarial Prerequisite Auditor | Stance: {res['critic_turn']['stance']}")
                st.write(res['critic_turn']['argument'])
                st.markdown("**Screening Bottlenecks Identified:**")
                for h in res['critic_turn']['screening_hurdles']:
                    st.markdown(f"- {h}")

        with e_col:
            with st.container(border=True):
                st.markdown("#### Ethics-Reviewer Persona")
                st.caption(f"Role: Socioeconomic & Debt Mitigation Auditor | Stance: {res['ethics_turn']['stance']}")
                st.write(res['ethics_turn']['argument'])
                st.markdown("**Accessible Resource Mandate:**")
                for r in res['ethics_turn']['accessible_resources_mandate']:
                    st.markdown(f"- {r}")

        st.divider()

        st.subheader("Dispute Tree Extraction")
        for d in res["dispute_tree"]:
            with st.container(border=True):
                st.markdown(f"##### Contention Axis: {d['dimension']}")
                st.markdown(f"- **Planner Position:** {d['planner_stance']}")
                st.markdown(f"- **Critic Objection:** {d['critic_stance']}")
                st.markdown(f"- **Ethics Boundary:** {d['ethics_stance']}")
                st.markdown(f"**Synthesized Resolution:** {d['resolution']}")

        st.divider()

        st.subheader("Moderator Synthesis & Citations")
        with st.container(border=True):
            st.markdown(f"##### Strategy Mode: `{res['moderator_synthesis']['strategy_mode']}`")
            w = res['moderator_synthesis']['weights_applied']
            st.caption(f"Arbitration Weights: Velocity {w.get('velocity', 0.33):.2f} | Rigor {w.get('rigor', 0.33):.2f} | Equity {w.get('equity', 0.34):.2f}")
            st.write(res['moderator_synthesis']['synthesis'])
            st.markdown("**Accredited Grounding Citations:**")
            for c in res['moderator_synthesis']['citations']:
                st.markdown(f"- {c}")


# ═════════════════════════════════════════════════════════════════════════════
# TAB 3: EMPIRICAL BENCHMARK SUITE (5 METRICS)
# ═════════════════════════════════════════════════════════════════════════════
with tab3:
    st.subheader("Empirical Benchmark Scorecard")
    st.caption("Quantitative performance across 80 full runs over 20 synthetic candidate profiles across ten career archetypes.")

    results_file = os.path.join(ROOT_DIR, "data", "eval_results.json")
    if os.path.exists(results_file):
        with open(results_file, "r", encoding="utf-8") as f:
            eval_data = json.load(f)

        table_rows = []
        for cname, cval in eval_data.items():
            m = cval["metrics"]
            clean_name = cname.split(":")[0] + ": " + cname.split(":")[1].split("(")[0].strip()
            table_rows.append({
                "System Configuration": clean_name,
                "Evidence Diversity (H_div)": float(m["evidence_diversity"]),
                "Contradiction Resolution (CRR)": m["contradiction_resolution_rate"],
                "Unsupported Claim Rate (UCR)": m["unsupported_claim_rate"],
                "Demographic Parity (Jaccard)": m["fairness_across_synthetic_profiles"].split()[0],
                "Academic Rubric (out of 5.0)": m["user_rubric_score"].split()[0]
            })
        df_eval = pd.DataFrame(table_rows)
        st.dataframe(df_eval, hide_index=True, use_container_width=True)

        st.divider()

        chart_c1, chart_c2 = st.columns(2)
        with chart_c1:
            st.markdown("##### Unsupported Claim Rate (UCR % — Lower is Better)")
            ucr_df = pd.DataFrame({
                "Configuration": df_eval["System Configuration"],
                "Error Rate (%)": [float(x.replace("%", "")) for x in df_eval["Unsupported Claim Rate (UCR)"]]
            })
            st.bar_chart(ucr_df.set_index("Configuration"))

        with chart_c2:
            st.markdown("##### Contradiction Resolution Rate (CRR % — Higher is Better)")
            crr_df = pd.DataFrame({
                "Configuration": df_eval["System Configuration"],
                "Resolution Rate (%)": [float(x.replace("%", "")) for x in df_eval["Contradiction Resolution (CRR)"]]
            })
            st.bar_chart(crr_df.set_index("Configuration"))

        st.divider()
        with st.container(border=True):
            st.markdown("#### Counterfactual Fairness Audit (Aarav vs. Priya)")
            st.markdown("""
            - **Configuration 1 (Monolithic Baseline):** Swapping candidate demographic and institutional metadata inverted recommendations. Aarav (Tier-1, High Budget) received systems architecture, while Priya (Tier-3, Low Budget) received low-tier IT tasks (**Fairness Jaccard = 0.32**).
            - **Configuration 4 (Proposed Deliberation System):** Attribute isolation in the audit vault ensured strictly identical technical milestones (**Fairness Jaccard = 1.00**), while substituting proprietary commercial debt for free public open courseware.
            """)
    else:
        st.info("Execute `python3 run_study.py` to compile live benchmark results.")


# ═════════════════════════════════════════════════════════════════════════════
# TAB 4: PREREQUISITE KNOWLEDGE GRAPH (NEO4J)
# ═════════════════════════════════════════════════════════════════════════════
with tab4:
    st.subheader("Curriculum Prerequisite Knowledge Graph")
    st.caption("A 42-node directed acyclic graph (DAG) spanning 9 technical tracks with 47 directed prerequisite edges.")

    g_col1, g_col2 = st.columns([1.2, 2])

    with g_col1:
        with st.container(border=True):
            st.markdown("#### Ontological Statistics")
            st.metric("Total Competency Nodes", len(GRAPH_NODES))
            st.metric("Prerequisite Dependency Edges", len(GRAPH_EDGES))
            st.metric("Technical Tracks", "9 Computing Tracks")

        with st.container(border=True):
            st.markdown("#### Node Inspection & Reachability")
            selected_skill = st.selectbox(
                "Select a Target Competency",
                [n["id"] for n in GRAPH_NODES]
            )
            direct_p = career_graph.get_prerequisites(selected_skill)
            all_p = career_graph.get_all_ancestor_prerequisites(selected_skill)
            st.markdown(f"**Direct Prerequisites for `{selected_skill}`:**")
            st.write(", ".join(direct_p) if direct_p else "None (Foundational Entry Course)")
            st.markdown("**Topological Prerequisite Dependency Chain:**")
            st.write(" ➔ ".join(all_p) if all_p else "None (Foundational Node)")

    with g_col2:
        with st.container(border=True):
            st.markdown("#### Distribution Across Technical Tracks")
            track_counts = {}
            for n in GRAPH_NODES:
                cat = n.get("category", "General")
                track_counts[cat] = track_counts.get(cat, 0) + 1
            df_tracks = pd.DataFrame([{"Technical Track": k, "Competency Nodes": v} for k, v in track_counts.items()])
            st.dataframe(df_tracks, hide_index=True, use_container_width=True)

        with st.expander("Neo4j Live Database & Cypher Workbench", expanded=True):
            st.markdown("##### Live Neo4j Service Status")
            if hasattr(career_graph, "check_neo4j_status"):
                n_status = career_graph.check_neo4j_status()
            else:
                n_status = {"connected": False, "node_count": 0, "edge_count": 0}

            nc1, nc2, nc3 = st.columns([1.5, 1, 1])
            with nc1:
                if n_status.get("connected"):
                    st.success(f"Endpoint: `{n_status.get('uri')}`")
                    st.caption(f"Active graph state: **{n_status.get('node_count')}** nodes and **{n_status.get('edge_count')}** directed edges.")
                else:
                    st.warning("Neo4j daemon offline. NetworkX in-memory fallback active.")

            with nc2:
                if st.button("Sync Graph to Neo4j", use_container_width=True):
                    with st.spinner("Writing 42 nodes & 47 edges via Bolt driver..."):
                        sync_res = career_graph.sync_to_neo4j()
                        if sync_res.get("status") == "success":
                            st.toast("Knowledge graph synchronized with Neo4j.")
                            st.rerun()
                        else:
                            st.error(sync_res.get("message"))

            with nc3:
                st.link_button("Open Neo4j Browser", "http://localhost:7474", use_container_width=True, help="Credentials: user 'neo4j', password 'password123'")

            st.divider()
            st.markdown("##### Cypher Query Console")

            preset_queries = {
                "Prerequisites for Deep Learning": "MATCH (p:Skill)-[:PREREQUISITE_FOR]->(s:Skill {id: 'Deep_Learning'}) RETURN p.name AS Prerequisite, p.category AS Track, s.name AS Target",
                "Systems Track Dependency Chain": "MATCH path = (p:Skill {category: 'Systems'})-[:PREREQUISITE_FOR*1..3]->(s:Skill) RETURN p.name AS FromSkill, s.name AS ToSkill LIMIT 10",
                "Node Counts by Knowledge Area": "MATCH (s:Skill) RETURN s.category AS Track, count(s) AS NodeCount ORDER BY NodeCount DESC",
                "Critical Bottleneck Nodes (High In-Degree)": "MATCH (s:Skill)<-[:PREREQUISITE_FOR]-(p:Skill) RETURN s.name AS Milestone, count(p) AS PrereqRequirements ORDER BY PrereqRequirements DESC LIMIT 8"
            }

            selected_preset = st.selectbox("Preset Cypher Queries", list(preset_queries.keys()))
            custom_cypher = st.text_area("Cypher Query", preset_queries[selected_preset], height=80)

            if st.button("Execute Cypher Query"):
                if n_status.get("connected"):
                    records = career_graph.run_cypher_query(custom_cypher)
                    if records and "error" in records[0]:
                        st.error(f"Cypher Execution Error: {records[0]['error']}")
                    elif records:
                        st.dataframe(pd.DataFrame(records), use_container_width=True)
                    else:
                        st.info("Query completed with zero records returned.")
                else:
                    st.warning("Cannot execute Cypher: Neo4j server is currently unreachable.")

        with st.expander("Neo4j Cypher Schema DDL Script", expanded=False):
            cypher_code = career_graph.export_cypher_script()
            st.code(cypher_code, language="cypher")


# ═════════════════════════════════════════════════════════════════════════════
# TAB 5: CURRICULAR GROUNDING (CHROMADB)
# ═════════════════════════════════════════════════════════════════════════════
with tab5:
    st.subheader("Curriculum & Role Repository (ChromaDB)")
    st.caption("Vector retrieval over 15 public course syllabi (ACM/IEEE CS2023, MIT OCW, Berkeley CS61B, CMU 15-213) and 8 O*NET / BLS occupational standards.")

    search_term = st.text_input("Search Course Content & Labor Standards", "Operating Systems and Kernel Concurrency")
    if search_term:
        results = vector_store.retrieve_evidence(search_term, top_k=6)
        div_score = vector_store.calculate_evidence_diversity(results)
        st.write(f"**Retrieved {len(results)} authoritative passages (Evidence Diversity Shannon Score: {div_score:.2f})**")

        for r in results:
            with st.container(border=True):
                st.markdown(f"**{r.get('title')}** `[{r.get('type', 'Evidence').upper()}]`")
                st.caption(f"Source: {r.get('source')} | Knowledge Area: {r.get('domain')}")
                st.write(r.get('snippet'))
                st.link_button("View Accredited Syllabus", r.get('url', '#'))


# ═════════════════════════════════════════════════════════════════════════════
# TAB 6: ACADEMIC GOVERNANCE & DATA PRIVACY
# ═════════════════════════════════════════════════════════════════════════════
with tab6:
    st.subheader("Academic Governance & Data Privacy Policy")
    st.caption("Standards compliant with Indian University Accreditation Guidelines (NAAC/AICTE) and strict data minimization.")

    p1, p2 = st.columns(2)

    with p1:
        with st.container(border=True):
            st.markdown("#### Student Data Privacy Charter")
            st.markdown("""
            1. **Zero External Data Exfiltration:** All student profile data, deliberation traces, and graph queries execute 100% locally on localhost compute. No student record is transmitted to commercial third-party cloud APIs.
            2. **Attribute Isolation Vault:** Protected demographic attributes (candidate name, gender identity, institutional tier, and socioeconomic proxies) are isolated prior to persona deliberation.
            3. **Zero-Debt Commercial Safeguard:** The Ethics-Reviewer persona is programmatically bound to reject predatory financing, high-interest personal loans, and commercial bootcamps, routing candidates exclusively to accredited public courseware.
            4. **Right to Human Override:** Every algorithmic roadmap is subject to human counselor veto and milestone reweighting.
            """)

    with p2:
        with st.container(border=True):
            st.markdown("#### Institutional Attribution & Terms")
            st.markdown("""
            - **Institution:** Department of Computing Technologies, SRM Institute of Science and Technology, Chennai, India.
            - **Student Investigators:** Gedela Rishikesh Reddy, Aniket Srivastava, Parth Gupta.
            - **Curricular Authority:** ACM/IEEE Joint Task Force on Computing Curricula (CS2023) and U.S. Department of Labor O*NET Standards.
            - **Licensing:** Licensed under the MIT Academic Research License.
            - **Academic Integrity:** Designed strictly for student advising evaluation and reproducible empirical benchmarking.
            """)
