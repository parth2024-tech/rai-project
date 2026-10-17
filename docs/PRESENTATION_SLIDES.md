# Audited Presentation Slide Deck: Debate-Based Career Guidance Agent

**Definitive Presentation File:**
* [`Final_Presentation.pptx`](file:///home/thor/Desktop/RAI%20Project/Final_Presentation.pptx)
* **Design Generator Script:** [`generate_deck.py`](file:///home/thor/Desktop/RAI%20Project/generate_deck.py)
* **Q&A Defense Sheet:** [`docs/QA_DEFENSE_SHEET.md`](file:///home/thor/Desktop/RAI%20Project/docs/QA_DEFENSE_SHEET.md)
* **Full Specification:** [`docs/PROJECT_SPECIFICATION.md`](file:///home/thor/Desktop/RAI%20Project/docs/PROJECT_SPECIFICATION.md)

---

### Audited Slide Deck Architecture: 18 Academic Slides

| Slide # | Section Title | Visual Architecture & Methodological Grounding |
| :---: | :--- | :--- |
| **01** | **Title Slide** | Executive Dark Navy title slide, project metadata, explicit scope to Computer Science & Software Engineering careers. **Status Banner:** `STATUS: PRE-IMPLEMENTATION RESEARCH PROPOSAL`. |
| **02** | **Problem Statement & Research Gap** | Hedged gap analysis: The Sycophancy Trap (Sharma et al.), the Illusion of False Certainty (Kadavath et al.), and Latent Demographic Steering (Geyik et al.). Hedged gap across reviewed career tools. Subtitle takeaway line. |
| **03** | **Literature Survey** | 4-column structured matrix citing canonical papers with verified DOIs: Du et al. (ICML '24), Liang et al. (EMNLP '23), Sharma et al. (ICLR '24), Geyik et al. (ACM KDD '19), Buçinca et al. (CSCW '21), Edge et al. (Microsoft '24). Attribution note. |
| **04** | **Comparative Feature Matrix** | Full capability comparison table benchmarking [1]–[6] against the Proposed System across 6 technical dimensions (Debate, Prerequisite DAG, Uncertainty, Forcing Gate, Fairness Audit, Local Privacy). |
| **05** | **Limitations of Paper & Evaluation** | **Dedicated Technical Disclosures Slide (Inserted after Slide 4):** 1. Architectural Limitations (Shared base priors, Coarse archetypes, Scope boundaries, Graph decay) · 2. Evaluation Limitations (Synthetic cohorts, Benchmark extremity, Decision fatigue, Counselor sample size, Heuristic weights) · 3. Summary Mitigation Matrix. |
| **06** | **System Architecture & Pipeline** | Native visual diagram with connector arrows: Intake $\to$ Hybrid Grounding $\to$ LangGraph Local Harness $\to$ Dialectic Triad Engine $\to$ Moderator $\to$ **Divergent Decision Branches ([YES: Veto Required] / [NO: Roadmap])**. |
| **07** | **Low-Level Design & Modules** | 8 planned Python modules (`intake_service.py`, `persona_engine.py`, `moderator_synthesizer.py`, etc.) + formal schemas for Neo4j Curricular DAG, Chroma/FAISS metadata, and LangGraph deliberation state. |
| **08** | **Persona Design & Epistemic Foils** | Three antagonistic career philosophies: Traditionalist ($T=0.3$), Builder ($T=0.7$), Specialist ($T=0.4$). Explicit defense of personas as epistemic foils to surface latent trade-offs, preventing single-model dogmatism. |
| **09** | **Knowledge Grounding & DAG Derivation** | Rigorous curricular derivation: projecting ACM/IEEE CS2023 Guidelines onto O\*NET/ESCO nodes (420 nodes, 890 edges, faculty-validated). Offline BLS/syllabi snapshots; DeBERTa-v3 Cross-Encoder NLI ($P > 0.80$) and BLS salary range checkers. |
| **10** | **Worked Walkthrough: Profile to Veto** | Concrete case study ("Priya", 3rd-year CSE, considering a $15k bootcamp to become Staff ML); side-by-side agent debate quotes; visual Dispute Tree $\mathcal{T}_{\text{dispute}}$; uncertainty calculation ($\hat{U}=0.74 > 0.65$); cognitive forcing trigger branch requiring human arbitration. |
| **11** | **Responsible AI: Uncertainty Indicator** | Composite Epistemic Uncertainty Indicator $\hat{U}(\mathcal{R}^*) = w_1 \cdot \hat{H}(\mathbf{\Pi}) + w_2 \cdot \hat{D}(G, P) + w_3 \cdot (1 - \text{NLI}_{entail})$. Parameter rationale for initial weights ($0.40/0.35/0.25$) and threshold $\theta_{\text{unc}}=0.65$ ($\sim 35\text{--}40\%$ override rate). |
| **12** | **Counterfactual Fairness Auditing** | 500+ synthetic profile pairs with **$N = 5$ repeated sampling runs** and clustered SEs. Targets: $\Delta_{parity} \le 0.05$, **TOST salary equivalence** bound $\delta = \pm \$2,500$ ($p < 0.05$), and Cross-SES ECRR parity $|\Delta_{ECRR}| \le 0.15$ with absolute cap $\le 0.30$. |
| **13** | **Outcome Measurement: 7 Metrics** | Exact mathematical definitions, directions, numerators, denominators, and target thresholds: PCR $\ge 80\%$, S-CRR $\ge 80\%$, UCR $< 5\%$, Counterfactual Parity $\Delta_p \le 0.05$, TOST $p < 0.05$, Counselor Risk AUC $\ge 0.82$, Counselor Likert $\ge 4.0/5.0$. Interpretation guardrails. |
| **14** | **Experimental Baseline Ladder** | Controlled 6-tier ablation ladder isolating every mechanism: Baseline A (Vanilla Single-Agent) $\to$ Baseline B (Compute-Matched Self-Consistency) $\to$ **Baseline C (Single-Agent Multi-Perspective Prompting)** $\to$ Baseline D (GraphRAG Single-Agent) $\to$ Baseline E (Unmoderated Triad) $\to$ Proposed Full System. |
| **15** | **Feasibility & Compute Budget** | Explicit GPU inference budget: local RTX 4090 / A100 (vLLM 4-bit AWQ 14B at 85 tok/s, 2,400 runs in **9.4 GPU hours** for Phase 1 pilot). Counselor study protocol (3 certified counselors, 60 double-blind roadmaps, 2.3 hours each). |
| **16** | **Responsible AI Governance & Ethics** | Preserving Student Critical Agency, Mitigating Credential Exploitation, Cognitive Forcing as a Pedagogical Safeguard, and Counselor-in-the-Loop Collaboration. |
| **17** | **Phased Research Roadmap** | 6-phase engineering and empirical evaluation roadmap; immediate 14-day next steps (Neo4j stack $\to$ 420-node DAG import $\to$ Baseline C authoring $\to$ adversarial dataset); explicit feedback requests for committee reviewers. |
| **18** | **Academic Bibliography** | Complete formal bibliographic citations for all peer-reviewed works referenced in the deck with verified DOIs (Du et al., Liang et al., Sharma et al., Geyik et al., Buçinca et al., Xiong et al., Edge et al., Kadavath et al., Cummings). |

---

### Quality & Presentation Invariants
- **Running Status Footer**: Present on every slide (`STATUS: Planned Design & Empirical Evaluation Protocol (Pre-Implementation Research Proposal)`).
- **Subtitle Takeaway Line**: Every slide carries a concise, italicized one-sentence takeaway line beneath its title.
- **Pure Presenter Talking Points**: Every slide contains comprehensive speaker notes phrased naturally for academic presentation, with zero meta-audit jargon.
- **Snug Visual Geometry**: Compact, well-proportioned cards with 11–12pt body text, sharp header tags, and native flowchart connectors.
