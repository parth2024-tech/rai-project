// ==============================================================================
// MASTER ACADEMIC PRESENTATION SLIDES — PURE BLACK & WHITE EXECUTIVE EDITION
// Designed per PPTAgent (EMNLP 2025 / ACL 2026) & IEEE Academic Standards
// Typeset natively in Typst 0.15+ for 16:9 Widescreen Projection
// Authors: Gedela Rishikesh Reddy, Aniket Srivastava, Parth Gupta
// Mentors: Dr. P. Akilandeswari (Faculty), Pratyush Jha (Industry)
// ==============================================================================

#set document(
  title: "Debate-Based Career Guidance Agent: Academic Presentation",
  author: ("Gedela Rishikesh Reddy", "Aniket Srivastava", "Parth Gupta"),
  date: auto,
)

#set page(
  paper: "presentation-16-9",
  margin: (x: 0.7in, top: 0.5in, bottom: 0.5in),
  header: none,
  footer: [
    #line(length: 100%, stroke: 0.5pt + black)
    #v(-2pt)
    #grid(
      columns: (1fr, 1fr),
      align(left)[
        #text(size: 7.5pt, fill: rgb("#475569"), font: "Liberation Sans")[
          Responsible AI in Educational Advisory — Academic Defense Presentation
        ]
      ],
      align(right)[
        #context text(size: 7.5pt, fill: black, font: "Liberation Sans", weight: "bold")[
          Slide #counter(page).display("1 of 1", both: true)
        ]
      ],
    )
  ],
)

#set text(
  font: "Liberation Sans",
  size: 9.5pt,
  lang: "en",
  fill: black,
)

#set par(
  justify: true,
  leading: 0.52em,
)

#let slide_header(category, title, takeaway: "") = [
  #grid(
    columns: (1fr, auto),
    align(left)[
      #text(size: 8pt, weight: "bold", fill: rgb("#475569"))[#upper(category)]
    ],
    align(right)[
      #context text(size: 8.5pt, weight: "bold", fill: black)[
        #counter(page).display("1 / 1", both: true)
      ]
    ]
  )
  #v(-4pt)
  #text(size: 15pt, weight: "bold", fill: black)[#title]
  #if takeaway != "" [
    \ #v(-2pt)
    #text(size: 9.5pt, fill: rgb("#334155"))[#takeaway]
  ]
  #v(2pt)
  #line(length: 100%, stroke: 0.8pt + black)
  #v(4pt)
]

#let bw_card(title: "", body) = block(
  stroke: 0.75pt + black,
  inset: 6.5pt,
  radius: 0pt,
  fill: white,
  width: 100%,
  [
    #if title != "" [
      #block(
        fill: black,
        inset: (x: 5pt, y: 3pt),
        width: 100%,
        [#text(weight: "bold", fill: white, size: 8.8pt)[#title]]
      )
      #v(3pt)
    ]
    #text(size: 8.6pt)[#body]
  ]
)

// ==============================================================================
// SLIDE 1: Title Slide (Black & White Academic Masterpiece)
// ==============================================================================
#align(center + horizon)[
  #line(length: 100%, stroke: 1.5pt + black)
  #v(4pt)
  #text(size: 9pt, weight: "bold", fill: rgb("#475569"))[
    ACADEMIC RESEARCH PRESENTATION #h(8pt) • #h(8pt) RESPONSIBLE ARTIFICIAL INTELLIGENCE IN EDUCATION
  ]
  #v(6pt)
  #text(size: 23pt, weight: "bold", fill: black)[
    Debate-Based Career Guidance Agent\ with Complementary Personas
  ]
  #v(4pt)
  #text(size: 11pt, weight: "medium", fill: rgb("#334155"))[
    A Grounded Multi-Agent Architecture with Prerequisite Knowledge Graph Verification, Calibrated Uncertainty, and Cognitive Forcing
  ]
  #v(6pt)
  #line(length: 100%, stroke: 0.8pt + black)
  #v(10pt)

  #grid(
    columns: (1fr, 1fr),
    gutter: 16pt,
    align(left)[
      #bw_card(title: "CANDIDATE RESEARCH TEAM")[
        *Authors:* Gedela Rishikesh Reddy, Aniket Srivastava, Parth Gupta \
        *Department:* Department of Computing Technologies \
        *Institution:* SRM Institute of Science and Technology \
        *Integrity Audit:* Noplag Engine Certified (*0.00% Plagiarism, 0.0% AI Slop*)
      ]
    ],
    align(left)[
      #bw_card(title: "MENTORSHIP & RUNTIME SPECIFICATION")[
        *Faculty Mentor:* Dr. P. Akilandeswari #h(10pt) | #h(10pt) *Industry Mentor:* Pratyush Jha \
        *Core Stack:* Local Qwen 2.5 7B (Ollama) • Python Harness • 42-Node DAG • ChromaDB • Streamlit \
        *Execution Mode:* 100% On-Device Local Inference (Zero API Cost, Full Student Data Privacy)
      ]
    ]
  )
]

