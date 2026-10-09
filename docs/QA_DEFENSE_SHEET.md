# Presentation Defense & Q&A Preparation Sheet
## Debate-Based Career Guidance Agent with Complementary Personas

This document provides technical justifications and talking points for anticipated questions from thesis committees, academic reviewers, and conference audiences.

---

### 1. Base Model Diversity & Persona Collapse
**Question:** *All three advising personas run on the same base model (Qwen-2.5-14B-Instruct). How do you ensure genuine diversity of thought rather than superficial stylistic variations?*
* **Response:**
  1. **Conflicting Optimization Directives:** Personas are assigned antagonistic objective functions via prompt contracts (Pragmatist penalizes volatility; Builder penalizes corporate bureaucracy; Specialist penalizes architectural shortcuts).
  2. **Temperature & Decoding Differentiation:** We configure distinct sampling parameters:
     * *Deep-Tech Specialist:* $T = 0.2$, top-$p = 0.8$ (deterministic, mathematically rigorous).
     * *Pragmatic Traditionalist:* $T = 0.4$, top-$p = 0.85$ (grounded, conservative).
     * *Entrepreneurial Builder:* $T = 0.7$, top-$p = 0.95$ (exploratory, divergent).
  3. **Adversarial Friction:** The Moderator does not allow passive agreement; it actively extracts contradictions from opening claims and forces agents to defend their philosophies against one another.
  4. **Hardware & Privacy Justification:** Qwen-2.5-14B was selected because it runs completely on-premise on consumer lab hardware (single RTX 4090 / 24GB VRAM in 4-bit AWQ or dual RTX 3090s via vLLM), guaranteeing zero candidate data exfiltration.

---

### 2. Derivation of the Knowledge Graph Prerequisite DAG
**Question:** *O\*NET and ESCO do not contain skill-to-skill prerequisite edges. How is your prerequisite DAG constructed?*
* **Response:**
  1. **Taxonomy Grounding:** O\*NET 29.2 and ESCO v1.2 establish formal nodes for occupations, work activities, and skills, along with importance/level ratings.
  2. **Curricular Projection:** We synthesize directed prerequisite edges ($s_i \to s_j$) by mapping accredited Computer Science curricula (ACM/IEEE-CS Curricula Guidelines) and Bloom’s Taxonomy cognitive progressions onto the taxonomy skill nodes.
  3. **Deterministic Cypher Verification:** Prerequisite compliance is verified deterministically in Neo4j via shortest-path traversal rather than relying on probabilistic LLM generation.

---

### 3. Verification Beyond Cosine Similarity
**Question:** *Why is cosine similarity insufficient for factual grounding, and how does NLI Cross-Encoder Entailment work?*
* **Response:**
  1. **Semantic Similarity vs. Factual Entailment:** Cosine similarity measures topical closeness, not factual truth. A claim stating "Salaries drop by 50%" has high cosine similarity to "Salaries increase by 50%".
  2. **NLI Cross-Encoder Validation:** We evaluate factual claims using a cross-encoder model:
     $$P(\text{Entailment} \mid \text{Retrieved Evidence Premise}) \ge 0.80$$
  3. **Numerical Guardrails:** Because cross-encoders can struggle with numerical bounds, salary and time commitments are validated using deterministic range checks against official BLS Occupational Employment Statistics.

---

### 4. Calibration & Tuning of the Uncertainty Indicator ($U_{\text{hat}}$)
**Question:** *How are the weights and threshold for $U_{\text{hat}}$ determined, and how is it validated?*
* **Response:**
  1. **Formulation:** $U_{\text{hat}}(\mathcal{R}^*) = w_1 \cdot \hat{H}(\mathbf{\Pi}) + w_2 \cdot \hat{D}(G, P) + w_3 \cdot (1 - \text{NLI}_{\text{entail}})$ with normalized components $\in [0, 1]$.
  2. **Weight Optimization:** Weights ($w_1 = 0.40, w_2 = 0.35, w_3 = 0.25$) were established via logistic regression on a held-out validation set of 50 counselor-annotated career pivot scenarios.
  3. **Empirical Validation:** Rather than claiming formal statistical calibration without ground truth, $U_{\text{hat}}$ is validated as a risk discriminator against expert counselor risk ratings, targeting an $AUC \ge 0.82$.

---

### 5. Equivalence Testing (TOST) vs. Null Hypothesis Testing
**Question:** *Why use Two One-Sided Tests (TOST) instead of standard t-tests for salary fairness?*
* **Response:**
  1. **The Fallacy of $p > 0.05$:** A non-significant standard t-test ($p > 0.05$) only indicates an absence of evidence, not evidence of absence of discrimination.
  2. **Equivalence Bounds:** We define an equivalence margin $\delta = \pm \$2,500$ (representing $< 3\%$ of starting software engineering salaries). TOST tests whether the observed difference is statistically confined within this equivalence band.
  3. **Clustered Standard Errors:** Because each counterfactual profile pair undergoes $N = 5$ repeated sampling runs, standard errors are clustered by profile pair to prevent inflated degrees of freedom.

---

### 6. Cognitive Forcing & Override Gate Trigger Rate
**Question:** *If the system intentionally creates debate friction, won't the override gate trigger 100% of the time?*
* **Response:**
  1. **Dispute Filtering:** The gate does not fire for minor pedagogical disagreements. It triggers only when $\hat{U}(\mathcal{R}^*) > \theta_{\text{unc}}$ ($0.65$) or when unresolved disputes in $K_{\text{unresolved}}$ represent *critical/irreversible* commitments (e.g. accumulating tuition debt or abandoning accredited degree progress).
  2. **Healthy Trigger Distribution:** The expected trigger rate is calibrated to $\sim 35\text{--}40\%$ on high-pivot profiles, ensuring that the gate provides meaningful friction without causing alert fatigue.
