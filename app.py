#!/usr/bin/env python3
"""
Responsible AI Career Guidance Multi-Persona Debate Prototype
Streamlit Web Application featuring:
- Planner, Critic, and Ethics-Reviewer Personas
- Moderator / Arbiter Synthesis Engine
- Interactive Debate Trace Viewer
- Calibrated Uncertainty Gauge & Dispute Tree
- Human Override & Counselor Trade-Off Sliders
- Chroma Vector Store Search (ACM Curricula & O*NET Roles)
- Neo4j Career-Skill Graph (42-Node Prerequisite DAG & Cypher Exporter)
- Empirical Benchmark & Comparative Evaluation (5 Metrics)
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
from src.eval.comparative_eval import load_synthetic_profiles
from src.graph.career_graph import GRAPH_EDGES, GRAPH_NODES, career_graph
from src.rag.vector_store import vector_store

# Page Configuration
st.set_page_config(
    page_title="Responsible AI Multi-Persona Career Debate System",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (Anti-Vibe-Coding Compliant: Professional Navy/Slate, No Purple Slop)
st.markdown("""
<style>
    .main-header {
        font-size: 2.1rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #475569;
        margin-bottom: 1.5rem;
    }
    .persona-card {
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 12px;
        border: 1px solid #cbd5e1;
    }
    .planner-card {
        background-color: #f0fdf4;
        border-left: 5px solid #16a34a;
    }
    .critic-card {
        background-color: #fff1f2;
        border-left: 5px solid #e11d48;
    }
    .ethics-card {
        background-color: #f8fafc;
        border-left: 5px solid #0284c7;
    }
    .moderator-card {
        background-color: #f8fafc;
        border-left: 5px solid #475569;
    }
    .dispute-box {
        background-color: #f1f5f9;
        border-radius: 6px;
        padding: 12px;
        margin-bottom: 10px;
        border: 1px solid #e2e8f0;
    }
    .metric-badge {
        display: inline-block;
        padding: 4px 8px;
        border-radius: 4px;
        font-weight: 600;
        font-size: 0.85rem;
    }
