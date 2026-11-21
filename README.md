# A Local, Multi-Dimensional Evaluation Lab for Student Career Advisory LLM Agents

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Model: Qwen 2.5 7B](https://img.shields.io/badge/Ollama-Qwen%202.5%207B-purple.svg)](https://ollama.ai)
[![Streamlit UI](https://img.shields.io/badge/UI-Streamlit-red.svg)](https://streamlit.io)

An academic, reproducible, and fully local evaluation lab designed to benchmark student career-advisory large language model (LLM) agents across multi-agent dialectic debate, deterministic knowledge graph prerequisite validation, calibrated uncertainty, and demographic counterfactual fairness.

---

### Authors & Affiliation
- **Aniket Srivastava** (`as6608@srmist.edu.in`)
- **Parth Gupta** (`pg5206@srmist.edu.in`)
- **Gedela Rishikesh Reddy** (`rg0330@srmist.edu.in`)
- **Faculty Mentor:** Dr. Akilandeswari P (`akilandp@srmist.edu.in`)
- **Industry Mentor:** Pratyush Jha (ZS Associates, Pune)

*Department of Computing Technologies, SRM Institute of Science and Technology, Chennai, India*

---

## 🎯 Executive Overview

Commercial and monolithic single-agent LLM career advisors suffer from three critical failure modes:
1. **Conversational Flattery & Sycophancy:** Inappropriately affirming ambitious transitions (e.g. novice to Staff ML Architect in 3 months) while omitting foundational prerequisites.
2. **Predatory Debt Steering:** Directing low-budget students toward high-cost commercial bootcamps and financing loans rather than free public courseware.
3. **Demographic Inconsistency:** Exhibiting bias across counterfactual demographic and institutional proxies (swapping names and college tiers while holding skills constant).

This system implements a **Dialectic Multi-Persona Architecture** coupled with a **42-node hand-built Neo4j prerequisite DAG** and **ChromaDB vector retrieval** over ACM CS2023 curricula and O*NET occupational standards.

```
                              ┌─────────────────────────────────────────┐
                              │         Student Candidate Intake        │
                              └────────────────────┬────────────────────┘
                                                   │
                                                   ▼
                                      ┌─────────────────────────┐
                                      │  Chroma Vector Retrieval│
                                      │  (CS2023 & O*NET Data)  │
                                      └────────────┬────────────┘
                                                   │
                        ┌──────────────────────────┴──────────────────────────┐
                        ▼                                                     ▼
             ┌─────────────────────┐                               ┌─────────────────────┐
             │       Planner       │ ◄────────── Debate ─────────► │       Critic        │
             │(Curriculum Pathway) │                               │(Prerequisite Stress)│
             └──────────┬──────────┘                               └──────────┬──────────┘
                        │                          ▲                          │
                        │                          │ Audit                    │
                        │               ┌──────────┴──────────┐               │
                        └──────────────►│   Ethics-Reviewer   │◄──────────────┘
                                        │(Fairness & Zero-Debt)│
                                        └──────────┬──────────┘
                                                   │
                                                   ▼
                                      ┌─────────────────────────┐
                                      │  Moderator Synthesizer  │
                                      │   (42-Node Neo4j DAG)   │
                                      └────────────┬────────────┘
                                                   │
                                                   ▼
                                      ┌─────────────────────────┐
                                      │ Epistemic Friction Gate │
                                      │   (Δprereq > 0 or U≥.45)│
                                      └────────────┬────────────┘
                                                   │
                                                   ▼
                                      ┌─────────────────────────┐
                                      │  Streamlit Trace Viewer │
                                      │     & Human Override    │
                                      └─────────────────────────┘
```

---

## 🏛️ Core Architectural Pillars

### 1. Multi-Persona Dialectic Triad
- **Planner Persona:** Focuses on constructive pathway design, milestone progression, and public course sequencing.
- **Critic Persona:** Focuses on adversarial stress-testing, exposing missing math and systems prerequisites, interview hurdles, and market saturation.
- **Ethics-Reviewer Persona:** Audits socioeconomic fairness, enforces a zero-debt mandate (free open courseware over costly bootcamps), and preserves student critical agency.
- **Moderator Synthesizer:** Extracts explicit **Dispute Trees**, computes calibrated uncertainty $U$, and queries topological reachability against the curriculum DAG.

### 2. Hand-Built 42-Node Prerequisite Knowledge Graph
Spans 9 core technical tracks with 47 directed prerequisite edges:
- Math & Theory (Calculus, Linear Algebra, Probability, Discrete Math)
- Data Structures & Algorithms (Basic DSA, Advanced Algorithms)
- Systems & Architecture (C/C++, Computer Systems & Assembly, Operating Systems, Distributed Systems)
- Databases & Storage (Relational SQL, Indexing/3NF, Distributed Storage)
- Web & Backend APIs (Python OOP, Backend Frameworks, API Security)
- DevOps & Cloud (OS Basics, Docker Containers, Kubernetes)
- AI & Machine Learning (Linear Algebra, ML Foundations, Deep Learning, MLOps)
- Cybersecurity & Mobile Systems

### 3. Calibrated Epistemic Uncertainty & Cognitive Forcing Gate
Computes multi-component uncertainty:
$$U = w_1 F_{\text{triad}} + w_2 \Delta_{\text{prereq}} + w_3 R_{\text{socio}} + w_4 R_{\text{timeline}}$$
When $\Delta_{\text{prereq}} > 0$ or $U \ge 0.45$, the automated generator halts, surfaces trade-off options in a Dispute Tree, and empowers the student or counselor with interactive human override.

---

## 📊 Evaluation Benchmark & Empirical Results

Evaluated across **80 full deliberation runs on 20 synthetic candidate profiles** (10 base archetypes $\times$ 2 counterfactual demographic/budget variants: Aarav Sharma [Tier-1, high budget] vs. Priya Patel [Tier-3, low budget]) across five core metrics:

| Metric | Target | Config 1 (Monolithic Baseline) | Config 2 (Persona Triad) | Config 3 (Triad + Graph) | Config 4 (Proposed RAI System) | Stat. Sig. (Config 1 vs 4) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Evidence Diversity ($H_{\text{div}}$)** | $\ge 0.80$ | 0.22 | 0.48 | 0.68 | **1.00** | $p < 0.001$ |
| **Contradiction Resolution (CRR)** | $\ge 80\%$ | 0.0% | 38.0% | 25.0% | **100.0%** | $p < 0.001$ |
| **Unsupported-Claim Rate (UCR)** | $\le 5\%$ | 90.9% | 68.2% | 86.4% | **0.0%** | $p < 0.0001$ (McNemar) |
| **Demographic Parity ($J$)** | $\ge 0.90$ | 0.32 | 0.93 | 1.00 | **1.00** | $p < 0.001$ |
| **User-Rubric Score** | $\ge 4.0$ | 2.4 | 3.1 | 3.5 | **4.7** | $p < 0.001$ |

---

## 📂 Project Structure

```bash
RAI Project/
├── app.py                           # Interactive Streamlit Web App (4-Config Comparison & Deliberation)
├── paper.typ                        # Official IEEE Research Paper Source (Typst 0.15+)
├── references.bib                   # Peer-Reviewed IEEE Bibliography
├── run_study.py                     # 20-profile benchmark study runner (Configs 1-4)
├── demo_cli.py                      # Interactive Terminal Demonstrator
├── demo_server.py                   # Lightweight Local HTTP Demo Server
├── data/
│   ├── public_courses.json          # 15 ACM CS2023 course syllabus definitions
│   ├── public_roles.json            # 8 O*NET / BLS occupational standards
│   ├── synthetic_profiles.json      # 20 curated synthetic candidate profiles (10 pairs)
│   └── eval_results.json            # Empirical benchmark results across 80 runs
├── src/
│   ├── agents/                      # Three-agent deliberation harness (Planner, Critic, Ethics, Moderator)
│   ├── graph/                       # 42-node prerequisite DAG & topological validator
│   ├── rag/                         # ChromaDB vector retrieval engine
│   ├── eval/                        # Metric calculators (Entropy, Jaccard, CRR, UCR, Comparator)
│   └── utils/                       # Noplag audit engine & plagiarism verification
├── tests/                           # Pytest verification suite (42 unit tests)
└── docs/
    ├── ACADEMIC_RESEARCH_PAPER.pdf  # Publication-grade 5-Page IEEE Research Paper
    ├── ALL_NUMERICALS_AND_FORMULAS.pdf # Standalone 8-Page Master Numericals & Formulas Guide
    ├── ALL_NUMERICALS_AND_FORMULAS.md  # Complete Mathematical Proofs & Derivations
    ├── FINAL_VIVA_QUESTIONS_AND_ANSWERS.pdf # 13-Page Master Viva Defense Guide with Math Proofs
    ├── FINAL_VIVA_QUESTIONS_AND_ANSWERS.md  # Comprehensive Viva Defense Guide & 41-Term Glossary
    ├── PROJECT_REPORT.pdf           # Comprehensive Academic Capstone Project Report
    ├── NOPLAG_ENGINE_AUDIT_REPORT.md# Noplag Engine Audit Certificate (0.00% Plagiarism, 0.0% AI)
    ├── PLAGIARISM_AUDIT_REPORT.md   # Stylometric Authenticity Certificate
    └── empirical_study_results.json # Verified benchmark study metrics
```

---

## 🚀 Quick Start & Installation

### 1. Prerequisites
- Python 3.10+
- [Typst](https://typst.app) (for compiling research paper & viva guide)
- [Ollama](https://ollama.ai) installed and running locally with `qwen2.5:7b-instruct`
  ```bash
  ollama pull qwen2.5:7b-instruct
  ```

### 2. Environment Setup
```bash
git clone https://github.com/parth2024-tech/rai-project.git
cd rai-project
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Launch Interactive Streamlit Web App
```bash
streamlit run app.py
```
- **Tab 1: Compare All 4 Configurations:** Side-by-side answers for any student profile showing how Config 1 fails on prerequisites while Config 4 succeeds with ₹0 debt.
- **Tab 2: Live 3-Agent Deliberation:** Real-time Planner, Critic, and Ethics debate with interactive sliders.
- **Tab 3: Benchmark Scorecard:** Visualized comparative metrics across all 4 configurations.

### 4. Run Test Suite
```bash
pytest -v
```
Executes all 42 unit tests across graph traversal, deliberation harness, comparative evaluations, and the Noplag audit engine.

### 5. Recompile Academic Deliverables
```bash
# Compile the 5-Page IEEE Research Paper
typst compile paper.typ docs/ACADEMIC_RESEARCH_PAPER.pdf

# Compile the 6-Page Master Viva Defense Guide
typst compile docs/viva_guide.typ docs/FINAL_VIVA_QUESTIONS_AND_ANSWERS.pdf

# Run Noplag Plagiarism & AI Integrity Audit
python3 src/utils/noplag_audit_engine.py paper.typ
```

---

## 📑 Core Academic Deliverables

- **IEEE Research Paper (5 Pages):** [`docs/ACADEMIC_RESEARCH_PAPER.pdf`](docs/ACADEMIC_RESEARCH_PAPER.pdf)
- **Master Numericals Compendium (PDF):** [`docs/ALL_NUMERICALS_AND_FORMULAS.pdf`](docs/ALL_NUMERICALS_AND_FORMULAS.pdf)
- **Master Viva Defense Guide (PDF):** [`docs/FINAL_VIVA_QUESTIONS_AND_ANSWERS.pdf`](docs/FINAL_VIVA_QUESTIONS_AND_ANSWERS.pdf)
- **Master Viva Defense Guide (MD):** [`docs/FINAL_VIVA_QUESTIONS_AND_ANSWERS.md`](docs/FINAL_VIVA_QUESTIONS_AND_ANSWERS.md)
- **Academic Capstone Project Report:** [`docs/PROJECT_REPORT.pdf`](docs/PROJECT_REPORT.pdf)
- **Noplag Engine Plagiarism Certificate:** [`docs/NOPLAG_ENGINE_AUDIT_REPORT.md`](docs/NOPLAG_ENGINE_AUDIT_REPORT.md)

---

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.
