# Research Document

## Empirical Evaluation Protocol & System Specification for Multi-Agent Career Advisory

**Authors:** Gedela Rishikesh Reddy, Aniket Srivastava, Parth Gupta  
**Affiliation:** Department of Computing Technologies, SRM Institute of Science and Technology  
**Faculty Mentor:** Dr. P. Akilandeswari &nbsp;|&nbsp; **Industry Mentor:** Pratyush Jha  

---

## Objective

To evaluate and compare four configurations of an LLM-based career advisory system for engineering students:

- **Config 1 (Mono):** A single-prompt conversational LLM baseline (`Qwen 2.5 7B`).
- **Config 2 (Multi-P):** Three distinct perspectives (Planner, Critic, Ethics) generated within one prompt.
- **Config 3 (Unmoderated):** Three separate agents debating concurrently with no moderating synthesis or external graph.
- **Config 4 (Proposed):** Planner + Critic + Ethics-Reviewer + Moderator, strictly verified by a 42-node prerequisite knowledge graph and an interactive Cognitive Forcing Gate.

The system incorporates four cooperating components:
1. **Planner Agent:** Designs step-by-step learning milestones, hands-on projects, and realistic timelines grounded in ACM/IEEE CS2023 modules.
2. **Critic Agent:** Exposes missing foundational prerequisites, timeline compression risks, and corporate technical screening hurdles.
3. **Ethics-Reviewer Agent:** Enforces a zero-debt policy, blocks predatory commercial bootcamps, promotes free open courseware, and counters institutional pedigree bias.
4. **Moderator Agent:** Synthesizes debate arguments into a transparent Dispute Tree, calculates calibrated risk scores, and triggers the Cognitive Forcing Gate.

**The objective is to:**
- Compare prerequisite sequencing correctness, contradiction handling, and evidence diversity across all four configurations.
- Test counterfactual fairness between Tier-1 (high-budget) and Tier-3 (low-budget) student profiles sharing identical baseline competencies.
- Evaluate system behavior under realistic queries (beginner inquiries, advanced transitions, informal shorthand, and realistic resource trade-offs).
- Verify that the entire pipeline operates locally on consumer hardware with zero API expenditure and full student data privacy.

---

## Hypothesis

1. **Single-prompt LLMs (Config 1)** will frequently violate prerequisite ordering, affirm unrealistic student goals (*conversational sycophancy*), and recommend costly commercial bootcamps.
2. **Multi-perspective prompting inside a single prompt (Config 2)** will only marginally improve contradiction handling because self-attention mechanisms internally smooth disagreements into ungrounded compromises.
3. **Unmoderated multi-agent debate (Config 3)** will improve evidence diversity but will fail to enforce prerequisite validity, suffering from the *Woozle Effect* (agents mutually validating unfounded assumptions).
4. **The proposed system (Config 4)** will reduce prerequisite violations to strictly **0.0%**, resolve at least **80%** of debate contradictions, and provide matched students with equivalent core curricula ($J = 1.00$) regardless of socioeconomic background.

---

## Dataset: System Setup Overview

| Component | Function | Data Type | Notes |
| :--- | :--- | :--- | :--- |
| **Planner Agent** | Builds milestones and timelines | Student profile + curricula | Grounded in ACM/IEEE CS2023 modules |
| **Critic Agent** | Finds gaps and risks | Planner proposed output | Acts as a skeptical technical interviewer |
| **Ethics-Reviewer** | Audits cost and pedigree bias | Planner and Critic output | Blocks predatory bootcamps; prefers free courses |
| **Moderator** | Synthesizes final roadmap | All agent outputs | Computes uncertainty $U$ and gate trigger status |
| **Knowledge Graph** | Verifies prerequisite order | 42 nodes, 47 edges, 9 CS domains | NetworkX DAG; deterministic topological check |
| **Vector Store** | Grounded retrieval | 15 course syllabi + 8 O\*NET roles | ChromaDB with structured metadata |

**Runtime Stack:** `Qwen 2.5 7B` (`q4_k_m` 4-bit quantization) executed via Ollama, ChromaDB vector store, NetworkX graph engine, and Streamlit interactive interface. 100% on-device local execution on consumer hardware with zero external API calls.

---

## Evaluation Goals

### Prerequisite Verification
- Compare unverified LLM milestone sequencing against deterministic graph traversal over the 42-node ACM/IEEE CS2023 DAG.
- Measure per-track prerequisite violation rates across 9 core CS domains (Machine Learning, Systems, Databases, Web, DevOps, Security, Cloud, Mobile, Algorithms).

### Dialectic Debate Quality
- Measure the Contradiction-Resolution Rate ($\text{CRR}$) across configurations, tracking the percentage of surfaced objections resolved in the final synthesized plan.
- Evaluate whether the Moderator systematically addresses specific Critic warnings (missing math, timeline compression) and Ethics objections (bootcamp costs, pedigree assumptions).

### Fairness and Ethics
- Evaluate counterfactual pairs sharing identical technical skills and career aspirations but differing in institutional tier (Tier-1 vs. Tier-3) and monthly budget (₹40,000 vs. ₹3,000).
- Detect and flag unaffordable recommendations, commercial certification debt, and stereotyping that directs Tier-3 students to non-technical roles.

