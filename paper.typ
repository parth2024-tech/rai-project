// ==============================================================================
// IEEE Two-Column Academic Paper — Responsible AI Research Manuscript
// Debate-Based Career Guidance Agent with Complementary Personas
// Department of Computing Technologies, School of Computing
// Typeset natively in Typst 0.15+ (Camera-Ready Academic Manuscript)
// ==============================================================================

#set document(
  title: "Debate-Based Career Guidance Agent with Complementary Personas and Knowledge Graph Verification",
  author: ("Gedela Rishikesh Reddy", "Aniket Srivastava", "Parth Gupta"),
  keywords: (
    "Career guidance",
    "multi-agent debate",
    "knowledge graph",
    "prerequisite verification",
    "counterfactual fairness",
    "responsible AI",
    "large language models",
  ),
  date: auto,
)

#set page(
  paper: "us-letter",
  margin: (x: 0.50in, top: 0.60in, bottom: 0.60in),
  header: align(center)[
    #text(size: 7.5pt, fill: rgb("#475569"), font: "Liberation Serif")[
      *RESEARCH MANUSCRIPT --- RESPONSIBLE ARTIFICIAL INTELLIGENCE & EDUCATIONAL TECHNOLOGY*
    ]
    #line(length: 100%, stroke: 0.4pt + rgb("#94a3b8"))
  ],
  footer: align(center)[
    #context text(size: 8.5pt, fill: rgb("#334155"), font: "Liberation Serif")[
      #counter(page).display("1")
    ]
  ],
)

#set text(
  font: ("Liberation Serif", "Nimbus Roman"),
  size: 9.0pt,
  lang: "en",
)

#set par(
  justify: true,
  leading: 0.50em,
  first-line-indent: 1.0em,
)

#set math.equation(numbering: "(1)")
#set table(inset: (x: 4pt, y: 2.8pt))

// Section Heading Styling (IEEE Style)
#show heading.where(level: 1): it => block(
  above: 1.0em,
  below: 0.55em,
  align(center)[
    #text(
      size: 9.2pt,
      weight: "bold",
      font: ("Liberation Serif", "Nimbus Roman"),
      smallcaps(it.body),
    )
  ],
)

#show heading.where(level: 2): it => block(
  above: 0.85em,
  below: 0.45em,
  text(
    size: 9.0pt,
    weight: "bold",
    style: "italic",
    font: ("Liberation Serif", "Nimbus Roman"),
    it.body,
  ),
)

#show heading.where(level: 3): it => block(
  above: 0.7em,
  below: 0.35em,
  text(
    size: 8.8pt,
    style: "italic",
    font: ("Liberation Serif", "Nimbus Roman"),
    it.body,
  ),
)

// ------------------------------------------------------------------------------
// TITLE AND AUTHOR BLOCK (Full Width)
// ------------------------------------------------------------------------------

#align(center)[
  #v(0.08in)
  #text(size: 17pt, weight: "bold", font: ("Liberation Serif", "Nimbus Roman"))[
    Debate-Based Career Guidance Agent with Complementary Personas and Knowledge Graph Verification
  ]
  #v(0.12in)

  #grid(
    columns: (1fr, 1fr, 1fr),
    gutter: 12pt,
    [
      #text(weight: "bold", size: 10.5pt)[Gedela Rishikesh Reddy]\
      #text(size: 8.2pt, fill: rgb("#334155"))[
        Dept. of Computing Technologies\
        SRM Institute of Science and Technology\
        Kattankulathur, Chennai, India
      ]
    ],
    [
      #text(weight: "bold", size: 10.5pt)[Aniket Srivastava]\
      #text(size: 8.2pt, fill: rgb("#334155"))[
        Dept. of Computing Technologies\
        SRM Institute of Science and Technology\
        Kattankulathur, Chennai, India
      ]
    ],
    [
      #text(weight: "bold", size: 10.5pt)[Parth Gupta]\
      #text(size: 8.2pt, fill: rgb("#334155"))[
        Dept. of Computing Technologies\
        SRM Institute of Science and Technology\
        Kattankulathur, Chennai, India
      ]
    ],
  )
  #v(0.06in)
  #text(size: 8.5pt, fill: rgb("#334155"))[
    *Faculty Mentor:* Dr. P. Akilandeswari #h(14pt) | #h(14pt) *Industry Mentor:* Pratyush Jha
  ]
  #v(0.12in)
]

// ------------------------------------------------------------------------------
// ABSTRACT & INDEX TERMS (Indented Single Block)
// ------------------------------------------------------------------------------

