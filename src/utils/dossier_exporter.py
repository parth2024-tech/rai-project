#!/usr/bin/env python3
"""
Counselor Audit Dossier & Roadmap Exporter
Implements:
- Standardized Markdown, HTML, and JSON audit dossiers for university career advisors
- Formats multi-agent deliberation traces, dispute trees, and prerequisite DAG checks
- Calibrated epistemic uncertainty visualization and human override decision records
- Full CLI support for batch export from synthetic or live candidate profiles
"""

import argparse
import html
import json
import os
import sys
from datetime import datetime, timezone
from typing import Any

# Ensure project root is in python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.agents.multi_agent_harness import MultiAgentDebateHarness


def generate_json_dossier(debate_result: dict[str, Any]) -> dict[str, Any]:
    """Generates a structured, machine-readable JSON dossier for LMS or counselor portals."""
    profile = debate_result.get("candidate_profile", {})
    turns = debate_result.get("persona_turns", {})
    moderator = debate_result.get("moderator_synthesis", {})
    uncertainty = debate_result.get("uncertainty_metrics", {})

    return {
        "dossier_version": "1.0.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "institution": "Department of Computer Science & Engineering - Responsible AI Lab",
        "candidate": {
            "name": profile.get("candidate_name", "Anonymous"),
            "target_role": profile.get("target", "Software Engineer"),
            "current_skills": profile.get("skills", []),
            "timeline": profile.get("timeline", "Not specified"),
            "budget": profile.get("budget", "Standard"),
            "college_tier": profile.get("college_tier", "Standard")
        },
        "deliberation_trace": {
            "planner": turns.get("planner", {}),
            "critic": turns.get("critic", {}),
            "ethics_reviewer": turns.get("ethics_reviewer", {}),
            "dispute_tree": debate_result.get("dispute_tree", [])
        },
        "governance_and_safety": {
            "prerequisite_violations": debate_result.get("prerequisite_violations", []),
            "calibrated_uncertainty": uncertainty.get("calibrated_uncertainty", 0.0),
            "epistemic_confidence": uncertainty.get("epistemic_confidence", 1.0),
            "calibration_interval": uncertainty.get("calibration_interval", [0.0, 1.0]),
            "gate_triggered": debate_result.get("gate_triggered", False),
            "human_override_active": debate_result.get("human_override_active", False)
        },
        "verified_roadmap": {
            "recommended_title": moderator.get("synthesized_plan_title", "Balanced Career Trajectory"),
            "executive_summary": moderator.get("balanced_summary", ""),
            "actionable_milestones": moderator.get("actionable_milestones", []),
            "prerequisites_to_fulfill": moderator.get("prerequisites_to_fulfill", [])
        },
        "evidence_citations": debate_result.get("evidence_retrieved", [])
    }


