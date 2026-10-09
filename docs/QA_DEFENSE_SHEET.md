# Presentation Defense & Q&A Preparation Sheet
## Debate-Based Career Guidance Agent with Complementary Personas

This document provides rigorous technical justifications and talking points for anticipated questions from thesis committees, academic reviewers, and conference audiences.

---

### 1. Honest Status: Pre-Implementation Proposal vs. Empirical Results
**Question:** *Are the reported numbers measured experimental results or hypothesized targets? What is currently built versus planned?*
* **Response:**
  1. **Explicit Pre-Implementation Status:** This work is a **formal system architecture and empirical evaluation proposal**. All metric values ($PCR \ge 80\%$, $S\text{-}CRR \ge 80\%$, $UCR < 5\%$) are hypothesized performance targets and benchmarks, not claimed completed outcomes.
  2. **Running Status Disclosure:** Every slide in our deck and documentation carries the explicit footer: `STATUS: Planned Design & Empirical Evaluation Protocol (Pre-Implementation Research Proposal)`.
  3. **Deliverables Roadmap:** We present an 8-stage execution roadmap progressing from local infrastructure setup to a 100-pair pilot benchmark (9.4 GPU hours) and a double-blind counselor study.

---

### 2. Core Baseline: Multi-Agent Debate vs. Single-Agent Multi-Perspective Prompting
**Question:** *Why use a multi-agent system when a single LLM could simply be prompted: "Analyze this candidate from three opposing perspectives—Corporate, Startup, and Deep-Tech—and surface the trade-offs"?*
* **Response:**
  1. **Controlled Isolation via Baseline C:** We have explicitly integrated **Baseline C (Single-Agent Multi-Perspective Prompting)** into our 6-config ablation ladder to directly test this hypothesis.
  2. **Context Window Homogenization:** Single-agent models prompted with multiple perspectives suffer from internal coherence collapse: the autoregressive attention mechanism rapidly converges on a middle ground, muting authentic dialectic tension.
  3. **Asymmetric Knowledge Access & Decoding:** Multi-agent architectures allow distinct system prompt contracts, isolated conversation states, and different decoding temperatures ($T=0.3$ for Traditionalist vs. $T=0.7$ for Builder), preventing early consensus.
  4. **Empirical Benchmark:** Comparing Baseline C against our Proposed System will quantify the exact margin of performance attributable to multi-agent dialectics versus multi-perspective chain-of-thought.

---

### 3. Base Model Diversity & Defense of Scripted Foils
**Question:** *All three personas run on the same base model (Qwen-2.5-14B). Aren't you simply scripting role-play and hard-coding opinions (e.g. LeetCode vs. 5NF)? How is that Responsible AI?*
* **Response:**
  1. **Epistemic Foils, Not Dogma:** The personas are engineered as *epistemic foils* designed to surface latent, structural trade-offs that single-agent assistants obscure.
  2. **Moderator Neutrality:** The Moderator prompt strictly forbids adopting any single persona's worldview; it facilitates structured cross-examination and extracts an objective Dispute Tree $\mathcal{T}_{\text{dispute}}$.
  3. **Temperature & Parameter Differentiation:**
     * *Deep-Tech Specialist:* $T = 0.4$, top-$p = 0.85$ (systems rigor, formal database normalization).
     * *Pragmatic Traditionalist:* $T = 0.3$, top-$p = 0.80$ (conservative, algorithmic depth).
     * *Entrepreneurial Builder:* $T = 0.7$, top-$p = 0.95$ (divergent, product-oriented).
  4. **Local Privacy Invariant:** Qwen-2.5-14B executes 100% on-premise on consumer workstation hardware, preventing candidate profile exfiltration. Future iterations will test heterogeneous model pools (Mistral + Llama-3.1 + Qwen) to remove shared base priors.

---

### 4. Derivation of the Knowledge Graph Prerequisite DAG
**Question:** *Neither O\*NET nor ESCO contains skill-to-skill prerequisite edges. Bloom's taxonomy orders cognitive levels, not topical dependencies. How is your prerequisite DAG constructed and validated?*
* **Response:**
  1. **ACM/IEEE CS2023 Grounding:** Rather than relying purely on Bloom's taxonomy, we synthesize prerequisite edges by projecting the official **ACM/IEEE CS2023 Curricular Guidelines** (Knowledge Areas: CS-DS, CS-AL, CS-OS, CS-SE) onto O\*NET 29.2 and ESCO competency nodes.
  2. **Formal Prerequisite Edges:** An edge $(s_A \to s_B)$ represents an explicit institutional catalog prerequisite (e.g. `Discrete Mathematics` $\to$ `Data Structures & Algorithms` $\to$ `Operating Systems Internals` $\to$ `Distributed Systems`).
  3. **Scale & Faculty Validation:** The prototype graph comprises **420 CSE skill nodes** and **890 directed prerequisite edges**, reviewed and validated by two academic Computer Science faculty members.
  4. **Deterministic Cypher Traversals:** Reachability is evaluated via deterministic graph queries, completely eliminating LLM hallucinations regarding prerequisite sequencing.