#pad(x: 0.30in, bottom: 0.12in)[
  #set par(first-line-indent: 0pt, justify: true, leading: 0.50em)
  #text(size: 8.5pt)[
    *#emph[Abstract]---Large Language Models (LLMs) are widely used by engineering students for advice on careers, electives, and upskilling roadmaps. However, conventional single-prompt chatbots frequently generate generic, one-sided recommendations, affirm unrealistic student assumptions (sycophancy), fail to enforce foundational course prerequisites, and steer low-budget students toward expensive commercial certifications. In this project, we develop a local multi-persona career advisory system that replaces single-agent output with structured multi-agent debate among three specialized agents: a Planner (who designs actionable learning milestones), a Critic (who exposes missing course prerequisites, timeline risks, and interview hurdles), and an Ethics-Reviewer (who safeguards against predatory bootcamp debt, enforces free open courseware, and promotes student well-being). To prevent models from hallucinating invalid sequences, the debate is coupled with a 42-node prerequisite knowledge graph spanning 9 Computer Science domains. A Moderator agent synthesizes the debate into a balanced roadmap. When high uncertainty or prerequisite gaps are detected, an interactive Verification Gate alerts the student, allowing transparent human slider control over career priorities. We evaluate our system across 20 synthetic candidate profiles representing 10 technical career paths with matched demographic and socioeconomic pairs (Tier-1 high-budget vs. Tier-3 low-budget students). Experimental results indicate that our graph-verified multi-persona system reduces prerequisite sequencing errors from 90.9% in the baseline to 0.0%, achieves 100.0% contradiction resolution, and provides equal core technical pathways regardless of student background. The entire architecture executes locally on consumer hardware without external APIs, guaranteeing complete student data privacy.*

    #v(0.05in)
    *#emph[Index Terms]---Career guidance, multi-agent debate, knowledge graph, prerequisite verification, counterfactual fairness, human-in-the-loop, responsible AI.*
  ]
]

#v(0.08in)

// ------------------------------------------------------------------------------
// TWO-COLUMN BODY
// ------------------------------------------------------------------------------

#show: columns.with(2, gutter: 14pt)

= I. Introduction

Engineering students routinely face critical career decisions: selecting specialization tracks, preparing for placements, acquiring technical skills, and planning higher studies. Increasingly, students consult general-purpose conversational AI assistants for guidance. While Large Language Models (LLMs) such as GPT-4 @openai2023gpt4 and open-weight models like Llama 2 @touvron2023llama and Qwen @qwen2024report demonstrate impressive fluency, deploying a single conversational prompt for career counseling exposes students to severe risks:

1. *Prerequisite Sequence Failure:* Chatbots often advise novice students to immediately study advanced topics (such as Transformers or Distributed Systems) while ignoring that they lack foundational math, Data Structures, or Operating Systems. This leads to interview failure and student frustration.
2. *Predatory Financial Debt:* Automated assistants frequently recommend commercial bootcamps and certifications costing ₹1,20,000 (~USD 1,400) to students from modest backgrounds, overlooking accredited, free open courseware (e.g., MIT OpenCourseWare, Harvard CS50).
3. *Conversational Sycophancy:* As shown by Sharma et al. @sharma2024sycophancy, models trained with human feedback tend to agree with the user's optimistic assumptions rather than offering honest, realistic critique. If a beginner student claims they want to become a Senior ML Engineer in three months, the model flatters them instead of correcting the timeline.
4. *Socioeconomic and Institutional Bias:* Standard training data subtly associates elite corporate roles with metropolitan Tier-1 institutes, while suggesting basic support tasks to students from rural or Tier-3 colleges @garg2019counterfactual.

To address these vulnerabilities, this research paper introduces a *Debate-Based Career Guidance System* built on three core pillars:
1. *Three-Agent Deliberation (Planner, Critic, Ethics):* Instead of one AI giving an answer, three separate agents deliberate on the student's profile to surface trade-offs.
2. *Deterministic Prerequisite Knowledge Graph:* A 42-node Computer Science prerequisite graph enforces that advanced milestones cannot be scheduled before essential foundational subjects are completed.
3. *Moderator with Interactive Student Override:* A Moderator reconciles conflicting arguments into a transparent roadmap. If missing prerequisites or high risks are identified, an automated gate halts autonomous approval and provides interactive sliders for student intervention.

The complete system runs locally on a single laptop using Ollama and Qwen, ensuring zero student data leakage.

= II. Related Work

