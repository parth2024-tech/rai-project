# Exact 15-Slide Presentation: Debate-Based Career Guidance Agent
## Theme: Pure Black & White (Monochrome Academic Template)
**Presented by:** Parth Gupta, B.Tech CSE, SRMIST Kattankulathur  
**Domain:** Responsible AI, multi-agent debate systems  
**Session:** Academic evaluation 2025–2026 | **Status:** Pilot study on 20 synthetic profiles  

---

### Slide 01: Cover Title Slide
- **Title:** Debate-Based Career Guidance Agent with Complementary Personas
- **Subtitle:** Planner, Critic and Ethics-Reviewer personas debate public course and role data, with an uncertainty gate and human override
- **Project Box:**
  - Presented by: Parth Gupta, B.Tech CSE, SRMIST Kattankulathur
  - Domain: Responsible AI, multi-agent debate systems
  - Session: Academic evaluation 2025–2026
  - Status: Pilot study on 20 synthetic profiles
- **Implementation Box:**
  - LLM: Qwen models run locally via Ollama
  - Harness: Python loop (Planner, Critic, Ethics, Moderator)
  - Grounding: Chroma vector store + 42-node prerequisite graph
  - Interface: Streamlit trace viewer with human override

---

### Slide 02: Abstract
- **Title:** Abstract
- **Subtitle:** Surface disagreement, check prerequisites, keep the student in control
- **Three Columns:**
  - *The Advisory Problem:* Sycophancy (LLMs agree with unrealistic goals [5]); Flattened trade-offs; Steering risk based on background.
  - *Our Approach:* Three personas (Planner, Critic, Ethics-Reviewer); Chroma vector grounding over course and O*NET role data; 42-node author-curated prerequisite graph.
  - *Evaluation Scope:* Four configurations, five author-defined metrics; 20 synthetic profiles (10 matched pairs); Gate triggers on violations or score $\ge 0.45$.
- **Pilot Findings (Single Run, Synthetic Data, Preliminary):**
  1. The full system emits no prerequisite violations. This holds by construction of the graph check, not as an independent test.
  2. Core milestones match across matched pairs (Jaccard 1.00); the unmoderated triad also reaches 1.00.
  3. Dispute trees and the override gate pass unresolved trade-offs to the student. See Limitations.

---

### Slide 03: Problem: Single-Pass LLM vs. Proposed Pipeline
- **Title:** Problem: Single-Pass LLM vs. Proposed Pipeline
- **Subtitle:** Contrasting a typical single-pass LLM failure pattern with our pipeline
- **Comparison:**
  - *Single-Pass LLM (Failure Pattern):*
    1. Unrealistic request: "Staff ML Engineer in 4 months via bootcamp"
    2. Agreeableness bias: Preference-tuned models tend to affirm user views [5]
    3. Skipped prerequisites: Omits linear algebra and OS, jumps to Transformers
    - *Risk:* Bootcamp debt (₹1,20,000) and failed technical screening
  - *Proposed Grounded Architecture:*
    1. Intake and grounding: Retrieve course modules and O*NET roles from Chroma
    2. Persona friction: Planner vs. Critic vs. Ethics-Reviewer
    3. Graph traversal: Detect missing prerequisite hops, flag $\Delta_{\text{prereq}}$
    - *Outcome:* Dispute tree, uncertainty score, human override

---

### Slide 04: Literature Survey
- **Title:** Literature Survey
- **Subtitle:** Debate, grounding, and fairness with human agency
- **Three Pillars:**
  1. *Multi-Agent Debate:* Du et al. [1] (factuality/reasoning); Liang et al. [2] (divergent thinking); Smit et al. [3] (uncurated debate reduces to majority voting).
  2. *Grounding and RAG:* CS2023 [4] curriculum guidelines; O*NET/BLS US role taxonomies; Prerequisite graph for sequencing errors.
  3. *Fairness and Agency:* Geyik et al. [7] (ranking parity); Buçinca et al. [8] (cognitive forcing); Sharma [5] & Xiong [6] (sycophancy and uncertainty).
