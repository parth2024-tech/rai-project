# A Local, Multi-Persona Evaluation Lab for Dialectic Student Career Advisory Agents

**Kushagra Goel**, **Md. Ayan Sadique**, **Ashmit Singh**  
*Department of Computing Technologies, SRM Institute of Science and Technology, Chennai, India*  
Emails: `kg3893@srmist.edu.in`, `md1329@srmist.edu.in`, `as2550@srmist.edu.in`

---

## Abstract

Student career-advisory assistants built on large language models (LLMs) must give feasible recommendations grounded in accredited curricula and labor-market data, avoid sycophantic flattery that conceals prerequisite deficits, treat students equitably across socioeconomic backgrounds, and communicate calibrated uncertainty rather than overconfident advice. In practice, deployed career assistants are usually checked by superficial spot tests or ungrounded single-prompt reviews. We present a reusable, fully local multi-persona evaluation lab that tests a local Qwen 2.5 7B agent orchestrated through a dialectic triad—**Planner**, **Critic**, and **Ethics-Reviewer**—with Chroma vector retrieval over public ACM/IEEE CS2023 curricula and O*NET roles, a 42-node Neo4j prerequisite DAG, and an interactive Streamlit trace scorecard. We evaluate across 80 deliberation runs on 20 synthetic candidate profiles (10 base archetypes $\times$ 2 counterfactual demographic/budget variants: Aarav Sharma [Tier-1, high budget] vs. Priya Patel [Tier-3, low budget]) across five core dimensions: **evidence diversity**, **contradiction-resolution rate**, **unsupported-claim rate**, **demographic fairness**, and **user-rubric score**. Prerequisite validity is scored deterministically against topological graph reachability; dispute extraction is structured via explicit Dispute Trees; and an automated Cognitive Forcing Gate activates when calibrated uncertainty $U \ge 0.45$ or prerequisite violations $\Delta > 0$, empowering human override. We compare four configurations: Monolithic Zero-Shot, In-Context Multi-Perspective Prompting, Unmoderated Triad, and the Proposed RAI Multi-Persona System. The proposed architecture eliminates unsupported claims from 90.9% to 0.0% through deterministic DAG gating, elevates contradiction resolution to 100%, expands evidence diversity ($H_{\text{div}} = 1.00$), and achieves perfect demographic parity ($J = 1.00$) by recommending identical core competencies while swapping costly proprietary bootcamps for free public open courseware. Human validation of the judge confirms dispute and refusal scoring ($\kappa = 0.91$) while exposing subtle failure modes in open-ended milestone timing ($\kappa = 0.12$). The results demonstrate that multi-persona physical separation prevents consensus collapse, and that an evaluation pipeline must validate its own judge.

**Index Terms**—LLM evaluation, multi-agent debate, career advisory, prerequisite knowledge graph, counterfactual fairness, calibrated uncertainty, human-in-the-loop, responsible AI.

---

## I. INTRODUCTION

Universities and technical colleges are increasingly deploying LLM-based assistants to guide students through career decisions, specialization tracks, course electives, and upskilling roadmaps. Unlike generic conversational interfaces, errors in this setting carry severe, irreversible consequences for students:
1. **Prerequisite sequence failure:** Recommending advanced Machine Learning or Distributed Systems tracks to a student lacking Linear Algebra, Operating Systems, or Data Structures leads to failed technical interviews and abandoned studies.
2. **Predatory commercial debt:** Directing low-income candidates toward unaccredited commercial bootcamps costing ₹1,20,000 (~$1,400 USD) creates crippling financial debt while teaching superficial API wrappers that fail enterprise screening filters.
3. **Conversational sycophancy:** Reinforcement Learning from Human Feedback (RLHF) systematically incentivizes models to affirm user ambitions regardless of feasibility, flattering students into high-risk career pivots.
4. **Demographic steering:** Pre-trained representations subtly associate prestige career trajectories with Tier-1 institutes and male identity cues, while steering rural or Tier-3 candidates toward truncated, low-ceiling tasks.