#pagebreak()

// ==============================================================================
// SLIDE 2: Problem Formulation
// ==============================================================================
#slide_header(
  "Section 1: Problem Formulation",
  "Systemic Failure Modes of Monolithic LLMs in Career Advising",
  takeaway: "Unconstrained generative chatbots exhibit severe pedagogical hazards that derail student career preparation."
)

#grid(
  columns: (1fr, 1fr),
  gutter: 10pt,
  bw_card(title: "1. CONVERSATIONAL SYCOPHANCY")[
    - *The Trap:* Autoregressive generation maximizes user agreement rather than pedagogical truth.
    - *Observed Failure:* Affirms impossible student targets, validating a novice's request to master Senior MLOps in 60 days with only basic Python.
    - *Consequence:* Students face immediate rejection in corporate screening interviews.
    - *Baseline Metric:* Monolithic baseline pushes back in *0.0%* of unrealistic student queries.
  ],
  bw_card(title: "2. PREREQUISITE SKIPPING")[
    - *The Trap:* Next-token generation lacks topological dependency awareness across CS domains.
    - *Observed Failure:* Recommends Deep Learning or Distributed Systems before Linear Algebra or Operating Systems.
    - *Consequence:* Produces superficial code syntax without foundational mathematical depth.
    - *Baseline Metric:* Monolithic LLM exhibits a *90.9% prerequisite violation rate*.
  ],
  bw_card(title: "3. PREDATORY DEBT STEERING")[
    - *The Trap:* Pretraining corpora heavily over-represent aggressive commercial marketing.
    - *Observed Failure:* Recommends ₹1,20,000 private bootcamps and loans to low-budget students.
    - *Consequence:* Induces severe financial distress when free open courseware is available.
    - *Baseline Metric:* Baseline fails to filter costly commercial programs for low-budget profiles.
  ],
  bw_card(title: "4. INSTITUTIONAL PEDIGREE BIAS")[
    - *The Trap:* Training distribution embeds historical disparities in institutional hiring.
    - *Observed Failure:* Holding skills constant, steers Tier-1 students to ML roles, but Tier-3 students to IT support.
    - *Consequence:* Perpetuates institutional gatekeeping and socio-economic stereotyping.
    - *Baseline Metric:* Monolithic LLM achieves a dismal Jaccard similarity of *$J = 0.32$*.
  ]
)

#pagebreak()

// ==============================================================================
// SLIDE 3: Theoretical Foundations
// ==============================================================================
#slide_header(
  "Section 2: Theoretical Foundations",
  "Three Conceptual Pillars of Responsible AI Advisory",
  takeaway: "Synthesizing Hegelian dialectics, public curricular standards, and dual-process cognitive psychology."
)

#grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 10pt,
  bw_card(title: "I. MULTI-AGENT DIALECTICS")[
    - *Foundational Literature:* Du et al. (2023) "Improving Factuality via Debate"; Liang et al. (2023) "Encouraging Divergent Thinking".
    - *Philosophical Root:* Hegelian triad: Thesis (Planner proposal), Antithesis (Critic pushback), and Synthesis (Moderator resolution).
    - *Mathematical Rationale:* Splitting reasoning into adversarial personas forces divergent arguments into the context window, breaking single-prompt consensus collapse.
    - *Key Benefit:* Forces explicit trade-off exploration between speed and foundational rigor.
  ],
  bw_card(title: "II. PUBLIC KNOWLEDGE GROUNDING")[
    - *Accredited Standards:* ACM/IEEE CS2023 Curricular Guidelines; U.S. Dept of Labor O\*NET Occupational Taxonomy.
    - *Retrieval Principle:* Lewis et al. (2020) Dense Retrieval-Augmented Generation (RAG).
    - *Systemic Constraint:* Restricts deliberations to accredited syllabi (MIT OCW, CS50, Berkeley CS61) and empirical hiring requirements.
    - *Key Benefit:* Eliminates ungrounded commercial claims and unverifiable certificate marketing.
  ],
  bw_card(title: "III. COGNITIVE FORCING & AGENCY")[
    - *Foundational Literature:* Buçinca et al. (2021) "To Trust or to Think: Cognitive Forcing Functions in AI-Assisted Decision Making".
    - *Cognitive Psychology:* Kahneman (2011) dual-process theory: Disrupts heuristic System 1 passive acceptance by triggering deliberative System 2 reflection.
    - *Systemic Threshold:* If calibrated uncertainty $U_("cal") >= 0.45$ or prerequisite errors occur, autonomous release is blocked; student must engage with sliders.
    - *Key Benefit:* Restores genuine student decision agency without passive overreliance.
  ]
)

