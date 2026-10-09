# Audited Presentation Slide Deck: Debate-Based Career Guidance Agent

**Definitive Presentation File:**
* [`Final_Presentation.pptx`](file:///home/thor/Desktop/RAI%20Project/Final_Presentation.pptx)
* **Design Generator Script:** [`generate_deck.py`](file:///home/thor/Desktop/RAI%20Project/generate_deck.py)
* **Q&A Defense Sheet:** [`docs/QA_DEFENSE_SHEET.md`](file:///home/thor/Desktop/RAI%20Project/docs/QA_DEFENSE_SHEET.md)
* **Full Specification:** [`docs/PROJECT_SPECIFICATION.md`](file:///home/thor/Desktop/RAI%20Project/docs/PROJECT_SPECIFICATION.md)

---

### Audited Slide Deck Architecture: 17 Academic Slides

| Slide # | Section Title | Visual Architecture & Methodological Grounding |
| :---: | :--- | :--- |
| **01** | **Title Slide** | Executive Dark Navy background, project metadata, explicit scope to Computer Science & Software Engineering careers. |
| **02** | **Executive Summary & Scope** | Explicitly defines CSE Core scope, contrasts monolithic status quo with multi-agent debate, introduces offline privacy model. |
| **03** | **Literature Survey** | 4-column structured matrix citing canonical papers: Du et al. (ICML '24), Liang et al. (EMNLP '23), Sharma et al. (ICLR '24), Geyik et al. (ACM KDD '19), Xiong et al. (ICLR '24), Buçinca et al. (CSCW '21), Edge et al. (Microsoft '24). Respectful gap statements. |
| **04** | **Problem Definition (High-Level)** | The Sycophancy Trap (Sharma et al.), the Illusion of False Certainty (Kadavath et al.), and Equity/Agency Failures (Geyik et al., Cummings). |
| **05** | **Problem Definition (Low-Level)** | Formal mathematical tuple $\mathcal{M} = \langle \mathcal{P}, \mathcal{G}, \mathcal{D}_{rag}, \mathbf{\Pi}, \mathcal{T}_{debate}, \Phi \rangle$. Protected attributes $a_{demo}$ explicitly excluded from generation profile $P$ and isolated into audit sandbox. Qualitative prompt directives clarified. |
| **06** | **Flowchart 1: System Architecture** | **Native Visual Diagram with Connector Arrows:** Intake $\to$ Hybrid Knowledge Base (Neo4j DAG + Offline FAISS) $\to$ LangGraph Multi-Agent Harness $\to$ 3 Personas $\to$ Moderator $\to$ **Decision Diamond with Labeled [YES: Override] and [NO: Pass] Branches** $\to$ Streamlit UI. |
| **07** | **The 3 Career Philosophy Personas** | **The Pragmatic Traditionalist** (Corporate, DSA, LeetCode, Conservative) · **The Entrepreneurial Builder** (Startup SaaS, AI Agents, Disruptive) · **The Deep-Tech Specialist** (Linux, 5NF DBs, Systems Rigor). Explains temperature and prompt differentiation against shared base model priors. |
| **08** | **The Moderator Agent** | Synthesizer & Strategist: Neutral facilitator directive, friction point injection, dispute tree extraction, and hybrid roadmap synthesis across $T_{debate} = 2$ rounds. |
| **09** | **Flowchart 2: The 5-Stage Debate Loop** | **Rigid Execution Loop Diagram:** Context Intake $\to$ Opening Statements (Parallel 150w) $\to$ Cross-Exam Friction $\to$ Rebuttals $\to$ Hybrid Synthesis. |
| **10** | **Hybrid Grounding (Derived GraphRAG)** | Explicitly clarifies that **skill prerequisite DAG is derived/synthesized** (projecting CS curricula & Bloom's taxonomy onto O\*NET 29.2 / ESCO v1.2 nodes). Ingests **offline snapshot corpus** (zero live web leaks). Replaces cosine similarity with **NLI Cross-Encoder Entailment** ($P > 0.80$) and BLS numerical bounds. |
| **11** | **Responsible AI: Uncertainty Indicator** | Composite Epistemic Uncertainty Indicator $\hat{U}(\mathcal{R}^*) = w_1 \cdot \hat{H}(\mathbf{\Pi}) + w_2 \cdot \hat{D}(G, P) + w_3 \cdot (1 - \text{NLI}_{entail})$ with tuned normalized weights ($w_1=0.40, w_2=0.35, w_3=0.25$). Cognitive forcing gate filtered by CriticalDispute to ensure $\sim 35\text{--}40\%$ override rate. |
| **12** | **Counterfactual Fairness Auditing** | 500+ synthetic profile pairs with **$N = 5$ repeated sampling runs** with clustered SEs. Targets: $\Delta_{parity} \le 0.05$, **TOST salary equivalence** bound $\delta = \pm \$2,500$ ($p < 0.05$), and Cross-SES ECRR parity $|\Delta_{ECRR}| \le 0.15$ with absolute cap $\le 0.30$. |
| **13** | **How to Measure Outcome** | Grounded, unconfounded target metrics: **Premise-Challenge Rate (PCR $\ge 80\%$)** to measure sycophancy reduction, **Substantiated CRR (S-CRR $\ge 80\%$)** to prevent ungrounded concessions, Unsupported-Claim Rate (UCR $< 5\%$), Counselor Risk AUC-ROC ($\ge 0.82$), Counselor Rubric ($\ge 4.0 / 5.0$ with Kendall's $W \ge 0.70$). |
| **14** | **Flowchart 3: Evaluation Pipeline** | **End-to-End Validation Pipeline:** Synthetic Profile Generator $\to$ Automated Debate Harness $\to$ Automated Metric Audit (NLI + Citation Verifiers) $\to$ Counselor Double-Blind Review & Scorecard. |
| **15** | **Unconfounded Ablation Matrix** | **Explicitly labeled as Hypothesized / Target Outcome Matrix.** Disentangles 6 controlled configurations: 1. Vanilla Baseline $\to$ 2. Compute-Matched Self-Consistency $\to$ 3. GraphRAG Single-Agent $\to$ 4. Dyadic Debate $\to$ 5. Unmoderated Triad $\to$ 6. Full Proposed System. |
| **16** | **Limitations, Risks & Strategic Roadmap** | Fulfills Responsible AI requirements: details base model dependency (Qwen-2.5-14B), synthetic profile limitations, cognitive friction burden, and outlines 4-phase research roadmap through longitudinal pilot. |
| **17** | **Academic Bibliography** | Complete formal bibliographic citations for all peer-reviewed works referenced in the deck (Du et al., Liang et al., Sharma et al., Geyik et al., Xiong et al., Buçinca et al., Edge et al., Kadavath et al., Cummings). |

---

### Speaker Notes Standards
- **Pure Presenter Talking Points**: Every slide contains comprehensive speaker notes phrased naturally for academic presentation.
- **Zero Meta-Audit Commentary**: All meta-audit language has been completely eliminated from notes; technical defense points are housed in [`docs/QA_DEFENSE_SHEET.md`](file:///home/thor/Desktop/RAI%20Project/docs/QA_DEFENSE_SHEET.md).