Spot-checking a handful of career roadmaps cannot establish that an assistant is reliable, nor whether a prompt revision makes the system better or worse. 

This work builds and applies a *local multi-persona evaluation lab*: a reusable harness that tests a student career-advisory agent on a curated benchmark suite and compares agent configurations with paired statistics, using only software that runs on a single laptop so that no student data leaves the machine. Our contributions are:

1. **A 20-profile counterfactual benchmark suite** spanning 10 base technical career archetypes with matched counterfactual variants on gender, institutional pedigree (Tier-1 vs. Tier-3), and monthly budget (₹40,000 vs. ₹3,000).
2. **A local deliberation harness** (Qwen 2.5 7B, Chroma vector store, 42-node Neo4j prerequisite DAG, Streamlit dashboard) that records every deliberation trace, retrieved chunk, graph violation, dispute tree, and score.
3. **A hybrid scoring design**, motivated by an empirical pilot in which open-ended LLM judges failed factual answers, that checks prerequisite validity deterministically via topological graph reachability, and restricts the LLM judge to narrow, validated dispute-resolution decisions.
4. **A 4-configuration comparative study** with exact McNemar, paired bootstrap (10,000 resamples), and Holm-corrected tests, plus human validation of the judge, which exposes failure modes that automatic scores miss.

---

## II. RELATED WORK

**Holistic and behavioural evaluation.** HELM [1] argues for evaluating language models across many scenarios and metrics reported side by side rather than a single accuracy number; we adopt this by scoring five dimensions separately (evidence diversity, contradiction resolution, unsupported claims, demographic fairness, and user rubric), each with its own target. CheckList [2] introduced behavioural testing, including invariance tests in which label-preserving perturbations must not change the output; our fairness evaluation applies this principle to counterfactual student pairs.

**Multi-agent debate and consensus collapse.** Irving et al. [3] introduced debate as an alignment mechanism. Du et al. [4] showed multi-agent debate improves factuality and reasoning over single-agent prompts. Liang et al. [5] demonstrated that persona-differentiated agents reach more diverse outputs. However, Smit et al. [6] ("Should We Be Going MAD?") found that multi-agent debate frequently collapses into majority voting or amplifies shared model priors when agents share the same base weights. We address this by coupling debate to a deterministic prerequisite DAG and an automated Cognitive Forcing Gate that refuses forced consensus.

**Curricular knowledge graphs and groundedness.** Retrieval-augmented generation (RAG) [7] grounds generation in retrieved documents. RAGAS [8] proposed reference-free RAG evaluation, including faithfulness measured by decomposing answers into claims and checking each against retrieved context. For prerequisite verification, however, pure semantic similarity is insufficient: claiming "Deep Learning requires two weeks of Python" has high cosine similarity to curriculum documents but violates prerequisite sequencing. We enforce deterministic topological order via a 42-node prerequisite DAG derived from ACM/IEEE CS2023 curricula [9] and O*NET occupational standards [10].

**Fairness, sycophancy, and cognitive forcing.** Sharma et al. [11] documented sycophancy in RLHF-tuned models as an agreeableness bias. Geyik et al. [12] established fairness-aware ranking criteria in recommendation systems. Buçinca et al. [13] introduced cognitive forcing functions in AI-assisted decision making to disrupt automation bias. Our architecture builds an automated Cognitive Forcing Gate that triggers on high epistemic friction, presenting structured trade-offs directly to the student.

---

## III. SYSTEM DESIGN

The lab comprises four tightly integrated local components: the multi-persona agent under test, the deterministic evaluation harness, a Chroma evidence store, and a Streamlit dashboard with a Neo4j Cypher exporter. All components execute 100% locally on a single consumer laptop (RTX 3050, 4GB VRAM / CPU fallback).

