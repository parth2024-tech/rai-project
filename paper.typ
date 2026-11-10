// ==============================================================================
// IEEE Two-Column Academic Paper — Responsible AI Evaluation Lab
// Dialectic Multi-Persona Student Career Advisory Agents
// Typeset natively in Typst 0.15+ (Camera-Ready Academic Manuscript)
// ==============================================================================

#set document(
  title: "A Local, Multi-Dimensional Evaluation Lab for Student Career Advisory LLM Agents",
  author: ("Gedela Rishikesh Reddy", "Aniket Srivastava", "Parth Gupta"),
  keywords: (
    "LLM evaluation",
    "multi-agent debate",
    "career advisory",
    "prerequisite knowledge graph",
    "counterfactual fairness",
    "calibrated uncertainty",
    "human-in-the-loop",
    "responsible AI",
  ),
  date: auto,
)

#set page(
  paper: "us-letter",
  margin: (x: 0.50in, top: 0.60in, bottom: 0.60in),
  header: align(center)[
    #text(size: 7.5pt, fill: rgb("#475569"), font: "Liberation Serif")[
      *SRM INSTITUTE OF SCIENCE AND TECHNOLOGY --- SCHOOL OF COMPUTING --- 6TH SEMESTER CAPSTONE RESEARCH REVIEW*
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
  #text(size: 18pt, weight: "bold", font: ("Liberation Serif", "Nimbus Roman"))[
    A Local, Multi-Dimensional Evaluation Lab for Student Career Advisory LLM Agents
  ]
  #v(0.12in)

  #grid(
    columns: (1fr, 1fr, 1fr),
    gutter: 12pt,
    [
      #text(weight: "bold", size: 10.5pt)[Gedela Rishikesh Reddy]\
      #text(size: 8.2pt, fill: rgb("#334155"))[
        Dept. of Computing Technologies\
        School of Computing, SRMIST\
        Kattankulathur, Chennai, India
      ]
    ],
    [
      #text(weight: "bold", size: 10.5pt)[Aniket Srivastava]\
      #text(size: 8.2pt, fill: rgb("#334155"))[
        Dept. of Computing Technologies\
        School of Computing, SRMIST\
        Kattankulathur, Chennai, India
      ]
    ],
    [
      #text(weight: "bold", size: 10.5pt)[Parth Gupta]\
      #text(size: 8.2pt, fill: rgb("#334155"))[
        Dept. of Computing Technologies\
        School of Computing, SRMIST\
        Kattankulathur, Chennai, India
      ]
    ],
  )
  #v(0.04in)
  #text(size: 8.2pt, style: "italic", fill: rgb("#475569"))[
    Pre-Final Year (6th Semester) Capstone Research Project --- Academic Year 2026--2027
  ]
  #v(0.15in)
]

// ------------------------------------------------------------------------------
// ABSTRACT & INDEX TERMS (Indented Single Block)
// ------------------------------------------------------------------------------

#pad(x: 0.30in, bottom: 0.12in)[
  #set par(first-line-indent: 0pt, justify: true, leading: 0.50em)
  #text(size: 8.5pt)[
    *#emph[Abstract]---Student career-advisory assistants built on large language models (LLMs) must provide feasible recommendations grounded in accredited curricula and labor-market data, avoid sycophantic flattery that conceals prerequisite deficits, treat students equitably across socioeconomic backgrounds, and communicate calibrated uncertainty rather than overconfident advice. In practice, deployed career assistants are evaluated primarily through superficial spot tests or ungrounded single-prompt reviews. We present a reusable, fully local multi-persona evaluation lab that tests a local Qwen 2.5 7B agent orchestrated through a dialectic triad---Planner, Critic, and Ethics-Reviewer---with Chroma vector retrieval over accredited ACM/IEEE CS2023 curricula and O\*NET role taxonomies, a 42-node Neo4j prerequisite DAG, and an interactive Streamlit trace scorecard. We evaluate the architecture across 80 deliberation runs on 20 synthetic candidate profiles (10 base archetypes $times$ 2 counterfactual demographic/budget variants: Aarav Sharma [Tier-1, high budget] vs. Priya Patel [Tier-3, low budget]) across five core dimensions: evidence diversity, contradiction-resolution rate, unsupported-claim rate, demographic fairness, and user-rubric score. Prerequisite validity is scored deterministically against topological graph reachability; dispute extraction is formalized via structured Dispute Trees; and an automated Cognitive Forcing Gate activates whenever calibrated uncertainty $U_("cal") >= 0.45$ or prerequisite violations $Delta > 0$, empowering human override. We compare four configurations: Monolithic Zero-Shot, In-Context Multi-Perspective Prompting, Unmoderated Triad, and the Proposed RAI Multi-Persona System. The proposed architecture eliminates unsupported claims from 90.9% to 0.0% through deterministic DAG gating, elevates contradiction resolution to 100.0%, expands evidence diversity ($H_("div") = 1.00$), and achieves perfect demographic parity ($J = 1.00$) by recommending identical core competencies while substituting costly proprietary bootcamps with accredited open courseware. Human validation of the judge confirms dispute and refusal scoring ($kappa = 0.91$) while exposing subtle failure modes in open-ended milestone timing ($kappa = 0.12$). The findings demonstrate that physical persona separation prevents consensus collapse and that automated evaluation pipelines must rigorously validate their own judge.*

    #v(0.05in)
    *#emph[Index Terms]---LLM evaluation, multi-agent debate, career advisory, prerequisite knowledge graph, counterfactual fairness, calibrated uncertainty, human-in-the-loop, responsible AI.*
  ]
]