def generate_markdown_dossier(debate_result: dict[str, Any]) -> str:
    """Generates an academic-grade Markdown dossier for advisors and students."""
    profile = debate_result.get("candidate_profile", {})
    turns = debate_result.get("persona_turns", {})
    planner = turns.get("planner", {})
    critic = turns.get("critic", {})
    ethics = turns.get("ethics_reviewer", {})
    moderator = debate_result.get("moderator_synthesis", {})
    dispute_tree = debate_result.get("dispute_tree", [])
    uncertainty = debate_result.get("uncertainty_metrics", {})
    violations = debate_result.get("prerequisite_violations", [])
    evidence = debate_result.get("evidence_retrieved", [])

    lines = [
        "# Responsible AI Career Guidance Audit Dossier",
        f"**Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}  ",
        "**System:** Debate-Based Career Guidance Agent with Complementary Personas  ",
        "**Institution:** Department of Computer Science & Engineering - Responsible AI Lab  ",
        "",
        "---",
        "",
        "## 1. Candidate Profile & Context",
        f"- **Candidate Name:** {profile.get('candidate_name', 'Student')}",
        f"- **Target Career Role:** {profile.get('target', 'Software Engineer')}",
        f"- **Current Verified Skills:** {', '.join(profile.get('skills', [])) if profile.get('skills') else 'None recorded'}",
        f"- **Target Timeline:** {profile.get('timeline', 'Flexible')}",
        f"- **Socioeconomic / Hardware Context:** Budget: {profile.get('budget', 'Moderate')} | College Tier: {profile.get('college_tier', 'Standard')}",
        "",
        "---",
        "",
        "## 2. Multi-Persona Deliberation Trace",
        "",
        "### 🟢 Planner Persona (Constructive Growth)",
        f"> **Stance:** {planner.get('stance', 'Execution & Velocity')}",
        "",
        planner.get("argument", "No statement provided."),
        "",
        f"**Proposed Milestones:** {', '.join(planner.get('proposed_milestones', []))}",
        "",
        "### 🔴 Critic Persona (Skeptical Stress-Testing)",
        f"> **Stance:** {critic.get('stance', 'Rigorous Prerequisite Verification')} (Assessed Risk: {critic.get('risk_level', 'Moderate')})",
        "",
        critic.get("argument", "No statement provided."),
        "",
        "**Identified Prerequisite Bottlenecks:**",
    ]

    bottlenecks = critic.get("identified_bottlenecks", [])
    if bottlenecks:
        for b in bottlenecks:
            lines.append(f"- ⚠️ {b}")
    else:
        lines.append("- *No critical bottlenecks flagged.*")

    lines.extend([
        "",
        "### 🟣 Ethics & Feasibility Reviewer (Equity & Agency Safeguard)",
        f"> **Stance:** {ethics.get('stance', 'Fairness & Mental Well-being')}",
        "",
        ethics.get("argument", "No statement provided."),
        "",
        f"- **Feasibility Rating:** {ethics.get('feasibility_rating', '3/5')}",
        f"- **Equity Safeguard:** {ethics.get('equity_recommendation', 'Ensure access to open courseware.')}",
        "",
        "---",
        "",
        "## 3. Dispute Tree & Resolved Contention Forks",
        "The following explicit trade-offs were debated and reconciled by the Moderator:",
        ""
    ])

    if dispute_tree:
        for idx, dispute in enumerate(dispute_tree, 1):
            lines.extend([
                f"### Dispute Fork {idx}: {dispute.get('dimension', 'Contention Point')}",
                f"- **Planner:** {dispute.get('planner_stance', '')}",
                f"- **Critic:** {dispute.get('critic_stance', '')}",
                f"- **Ethics-Reviewer:** {dispute.get('ethics_stance', '')}",
                f"- **Reconciled Resolution:** ✅ *{dispute.get('resolution', '')}*",
                ""
            ])
    else:
        lines.append("*No disputes recorded in deliberation.*")

    lines.extend([
        "---",
        "",
        "## 4. Prerequisite DAG Verification & Calibrated Uncertainty",
        ""
    ])

    if violations:
        lines.append("### ⚠️ Curricular Prerequisite Violations Detected:")
        for v in violations:
            missing_str = ", ".join(v.get("missing_prerequisites", []))
            lines.append(f"- **Target Skill:** `{v.get('skill')}` — Missing Prerequisite(s): `{missing_str}`")
    else:
        lines.append("### ✅ Curricular Prerequisite Check: All proposed skills satisfy topological DAG ordering.")

    u_score = uncertainty.get("calibrated_uncertainty", 0.0)
    conf = uncertainty.get("epistemic_confidence", 1.0)
    interval = uncertainty.get("calibration_interval", [0.0, 1.0])

    lines.extend([
        "",
        "### Epistemic Uncertainty Metrics:",
        f"- **Calibrated Uncertainty ($\\hat{{U}}$):** `{u_score:.3f}` (Scale: 0.0 to 1.0)",
        f"- **Epistemic Confidence:** `{conf:.3f}`",
        f"- **95% Calibration Interval:** `[{interval[0]:.3f}, {interval[1]:.3f}]`",
        f"- **Friction Contribution:** `{uncertainty.get('friction_score', 0.0):.2f}`",
        f"- **Prerequisite Gap Penalty:** `{uncertainty.get('prerequisite_gap_penalty', 0.0):.2f}`",
        f"- **Socioeconomic Risk Factor:** `{uncertainty.get('socioeconomic_risk_penalty', 0.0):.2f}`",
        f"- **Cognitive Forcing Gate Status:** **{'🚨 TRIGGERED (Human Override Active)' if debate_result.get('gate_triggered') else '🟢 PASS (Low Risk)'}**",
        "",
        "---",
        "",
        "## 5. Actionable Roadmap & Grounded Evidence Citations",
        f"### {moderator.get('synthesized_plan_title', 'Synthesized Career Trajectory')}",
        "",
        moderator.get("balanced_summary", ""),
        "",
        "### Recommended Step-by-Step Milestones:"
    ])

    milestones = moderator.get("actionable_milestones", [])
    if milestones:
        for idx, m in enumerate(milestones, 1):
            lines.append(f"{idx}. **{m}**")
    else:
        lines.append("- *No milestones generated.*")

    lines.extend([
        "",
        "### Grounded Evidence Sources (Public Curricula & O*NET):"
    ])

    if evidence:
        for e in evidence:
            lines.append(f"- **[{e.get('domain', 'Curriculum')}]** {e.get('title', 'Course')} ({e.get('code', 'REF')})")
    else:
        lines.append("- *ACM/IEEE Computing Curricula 2023 & O*NET 29.2 Standard Tables.*")

    lines.extend([
        "",
        "---",
        "*Dossier compiled by Antigravity Responsible AI Agent Platform for Academic and Counseling Review.*"
    ])

    return "\n".join(lines)


