# College Viva & Presentation Defense Guide
## Debate-Based Career Guidance Agent with Complementary Personas and Knowledge Graph Verification
**Department of Computing Technologies | SRM Institute of Science and Technology**  
**Faculty Mentor:** Dr. P. Akilandeswari | **Industry Mentor:** Pratyush Jha

---

## 🎯 1. The 60-Second Elevator Pitch
*(Memorize this exact flow for your opening remarks when the examiner says "Introduce your project"):*

> "Good morning, respected faculty and examiners.
> 
> Today, engineering students heavily rely on conversational AI tools like ChatGPT for career and placement roadmaps. However, conventional single-prompt chatbots suffer from three major failures:
> 1. **They skip foundational prerequisites:** They enthusiastically advise beginners to jump straight into advanced topics like Deep Learning or Distributed Systems without checking if they know Linear Algebra or Operating Systems.
> 2. **They push expensive commercial bootcamps:** They recommend ₹1,20,000 commercial courses to students from modest backgrounds while ignoring free, world-class resources like MIT OpenCourseWare and Harvard CS50.
> 3. **They flatter the student (sycophancy):** If a student claims they will become a Senior AI Engineer in 3 months, the model agrees instead of giving honest feedback.
> 
> To solve this, our project replaces a single chatbot with a **Debate-Based Multi-Persona System**:
> - A **Planner** creates the roadmap.
> - A **Critic** attacks unrealistic timelines and missing prerequisites.
> - An **Ethics-Reviewer** defends student finances, prevents debt, and enforces free open-source courseware.
> - A **42-Node Knowledge Graph** checks prerequisites mathematically in Python code, eliminating prerequisite errors from **90.9% down to 0.0%**.
> - An interactive **Cognitive Forcing Gate** gives the student transparent slider control over their priorities.
> 
> The entire system runs **100% locally on a student laptop** using Ollama and Qwen 2.5 7B, guaranteeing zero API costs and total student data privacy."

---

## 💻 2. The Two Most Feared Questions (And Exact Winning Answers)

### Question 1: *"Where is your model? Did you train it from scratch?"*
* **Faculty Trap:** If you say "Yes, we trained it," they will ask for GPU cluster logs, loss curves, and epochs. If you say "No, it's just ChatGPT API," they will say you did zero engineering work.
* **Winning Answer:**
  > "Sir, we did not train a foundation model from scratch because training a 7-billion parameter LLM requires thousands of GPU hours and millions of dollars. Instead, we use **Qwen 2.5 7B**, an open-weight foundation model running **100% locally on our laptop via Ollama**.
  > 
  > **What WE designed and engineered is:**
  > 1. The **Multi-Agent Dialectic Architecture**: Configuring 3 distinct persona contracts with divergent decoding temperatures ($T=0.3$ for Critic, $T=0.7$ for Planner) to prevent conversational collapse.
  > 2. The **42-Node Knowledge Graph in NetworkX**: 42 computer science nodes and 47 directed prerequisite edges that check curriculum reachability deterministically in $O(V+E)$ time.
  > 3. The **ChromaDB Vector Retrieval Pipeline**: Indexing ACM CS2023 curricula, MIT OCW, Harvard CS50, and O*NET job standards.
  > 4. The **Cognitive Forcing Gate**: Mathematical uncertainty formulation ($U_{\text{cal}}$) and the Streamlit human-in-the-loop override interface.
  > 5. The **20-Profile Benchmark Suite**: 80 automated comparative runs evaluating prerequisite safety, evidence diversity, and counterfactual fairness."

---

### Question 2: *"Where did you get the data? How is it validated?"*
* **Faculty Trap:** Examiners want to know if you made up the curriculum or downloaded random internet data.
* **Winning Answer:**
  > "Sir, our system uses three verified, accredited data sources:
  > 1. **Accredited University Curricula:** 15 official course specifications directly from the **ACM/IEEE CS2023 Curricular Guidelines**, **MIT OpenCourseWare (18.06, 6.006)**, and **Harvard CS50**, indexed in our local ChromaDB vector store.
  > 2. **Government Occupational Standards:** 8 official career taxonomies from the **U.S. Department of Labor O*NET 29.2** and **Bureau of Labor Statistics (BLS)**, providing official salary percentiles and entry requirements.
  > 3. **The 20-Profile Benchmark Suite:** 20 synthetic candidate profiles across 10 CS career tracks. We paired them into 10 **counterfactual pairs** (holding skills, GPA, and career goals identical while varying college tier and monthly budget) so we could scientifically audit whether our AI exhibits bias."