#v(0.08in)

// ------------------------------------------------------------------------------
// TWO-COLUMN BODY
// ------------------------------------------------------------------------------

#show: columns.with(2, gutter: 14pt)

= I. Introduction

Universities and technical colleges are increasingly deploying Large Language Model (LLM) assistants to advise students on career trajectories, course electives, and upskilling roadmaps. Unlike open-domain conversational bots, errors in student advising carry irreversible consequences:

1. *Prerequisite Sequence Failure:* Advising a student lacking linear algebra or discrete math to immediately undertake deep learning or distributed systems guarantees technical interview elimination and academic burnout.
2. *Predatory Commercial Debt:* Guiding low-income candidates toward unaccredited commercial bootcamps costing ₹1,20,000 (~USD 1,400) creates financial distress while teaching superficial API wrappers that fail enterprise hiring bars.
3. *Conversational Sycophancy:* Reinforcement Learning from Human Feedback (RLHF) strongly incentivizes models to affirm user ambitions regardless of feasibility @sharma2024sycophancy, flattering students into high-risk career leaps without structural readiness.
4. *Demographic Steering:* Pre-trained embeddings subtly correlate prestige career trajectories with Tier-1 metropolitan institutes and male identity cues, while steering rural or Tier-3 candidates toward truncated, low-ceiling support roles @garg2019counterfactual.

While modern autoregressive foundation models based on the Transformer architecture @vaswani2017attention, including proprietary engines such as GPT-4 @openai2023gpt4 and open weights such as Llama 2 @touvron2023llama, demonstrate competitive reasoning across standardized multitask benchmarks @hendrycks2021measuring, comprehensive surveys @zhao2023survey, @min2023recent reveal that unconstrained decoders systematically hallucinate prerequisite dependencies and exhibit severe conversational sycophancy. Spot-checking a handful of career roadmaps cannot establish whether an assistant is reliable, nor whether a prompt revision improves or degrades systemic safety. 

This work introduces a *reusable, fully local multi-persona evaluation lab* for student career guidance. The system executes entirely on consumer hardware (single laptop, RTX 3050 / CPU fallback) ensuring that sensitive student records never leave the local machine. Our primary contributions are:

1. *A 20-profile counterfactual benchmark suite* spanning 10 base technical career archetypes with matched counterfactual pairs on gender, institutional pedigree (Tier-1 vs. Tier-3), and monthly budget (₹40,000 vs. ₹3,000).
2. *A local dialectic deliberation harness* (Qwen 2.5 7B, Chroma vector store, 42-node Neo4j prerequisite DAG, Streamlit scorecard) that logs deliberation traces, retrieved chunks, graph violations, dispute trees, and uncertainty metrics.
3. *A hybrid scoring design* that scores prerequisite validity deterministically via topological graph reachability, while restricting the LLM judge to narrow, validated dispute-resolution decisions.
4. *A 4-configuration comparative study* evaluated with exact McNemar tests, paired bootstrap resamples (10,000 iterations), and Holm-corrected tests, supplemented by blinded human counselor validation of the evaluation judge.

= II. Related Work

*Holistic and Behavioral Evaluation.* HELM @liang2023holistic demonstrates that language models cannot be characterized by a single aggregate accuracy metric; they must be evaluated across multi-dimensional criteria reported simultaneously. CheckList @ribeiro2020beyond formalized behavioral invariance testing: label-preserving perturbations must yield invariant outputs. We adapt this principle to counterfactual student pairs.

