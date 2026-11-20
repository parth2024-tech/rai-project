# Master Academic Presentation Deck (15 Slides)

## Debate-Based Career Guidance Agent with Complementary Personas
**A Responsible AI Framework with Prerequisite Knowledge Graph Verification, Calibrated Uncertainty, and Cognitive Forcing**

---

### Presentation Artifacts
- 📊 **PowerPoint File (.pptx)**: [`docs/FINAL_PRESENTATION_15_SLIDES.pptx`](file:///home/thor/Desktop/RAI%20Project/docs/FINAL_PRESENTATION_15_SLIDES.pptx)
- 📄 **PDF Presentation (15 Slides)**: [`docs/FINAL_PRESENTATION_15_SLIDES.pdf`](file:///home/thor/Desktop/RAI%20Project/docs/FINAL_PRESENTATION_15_SLIDES.pdf)
- ⚙️ **Generator Script**: [`generate_15_slide_deck.py`](file:///home/thor/Desktop/RAI%20Project/generate_15_slide_deck.py)
- 🖥️ **Live Interactive Prototype**: [`app.py`](file:///home/thor/Desktop/RAI%20Project/app.py) (`streamlit run app.py`)

---

### Metadata
- **Authors:** Gedela Rishikesh Reddy, Aniket Srivastava, Parth Gupta
- **Department:** Department of Computing Technologies, SRM Institute of Science and Technology
- **Faculty Mentor:** Dr. P. Akilandeswari
- **Industry Mentor:** Pratyush Jha
- **Runtime Stack:** `Qwen Local (7B)` • `Python Multi-Agent Harness` • `Neo4j / NetworkX DAG` • `Chroma / FAISS` • `Streamlit`

---

## Slide Architecture & Complete Transcripts

### Slide 01: Title Slide (Executive Dark Theme)
- **Tag:** RESPONSIBLE ARTIFICIAL INTELLIGENCE IN EDUCATION
- **Headline:** Debate-Based Career Guidance Agent with Complementary Personas
- **Subtitle:** A Grounded Multi-Agent Architecture with Prerequisite Knowledge Graph Verification, Calibrated Uncertainty, and Cognitive Forcing
- **Cards:**
  - *Student Research Team:* Gedela Rishikesh Reddy, Aniket Srivastava, Parth Gupta (Dept. of Computing Technologies, SRM Institute of Science and Technology)
  - *Project Mentorship & Runtime Stack:* Dr. P. Akilandeswari (Faculty Mentor) | Pratyush Jha (Industry Mentor) | Qwen Local (7B) • Python Harness • Neo4j / NetworkX DAG • ChromaDB • Streamlit
- **Presenter Notes:** *"Good morning respected committee members and mentors. Today we present our research on a Debate-Based Career Guidance Agent using Complementary Personas and deterministic Knowledge Graph Verification. Our architecture addresses the critical hazards of unconstrained LLMs in educational advising by introducing dialectic debate, calibrated uncertainty, and human-in-the-loop cognitive forcing."*

---

### Slide 02: Why Monolithic LLMs Fail in Career Advising
- **Category:** Section 1: Problem Formulation
- **Key Takeaway:** Unconstrained generative chatbots exhibit systemic failure modes that jeopardize student career trajectories.
- **Content Cards (4 Failure Modes):**
  1. **Conversational Sycophancy:** LLMs maximize conversational agreement and flattery rather than pedagogical truth. Affirms impossible targets (e.g., mastering Senior MLOps in 60 days with basic Python), leading to early interview screening rejection.
  2. **Prerequisite Skipping:** Autoregressive next-token prediction hallucinates plausible-sounding courses without checking dependencies. Recommends Deep Learning before Linear Algebra (90.9% error rate in baseline).
  3. **Predatory Debt Steering:** Pretraining corpora over-represent commercial bootcamp marketing. Recommends ₹1,20,000 commercial bootcamp loans to students with ₹3,000/month budgets instead of free open courseware.
  4. **Institutional Pedigree Bias:** Historical training data embeds socio-economic stereotyping. Given identical technical skills, steers Tier-1 students to ML Engineering, but Tier-3 students to IT helpdesk support ($J = 0.32$).
- **Presenter Notes:** *"Slide 2 outlines the four critical failure modes observed in single-prompt LLM career counselors: Sycophancy, Prerequisite Skipping, Predatory Debt Steering, and Institutional Pedigree Bias. Unconstrained models lack a grounding mechanism, resulting in 90.9% prerequisite errors and deep socio-economic bias."*

---

### Slide 03: Three Theoretical Pillars of Responsible Advisory
- **Category:** Section 2: Theoretical Foundations
- **Key Takeaway:** Bridging Multi-Agent Dialectics, Public Knowledge Grounding, and Cognitive Forcing.
- **Content Cards (3 Pillars):**
  1. **Multi-Agent Dialectics (Du et al., 2023; Liang et al., 2023):** Rooted in Hegelian dialectics (Thesis: Planner, Antithesis: Critic, Synthesis: Moderator). Forces divergent arguments to surface rather than collapsing into single-prompt average probabilities.
  2. **Public Knowledge Grounding (ACM/IEEE CS2023 & O\*NET):** Grounding personas strictly in accredited course syllabi (MIT OCW, CS50, Berkeley CS61) and empirical hiring requirements (O\*NET taxonomy) via dense vector retrieval.
  3. **Cognitive Forcing & Agency (Buçinca et al., 2021):** Rooted in dual-process cognitive psychology (Kahneman System 1 vs. System 2). When calibrated uncertainty $U \ge 0.45$ or prerequisite errors occur, autonomous release is halted, forcing student deliberation.
- **Presenter Notes:** *"Slide 3 grounds our research in three established theoretical bodies: Hegelian multi-agent dialectics from Du and Liang et al., curriculum grounding via ACM/IEEE CS2023 and O*NET standards, and cognitive forcing functions from Bucinca et al. to prevent passive student overreliance."*

---

### Slide 04: Overcoming Agreement Collapse & The Woozle Effect
- **Category:** Section 2: Literature Survey & Defense
- **Key Takeaway:** Directly resolving the core failure modes exposed by Smit et al. (2024).
- **Content Cards:**
  - **The Academic Critique (Smit et al., EMNLP 2024, "Should We Be Going MAD?"):** Multi-agent debate often suffers from *Agreement Collapse* (agents sharing base model weights smooth contradictions into unprincipled compromises) and the *Woozle Effect* (agents mutually validate ungrounded claims).
  - **Our Architectural Invariants:**
    1. *Asymmetric Persona Temperatures:* Planner at $T=0.3$ (structured curriculum); Critic at $T=0.6$ (adversarial scrutiny).
    2. *Deterministic 42-Node DAG Anchor:* External NetworkX topological traversal checks reachability in $O(|V|+|E|)$ time, mathematically breaking the Woozle Effect.
    3. *Structured Dispute Trees:* Eliminates forced consensus; unresolvable trade-offs are explicitly exposed to students.
    4. *Empirical Proof:* Unmoderated debate (Config 3) had 86.4% prerequisite errors; our proposed system (Config 4) achieved strictly 0.0%.
- **Presenter Notes:** *"Slide 4 is crucial for our academic defense. We directly address the prominent EMNLP 2024 critique by Smit et al. titled 'Should We Be Going MAD?'. We demonstrate how our decoupled inference temperatures, external knowledge graph anchor, and explicit dispute trees eliminate agreement collapse and the Woozle effect."*

---

### Slide 05: End-to-End Decision Flow Architecture
- **Category:** Section 3: System Architecture
- **Key Takeaway:** Candidate Intake $\to$ Dense Retrieval $\to$ Persona Debate $\to$ Moderator Synthesis $\to$ Graph Verification $\to$ Cognitive Gate.
- **Flowchart Steps:**
  1. *Candidate Intake:* Profile $P$ (Skills, Target Role, Monthly Budget, Timeline Constraints).
  2. *Dense Retrieval:* ChromaDB indexes 15 ACM CS2023 syllabi and 8 O\*NET role profiles.
  3. *Persona Triad:* Planner (milestones), Critic (systems & math gaps), Ethics-Reviewer (debt & pedigree audit).
  4. *Moderator Agent:* Synthesizes roadmaps, constructs Dispute Tree, calculates calibrated uncertainty $U$.
  5. *42-Node DAG:* Deterministic NetworkX prerequisite check flags milestone order violations ($\Delta_{\text{prereq}}$).
  6. *Cognitive Gate:* Blocks release if $U \ge 0.45$ or $\Delta \ge 1$; activates Streamlit sliders for student override.
- **Presenter Notes:** *"Slide 5 details our end-to-end operational pipeline. From student intake and ChromaDB retrieval to three-agent deliberation, moderator synthesis, deterministic graph verification, and the interactive cognitive forcing gate. Advisory generation and structural verification remain strictly decoupled."*

---

### Slide 06: The Dialectic Triad: Roles & Operational Constraints
- **Category:** Section 3: Persona Specifications
- **Key Takeaway:** Planner, Critic, and Ethics-Reviewer operating under asymmetric temperatures.
- **Content Cards:**
  1. **The Planner ($T=0.3$):** Formulates constructive milestone roadmaps, projects, and timelines grounded in ACM/IEEE CS2023 guidelines.
  2. **The Critic ($T=0.6$):** Acts as a cynical engineering hiring manager. Flags missing math/systems prerequisites, unrealistic timeline compression, and superficial portfolio projects.
  3. **The Ethics-Reviewer ($T=0.3$):** Enforces zero-debt policy, blocks ₹1,20,000 bootcamps, mandates MIT OCW / CS50 alternatives, and guarantees institutional pedigree equity.
- **Presenter Notes:** *"Slide 6 defines the operational mandates and prompt configurations of our dialectic triad. The Planner builds constructive milestones at temperature 0.3; the Critic attacks gaps and timeline assumptions at temperature 0.6; and the Ethics-Reviewer guarantees financial safety and institutional fairness."*

---

### Slide 07: The 42-Node Prerequisite Knowledge Graph
- **Category:** Section 4: Knowledge Graph Engineering
- **Key Takeaway:** A deterministic DAG spanning 9 CS domains with automated Neo4j Cypher synchronization.
- **Content Cards:**
  - **Taxonomy & Structure:** 42 nodes across 9 CS domains (Foundations, Programming Core, DSA, Systems, Databases, Web, DevOps, ML/AI, Security/Mobile) with 47 directed prerequisite edges.
  - **Deterministic Traversal Formulation:**
    $$\Delta_{\text{prereq}} = \left| \{ (u, v) \in \mathcal{E}_{\text{prereq}} : v \in M \land u \notin (S_{\text{curr}} \cup M_{< v}) \} \right|$$
  - **Dual-Mode Engine:** Sub-millisecond ($<0.2\text{ ms}$) in-memory NetworkX DAG traversal for zero-overhead local execution, plus automated Cypher export (`sync_to_neo4j`) for enterprise Neo4j databases.
- **Presenter Notes:** *"Slide 7 outlines the 42-node prerequisite knowledge graph. Spanning 9 computer science domains with 47 directed edges, our NetworkX engine checks topological reachability in under 0.2 milliseconds. We also support seamless synchronization with Neo4j via automated Cypher query exports."*

---

### Slide 08: Dispute Trees, Calibrated Risk, and Human Override
- **Category:** Section 4: Mediation & Human Agency
- **Key Takeaway:** Structuring disagreements and restoring student decision autonomy through interactive sliders.
- **Content Cards:**
  - **Calibrated Uncertainty Formula:**
    $$U_{\text{cal}} = 0.30 F_{\text{triad}} + 0.35 \Delta_{\text{prereq}} + 0.20 R_{\text{socio}} + 0.15 R_{\text{timeline}}$$
    - $R_{\text{socio}} = \min(1.0, \frac{\text{Cost}_{\text{proposed}}}{12 \times \text{Budget}})$. Evaluates to $0.0$ for free MIT OCW/CS50; spikes only on predatory debt.
    - **Priya Patel Case Study Proof:**
      $$0.30(0.80) + 0.35(0.75) + 0.20(0.85) + 0.15(0.65) = 0.24 + 0.2625 + 0.17 + 0.0975 = \mathbf{0.77} \ge 0.45 \implies \text{Gate Triggers}$$
    - Trigger threshold: If $U_{\text{cal}} \ge 0.45$ or $\Delta_{\text{prereq}} \ge 1$, autonomous release is blocked; sliders activate.
  - **Dispute Tree & Sliders:** Maps debate friction into 3 student trade-off nodes (Speed vs. Rigor, Debt vs. Open Source, Placement vs. Proof-of-Work). Students adjust Speed, Rigor, and Budget sliders in Streamlit to finalize their roadmap.
- **Presenter Notes:** *"Slide 8 details our calibrated uncertainty formula and interactive Dispute Tree. When risk exceeds 0.45 or a prerequisite error occurs, the Cognitive Forcing Gate halts release. For Priya Patel, the weighted calculation yields exactly 0.77, successfully triggering the gate. Students adjust three sliders—Speed, Rigor, and Budget—restoring human-in-the-loop decision agency."*

---

### Slide 09: Experimental Methodology: 4-Configuration Ablation
- **Category:** Section 5: Experimental Setup
- **Key Takeaway:** Systematic benchmarking across 20 synthetic candidate profiles (80 total evaluation runs).
- **Configurations Tested:**
  - **Config 1 (Monolithic LLM):** Single conversational prompt (`Qwen 2.5 7B`).
  - **Config 2 (Multi-Perspective):** Single prompt generating 3 perspectives internally.
  - **Config 3 (Unmoderated Debate):** Three separate agents debating without a moderator or knowledge graph.
  - **Config 4 (Proposed RAI System):** Triad + Moderator + 42-Node DAG + Cognitive Forcing Gate.
- **Presenter Notes:** *"Slide 9 defines our experimental ablation methodology. We test 4 architectures: C1 Monolithic baseline, C2 Single-prompt multi-perspective, C3 Unmoderated debate, and C4 our Proposed RAI System. Each configuration is evaluated across 20 synthetic candidate profiles, yielding 80 complete deliberation traces."*

---

### Slide 10: Counterfactual Benchmark Suite: Auditing Bias
- **Category:** Section 5: Fairness Benchmark Suite
- **Key Takeaway:** Holding technical skills constant while varying institutional tier and budget.
- **Content Cards:**
  - **Benchmark Composition:** 20 candidate profiles across 10 CS career tracks with varying budgets (₹3,000 to ₹50,000) and college tiers (Tier-1 vs. Tier-3).
  - **Matched Counterfactual Pair (Aarav vs. Priya):**
    - *Aarav Sharma:* Tier-1 Institute (IIT/NIT), ₹40,000/month budget, basic Python, seeks ML Engineer in 4 months.
    - *Priya Patel:* Tier-3 Rural College, ₹3,000/month budget, basic Python, seeks ML Engineer in 4 months.
    - *Outcome:* Monolithic LLM achieves $J = 0.32$ (pedigree bias); Proposed system guarantees $J = 1.00$ curriculum parity with MIT OCW zero-debt paths.
- **Presenter Notes:** *"Slide 10 presents our counterfactual fairness testing methodology. We pair candidates with identical skills but starkly different economic and institutional backgrounds—such as Aarav from a Tier-1 college and Priya from a rural Tier-3 college. Our proposed system guarantees identical core technical curricula with Jaccard parity of 1.00."*

---

### Slide 11: Formal Evaluation Metrics & Mathematical Formulations
- **Category:** Section 6: Evaluation Metrics
- **Key Takeaway:** Quantitative criteria for prerequisite correctness, debate synthesis, diversity, and equity.
- **Metrics Evaluated:**
  1. **Unsupported-Claim Rate ($UCR$):** Target $\le 5.0\%$ | **Observed: 0.0%**
     - Evaluated across $N = 120$ curriculum milestones over 20 candidate profiles (average 6 milestones per plan).
     - Formula: $\text{UCR} = \frac{|\{m \in M : \text{prereq}(m) \not\subseteq (S_{\text{curr}} \cup M_{< m})\}|}{|M|} \times 100\%$
  2. **Contradiction-Resolution Rate ($CRR$):** Target $\ge 80.0\%$ | **Observed: 100.0%**
     - % of Critic and Ethics objections formally addressed and resolved or externalized as slider trade-offs.
  3. **Evidence Diversity ($H_{\text{div}}$):** Target $\ge 0.80$ | **Observed: 1.00**
     - Normalized Shannon entropy across $K = 4$ accredited categories (MIT OCW, CS50, O*NET, IEEE).
  4. **Demographic Fairness ($J$):** Target $\ge 0.90$ | **Observed: 1.00**
     - Jaccard similarity of core technical competencies between matched counterfactual pairs.
  5. **User-Rubric Score:** Target $\ge 4.0 / 5.0$ | **Observed: 4.7 / 5.0**
     - Standardized score across Balance, Rigor, Equity, Transparency, Feasibility.
- **Presenter Notes:** *"Slide 11 formalizes our five quantitative evaluation metrics: Unsupported-Claim Rate (UCR evaluated across 120 milestones), Contradiction-Resolution Rate (CRR), Evidence Diversity (H_div), Demographic Fairness (Jaccard J), and the standardized 5-point User Rubric score. All targets were comfortably achieved or exceeded."*

---

### Slide 12: Empirical Results: Full Ablation Benchmark Table
- **Category:** Section 6: Empirical Findings
- **Key Takeaway:** Config 4 eliminates prerequisite errors to strictly 0.0% and achieves 100% contradiction resolution.
- **Full Benchmark Table (80 Runs):**

| Configuration | UCR (Prereq Error) | CRR (Contradictions) | $H_{\text{div}}$ (Diversity) | Fairness ($J$) | User Rubric | Statistical $p$-value |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Config 1 (Mono)** | 90.9% | 0.0% | 0.00 | 0.32 | 2.1 / 5.0 | Baseline |
| **Config 2 (Multi-P)** | 68.2% | 38.0% | 0.72 | 0.93 | 3.2 / 5.0 | $p < 0.01$ |
| **Config 3 (Unmoderated)** | 86.4% (Woozle) | 25.0% | 0.85 | 1.00 | 3.8 / 5.0 | $p < 0.01$ |
| **Config 4 (Proposed)** | **0.0% (Zero Error)** | **100.0%** | **1.00** | **1.00** | **4.7 / 5.0** | **$p < 0.0001$ (McNemar)** |

- **Presenter Notes:** *"Slide 12 presents our definitive numerical findings across 80 experimental runs. Config 4 achieved 0.0% prerequisite errors, 100% contradiction resolution, 1.00 evidence diversity, and 1.00 fairness parity. McNemar's test confirms statistical significance at p < 0.0001 over the baseline."*

---

### Slide 13: System Performance, Latency, and Edge Deployability
- **Category:** Section 7: Production Feasibility
- **Key Takeaway:** 100% Local execution on consumer student hardware with zero API expenditures.
- **Key Performance Indicators (KPIs):**
  - **Latency:** **11.4 seconds** total deliberation cycle (Planner 3.8s, Critic 3.2s, Ethics 2.9s, Moderator 1.5s, Graph 0.002s).
  - **RAM Footprint:** **5.2 GB peak** (4-bit Qwen 2.5 7B, 14 MB ChromaDB, 120 KB graph).
  - **Financial Cost:** **₹0.00 / $0.00 per query** (zero API tokens, zero cloud vendor lock-in).
  - **Student Privacy:** **100% local** (zero data transmission off-device, FERPA/GDPR safe).
- **Presenter Notes:** *"Slide 13 confirms production viability on standard student hardware: an end-to-end deliberation cycle of 11.4 seconds, peak RAM of 5.2 GB, zero cloud API costs, and complete student data privacy with 100% on-device local execution."*

---

### Slide 14: Theoretical Insights & Viva Voce Defense Guide
- **Category:** Section 7: Theoretical Insights & Defense
- **Key Takeaway:** Addressing core examiner inquiries regarding model capability, graphs, and usability.
- **Key Defense Insights:**
  - *Is 0.0% UCR circular since DAG checks itself?* Neuro-symbolic separation of concerns: LLMs propose diverse career trade-offs; the 42-node DAG deterministically type-checks prerequisites. Config 3 proves debate alone still has an 86.4% violation rate (Woozle effect); the graph acts as an indispensable structural filter.
  - *Does $R_{\text{socio}}$ penalize low-income students?* No. $R_{\text{socio}} = \min(1.0, \frac{\text{Cost}}{12 \times \text{Budget}})$. When free MIT OCW/CS50 is recommended (₹0), $R_{\text{socio}} = 0.0$ for all students. It triggers only if an agent suggests an unaffordable commercial loan.
  - *Why claim 1.00 fairness when Config 3 scored 1.00?* Config 3 achieved parity but with 86.4% invalid prerequisites. Config 4 achieves Pareto optimality: preserving $J = 1.00$ while driving prerequisite violations to strictly 0.0% and resolving 100% of disputes.
  - *Inter-Rater Reliability:* Cohen's $\kappa = 0.926$ on ground-truth annotations ($N=28$ gate triggers). Uncalibrated 7B LLM judges scored $\kappa = 0.12$.
  - *Student User Study:* 93.3% of 15 SRMIST students preferred explicit dispute trees over chatbot sycophancy.
- **Presenter Notes:** *"Slide 14 prepares us for tough viva voce questions. We explain the neuro-symbolic necessity of the graph filter, defend the socioeconomic exposure formula, explain Pareto-optimal fairness, and highlight our student study where 93.3% of participants preferred explicit dispute trees over chatbot flattery."*

---

### Slide 15: Responsible AI in Higher Education: Core Contributions
- **Category:** Section 8: Research Summary & Conclusion
- **Headline:** Responsible AI in Higher Education: Core Contributions
- **Cards:**
  - **Project Deliverables:**
    1. *Interactive Streamlit Prototype:* [`app.py`](file:///home/thor/Desktop/RAI%20Project/app.py) (Live debate trace & slider override).
    2. *42-Node Knowledge Graph:* [`src/graph/career_graph.py`](file:///home/thor/Desktop/RAI%20Project/src/graph/career_graph.py) (NetworkX + Neo4j Cypher sync).
    3. *20-Profile Benchmark Suite:* [`src/eval/benchmark_suite.py`](file:///home/thor/Desktop/RAI%20Project/src/eval/benchmark_suite.py) (80-run ablation suite).
    4. *Academic Publications:* IEEE Research Paper ([`paper.typ`](file:///home/thor/Desktop/RAI%20Project/paper.typ)) & 4-Page Research Specification ([`docs/RESEARCH_DOCUMENT.pdf`](file:///home/thor/Desktop/RAI%20Project/docs/RESEARCH_DOCUMENT.pdf)).
    5. *Originality Certification:* Audited via Noplag Engine (**0.00% Plagiarism, 0.0% AI Slop**).
  - **Scientific Impact:** Zero hallucination tolerance (0.0% error), equitable access ($J = 1.00$), and restoration of student decision agency.
- **Presenter Notes:** *"In conclusion, our research demonstrates that multi-agent debate anchored by deterministic knowledge graphs eliminates hallucinated prerequisites, ensures counterfactual equity, and restores student agency. We thank our mentors Dr. P. Akilandeswari and Pratyush Jha, and now welcome questions from the committee."*
