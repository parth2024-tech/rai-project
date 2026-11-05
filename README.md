# A Local, Multi-Dimensional Evaluation Lab for Student Career Advisory LLM Agents

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Model: Qwen 2.5 7B](https://img.shields.io/badge/Ollama-Qwen%202.5%207B-purple.svg)](https://ollama.ai)
[![Streamlit UI](https://img.shields.io/badge/UI-Streamlit-red.svg)](https://streamlit.io)

An academic, reproducible, and fully local evaluation lab designed to benchmark student career-advisory large language model (LLM) agents across multi-agent dialectic debate, deterministic knowledge graph prerequisite validation, calibrated uncertainty, and demographic counterfactual fairness.

---

### Authors & Affiliation
- **Gedela Rishikesh Reddy**
- **Aniket Srivastava**
- **Parth Gupta**

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
├── app.py                      # Interactive Streamlit Prototype & Trace Viewer
├── run_study.py                # 20-profile benchmark study runner (Configs 1-4)
├── generate_paper_pdf.py       # IEEE 5-page publication compiler (HTML -> PDF via Chromium)
├── generate_deck.py            # Academic presentation slide generator (PPTX & PDF)
├── data/
│   ├── public_courses.json     # 15 ACM CS2023 course syllabus definitions
│   ├── public_roles.json       # 8 O*NET / BLS occupational standards
│   ├── synthetic_profiles.json # 20 curated synthetic candidate profiles (10 pairs)
│   └── eval_results.json       # Empirical benchmark results across 80 runs
├── src/
│   ├── agents/                 # Multi-persona deliberation harness (Planner, Critic, Ethics, Moderator)
│   ├── graph/                  # 42-node Neo4j curriculum DAG & topological validator
│   ├── rag/                    # ChromaDB vector retrieval engine
│   └── eval/                   # Metric calculators (Entropy, Jaccard, CRR, UCR, Bootstrap)
└── docs/
    ├── ACADEMIC_RESEARCH_PAPER.pdf  # Compiled 5-Page IEEE Publication Paper
    ├── ACADEMIC_RESEARCH_PAPER.html # Print template with textbook IEEE styling
    ├── ACADEMIC_RESEARCH_PAPER.md   # Full markdown source of the research paper
    ├── Final_Presentation.pdf       # 18-Slide Academic Presentation
    ├── PRESENTATION_SLIDES.md       # Slide deck documentation & speaker notes
    └── QA_DEFENSE_SHEET.md          # 20-question viva / defense question-and-answer sheet
```

---

## 🚀 Quick Start & Installation

### 1. Prerequisites
- Python 3.10+
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

### 3. Launch Interactive Streamlit Prototype
```bash
streamlit run app.py
```
Explore candidate profiles, trigger real-time multi-persona debates, view the 42-node prerequisite graph, inspect Dispute Trees, and test human override gates.

### 4. Run Comparative Evaluation Study
```bash
python3 run_study.py
```
Executes the four experimental configurations across all 20 candidate profiles and updates `data/eval_results.json`.

### 5. Recompile Academic Deliverables
```bash
# Compile the 5-page IEEE Research Paper
python3 generate_paper_pdf.py

# Compile the 18-slide Academic Presentation Deck
python3 generate_deck.py
```

---

## 📑 Academic Publications & Deliverables

- **IEEE Research Paper (5 Pages):** [`docs/ACADEMIC_RESEARCH_PAPER.pdf`](docs/ACADEMIC_RESEARCH_PAPER.pdf)
- **Academic Presentation Deck (18 Slides):** [`docs/Final_Presentation.pdf`](docs/Final_Presentation.pdf)
- **Viva Defense Sheet:** [`docs/QA_DEFENSE_SHEET.md`](docs/QA_DEFENSE_SHEET.md)

---

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.
