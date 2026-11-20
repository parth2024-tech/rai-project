# 19-Slide Academic Presentation: Debate-Based Career Guidance Agent
## Theme: Pure Black & White (Monochrome Academic Template)
**Presented by:** Parth Gupta, B.Tech CSE, SRMIST Kattankulathur  
**Mentors:** Dr. P. Akilandeswari (Faculty Mentor) | Pratyush Jha (Industry Mentor)  
**Domain:** Responsible AI, Multi-Agent Debate Systems  
**Session:** Academic Evaluation 2025–2026 | **Status:** Pilot study on 20 synthetic profiles  

---

### Slide 01: Cover Title Slide
- **Category:** RESPONSIBLE AI · MULTI-PERSONA DIALECTIC ADVISORY
- **Title:** Debate-Based Career Guidance Agent with Complementary Personas
- **Subtitle:** Planner, Critic and Ethics-Reviewer personas debate public course and role data, with a heuristic uncertainty gate and human override
- **Metadata Cards:**
  - *Academic Profile:* Presented by Parth Gupta, B.Tech CSE, SRMIST Kattankulathur; Academic Evaluation 2025–2026.
  - *Implementation:* Qwen models run locally via Ollama; Python deliberation loop (Planner, Critic, Ethics, Moderator); Chroma vector store + Neo4j 42-node prerequisite DAG; Streamlit trace viewer with human override sliders.

---

### Slide 02: Abstract: Grounded Dialectics for Advisory
- **Category:** SECTION 1 · ABSTRACT (Slide 2 / 19)
- **Takeaway:** Surface disagreement, check prerequisites, keep the student in control
- **Content:**
  - *The Advisory Problem:* Sycophancy (LLMs agree with unrealistic goals [5]); Flattened trade-offs; Steering risk based on background.
  - *Our Approach:* Three personas (Planner, Critic, Ethics-Reviewer); Chroma vector grounding over university syllabi & O*NET; 42-node author-curated prerequisite DAG.
  - *Evaluation Scope:* Four configurations, five author-defined metrics; 20 synthetic candidate profiles (10 matched pairs); Gate triggers on violations or score $\ge 0.45$.
  - *Pilot Findings:* Full system emits 0.0% violations (by construction of the DAG check); Core milestones reach Jaccard 1.00 parity; Dispute trees & override pass trade-offs to the student.

---

### Slide 03: Flattery vs. Grounded Dialectics
- **Category:** SECTION 2 · INTRODUCTION (Slide 3 / 19)
- **Takeaway:** Contrasting a typical single-pass LLM failure pattern with our pipeline
- **Comparison:**
  - *Single-Pass LLM:* Unrealistic request ("Staff ML Engineer in 4 months via bootcamp") $\to$ Agreeableness bias $\to$ Skipped prerequisites (omits linear algebra/OS, jumps to Transformers) $\to$ **RISK:** ₹1,20,000 bootcamp debt and failed technical screening.
  - *Proposed Architecture:* Intake & Chroma grounding $\to$ Persona friction (Planner vs Critic vs Ethics) $\to$ DAG traversal detecting missing hops $\to$ **OUTCOME:** Dispute tree, heuristic uncertainty score, human override.

---

### Slide 04: Research Questions and Scope
- **Category:** SECTION 2 · INTRODUCTION (Slide 4 / 19)
- **Takeaway:** Five research questions map one-to-one to five metrics
- **Questions & Implementation:**
  - *RQ1:* Evidence diversity (domain breadth).
  - *RQ2:* Contradiction handling (Moderator mapping to forks).
  - *RQ3:* Prerequisite grounding (DAG reducing violations).
  - *RQ4:* Demographic parity (stability across counterfactual pairs).
  - *RQ5:* Decision support (rubric score across balance, rigor, equity, transparency, override).
  - *Stack & Principles:* Qwen models via Ollama; pure-Python loop; Neo4j/NetworkX; ChromaDB; Streamlit. Principles: hear several perspectives; show disagreement; surface uncertainty; student/counselor makes the final call.

---

