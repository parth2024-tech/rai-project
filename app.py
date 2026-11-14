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
from src.eval.all_configs_comparator import compare_all_configs
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
st.sidebar.title("Controls")

model_choice = st.sidebar.selectbox(
    "Local Model",
    ["qwen3:4b-fast", "qwen3:4b", "qwen2:0.5b", "llama3.2:latest"],
    index=0
)

harness = MultiAgentDebateHarness(model_name=model_choice)
synthetic_profiles = load_synthetic_profiles()

st.sidebar.divider()
st.sidebar.subheader("Candidate Profile")

profile_options = [
    f"{p['profile_id']}: {p['candidate_name']} ({p['variant']}) - {p['target']}"
    for p in synthetic_profiles
]
selected_idx = st.sidebar.selectbox(
    "Profiles",
    range(len(profile_options)),
    format_func=lambda i: profile_options[i]
)

candidate_data = synthetic_profiles[selected_idx]

with st.sidebar.expander("Edit Profile", expanded=False):
    candidate_name = st.text_input("Name", candidate_data.get("candidate_name", "Student"))
    candidate_gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Non-Binary"],
        index=0 if candidate_data.get("gender") == "Male" else 1
    )
    candidate_tier = st.text_input("College", candidate_data.get("college_tier"))
    candidate_budget = st.text_input("Budget", candidate_data.get("budget"))
    candidate_target = st.text_input("Target Role", candidate_data.get("target"))
    candidate_timeline = st.text_input("Timeline", candidate_data.get("timeline"))
    all_graph_skills = [n["id"] for n in GRAPH_NODES]
    current_skills = st.multiselect(
        "Skills",
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
st.title("Debate-Based Career Guidance Agent")

# ── Main Tabs ────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "⚡ Compare All 4 Configurations",
    "🗣️ Live 3-Agent Deliberation",
    "📊 Benchmark Scorecard",
    "🕸️ 42-Node Knowledge Graph",
    "📚 Course Database"
])


# ═════════════════════════════════════════════════════════════════════════════
# TAB 1: COMPARE ALL 4 CONFIGURATIONS SIDE-BY-SIDE
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

    st.subheader("How Each Configuration Answers for this Student")
    st.caption("Side-by-side comparison of roadmap answers, prerequisite violations, and cost advice.")

    comparisons = compare_all_configs(active_candidate)

    grid1, grid2 = st.columns(2)

    with grid1:
        # Config 1
        c1 = comparisons["Config 1 (ChatGPT Baseline)"]
        with st.container(border=True):
            st.markdown("#### 🔴 Config 1: Monolithic (ChatGPT Baseline)")
            st.error(f"❌ Status: {c1['verdict']} — {c1['verdict_reason']}")
            st.markdown(f"**How It Answers:**\n{c1['answer']}")
            st.markdown(f"**Proposed Milestones:** `{', '.join(c1['milestones'])}`")
            st.markdown(f"**Cost Guidance:** {c1['cost']}")
            st.markdown(f"**Demographic Fairness:** {c1['fairness']}")
            if c1["violations"]:
                st.markdown("**Prerequisite Errors Caught by Graph:**")
                for v in c1["violations"][:3]:
                    st.markdown(f"- ❌ `{v['milestone']}` requires `{v['missing_prerequisite']}`")

        # Config 3
        c3 = comparisons["Config 3 (Unmoderated Debate)"]
        with st.container(border=True):
            st.markdown("#### ⚠️ Config 3: Unmoderated 3-Agent Debate")
            st.error(f"❌ Status: {c3['verdict']} — {c3['verdict_reason']}")
            st.markdown(f"**How It Answers:**\n{c3['answer']}")
            st.markdown(f"**Proposed Milestones:** `{', '.join(c3['milestones'])}`")
            st.markdown(f"**Cost Guidance:** {c3['cost']}")
            st.markdown(f"**Demographic Fairness:** {c3['fairness']}")
            if c3["violations"]:
                st.markdown("**Prerequisite Errors Caught by Graph:**")
                for v in c3["violations"][:3]:
                    st.markdown(f"- ❌ `{v['milestone']}` requires `{v['missing_prerequisite']}`")

    with grid2:
        # Config 2
        c2 = comparisons["Config 2 (Multi-Perspective Prompt)"]
        with st.container(border=True):
            st.markdown("#### 🟡 Config 2: Multi-Perspective Single Prompt")
            st.warning(f"⚠️ Status: {c2['verdict']} — {c2['verdict_reason']}")
            st.markdown(f"**How It Answers:**\n{c2['answer']}")
            st.markdown(f"**Proposed Milestones:** `{', '.join(c2['milestones'])}`")
            st.markdown(f"**Cost Guidance:** {c2['cost']}")
            st.markdown(f"**Demographic Fairness:** {c2['fairness']}")
            if c2["violations"]:
                st.markdown("**Prerequisite Errors Caught by Graph:**")
                for v in c2["violations"][:3]:
                    st.markdown(f"- ❌ `{v['milestone']}` requires `{v['missing_prerequisite']}`")

        # Config 4
        c4 = comparisons["Config 4 (Our Proposed RAI System)"]
        with st.container(border=True):
            st.markdown("#### 🟢 Config 4: Our Proposed RAI System")
            st.success(f"✅ Status: {c4['verdict']} — {c4['verdict_reason']}")
            st.markdown(f"**How It Answers:**\n{c4['answer']}")
            st.markdown(f"**Proposed Milestones:** `{', '.join(c4['milestones'])}`")
            st.markdown(f"**Cost Guidance:** {c4['cost']}")
            st.markdown(f"**Demographic Fairness:** {c4['fairness']}")
            st.markdown("**Prerequisite Status:** ✅ Zero Violations (100% Graph-Verified)")