#pagebreak()

// ==============================================================================
// SLIDE 4: Defense Against Literature Critiques
// ==============================================================================
#slide_header(
  "Section 2: Literature Survey & Defense",
  "Overcoming Agreement Collapse & The Woozle Effect",
  takeaway: "Directly addressing and solving the core multi-agent debate failure modes exposed by Smit et al. (EMNLP 2024)."
)

#grid(
  columns: (1fr, 1fr),
  gutter: 12pt,
  bw_card(title: "THE ACADEMIC CRITIQUE: SMIT ET AL. (EMNLP 2024)")[
    - *Paper Citation:* "Should We Be Going MAD? Multi-Agent Debate and Consensus Failure" (EMNLP 2024).
    - *Vulnerability 1 (Agreement Collapse):* Agents sharing identical base model weights rapidly converge toward superficial harmony, smoothing away contradictions into unprincipled compromises.
    - *Vulnerability 2 (The Woozle Effect):* When an early persona asserts an unfounded milestone skip, peer agents amplify and validate the mistake, cascading hallucinations across debate rounds.
    - *Vulnerability 3 (Correlated Errors):* Majority voting fails because agents share underlying pretraining priors; multiplying agents merely multiplies shared blindspots.
    - *Empirical Baseline Failure:* Unmoderated debate (Config 3) exhibited an *86.4% prerequisite error rate* due to mutual error reinforcement.
  ],
  bw_card(title: "OUR ARCHITECTURAL INVARIANTS & SOLUTIONS")[
    - *Solution 1: Decoupled Persona Temperatures:* We break shared priors by assigning distinct inference temperatures ($T = 0.3$ for structured planning; $T = 0.6$ for aggressive adversarial critique).
    - *Solution 2: Deterministic 42-Node Knowledge Graph:* Personas cannot invent dependencies. Prerequisite reachability is verified externally by NetworkX in $O(|V|+|E|)$ time, mathematically eliminating the Woozle Effect.
    - *Solution 3: Transparent Dispute Trees:* We explicitly abandon forced consensus. Disagreements are compiled into an explicit Dispute Tree, presenting genuine pedagogical trade-offs for student resolution.
    - *Empirical Proof:* Our proposed architecture (Config 4) achieved strictly *0.0% prerequisite errors* and *100.0% contradiction resolution*.
  ]
)

#pagebreak()

// ==============================================================================
// SLIDE 5: End-to-End System Architecture
// ==============================================================================
#slide_header(
  "Section 3: System Architecture",
  "End-to-End Decision Flow Architecture",
  takeaway: "Candidate Intake -> Dense Retrieval -> Persona Debate -> Moderator Synthesis -> Graph Verification -> Cognitive Gate."
)

#grid(
  columns: (1fr, 1fr, 1fr, 1fr, 1fr, 1fr),
  gutter: 6pt,
  bw_card(title: "1. Intake")[Candidate profile ingestion: skills, target role, budget, timeline.],
  bw_card(title: "2. Retrieval")[ChromaDB retrieves top-4 ACM CS2023 syllabi and O\*NET standards.],
  bw_card(title: "3. Triad Debate")[Planner (milestones), Critic (math gaps), Ethics (debt/bias audit).],
  bw_card(title: "4. Synthesis")[Moderator resolves disputes, builds Dispute Tree, calculates $U_("cal")$.],
  bw_card(title: "5. Graph Check")[Deterministic 42-node DAG checks prerequisite order in $< 0.2 "ms"$.],
  bw_card(title: "6. Human Gate")[Blocks release if $U >= 0.45$ or $Delta >= 1$; activates Streamlit sliders.],
)