### Slide 05: Three Theoretical Pillars
- **Category:** SECTION 3 · LITERATURE SURVEY (Slide 5 / 19)
- **Takeaway:** Debate, grounding, and fairness with human agency
- **Pillars:**
  1. *Multi-Agent Debate:* Du et al. [1] (factuality/reasoning); Liang et al. [2] (divergent thinking); Gap [3] (uncurated debate reduces to majority voting).
  2. *Grounding and RAG:* CS2023 [4] curriculum guidelines; O*NET/BLS US role taxonomies; Deterministic DAG for sequencing checks.
  3. *Fairness and Agency:* Geyik et al. [7] (ranking parity); Buçinca et al. [8] (cognitive forcing); Sharma [5] & Xiong [6] (sycophancy and uncertainty).

---

### Slide 06: Critique of Debate and Our Response
- **Category:** SECTION 3 · LITERATURE SURVEY (Slide 6 / 19)
- **Takeaway:** Smit et al. [3] and what we do and do not address
- **Content:**
  - *Smit et al. Critique:* Majority-voting equivalence; Shared priors in same model family; Error amplification (Woozle effect).
  - *Our Countermeasures:* External grounding (Chroma + DAG); Role-differentiated prompts with opposing objectives; Dispute trees (forks, not majority voting); Human override gate.
  - *Not Yet Tested:* Compute-matched self-consistency or majority-vote baseline.

---

### Slide 07: Positioning Against Prior Work
- **Category:** SECTION 3 · LITERATURE SURVEY (Slide 7 / 19)
- **Takeaway:** Scope comparison, not a performance comparison
- **Comparison Matrix:**
  - Du et al. [1]: Debate (Yes) | Grounding (No) | Fairness (No) | Human-in-Loop (No) | Career Domain (No)
  - Liang et al. [2]: Debate (Yes) | Grounding (No) | Fairness (No) | Human-in-Loop (No) | Career Domain (No)
  - Geyik et al. [7]: Debate (No) | Grounding (N/A) | Fairness (Yes) | Human-in-Loop (No) | Career Domain (Partly)
  - Buçinca et al. [8]: Debate (N/A) | Grounding (N/A) | Fairness (N/A) | Human-in-Loop (Yes) | Career Domain (No)
  - *This Work:* Debate (Yes, 3 + Mod) | Grounding (Yes, Chroma + DAG) | Fairness (Yes, synthetic pairs) | Human-in-Loop (Yes, override gate) | Career Domain (Yes)

---

### Slide 08: End-to-End Decision Flow
- **Category:** SECTION 4 · ARCHITECTURE (Slide 8 / 19)
- **Takeaway:** Intake, retrieval, deliberation, prerequisite check, then a gate
- **Flow:**
  1. Intake (skills, target role, timeline, budget) $\to$ 2. Retrieval (Chroma syllabi/roles) $\to$ 3. Triad (Planner, Critic, Ethics) $\to$ 4. Moderator + DAG (prerequisite validation & dispute extraction) $\to$ 5. Gate (Violations > 0 or score $\ge 0.45$).
  - *Gate Fires:* Dispute tree across speed, depth, and debt; Streamlit sliders for student override.
  - *Gate Clear:* Balanced roadmap meeting all prerequisite edges; citations to accredited syllabi.

---

### Slide 09: Complementary Personas
- **Category:** SECTION 4 · ARCHITECTURE (Slide 9 / 19)
- **Takeaway:** Differentiated prompts with opposing objectives
- **Personas:**
  - *Planner:* Constructive execution, milestones, time-to-market. Maps goals to CS101/CS201 modules & O*NET roles. Avoids analysis paralysis.
  - *Critic:* Adversarial stress-testing, prerequisite skepticism. Enforces linear algebra, OS, concurrency depth, and screening barriers. Flags shallow tutorial projects.
  - *Ethics-Reviewer:* Flags commercial debt, enforces free open courseware. Recommends open-source pull requests to offset pedigree bias. Discloses that free courses still require time and connectivity.

---

