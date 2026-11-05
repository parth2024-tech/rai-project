#!/usr/bin/env python3
"""
Empirical Evaluation Study Runner
Runs 20 synthetic candidate profiles across 4 configurations using local Qwen.
Evaluates the 5 Official Committee Metrics:
1. Evidence Diversity (H_div - Shannon Entropy of cited public course/role domains)
2. Contradiction-Resolution Rate (CRR - % of surfaced Critic/Ethics objections resolved)
3. Unsupported-Claim Rate (UCR - % of milestones violating prerequisite DAG or lacking citations)
4. Fairness Across Synthetic Profiles (Jaccard similarity J(A, B) across counterfactual demographic pairs)
5. User-Rubric Score (1.0 to 5.0 across Balance, Rigor, Fairness, Disagreement Transparency, and Override Control)
"""

import os
import sys

# Ensure root directory is on python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.eval.comparative_eval import ComparativeEvaluator


def main():
    print("=" * 72)
    print(" RESPONSIBLE AI MULTI-PERSONA CAREER DEBATE SYSTEM")
    print(" Empirical Evaluation: 20 Synthetic Profiles × 4 Configurations")
    print(" Personas: Planner, Critic, Ethics-Reviewer, Moderator")
    print(" Stack: Qwen Local | Python Multi-Agent Harness | Neo4j Graph | Chroma | Streamlit")
    print("=" * 72)
    print("\nExecuting evaluation pipeline across 20 synthetic profiles...")

    evaluator = ComparativeEvaluator()
    results = evaluator.run_all_configurations()

    print("\n" + "=" * 72)
    print(" FINAL COMPARATIVE EVALUATION RESULTS (5 OFFICIAL METRICS)")
    print("=" * 72)

    headers = ["Configuration", "Evidence Div", "CRR (%)", "UCR (%)", "Fairness (Jaccard)", "User Rubric"]
    print(f"{headers[0]:<36} | {headers[1]:<12} | {headers[2]:<8} | {headers[3]:<8} | {headers[4]:<18} | {headers[5]:<10}")
    print("-" * 105)

    for config_name, data in results.items():
        m = data["metrics"]
        short_name = config_name.split(":")[0] + ": " + config_name.split(":")[1].split("(")[0].strip()
        print(f"{short_name:<36} | {m['evidence_diversity']:<12} | {m['contradiction_resolution_rate']:<8} | {m['unsupported_claim_rate']:<8} | {m['fairness_across_synthetic_profiles']:<18} | {m['user_rubric_score']:<10}")

    print("-" * 105)
    print("Results successfully persisted to: data/eval_results.json")
    print("=" * 72)

if __name__ == "__main__":
    main()