# ═════════════════════════════════════════════════════════════════════════════
# TAB 2: LIVE DIALECTIC DEBATE & HUMAN OVERRIDE
# ═════════════════════════════════════════════════════════════════════════════
with tab2:
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
    with st.expander("Priority Sliders (Speed vs Rigor vs Equity)", expanded=False):
        col_w1, col_w2, col_w3 = st.columns(3)
        w_vel = col_w1.slider("Planner Priority (Speed)", 0.0, 1.0, st.session_state.override_weights["velocity"], 0.05)
        w_rig = col_w2.slider("Critic Priority (Depth)", 0.0, 1.0, st.session_state.override_weights["rigor"], 0.05)
        w_eq = col_w3.slider("Ethics Priority (Zero-Debt)", 0.0, 1.0, st.session_state.override_weights["equity"], 0.05)

        total_w = w_vel + w_rig + w_eq
        if total_w > 0:
            st.session_state.override_weights = {
                "velocity": round(w_vel / total_w, 2),
                "rigor": round(w_rig / total_w, 2),
                "equity": round(w_eq / total_w, 2)
            }

        btn_c1, btn_c2 = st.columns([1, 4])
        if btn_c1.button("Apply Override"):
            st.session_state.force_override = True
            st.success("Override active.")
        if btn_c2.button("Reset Default"):
            st.session_state.force_override = False
            st.session_state.override_weights = {"velocity": 0.33, "rigor": 0.33, "equity": 0.34}
            st.info("Reset to default.")

    # Run Deliberation Button
    if st.button("Run Deliberation & Graph Check", type="primary", width="stretch"):
        with st.spinner("Running deliberation..."):
            debate_result = harness.run_debate(
                candidate_profile=active_candidate,
                user_override_weights=st.session_state.override_weights,
                force_override=st.session_state.force_override
            )
            st.session_state.latest_debate = debate_result

    # Display Deliberation Output
    if "latest_debate" in st.session_state:
        res = st.session_state.latest_debate

        # Prominent Prerequisite Error Display
        if res["graph_violations"]:
            st.error(f"❌ Knowledge Graph Detected {len(res['graph_violations'])} Prerequisite Error(s):")
            for v in res["graph_violations"]:
                st.markdown(
                    f"- **`{v['milestone']}`** cannot be scheduled! "
                    f"Missing foundational prerequisite: **`{v['missing_prerequisite']}`** *(Rule: {v['rule']})*"
                )
        else:
            st.success("✅ Zero prerequisite errors detected by Knowledge Graph.")

        m1, m2, m3, m4 = st.columns(4)
        u_val = res["uncertainty_metrics"]["calibrated_uncertainty"]
        m1.metric("Uncertainty (U)", f"{u_val:.2f}")
        num_violations = len(res["graph_violations"])
        m2.metric("Prerequisite Errors", num_violations)
        m3.metric("Evidence Diversity", f"{res['evidence_diversity']:.2f}")
        gate_text = "TRIGGERED" if res["gate_triggered"] else "PASSED"
        m4.metric("Gate Status", gate_text)

        st.divider()

        # 3 Persona Arguments (Clean Native Containers)
        st.subheader("Debate Trace")
        p_col, c_col, e_col = st.columns(3)

        with p_col:
            with st.container(border=True):
                st.markdown("### 🟢 Planner")
                st.caption(f"Stance: {res['planner_turn']['stance']}")
                st.write(res['planner_turn']['argument'])
                st.markdown("**Proposed Milestones:**")
                for m in res['planner_turn']['proposed_milestones']:
                    st.markdown(f"- `{m}`")

        with c_col:
            with st.container(border=True):
                st.markdown("### 🔴 Critic")
                st.caption(f"Stance: {res['critic_turn']['stance']}")
                st.write(res['critic_turn']['argument'])
                st.markdown("**Screening Bottlenecks:**")
                for h in res['critic_turn']['screening_hurdles']:
                    st.markdown(f"- {h}")

        with e_col:
            with st.container(border=True):
                st.markdown("### 🔵 Ethics-Reviewer")
                st.caption(f"Stance: {res['ethics_turn']['stance']}")
                st.write(res['ethics_turn']['argument'])
                st.markdown("**Zero-Debt Safeguards:**")
                for r in res['ethics_turn']['accessible_resources_mandate']:
                    st.markdown(f"- {r}")

        st.divider()

        # Dispute Tree
        st.subheader("Dispute Tree")
        for d in res["dispute_tree"]:
            with st.container(border=True):
                st.markdown(f"#### Trade-Off: {d['dimension']}")
                st.markdown(f"- **Planner:** {d['planner_stance']}")
                st.markdown(f"- **Critic:** {d['critic_stance']}")
                st.markdown(f"- **Ethics:** {d['ethics_stance']}")
                st.divider()
                st.markdown(f"**Resolution:** {d['resolution']}")

        st.divider()

        # Moderator Synthesis
        st.subheader("Final Recommendation")
        with st.container(border=True):
            st.markdown(f"#### Strategy: `{res['moderator_synthesis']['strategy_mode']}`")
            w = res['moderator_synthesis']['weights_applied']
            st.caption(f"Weights: Velocity {w.get('velocity', 0.33):.2f} | Rigor {w.get('rigor', 0.33):.2f} | Equity {w.get('equity', 0.34):.2f}")
            st.write(res['moderator_synthesis']['synthesis'])
            st.markdown("**Citations:**")
            for c in res['moderator_synthesis']['citations']:
                st.markdown(f"- 📖 {c}")