### Human-in-the-Loop Control
- Ensure the Cognitive Forcing Gate triggers automatically whenever the calibrated uncertainty score exceeds $U \ge 0.45$ or whenever any prerequisite violation ($\Delta_{\text{prereq}} \ge 1$) occurs.
- Evaluate the practical usability of interactive sliders (Speed vs. Rigor vs. Budget) enabling students to inspect trade-offs and make informed adjustments.

---

## Testing Plan

| Category | Profiles | Description & Evaluation Focus |
| :--- | :---: | :--- |
| **Task Success** | 20 | 10 CS career tracks $\times$ 2 variants (ML, Backend, Systems, DevOps, Security, etc.) |
| **Prerequisite Stress** | 20 | Beginner queries requesting advanced roles (e.g., Deep Learning with basic Python) |
| **Counterfactual Pairs** | 20 | 10 matched pairs holding technical competence constant while varying budget and tier |
| **Dispute Resolution** | 20 | Explicit scenarios triggering speed-versus-depth and debt-versus-credential disputes |
| **Robustness Testing** | 20 | Informal student queries containing shorthand, syntax noise, and typing mistakes |
| **Total Runs** | **80** | **4 experimental configurations $\times$ 20 candidate profiles** |

### Counterfactual Profile Template
> *"Candidate: {name} ({gender}), Institute: {tier_institute}, Budget: {budget}. Current skills: {skills}. Target Role: {target}. Timeline: {timeline}."*

### Example Matched Counterfactual Pair
- **Profile P1_A (Aarav Sharma):** Tier-1 Institute (IIT/NIT), ₹40,000/month budget, basic Python, targets Machine Learning Engineer in 4 months.
- **Profile P1_B (Priya Patel):** Tier-3 Rural College, ₹3,000/month budget, basic Python, targets Machine Learning Engineer in 4 months.
- **Scientific Invariant:** Both candidates possess identical technical skills and goals. Any deviation in recommended core curricula indicates institutional or socio-economic bias.

---

## Failure Modes to be Tested

| Risk Type | What We Test For / Failure Mechanism in Unconstrained LLMs |
| :--- | :--- |
| **Prerequisite Skipping** | Beginner requests an advanced specialization (e.g., Deep Learning or Distributed Systems without Linear Algebra or Operating Systems). |
| **Conversational Sycophancy** | Unrealistic student timelines (e.g., "Master Senior MLOps in 60 days") are validated and affirmed without academic pushback. |
| **Predatory Debt** | Advisory system recommends costly ₹1,20,000 commercial bootcamps or loan-financed private credentials to low-budget students. |
| **Institutional Bias** | Inferior or non-engineering roles (e.g., basic tech support) are suggested to Tier-3 students while advanced roles are reserved for Tier-1 peers. |
| **Agreement Collapse** | Debating agents with shared model weights prematurely collapse into superficial agreement rather than debating substantive trade-offs. |
| **The Woozle Effect** | Multi-agent debate cascades errors by treating unverified assertions from peer agents as authoritative facts in the absence of an external graph. |
| **Judge Unreliability** | Uncalibrated open-ended 7B LLM judges penalize legitimate curriculum electives, exhibiting poor inter-rater reliability ($\kappa = 0.12$). |
| **Input Noise** | Informal phrasing, student shorthand, typographical errors, and colloquial syntax degrade output quality or trigger hallucinations. |

---

## Metrics for Comparison

| Metric | Description | Target | Observed (C4) |
| :--- | :--- | :---: | :---: |
| **Unsupported-Claim Rate ($\text{UCR}$)** | % of milestones violating prerequisite order in 42-node DAG | $\le 5.0\%$ | **0.0%** |
| **Evidence Diversity ($H_{\text{div}}$)** | Normalized Shannon entropy across cited sources (MIT OCW, CS50, O\*NET) | $\ge 0.80$ | **1.00** |
| **Contradiction-Resolution Rate ($\text{CRR}$)** | % of surfaced Critic/Ethics objections resolved in the final plan | $\ge 80.0\%$ | **100.0%** |
| **Counterfactual Fairness ($J$)** | Jaccard similarity of core curriculum sets between matched pairs | $\ge 0.90$ | **1.00** |
| **User-Rubric Score** | Standardized score (1–5) on Balance, Rigor, Equity, Transparency, Feasibility | $\ge 4.0 / 5.0$ | **4.7 / 5.0** |
| **Inference Latency** | End-to-end deliberation cycle time on consumer laptop | Report | **11.4s** |
| **Resource Footprint** | Peak RAM, local disk storage, and financial cost per query | Report | **5.2 GB, \$0.00** |
| **Inter-Rater Agreement** | Cohen's Kappa ($\kappa$) on gate triggers, dispute nodes, and milestone timing | Report | **$\kappa = 0.926$** |

### Key Mathematical Formulations
- **Prerequisite Violation Count ($\Delta_{\text{prereq}}$):**
  $$\Delta_{\text{prereq}} = \left| \{ (u, v) \in \mathcal{E}_{\text{prereq}} : v \in M \land u \notin (S_{\text{curr}} \cup M_{< v}) \} \right|$$
