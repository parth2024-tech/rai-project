# Key Research Papers: Debate-Based Career Guidance Agent

This bibliography covers the foundational and state-of-the-art literature directly supporting the multi-persona debate, responsible AI, calibrated uncertainty, and human-in-the-loop architecture.

---

### 1. Multi-Agent Debate for Factuality & Hallucination Suppression
* **Title:** *Improving Factuality and Reasoning in Language Models through Multiagent Debate*
* **Authors:** Yilun Du, Shuang Li, Antonio Torralba, Joshua B. Tenenbaum, Igor Mordatch
* **Venue / Year:** ICML 2024 / [arXiv:2305.14325](https://arxiv.org/abs/2305.14325)
* **Relevance to Project:**
  Provides the primary empirical and theoretical proof that iterative debate across multiple agent instances significantly reduces factual hallucinations and improves reasoning consistency compared to single-agent prompting. Directly validates the interaction harness between the **Planner** and **Critic**.

---

### 2. Complementary Personas & Divergent Exploration
* **Title:** *Encouraging Divergent Thinking in Large Language Models via Multi-Agent Debate*
* **Authors:** Tian Liang, Zhiwei He, Wenxiang Jiao, Xing Wang, Yan Wang, Rui Wang, Yujiu Yang, Zhaopeng Tu, Shuming Shi
* **Venue / Year:** EMNLP 2023 / [arXiv:2305.19118](https://arxiv.org/abs/2305.19118)
* **Relevance to Project:**
  Proves that assigning distinct personas with divergent goals prevents premature consensus collapse and stimulates exploring alternative solution paths. Foundation for designing complementary agent prompts (**Planner** optimizing opportunity vs. **Critic** optimizing friction vs. **Ethics-Reviewer** auditing equity).

---

### 3. Sycophancy Mitigation & Unbiased Advisory
* **Title:** *Towards Understanding Sycophancy in Language Models*
* **Authors:** Mrinank Sharma, Meg Tong, Tomasz Korbak, David Duvenaud, Amanda Askell, Samuel R. Bowman, Newton Cheng, et al.
* **Venue / Year:** ICLR 2024 / [arXiv:2310.13548](https://arxiv.org/abs/2310.13548)
* **Relevance to Project:**
  Diagnoses the exact vulnerability this project targets: standard LLMs' tendency to flatter the user, affirm unrealistic transition plans, and conceal risks to maximize conversational agreement. Provides motivation for adversarial red-teaming personas.

---

### 4. Epistemic Uncertainty Elicitation & Calibration
* **Title:** *Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs*
* **Authors:** Miao Xiong, Zhiyuan Hu, Xinyun Lu, Yifei Li, Jie Fu, Junxian He, Bryan Hooi
* **Venue / Year:** ICLR 2024 / [arXiv:2306.13063](https://arxiv.org/abs/2306.13063)
* **Relevance to Project:**
  Evaluates methods to elicit calibrated confidence scores and verbalized uncertainty from LLMs. Serves as the mathematical blueprint for the system's calibrated uncertainty metric ($U(\mathcal{R}^*) \in [0, 1]$), ensuring the model reports self-aware risk levels rather than overconfident assertions.

---

### 5. Automation Bias Mitigation & Cognitive Forcing Functions (Human Override)
* **Title:** *To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making*
* **Authors:** Zana Buçinca, Maja Barbara Malaya, Krzysztof Z. Gajos
* **Venue / Year:** ACM CSCW / PACMHCI 2021 / [DOI:10.1145/3449287](https://doi.org/10.1145/3449287)
* **Relevance to Project:**
  Demonstrates that presenting finished AI recommendations causes automation bias (blind user compliance). Introduces "cognitive forcing functions"—introducing deliberate decision friction by exposing disagreement traces and requiring explicit human override before commitment.

---

### 6. Graph-Grounded Trajectory & Ontological Retrieval (GraphRAG)
* **Title:** *From Local to Global: A Graph RAG Approach to Query-Focused Summarization*
* **Authors:** Darren Edge, Ha Trinh, Newman Cheng, Joshua Bradley, Alex Chao, Apurva Mody, Steven Truitt, Jonathan Larson
* **Venue / Year:** Microsoft Research 2024 / [arXiv:2404.16130](https://arxiv.org/abs/2404.16130)
* **Relevance to Project:**
  Demonstrates how combining structured knowledge graph hierarchies with unstructured vector retrieval (GraphRAG) solves vector-search blindspots. Justifies integrating the **Neo4j** career-skill prerequisite graph with **Chroma/FAISS** course catalogs.