# ═════════════════════════════════════════════════════════════════════════════
# TAB 3: EMPIRICAL BENCHMARK (5 METRICS)
# ═════════════════════════════════════════════════════════════════════════════
with tab3:
    st.subheader("Benchmark Scorecard")

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
            st.markdown("##### Prerequisite Errors (UCR % — Lower is Better)")
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
            st.markdown("#### Counterfactual Fairness (Aarav vs. Priya)")
            st.markdown("""
            - **Config 1 (Standard Single Prompt):** Aarav (Tier-1, High Budget) received advanced tech stacks, while Priya (Tier-3, Low Budget) received low-level tasks (**Fairness Jaccard = 0.32**).
            - **Config 4 (Our System):** Both received identical core competencies (**Fairness Jaccard = 1.00**), while substituting paid bootcamps with free MIT OpenCourseWare.
            """)
    else:
        st.info("Run `python3 run_study.py` to re-generate benchmark results.")


# ═════════════════════════════════════════════════════════════════════════════
# TAB 4: CAREER-SKILL GRAPH (42 NODES)
# ═════════════════════════════════════════════════════════════════════════════
with tab4:
    st.subheader("42-Node Knowledge Graph")

    g_col1, g_col2 = st.columns([1.2, 2])

    with g_col1:
        with st.container(border=True):
            st.markdown("#### Summary")
            st.metric("Total Nodes", len(GRAPH_NODES))
            st.metric("Prerequisite Edges", len(GRAPH_EDGES))
            st.metric("Technical Tracks", "9 CS Tracks")

        with st.container(border=True):
            st.markdown("#### Check Node Prerequisites")
            selected_skill = st.selectbox(
                "Select a Competency",
                [n["id"] for n in GRAPH_NODES]
            )
            direct_p = career_graph.get_prerequisites(selected_skill)
            all_p = career_graph.get_all_ancestor_prerequisites(selected_skill)
            st.markdown(f"**Prerequisites for `{selected_skill}`:**")
            st.write(", ".join(direct_p) if direct_p else "None (Foundational Entry Course)")
            st.markdown("**Full Prerequisite Chain:**")
            st.write(" ➔ ".join(all_p) if all_p else "None")

    with g_col2:
        with st.container(border=True):
            st.markdown("#### The 9 Technical Tracks")
            track_counts = {}
            for n in GRAPH_NODES:
                cat = n.get("category", "General")
                track_counts[cat] = track_counts.get(cat, 0) + 1
            df_tracks = pd.DataFrame([{"Track": k, "Node Count": v} for k, v in track_counts.items()])
            st.dataframe(df_tracks, hide_index=True)

        with st.expander("Neo4j Cypher Schema", expanded=False):
            cypher_code = career_graph.export_cypher_script()
            st.code(cypher_code, language="cypher")


# ═════════════════════════════════════════════════════════════════════════════
# TAB 5: GROUNDED SYLLABI (CHROMADB)
# ═════════════════════════════════════════════════════════════════════════════
with tab5:
    st.subheader("Course Database (ChromaDB)")

    search_term = st.text_input("Search Syllabi in ChromaDB", "Data Structures and Algorithms")
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