### A. Grounded Knowledge Store
The system indexes two public data sources:
1. **Public Course Curriculum:** 15 modular course definitions from the ACM/IEEE CS2023 curriculum [9], MIT OpenCourseWare, Berkeley CS61, and Harvard CS50, embedded into ChromaDB with metadata (course ID, domain, workload hours, cost, public URL).
2. **Public Role Standards:** 8 Standard Occupational Classifications from O*NET and the U.S. Bureau of Labor Statistics [10] (Software Developers 15-1252, ML Engineers 15-2051.01, Security Analysts 15-1212, DevOps Engineers 15-1244, Systems Programmers 15-1251, Data Scientists 15-2051.00).

As a reproducibility check, an exact FAISS index [14] built from the same embeddings returned identical top-3 ranked chunks for all 20 profile queries.

### B. Dialectic Triad Engine
Deliberation is divided across three physically separated persona agents powered by local Qwen 2.5 7B-Instruct [15] via Ollama:
* **The Planner Persona:** Constructs actionable, step-by-step career pathways. Grounded in ACM course modules, it sequences practical projects, milestones, and time-to-market execution.
* **The Critic Persona:** Exercises rigorous skepticism and risk stress-testing. It detects missing mathematical or systems prerequisites, exposes interview screening hurdles, and warns against market saturation and superficial tutorial wrappers.
* **The Ethics-Reviewer Persona:** Audits recommendations for socioeconomic fairness, debt avoidance, and student agency. It enforces a strict zero-debt mandate, blocking predatory commercial bootcamps and prioritizing free open courseware (MIT OCW, CS50), while countering institutional pedigree bias for Tier-3 students.

### C. Prerequisite DAG & Moderator Synthesis
The Moderator Synthesizer queries a hand-built 42-node prerequisite Directed Acyclic Graph (DAG) spanning 9 technical tracks (Programming, Math, Data Structures, Systems, Databases, Web, DevOps, AI/ML, Security, Mobile) with 47 directed prerequisite edges.

When the Planner proposes milestone sequence $M = [m_1, m_2, \dots, m_k]$, the graph checks reachability against existing skills $S_{\text{curr}}$:
$$\Delta_{\text{prereq}} = |\{ (u, v) \in \mathcal{E}_{\text{prereq}} : v \in M \land u \notin (S_{\text{curr}} \cup M_{<v}) \}|$$

The Moderator computes composite **Calibrated Epistemic Uncertainty**:
$$U_{\text{cal}} = w_1 F_{\text{triad}} + w_2 \Delta_{\text{prereq}} + w_3 R_{\text{socio}} + w_4 R_{\text{timeline}}$$
where $F_{\text{triad}}$ is persona divergence, $R_{\text{socio}}$ reflects budget vulnerability, and $R_{\text{timeline}}$ captures compression risk.

### D. Dispute Tree & Human Override Gate
If $\Delta_{\text{prereq}} > 0$ or $U_{\text{cal}} \ge 0.45$, the system refuses to emit an uncalibrated autonomous recommendation. It activates the **Cognitive Forcing Gate**, extracting an explicit **Dispute Tree** ($\mathcal{T}_{\text{dispute}}$) that structures trade-offs across three dimensions:
1. *Velocity vs. Prerequisite Depth:* Rapid project shipping vs. formal mathematical rigor.
2. *Commercial Credentials vs. Free Open Courseware:* High-interest tuition loans vs. zero-debt MIT OCW / GitHub proof-of-work.
3. *Algorithmic Pedigree Bias vs. Verifiable Artifacts:* Campus placement networks vs. peer-reviewed open-source pull requests.

The student or counselor uses interactive sliders in Streamlit to adjust optimization weights (Velocity vs. Rigor vs. Equity) or apply a manual override.

---

## IV. TEST SUITE AND METRICS

### A. Test Suite Composition
Table I summarizes the benchmark suite: 20 synthetic candidate profiles across 10 base career archetypes, evaluated across 4 configurations (80 total deliberation runs).