---

### 5. Verification Beyond Cosine Similarity (NLI & Salary Checkers)
**Question:** *Why is cosine similarity insufficient for factual grounding, and how does NLI Cross-Encoder Entailment work?*
* **Response:**
  1. **Semantic Similarity vs. Factual Entailment:** Cosine similarity measures topical closeness, not factual entailment. A statement claiming "Junior salaries average $250k" has high cosine similarity to "Junior salaries average $85k".
  2. **Cross-Encoder NLI Threshold ($P > 0.80$):** We evaluate milestone claims using DeBERTa-v3-large Cross-Encoder NLI:
     $$P(\text{Entailment} \mid \text{Retrieved Syllabi / BLS Premise}) > 0.80$$
     This threshold is standard literature operating practice for high-precision factual verification.
  3. **Deterministic Numerical Checkers:** Salary and timeline claims are checked against official quarterly BLS wage distributions (p25–p75), strictly rejecting hallucinated compensation.

---

### 6. Rationale & Tuning for Uncertainty Weights ($w_1, w_2, w_3$) and Thresholds
**Question:** *Where do the weights $w_1=0.40, w_2=0.35, w_3=0.25$ and the threshold $\theta_{\text{unc}}=0.65$ come from?*
* **Response:**
  1. **Normalized Formulation:** $\hat{U}(\mathcal{R}^*) = w_1 \cdot \hat{H}(\mathbf{\Pi}) + w_2 \cdot \hat{D}(G, P) + w_3 \cdot (1 - \text{NLI}_{\text{entail}})$ where all components are normalized to $[0, 1]$ and $\sum w_i = 1.0$.
  2. **Initial Heuristic Priority:** Debate friction is given the highest weight ($0.40$) as the primary signal of genuine philosophical contention, followed by graph hop distance ($0.35$) and NLI deficit ($0.25$).
  3. **Formal Tuning Protocol:** These weights are labeled as *initial operating baselines*. In Phase 4, they will be fitted via cross-validated ridge logistic regression against a validation set of 50 counselor-annotated career risk scenarios.
  4. **Trigger Threshold ($\theta_{\text{unc}} = 0.65$):** Selected to target an expected $\sim 35\text{--}40\%$ override rate on high-stakes career pivot queries, preventing both blind automation compliance and modal fatigue.

---

### 7. Equivalence Testing (TOST) vs. Standard Null Hypothesis Testing
**Question:** *Why use Two One-Sided Tests (TOST) instead of standard t-tests for salary fairness?*
* **Response:**
  1. **The Fallacy of $p > 0.05$:** A non-significant standard t-test ($p > 0.05$) only indicates an absence of evidence, not evidence of absence of discrimination.
  2. **Equivalence Bounds:** We define an equivalence margin $\delta = \pm \$2,500$ (representing $< 3\%$ of starting software engineering salaries). TOST tests whether the observed difference is statistically confined within this equivalence band.
  3. **Clustered Standard Errors:** Because each counterfactual profile pair undergoes $N = 5$ repeated sampling runs, standard errors are clustered by profile pair to prevent inflated degrees of freedom.

---

### 8. Feasibility & Compute Budget Protocol
**Question:** *Evaluating 500 profile pairs across 5 runs and 6 configurations requires 30,000 debates. Is this computationally feasible? How are counselors recruited?*
* **Response:**
  1. **Phase 1 Pilot Feasibility (9.4 GPU Hours):**
     * 100 counterfactual pairs (200 profiles) $\times$ $N = 3$ repeated runs across 4 primary configurations = **2,400 debate runs**.
     * Local Qwen-2.5-14B (4-bit AWQ via vLLM) generates $\sim 85$ tok/s. A 2-round debate ($\sim 1,200$ tokens) takes $\sim 14.1$ seconds.
     * $2,400 \times 14.1\text{s} \approx 33,840\text{s} \approx \mathbf{9.4\text{ GPU hours}}$ on a single RTX 4090 workstation overnight.
  2. **Phase 2 Full Scale:** 500 pairs $\times$ $N=5$ runs distributed across two workstations over a weekend ($\sim 48$ GPU hours).
  3. **Counselor Study Protocol:** Three certified university career counselors evaluate a double-blind, stratified sample of **60 randomized roadmaps** (10 from each ablation tier). At 7 minutes per roadmap, this requires only **2.3 hours per counselor**, making recruitment highly feasible.