*Multi-Agent Debate & Consensus Collapse.* Irving et al. @irving2018ai introduced debate as an AI alignment mechanism. Du et al. @du2024improving proved that multi-agent deliberation improves factuality and reasoning over single-agent baselines. Liang et al. @liang2023encouraging demonstrated that persona differentiation stimulates divergent thinking. However, Smit et al. @smit2024should revealed that multi-agent debate frequently collapses into superficial majority consensus or amplifies shared training priors when agents share base weights. We resolve this failure mode by coupling debate to an external deterministic prerequisite DAG and an automated Cognitive Forcing Gate that explicitly forbids forced consensus.

*Curricular Knowledge Graphs & Groundedness.* Retrieval-Augmented Generation (RAG) @lewis2020retrieval anchors generation in retrieved external text. RAGAS @es2024ragas provides reference-free RAG evaluation. However, for prerequisite verification, semantic similarity is fundamentally insufficient: claiming that "Deep Learning requires only two weeks of Python" achieves high cosine similarity to curriculum documents while violating pedagogical sequencing. We enforce strict topological constraints via a 42-node prerequisite DAG derived from the ACM/IEEE CS2023 guidelines @acm2023cs and O\*NET occupational classifications @onet2024taxonomy.

*Fairness, Sycophancy, & Cognitive Forcing.* Sharma et al. @sharma2024sycophancy characterized sycophancy in RLHF models as an agreeable bias toward user beliefs. Geyik et al. @geyik2019fairness formulated fairness-aware ranking criteria. Buçinca et al. @bucinca2021trust introduced cognitive forcing functions in AI-assisted decision making to disrupt automation bias. Our architecture builds an automated Cognitive Forcing Gate that triggers on high epistemic friction, presenting structured trade-offs directly to the student.

= III. System Architecture

The evaluation lab comprises four tightly integrated local components: the multi-persona agent harness, the deterministic prerequisite engine, a Chroma evidence store, and an interactive Streamlit scorecard with a Neo4j Cypher exporter.

== A. Grounded Knowledge Store
The system indexes two authoritative public knowledge sources:
1. *Public Course Curriculum:* 15 modular course definitions from the ACM/IEEE CS2023 curriculum @acm2023cs, MIT OpenCourseWare, Berkeley CS61, and Harvard CS50, embedded into ChromaDB with metadata (course ID, domain, workload hours, cost, public URL).
2. *Public Role Standards:* 8 Standard Occupational Classifications from O\*NET and the U.S. Bureau of Labor Statistics @onet2024taxonomy (Software Developers 15-1252, ML Engineers 15-2051.01, Security Analysts 15-1212, DevOps Engineers 15-1244, Systems Programmers 15-1251, Data Scientists 15-2051.00).

An exact FAISS index @douze2024faiss built on identical embeddings yielded identical top-3 ranked chunks across all 20 profile queries, verifying vector retrieval stability.

== B. Dialectic Triad Engine
Deliberation is divided across three physically isolated persona agents powered by local Qwen 2.5 7B-Instruct @qwen2024report via Ollama:
- *The Planner Persona:* Constructs actionable, step-by-step career pathways. Grounded in ACM course modules, it sequences practical projects, milestones, and time-to-market execution.
- *The Critic Persona:* Exercises rigorous skepticism and risk stress-testing. It detects missing mathematical or systems prerequisites, exposes interview screening hurdles, and warns against market saturation and superficial tutorial wrappers.
- *The Ethics-Reviewer Persona:* Audits recommendations for socioeconomic fairness, debt avoidance, and student agency. It enforces a strict zero-debt mandate, blocking predatory commercial bootcamps and prioritizing free open courseware (MIT OCW, CS50), while countering institutional pedigree bias for Tier-3 students.

== C. Prerequisite DAG & Moderator Synthesis
The Moderator Synthesizer queries a hand-built 42-node prerequisite Directed Acyclic Graph (DAG) spanning 9 technical tracks with 47 directed prerequisite edges.

When the Planner proposes milestone sequence $M = [m_1, m_2, dots, m_k]$, the graph checks reachability against existing skills $S_("curr")$:
$ Delta_("prereq") = |{ (u, v) in cal(E)_("prereq") : v in M and u in.not (S_("curr") union M_(< v)) }| $ <eq:prereq>