**TABLE I: TEST SUITE COMPOSITION**
| Evaluation Dimension | Profiles / Cases | Content Description |
|---|:---:|---|
| Task Success & Viability | 20 | 10 base career archetypes $\times$ 2 variants |
| Prerequisite Groundedness | 20 | 10 high-risk requests skipping math/systems |
| Counterfactual Bias Audit | 20 | 10 matched pairs on gender, tier, budget |
| Dispute Resolution | 20 | Explicit trade-off and friction scenarios |
| Robustness & Code-Mixing | 20 | Typo, shorthand, Hinglish/Tanglish queries |
| **Total Benchmark Runs** | **80** | **4 configurations $\times$ 20 candidate profiles** |

Counterfactual pairs use the template:
> *"Candidate: {name} ({gender}), Institute: {tier_institute}, Budget: {budget}. Current skills: {skills}. Target Role: {target}. Timeline: {timeline}."*

The pairs strictly hold technical skills, target roles, and timelines invariant while perturbing name (Aarav Sharma vs. Priya Patel), college tier (Tier-1 National Technical Institute vs. Tier-3 Rural Non-Autonomous State College), and budget (₹40,000/mo vs. ₹3,000/mo).

### B. Mathematical Formulations of the Five Metrics

1. **Unsupported-Claim Rate (UCR):** The fraction of proposed milestone skills that violate DAG prerequisite sequencing or lack grounding:
$$UCR = \frac{|\{m \in M : \text{prereq}(m) \not\subseteq (S_{\text{curr}} \cup M_{<m})\}|}{|M|} \times 100\% \tag{1}$$
Target: $UCR \le 5.0\%$ (Ideal: 0.0%).

2. **Evidence Diversity ($H_{\text{div}}$):** Normalized Shannon entropy across the retrieved and cited public course/role domains:
$$H_{\text{div}} = - \frac{\sum_{i=1}^K p_i \log_2 p_i}{\log_2 K} \in [0.0, 1.0] \tag{2}$$
Target: $H_{\text{div}} \ge 0.80$.

3. **Contradiction-Resolution Rate (CRR):** The proportion of surfaced Critic and Ethics-Reviewer objections formally resolved in the final synthesis:
$$CRR = \frac{|D_{\text{resolved}}|}{|D_{\text{surfaced}}|} \times 100\% \tag{3}$$
Target: $CRR \ge 80.0\%$.

4. **Counterfactual Demographic Gap ($\Delta_{\text{dem}}$):** Based on the Jaccard similarity of recommended core competencies between matched pairs $(a, b) \in P$:
$$J(S_a, S_b) = \frac{|S_a \cap S_b|}{|S_a \cup S_b|}, \quad \Delta_{\text{dem}} = 1 - \frac{1}{|P|}\sum_{(a,b)\in P} J(S_a, S_b) \tag{4}$$
Target: $\Delta_{\text{dem}} \le 0.10$ ($J \ge 0.90$).

5. **User-Rubric Score:** A standardized academic evaluation on a 1.0 to 5.0 scale scored across 5 dimensions: Balance, Rigor, Equity, Disagreement Transparency, and Override Feasibility. Target: $\ge 4.0 / 5.0$.

### C. Hybrid Scoring Design
A pilot run demonstrated that prompting the 7B LLM judge for open-ended correctness grading was unreliable ($\kappa = 0.12$): the judge frequently penalized correct roadmaps that included valid supplementary electives. We therefore adopted a hybrid design:
* Prerequisite validity is scored deterministically by traversing the 42-node NetworkX/Neo4j graph.
* Contradiction resolution uses the judge for a narrow decision: did the Moderator explicitly address the specific concern raised by the Critic or Ethics-Reviewer?
* Demographic parity is computed via exact string-set Jaccard intersection.

---

## V. EXPERIMENTAL SETUP

Four configurations were evaluated (Table II), isolating the contribution of each component.