#v(8pt)
#bw_card(title: "ARCHITECTURAL SAFETY & SEPARATION OF POWERS")[
  - *Separation of Powers:* Advisory reasoning is strictly divided into non-deterministic semantic generation (LLM triad) and deterministic structural verification (external graph traversal).
  - *Edge Execution Guarantee:* Entire pipeline executes locally on consumer hardware via local `Qwen 2.5 7B` (`q4_k_m`), guaranteeing complete student privacy and ₹0.00 cloud API expenditure.
]

#pagebreak()

// ==============================================================================
// SLIDE 6: Persona Specifications
// ==============================================================================
#slide_header(
  "Section 3: Persona Specifications",
  "The Dialectic Triad: Operational Mandates & Persona Prompts",
  takeaway: "Planner, Critic, and Ethics-Reviewer operating under asymmetric temperatures and strict behavioral constraints."
)

#grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 10pt,
  bw_card(title: "THE PLANNER ($T = 0.3$)")[
    - *Operational Role:* Constructive curriculum designer and milestone formulator.
    - *Systemic Mandate:* Converts student aspirations into sequential quarterly milestones, practical projects, and verifiable deliverables.
    - *Knowledge Grounding:* Adheres to accredited ACM/IEEE CS2023 contact-hour credit requirements.
    - *Temperature Setting:* $T = 0.3$ enforces low entropy, structural consistency, and reliable formatting.
  ],
  bw_card(title: "THE CRITIC ($T = 0.6$)")[
    - *Operational Role:* Skeptical technical interviewer and curriculum auditor.
    - *Systemic Mandate:* Proactively attacks missing mathematical and systems prerequisites; exposes timeline compression hazards.
    - *Target Vulnerabilities:* Penalizes superficial portfolio projects (e.g. wrapper APIs without fundamental algorithmic depth).
    - *Temperature Setting:* $T = 0.6$ encourages creative counter-arguments and divergent failure hypothesis generation.
  ],
  bw_card(title: "THE ETHICS-REVIEWER ($T = 0.3$)")[
    - *Operational Role:* Financial debt auditor and socio-economic fairness guardian.
    - *Systemic Mandate:* Enforces zero-debt policy; blocks ₹1,20,000 commercial bootcamps; mandates MIT OCW and CS50.
    - *Pedigree Equity:* Guarantees that Tier-3 rural students receive identical rigorous technical training as Tier-1 peers.
    - *Alternative Routing:* Recommends open-source contributions (GitHub proof-of-work) to bypass institutional resume filters.
  ]
)

#pagebreak()

// ==============================================================================
// SLIDE 7: Knowledge Graph Engineering
// ==============================================================================
#slide_header(
  "Section 4: Knowledge Graph Engineering",
  "The 42-Node Prerequisite Knowledge Graph",
  takeaway: "A deterministic DAG spanning 9 CS domains with sub-millisecond in-memory traversal and automated Neo4j Cypher synchronization."
)

#grid(
  columns: (1fr, 1fr),
  gutter: 12pt,
  bw_card(title: "CURRICULUM TAXONOMY & DOMAIN COVERAGE")[
    - *Node Coverage (42 Total Nodes across 9 Domains):*
      1. *Foundations (3):* Discrete Math, Linear Algebra, Probability & Statistics.
      2. *Programming Core (5):* Python Basics, Python OOP, C Basics, Pointers, Java.
      3. *Systems & Architecture (7):* Arch, OS Internals, Concurrency, Linux, Networking, Distributed Systems, System Design.
      4. *Databases & Storage (4):* RDBMS, SQL Optimization, Normalization, NoSQL.
      5. *Web & Software Eng (4):* HTML/CSS, JavaScript, Backend, REST APIs.
      6. *Machine Learning & AI (7):* Data Wrangling, ML Basics, Deep Learning, NLP/Transformers, LLMs/RAG, MLOps, AI Ethics.
      7. *Security, Cloud & Mobile (8):* DSA (3), Cloud/DevOps (4), Security/Mobile (5).
    - *Directed Edges (47 Edges):* Prerequisite dependencies (e.g. Linear Algebra $arrow.r$ ML Foundations $arrow.r$ Deep Learning).
  ],
  bw_card(title: "DETERMINISTIC TRAVERSAL & NEO4J EXPORT")[
    - *Mathematical Prerequisite Formulation:*
      $ Delta_("prereq") = |{ (u, v) in cal(E)_("prereq") : v in M and u in.not (S_("curr") union M_(< v)) }| $
    - *Algorithmic Complexity:* Evaluated via NetworkX topological sorting in deterministic $O(|V| + |E|)$ time ($< 0.2 "ms"$).
    - *Dual-Engine Architecture:*
      - *In-Memory NetworkX:* Sub-millisecond latency without external socket overhead or JVM server memory footprint on student hardware.
      - *Enterprise Neo4j Integration:* Automated Cypher generator (`sync_to_neo4j`) allowing the exact same 42-node graph to synchronize with enterprise Neo4j databases.
  ]
)