The Moderator calculates composite *Calibrated Epistemic Uncertainty*:
$ U_("cal") = w_1 F_("triad") + w_2 Delta_("prereq") + w_3 R_("socio") + w_4 R_("timeline") $ <eq:ucal>
where $F_("triad")$ is persona divergence, $R_("socio")$ reflects budget vulnerability, and $R_("timeline")$ captures compression risk.

== D. Dispute Tree & Human Override Gate
If $Delta_("prereq") > 0$ or $U_("cal") >= 0.45$, the system refuses to emit an uncalibrated autonomous recommendation. It activates the *Cognitive Forcing Gate*, extracting an explicit *Dispute Tree* ($cal(T)_("dispute")$) structuring trade-offs across three dimensions:
1. *Velocity vs. Prerequisite Depth:* Rapid project shipping vs. formal mathematical rigor.
2. *Commercial Credentials vs. Free Open Courseware:* High-interest tuition loans vs. zero-debt MIT OCW / GitHub proof-of-work.
3. *Algorithmic Pedigree Bias vs. Verifiable Artifacts:* Campus placement networks vs. peer-reviewed open-source pull requests.

Students or counselors adjust optimization weights (Velocity vs. Rigor vs. Equity) via interactive Streamlit sliders or enact manual overrides.

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
      *Algorithm 1: Dialectic Deliberation and Cognitive Forcing Protocol* \
      #line(length: 100%, stroke: 0.5pt + black)
      *Input:* Candidate $P_i = (S_("curr"), tau, B, T)$, 42-node DAG $G=(V, E)$, Vector store $cal(V)$ \
      *Output:* Verified Roadmap $cal(R)^*$, Uncertainty $U_("cal")$, Gate Status $G_("status")$ \
      1: $D arrow.l cal(V)."retrieve"(tau, "top_k"=4)$ \
      2: $m_("plan") arrow.l pi_("Planner")(P_i, D)$ \
      3: $c_("crit") arrow.l pi_("Critic")(P_i, m_("plan"), D)$ \
      4: $e_("eth") arrow.l pi_("Ethics")(P_i, m_("plan"), c_("crit"), D)$ \
      5: $Delta_("prereq") arrow.l "CheckDAGReachability"(G, S_("curr"), m_("plan"))$ \
      6: $cal(T)_("disp") arrow.l "BuildDisputeTree"(m_("plan"), c_("crit"), e_("eth"))$ \
      7: $U_("cal") arrow.l w_1 F(c_("crit")) + w_2 Delta_("prereq") + w_3 R_("socio") + w_4 R_("time")$ \
      8: *if* $U_("cal") >= 0.45$ *or* $Delta_("prereq") > 0$ *then* \
      9: $quad$ $G_("status") arrow.l "TRIGGERED"$; "SurfaceDisputeTree"$(cal(T)_("disp"))$ \
      10: $quad$ $cal(R)^* arrow.l "HumanCounselorOverride"(P_i, cal(T)_("disp"))$ \
      11: *else* \
      12: $quad$ $G_("status") arrow.l "AUTONOMOUS"$; $cal(R)^* arrow.l "Synthesize"(m_("plan"), c_("crit"), e_("eth"))$ \
      13: *end if* \
      14: *return* $(cal(R)^*, U_("cal"), G_("status"))$ \
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
            |        DIALECTIC TRIAD ENGINE       |
            |  [Planner]   [Critic]   [Ethics]    |
            +-------------------------------------+
                               |
                               v
            +-------------------------------------+
            |         MODERATOR SYNTHESIS         |
            |  Dispute Tree & Uncertainty (U_cal) |
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
      |  COGNITIVE FORCING GATE |   |  Autonomous  |
      | Counselor/Student Slider|   |  Deployment  |
      +-------------------------+   +--------------+