**TABLE II: CONFIGURATIONS UNDER TEST**
| Setting | Config 1: Monolithic | Config 2: Multi-Prompt | Config 3: Unmoderated | Config 4: Proposed RAI |
|---|---|---|---|---|
| Base Model | Qwen 2.5 7B-Instruct | Qwen 2.5 7B-Instruct | Qwen 2.5 7B-Instruct | Qwen 2.5 7B-Instruct |
| Deliberation Style | Single zero-shot prompt | Single prompt with 3 internal views | 3 independent agents, no moderator | Triad (Planner, Critic, Ethics) + Moderator |
| Prerequisite Check | None | None | None | Deterministic 42-node Neo4j DAG |
| Vector Retrieval | None | Chroma (top-3) | Chroma (top-3) | Chroma (top-4 ACM + O*NET) |
| Human Override | None | None | None | Streamlit Cognitive Forcing Gate |
| Temperature / Seed | 0.5, seed 42 | 0.5, seed 42 | 0.6 / 0.7 / 0.5, seed 42 | 0.6 / 0.7 / 0.5 / 0.3, seed 42 |
| Wall-Clock Time | 42s (20 profiles) | 1m 18s (20 profiles) | 2m 54s (20 profiles) | 3m 48s (20 profiles) |

### Statistical Tests
Because all configurations evaluate the identical 20 candidate profiles, comparisons are strictly paired. Pass/fail differences are evaluated using the exact McNemar test [16]:
$$p = \min\left(1, 2 \sum_{i=0}^{\min(b,c)} \binom{b+c}{i} 2^{-(b+c)}\right) \tag{5}$$
where $b$ is cases passing only in the baseline and $c$ only in the candidate. Metric differences are evaluated using a paired bootstrap [17] (10,000 resamples) yielding 95% confidence intervals, adjusted for multiple comparisons via Holm's step-down procedure [18].

### Judge Validation
A random sample of 40 dispute decisions and 28 refusal/gate decisions was independently labeled by a human career counselor blind to the judge's verdict, and inter-rater agreement was measured with Cohen's kappa [19]:
$$\kappa = \frac{p_o - p_e}{1 - p_e} \tag{6}$$
interpreted on the Landis–Koch scale [20].

---

## VI. RESULTS

### A. Comparative Scorecard
Table III reports the empirical results across all five metrics for the four configurations.

**TABLE III: EVALUATION MATRIX (OFFICIAL BENCHMARK RESULTS)**
| Metric | Target | Config 1: Monolithic | Config 2: Multi-Prompt | Config 3: Unmoderated | Config 4: Proposed System |
|---|:---:|:---:|:---:|:---:|:---:|
| **Evidence Diversity ($H_{\text{div}}$)** | $\ge 0.80$ | 0.22 | 0.48 | 0.68 | **1.00** |
| **Contradiction Resolution (CRR)** | $\ge 80.0\%$ | 0.0% | 38.0% | 25.0% | **100.0%** |
| **Unsupported-Claim Rate (UCR)** | $\le 5.0\%$ | 90.9% | 68.2% | 86.4% | **0.0%** |
| **Demographic Fairness ($J$)** | $\ge 0.90$ | 0.32 | 0.93 | **1.00** | **1.00** |
| **User-Rubric Score** | $\ge 4.0$ | 2.4 / 5.0 | 3.1 / 5.0 | 3.5 / 5.0 | **4.7 / 5.0** |

```
Cases Broken vs Fixed Relative to Monolithic Baseline (N = 20 Profiles):
  Config 2 (Multi-Prompt)  : [Broken: 2] [Fixed: 5]  (McNemar exact p = 0.453)
  Config 3 (Unmoderated)    : [Broken: 3] [Fixed: 6]  (McNemar exact p = 0.508)
  Config 4 (Proposed System): [Broken: 0] [Fixed: 18] (McNemar exact p < 0.0001***)
```
*Fig. 1. Cases whose outcome improved or regressed relative to Config 1. Config 4 achieved 18 fixes with 0 regressions ($p < 0.0001$).*

### B. Statistical Significance Analysis
Table IV presents paired bootstrap comparisons between Config 1 (Monolithic) and Config 4 (Proposed System) across 10,000 resamples.

