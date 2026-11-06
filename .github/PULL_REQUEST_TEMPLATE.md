## Summary of Changes

Describe the changes proposed in this Pull Request and their motivation.

## Responsible AI & Evaluation Checklist

- [ ] **Multi-Agent Alignment**: Ensures no persona is rendered one-sided or suppressed.
- [ ] **Prerequisite Verification**: Traversed against the 42-node Career-Skill DAG in `src/graph/career_graph.py`.
- [ ] **Uncertainty Calibration**: Verified that composite epistemic uncertainty bounds remain in $[0.0, 1.0]$.
- [ ] **Fairness & Non-Steering**: Tested against paired synthetic demographic profiles (`data/synthetic_profiles.json`).
- [ ] **Human-in-the-Loop**: Preserves user override gateway functionality.
- [ ] **Testing**: Added/updated unit tests in `tests/` and confirmed `pytest` passes with 0 failures.
- [ ] **Code Hygiene**: Clean linting with `ruff check .` and typing with `mypy src/`.