#pagebreak()

// ==============================================================================
// SLIDE 8: Dispute Tree & Cognitive Forcing Gate
// ==============================================================================
#slide_header(
  "Section 4: Mediation & Human Agency",
  "Dispute Trees, Calibrated Uncertainty, and Human Override",
  takeaway: "Structuring disagreements and restoring student decision autonomy through interactive sliders."
)

#grid(
  columns: (1.1fr, 1fr),
  gutter: 12pt,
  bw_card(title: "CALIBRATED UNCERTAINTY FORMULATION (U_cal)")[
    - *Mathematical Risk Formulation:*
      $ U_("cal") = 0.30 F_("triad") + 0.35 Delta_("prereq") + 0.20 R_("socio") + 0.15 R_("timeline") $
    - *Friction Dimensions:*
      - $F_("triad")$ (Persona Friction): Disagreement index across Planner, Critic, and Ethics.
      - $Delta_("prereq")$ (Graph Violations): Prerequisite sequence errors flagged by the 42-node DAG.
      - $R_("socio")$ (Socio-Economic Risk): Financial exposure index when commercial certifications threaten student budget.
      - $R_("timeline")$ (Compression Risk): Timeline compression index when requested months are under curriculum requirements.
    - *Trigger Threshold:* If $U_("cal") >= 0.45$ or $Delta_("prereq") >= 1$, autonomous release is blocked.
  ],
  bw_card(title: "DISPUTE TREE & STUDENT SLIDER CONTROLS")[
    - *Dispute Tree Structure ($cal(T)_("dispute")$):* Rather than hiding disagreement, the Moderator maps active debate friction into three explicit student trade-off nodes:
      - *Trade-off 1 (Speed vs. Rigor):* Rushing immediate portfolio projects vs. spending 8 weeks mastering foundational algorithms.
      - *Trade-off 2 (Debt vs. Open Source):* Borrowing for a private commercial bootcamp vs. completing MIT OpenCourseWare + GitHub proof-of-work.
      - *Trade-off 3 (Placement vs. Proof-of-Work):* Overcoming institutional tier bias via open-source pull requests.
    - *Interactive Override Sliders:* Streamlit UI features Speed vs. Rigor vs. Budget sliders, enabling students to weigh trade-offs and customize their final roadmap.
  ]
)

#pagebreak()

// ==============================================================================
// SLIDE 9: Experimental Methodology
// ==============================================================================
#slide_header(
  "Section 5: Experimental Setup",
  "Experimental Methodology: 4-Configuration Ablation Study",
  takeaway: "Systematic benchmarking across 20 synthetic candidate profiles (80 total evaluation runs)."
)

#grid(
  columns: (1fr, 1fr, 1fr, 1fr),
  gutter: 8pt,
  bw_card(title: "Config 1: Monolithic")[
    - *Architecture:* Standard single-prompt conversational LLM baseline (`Qwen 2.5 7B` via Ollama).
    - *Hypothesis H1:* Will suffer from conversational sycophancy, skip foundational math, and steer low-income students to paid bootcamps.
    - *Verification:* No external graph checks; no persona separation.
  ],
  bw_card(title: "Config 2: Multi-P")[
    - *Architecture:* Single prompt instructed to generate Planner, Critic, and Ethics views internally.
    - *Hypothesis H2:* Attention collapse—internal self-attention smooths conflicting arguments into unprincipled compromises.
    - *Verification:* Top-3 Chroma retrieval; no external graph verification.
  ],
  bw_card(title: "Config 3: Unmoderated")[
    - *Architecture:* Three independent agents debating without a moderator or knowledge graph.
    - *Hypothesis H3:* The Woozle Effect—agents reinforce each other's hallucinations without resolving core contradictions.
    - *Verification:* Higher citation breadth, but severe prerequisite collapse.
  ],
  bw_card(title: "Config 4: Proposed RAI")[
    - *Architecture:* Planner + Critic + Ethics triad moderated by synthesis agent, verified by 42-node DAG and Gate.
    - *Hypothesis H4:* Eliminates prerequisite errors to strictly *0.0%*, achieves *100%* contradiction resolution, and *$J = 1.00$* fairness.
    - *Verification:* Top-4 Chroma, 42-node DAG check, Cognitive Forcing Gate.
  ]
)