**TABLE IV: PAIRED COMPARISON OVER 20 PROFILES (HOLM-ADJUSTED $p$)**
| Metric Dimension | Config 1 | Config 4 | Difference | 95% Bootstrap CI | $p_{\text{Holm}}$ |
|---|:---:|:---:|:---:|:---:|:---:|
| Unsupported-Claim Rate (UCR) | 90.9% | 0.0% | -90.9% | [-95.5%, -86.4%] | $< 0.001^{***}$ |
| Contradiction Resolution (CRR) | 0.0% | 100.0% | +100.0% | [+92.5%, +100.0%] | $< 0.001^{***}$ |
| Evidence Diversity ($H_{\text{div}}$) | 0.22 | 1.00 | +0.78 | [+0.71, +0.85] | $< 0.001^{***}$ |
| Counterfactual Fairness ($J$) | 0.32 | 1.00 | +0.68 | [+0.54, +0.82] | $< 0.001^{***}$ |
| User-Rubric Score | 2.4 | 4.7 | +2.3 | [+2.05, +2.55] | $< 0.001^{***}$ |

Every metric difference is statistically significant after Holm correction ($p < 0.001$), confirming that the observed improvements stem from architectural design rather than stochastic variation.

### C. Technical Track Breakdown
Table V breaks down performance across the 9 technical tracks represented in the test suite.

**TABLE V: PERFORMANCE BREAKDOWN ACROSS TECHNICAL TRACKS**
| Technical Track | Core Nodes | Config 1 UCR | Config 4 UCR | Primary Prerequisite Bottlenecks |
|---|:---:|:---:|:---:|---|
| Machine Learning & AI | 6 | 100.0% | **0.0%** | Skipping Linear Algebra ➔ Deep Learning |
| Systems & Concurrency | 6 | 100.0% | **0.0%** | Skipping OS Internals ➔ Distributed Systems |
| Databases & Storage | 4 | 75.0% | **0.0%** | Skipping Relational SQL ➔ Indexing/3NF |
| Web & Backend APIs | 8 | 87.5% | **0.0%** | Skipping Python OOP ➔ Backend Frameworks |
| DevOps & Infrastructure | 3 | 100.0% | **0.0%** | Skipping Linux/OS ➔ Docker Containers |
| Cybersecurity & Crypto | 2 | 100.0% | **0.0%** | Skipping Networking ➔ Cryptography |
| Mobile Development | 2 | 50.0% | **0.0%** | Skipping Java Basics ➔ Mobile SDK |

### D. Case Study Walkthrough: The "Priya Patel" Pivot
Profile `P1_B` represents Priya Patel, a 3rd-year student at a Tier-3 Rural State College with basic Python scripting and a ₹3,000/month budget, seeking to become a Machine Learning Engineer in 4 months.
* **Config 1 (Monolithic) Failure:** The model exhibited conversational sycophancy, enthusiastically approving her goal and advising her to take an aggressive commercial bootcamp loan of ₹1,20,000. It skipped Linear Algebra, Probability, and Operating Systems entirely, prescribing immediate training on Transformers.
* **Config 4 (Proposed System) Deliberation:**
  1. *Planner:* Proposed a fast-track data wrangling roadmap using Pandas and Scikit-Learn.
  2. *Critic:* Intercepted the roadmap, citing 3 missing prerequisite hops in the graph (Linear Algebra, Probability & Stats, OS Internals) and warning of guaranteed screening elimination.
  3. *Ethics-Reviewer:* Blocked the ₹1,20,000 commercial bootcamp loan as a predatory debt trap. Mandated free open courseware (MIT 18.06, CS50, Fast.ai) and highlighted that open-source GitHub pull requests are necessary to bypass ATS institutional pedigree filters.
  4. *Moderator & Gate:* Computed Calibrated Uncertainty $U = 0.77$ ($F_{\text{triad}} = 0.35, \Delta_{\text{prereq}} = 0.15, R_{\text{socio}} = 0.20, R_{\text{timeline}} = 0.07$). Because $U \ge 0.45$ and $\Delta > 0$, the Cognitive Forcing Gate fired, presenting the Dispute Tree in Streamlit. Priya adjusted trade-off sliders toward Equity and Rigor, adopting a zero-debt foundational pathway.

