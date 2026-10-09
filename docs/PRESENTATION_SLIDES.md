# Slide Deck Outline: Debate-Based Career Guidance Agent

**File generated:** [`Debate_Career_Guidance_Agent_Presentation.pptx`](file:///home/thor/Desktop/RAI%20Project/Debate_Career_Guidance_Agent_Presentation.pptx)  
**Format:** 16:9 Widescreen (13.333" x 7.5"), Professional Academic & Technical Palette (Slate / Teal / Navy).

---

### Slide 1: Title Slide
* **Title:** Debate-Based Career Guidance Agent with Complementary Personas
* **Subtitle:** Mitigating Sycophancy, Ensuring Fairness, and Calibrating Epistemic Uncertainty via Dialectic Deliberation (Planner, Critic, Ethics-Reviewer)
* **Kicker:** Responsible AI · Multi-Agent Deliberation · Knowledge Graphs
* **Tech Stack:** Qwen Local (Ollama/vLLM) · LangGraph Python Multi-Agent · Neo4j Career Graph · Chroma/FAISS · Streamlit
* **Speaker Notes:** Introduce the project as an advanced Responsible AI system solving the core flaws of LLM-based career guidance through adversarial multi-persona debate.

---

### Slide 2: The Problem: Why Single-Agent LLMs Fail
* **Card 1: The Sycophancy Trap** — LLMs maximize conversational agreement, validating unrealistic career transitions and inducing catastrophic credential debt.
* **Card 2: Illusion of Certainty** — Generates authoritative, single-path roadmaps that mask hiring volatility, skill deprecation, and completion dropouts.
* **Card 3: Demographic Stereotyping** — Inherits historical workforce biases, systematically channeling non-traditional candidates into lower-agency certifications.
* **Speaker Notes:** Highlight how single-agent LLMs are structurally ill-suited for high-stakes, irreversible life decisions like career transitions.

---

### Slide 3: The Solution: Dialectic Multi-Persona Deliberation
* **Dialectic Triad Architecture:**
  * Planner (Thesis): Proposes career pathways and forward milestones.
  * Critic (Antithesis): Scrutinizes prerequisites, time bounds, and labor risks.
  * Ethics-Reviewer (Guardrail): Audits credential debt, well-being, and fairness.
  * Arbiter (Synthesis): Synthesizes balanced guidance, maps dispute traces, and calibrates uncertainty.
* **Responsible AI Pillars:** Avoiding one-sided advice, transparency of disagreement, demographic fairness, calibrated uncertainty, meaningful human override.
* **Speaker Notes:** Explain why a dialectic triad provides superior checks and balances compared to both single-agent systems and simple bilateral debates.

---

### Slide 4: Complementary Personas Deep-Dive
* **Planner Persona ($\pi_P$):** Proactive Opportunity Optimizer — Maps skills to target roles, generates milestones, defends paths with course & salary citations.
* **Critic Persona ($\pi_C$):** Adversarial Feasibility Auditor — Interrogates prerequisite DAG violations, temporal overload, and labor saturation risks.
* **Ethics-Reviewer ($\pi_E$):** Socio-Economic Equity Guardian — Audits tuition cost-to-income risk, work-life sustainability, and prevents demographic stereotyping.
* **Speaker Notes:** Detail the distinct prompt contracts and opposing mathematical objective functions governing each persona.

---

### Slide 5: Multi-Turn Dialectic Protocol & State Machine
* **Step 1:** Round 1 (Thesis) — Planner constructs initial grounded trajectory.
* **Step 2:** Round 2 (Operational Attack) — Critic identifies prerequisite gaps and temporal infeasibility.
* **Step 3:** Round 3 (Normative Review) — Ethics-Reviewer audits credential pricing and burnout risks.
* **Step 4:** Round 4 (Rebuttal & Adaptation) — Planner concedes unviable steps or refutes using verified evidence.
* **Step 5:** Convergence (Arbiter Synthesis) — Arbiter maps the dispute graph, computes uncertainty $U(\mathcal{R}^*)$, and triggers override gates.
* **Speaker Notes:** Walk the audience through the turn-by-turn state transitions in the LangGraph harness.

---

### Slide 6: Hybrid GraphRAG Grounding
* **Neo4j Career Knowledge Graph:** Formal O*NET/ESCO ontology, deterministic prerequisite DAG constraints, and weighted role-competency edges.
* **Chroma / FAISS Vector Store:** Unstructured syllabi from accredited universities, real-time job listings, and BLS wage tables with attribution score $> 0.85$.
* **Speaker Notes:** Emphasize that vector retrieval alone fails at structural reasoning; combining graph traversal with dense embeddings guarantees factual rigor.

---

### Slide 7: Calibrated Uncertainty & Meaningful Human Override
* **Epistemic Uncertainty $U(\mathcal{R}^*)$:** Weighted combination of Persona Position Entropy $H(\mathbf{\Pi})$, Graph Distance Sparsity, and Grounding Attribution Density.
* **Human Override Gate (Cognitive Forcing):** Triggers when uncertainty exceeds threshold or fundamental trade-offs remain unresolved; halts autonomous execution to force deliberate human arbitration.
* **Speaker Notes:** Demonstrate how this directly mitigates automation bias by transforming the user from a passive recipient into an active decision-maker.

---

### Slide 8: Evaluation Methodology & Metrics
* **Evidence Diversity ($ED$):** Shannon entropy across multi-source categories ($ED > 1.85$ bits).
* **Contradiction-Resolution Rate ($CRR$):** Proportion of Critic challenges resolved or conceded ($CRR \ge 85\%$).
* **Unsupported-Claim Rate ($UCR$):** Factual assertions lacking grounding citations ($UCR < 5.0\%$).
* **Counterfactual Parity ($\Delta_{parity}$):** Recommendation divergence across 500+ synthetic profile pairs ($\Delta_{parity} \le 0.05$).
* **Expected Calibration Error ($ECE$):** Reliability calibration of risk predictions ($ECE < 0.08$).
* **Expert & User Rubric:** Double-blind evaluation by certified counselors (Target $\ge 4.5 / 5.0$).
* **Speaker Notes:** Outline the concrete, reproducible evaluation metrics across computational and human tiers.

---

### Slide 9: Ablation Study: 4-Way Comparative Architecture
* **Baseline 1 (Vanilla Qwen):** High sycophancy, hallucinatory roadmaps, zero calibrated uncertainty.
* **Baseline 2 (Single-Agent RAG):** Improved facts, but suffers from monolithic confirmation bias.
* **Ablation (Dyadic Debate):** Operational scrutiny, but blind to socio-economic and ethical concerns.
* **Full Dialectic System:** Balanced trade-offs, highest CRR, lowest UCR, verified demographic fairness.
* **Speaker Notes:** Highlight the ablation results showing each component's distinct causal contribution.

---

### Slide 10: Prototype Implementation: Streamlit Debate Trace Viewer
* **Front-End Experience:** Side-by-side round arguments, interactive dispute tree visualizer, calibrated risk gauges, one-click override & constraint injection panel.
* **Local Infrastructure:** 100% on-premise execution via local Qwen (Ollama/vLLM) ensuring data privacy, coupled with Neo4j Community Edition and FAISS.
* **Speaker Notes:** Showcase the user interface designed around transparency, inspectability, and candidate privacy.

---

### Slide 11: Conclusion & Academic Significance
* **Summary of Contributions:**
  1. Eliminates single-agent sycophancy through multi-persona debate.
  2. Grounds planning via hybrid GraphRAG (Neo4j + Vector).
  3. Replaces false certainty with calibrated epistemic scoring and explicit dispute graphs.
  4. Protects human agency through cognitive forcing functions and override gates.
  5. Enforces demographic fairness across synthetic profile audits.
