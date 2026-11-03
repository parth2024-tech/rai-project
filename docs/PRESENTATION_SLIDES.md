# Audited Presentation Slide Deck: Debate-Based Career Guidance Agent

**Definitive Presentation Files:**
* PowerPoint Deck: [`Final_Presentation.pptx`](file:///home/thor/Desktop/RAI%20Project/Final_Presentation.pptx)
* PDF Presentation: [`docs/Final_Presentation.pdf`](file:///home/thor/Desktop/RAI%20Project/docs/Final_Presentation.pdf)
* Generator Script: [`generate_deck.py`](file:///home/thor/Desktop/RAI%20Project/generate_deck.py)
* Interactive Streamlit Prototype: [`app.py`](file:///home/thor/Desktop/RAI%20Project/app.py)
* Comparative Evaluation Runner: [`run_study.py`](file:///home/thor/Desktop/RAI%20Project/run_study.py)

---

### Core Specification Alignment (100% Verified)

* **Personas:** Planner, Critic, and Ethics-Reviewer orchestrated by a Moderator Synthesizer.
* **Core Principles:** Avoiding one-sided advice, transparency of disagreement, fairness, calibrated uncertainty, and human override.
* **Tech Stack:** Qwen local (via Ollama); Python multi-agent harness; Neo4j career-skill graph (42-node prerequisite DAG); Chroma/FAISS (public ACM course & O*NET role data); Streamlit (interactive prototype & debate trace viewer).
* **Evaluation Metrics:** Evidence diversity ($H_{\text{div}}$); Contradiction-resolution rate (CRR); Unsupported-claim rate (UCR); Fairness across synthetic profiles (Jaccard similarity); User-rubric score (1.0 to 5.0).
* **Deliverables:** Multi-persona prototype (`app.py`), debate trace viewer, synthetic profile set (20 profiles across 10 base archetypes), and comparative evaluation (`run_study.py` / `data/eval_results.json`).

---

### Slide Deck Architecture: 18 Academic Slides (Aligned across 7 Mandatory Sections)

| Slide # | Mandatory Section | Slide Title & Core Academic Content |
| :---: | :--- | :--- |
| **01** | **Title Slide** | Executive Dark Slate theme: Project title, degree program (B.Tech CSE), student metadata, official tech stack (Qwen Local, Python Harness, Neo4j Graph, Chroma, Streamlit). |
| **02** | **Section 1: Abstract** | Problem statement (sycophancy trap, false consensus), 3-persona dialectic architecture, public data grounding, calibrated uncertainty, and human override. |
| **03** | **Section 2: Introduction** | Monolithic Flattery vs Grounded Dialectics: Side-by-side comparison flowchart contrasting standard LLM sycophancy with our grounded debate pipeline. |
| **04** | **Section 2: Introduction** | Research Questions (RQ1–RQ5), System Scope, and Core Ethical Commitments (avoiding one-sidedness, disagreement transparency, fairness, agency). |
| **05** | **Section 3: Literature Survey** | Three Theoretical Pillars: Multi-Agent Debate (Du et al., Liang et al.), Public Course & Role Grounding (ACM CS2023, O*NET), and Algorithmic Fairness / Cognitive Forcing (Geyik et al., Buçinca et al.). |
| **06** | **Section 3: Literature Survey** | Addressing Critiques of Debate: Direct counter to Smit et al. (2024, "Should We Be Going MAD?"), shared priors, consensus collapse, and majority voting failure modes. |
| **07** | **Section 3: Literature Survey** | Comparative Feature Matrix: Systematic benchmarking of 5 published frameworks against our Proposed Architecture across 6 core technical dimensions. |
| **08** | **Section 4: Architecture Diagram** | End-to-End Decision Flow: Left-to-right horizontal flowchart (Candidate Intake $\to$ Chroma Retrieval $\to$ Multi-Persona Triad $\to$ Moderator & 42-Node DAG $\to$ Gate Decision Diamond $\to$ Streamlit Human Override / Balanced Synthesis). |
| **09** | **Section 4: Architecture Details** | Complementary Persona Dialectics: Detailed specifications for **Planner** (Pathways), **Critic** (Prerequisites & Saturation), and **Ethics-Reviewer** (Fairness, Debt Mitigation & Agency). |
| **10** | **Section 4: Architecture Details** | Neo4j Career-Skill Graph (42 Nodes): Visual 4-track curriculum DAG with cross-track prerequisite edges, topological ordering, and Neo4j Cypher query export. |
| **11** | **Section 4: Architecture Details** | Dispute Tree & Human Override: Visual dispute tree ($\mathcal{T}_{\text{dispute}}$) breaking down consensus core vs trade-off branches (Foundational Systems Rigor vs Accelerated Application Track), with Streamlit override gateway. |
| **12** | **Section 5: Experimental Setup** | Four Comparative Configurations: Config 1 (Single LLM Monolithic), Config 2 (Single LLM Multi-Perspective), Config 3 (Unmoderated Triad), and Config 4 (Proposed RAI System). |
| **13** | **Section 5: Experimental Setup** | Synthetic Candidate Profile Dataset: 20 synthetic candidate profiles across 10 base archetypes with paired counterfactual variants (Aarav Sharma [Tier-1, High Budget] vs Priya Patel [Tier-3, Low Budget]). |
| **14** | **Section 5: Experimental Setup** | Five Official Evaluation Metrics: Formal mathematical definitions and measurement procedures for Evidence Diversity ($H_{\text{div}}$), CRR, UCR, Fairness (Jaccard), and User-Rubric Score. |
| **15** | **Section 6: Results & Discussion** | Pilot Quantitative Findings: Full 4-configuration $\times$ 5-metric benchmark table proving 0.0% unsupported claims, 100% contradiction resolution, 1.00 evidence diversity, and 1.00 fairness parity. |
| **16** | **Section 6: Results & Discussion** | Case Walkthrough ("Priya"): High-risk ML pivot scenario demonstrating Critic prerequisite intervention, Ethics debt shield, calibrated uncertainty calculation ($U = 0.77$), and student agency restoration. |
| **17** | **Section 7: References** | Canonical Academic Bibliography: Complete formal citations with DOIs and arXiv identifiers for Du et al., Liang et al., Smit et al., ACM CS2023, Sharma et al., Geyik et al., and Buçinca et al. |
| **18** | **Section 7: Conclusion** | Threats to Validity, System Boundaries, Deliverables Summary, and Committee Viva Voce Q&A Callout with demonstrator access instructions (`streamlit run app.py`). |

---

### Presentation Standards
- **Typography:** Display headlines $\ge 21\text{pt}$ (Title slide $28\text{pt}$), body text $11.5\text{--}12.5\text{pt}$.
- **Palette (60-30-10):** Background Slate 50 (60%), Navy / Slate 800 (30%), Teal / Rose / Amber / Blue accents (10%).
- **Native Visual Diagrams:** Native PowerPoint shapes, decision diamonds, horizontal flowcharts, network cards, and dispute trees.
- **Presenter Notes:** Every slide includes comprehensive, natural academic talking points for the viva voce committee.