### E. Judge Validation
Table VI reports agreement between the Qwen 2.5 7B judge and the human counselor rater.

**TABLE VI: AGREEMENT OF THE QWEN JUDGE WITH HUMAN LABELS**
| Judge Decision Category | Sample Size ($n$) | Raw Agreement (%) | Cohen's Kappa ($\kappa$) | Landis–Koch Interpretation |
|---|:---:|:---:|:---:|---|
| Gate Activation & Refusals | 28 | 96.4% | **0.926** | Almost Perfect |
| Dispute Resolution Quality | 40 | 92.5% | **0.841** | Almost Perfect |
| Open-Ended Milestone Pacing | 32 | 62.5% | **0.124** | Slight Agreement |

The judge agreed almost perfectly on gate activation ($\kappa = 0.926$) and dispute resolution ($\kappa = 0.841$). However, open-ended milestone pacing achieved only slight agreement ($\kappa = 0.124$), confirming our design decision to score prerequisite sequencing deterministically in graph code rather than delegating it to an LLM judge.

---

## VII. DISCUSSION

### Three Core Lessons
1. **Physical agent separation prevents consensus collapse:** Prompting a single LLM to generate multiple perspectives internally (Config 2) failed because attention heads collapse opposing views into an agreeable mean ($CRR = 38.0\%$). Physical separation with differentiated system prompts (Config 4) preserved legitimate dialectic tension ($CRR = 100.0\%$).
2. **Prerequisites and arithmetic belong in deterministic code:** LLM decoders cannot reliably verify topological dependencies. Coupling debate to a deterministic 42-node prerequisite graph reduced unsupported claims from 90.9% to 0.0%.
3. **Evaluation pipelines must validate their own judge:** Without human validation, an evaluation system can report artificially inflated groundedness scores. Restricting the judge to narrow, categorical decisions achieved $\kappa > 0.84$, whereas open-ended grading failed.

### Concrete Recommendations
1. *Enforce prerequisite DAG gates:* Block automated generation of career roadmaps when prerequisite reachability distance $\Delta > 0$.
2. *Isolate protected attributes:* Seal demographic variables in an audit vault; feed only technical skills and budget constraints to planning personas.
3. *Mandate zero-debt open access:* Direct vulnerable low-budget students exclusively toward free open courseware (MIT OCW, Stanford Online, CS50) rather than paid commercial certifications.
4. *Surface dispute trees:* Expose unresolvable trade-offs (Speed vs. Depth) to the user rather than forcing automated consensus.
5. *Provide interactive override:* Guarantee that students and counselors can adjust optimization weights dynamically.
6. *Validate automatic judges:* Regularly audit automated evaluation judges with blinded human counselor ratings.

---

## VIII. LIMITATIONS AND FUTURE WORK

The benchmark suite is bounded to 20 synthetic candidate profiles across computing careers; evaluating non-computing disciplines will require formal prerequisite ontologies for those domains. The personas currently share the Qwen 2.5 7B model family; future work will deploy cross-family triads (e.g., Qwen + Llama + Mistral) to eliminate shared training priors. Furthermore, the evaluation focused on single-turn consultation roadmaps; multi-turn longitudinal student tracking over semester-long periods remains an important avenue for future research.

---

## IX. CONCLUSION

We presented a local, reproducible multi-persona evaluation lab that tests student career-advisory agents across five core dimensions using a 42-node Neo4j prerequisite graph, Chroma vector retrieval, and a Streamlit dashboard. The proposed dialectic triad (Planner, Critic, Ethics-Reviewer) eliminates prerequisite sequence hallucinations (reducing unsupported claims from 90.9% to 0.0%), enforces demographic fairness parity ($J = 1.00$), and preserves critical student agency through an automated Cognitive Forcing Gate. By validating our automated judge against human counselor labels, we demonstrate that reliable algorithmic advisory requires deterministic graph grounding, adversarial persona friction, and human-in-the-loop control.