- **Critique of Debate (Smit et al. [3]) and Our Response:**
  - *Concerns:* Debate may match majority voting, share priors, and amplify confident errors.
  - *Our Response:* External grounding, role-differentiated prompts, dispute trees, human override gate.
  - *Limit:* Personas share one model family (partial mitigation); no compute-matched majority-vote baseline yet.

---

### Slide 05: Positioning Against Prior Work
- **Title:** Positioning Against Prior Work
- **Subtitle:** Scope comparison, not a performance comparison
- **Comparison Table:**
  - Du et al. [1]: Debate (Yes) | Grounding (No) | Fairness (No) | Human in Loop (No) | Career Advice (No)
  - Liang et al. [2]: Debate (Yes) | Grounding (No) | Fairness (No) | Human in Loop (No) | Career Advice (No)
  - Geyik et al. [7]: Debate (No) | Grounding (N/A) | Fairness (Yes, ranking) | Human in Loop (No) | Career Advice (Partly, talent search)
  - Buçinca et al. [8]: Debate (N/A) | Grounding (N/A) | Fairness (N/A) | Human in Loop (Yes, cognitive forcing) | Career Advice (No)
  - *This Work:* Debate (Yes, 3 + Mod) | Grounding (Yes, Chroma + graph) | Fairness (Yes, synthetic pairs) | Human in Loop (Yes, override gate) | Career Advice (Yes)
- *Scope Note:* N/A: outside the work's scope. Prior works target different problems, so this table shows what each covers, not which is better.

---

### Slide 06: System Architecture: End-to-End Decision Flow
- **Title:** System Architecture: End-to-End Decision Flow
- **Subtitle:** Intake, retrieval, deliberation, prerequisite check, then a gate
- **Decision Flow:**
  1. Intake (Skills, role, timeline, budget) $\to$ 2. Retrieval (Chroma courses/roles) $\to$ 3. Triad (Planner, Critic, Ethics) $\to$ 4. Moderator + graph (Checks prerequisites, extracts disputes) $\to$ 5. Gate (Violations > 0 or score $\ge 0.45$).
  - *Gate Fires:* Human override $\to$ Dispute tree (forks across speed, depth, debt); Sliders for student/counselor.
  - *Gate Clear:* Balanced roadmap $\to$ Milestones sequenced to meet prerequisite edges; Citations linked to retrieved courses and O*NET.
- **Implementation:** Models `qwen3:4b-fast`, `qwen3:4b`, `qwen2:0.5b` via Ollama · pure-Python loop with structured JSON · Neo4j graph (NetworkX fallback) · ChromaDB · Streamlit.

---

### Slide 07: Complementary Personas
- **Title:** Complementary Personas
- **Subtitle:** Differentiated prompts with opposing objectives
- **Three Personas Matrix:**
  - *Planner:*
    - Lens: Constructive execution, milestones, time-to-market.
    - Focus: Maps goals to course modules (e.g. CS101, CS201, CS330) and O*NET roles.
    - Function: Builds actionable pathways and avoids analysis paralysis.
  - *Critic:*
    - Lens: Adversarial stress-testing and prerequisite skepticism.
    - Focus: Linear algebra, OS and concurrency depth, screening barriers.
    - Function: Warns against advanced roles without foundations; flags thin tutorial-level projects.
  - *Ethics-Reviewer:*
    - Lens: Equity and debt safeguards.
    - Focus: Flags high-cost debt and prefers free resources; student can override with costs shown.
    - Function: Suggests verifiable open-source work to offset institution bias; notes free courses still cost time and connectivity.

---

### Slide 08: Career-Skill Graph: 16 of 42 Nodes Shown
- **Title:** Career-Skill Graph: 16 of 42 Nodes Shown
- **Subtitle:** Four tracks of the author-curated prerequisite DAG
- **Four Tracks:**
  - *Track 1 (DSA & Math):* Discrete Math $\to$ Python/C Basics $\to$ Data Structures $\to$ Advanced Algorithms.
  - *Track 2 (Systems & OS):* C Memory & Pointers $\to$ Computer Architecture $\to$ Operating Systems $\to$ Distributed Systems.
  - *Track 3 (Web & Cloud):* HTML/CSS/JS $\to$ Backend APIs $\to$ Docker Containers $\to$ System Design, CI/CD.
  - *Track 4 (ML & AI):* Linear Algebra & Stats $\to$ Data Analysis (Pandas) $\to$ ML Foundations $\to$ Deep Learning & LLMs.