</style>
""", unsafe_allow_html=True)


# ── Sidebar: Model & Candidate Setup ─────────────────────────────────────────
st.sidebar.title("⚙️ System Control")
st.sidebar.caption("Responsible AI Career Deliberation Platform")

model_choice = st.sidebar.selectbox(
    "Local Inference Model (Qwen/Ollama)",
    ["qwen3:4b-fast", "qwen3:4b", "qwen2:0.5b", "llama3.2:latest"],
    index=0
)

harness = MultiAgentDebateHarness(model_name=model_choice)
synthetic_profiles = load_synthetic_profiles()

st.sidebar.markdown("---")
st.sidebar.subheader("👤 Candidate Selection")

profile_options = [f"{p['profile_id']}: {p['candidate_name']} ({p['variant']}) - {p['target']}" for p in synthetic_profiles]
selected_idx = st.sidebar.selectbox(
    "Load Synthetic Profile (20 Profiles)",
    range(len(profile_options)),
    format_func=lambda i: profile_options[i]
)

candidate_data = synthetic_profiles[selected_idx]

with st.sidebar.expander("📝 Edit Candidate Attributes", expanded=False):
    candidate_name = st.text_input("Name", candidate_data.get("candidate_name", "Student"))
    candidate_gender = st.selectbox("Gender", ["Male", "Female", "Non-Binary"], index=0 if candidate_data.get("gender") == "Male" else 1)
    candidate_tier = st.text_input("College Tier / Institute", candidate_data.get("college_tier"))
    candidate_budget = st.text_input("Monthly Budget", candidate_data.get("budget"))
    candidate_target = st.text_input("Target Career Role", candidate_data.get("target"))
    candidate_timeline = st.text_input("Available Timeline", candidate_data.get("timeline"))
    all_graph_skills = [n["id"] for n in GRAPH_NODES]
    current_skills = st.multiselect(
        "Verified Skills",
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


# ── Main Tabs ────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs([
    "🗣️ Dialectic Debate & Override",
    "📊 Empirical Benchmark (5 Metrics)",
    "🌐 Career-Skill Graph (Neo4j)",
    "📚 Public Knowledge Base (Chroma)"
])


# ═════════════════════════════════════════════════════════════════════════════
# TAB 1: DIALECTIC DEBATE & HUMAN OVERRIDE
# ═════════════════════════════════════════════════════════════════════════════
with tab1:
    st.markdown('<div class="main-header">Multi-Persona Career Debate Engine</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Adversarial deliberation between Planner, Critic, and Ethics-Reviewer grounded in public course data and a 42-node prerequisite graph.</div>', unsafe_allow_html=True)

    # Candidate Summary Banner
    c1, c2, c3, c4 = st.columns([1.2, 1.2, 1.2, 1.4])
    c1.metric("Candidate", active_candidate["candidate_name"])
    c2.metric("Target Career", active_candidate["target"])
    c3.metric("Timeline", active_candidate["timeline"])
    c4.metric("Budget & College", f"{active_candidate['budget'].split()[0]} | {active_candidate['college_tier'].split()[0]}")

    st.markdown("---")

    # Override Controls in Session State
    if "override_weights" not in st.session_state:
        st.session_state.override_weights = {"velocity": 0.33, "rigor": 0.33, "equity": 0.34}
    if "force_override" not in st.session_state:
        st.session_state.force_override = False

    # Human Override Controls Expander
    with st.expander("🛠️ Human-in-the-Loop Override Panel (Counselor / Student Controls)", expanded=False):
        st.write("Adjust optimization weights to calibrate how the Moderator synthesizes conflicting persona arguments:")
        col_w1, col_w2, col_w3 = st.columns(3)
        w_vel = col_w1.slider("Planner Velocity (Speed to Market)", 0.0, 1.0, st.session_state.override_weights["velocity"], 0.05)
        w_rig = col_w2.slider("Critic Rigor (Prerequisite Depth)", 0.0, 1.0, st.session_state.override_weights["rigor"], 0.05)
        w_eq = col_w3.slider("Ethics Equity (Debt & Burnout Shield)", 0.0, 1.0, st.session_state.override_weights["equity"], 0.05)

        total_w = w_vel + w_rig + w_eq
        if total_w > 0:
            st.session_state.override_weights = {
                "velocity": round(w_vel / total_w, 2),
                "rigor": round(w_rig / total_w, 2),
                "equity": round(w_eq / total_w, 2)
            }

        btn_c1, btn_c2 = st.columns([1, 4])
        if btn_c1.button("Force Human Override"):
            st.session_state.force_override = True
            st.success("Human Override Flag Active: Committee will adopt counselor constraints.")
        if btn_c2.button("Reset to Autonomous Debate"):
            st.session_state.force_override = False
            st.session_state.override_weights = {"velocity": 0.33, "rigor": 0.33, "equity": 0.34}
            st.info("Reset to autonomous triad debate.")

    # Trigger Debate Button
    if st.button("🚀 Run Multi-Persona Deliberation", type="primary"):
        with st.spinner("Executing multi-persona deliberation loop with local Qwen and Chroma..."):
            debate_result = harness.run_debate(
                candidate_profile=active_candidate,
                user_override_weights=st.session_state.override_weights,
                force_override=st.session_state.force_override
            )
            st.session_state.latest_debate = debate_result

    # Display Debate Results
    if "latest_debate" in st.session_state:
        res = st.session_state.latest_debate
        st.markdown("### 🔍 Calibrated Uncertainty & Gate Status")

        m_col1, m_col2, m_col3, m_col4 = st.columns(4)
        u_val = res["uncertainty_metrics"]["calibrated_uncertainty"]
        m_col1.metric("Calibrated Uncertainty", f"{u_val:.2f}", delta=f"Conf: {res['uncertainty_metrics']['epistemic_confidence']:.2f}")
        m_col2.metric("Prerequisite Violations (Δ)", len(res["graph_violations"]), delta="Detected" if res["graph_violations"] else "Clean", delta_color="inverse")
        m_col3.metric("Evidence Diversity (H_div)", f"{res['evidence_diversity']:.2f}", delta="4 Sources Cited")
        gate_text = "TRIGGERED (Override Needed)" if res["gate_triggered"] else "PASSED (Safe)"
        m_col4.metric("Gate Status", gate_text, delta=res["moderator_synthesis"]["gate_status"])

        if res["graph_violations"]:
            with st.warning(f"⚠️ {len(res['graph_violations'])} Prerequisite Bottlenecks Intercepted by Knowledge Graph"):
                for v in res["graph_violations"]:
                    st.write(f"- **{v['milestone']}** requires **{v['missing_prerequisite']}** (Rule: {v['rule']})")

        st.markdown("---")
        st.markdown("### 🎭 Interactive Debate Trace Viewer")

        # 3 Personas in 3 Columns
        p_col, c_col, e_col = st.columns(3)

        with p_col:
            st.markdown(f"""
            <div class="persona-card planner-card">
                <h4>🟢 Planner Persona</h4>
                <p><strong>Stance:</strong> {res['planner_turn']['stance']}</p>
                <hr style="margin: 8px 0;">
                <p>{res['planner_turn']['argument']}</p>
                <p><strong>Proposed Milestones:</strong></p>
                <ul>{"".join([f"<li><code>{m}</code></li>" for m in res['planner_turn']['proposed_milestones']])}</ul>
            </div>
            """, unsafe_allow_html=True)

        with c_col:
            st.markdown(f"""
            <div class="persona-card critic-card">
                <h4>🔴 Critic Persona</h4>
                <p><strong>Stance:</strong> {res['critic_turn']['stance']}</p>
                <hr style="margin: 8px 0;">
                <p>{res['critic_turn']['argument']}</p>
                <p><strong>Screening Bottlenecks:</strong></p>
                <ul>{"".join([f"<li>{h}</li>" for h in res['critic_turn']['screening_hurdles']])}</ul>
            </div>
            """, unsafe_allow_html=True)

        with e_col:
            st.markdown(f"""
            <div class="persona-card ethics-card">
                <h4>🔵 Ethics-Reviewer Persona</h4>
                <p><strong>Stance:</strong> {res['ethics_turn']['stance']}</p>
                <hr style="margin: 8px 0;">
                <p>{res['ethics_turn']['argument']}</p>
                <p><strong>Equity Safeguards:</strong></p>
                <ul>{"".join([f"<li>{r}</li>" for r in res['ethics_turn']['accessible_resources_mandate']])}</ul>
            </div>
            """, unsafe_allow_html=True)

        # Dispute Tree Visualization
        st.markdown("### 🌲 Dispute Tree (Surfaced Contradictions & Resolutions)")
        for d in res["dispute_tree"]:
            st.markdown(f"""
            <div class="dispute-box">
                <strong style="color: #1e293b; font-size: 1.05rem;">⚡ Dimension: {d['dimension']}</strong>
                <div style="margin-top: 6px; font-size: 0.9rem;">
                    <span style="color: #16a34a;"><strong>Planner:</strong> {d['planner_stance']}</span><br>
                    <span style="color: #e11d48;"><strong>Critic:</strong> {d['critic_stance']}</span><br>
                    <span style="color: #0284c7;"><strong>Ethics:</strong> {d['ethics_stance']}</span>
                </div>
                <div style="margin-top: 8px; padding-top: 6px; border-top: 1px dashed #cbd5e1; color: #0f172a;">
                    <strong>🤝 Synthesized Resolution:</strong> {d['resolution']}
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Moderator Synthesis Box
        st.markdown("### ⚖️ Moderator / Arbiter Balanced Synthesis")
        st.markdown(f"""
        <div class="persona-card moderator-card">
            <h4>Balanced Recommendation ({res['moderator_synthesis']['strategy_mode']})</h4>
            <p><strong>Weights Applied:</strong> Velocity: {res['moderator_synthesis']['weights_applied'].get('velocity', 0.33):.2f} | Rigor: {res['moderator_synthesis']['weights_applied'].get('rigor', 0.33):.2f} | Equity: {res['moderator_synthesis']['weights_applied'].get('equity', 0.34):.2f}</p>
            <hr style="margin: 8px 0;">
            <p>{res['moderator_synthesis']['synthesis'].replace(chr(10), '<br>')}</p>
            <p><strong>Grounding Citations:</strong></p>
            <ul>{"".join([f"<li>📖 {c}</li>" for c in res['moderator_synthesis']['citations']])}</ul>
        </div>
        """, unsafe_allow_html=True)


