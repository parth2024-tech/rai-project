#!/usr/bin/env python3
"""
Responsible AI Career Guidance Multi-Persona Debate Prototype
Streamlit Web Application (Minimal, Theme-Adaptive, College-Level Design):
- Planner, Critic, and Ethics-Reviewer Personas
- Deterministic 42-Node Knowledge Graph Prerequisite Validation
- Epistemic Uncertainty & Interactive Dispute Tree
- Human Override Sliders (Speed vs Rigor vs Equity)
- Empirical Benchmark (5 Metrics)
- Knowledge Graph Traversal & Chroma Vector Store
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
    page_title="Career Guidance Multi-Persona Debate Lab",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Sidebar: Model & Candidate Setup ─────────────────────────────────────────
st.sidebar.title("⚙️ System Control")
st.sidebar.caption("Undergraduate Capstone Evaluation Lab")

model_choice = st.sidebar.selectbox(
    "Local Inference Model (Ollama)",
    ["qwen3:4b-fast", "qwen3:4b", "qwen2:0.5b", "llama3.2:latest"],
    index=0
)

harness = MultiAgentDebateHarness(model_name=model_choice)
synthetic_profiles = load_synthetic_profiles()

st.sidebar.divider()
st.sidebar.subheader("👤 Select Candidate Profile")

profile_options = [
    f"{p['profile_id']}: {p['candidate_name']} ({p['variant']}) - {p['target']}"
    for p in synthetic_profiles
]
selected_idx = st.sidebar.selectbox(
    "Benchmark Profiles (20 Profiles / 10 Pairs)",
    range(len(profile_options)),
    format_func=lambda i: profile_options[i]
)

candidate_data = synthetic_profiles[selected_idx]

with st.sidebar.expander("📝 View / Edit Profile Details", expanded=False):
    candidate_name = st.text_input("Candidate Name", candidate_data.get("candidate_name", "Student"))
    candidate_gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Non-Binary"],
        index=0 if candidate_data.get("gender") == "Male" else 1
    )
    candidate_tier = st.text_input("College / Institute", candidate_data.get("college_tier"))
    candidate_budget = st.text_input("Monthly Budget", candidate_data.get("budget"))
    candidate_target = st.text_input("Target Career Role", candidate_data.get("target"))
    candidate_timeline = st.text_input("Target Timeline", candidate_data.get("timeline"))
    all_graph_skills = [n["id"] for n in GRAPH_NODES]
    current_skills = st.multiselect(
        "Current Verified Skills",
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

# ── Main Header ──────────────────────────────────────────────────────────────
st.title("⚖️ Debate-Based Career Guidance Agent")
st.caption(
    "SRMIST School of Computing — 6th Semester Capstone Research Prototype | "
    "Multi-Agent Deliberation (Planner, Critic, Ethics) with 42-Node Knowledge Graph Verification"
)

# ── Main Tabs ────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs([
    "🗣️ Dialectic Debate & Trace",
    "📊 Benchmark Results (5 Metrics)",
    "🕸️ 42-Node Knowledge Graph",
    "📚 Grounded Syllabi (ChromaDB)"
])


# ═════════════════════════════════════════════════════════════════════════════
# TAB 1: DIALECTIC DEBATE & HUMAN OVERRIDE
# ═════════════════════════════════════════════════════════════════════════════
with tab1:
    # Candidate Summary Banner
    with st.container(border=True):
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Student Name", active_candidate["candidate_name"])
        c2.metric("Target Career Role", active_candidate["target"])
        c3.metric("Available Timeline", active_candidate["timeline"])
        c4.metric("Budget & College Tier", f"{active_candidate['budget'].split()[0]} | {active_candidate['college_tier'].split()[0]}")
        st.write(f"**Verified Current Skills:** {', '.join(active_candidate['skills']) if active_candidate['skills'] else 'Beginner (No prior CS courses)'}")

    # Session State for Override Controls
    if "override_weights" not in st.session_state:
        st.session_state.override_weights = {"velocity": 0.33, "rigor": 0.33, "equity": 0.34}
    if "force_override" not in st.session_state:
        st.session_state.force_override = False

    # Human-in-the-Loop Override Sliders
    with st.expander("🎛️ Human-in-the-Loop Override Sliders (Student / Counselor Controls)", expanded=False):
        st.write("Adjust priority sliders to guide how the Moderator resolves disagreements among the agents:")
        col_w1, col_w2, col_w3 = st.columns(3)
        w_vel = col_w1.slider("Planner Priority (Speed to Placement)", 0.0, 1.0, st.session_state.override_weights["velocity"], 0.05)
        w_rig = col_w2.slider("Critic Priority (Prerequisite Depth)", 0.0, 1.0, st.session_state.override_weights["rigor"], 0.05)
        w_eq = col_w3.slider("Ethics Priority (Zero-Debt & Balance)", 0.0, 1.0, st.session_state.override_weights["equity"], 0.05)

        total_w = w_vel + w_rig + w_eq
        if total_w > 0:
            st.session_state.override_weights = {
                "velocity": round(w_vel / total_w, 2),
                "rigor": round(w_rig / total_w, 2),
                "equity": round(w_eq / total_w, 2)
            }

        btn_c1, btn_c2 = st.columns([1, 4])
        if btn_c1.button("Apply Human Override"):
            st.session_state.force_override = True
            st.success("Human Override Active: Moderator will follow your custom weights.")
        if btn_c2.button("Reset to Balanced Default"):
            st.session_state.force_override = False
            st.session_state.override_weights = {"velocity": 0.33, "rigor": 0.33, "equity": 0.34}
            st.info("Reset to balanced autonomous debate.")

    # Run Deliberation Button
    if st.button("🚀 Run 3-Agent Deliberation & Graph Check", type="primary", width="stretch"):
        with st.spinner("Running Planner, Critic, Ethics-Reviewer, and Knowledge Graph validation..."):
            debate_result = harness.run_debate(
                candidate_profile=active_candidate,
                user_override_weights=st.session_state.override_weights,
                force_override=st.session_state.force_override
            )
            st.session_state.latest_debate = debate_result

    # Display Deliberation Output
    if "latest_debate" in st.session_state:
        res = st.session_state.latest_debate

        st.subheader("1. Knowledge Graph Verification & Uncertainty Status")
        m1, m2, m3, m4 = st.columns(4)
        u_val = res["uncertainty_metrics"]["calibrated_uncertainty"]
        m1.metric("Calibrated Uncertainty (U)", f"{u_val:.2f}", help="Composite score: debate friction + missing prerequisites + budget strain + timeline pressure.")
        num_violations = len(res["graph_violations"])
        m2.metric("Prerequisite Errors (Δ)", num_violations, delta="Detected" if num_violations > 0 else "Clean", delta_color="inverse")
        m3.metric("Evidence Diversity (H_div)", f"{res['evidence_diversity']:.2f}", delta="Diverse Syllabi Cited")
        gate_text = "TRIGGERED (Override Required)" if res["gate_triggered"] else "PASSED (Safe)"
        m4.metric("Cognitive Gate Status", gate_text)

        # Prominent Prerequisite Error Display
        if res["graph_violations"]:
            st.error(f"🚨 KNOWLEDGE GRAPH CAUGHT {len(res['graph_violations'])} PREREQUISITE ERROR(S) IN PROPOSED PLAN:")
            for v in res["graph_violations"]:
                st.markdown(
                    f"- ❌ Milestone **`{v['milestone']}`** cannot be started yet! "
                    f"Missing foundational prerequisite: **`{v['missing_prerequisite']}`** *(Rule: {v['rule']})*"
                )
        else:
            st.success("✅ All proposed milestones satisfy knowledge graph prerequisites (Zero Sequencing Errors).")

        st.divider()

        # 3 Persona Arguments (Clean Native Containers)
        st.subheader("2. Interactive Multi-Agent Debate Trace")
        p_col, c_col, e_col = st.columns(3)

        with p_col:
            with st.container(border=True):
                st.markdown("### 🟢 Planner Persona")
                st.caption(f"**Stance:** {res['planner_turn']['stance']}")
                st.write(res['planner_turn']['argument'])
                st.markdown("**Proposed Milestones:**")
                for m in res['planner_turn']['proposed_milestones']:
                    st.markdown(f"- `{m}`")

        with c_col:
            with st.container(border=True):
                st.markdown("### 🔴 Critic Persona")
                st.caption(f"**Stance:** {res['critic_turn']['stance']}")
                st.write(res['critic_turn']['argument'])
                st.markdown("**Screening Bottlenecks Identified:**")
                for h in res['critic_turn']['screening_hurdles']:
                    st.markdown(f"- {h}")

        with e_col:
            with st.container(border=True):
                st.markdown("### 🔵 Ethics-Reviewer Persona")
                st.caption(f"**Stance:** {res['ethics_turn']['stance']}")
                st.write(res['ethics_turn']['argument'])
                st.markdown("**Zero-Debt & Open Courseware:**")
                for r in res['ethics_turn']['accessible_resources_mandate']:
                    st.markdown(f"- {r}")

        st.divider()

        # Dispute Tree
        st.subheader("3. Dispute Tree (Surfaced Disagreements & Resolutions)")
        for d in res["dispute_tree"]:
            with st.container(border=True):
                st.markdown(f"#### ⚡ Trade-Off: {d['dimension']}")
                st.markdown(f"- **🟢 Planner View:** {d['planner_stance']}")
                st.markdown(f"- **🔴 Critic View:** {d['critic_stance']}")
                st.markdown(f"- **🔵 Ethics View:** {d['ethics_stance']}")
                st.divider()
                st.markdown(f"**🤝 Reconciled Resolution:** {d['resolution']}")

        st.divider()

        # Moderator Synthesis
        st.subheader("4. Moderator Final Balanced Recommendation")
        with st.container(border=True):
            st.markdown(f"#### Synthesis Strategy: `{res['moderator_synthesis']['strategy_mode']}`")
            w = res['moderator_synthesis']['weights_applied']
            st.caption(f"Weights Applied — Velocity: {w.get('velocity', 0.33):.2f} | Rigor: {w.get('rigor', 0.33):.2f} | Equity: {w.get('equity', 0.34):.2f}")
            st.write(res['moderator_synthesis']['synthesis'])
            st.markdown("**Accredited Grounding Sources Cited:**")
            for c in res['moderator_synthesis']['citations']:
                st.markdown(f"- 📖 {c}")


# ═════════════════════════════════════════════════════════════════════════════
# TAB 2: EMPIRICAL BENCHMARK (5 METRICS)
# ═════════════════════════════════════════════════════════════════════════════
with tab2:
    st.subheader("Empirical Benchmark Scorecard (20 Profiles × 4 Configurations = 80 Runs)")
    st.caption("Ablation study comparing single-prompt baseline against our graph-verified multi-persona system.")

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
                "Prerequisite Errors (UCR)": m["unsupported_claim_rate"],
                "Fairness Overlap (Jaccard)": m["fairness_across_synthetic_profiles"].split()[0],
                "Counselor Rubric Score": m["user_rubric_score"].split()[0] + " / 5.0"
            })
        df_eval = pd.DataFrame(table_rows)
        st.dataframe(df_eval, hide_index=True)

        st.divider()

        chart_c1, chart_c2 = st.columns(2)
        with chart_c1:
            st.markdown("##### Prerequisite Sequencing Errors (UCR % — Lower is Better)")
            ucr_df = pd.DataFrame({
                "Configuration": df_eval["System Configuration"],
                "Error Rate (%)": [float(x.replace("%", "")) for x in df_eval["Prerequisite Errors (UCR)"]]
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
            st.markdown("#### ⚖️ Counterfactual Fairness Analysis (Aarav vs. Priya)")
            st.markdown("""
            - **In Config 1 (Standard Single Prompt):** Aarav (Tier-1, High Budget) was advised advanced engineering projects, while Priya (Tier-3, Low Budget) was steered toward basic support tasks (**Fairness Jaccard = 0.32**).
            - **In Config 4 (Our System):** Both received identical, topologically verified core competencies (**Fairness Jaccard = 1.00**), while the Ethics-Reviewer replaced costly commercial bootcamps with free accredited MIT OpenCourseWare and Harvard CS50.
            """)
    else:
        st.info("Run `python3 run_study.py` to re-generate benchmark results.")


# ═════════════════════════════════════════════════════════════════════════════
# TAB 3: CAREER-SKILL GRAPH (42 NODES)
# ═════════════════════════════════════════════════════════════════════════════
with tab3:
    st.subheader("42-Node Computer Science Prerequisite Knowledge Graph")
    st.caption("Hand-built directed acyclic graph (DAG) spanning 9 technical tracks with 47 prerequisite edges.")

    g_col1, g_col2 = st.columns([1.2, 2])

    with g_col1:
        with st.container(border=True):
            st.markdown("#### Graph Summary")
            st.metric("Total Ontology Nodes", len(GRAPH_NODES))
            st.metric("Prerequisite Directed Edges", len(GRAPH_EDGES))
            st.metric("Technical Tracks", "9 Core CS Subfields")

        with st.container(border=True):
            st.markdown("#### Check Node Prerequisites")
            selected_skill = st.selectbox(
                "Select a CS Competency",
                [n["id"] for n in GRAPH_NODES]
            )
            direct_p = career_graph.get_prerequisites(selected_skill)
            all_p = career_graph.get_all_ancestor_prerequisites(selected_skill)
            st.markdown(f"**Immediate Prerequisites for `{selected_skill}`:**")
            st.write(", ".join(direct_p) if direct_p else "None (Foundational Entry Course)")
            st.markdown("**Full Prerequisite Chain (Ancestors):**")
            st.write(" ➔ ".join(all_p) if all_p else "None")

    with g_col2:
        with st.container(border=True):
            st.markdown("#### The 9 Technical Tracks & Competency Distribution")
            track_counts = {}
            for n in GRAPH_NODES:
                cat = n.get("category", "General")
                track_counts[cat] = track_counts.get(cat, 0) + 1
            df_tracks = pd.DataFrame([{"Track": k, "Node Count": v} for k, v in track_counts.items()])
            st.dataframe(df_tracks, hide_index=True)

        with st.expander("📄 View Generated Neo4j Cypher Schema", expanded=False):
            cypher_code = career_graph.export_cypher_script()
            st.code(cypher_code, language="cypher")


# ═════════════════════════════════════════════════════════════════════════════
# TAB 4: GROUNDED SYLLABI (CHROMADB)
# ═════════════════════════════════════════════════════════════════════════════
with tab4:
    st.subheader("Public Knowledge Base & Syllabi (ChromaDB)")
    st.caption("Indexed ACM/IEEE CS2023 curricula, MIT OpenCourseWare, Harvard CS50, and O*NET standards.")

    search_term = st.text_input("Semantic Search in ChromaDB Vector Store", "Data Structures and Algorithms")
    if search_term:
        results = vector_store.retrieve_evidence(search_term, top_k=6)
        div_score = vector_store.calculate_evidence_diversity(results)
        st.write(f"**Retrieved {len(results)} chunks (Evidence Diversity Shannon Score: {div_score:.2f})**")

        for r in results:
            with st.container(border=True):
                st.markdown(f"**{r.get('title')}** `[{r.get('type', 'Evidence').upper()}]`")
                st.caption(f"Source: {r.get('source')} | Domain: {r.get('domain')}")
                st.write(r.get('snippet'))
                st.link_button("View Official Curriculum ↗", r.get('url', '#'))