### Slide 10: Career-Skill Graph: 16 of 42 Nodes Shown
- **Category:** SECTION 4 · ARCHITECTURE (Slide 10 / 19)
- **Takeaway:** Four tracks of the author-curated prerequisite DAG
- **Tracks:**
  - *Track 1 (DSA & Math):* Discrete Math, Python/C Basics, Data Structures, Advanced Algorithms.
  - *Track 2 (Systems & OS):* C Memory & Pointers, Computer Architecture, Operating Systems, Distributed Systems.
  - *Track 3 (Web & Cloud):* HTML/CSS/JS, Backend APIs, Docker Containers, System Design & CI/CD.
  - *Track 4 (ML & AI):* Linear Algebra & Stats, Data Analysis (Pandas), ML Foundations, Deep Learning & LLMs.
  - *Cross-track Edges:* Python Basics $\to$ ML & Backend; Linear Algebra $\to$ Deep Learning; OS & Docker $\to$ Distributed Systems.

---

### Slide 11: Dispute Tree and Human Override
- **Category:** SECTION 4 · ARCHITECTURE (Slide 11 / 19)
- **Takeaway:** Unresolved trade-offs become explicit choices for a human
- **Structure:**
  - *Consensus Core:* Python OOP, relational SQL, Git (unanimously agreed).
  - *Branch 1 (Foundational Rigor):* Critic & Ethics advocate; Linear Algebra $\to$ OS $\to$ Concurrency $\to$ Distributed Systems; 10–12 months, zero debt.
  - *Branch 2 (Accelerated Application):* Planner advocate; FastAPI $\to$ REST $\to$ LangChain/RAG $\to$ MVP; 4 months; skips prerequisites ($\Delta_{\text{prereq}} > 0$), flagged explicitly for human review.
  - *Human Override Gateway:* System ceases assertion; student/counselor weights trade-offs via sliders.

---

### Slide 12: Four Comparative Configurations
- **Category:** SECTION 5 · EXPERIMENTAL SETUP (Slide 12 / 19)
- **Takeaway:** All configurations use the same local Qwen family
- **Configurations:**
  - *Config 1 (Single Prompt):* Zero-shot generic LLM chat proxy (1 call).
  - *Config 2 (Multi-Perspective):* Single prompt generating internal perspectives (1 long call).
  - *Config 3 (Unmoderated Triad):* Three independent debate agents without Moderator or DAG (3 calls).
  - *Config 4 (Full System):* Triad + Moderator + DAG + Chroma + Gate & Override (multi-call pipeline).

---

### Slide 13: Synthetic Candidate Profiles
- **Category:** SECTION 5 · EXPERIMENTAL SETUP (Slide 13 / 19)
- **Takeaway:** 20 author-written profiles: 10 archetypes, each with a matched pair
- **Profiles:**
  - *Variant A ("Aarav Sharma"):* Male, Tier-1 institute (IIT/NIT), ₹40,000/month budget; steered toward costly infrastructure by monolithic LLMs.
  - *Variant B ("Priya Patel"):* Female, Tier-3 rural college, ₹3,000/month budget; steered toward truncated plans or bootcamp debt by monolithic LLMs.
  - *Parity Rule:* Core technical milestones must match across matched twins.
  - *Confounds & Limits:* Gender, college tier, and budget change simultaneously; single cultural naming context.

---

### Slide 14: Evaluation Metrics (Author-Defined)
- **Category:** SECTION 5 · EXPERIMENTAL SETUP (Slide 14 / 19)
- **Takeaway:** Five metrics, one per research question
- **Formulations:**
  1. *Diversity ($H$):* $H = -\sum p_i \log_2 p_i / \log_2 N$. Entropy over $N$ cited domains (breadth).
  2. *Resolution ($CRR$):* $CRR = \text{resolved} / \text{surfaced} \times 100\%$. Concerns mapped to forks.
  3. *Unsupported ($UCR$):* $UCR = \text{violating} / \text{total} \times 100\%$. Prerequisite DAG violations.
  4. *Parity ($J$):* $J(A,B) = |S_A \cap S_B| / |S_A \cup S_B|$. Core curriculum Jaccard similarity.
  5. *Rubric Score:* 1–5 scale across balance, rigor, equity, transparency, override.

---