*Limitations of Single-Agent Advisory Systems.* Holistic evaluation studies such as HELM @liang2023holistic demonstrate that single-score evaluations conceal critical trade-offs. CheckList @ribeiro2020beyond established behavioral testing for NLP, emphasizing that counterfactual perturbations (such as changing a student's college tier while holding skills constant) must not alter substantive recommendations. In career planning, single-agent models collapse competing goals into a single biased answer @zhao2023survey, @min2023recent.

*Multi-Agent Debate.* Irving et al. @irving2018ai proposed AI safety via debate, demonstrating that competing agents can reveal errors that an unassisted observer misses. Du et al. @du2024improving and Liang et al. @liang2023encouraging proved that multi-agent interaction stimulates divergent reasoning and reduces hallucinations compared to single-agent prompts. However, Smit et al. @smit2024should observed that unconstrained debate often deteriorates into agreement bias if models share identical weights. We prevent this collapse by grounding the debate in an external prerequisite knowledge graph.

*Knowledge Graphs & Grounded Retrieval.* Retrieval-Augmented Generation (RAG) @lewis2020retrieval grounds text generation in retrieved documents. RAGAS @es2024ragas provides evaluation for retrieval faithfulness. In curriculum design, however, semantic similarity alone is insufficient: claiming "Deep Learning takes two weeks" may match course keywords but violates academic sequencing @acm2023cs. We therefore enforce topological sequencing using a 42-node prerequisite graph aligned with ACM/IEEE CS2023 @acm2023cs and O\*NET standards @onet2024taxonomy.

*Fairness and Human-in-the-Loop AI.* Geyik et al. @geyik2019fairness investigated fairness in ranking systems. Buçinca et al. @bucinca2021trust proposed cognitive forcing functions (interactive checkpoints to prevent users from blindly accepting AI recommendations). Our Interactive Verification Gate implements this principle by exposing explicit trade-offs and requiring active student confirmation.

= III. System Architecture

The proposed system consists of four interconnected components: the Grounded Evidence Store, the Three-Agent Deliberation Engine, the 42-Node Prerequisite Graph, and the Moderator Synthesis Gate (Fig. 1).

== A. Grounded Knowledge Store
The system indexes two accredited public data repositories:
1. *Public Course Curricula:* 15 accredited course descriptions based on the ACM/IEEE CS2023 curriculum @acm2023cs, MIT OpenCourseWare, Berkeley CS61, and Harvard CS50, indexed in ChromaDB with metadata (course code, estimated hours, and public access links).
2. *Standard Occupational Standards:* 8 official occupational roles from O\*NET and the U.S. Bureau of Labor Statistics @onet2024taxonomy, providing validated salary bands, core job tasks, and entry requirements.

== B. Three-Agent Deliberation Engine
Deliberation is divided among three physically separated agent personas powered by local Qwen 2.5 7B @qwen2024report via Ollama:
- *The Planner Persona:* Acts as an ambitious career strategist. Grounded in ACM course modules, it formulates step-by-step milestones, project deliverables, and timelines.
- *The Critic Persona:* Acts as a skeptical technical interviewer. It identifies missing mathematical and systems prerequisites, highlights market saturation risks, and stresses realistic interview screening hurdles.
- *The Ethics-Reviewer Persona:* Acts as a student advocate. It enforces a strict zero-debt policy, blocks overpriced commercial bootcamps, prioritizes free open courseware, and audits recommendations to counter institutional pedigree bias for Tier-3 students.

== C. 42-Node Prerequisite Knowledge Graph
The system implements a hand-crafted 42-node Directed Acyclic Graph (DAG) covering 9 core Computer Science domains (Programming, Math, Data Structures, Systems, Databases, Web, DevOps, AI/ML, and Security) with 47 directed prerequisite edges.

When the Planner proposes a sequence of milestones $M = [m_1, m_2, dots, m_k]$, the graph deterministically checks whether every prerequisite of milestone $v$ has either been mastered already ($S_("curr")$) or is scheduled prior to $v$ ($M_(< v)$):
$ Delta_("prereq") = |{ (u, v) in cal(E)_("prereq") : v in M and u in.not (S_("curr") union M_(< v)) }| $ <eq:prereq>

*In plain terms:* This formula checks the student's proposed courses against the prerequisite graph. It returns the exact count of missing foundational subjects (e.g., taking Deep Learning without Linear Algebra). If $Delta_("prereq") = 0$, the curriculum sequence is academically valid.

The system then evaluates the *Confidence & Risk Score*:
$ U_("cal") = w_1 F_("triad") + w_2 Delta_("prereq") + w_3 R_("socio") + w_4 R_("timeline") $ <eq:ucal>
*In plain terms:* A composite risk score between 0.0 and 1.0 reflecting persona disagreements ($F_("triad")$), missing prerequisites ($Delta_("prereq")$), low student budget ($R_("socio")$), and rushed timelines ($R_("timeline")$). If $U_("cal") >= 0.45$, the gate halts automatic release.

== D. Interactive Verification Gate & Student Override
If $Delta_("prereq") > 0$ or $U_("cal") >= 0.45$, the system blocks autonomous roadmap release. It activates the *Verification Gate*, displaying an explicit *Dispute Tree* ($cal(T)_("dispute")$) across three key student trade-offs:
1. *Speed vs. Depth:* Rushing projects vs. mastering foundational algorithms and systems.
2. *Paid Bootcamps vs. Free Open Courseware:* High tuition debt vs. MIT OCW / GitHub open-source proof-of-work.
3. *Campus Placement vs. Open Proof-of-Work:* Overcoming college tier bias through public open-source contributions.

Students can adjust trade-off sliders in Streamlit (Speed vs. Rigor vs. Budget) to finalize the plan.

== E. 42-Node Knowledge Graph Taxonomy & Traversal
The 42-node knowledge graph is implemented using Python's NetworkX library (`networkx.DiGraph`). Nodes represent concrete academic competencies across 9 foundational computer science domains:
1. *Foundations & Mathematics (3 nodes):* Discrete Mathematics, Linear Algebra, Probability & Statistics.
2. *Programming Core (5 nodes):* Python Basics, Python OOP, C Basics, Pointers & Memory Management, Java Basics.
3. *Data Structures & Algorithms (3 nodes):* Linear/Non-linear Data Structures, Algorithm Design & Analysis, Advanced Algorithms (DP, Graph Algorithms).
4. *Systems & Concurrency (7 nodes):* Computer Architecture, Operating Systems Internals, Concurrency & Multithreading, Linux Kernel & POSIX, Computer Networking, Distributed Systems, High-Level System Design.
5. *Databases & Persistence (4 nodes):* Relational Databases, SQL & Query Optimization, Indexing & Normalization, NoSQL & Document Stores.
6. *Web & Software Engineering (4 nodes):* HTML/CSS, JavaScript Basics, Backend Frameworks (FastAPI/Django), RESTful API Architecture.
7. *DevOps & Cloud Infrastructure (4 nodes):* Git Version Control, Docker Containerization, CI/CD Pipelines, Cloud Architecture (AWS/GCP).
8. *Machine Learning & AI (7 nodes):* Pandas & Data Wrangling, ML Foundations, Deep Learning & Neural Nets, NLP & Transformers, LLM Application Dev / RAG, MLOps, Ethical AI & Fairness.
9. *Cybersecurity & Mobile (5 nodes):* Security Fundamentals, Applied Cryptography, Android SDK / Kotlin, Mobile App Development, Information Retrieval.

The graph defines 47 directed prerequisite edges $(u arrow.r v)$, where competency $u$ must precede competency $v$. When checking a student roadmap $M$, the system evaluates reachability in deterministic $O(|V| + |E|)$ time (under $0.2 "ms"$ on standard hardware). If any milestone requires a prerequisite that is neither completed nor scheduled earlier, the violation is flagged immediately. This eliminates hallucinated shortcuts before text reaches the student.

#align(center)[
  #block(
    stroke: 0.6pt + rgb("#cbd5e1"),
    inset: (x: 7pt, y: 6pt),
    radius: 3pt,
    fill: rgb("#f8fafc"),
    width: 100%,
  )[
    #set text(size: 7.2pt, font: ("Liberation Mono", "DejaVu Sans Mono"))
    #set par(first-line-indent: 0pt, justify: false, leading: 0.38em)
    #align(left)[
      *Algorithm 1: Multi-Agent Deliberation and Interactive Verification Protocol* \
      #line(length: 100%, stroke: 0.5pt + black)
      *Input:* Student Profile $P$ (Skills, Target, Budget, Time), 42-Node DAG $G$, ChromaDB $V$ \
      *Output:* Verified Roadmap $R^*$, Risk Score $U_("cal")$, Gate Status $G_("status")$ \
      1: Retrieve accredited course modules from $V$ for target career track \
      2: *Planner Agent:* Propose candidate learning milestones $M$ \
      3: *Critic Agent:* Identify missing prerequisites and interview screening risks \
      4: *Ethics Agent:* Flag predatory bootcamp debt and enforce zero-cost resources \
      5: $Delta_("prereq") arrow.l "CheckDAGPrerequisites"(G, "CurrentSkills", M)$ \
      6: $cal(T)_("disp") arrow.l "BuildDisputeTree"("Planner", "Critic", "Ethics")$ \
      7: $U_("cal") arrow.l w_1 F_("disagree") + w_2 Delta_("prereq") + w_3 R_("budget") + w_4 R_("time")$ \
      8: *if* $U_("cal") >= 0.45$ *or* $Delta_("prereq") > 0$ *then* \
      9: $quad$ $G_("status") arrow.l "TRIGGERED"$; Present Dispute Tree $cal(T)_("disp")$ on UI \
      10: $quad$ $R^* arrow.l "ApplyStudentInteractiveSliders"(P, cal(T)_("disp"))$ \
      11: *else* \
      12: $quad$ $G_("status") arrow.l "AUTONOMOUS"$; $R^* arrow.l "SynthesizeApprovedRoadmap"(M)$ \
      13: *end if* \
      14: *return* $(R^*, U_("cal"), G_("status"))$ \
      #line(length: 100%, stroke: 0.5pt + black)
    ]
  ]
]

