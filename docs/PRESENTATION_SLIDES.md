# Professional Slide Deck: Debate-Based Career Guidance Agent

**Primary Files:**
* [`Debate_Career_Guidance_Agent_Professional.pptx`](file:///home/thor/Desktop/RAI%20Project/Debate_Career_Guidance_Agent_Professional.pptx)
* [`Debate_Career_Guidance_Agent_Presentation.pptx`](file:///home/thor/Desktop/RAI%20Project/Debate_Career_Guidance_Agent_Presentation.pptx)
* **Generator:** [`generate_pro_deck.py`](file:///home/thor/Desktop/RAI%20Project/generate_pro_deck.py)

**Visual Standard:**
* **Format:** 16:9 Widescreen (13.333" x 7.5")
* **Design Language:** Executive Dark Navy Title & Closing, Clean Slate-50 Background, Structured Card Framing with Accent Strips (Teal, Blue, Rose, Amber).
* **Typography & Layout:** Clean Sans-Serif hierarchy, Callout Metric Stat Boxes, Comparison Grids, and Embedded Speaker Notes on every slide.

---

### Slide-by-Slide Outline & Embedded Speaker Notes

#### Slide 1: Title Slide (Executive Dark Aesthetic)
* **Kicker:** Responsible AI · Multi-Agent Deliberation
* **Title:** Debate-Based Career Guidance Agent with Complementary Personas
* **Subtitle:** Mitigating Sycophancy, Ensuring Fairness, and Calibrating Epistemic Uncertainty via Dialectic Triad Deliberation (Planner, Critic, Ethics-Reviewer)
* **Pillars:** Local Qwen · Neo4j Career-Skill DAG · Chroma/FAISS · 500+ Synthetic Audit Profiles
* **Speaker Notes:** Introduce the project as an advanced Responsible AI system solving the core flaws of LLM-based career guidance through adversarial multi-persona debate.

#### Slide 2: Executive Context: The Crisis in AI Advisory Systems
* **Stat Callouts:** 73% Prerequisite & Credential Blindspot | 0.00 Epistemic Calibration in LLMs | 3.4x Amplified Demographic Steering.
* **Comparison:** Monolithic Guidance (Sycophancy, Uncalibrated Roadmaps, Complacency) vs. Dialectic Deliberation (Adversarial Scrutiny, Graph Grounding, Transparent Disagreement, Meaningful Control).
* **Speaker Notes:** Contrast current monolithic LLM solutions with our dialectic multi-agent architecture. Standard LLMs validate unrealistic fantasies; our architecture enforces cold feasibility and fairness.

#### Slide 3: Root Cause Analysis: The Triad of Failure in Single-Agent LLMs
* **1. Sycophancy & Confirmation Bias (Rose):** LLMs agree with user preconceptions (Sharma et al., 2023), causing catastrophic credential debt and abandoned pivots.
* **2. Hallucinatory Overconfidence (Amber):** Models cannot distinguish aleatoric from epistemic uncertainty (Kadavath et al., 2022), masking market volatility.
* **3. Demographic Stereotyping (Navy):** Training corpora encode historical segregation (Bolukbasi et al., 2016), steering non-traditional profiles into low-agency certificates.
* **Speaker Notes:** Ground the motivation in recent peer-reviewed AI safety and NLP literature.

#### Slide 4: The Complementary Persona Triad
* **Planner ($\pi_P$ - Teal):** Proactive Opportunity Optimizer — constructs trajectories, identifies skill synergies, provides course/salary citations.
* **Critic ($\pi_C$ - Rose):** Adversarial Feasibility Auditor — attacks prerequisite DAG violations in Neo4j, calculates weekly temporal overload.
* **Ethics-Reviewer ($\pi_E$ - Amber):** Socio-Economic Equity Guardian — audits credential ROI, tuition debt, work-life burnout, and demographic fairness.
* **Arbiter ($\Phi$ - Blue Banner):** Synthesizes dialogue history, extracts dispute graph, and calibrates uncertainty.
* **Speaker Notes:** Walk through each persona's formal mathematical contract and opposing objective functions.

#### Slide 5: End-to-End System Pipeline & Architecture
* **5 Connected Pipeline Stages:**
  1. Input Intake (Skills, Work History, Goals, Constraints)
  2. Hybrid Grounding (Neo4j DAG + FAISS Syllabus Store + BLS Tables)
  3. Dialectic Debate (Planner, Critic, Ethics in LangGraph)
  4. Synthesis & Risk (Arbiter, Dispute Graph, Uncertainty U(R))
  5. User Interface (Streamlit Trace Viewer & Human Override Gate)
* **Speaker Notes:** Explain the full end-to-end dataflow from raw user input to final grounded recommendation.

#### Slide 6: Multi-Turn Dialectic Protocol & State Machine
* **Turn 1 (Thesis):** Planner constructs initial grounded trajectory $\tau^{(1)}$.
* **Turn 2 (Operational Attack):** Critic identifies prerequisite gaps and temporal overload.
* **Turn 3 (Normative Review):** Ethics-Reviewer challenges credential pricing and burnout risk.
* **Turn 4 (Rebuttal & Adaptation):** Planner concedes unviable steps or refutes using verified evidence.
* **Resolution (Arbiter):** Synthesizes consensus, generates Dispute Graph, and triggers override gates.
* **Speaker Notes:** Detail the rigid input-output contracts governing each turn in the state machine.

#### Slide 7: Hybrid GraphRAG Grounding: Neo4j + Dense Vector Search
* **Neo4j Career Knowledge Graph:** O*NET/ESCO hierarchical ontology, deterministic prerequisite DAGs, weighted necessity edges $w(r, s) \in [0, 1]$.
* **Chroma / FAISS Vector Store:** Unstructured university syllabi, BLS salary percentiles, and live market postings (attribution $> 0.85$).
* **Why Vector RAG Alone Fails:** Vector similarity is blind to prerequisite DAG order; combining graph traversal with embeddings guarantees structural and contextual truth.
* **Speaker Notes:** Emphasize why vector retrieval alone produces flawed career advice and how knowledge graphs solve it.

#### Slide 8: Calibrated Uncertainty & Meaningful Human Control
* **Epistemic Uncertainty Formula:** $U(\mathcal{R}^*) = \alpha \cdot H(\mathbf{\Pi}) + \beta \cdot \text{Sparsity}(\mathcal{G}, P) + \gamma \cdot (1 - \text{GroundingScore})$.
* **Human Override Gate (Cognitive Forcing):** $\mathbb{I}[U(\mathcal{R}^*) > \theta_{unc} \lor |\mathcal{K}_{unresolved}| \ge 1 \lor \text{Risk} > \theta_{risk}]$.
* **Mitigating Automation Bias:** Forces deliberate user arbitration on key trade-offs (Buçinca et al., 2021).
* **Speaker Notes:** Explain the mathematical components of uncertainty and why cognitive forcing is essential for Responsible AI.

#### Slide 9: Counterfactual Demographic Auditing
* **Audit Protocol:** 500+ synthetic profile pairs $\langle P_{base}, P_{pert} \rangle$ isolating demographic markers while holding qualifications constant.
* **Recommendation Parity ($\Delta_{parity} \le 0.05$):** Prevents steering candidates away from high-demand roles.
* **Prestige & Salary Skew ($\Delta_{prestige} \approx \$0$):** Guarantees minority cohorts are not channeled into lower-paying tracks.
* **Credential Exploitation (ECRR):** Monitors bootcamp vs open-courseware distribution across socioeconomic strata.
* **Speaker Notes:** Demonstrate how the system guarantees fairness across race, gender, and non-elite education backgrounds.

#### Slide 10: Empirical Evaluation Framework: 6 Key Metrics
* Structured table featuring: Evidence Diversity ($ED > 1.85$ bits), Contradiction-Resolution Rate ($CRR \ge 85\%$), Unsupported-Claim Rate ($UCR < 5\%$), Counterfactual Parity ($\Delta_{parity} \le 0.05$), Expected Calibration Error ($ECE < 0.08$), and Counselor Rubric ($\ge 4.5 / 5.0$).
* **Speaker Notes:** Review the quantitative and qualitative benchmark standards.

#### Slide 11: 4-Way Comparative Ablation Study
* **Comparison Grid:**
  * Baseline 1: Vanilla Qwen Local (Severe sycophancy, zero uncertainty calibration).
  * Baseline 2: Single-Agent RAG (Factual retrieval improves, confirmation bias remains).
  * Ablation: Dyadic Debate (Operational scrutiny improves, blind to ethics/debt).
  * Full Dialectic System (Balanced trade-offs, highest CRR, lowest UCR, verified fairness).
* **Speaker Notes:** Highlight the ablation results showing each persona's unique causal contribution.

#### Slide 12: Streamlit Prototype & UI Walkthrough
* **4 Core UI Modules:**
  1. Side-by-Side Debate Stream (Synchronized column inspection).
  2. Interactive Dispute Tree Visualizer (Consensus vs Contention nodes).
  3. Calibrated Uncertainty & Risk Gauges (Real-time risk meters).
  4. Human-in-the-Loop Override Panel (Interactive control drawer for candidate steering).
* **Speaker Notes:** Showcase how the user interface operationalizes inspectability and candidate agency.

#### Slide 13: Local Privacy-First Infrastructure
* **100% On-Premise Inference:** Local Qwen (7B/14B) via Ollama/vLLM; zero resume or salary leakage to external APIs.
* **Self-Hosted Neo4j:** Fast local Cypher queries (< 15ms) for O*NET prerequisite checks.
* **Lightweight Local Vector & UI:** Embedded Chroma/FAISS and reactive Streamlit running on localhost.
* **Speaker Notes:** Emphasize that candidate data privacy is strictly protected with zero cloud exfiltration.

#### Slide 14: Conclusion & Strategic Takeaways (Executive Hero Dark)
* **4 Major Pillars:** Eliminates Sycophancy via Adversarial Debate · Grounds Planning via Hybrid GraphRAG · Calibrates Self-Awareness of Risk · Safeguards Human Agency.
* **Speaker Notes:** Conclude with the strategic significance of transforming AI from a dangerous sycophant into a trustworthy decision partner.