---

## 📊 3. The 5 Formulas in Simple Words (Viva Cheat Sheet)

| Formula Symbol | Metric Name | What It Means in Plain English | Baseline | Our System |
| :--- | :--- | :--- | :---: | :---: |
| **$UCR$** | Unsupported-Claim / Prerequisite Error Rate | Out of all recommended milestones, what % skipped necessary prior subjects? *(e.g. taking Deep Learning without Linear Algebra)* | **90.9%** | **0.0%** |
| **$\Delta_{\text{prereq}}$** | Missing Prerequisite Count | The raw number of foundational subjects missing in a proposed roadmap. | $\ge 2.8$ | **0** |
| **$H_{\text{div}}$** | Evidence Diversity | Does the AI cite multiple diverse sources (MIT + Harvard + O*NET) instead of just repeating one link? | **0.22** | **1.00** |
| **$CRR$** | Contradiction Resolution Rate | When the Critic and Ethics agents raised objections, did the Moderator successfully fix them in the final roadmap? | **0.0%** | **100.0%** |
| **$J$** | Demographic Fairness (Jaccard Score) | Do two students with identical skills get the same core curriculum regardless of whether they study at IIT or a rural Tier-3 college? | **0.32** | **1.00** |
| **$U_{\text{cal}}$** | Calibrated Uncertainty | A score between $0$ and $1$ combining debate friction, missing prerequisites, budget limits, and timeline pressure. If $\ge 0.45$, the gate halts and asks the student to decide. | N/A | **Active** |

---

## 🛠️ 4. What Did WE Build in Code? (The Architecture Breakdown)

If the examiner asks: *"Show me your code structure"*:
1. `src/graph/career_graph.py`: Contains the 42 nodes and 47 prerequisite edges in NetworkX. Traverses the graph in $O(V+E)$ time ($< 0.2\text{ ms}$).
2. `src/agents/personas.py`: Defines the system prompts and temperature contracts for Planner, Critic, Ethics-Reviewer, and Moderator.
3. `src/retrieval/vector_store.py`: Loads ACM/MIT/O*NET chunks into local ChromaDB with cosine vector search.
4. `src/gate/cognitive_gate.py`: Calculates uncertainty $U_{\text{cal}}$, extracts the 3-point Dispute Tree, and manages the interactive override sliders.
5. `app.py`: Streamlit frontend with interactive UI, dispute visualization, and roadmap export.
6. `src/utils/plagiarism_auditor.py`: Automated n-gram audit script verifying 0% plagiarism.

---

## 🎓 5. Top 10 Faculty Viva Questions & Exact Answers

### Q1: Why 3 separate agents instead of 1 prompt saying "Think from 3 perspectives"?
> "Sir, we actually tested that! That was **Configuration 2 (Multi-Perspective Prompting)** in our paper. When you ask a single LLM to play multiple roles, the internal attention mechanism averages the conflicting opinions and converges on an optimistic middle ground. Contradiction resolution was only 38%. With physically separate agents running with distinct prompts and temperatures, the Critic and Ethics agents cannot be silenced by the Planner."

### Q2: Why did you need a Knowledge Graph if LLMs are already smart?
> "Sir, Large Language Models are probabilistic next-token predictors. They have no concept of strict mathematical dependency. If a student says 'I want to build an LLM in 1 month', the LLM generates tokens about PyTorch and Transformers because they match semantically, ignoring that the student doesn't know Python OOP or Linear Algebra. Our 42-node Directed Acyclic Graph (DAG) evaluates prerequisites deterministically in code in 0.12 milliseconds, guaranteeing 100% prerequisite safety."