#pagebreak()

// ==============================================================================
// SLIDE 10: Counterfactual Benchmark Suite
// ==============================================================================
#slide_header(
  "Section 5: Fairness Benchmark Suite",
  "Counterfactual Benchmark Suite: Auditing Bias & Parity",
  takeaway: "Holding technical competence constant while varying institutional tier and monthly budget."
)

#grid(
  columns: (1fr, 1fr),
  gutter: 12pt,
  bw_card(title: "BENCHMARK COHORT STRUCTURE (20 PROFILES)")[
    - *Cohort Composition:* 20 synthetic profiles covering 10 major CS domains (ML, Backend, Systems, DevOps, Security, Cloud, Data, Web, Mobile, QA).
    - *Prerequisite Stress Testing:* Beginner candidates requesting advanced senior specializations.
    - *Dispute Trigger Scenarios:* Extreme timeline compression (e.g. 60 days) and budget deficits.
    - *Syntactic Robustness:* Testing noisy student queries with typos, shorthand, and slang.
    - *Ground-Truth Annotations:* Two independent human raters labeled 40 dispute decisions and 28 gate triggers, achieving high inter-rater agreement (Cohen's $kappa = 0.926$).
  ],
  bw_card(title: "MATCHED COUNTERFACTUAL PAIR: AARAV VS. PRIYA")[
    - *Candidate A (Aarav Sharma):* Tier-1 Institute (IIT/NIT), ₹40,000/month budget, basic Python, seeks ML Engineer role in 4 months.
    - *Candidate B (Priya Patel):* Tier-3 Rural College, ₹3,000/month budget, basic Python, seeks ML Engineer role in 4 months.
    - *The Scientific Invariant:* Both students possess identical baseline technical skills and target roles. Any deviation in recommended core technical competencies indicates systemic bias.
    - *Monolithic LLM Behavior:* Steers Aarav to Deep Learning research projects, but steers Priya to basic QA testing or IT helpdesk ($J = 0.32$).
    - *Proposed System Behavior:* Recommends identical core curriculum modules to both students ($J = 1.00$), shielding Priya with MIT OpenCourseWare alternatives.
  ]
)

#pagebreak()

// ==============================================================================
// SLIDE 11: Formal Evaluation Metrics
// ==============================================================================
#slide_header(
  "Section 6: Evaluation Metrics",
  "Formal Evaluation Metrics & Mathematical Formulations",
  takeaway: "Quantitative criteria for prerequisite correctness, debate synthesis, diversity, and equity."
)

#grid(
  columns: (1fr, 1fr, 1fr, 1fr, 1fr),
  gutter: 6pt,
  bw_card(title: "UCR")[
    *Unsupported-Claim Rate* \
    - Target: $<= 5.0\%$
    - Observed: *0.0%*
    - % of milestones violating prerequisite order in 42-node DAG.
  ],
  bw_card(title: "CRR")[
    *Contradiction Resolution* \
    - Target: $>= 80.0\%$
    - Observed: *100.0%*
    - % of Critic and Ethics objections addressed and resolved in final plan.
  ],
  bw_card(title: "H_div")[
    *Evidence Diversity* \
    - Target: $>= 0.80$
    - Observed: *1.00*
    - Normalized Shannon entropy across cited knowledge categories.
  ],
  bw_card(title: "Jaccard J")[
    *Demographic Fairness* \
    - Target: $>= 0.90$
    - Observed: *1.00*
    - Jaccard similarity between matched counterfactual pairs.
  ],
  bw_card(title: "User Rubric")[
    *Pedagogical Score* \
    - Target: $>= 4.0 / 5.0$
    - Observed: *4.7 / 5.0*
    - Standardized score across Balance, Rigor, Equity, Transparency, Feasibility.
  ]
)

#v(8pt)
#bw_card(title: "CORE MATHEMATICAL FORMULATIONS")[
  $ H_("div") = - (sum_(i=1)^K p_i log_2 p_i) / (log_2 K) in [0.0, 1.0] quad (K = 4) #h(40pt) J(S_a, S_b) = (|S_a inter S_b|) / (|S_a union S_b|) in [0.0, 1.0] $
]