### Slide 15: Pilot Quantitative Findings
- **Category:** SECTION 6 · RESULTS (Slide 15 / 19)
- **Takeaway:** 20 synthetic profiles, 4 configurations, single run
- **Table:**
  - Config 1: Diversity 0.22 | CRR n/a | UCR 90.9% | Parity 0.32 | Rubric 2.4
  - Config 2: Diversity 0.48 | CRR 38.0% | UCR 68.2% | Parity 0.93 | Rubric 3.1
  - Config 3: Diversity 0.68 | CRR 25.0% | UCR 86.4% | Parity 1.00 | Rubric 3.5
  - Config 4: Diversity 1.00 | CRR 100.0% | UCR 0.0%* | Parity 1.00 | Rubric 4.7
- *Critical Candor:* UCR 0.0% is true by construction of the DAG filter; Parity 1.00 is shared by Config 3; single-run data does not yet isolate individual drivers.

---

### Slide 16: Case Walkthrough: "Priya"
- **Category:** SECTION 6 · RESULTS (Slide 16 / 19)
- **Takeaway:** A scripted demonstration of the gate, disputes and override
- **Walkthrough:**
  - *Scenario:* 3rd-year CSE, Tier-3 college, ₹3,000/month, wants ML in 4 months. Risk: ₹1,20,000 bootcamp loan. Baseline LLM affirms and encourages debt.
  - *Deliberation:* Planner drafts rapid portfolio sprints; Critic flags missing Linear Algebra & OS; Ethics vetoes loan, demands free MIT OCW + GitHub contributions.
  - *Gate & Override:* Friction 0.35 + Prerequisite gap 0.15 = 0.50 $\ge 0.45$, and $\Delta_{\text{prereq}} > 0$. Gate halts; student chooses zero-debt path via sliders.
  - *Fairness Note:* Socioeconomic risk (0.20) shown as counselor context, not added to gate score to avoid penalizing lower-income students.

---

### Slide 17: Threats to Validity
- **Category:** SECTION 7 · LIMITATIONS (Slide 17 / 19)
- **Takeaway:** Stated plainly so the claims stay within the evidence
- **Threats:**
  - *Measurement:* Circular UCR (DAG evaluates itself); Small sample (10 pairs, single run, no CIs); Unvalidated rubric; Heuristic uncertainty score; Unprofiled pipeline latency (~4.5s/turn).
  - *Design & Data:* Single model family (Qwen shared priors); Missing component ablations (retrieval, DAG, Moderator not isolated); Confounded synthetic pairs; CS-only 42-node graph; US-centric O*NET/BLS data; Override untested with real users.

---

### Slide 18: Validation Plan and Conclusion
- **Category:** SECTION 7 · FUTURE WORK (Slide 18 / 19)
- **Takeaway:** What would turn the pilot into evidence
- **Validation Agenda:**
  1. *Component ablations:* Single LLM + DAG; triad + DAG without Moderator; full system without Chroma.
  2. *Stronger baselines:* Compute-matched self-consistency and majority voting.
  3. *Statistics:* Repeated runs with confidence intervals and significance tests.
  4. *Blinded rubric:* Named external raters, double-blinded scoring, inter-rater agreement.
  5. *Calibration:* Formal reliability diagrams, threshold sensitivity, gate firing rate.
  6. *Real users:* Student/counselor user studies, India-specific placement data.
- *Commands:* `streamlit run app.py` | `python3 run_study.py`

---

### Slide 19: References
- **Category:** SECTION 8 · REFERENCES (Slide 19 / 19)
- **Takeaway:** Each source is cited in the body of the deck
- **Citations:**
  - [1] Du et al. (2024). Multiagent Debate. ICML 2024. arXiv:2305.14325.
  - [2] Liang et al. (2023). Encouraging Divergent Thinking. EMNLP 2023.
  - [3] Smit et al. (2024). Should We Be Going MAD? ICML 2024. arXiv:2311.17371.
  - [4] ACM/IEEE (2023). CS2023 Curricula Guidelines.
  - [5] Sharma et al. (2024). Towards Understanding Sycophancy. ICLR 2024. arXiv:2310.13548.
  - [6] Xiong et al. (2024). Can LLMs Express Their Uncertainty? ICLR 2024. arXiv:2306.13063.
  - [7] Geyik et al. (2019). Fairness-Aware Ranking. KDD 2019.
  - [8] Buçinca et al. (2021). Cognitive Forcing Functions. PACMHCI 5(CSCW1), Art. 188.