### Q3: What happens if a student refuses to study prerequisites and uses the slider?
> "Sir, that is the exact purpose of the **Cognitive Forcing Gate**. We do not patronize the student by hiding options. If the student overrides the Critic using the slider, the system logs the override, generates an 'Accelerated High-Risk Pathway', but explicitly flags: *'Warning: Candidate accepted high screening failure risk on Milestone 2 due to missing Operating Systems foundations.'* The student makes an informed choice rather than being blindly misled."

### Q4: What model did you use, and what are its hardware requirements?
> "Sir, we use **Qwen 2.5 7B** quantized to 4-bit (`q4_k_m`) running via Ollama. It consumes **5.2 GB of RAM**, fits easily on any modern 16 GB laptop, and generates each debate response in ~3 to 4 seconds (~11.4 seconds total for the entire pipeline). It costs ₹0 in API fees and runs completely offline."

### Q5: How did you prove that your system is fair to poor or Tier-3 students?
> "Sir, we used **Counterfactual Demographic Pairs**. We created 10 matched student pairs where skills, GPA, and goals were identical, but one had ₹40,000 budget at a Tier-1 college, and the other had ₹3,000 budget at a rural Tier-3 college. Baseline ChatGPT gave the rich student advanced topics and the poor student low-level support roles ($J = 0.32$). Our system recommended identical core technical competencies ($J = 1.00$) while substituting expensive bootcamps with free MIT OpenCourseWare."

### Q6: What is the "Priya Patel" Case Study in your paper?
> "Sir, Priya Patel is Profile P1_B in our benchmark: a 3rd-year student at a rural college with ₹3,000 monthly budget wanting to become an ML Engineer in 4 months. Standard ChatGPT flattered her and told her to take a ₹1,20,000 bootcamp loan. In our system, the Critic flagged that she lacked Linear Algebra and OS, the Ethics agent blocked the predatory loan, and the Moderator helped her choose a zero-debt roadmap using MIT 18.06 and open-source GitHub projects."

### Q7: Why did you choose Typst to write your research paper instead of LaTeX?
> "Sir, Typst is a modern, Rust-based typesetting system that compiles in under 20 milliseconds, compared to LaTeX which takes 10 to 30 seconds. Typst provides clean diagnostics, deterministic math layouts, and native IEEE bibliography formatting while guaranteeing 0% formatting warnings."

### Q8: What statistical tests did you run to prove your results aren't just random luck?
> "Sir, we ran two formal statistical tests:
> 1. **McNemar's Paired Test:** Proved that our 18 fixed profiles vs. 0 regressions compared to baseline is statistically significant with $p < 0.0001$.
> 2. **Cohen's Kappa ($\kappa$):** Tested inter-annotator reliability between our two independent student annotators on the 20 benchmark profiles based on official ACM CS2023 syllabi. We achieved $\kappa = 0.926$ on gate triggers and $\kappa = 0.841$ on dispute resolutions, proving 'Almost Perfect' consistency in our ground-truth labels."

### Q9: How does this project benefit SRMIST students specifically?
> "Sir, during 6th and 7th semester campus placements, students get overwhelmed by aggressive ads for commercial bootcamps and certifications. If deployed on SRM's internal student portal, students can input their dream company or job role and receive an honest, prerequisite-checked roadmap using free NPTEL, MIT, and CS50 resources, with zero risk of commercial exploitation."

### Q10: What are the future enhancements?
> "Sir, our future scope includes:
> 1. Expanding the knowledge graph from 42 Computer Science nodes to Mechanical, Electrical, and Biotechnology domains.
> 2. Integrating GitHub API to automatically verify student commits and projects instead of relying solely on self-reported skills.
> 3. Conducting a longitudinal study tracking student placement conversion rates across multiple semesters."

---

## 🏆 Summary Checklist for Defense Day
- [x] Streamlit app ready to run: `streamlit run app.py`
- [x] Local Ollama daemon running: `ollama run qwen2.5:7b`
- [x] Paper compiled and ready: `docs/ACADEMIC_RESEARCH_PAPER.pdf` (5 full, balanced pages, 0% plagiarism)
- [x] 33/33 Pytest test suite passing: `pytest`
- [x] Clear understanding of the 3 personas, the 42-node graph, and the 5 formulas.