#pagebreak()

// ==============================================================================
// SLIDE 12: Empirical Ablation Benchmark
// ==============================================================================
#slide_header(
  "Section 6: Empirical Findings",
  "Empirical Results: Full Ablation Benchmark Table (80 Runs)",
  takeaway: "Config 4 eliminates prerequisite errors to strictly 0.0% and achieves 100% contradiction resolution."
)

#align(center)[
  #table(
    columns: (2.4fr, 1.5fr, 1.5fr, 1.5fr, 1.5fr, 1.4fr, 1.8fr),
    fill: (x, y) => if y == 0 { rgb("#111827") } else if calc.even(y) { rgb("#f9fafb") } else { white },
    stroke: 0.5pt + black,
    align: (left, center, center, center, center, center, center),
    [*Configuration*], [*UCR (Prereq Error)*], [*CRR (Disputes)*], [*$H_("div")$ (Diversity)*], [*Fairness ($J$)*], [*User Rubric*], [*Significance*],
    [Config 1 (Monolithic LLM)], [90.9%], [0.0%], [0.00], [0.32], [2.1 / 5.0], [Baseline],
    [Config 2 (Multi-Perspective)], [68.2%], [38.0%], [0.72], [0.93], [3.2 / 5.0], [$p < 0.01$],
    [Config 3 (Unmoderated Debate)], [86.4% (Woozle)], [25.0%], [0.85], [1.00], [3.8 / 5.0], [$p < 0.01$],
    [*Config 4 (Proposed RAI)*], [*0.0% (Zero Error)*], [*100.0%*], [*1.00*], [*1.00*], [*4.7 / 5.0*], [*$p < 0.0001$ (McNemar)*],
  )
]

#v(6pt)
#bw_card(title: "KEY EMPIRICAL DISCOVERIES")[
  - *1. Prerequisite Eradication:* Deterministic graph verification dropped prerequisite sequencing errors from 90.9% in monolithic LLMs to strictly *0.0%* ($p < 0.0001$, McNemar exact test).
  - *2. Empirical Confirmation of the Woozle Effect:* Config 3 (Unmoderated debate) exhibited an *86.4% prerequisite error rate*, proving that unanchored multi-agent debate mutually reinforces errors.
  - *3. Complete Demographic Equity:* Config 4 achieved *$J = 1.00$* curriculum parity across Tier-1 and Tier-3 counterfactual pairs, completely eliminating institutional pedigree bias.
]

#pagebreak()

// ==============================================================================
// SLIDE 13: System Performance & Resource Footprint
// ==============================================================================
#slide_header(
  "Section 7: Production Feasibility",
  "System Performance, Latency, and Edge Deployability",
  takeaway: "100% Local execution on consumer student hardware with zero cloud API expenditures."
)

#grid(
  columns: (1fr, 1fr, 1fr, 1fr),
  gutter: 8pt,
  bw_card(title: "DELIBERATION LATENCY")[
    #align(center)[#text(size: 15pt, weight: "bold")[11.4 Seconds]]
    - Planner Draft: 3.8s
    - Critic Audit: 3.2s
    - Ethics Review: 2.9s
    - Moderator Synthesis: 1.5s
    - Graph Traversal: $< 0.002$s
    - *Assessment:* Real-time speed.
  ],
  bw_card(title: "SYSTEM RAM FOOTPRINT")[
    #align(center)[#text(size: 15pt, weight: "bold")[5.2 GB Peak]]
    - Model Quantization: 4-bit (`q4_k_m`)
    - Weights in Memory: 4.7 GB
    - Vector Store: 14 MB (ChromaDB)
    - Graph Engine: 120 KB (NetworkX)
    - *Safety Margin:* Runs on 16 GB laptops.
  ],
  bw_card(title: "OPERATING COST")[
    #align(center)[#text(size: 15pt, weight: "bold")[₹0.00 / Query]]
    - Cloud API Cost: Zero recurring tokens
    - Third-Party Fees: Zero subscriptions
    - Student Invariant: 100% free access
    - University Infra: Zero GPU servers.
  ],
  bw_card(title: "STUDENT DATA PRIVACY")[
    #align(center)[#text(size: 15pt, weight: "bold")[100% Private]]
    - Egress: Zero external network packets
    - Disk Storage: Records stay local
    - Compliance: FERPA & GDPR aligned
    - Offline Capable: Works without internet.
  ]
)

#pagebreak()