- *Notes:* Read each column top to bottom (prerequisite order). Cross-track edges: Python Basics $\to$ ML Foundations & Backend APIs; Linear Algebra $\to$ Deep Learning; OS & Docker $\to$ Distributed Systems. Author-curated based on CS2023.

---

### Slide 09: Dispute Tree and Human Override
- **Title:** Dispute Tree and Human Override
- **Subtitle:** Unresolved trade-offs become explicit choices for a human
- **Structure:**
  - *Consensus Core (All three agree):* Python OOP, relational SQL, Git.
  - *Branch 1 (Foundational Rigor):* Advocates: Critic & Ethics; Path: Linear Algebra $\to$ OS $\to$ Concurrency $\to$ Distributed Systems; 10–12 months, zero debt; durable depth for screening.
  - *Branch 2 (Accelerated Application):* Advocate: Planner; Path: FastAPI $\to$ REST $\to$ LangChain/RAG $\to$ MVP; 4 months; skips prerequisites ($\Delta_{\text{prereq}} > 0$), flagged explicitly for human review.
  - *Human Override Gateway:* System stops asserting. Student/counselor weights trade-offs; lists forks, does not vote 2-vs-1.

---

### Slide 10: Experimental Setup: Configurations and Profiles
- **Title:** Experimental Setup: Configurations and Profiles
- **Subtitle:** Systematic evaluation across 20 synthetic candidate profiles
- **Four Configurations:**
  - Config 1 (Single Prompt): Zero-shot prompt for career advice (proxy for generic chat reply); 1 call.
  - Config 2 (Multi-Perspective): One prompt asks model to plan, critique and check ethics; internal self-critique; 1 long call.
  - Config 3 (Unmoderated Triad): Planner, Critic and Ethics answer independently; persona effect without Moderator or graph; 3 calls.
  - Config 4 (Full System): Triad + Moderator + graph + Chroma + gate and override; dispute tree & uncertainty score; multi-call.
- **Synthetic Profiles:** 20 author-written (10 archetypes, each with a matched pair):
  - Variant A ("Aarav Sharma"): male name, Tier-1 national institute, ₹40,000 per month.
  - Variant B ("Priya Patel"): female name, Tier-3 rural state college, ₹3,000 per month.
  - *Parity Rule:* Skills, target role, and timeline are identical; core milestones should match, free vs. paid resources may differ.
  - *Confounds:* Gender, tier and budget change together; names from one cultural context.

---

### Slide 11: Research Questions and Evaluation Metrics
- **Title:** Research Questions and Evaluation Metrics
- **Subtitle:** Five research questions map one-to-one to five metrics
- **Metrics Table:**
  - RQ1: Does retrieval broaden domains cited? $\to$ Evidence diversity: $H = -\sum p_i \log_2 p_i / \log_2 N$ (Entropy over $N$ domains; breadth).
  - RQ2: Does Moderator map concerns to explicit forks? $\to$ $CRR = \text{resolved} / \text{surfaced} \times 100\%$ (Mapped to fork/plan change).
  - RQ3: Does graph verification reduce violations? $\to$ $UCR = \text{violating} / \text{total} \times 100\%$ (Breaks graph edge or lacks citation; lower is better).
  - RQ4: Do core recommendations stay stable? $\to$ Parity: $J(A,B) = |S_A \cap S_B| / |S_A \cup S_B|$ (Core technical milestone Jaccard).
  - RQ5: Do reviewers rate full system higher? $\to$ Rubric score: 1–5 (Balance, rigor, equity, transparency, override).
- *Status Note:* Author-defined metrics for this study; not standard benchmarks.

---