# ═════════════════════════════════════════════════════════════════════════════
# TAB 2: EMPIRICAL BENCHMARK (5 METRICS)
# ═════════════════════════════════════════════════════════════════════════════
with tab2:
    st.markdown('<div class="main-header">Empirical Benchmark & Comparative Evaluation</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Evaluation of 20 Synthetic Profiles across 4 System Configurations on the 5 Official Metrics.</div>', unsafe_allow_html=True)

    results_file = os.path.join(ROOT_DIR, "data", "eval_results.json")
    if os.path.exists(results_file):
        with open(results_file, "r", encoding="utf-8") as f:
            eval_data = json.load(f)

        # Build Comparison DataFrame
        table_rows = []
        for cname, cval in eval_data.items():
            m = cval["metrics"]
            table_rows.append({
                "Configuration": cname.split(":")[0] + ": " + cname.split(":")[1].split("(")[0].strip(),
                "Evidence Diversity (H_div)": float(m["evidence_diversity"]),
                "Contradiction-Resolution Rate": m["contradiction_resolution_rate"],
                "Unsupported-Claim Rate": m["unsupported_claim_rate"],
                "Fairness (Jaccard)": m["fairness_across_synthetic_profiles"].split()[0],
                "User-Rubric Score": m["user_rubric_score"].split()[0] + " / 5.0"
            })
        df_eval = pd.DataFrame(table_rows)
        st.dataframe(df_eval, use_container_width=True)

        st.markdown("---")
        st.markdown("### 📊 Metric Visualizations")

        chart_c1, chart_c2 = st.columns(2)

        with chart_c1:
            st.markdown("#### Unsupported-Claim Rate (UCR % - Lower is Better)")
            ucr_df = pd.DataFrame({
                "Configuration": df_eval["Configuration"],
                "UCR (%)": [float(x.replace("%", "")) for x in df_eval["Unsupported-Claim Rate"]]
            })
            st.bar_chart(ucr_df.set_index("Configuration"))

        with chart_c2:
            st.markdown("#### Contradiction-Resolution Rate (CRR % - Higher is Better)")
            crr_df = pd.DataFrame({
                "Configuration": df_eval["Configuration"],
                "CRR (%)": [float(x.replace("%", "")) for x in df_eval["Contradiction-Resolution Rate"]]
            })
            st.bar_chart(crr_df.set_index("Configuration"))

        st.markdown("---")
        st.markdown("### ⚖️ Aarav vs Priya Counterfactual Fairness Analysis")
        st.markdown("""
        In **Config 1 (Single LLM Monolithic)**, Aarav (Tier-1, High Budget) receives an aggressive high-tech stack while Priya (Tier-3, Low Budget) receives a truncated low-tier pathway (**Fairness Jaccard = 0.32**).
        In **Config 4 (Proposed RAI Multi-Persona System)**, both receive the identical topologically valid core skill pathway, while the Ethics-Reviewer dynamically swaps costly paid tools for free public open courseware (**Fairness Jaccard = 1.00**).
        """)
    else:
        st.info("Run `python3 run_study.py` to generate the evaluation dataset.")