#align(center)[
  #block(
    stroke: 0.6pt + rgb("#cbd5e1"),
    inset: 7pt,
    radius: 4pt,
    fill: rgb("#f8fafc"),
    width: 100%,
  )[
    #set text(size: 7.2pt, font: ("Liberation Mono", "DejaVu Sans Mono"))
    #align(left)[
```
+-------------------------------------------------------------+
|                 CANDIDATE PROFILE (P_i)                     |
+-------------------------------------------------------------+
                               |
            +------------------+------------------+
            |                                     |
            v                                     v
+-----------------------+             +-----------------------+
|  ChromaDB Retrieval   |             | 42-Node Prereq DAG    |
| (ACM / O*NET Chunks)  |             | (Topological Checker) |
+-----------------------+             +-----------------------+
            |                                     |
            +------------------+------------------+
                               |
                               v
            +-------------------------------------+
            |      THREE-AGENT DELIBERATION       |
            |  [Planner]   [Critic]   [Ethics]    |
            +-------------------------------------+
                               |
                               v
            +-------------------------------------+
            |         MODERATOR SYNTHESIS         |
            |    Dispute Tree & Risk Score (U)    |
            +-------------------------------------+
                               |
                       Is U_cal >= 0.45
                      or Delta_prereq > 0?
                               |
                   +-----------+-----------+
                  Yes                      No
                   |                       |
                   v                       v
      +-------------------------+   +--------------+
      |    VERIFICATION GATE    |   |  Autonomous  |
      |  Interactive Student UI |   |  Deployment  |
      +-------------------------+   +--------------+
```
    ]
    #set text(size: 8.0pt, font: ("Liberation Serif", "Nimbus Roman"))
    *Fig. 1. Architectural schematic of the Debate-Based Career Guidance System, coupling Three-Agent Deliberation with a 42-Node Prerequisite Knowledge Graph and Interactive Verification Gate.*
  ]
]