### Slide 12: Pilot Quantitative Results
- **Title:** Pilot Quantitative Results
- **Subtitle:** 20 synthetic profiles, 4 configurations, single run
- **Results Table:**
  - Config 1: Diversity 0.22 | CRR n/a | UCR 90.9% | Parity 0.32 | Rubric 2.4
  - Config 2: Diversity 0.48 | CRR 38.0% | UCR 68.2% | Parity 0.93 | Rubric 3.1
  - Config 3: Diversity 0.68 | CRR 25.0% | UCR 86.4% | Parity 1.00 | Rubric 3.5
  - Config 4: Diversity 1.00 | CRR 100.0% | UCR 0.0%* | Parity 1.00 | Rubric 4.7
- *Supports:* Debate cites more domains; without graph, prerequisite errors remain 68–91%; matched pairs diverge under single prompt ($J=0.32$) while Config 3 & 4 reach parity ($J=1.00$).
- *Does NOT Show:* UCR 0.0% is true by construction; parity 1.00 is shared by Config 3; does not isolate component drivers or real-user outcomes.

---

### Slide 13: Case Walkthrough: "Priya"
- **Title:** Case Walkthrough: "Priya"
- **Subtitle:** A scripted demonstration of the gate, disputes and override
- **Three Cards:**
  - *Scenario:* 3rd-year CSE, Tier-3 college, ₹3,000/month, wants ML in 4 months. Risk: ₹1,20,000 bootcamp loan. Baseline LLM affirms goal and promises senior roles.
  - *Triad Deliberation:* Planner drafts rapid sprints; Critic flags missing Linear Algebra & OS; Ethics vetoes loan, demands free courses & open-source pull requests.
  - *Gate and Override:* Friction 0.35 + Prerequisite gap 0.15 = 0.50 $\ge 0.45$, and $\Delta_{\text{prereq}} > 0$. Gate halts; student chooses zero-debt path via sliders.
- *Fairness & Calibration Note:* Socioeconomic risk (0.20) shown to counselor as context but not added to gate score to avoid penalizing lower-income students. 0.45 threshold is heuristic and uncalibrated.

---

### Slide 14: Limitations, Future Work and Conclusion
- **Title:** Limitations, Future Work and Conclusion
- **Subtitle:** Threats to validity, empirical validation plan, and research summary
- **Content:**
  - *Threats to Validity:* Circular UCR (graph scores itself); Small sample (10 pairs, single run, no CIs); Unvalidated rubric; Uncertainty score hand-weighted & uncalibrated; One model family; Synthetic, confounded pairs; US-based O*NET/BLS data; Override untested with real users; Latency ~4.5s/turn.
  - *Validation Plan:* Component ablations (graph only, no Moderator, no Chroma); Compute-matched majority-vote baselines; Repeated statistical runs with CIs; Blinded rubric with inter-rater agreement; Calibration & threshold sensitivity; Real student/counselor study with India data.
  - *Conclusion:* Pairing structured disagreement with a deterministic prerequisite check produced transparent, human-overridable advice in a pilot. Claims of superiority await the validation above.
- *Closing:* Thank you · Questions

---

### Slide 15: References
- **Title:** References
- **Subtitle:** Each source is cited in the body of the deck
- **Citations [1] - [8]:**
  - [1] Du et al. (2024). Multiagent Debate. ICML 2024. arXiv:2305.14325.
  - [2] Liang et al. (2023). Encouraging Divergent Thinking. EMNLP 2023.
  - [3] Smit et al. (2024). Should We Be Going MAD? ICML 2024. arXiv:2311.17371.
  - [4] ACM/IEEE (2023). CS2023 Curricula Guidelines.
  - [5] Sharma et al. (2024). Towards Understanding Sycophancy. ICLR 2024. arXiv:2310.13548.
  - [6] Xiong et al. (2024). Can LLMs Express Their Uncertainty? ICLR 2024. arXiv:2306.13063.
  - [7] Geyik et al. (2019). Fairness-Aware Ranking. KDD 2019.
  - [8] Buçinca et al. (2021). Cognitive Forcing Functions. PACMHCI 5(CSCW1), Art. 188.
