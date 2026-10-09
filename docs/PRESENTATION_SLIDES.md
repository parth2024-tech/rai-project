# Audited Presentation Slide Deck: Debate-Based Career Guidance Agent

**Primary Presentation File:**
* [`Final_Presentation.pptx`](file:///home/thor/Desktop/RAI%20Project/Final_Presentation.pptx)
* **Design Generator Script:** [`generate_deck.py`](file:///home/thor/Desktop/RAI%20Project/generate_deck.py)

---

### Audit-Compliant Slide Deck Architecture: 16 Academic Slides

| Slide # | Section Title | Audit Fixes & Methodological Grounding |
| :---: | :--- | :--- |
| **01** | **Title Slide** | Executive Dark Navy title slide, project metadata, explicit scope to Computer Science & Software Engineering careers. |
| **02** | **Executive Summary & Scope** | Explicitly defines CSE Core scope, contrasts monolithic status quo with multi-agent debate, introduces offline privacy model. |
| **03** | **Literature Survey** | 4-column matrix citing 7 papers: Du et al. (ICML '24), Liang et al. (EMNLP '23), Sharma et al. (ICLR '24), **Chen et al. (ACM FAccT '23)** on recommender fairness, Xiong et al. (ICLR '24), Buçinca et al. (CSCW '21), Edge et al. (Microsoft '24). Respectful gap statements. |
| **04** | **Problem Definition (High-Level)** | The Sycophancy Trap (Sharma et al.), the Illusion of False Certainty (Kadavath et al.), and Equity/Agency Failures (Chen et al.). |
| **05** | **Problem Definition (Low-Level)** | Formal mathematical tuple $\mathcal{M} = \langle \mathcal{P}, \mathcal{G}, \mathcal{D}_{rag}, \mathbf{\Pi}, \mathcal{T}_{debate}, \Phi \rangle$. Protected attributes $a_{demo}$ explicitly excluded from generation profile $P$ and isolated into audit sandbox. Qualitative prompt directives clarified. |
| **06** | **Flowchart 1: System Architecture** | **Native Visual Diagram with Connector Arrows:** Intake $\to$ Hybrid Knowledge Base (Neo4j DAG + Offline FAISS) $\to$ LangGraph Multi-Agent Harness $\to$ 3 Personas $\to$ Moderator $\to$ **Decision Diamond with Labeled [YES: Override] and [NO: Pass] Branches** $\to$ Streamlit UI. |
| **07** | **The 3 Career Philosophy Personas** | **The Pragmatic Traditionalist** (Corporate, DSA, LeetCode, Conservative) · **The Entrepreneurial Builder** (Startup SaaS, AI Agents, Disruptive) · **The Deep-Tech Specialist** (Linux, 5NF DBs, Systems Rigor). Explains temperature and prompt differentiation against shared base model priors. |
| **08** | **The Moderator Agent** | Synthesizer & Strategist: Neutral facilitator directive, friction point injection, dispute tree extraction, and hybrid roadmap synthesis. |
| **09** | **Flowchart 2: The 5-Stage Debate Loop** | **Rigid Execution Loop Diagram:** Context Intake $\to$ Opening Statements (Parallel 150w) $\to$ Cross-Exam Friction $\to$ Rebuttals $\to$ Hybrid Synthesis across $T_{debate} = 2$ rounds. |
| **10** | **Hybrid Grounding (Derived GraphRAG)** | Explicitly clarifies that **skill prerequisite DAG is derived/synthesized** (projecting CS curricula & Bloom's taxonomy onto O\*NET 29.2 / ESCO v1.2 nodes). Ingests **offline snapshot corpus** (zero live web leaks). Replaces cosine similarity with **NLI Cross-Encoder Entailment** ($P > 0.80$). |
| **11** | **Responsible AI: Uncertainty Indicator** | Composite Epistemic Uncertainty Indicator $\hat{U}(\mathcal{R}^*) = w_1 \cdot \hat{H}(\mathbf{\Pi}) + w_2 \cdot \hat{D}(G, P) + w_3 \cdot (1 - \text{NLI}_{entail})$ with normalized weights. Rigorously defines $K_{unresolved}$, $Risk$, and threshold triggers. |
| **12** | **Counterfactual Fairness Auditing** | 500+ synthetic profile pairs with **$N = 5$ repeated sampling runs** to decouple demographic effects from stochastic decoding noise. Targets: $\Delta_{parity} \le 0.05$, $|\Delta_{prestige}| < \$2,500$ (t-test $p > 0.05$), and defines ECRR (Exploitative Credential Recommendation Ratio). |
| **13** | **How to Measure Outcome** | Grounded, realistic targets: Evidence Diversity $ED > 1.40$ bits ($> 70\%$ max entropy across 4 sources), Contradiction-Resolution Rate (CRR $\ge 85\%$), Unsupported-Claim Rate (UCR $< 5\%$), Counselor Rubric ($\ge 4.0 / 5.0$ with Kendall's $W \ge 0.70$). |
| **14** | **Flowchart 3: Evaluation Pipeline** | **End-to-End Validation Pipeline:** Synthetic Profile Generator $\to$ Automated Debate Harness $\to$ Automated Metric Audit (NLI + Citation Verifiers) $\to$ Counselor Double-Blind Review & Scorecard. |
| **15** | **Unconfounded Ablation Matrix** | **Explicitly labeled as Hypothesized / Target Outcome Matrix.** Disentangles 6 controlled configurations: 1. Vanilla Baseline $\to$ 2. Vector RAG $\to$ 3. GraphRAG $\to$ 4. Dyadic Debate $\to$ 5. Unmoderated Triad $\to$ 6. Full Proposed System. |
| **16** | **Limitations, Risks & Strategic Conclusion** | Fulfills Responsible AI requirements: details base model dependency (Qwen-2.5-14B), derived DAG maintenance, user cognitive friction burden, and confirms 100% on-premise privacy via offline snapshots. |

All slides include updated, comprehensive presentation speaker notes addressing defensive questions and methodological rationale.