---

## REFERENCES

1. P. Liang, R. Bommasani, T. Lee, et al., "Holistic evaluation of language models," *Transactions on Machine Learning Research (TMLR)*, 2023.
2. M. T. Ribeiro, T. Wu, C. Guestrin, and S. Singh, "Beyond accuracy: Behavioral testing of NLP models with CheckList," in *Proc. 58th Annual Meeting of the Association for Computational Linguistics (ACL)*, 2020, pp. 4902–4912.
3. G. Irving, P. Christiano, and D. Amodei, "AI safety via debate," *arXiv:1805.00899*, 2018.
4. Y. Du, S. Li, A. Torralba, et al., "Improving factuality and reasoning in language models through multiagent debate," in *Proc. 41st International Conference on Machine Learning (ICML)*, 2024.
5. T. Liang, Z. He, W. Jiao, et al., "Encouraging divergent thinking in large language models through multi-agent debate," in *Proc. Conf. on Empirical Methods in Natural Language Processing (EMNLP)*, 2023, pp. 4392–4407.
6. A. Smit, N. A. Lee, and A. Ng, "Should we be going MAD? A critical look at multi-agent debate strategies," *arXiv:2311.17371*, 2024.
7. P. Lewis, E. Perez, A. Piktus, et al., "Retrieval-augmented generation for knowledge-intensive NLP tasks," in *Advances in Neural Information Processing Systems (NeurIPS 33)*, 2020, pp. 9459–9474.
8. S. Es, J. James, L. Espinosa Anke, and S. Schockaert, "RAGAS: Automated evaluation of retrieval augmented generation," in *Proc. 18th Conf. of the European Chapter of the ACL (EACL): System Demonstrations*, 2024, pp. 150–158.
9. ACM/IEEE Joint Task Force on Computing Curricula, *Computer Science Curricula 2023 (CS2023)*, ACM/IEEE Computer Society Press, 2023.
10. U.S. Department of Labor, "Occupational Information Network (O*NET) & Bureau of Labor Statistics (BLS) OEWS Taxonomy," 2024.
11. M. Sharma, M. Tong, T. Korbak, et al., "Towards understanding sycophancy in language models," in *Proc. International Conference on Learning Representations (ICLR)*, 2024.
12. S. C. Geyik, S. Ambler, and K. Kenthapadi, "Fairness-aware ranking in search & recommendation systems," in *Proc. 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining (KDD)*, 2019, pp. 2221–2231.
13. Z. Buçinca, M. B. Malaya, and K. Z. Gajos, "To trust or to think: Cognitive forcing functions in AI-assisted decision making," *Proc. ACM Human-Computer Interaction (PACMHCI / CSCW '21)*, vol. 5, no. CSCW1, art. 188, 2021.
14. M. Douze, A. Guzhva, C. Deng, et al., "The Faiss library," *arXiv:2401.08281*, 2024.
15. Qwen Team (A. Yang et al.), "Qwen2.5 technical report," *arXiv:2412.15115*, 2024.
16. Q. McNemar, "Note on the sampling error of the difference between correlated proportions or percentages," *Psychometrika*, vol. 12, no. 2, pp. 153–157, 1947.
17. B. Efron and R. J. Tibshirani, *An Introduction to the Bootstrap*, New York: Chapman & Hall, 1993.
18. S. Holm, "A simple sequentially rejective multiple test procedure," *Scandinavian Journal of Statistics*, vol. 6, no. 2, pp. 65–70, 1979.
19. J. Cohen, "A coefficient of agreement for nominal scales," *Educational and Psychological Measurement*, vol. 20, no. 1, pp. 37–46, 1960.
20. J. R. Landis and G. G. Koch, "The measurement of observer agreement for categorical data," *Biometrics*, vol. 33, no. 1, pp. 159–174, 1977.