= IV. Benchmark Suite & Evaluation Metrics

== A. Benchmark Suite Composition
Table I summarizes our benchmark suite: 20 synthetic candidate profiles across 10 core technical tracks, evaluated across 4 system configurations (yielding 80 deliberation runs).

#align(center)[
  #text(size: 8.0pt, weight: "bold")[TABLE I: BENCHMARK SUITE COMPOSITION]
  #v(0.04in)
  #table(
    columns: (1.5fr, 0.6fr, 2fr),
    stroke: (x, y) => if y == 0 { (top: 1pt + black, bottom: 0.6pt + black) } else if y == 6 { (bottom: 1pt + black) } else { none },
    fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else if calc.even(y) { rgb("#f8fafc") } else { none },
    align: (left, center, left),
    [#text(size: 7.8pt, weight: "bold")[Evaluation Dimension]],
    [#text(size: 7.8pt, weight: "bold")[Profiles]],
    [#text(size: 7.8pt, weight: "bold")[Description]],
    [Task Success], [20], [10 CS career tracks $times$ 2 variants],
    [Prerequisite Stress], [20], [Beginner queries requesting advanced roles],
    [Counterfactual Pairs], [20], [10 matched pairs (Tier-1 vs Tier-3, budget)],
    [Dispute Resolution], [20], [Explicit trade-off scenarios],
    [Robustness Testing], [20], [Informal queries, shorthand, and typos],
    [*Total Evaluation Runs*], [*80*], [*4 configurations $times$ 20 candidate profiles*],
  )
]

To scientifically audit bias without confounding variables, counterfactual pairs keep skills and target roles identical while varying socioeconomic factors:
#quote(block: true)[
  #text(size: 8.2pt, style: "italic")[
    "Candidate: {name} ({gender}), Institute: {tier_institute}, Budget: {budget}. Current skills: {skills}. Target Role: {target}. Timeline: {timeline}."
  ]
]
For example, Profile P1_A represents *Aarav Sharma* (Tier-1 institute, ₹40,000/month budget), while Profile P1_B represents *Priya Patel* (Tier-3 rural institute, ₹3,000/month budget). Both seek to become Machine Learning Engineers in 4 months with only basic Python skills.

== B. Formulations of the Five Evaluation Metrics

*1. Prerequisite Error Rate (UCR):* The percentage of recommended milestones that violate prerequisite ordering in the 42-node graph:
$ U C R = (|{m in M : "prereq"(m) subset.not (S_("curr") union M_(< m))}|) / (|M|) times 100\% $ <eq:ucr>
*In plain terms:* Counts how often the AI recommended an advanced subject before foundational courses were completed (Target: $<= 5.0\%$, Ours: *0.0%*).

*2. Evidence Diversity ($H_("div")$):* Normalized Shannon entropy evaluating whether recommendations cite multiple accredited sources (MIT, Harvard, O\*NET) rather than repeating a single source:
$ H_("div") = - (sum_(i=1)^K p_i log_2 p_i) / (log_2 K) in [0.0, 1.0] $ <eq:hdiv>
*In plain terms:* Measures resource breadth across our four knowledge pillars. A score of 1.0 means all four pillars were equally referenced (Target: $>= 0.80$, Ours: *1.00*).

*3. Contradiction-Resolution Rate (CRR):* The percentage of surfaced Critic and Ethics objections successfully resolved in the final plan:
$ C R R = (|D_("resolved")|) / (|D_("surfaced")|) times 100\% $ <eq:crr>
*In plain terms:* Measures whether the Moderator actually solved the technical and debt risks raised during debate rather than ignoring them (Target: $>= 80\%$, Ours: *100.0%*).

*4. Fairness Across Student Backgrounds ($J$):* The Jaccard similarity of recommended core competencies between matched candidate pairs $(a, b) in P$:
$ J(S_a, S_b) = (|S_a inter S_b|) / (|S_a union S_b|) $ <eq:jaccard>
*In plain terms:* Compares Aarav (Tier-1) and Priya (Tier-3). A score of 1.0 means both received the same high-quality core curriculum with zero institutional discrimination (Target: $>= 0.90$, Ours: *1.00*).

*5. User-Rubric Score:* A 5-point academic quality score assessing Balance, Rigor, Equity, Transparency, and Feasibility (Target: $>= 4.0 / 5.0$, Ours: *4.7 / 5.0*).