# ═════════════════════════════════════════════════════════════════════════════
# TAB 3: CAREER-SKILL GRAPH (NEO4J)
# ═════════════════════════════════════════════════════════════════════════════
with tab3:
    st.markdown('<div class="main-header">Neo4j Career-Skill Knowledge Graph</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">42-node prerequisite DAG ontology across 9 technical tracks with Neo4j Cypher generation.</div>', unsafe_allow_html=True)

    g_col1, g_col2 = st.columns([1.2, 2])

    with g_col1:
        st.markdown("#### Graph Summary Statistics")
        st.metric("Total Ontology Nodes", len(GRAPH_NODES))
        st.metric("Prerequisite Directed Edges", len(GRAPH_EDGES))
        st.metric("Technical Tracks", "9 Tracks (Prog, Math, DSA, Sys, DB, Web, DevOps, AI, Sec)")

        selected_skill = st.selectbox(
            "Inspect Node Prerequisites",
            [n["id"] for n in GRAPH_NODES]
        )
        direct_p = career_graph.get_prerequisites(selected_skill)
        all_p = career_graph.get_all_ancestor_prerequisites(selected_skill)
        st.write(f"**Direct Prerequisites for `{selected_skill}`:**")
        st.write(", ".join(direct_p) if direct_p else "None (Foundational Entry Node)")
        st.write("**Full Ancestor Prerequisite Chain:**")
        st.write(" ➔ ".join(all_p) if all_p else "None")

    with g_col2:
        st.markdown("#### ⚡ Neo4j Driver Connection & Cypher Export")
        neo_uri = st.text_input("Neo4j Bolt URI", "bolt://localhost:7687")
        neo_user = st.text_input("Neo4j Username", "neo4j")
        neo_pass = st.text_input("Neo4j Password", "password", type="password")

        if st.button("🔗 Sync Graph to Neo4j Instance"):
            sync_res = career_graph.sync_to_neo4j(uri=neo_uri, auth=(neo_user, neo_pass))
            if sync_res["status"] == "success":
                st.success(sync_res["message"])
            else:
                st.info(sync_res["message"])

        with st.expander("📄 View Generated Neo4j Cypher Queries", expanded=False):
            cypher_code = career_graph.export_cypher_script()
            st.code(cypher_code, language="cypher")