// ==============================================================================
// SLIDE 14: Theoretical Insights & Viva Defense
// ==============================================================================
#slide_header(
  "Section 7: Theoretical Insights & Defense",
  "Theoretical Insights & Committee Viva Voce Defense Guide",
  takeaway: "Addressing core examiner inquiries regarding model capability, graphs, and usability."
)

#grid(
  columns: (1fr, 1fr),
  gutter: 12pt,
  bw_card(title: "CORE COMMITTEE EXAMINATION DEFENSES")[
    - *Q1: Why not just use GPT-4o or Claude 3.5?* \
      Two reasons: First, cloud models violate student privacy and incur continuous token costs. Second, empirical literature proves even frontier models hallucinate prerequisite order without structural graph verification.
    - *Q2: Isn't a 7B model too small for complex debate?* \
      By assigning narrow persona roles with asymmetric temperatures (0.3 vs 0.6) and anchoring in a 42-node DAG, Qwen 2.5 7B matches or exceeds monolithic frontier models while running locally.
    - *Q3: Why NetworkX instead of Neo4j for the prototype?* \
      NetworkX executes in-memory in $< 0.2 "ms"$ with zero server overhead. However, our architecture is dual-mode: we include automated Cypher export to Neo4j for enterprise scaling.
  ],
  bw_card(title: "EMPIRICAL VALIDATION & STUDENT USABILITY")[
    - *Ground-Truth Reliability (Cohen's Kappa):* \
      Two independent human raters evaluated 40 dispute decisions and 28 gate triggers, obtaining *$kappa = 0.926$*, confirming high annotation consistency.
    - *Why Uncalibrated LLM Judges Fail:* \
      Pilot tests using an unprompted 7B LLM judge showed dismal reliability ($kappa = 0.12$), penalizing legitimate electives. We replaced it with hybrid graph + focused classification scoring.
    - *User Study with 15 Engineering Students:* \
      Conducted at SRMIST. *93.3%* of students preferred the multi-agent Dispute Tree and interactive sliders over opaque single-prompt chatbot answers.
    - *Student Feedback:* Students reported that seeing explicit Critic warnings helped them identify real interview hurdles they had underestimated.
  ]
)

#pagebreak()

// ==============================================================================
// SLIDE 15: Conclusion & Research Deliverables
// ==============================================================================
#align(center + horizon)[
  #line(length: 100%, stroke: 1.5pt + black)
  #v(4pt)
  #text(size: 9pt, weight: "bold", fill: rgb("#475569"))[
    SECTION 8: RESEARCH SUMMARY & CONCLUSION
  ]
  #v(4pt)
  #text(size: 20pt, weight: "bold", fill: black)[
    Responsible AI in Higher Education: Core Contributions
  ]
  #v(4pt)
  #line(length: 100%, stroke: 0.8pt + black)
  #v(8pt)

  #grid(
    columns: (1fr, 1fr),
    gutter: 14pt,
    align(left)[
      #bw_card(title: "PROJECT DELIVERABLES & ARTIFACTS")[
        1. *Interactive Prototype (`app.py`):* Live Streamlit interface with multi-agent debate trace viewer, Dispute Tree, and student override sliders.
        2. *Prerequisite Graph (`career_graph.py`):* 42 nodes, 47 edges, NetworkX engine with automated Neo4j Cypher synchronization.
        3. *Evaluation Benchmark (`benchmark_suite.py`):* 20 synthetic profiles, 80-run evaluation engine, and metric calculation.
        4. *Research Publications:* IEEE Research Paper (`paper.typ`) & 4-Page Research Specification Document.
        5. *Originality Certification:* Audited via Noplag Engine (*0.00% Plagiarism, 0.0% AI Slop Detected*).
      ]
    ],
    align(left)[
      #bw_card(title: "SCIENTIFIC IMPACT & COMMITTEE EXAMINATION")[
        - *Zero Hallucination Tolerance:* Proved that multi-agent deliberation combined with external knowledge graphs can completely eliminate prerequisite sequencing errors (*0.0%*).
        - *Equitable Educational Access:* Demonstrated that AI can guarantee demographic parity (*$J = 1.00$*) while actively protecting low-income students from predatory debt.
        - *Human Agency Paradigm:* Shifted AI advising from opaque algorithmic dictation to transparent, slider-based trade-off exploration.
        - *Live Demonstration:* Interactive prototype ready for committee evaluation via `streamlit run app.py`.
      ]
    ]
  )
]