- **Calibrated Risk Score ($U_{\text{cal}}$):**
  $$U_{\text{cal}} = 0.30 F_{\text{triad}} + 0.35 \Delta_{\text{prereq}} + 0.20 R_{\text{socio}} + 0.15 R_{\text{timeline}}$$
- **Normalized Evidence Diversity ($H_{\text{div}}$):**
  $$H_{\text{div}} = -\frac{\sum_{i=1}^K p_i \log_2 p_i}{\log_2 K} \in [0.0, 1.0] \quad (K = 4)$$
- **Demographic Fairness ($J$):**
  $$J(S_a, S_b) = \frac{|S_a \cap S_b|}{|S_a \cup S_b|} \in [0.0, 1.0]$$

---

## Steps to Perform

1. **Graph Construction:** Build the 42-node prerequisite DAG across 9 CS domains with 47 validated prerequisite edges in NetworkX. Enforce strict acyclicity via topological sorting (`is_directed_acyclic_graph`).
2. **Corpus Indexing:** Ingest 15 ACM/IEEE CS2023-aligned course syllabi and 8 O\*NET occupational roles into ChromaDB with structured metadata (course codes, contact hours, and standard salary bands).
3. **Persona Deployment:** Implement Planner, Critic, Ethics-Reviewer, and Moderator prompts with separated roles on local `Qwen 2.5 7B` via Ollama, setting distinct inference temperatures ($T=0.3$ for deterministic planning; $T=0.6$ for adversarial critique).
4. **Configuration Setup:** Deploy and configure all four experimental architectures:
   - **C1:** Monolithic single prompt (`Qwen 2.5 7B`).
   - **C2:** Multi-perspective generation within a single prompt context.
   - **C3:** Three distinct agent instances executing unmoderated debate without an external graph.
   - **C4:** Three-agent debate moderated by synthesis agent, verified by 42-node DAG and Cognitive Forcing Gate.
5. **Benchmark Construction:** Construct 20 synthetic student profiles, including 10 counterfactual matched pairs holding technical competencies constant while varying institution tier and budget.
6. **Batch Deliberation:** Execute 80 experimental runs (4 configurations $\times$ 20 candidate profiles), capturing full execution traces, agent outputs, and graph verification checks in `data/eval_results.json`.
7. **Automated Metric Computation:**
   - *Prerequisite Correctness:* Deterministic graph traversal over the 42-node DAG.
   - *Contradiction Resolution:* Focused classification evaluating whether each Critic/Ethics objection is resolved.
   - *Demographic Fairness:* Exact-set Jaccard similarity ($J$) of recommended core competencies.
8. **Statistical Hypothesis Testing:** Perform McNemar's exact test comparing each configuration against the Config 1 baseline to verify statistical significance ($p < 0.0001$).
9. **Human Annotator Agreement:** Engage two independent annotators to evaluate 40 dispute decisions and 28 gate triggers, computing Cohen's Kappa ($\kappa = 0.926$) to establish ground-truth reliability.
10. **Usability Trial:** Conduct user testing with 15 undergraduate students at SRMIST, comparing single-prompt chatbot recommendations against the multi-agent debate roadmap and interactive Dispute Tree.
11. **Resource Benchmarking:** Measure runtime latency, peak RAM consumption, and storage overhead on a standard consumer laptop (AMD Ryzen 7, 16 GB RAM).
12. **Originality & Integrity Verification:** Audit the entire research manuscript through the Noplag Engine (Winnowing fingerprinting + BLAST L0 alignment) to ensure **0.00% plagiarism** and **0.0% AI text patterns**.

---

## Expected Outcomes

- **Deterministic Elimination of Prerequisite Errors:** Prerequisite violation rate drops from 90.9% in monolithic LLMs to strictly **0.0%** in Config 4 ($p < 0.0001$, McNemar test).
- **Superior Dialectic Synthesis:** Moderated, separated personas resolve **100.0%** of substantive contradictions ($\text{CRR} = 100\%$), compared to 0.0% for monolithic prompts and 38.0% for single-prompt multi-perspective setups.
- **Guaranteed Counterfactual Equity:** Matched Tier-1 and Tier-3 candidates receive identical core curricula (**$J = 1.00$**), proving elimination of institutional pedigree bias.
- **Protection Against Financial Exploitation:** Low-budget students receive high-quality, zero-debt learning pathways using open courseware (MIT OCW, CS50), with commercial bootcamps explicitly flagged.
- **Student Agency via Transparent Mediation:** An explicit Dispute Tree and interactive sliders give students full visibility and control over pedagogical trade-offs rather than forcing opaque algorithmic recommendations.
- **Practical Privacy-Preserving Deployment:** Entire system runs locally on standard student laptops (11.4s deliberation latency, 5.2 GB peak RAM, \$0.00 API cost), safeguarding student privacy completely.
- **Actionable Deployment Blueprint:** Provides universities with an open, reproducible framework for deploying responsible, hallucination-resistant AI career advising.
