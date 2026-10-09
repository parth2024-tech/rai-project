# Presentation Slide Deck: Debate-Based Career Guidance Agent

**Primary Presentation File:**
* [`Final_Presentation.pptx`](file:///home/thor/Desktop/RAI%20Project/Final_Presentation.pptx)
* **Design Generator Script:** [`generate_deck.py`](file:///home/thor/Desktop/RAI%20Project/generate_deck.py)

---

### Slide Deck Architecture: 15 High-Signal Human-Crafted Slides

| Slide # | Section Title | Content, Flowcharts & Methodological Focus |
| :---: | :--- | :--- |
| **01** | **Title Slide** | Executive Dark Navy academic title slide, Qwen-Local / Neo4j / LangGraph / Streamlit stack, research metadata. |
| **02** | **Literature Survey** | 4-column matrix citing Du et al. (ICML '24), Liang et al. (EMNLP '23), Sharma et al. (ICLR '24), Xiong et al. (ICLR '24), Buçinca et al. (CSCW '21), Edge et al. (Microsoft '24). |
| **03** | **Problem Definition (High-Level)** | One-Dimensional LLM Advice vs. Real-World Career Trade-offs: The Sycophancy-Viability Trap, the Illusion of False Certainty, and Automation Complacency. |
| **04** | **Problem Definition (Low-Level)** | Formal mathematical environment tuple $\mathcal{M} = \langle \mathcal{P}, \mathcal{G}, \mathcal{D}_{rag}, \mathbf{\Pi}, \mathcal{T}_{debate}, \Phi \rangle$, state transitions, and conflicting optimization goals. |
| **05** | **Flowchart 1: System Architecture** | **Native Visual Diagram with Connector Arrows:** Candidate Intake $\to$ Hybrid Knowledge Base (Neo4j DAG + FAISS) $\to$ LangGraph Multi-Agent Harness $\to$ Multi-Persona Deliberation Engine $\to$ Decision Diamond Gate $\to$ Streamlit UI. |
| **06** | **The 3 Career Philosophy Personas** | Deep specification of conflicting advising goals: **The Pragmatic Traditionalist** (Corporate, DSA, LeetCode), **The Entrepreneurial Builder** (Startup, AI SaaS, Agentic RAG), **The Deep-Tech Specialist** (Linux, 5NF Databases, Infrastructure). |
| **07** | **The Moderator Agent** | Synthesizer & Strategist: System prompt directive, probing friction point generation, dispute tree extraction, calibrated uncertainty calculation, and hybrid plan synthesis. |
| **08** | **Flowchart 2: The 5-Stage Debate Workflow** | **Execution Loop Diagram:** 1. Context Intake $\to$ 2. Opening Statements (Parallel 150w) $\to$ 3. Cross-Exam Friction $\to$ 4. Rebuttals $\to$ 5. Hybrid Synthesis with Override. |
| **09** | **Hybrid Grounding** | Neo4j Knowledge Graph (O\*NET/ESCO DAG, deterministic prerequisites) vs. FAISS Vector Store (syllabi & wage tables) + "Why Vector RAG Alone Fails" banner. |
| **10** | **Responsible AI: Calibrated Uncertainty** | Epistemic Uncertainty Formula $U(\mathcal{R}^*) = \alpha \cdot H(\mathbf{\Pi}) + \beta \cdot \text{Sparsity}(\mathcal{G}, P) + \gamma \cdot (1 - \text{GroundingScore})$ and Cognitive Forcing Trigger Gate ($TriggerOverride$). |
| **11** | **Counterfactual Fairness Auditing** | 500+ synthetic profile pair testing protocol, Recommendation Parity ($\Delta_{parity} \le 0.05$), Salary Skew, and Credential Exploitation Ratios. |
| **12** | **How to Measure Outcome** | Comprehensive 6-metric benchmark table: Evidence Diversity, Contradiction-Resolution Rate (CRR $\ge 85\%$), Unsupported-Claim Rate (UCR $< 5\%$), Counterfactual Parity, ECE, Counselor Rubric. |
| **13** | **Flowchart 3: Evaluation Pipeline** | **End-to-End Validation Pipeline:** Synthetic Profile Generator $\to$ Automated Debate Harness $\to$ Automated Metric Audit (NLI + Citation Verifiers) $\to$ Counselor Double-Blind Review & Scorecard. |
| **14** | **Comparative Ablation Benchmarks** | 4-way comparative matrix: Vanilla Qwen vs. Single-Agent RAG vs. Dyadic Debate vs. Full Dialectic Triad. |
| **15** | **Prototype, Privacy & Conclusion** | Streamlit UI walkthrough (Debate trace, dispute tree, risk gauges, human override) + 100% on-premise local privacy with local Qwen. |

All slides include embedded presentation speaker notes inside PowerPoint's native notes pane.