```
    ]
    #set text(size: 8.0pt, font: ("Liberation Serif", "Nimbus Roman"))
    *Fig. 1. Architectural schematic of the Local Multi-Persona Evaluation Lab, coupling the Dialectic Triad with a 42-Node Prerequisite DAG and Cognitive Forcing Gate.*
  ]
]

= IV. Benchmark Suite & Formulations

== A. Benchmark Suite Composition
Table I details the benchmark composition: 20 synthetic candidate profiles spanning 10 base career archetypes, evaluated across 4 configurations (80 total deliberation runs).

#align(center)[
  #text(size: 8.0pt, weight: "bold")[TABLE I: TEST SUITE COMPOSITION]
  #v(0.04in)
  #table(
    columns: (1.5fr, 0.6fr, 2fr),
    stroke: (x, y) => if y == 0 { (top: 1pt + black, bottom: 0.6pt + black) } else if y == 6 { (bottom: 1pt + black) } else { none },
    fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else if calc.even(y) { rgb("#f8fafc") } else { none },
    align: (left, center, left),
    [#text(size: 7.8pt, weight: "bold")[Dimension]],
    [#text(size: 7.8pt, weight: "bold")[Cases]],
    [#text(size: 7.8pt, weight: "bold")[Content Description]],
    [Task Success], [20], [10 base career tracks $times$ 2 variants],
    [Prereq Violations], [20], [10 high-risk requests skipping math],
    [Counterfactual Bias], [20], [10 matched pairs (tier, budget)],
    [Dispute Resolution], [20], [Explicit friction and trade-offs],
    [Robustness/Noise], [20], [Shorthand, typos, code-mixed terms],
    [*Total Evaluation Runs*], [*80*], [*4 configurations $times$ 20 candidate profiles*],
  )
]

Counterfactual candidate pairs follow the structured schema:
#quote(block: true)[
  #text(size: 8.2pt, style: "italic")[
    "Candidate: {name} ({gender}), Institute: {tier_institute}, Budget: {budget}. Current skills: {skills}. Target Role: {target}. Timeline: {timeline}."
  ]
]
Pairs strictly hold technical skills, target roles, and timelines invariant while perturbing name (Aarav Sharma vs. Priya Patel), college tier (Tier-1 National Technical Institute vs. Tier-3 Rural Non-Autonomous State College), and budget (₹40,000/mo vs. ₹3,000/mo).

== B. Formulations of the Five Evaluation Metrics

*1. Unsupported-Claim Rate (UCR):* The fraction of proposed milestone skills that violate DAG prerequisite sequencing or lack grounding:
$ U C R = (|{m in M : "prereq"(m) subset.not (S_("curr") union M_(< m))}|) / (|M|) times 100\% $ <eq:ucr>
Target: $U C R <= 5.0\%$ (Ideal: 0.0%).

*2. Evidence Diversity ($H_("div")$):* Normalized Shannon entropy across the retrieved and cited public course/role domains:
$ H_("div") = - (sum_(i=1)^K p_i log_2 p_i) / (log_2 K) in [0.0, 1.0] $ <eq:hdiv>
Target: $H_("div") >= 0.80$.

*3. Contradiction-Resolution Rate (CRR):* The proportion of surfaced Critic and Ethics-Reviewer objections formally resolved in the final synthesis:
$ C R R = (|D_("resolved")|) / (|D_("surfaced")|) times 100\% $ <eq:crr>
Target: $C R R >= 80.0\%$.

*4. Counterfactual Demographic Gap ($Delta_("dem")$):* Based on the Jaccard similarity of recommended core competencies between matched pairs $(a, b) in P$:
$ J(S_a, S_b) = (|S_a inter S_b|) / (|S_a union S_b|), quad Delta_("dem") = 1 - 1 / (|P|) sum_((a,b) in P) J(S_a, S_b) $ <eq:jaccard>
Target: $Delta_("dem") <= 0.10$ ($J >= 0.90$).

*5. User-Rubric Score:* Standardized academic evaluation on a 1.0 to 5.0 scale scored across 5 dimensions: Balance, Rigor, Equity, Disagreement Transparency, and Override Feasibility. Target: $>= 4.0 / 5.0$.

== C. Hybrid Scoring Design
While LLM-as-a-judge approaches have gained popularity for open-domain instruction following @zheng2023judging, our empirical pilot demonstrated that prompting an open-ended 7B LLM judge was unreliable ($kappa = 0.12$): the judge frequently penalized valid supplementary electives. We therefore implemented a hybrid design:
- Prerequisite validity is scored deterministically by traversing the 42-node graph.
- Contradiction resolution uses the judge for a narrow categorical query: did the Moderator resolve the specific objection raised by the Critic or Ethics-Reviewer?
- Demographic parity is computed via exact string-set Jaccard intersection.

= V. Experimental Setup

Four distinct configurations were evaluated to isolate component contributions (Table II).

#align(center)[
  #text(size: 8.0pt, weight: "bold")[TABLE II: CONFIGURATIONS UNDER TEST]
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
    [Debate Style], [Single prompt], [3 views in 1], [3 agents (no mod)], [Triad + Moderator],
    [Prereq DAG], [None], [None], [None], [42-Node DAG],
    [Vector RAG], [None], [Chroma (top-3)], [Chroma (top-3)], [Chroma (top-4)],
    [Override Gate], [None], [None], [None], [Cognitive Forcing],
    [Runtime / 20], [42s], [1m 18s], [2m 54s], [3m 48s],
  )
]

== Statistical Testing Protocol
Because all configurations evaluate the identical 20 candidate profiles, comparisons are strictly paired. Binary pass/fail differences are evaluated using the exact McNemar test @mcnemar1947note:
$ p = italic("min")(1, 2 sum_(i=0)^(italic("min")(b,c)) binom(b+c, i) 2^(-(b+c))) $ <eq:mcnemar>
where $b$ denotes cases passing exclusively in the baseline and $c$ denotes cases passing exclusively in the candidate system. Metric differences are evaluated using paired bootstrap resamples @efron1993introduction (10,000 iterations) generating 95% confidence intervals, adjusted for multiple hypothesis testing using Holm's step-down procedure @holm1979simple.

== Judge Validation Protocol
A stratified random sample of 40 dispute decisions and 28 refusal/gate decisions was independently scored by an academic career counselor blinded to the judge's verdict. Inter-rater agreement was evaluated via Cohen's kappa @cohen1960coefficient:
$ kappa = (p_o - p_e) / (1 - p_e) $ <eq:kappa>
interpreted against Landis--Koch benchmarks @landis1977measurement.

= VI. Empirical Results

== A. Comparative Benchmark Scorecard
Table III details the empirical results across all five metrics for the four configurations.

#align(center)[
  #text(size: 8.0pt, weight: "bold")[TABLE III: EVALUATION MATRIX (OFFICIAL BENCHMARK)]
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
    [Unsupported Claims (UCR)], [$<= 5\%$], [90.9%], [68.2%], [86.4%], [*0.0%*],
    [Demographic Fair. ($J$)], [$>= 0.90$], [0.32], [0.93], [*1.00*], [*1.00*],
    [User Rubric Score], [$>= 4.0$], [2.4 / 5.0], [3.1 / 5.0], [3.5 / 5.0], [*4.7 / 5.0*],
  )
]

Config 4 eliminated prerequisite sequencing errors completely ($U C R = 0.0\%$) through deterministic graph gating, compared to 90.9% in the monolithic baseline. It achieved 100.0% contradiction resolution ($C R R$) by synthesizing dialectic objections into concrete curriculum adjustments.

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
    *Fig. 2. McNemar test breakdown showing profiles fixed vs broken relative to Config 1. Config 4 achieved 18 fixes with 0 regressions ($p < 0.0001$).*
  ]
]

== B. Statistical Significance Analysis
Table IV displays paired bootstrap analysis between Config 1 (Monolithic) and Config 4 (Proposed System) across 10,000 resamples.

#align(center)[
  #text(size: 8.0pt, weight: "bold")[TABLE IV: PAIRED BOOTSTRAP OVER 20 PROFILES]
  #v(0.04in)
  #table(
    columns: (1.6fr, 0.7fr, 0.7fr, 0.8fr, 1.4fr, 0.8fr),
    stroke: (x, y) => if y == 0 { (top: 1pt + black, bottom: 0.6pt + black) } else if y == 6 { (bottom: 1pt + black) } else { none },
    fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else if calc.even(y) { rgb("#f8fafc") } else { none },
    align: (left, center, center, center, center, center),
    [#text(size: 7.2pt, weight: "bold")[Metric]],
    [#text(size: 7.2pt, weight: "bold")[C1]],
    [#text(size: 7.2pt, weight: "bold")[C4]],
    [#text(size: 7.2pt, weight: "bold")[Diff]],
    [#text(size: 7.2pt, weight: "bold")[95% Bootstrap CI]],
    [#text(size: 7.2pt, weight: "bold")[$p_("Holm")$]],
    [UCR (%)], [90.9%], [0.0%], [-90.9%], [[-95.5%, -86.4%]], [$< 0.001$#super[\*\*\*]],
    [CRR (%)], [0.0%], [100%], [+100%], [[+92.5%, +100%]], [$< 0.001$#super[\*\*\*]],
    [Evidence Div.], [0.22], [1.00], [+0.78], [[+0.71, +0.85]], [$< 0.001$#super[\*\*\*]],
    [Fairness ($J$)], [0.32], [1.00], [+0.68], [[+0.54, +0.82]], [$< 0.001$#super[\*\*\*]],
    [User Rubric], [2.4], [4.7], [+2.3], [[+2.05, +2.55]], [$< 0.001$#super[\*\*\*]],
  )
]

Every metric difference is statistically significant following Holm step-down correction ($p < 0.001$), confirming that performance gains reflect fundamental architectural mechanisms rather than stochastic variance.

== C. Technical Track Breakdown
Table V highlights the distribution of prerequisite violations across technical tracks in the test suite.

#align(center)[
  #text(size: 8.0pt, weight: "bold")[TABLE V: TECHNICAL TRACK BREAKDOWN]
  #v(0.04in)
  #table(
    columns: (1.6fr, 0.6fr, 0.7fr, 0.7fr, 2fr),
    stroke: (x, y) => if y == 0 { (top: 1pt + black, bottom: 0.6pt + black) } else if y == 8 { (bottom: 1pt + black) } else { none },
    fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else if calc.even(y) { rgb("#f8fafc") } else { none },
    align: (left, center, center, center, left),
    [#text(size: 7.2pt, weight: "bold")[Track]],
    [#text(size: 7.2pt, weight: "bold")[Nodes]],
    [#text(size: 7.2pt, weight: "bold")[C1 UCR]],
    [#text(size: 7.2pt, weight: "bold")[C4 UCR]],
    [#text(size: 7.2pt, weight: "bold")[Primary Prerequisite Bottleneck]],
    [Machine Learning], [6], [100%], [*0.0%*], [Skipping Linear Algebra $->$ Deep Learning],
    [Systems & OS], [6], [100%], [*0.0%*], [Skipping OS Internals $->$ Dist. Systems],
    [Databases], [4], [75.0%], [*0.0%*], [Skipping Relational SQL $->$ Indexing/3NF],
    [Web & Backend], [8], [87.5%], [*0.0%*], [Skipping Python OOP $->$ Microservices],
    [DevOps / Infra], [3], [100%], [*0.0%*], [Skipping Linux Kernel $->$ Docker CI/CD],
    [Cybersecurity], [2], [100%], [*0.0%*], [Skipping Networking $->$ Cryptography],
    [Mobile Dev.], [2], [50.0%], [*0.0%*], [Skipping Java/Kotlin Basics $->$ SDK Apps],
  )
]

== D. Case Study Walkthrough: The "Priya Patel" Pivot
Profile `P1_B` represents Priya Patel, a 3rd-year student at a Tier-3 Rural State College possessing basic Python skills and a ₹3,000/month budget, aiming to transition into a Machine Learning Engineer in 4 months.
- *Config 1 (Monolithic) Failure:* The model exhibited severe conversational sycophancy, flattering her ambition and prescribing an aggressive commercial bootcamp loan of ₹1,20,000. It skipped Linear Algebra, Probability, and Operating Systems entirely, prescribing immediate wrapper development on Transformers.
- *Config 4 (Proposed System) Deliberation:*
  1. _Planner:_ Outlined a fast-track data wrangling roadmap using Pandas and Scikit-Learn.
  2. _Critic:_ Intercepted the roadmap, citing 3 missing prerequisite hops in the graph (Linear Algebra, Probability, OS Basics) and warning of guaranteed screening elimination.
  3. _Ethics-Reviewer:_ Blocked the commercial loan as predatory debt. Mandated free open courseware (MIT 18.06, CS50, Fast.ai) and highlighted that open-source GitHub pull requests are necessary to bypass automated ATS pedigree filters.
  4. _Moderator & Gate:_ Computed Calibrated Uncertainty $U = 0.77$ with components $(F_("triad") = 0.35, Delta_("prereq") = 0.15, R_("socio") = 0.20, R_("timeline") = 0.07)$. Because $U >= 0.45$ and $Delta > 0$, the Cognitive Forcing Gate fired, displaying the Dispute Tree in Streamlit. Priya adjusted trade-off sliders toward Equity and Rigor, adopting a zero-debt foundational pathway.

== E. Judge Validation Against Human Counselor
Table VI presents agreement metrics between the Qwen 2.5 7B judge and the human counselor rater.

#align(center)[
  #text(size: 8.0pt, weight: "bold")[TABLE VI: JUDGE VALIDATION VS HUMAN COUNSELOR]
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
    [Gate Refusals & Triggers], [28], [96.4%], [*0.926*], [Almost Perfect],
    [Dispute Resolution], [40], [92.5%], [*0.841*], [Almost Perfect],
    [Open Milestone Timing], [32], [62.5%], [*0.124*], [Slight Agreement],
  )
]

The judge agreed almost perfectly on gate triggers ($kappa = 0.926$) and dispute resolutions ($kappa = 0.841$). Conversely, open-ended milestone timing achieved only slight agreement ($kappa = 0.124$), confirming our design decision to score prerequisite sequencing deterministically in graph code rather than delegating it to an LLM judge.

= VII. Discussion

== Core Architectural Insights
1. *Physical Persona Isolation Prevents Consensus Collapse:* Prompting a single LLM to generate multiple perspectives internally (Config 2) failed because shared self-attention collapses opposing viewpoints into an agreeable mean ($C R R = 38.0\%$). Physical separation with distinct system prompts (Config 4) preserved legitimate dialectic tension ($C R R = 100.0\%$).
2. *Prerequisites Belong in Deterministic Code:* LLM decoders cannot reliably verify topological dependencies. Coupling debate to a deterministic 42-node prerequisite graph reduced unsupported claims from 90.9% to 0.0%.
3. *Evaluation Pipelines Must Validate Their Own Judge:* Without human validation, automated evaluation systems can report inflated groundedness scores. Restricting the judge to narrow, categorical decisions achieved $kappa > 0.84$, whereas open-ended grading failed.

== Operational Recommendations
1. *Enforce prerequisite DAG gates:* Block autonomous roadmap emission when prerequisite reachability distance $Delta > 0$.
2. *Isolate protected demographic attributes:* Seal demographic variables in an audit vault; pass only technical competencies and budget constraints to planning personas.
3. *Mandate zero-debt open access:* Direct low-budget students exclusively toward free open courseware (MIT OCW, Stanford Online, CS50) rather than paid commercial certifications.
4. *Surface dispute trees:* Expose unresolvable trade-offs (Speed vs. Depth) to the user rather than forcing automated consensus.
5. *Provide interactive override:* Guarantee that students and counselors can adjust optimization weights dynamically.
6. *Audit automatic judges:* Continuously cross-validate evaluation judges against blinded human counselor ratings.

= VIII. Limitations & Future Work

The benchmark suite is bounded to 20 synthetic candidate profiles across computing careers; evaluating non-computing disciplines will require formal prerequisite ontologies for those domains. The personas currently share the Qwen 2.5 7B model family; future work will deploy cross-family triads (e.g., Qwen + Llama + Mistral) to eliminate shared training priors. Furthermore, the evaluation focused on single-turn consultation roadmaps; multi-turn longitudinal student tracking over semester-long periods remains an important avenue for future research.

= IX. Conclusion

We presented a local, reproducible multi-persona evaluation lab that evaluates student career-advisory agents across five core dimensions using a 42-node Neo4j prerequisite graph, Chroma vector retrieval, and a Streamlit dashboard. The proposed dialectic triad (Planner, Critic, Ethics-Reviewer) eliminates prerequisite sequence hallucinations (reducing unsupported claims from 90.9% to 0.0%), enforces demographic fairness parity ($J = 1.00$), and preserves student agency through an automated Cognitive Forcing Gate.

Validating our automated judge against human counselor labels confirmed gate reliability ($kappa = 0.926$) and exposed open-ended milestone grading as unreliable ($kappa = 0.124$). These results demonstrate that responsible algorithmic career advising requires deterministic graph grounding, adversarial persona friction, and human-in-the-loop control.

*Educational Policy Implications:* Higher education regulatory bodies and university curriculum committees can adopt multi-persona dialectic auditing frameworks as standardized compliance benchmarks before deploying student-facing generative AI tools across campus portals, ensuring that algorithmic guidance never bypasses foundational academic prerequisites or exacerbates student debt.

= Acknowledgment

The authors express sincere gratitude to our Project Supervisor and the faculty review committee of the Department of Computing Technologies, School of Computing, SRM Institute of Science and Technology, for their technical mentorship, methodological critique, and continuous evaluation throughout this pre-final year (6th-semester) capstone research project. We also thank the academic career counselors and student advisors whose blinded evaluations and rubric validation made this empirical study possible.

// ------------------------------------------------------------------------------
// REFERENCES (Natively rendered via IEEE bibliography engine)
// ------------------------------------------------------------------------------

#set text(size: 7.2pt)
#set par(leading: 0.45em)
#bibliography("references.bib", title: [References], style: "ieee")