def generate_html_dossier(debate_result: dict[str, Any]) -> str:
    """Generates a standalone, responsive HTML dossier with executive styling for counselor reviews."""
    md_content = generate_markdown_dossier(debate_result)
    profile = debate_result.get("candidate_profile", {})
    uncertainty = debate_result.get("uncertainty_metrics", {})
    gate_triggered = debate_result.get("gate_triggered", False)
    u_score = uncertainty.get("calibrated_uncertainty", 0.0)

    gate_color = "#e11d48" if gate_triggered else "#0d9488"
    gate_label = "COGNITIVE FORCING TRIGGERED — COUNSELOR OVERRIDE REQUIRED" if gate_triggered else "VERIFIED PASS — LOW UNCERTAINTY"

    # Minimal clean HTML wrapper
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>RAI Career Audit Dossier - {html.escape(profile.get('candidate_name', 'Student'))}</title>
<style>
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    line-height: 1.6;
    color: #1e293b;
    background-color: #f8fafc;
    margin: 0;
    padding: 30px 20px;
  }}
  .container {{
    max-width: 860px;
    margin: 0 auto;
    background: #ffffff;
    padding: 40px;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.06);
    border: 1px solid #e2e8f0;
  }}
  h1 {{ color: #0f172a; font-size: 26px; border-bottom: 2px solid #0d9488; padding-bottom: 10px; margin-top: 0; }}
  h2 {{ color: #1e293b; font-size: 20px; margin-top: 30px; border-bottom: 1px solid #cbd5e1; padding-bottom: 6px; }}
  h3 {{ color: #334155; font-size: 16px; margin-top: 20px; }}
  .badge {{
    display: inline-block;
    padding: 6px 14px;
    font-size: 13px;
    font-weight: 700;
    color: #ffffff;
    background-color: {gate_color};
    border-radius: 6px;
    letter-spacing: 0.5px;
    margin-bottom: 20px;
  }}
  .metric-card {{
    background: #f1f5f9;
    border-left: 4px solid #0d9488;
    padding: 15px 20px;
    margin: 15px 0;
    border-radius: 0 8px 8px 0;
  }}
  pre {{
    background: #0f172a;
    color: #f8fafc;
    padding: 15px;
    border-radius: 8px;
    overflow-x: auto;
    font-size: 13px;
  }}
  blockquote {{
    border-left: 4px solid #2563eb;
    margin: 10px 0;
    padding: 10px 15px;
    background-color: #eff6ff;
    border-radius: 0 6px 6px 0;
  }}
  .footer {{
    margin-top: 40px;
    padding-top: 15px;
    border-top: 1px solid #e2e8f0;
    font-size: 12px;
    color: #64748b;
    text-align: center;
  }}
</style>
</head>
<body>
<div class="container">
  <div class="badge">{gate_label}</div>
  <div class="metric-card">
    <strong>Epistemic Uncertainty:</strong> {u_score:.3f} / 1.0 &nbsp;|&nbsp;
    <strong>Candidate:</strong> {html.escape(profile.get('candidate_name', 'Student'))} &nbsp;|&nbsp;
    <strong>Target:</strong> {html.escape(profile.get('target', 'Software Engineer'))}
  </div>
  <pre style="white-space: pre-wrap; font-family: inherit; background: transparent; color: inherit; padding: 0;">{html.escape(md_content)}</pre>
  <div class="footer">
    Department of Computer Science &amp; Engineering &bull; Responsible Artificial Intelligence Platform &bull; Academic Year 2026-2027
  </div>
</div>
</body>
</html>"""
    return html_template


def export_dossier_to_file(debate_result: dict[str, Any], filepath: str, fmt: str = "markdown") -> str:
    """Exports the dossier to a target file in markdown, html, or json format."""
    os.makedirs(os.path.dirname(os.path.abspath(filepath)), exist_ok=True)
    if fmt == "html":
        content = generate_html_dossier(debate_result)
    elif fmt == "json":
        content = json.dumps(generate_json_dossier(debate_result), indent=2)
    else:
        content = generate_markdown_dossier(debate_result)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return filepath


def main() -> None:
    parser = argparse.ArgumentParser(description="Export Counselor Audit Dossier from Multi-Agent Career Debate.")
    parser.add_argument("--profile-index", type=int, default=0, help="Index of profile in synthetic_profiles.json (0-19)")
    parser.add_argument("--format", choices=["markdown", "html", "json"], default="markdown", help="Output format")
    parser.add_argument("--output", type=str, default="", help="Target output file path")
    parser.add_argument("--override-planner", type=float, default=1.0, help="Planner weight override")
    parser.add_argument("--override-critic", type=float, default=1.0, help="Critic weight override")
    parser.add_argument("--override-ethics", type=float, default=1.0, help="Ethics weight override")
    args = parser.parse_args()

    # Load synthetic profiles
    profiles_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "synthetic_profiles.json")
    with open(profiles_path, "r", encoding="utf-8") as f:
        profiles = json.load(f)

    if args.profile_index < 0 or args.profile_index >= len(profiles):
        print(f"Error: Invalid profile index {args.profile_index}. Must be between 0 and {len(profiles) - 1}.")
        sys.exit(1)

    profile = profiles[args.profile_index]
    harness = MultiAgentDebateHarness()
    override_weights = {
        "planner": args.override_planner,
        "critic": args.override_critic,
        "ethics": args.override_ethics
    }

    print(f"Executing multi-agent debate for {profile.get('candidate_name')} (Target: {profile.get('target')})...")
    result = harness.run_debate(profile, user_override_weights=override_weights)

    if not args.output:
        ext = "html" if args.format == "html" else ("json" if args.format == "json" else "md")
        sanitized_name = profile.get("candidate_name", "student").lower().replace(" ", "_")
        args.output = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "docs", f"dossier_{sanitized_name}.{ext}")

    out_file = export_dossier_to_file(result, args.output, fmt=args.format)
    print(f"Successfully generated counselor audit dossier: {out_file}")


if __name__ == "__main__":
    main()