# ═════════════════════════════════════════════════════════════════════════════
# TAB 4: PUBLIC KNOWLEDGE BASE (CHROMA)
# ═════════════════════════════════════════════════════════════════════════════
with tab4:
    st.markdown('<div class="main-header">Public Course & Role Knowledge Base</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Indexed ACM/IEEE CS2023 curricula, MIT OpenCourseWare, and O*NET occupational standards.</div>', unsafe_allow_html=True)

    search_term = st.text_input("🔍 Semantic Search Chroma Vector Store", "Distributed Systems and Concurrency")
    if search_term:
        results = vector_store.retrieve_evidence(search_term, top_k=6)
        div_score = vector_store.calculate_evidence_diversity(results)
        st.write(f"**Retrieved {len(results)} items (Evidence Diversity Shannon Score: {div_score:.2f})**")

        for r in results:
            with st.container():
                st.markdown(f"""
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 12px; margin-bottom: 10px;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <strong style="font-size: 1.05rem; color: #0f172a;">{r.get('title')}</strong>
                        <span style="background: #e2e8f0; padding: 2px 8px; border-radius: 4px; font-size: 0.8rem; font-weight: 600;">{r.get('type', 'Evidence').upper()}</span>
                    </div>
                    <div style="font-size: 0.85rem; color: #64748b; margin: 4px 0;">Source: {r.get('source')} | Domain: {r.get('domain')}</div>
                    <p style="margin: 6px 0 0 0; font-size: 0.9rem; color: #334155;">{r.get('snippet')}</p>
                    <a href="{r.get('url', '#')}" target="_blank" style="font-size: 0.8rem; color: #0284c7; text-decoration: none;">View Official Curriculum ↗</a>
                </div>
                """, unsafe_allow_html=True)