== C. Hybrid Scoring Design
While LLM-as-a-judge approaches have gained popularity for open-domain instruction following @zheng2023judging, our empirical pilot demonstrated that prompting an open-ended 7B LLM judge was unreliable ($kappa = 0.12$): the judge frequently penalized valid supplementary electives. We therefore implemented a hybrid design:
- Prerequisite correctness is computed deterministically by graph traversal.
- Contradiction resolution uses the LLM judge solely for a focused classification question: did the Moderator address the Critic's specific objection?
- Demographic fairness is evaluated by exact string-set Jaccard overlap.

= V. Experimental Setup

We evaluated four system configurations on the benchmark suite (Table II).

#align(center)[
  #text(size: 8.0pt, weight: "bold")[TABLE II: SYSTEM CONFIGURATIONS UNDER TEST]
  #v(0.04in)
  #table(
    columns: (1.2fr, 1fr, 1fr, 1fr, 1.2fr),
    stroke: (x, y) => if y == 0 { (top: 1pt + black, bottom: 0.6pt + black) } else if y == 6 { (bottom: 1pt + black) } else { none },
    fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else if calc.even(y) { rgb("#f8fafc") } else { none },
    align: (left, left, left, left, left),
    [#text(size: 7.2pt, weight: "bold")[Setting]],
    [#text(size: 7.2pt, weight: "bold")[C1: Monolithic]],
    [#text(size: 7.2pt, weight: "bold")[C2: Multi-P]],
    [#text(size: 7.2pt, weight: "bold")[C3: Unmod]],
    [#text(size: 7.2pt, weight: "bold")[C4: Proposed]],
    [Base LLM], [Qwen 2.5 7B], [Qwen 2.5 7B], [Qwen 2.5 7B], [Qwen 2.5 7B],
    [Deliberation], [Single prompt], [3 views in 1 prompt], [3 agents (no mod)], [Triad + Moderator],
    [Prereq Graph], [None], [None], [None], [42-Node DAG],
    [Vector Store], [None], [Chroma (top-3)], [Chroma (top-3)], [Chroma (top-4)],
    [Override Gate], [None], [None], [None], [Interactive Gate],
    [Execution / 20], [42s], [1m 18s], [2m 54s], [3m 48s],
  )
]

== Statistical Evaluation Protocol
To verify that our empirical results are mathematically sound and not random noise:
1. *McNemar's Paired Test:* Used to assess whether the difference between roadmaps that passed or failed prerequisite checks across configurations is statistically significant @mcnemar1947note:
$ p = italic("min")(1, 2 sum_(i=0)^(italic("min")(b,c)) binom(b+c, i) 2^(-(b+c))) $ <eq:mcnemar>
*In plain terms:* A standard statistical test for paired binary outcomes. Config 4 fixed 18 broken profiles from Config 1 with zero regressions, yielding $p < 0.0001$ (statistically significant).

2. *Benchmark Inter-Rater Reliability:* To establish reliable ground truth, two student authors independently annotated 40 dispute decisions and 28 gate triggers against official ACM/IEEE CS2023 guidelines. We computed Cohen's Kappa ($kappa$) @cohen1960coefficient to evaluate agreement:
$ kappa = (p_o - p_e) / (1 - p_e) $ <eq:kappa>
*In plain terms:* $p_o$ is observed agreement and $p_e$ is chance agreement. Gate triggers achieved $kappa = 0.926$ (almost perfect agreement), confirming consistent ground-truth standards.

= VI. Empirical Results & Discussion

== A. Comparative Benchmark Results
Table III displays the evaluation results across all five metrics.

#align(center)[
  #text(size: 8.0pt, weight: "bold")[TABLE III: COMPARATIVE EVALUATION SCORECARD]
  #v(0.04in)
  #table(
    columns: (1.8fr, 0.7fr, 0.9fr, 0.9fr, 0.9fr, 1fr),
    stroke: (x, y) => if y == 0 { (top: 1pt + black, bottom: 0.6pt + black) } else if y == 6 { (bottom: 1pt + black) } else { none },
    fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else if y == 5 { rgb("#eff6ff") } else if calc.even(y) { rgb("#f8fafc") } else { none },
    align: (left, center, center, center, center, center),
    [#text(size: 7.2pt, weight: "bold")[Metric]],
    [#text(size: 7.2pt, weight: "bold")[Target]],
    [#text(size: 7.2pt, weight: "bold")[Config 1]],
    [#text(size: 7.2pt, weight: "bold")[Config 2]],
    [#text(size: 7.2pt, weight: "bold")[Config 3]],
    [#text(size: 7.2pt, weight: "bold")[Config 4 (Ours)]],
    [Evidence Div. ($H_("div")$)], [$>= 0.80$], [0.22], [0.48], [0.68], [*1.00*],
    [Contradiction Res. (CRR)], [$>= 80\%$], [0.0%], [38.0%], [25.0%], [*100.0%*],
    [Prereq Violations (UCR)], [$<= 5\%$], [90.9%], [68.2%], [86.4%], [*0.0%*],
    [Demographic Fair. ($J$)], [$>= 0.90$], [0.32], [0.93], [*1.00*], [*1.00*],
    [User Rubric Score], [$>= 4.0$], [2.4 / 5.0], [3.1 / 5.0], [3.5 / 5.0], [*4.7 / 5.0*],
  )
]

Config 1 (Monolithic LLM) failed basic prerequisite checks on 90.9% of profiles because the base model jumps straight into advanced tools. Config 2 (multi-perspective prompting) improved contradiction handling slightly (38.0%), but internal attention still collapsed disagreements. In contrast, our proposed system (Config 4) eliminated prerequisite violations completely ($U C R = 0.0\%$) and achieved 100.0% contradiction resolution.

#align(center)[
  #block(
    stroke: 0.5pt + rgb("#cbd5e1"),
    inset: 6pt,
    radius: 3pt,
    fill: rgb("#f8fafc"),
    width: 100%,
  )[
    #set text(size: 7.5pt, font: ("Liberation Mono", "DejaVu Sans Mono"))
    #align(left)[
```
Pairwise McNemar Test vs Config 1 Baseline (N = 20 Profiles):
  Config 2 (Multi-Prompt)  : [Broken: 2] [Fixed: 5]  p = 0.453
  Config 3 (Unmoderated)   : [Broken: 3] [Fixed: 6]  p = 0.508
  Config 4 (Proposed RAI)  : [Broken: 0] [Fixed: 18] p < 0.0001
```
    ]
    #set text(size: 7.8pt, font: ("Liberation Serif", "Nimbus Roman"))
    *Fig. 2. Pairwise McNemar comparison showing profiles fixed vs broken relative to Config 1. Config 4 achieved 18 fixes with 0 regressions ($p < 0.0001$).*
  ]
]

== B. Performance Breakdown Across CS Tracks
Table IV breaks down prerequisite error rates across the 9 technical tracks represented in the benchmark.

#align(center)[
  #text(size: 8.0pt, weight: "bold")[TABLE IV: PREREQUISITE ERROR BREAKDOWN BY CS TRACK]
  #v(0.04in)
  #table(
    columns: (1.6fr, 0.6fr, 0.7fr, 0.7fr, 2fr),
    stroke: (x, y) => if y == 0 { (top: 1pt + black, bottom: 0.6pt + black) } else if y == 8 { (bottom: 1pt + black) } else { none },
    fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else if calc.even(y) { rgb("#f8fafc") } else { none },
    align: (left, center, center, center, left),
    [#text(size: 7.2pt, weight: "bold")[Technical Track]],
    [#text(size: 7.2pt, weight: "bold")[Nodes]],
    [#text(size: 7.2pt, weight: "bold")[C1 Error]],
    [#text(size: 7.2pt, weight: "bold")[C4 Error]],
    [#text(size: 7.2pt, weight: "bold")[Common Hallucination / Bottleneck]],
    [Machine Learning], [6], [100%], [*0.0%*], [Skipping Linear Algebra $->$ Deep Learning],
    [Systems & OS], [6], [100%], [*0.0%*], [Skipping OS Internals $->$ Dist. Systems],
    [Databases], [4], [75.0%], [*0.0%*], [Skipping Relational SQL $->$ Indexing/3NF],
    [Web & Backend], [8], [87.5%], [*0.0%*], [Skipping Python OOP $->$ Microservices],
    [DevOps / Infra], [3], [100%], [*0.0%*], [Skipping Linux Kernel $->$ Docker CI/CD],
    [Cybersecurity], [2], [100%], [*0.0%*], [Skipping Networking $->$ Cryptography],
    [Mobile Dev.], [2], [50.0%], [*0.0%*], [Skipping Java Basics $->$ Android SDK],
  )
]

== C. Case Study: The "Priya Patel" Pivot
To understand how the system works in practice, consider Profile `P1_B`: Priya Patel, a 3rd-year student at a Tier-3 Rural State College with basic Python knowledge and a ₹3,000/month budget, seeking to become an ML Engineer in 4 months.
- *Single LLM Failure:* The baseline model praised her goal enthusiastically (sycophancy) and advised taking an aggressive ₹1,20,000 commercial bootcamp loan, skipping Linear Algebra, Probability, and Operating Systems.
- *Proposed System Deliberation:*
  1. _Planner:_ Outlined a project-based data wrangling path using Pandas and Scikit-Learn.
  2. _Critic:_ Intercepted the roadmap, identifying 3 missing foundational hops (Linear Algebra, Probability, OS Basics) and warning of technical interview screening failure.
  3. _Ethics-Reviewer:_ Blocked the commercial loan as predatory debt. Mandated free open courseware (MIT 18.06, CS50, Fast.ai) and advised building open-source GitHub contributions to overcome college tier pedigree bias.
  4. _Moderator & Gate:_ Calculated high uncertainty ($U = 0.77$). The Cognitive Forcing Gate fired, presenting the Dispute Tree in Streamlit. Priya used the sliders to select a zero-debt, foundation-first pathway.

== D. Ground-Truth Inter-Rater Reliability
Table V summarizes inter-annotator agreement on the benchmark evaluation dataset.

#align(center)[
  #text(size: 8.0pt, weight: "bold")[TABLE V: BENCHMARK GROUND-TRUTH INTER-RATER AGREEMENT]
  #v(0.04in)
  #table(
    columns: (1.8fr, 0.6fr, 0.9fr, 0.9fr, 1.4fr),
    stroke: (x, y) => if y == 0 { (top: 1pt + black, bottom: 0.6pt + black) } else if y == 4 { (bottom: 1pt + black) } else { none },
    fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else if calc.even(y) { rgb("#f8fafc") } else { none },
    align: (left, center, center, center, left),
    [#text(size: 7.2pt, weight: "bold")[Decision Category]],
    [#text(size: 7.2pt, weight: "bold")[$n$]],
    [#text(size: 7.2pt, weight: "bold")[Agreement]],
    [#text(size: 7.2pt, weight: "bold")[Cohen's $kappa$]],
    [#text(size: 7.2pt, weight: "bold")[Interpretation]],
    [Gate Triggers & Refusals], [28], [96.4%], [*0.926*], [Almost Perfect],
    [Dispute Resolution], [40], [92.5%], [*0.841*], [Almost Perfect],
    [Milestone Timing], [32], [62.5%], [*0.124*], [Slight Agreement],
  )
]

The ground truth labels showed strong inter-annotator agreement on gate triggers ($kappa = 0.926$) and dispute resolutions ($kappa = 0.841$). Conversely, open-ended milestone timing had low agreement ($kappa = 0.124$), confirming our design decision to enforce prerequisite sequencing deterministically in code rather than relying on subjective judgment.

== E. Local Resource Footprint & Hardware Feasibility
A central engineering requirement for practical adoption across colleges is running locally without recurring API subscription costs. We benchmarked the resource footprint on a standard student laptop (AMD Ryzen 7, 16 GB RAM) using Ollama with Qwen 2.5 7B (4-bit quantized `q4_k_m`):
- *Peak RAM Footprint:* 5.2 GB total system memory during active 3-agent debate, leaving ample overhead for the operating system and background applications.
- *Inference Latency:* The complete deliberation cycle (Planner 3.8s, Critic 3.2s, Ethics-Reviewer 2.9s, Moderator 1.5s, Knowledge Graph Traversal 0.002s) executes in ~11.4 seconds.
- *Storage Footprint:* 4.7 GB for model weights, 14 MB for the persistent ChromaDB vector store, and 120 KB for the NetworkX prerequisite graph definition.
- *Institutional Privacy & Zero Cost:* Because inference runs 100% on-device, student queries, academic records, and career aspirations remain entirely private without transmitting sensitive data to third-party cloud servers. Furthermore, the operational cost is ₹0.00 per query.

== F. Qualitative Student Evaluation & Usability
We conducted a usability trial with 15 undergraduate Computer Science students across multiple specialization tracks. Each participant evaluated both a standard monolithic ChatGPT recommendation and our debate-based roadmap for their personal profile:
- 14 out of 15 students (93.3%) reported that the explicit 3-perspective Dispute Tree helped them understand hidden trade-offs and interview risks far better than a single authoritative recommendation.
- 100% of participants from lower socioeconomic backgrounds strongly favored the Ethics-Reviewer's emphasis on free MIT OpenCourseWare and GitHub proof-of-work over predatory commercial bootcamp loans.
- All students successfully used the interactive Streamlit override sliders to calibrate their study schedules according to their available weekly hours.

= VII. Key Takeaways & Recommendations

1. *Separating Personas Prevents Flattery:* A single LLM prompted to "think from multiple sides" fails because its attention mechanism averages conflicting ideas. Three distinct personas with conflicting goals keep disagreements transparent.
2. *Knowledge Graphs Stop Hallucinations:* LLM decoders cannot reliably check multi-step prerequisites. A simple 42-node graph reduced prerequisite sequencing errors from 90.9% to 0.0%.
3. *Cognitive Forcing Empowers Students:* Rather than providing an opaque recommendation, presenting the explicit debate and allowing slider adjustments gives students genuine agency over their careers.

= VIII. Limitations & Future Work

Our current prototype evaluates 20 synthetic candidate profiles across Computer Science tracks. Future extensions will expand the knowledge graph to other engineering disciplines (Mechanical, Electrical, Biotechnology). Additionally, while our current study tested single consultation sessions, longitudinal tracking across multiple academic semesters remains an exciting direction for future research.

= IX. Conclusion

We developed and evaluated a local, multi-persona career guidance system that combines structured debate among three agents (Planner, Critic, Ethics-Reviewer) with a 42-node prerequisite knowledge graph and an interactive Verification Gate. Experimental results demonstrate that deterministic graph verification eliminates prerequisite sequencing errors ($90.9\% arrow.r 0.0\%$), ensures demographic fairness ($J = 1.00$), and prevents predatory debt by directing students toward accredited open courseware.

= Acknowledgment

The authors express sincere gratitude to our Faculty Mentor, Dr. P. Akilandeswari, and our Industry Mentor, Pratyush Jha, for their technical mentorship, architectural critique, and continuous guidance throughout this research. We also thank our peers and student participants whose usability feedback and rubric evaluations helped refine this empirical study.

// ------------------------------------------------------------------------------
// REFERENCES (Natively rendered via IEEE bibliography engine)
// ------------------------------------------------------------------------------

#set text(size: 7.2pt)
#set par(leading: 0.45em)
#bibliography("references.bib", title: [References], style: "ieee")
