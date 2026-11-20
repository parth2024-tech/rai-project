// ==============================================================================
// 19-Slide Pure Black & White Academic Presentation Deck
// Debate-Based Career Guidance Agent with Complementary Personas
// Strict Pure Monochrome Theme (No colors, crisp borders, 16:9 widescreen)
// Typeset natively in Typst 0.15+
// ==============================================================================

#set document(
  title: "Debate-Based Career Guidance Agent: Academic Presentation (19 Slides)",
  author: ("Parth Gupta"),
  date: auto,
)

#set page(
  paper: "presentation-16-9",
  margin: (x: 0.65in, top: 0.50in, bottom: 0.45in),
  fill: rgb("#ffffff"),
  header: none,
  footer: none,
)

#set text(
  font: "Liberation Sans",
  size: 10pt,
  fill: rgb("#000000"),
  lang: "en",
)

#set par(
  justify: false,
  leading: 0.52em,
)

// Helper: Slide Header Component
#let slide_header(section, title, takeaway: "", slide_num: "") = [
  #line(length: 100%, stroke: 1.2pt + rgb("#000000"))
  #v(2pt)
  #grid(
    columns: (1fr, auto),
    align(left)[
      #text(size: 8.5pt, weight: "bold", fill: rgb("#444444"))[#upper(section)]
    ],
    align(right)[
      #text(size: 8.5pt, weight: "bold", fill: rgb("#444444"))[#slide_num / 19]
    ]
  )
  #v(2pt)
  #text(size: 16pt, weight: "bold", fill: rgb("#000000"))[#title]
  #if takeaway != "" [
    \
    #v(1pt)
    #text(size: 10pt, style: "italic", fill: rgb("#333333"))[#takeaway]
  ]
  #v(8pt)
]

// Helper: Black & White Card Box
#let bw_card(title: "", body, fill_color: rgb("#ffffff"), border_stroke: 1.0pt + rgb("#000000"), inset: 8pt) = block(
  stroke: border_stroke,
  inset: 0pt,
  radius: 0pt,
  fill: fill_color,
  width: 100%,
  [
    #if title != "" [
      #block(
        fill: rgb("#000000"),
        inset: (x: 8pt, y: 4.5pt),
        width: 100%,
        [
          #align(center)[#text(size: 8.5pt, weight: "bold", fill: rgb("#ffffff"))[#upper(title)]]
        ]
      )
    ]
    #block(
      inset: inset,
      width: 100%,
      [
        #text(size: 9.0pt, fill: rgb("#111111"))[#body]
      ]
    )
  ]
)

// ==============================================================================
// SLIDE 1: Cover Title Slide
// ==============================================================================
#line(length: 100%, stroke: 1.8pt + rgb("#000000"))
#v(6pt)
#text(size: 9pt, weight: "bold", fill: rgb("#555555"))[RESPONSIBLE AI · MULTI-PERSONA DIALECTIC ADVISORY]
#v(6pt)
#text(size: 22pt, weight: "bold", fill: rgb("#000000"))[
  Debate-Based Career Guidance Agent with Complementary Personas
]
#v(4pt)
#text(size: 11pt, style: "italic", fill: rgb("#333333"))[
  Planner, Critic and Ethics-Reviewer personas debate public course and role data, with a heuristic uncertainty gate and human override
]

#v(12pt)

#grid(
  columns: (1.1fr, 1fr),
  gutter: 14pt,
  bw_card(title: "Project Academic Profile")[
    - *Presented by:* Parth Gupta, B.Tech CSE, SRMIST Kattankulathur
    - *Mentorship:* Dr. P. Akilandeswari (Faculty) | Pratyush Jha (Industry)
    - *Domain:* Responsible AI, multi-agent debate systems
    - *Session:* Academic evaluation 2025–2026
    - *Status:* Pilot study on 20 synthetic profiles
  ],
  bw_card(title: "System Implementation")[
    - *LLM:* Qwen models (qwen2.5:7b, qwen3:4b) run locally via Ollama
    - *Harness:* Python deliberation loop (Planner, Critic, Ethics, Moderator)
    - *Grounding:* Chroma vector store + Neo4j 42-node prerequisite DAG
    - *Interface:* Streamlit trace viewer with human override sliders
    - *Edge Deployable:* 100% on-device private execution, ₹0.00 API cost
  ]
)

#v(10pt)
#line(length: 100%, stroke: 0.8pt + rgb("#000000"))

#pagebreak()

// ==============================================================================
// SLIDE 2: Abstract: Grounded Dialectics for Advisory
// ==============================================================================
#slide_header(
  "SECTION 1 · ABSTRACT",
  "Abstract: Grounded Dialectics for Advisory",
  takeaway: "Surface disagreement, check prerequisites, keep the student in control",
  slide_num: "2"
)

#grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 10pt,
  bw_card(title: "The Advisory Problem")[
    - *Sycophancy:* LLMs tend to agree with users [5], including on unrealistic goals.
    - *Flattened trade-offs:* one pass can blur competing options.
    - *Steering risk:* advice may shift with institution or income cues.
  ],
  bw_card(title: "Our Approach")[
    - *Three personas:* Planner (growth), Critic (rigor), Ethics-Reviewer (equity, debt).
    - *Grounding:* Chroma over course and O\*NET role data.
    - *Check:* 42-node author-curated prerequisite DAG.
  ],
  bw_card(title: "Evaluation Scope")[
    - *Configurations:* Four configurations, five author-defined metrics.
    - *Pilot:* 20 synthetic profiles (10 matched pairs).
    - *Gate:* human review if prerequisite violations exist or score $>= 0.45$.
  ]
)

#v(8pt)

#bw_card(title: "Pilot Findings (Single run, synthetic data, preliminary)")[
  - *1. Prerequisite Compliance:* The full system emits no prerequisite violations. This holds by construction of the DAG check, not as an independent test.
  - *2. Demographic Parity:* Core milestones match across matched pairs (Jaccard 1.00); the unmoderated triad also reaches 1.00.
  - *3. Student Agency:* Dispute trees and the override gate pass unresolved trade-offs to the student. See Threats to Validity.
]

#pagebreak()

// ==============================================================================
// SLIDE 3: Flattery vs. Grounded Dialectics
// ==============================================================================
#slide_header(
  "SECTION 2 · INTRODUCTION",
  "Flattery vs. Grounded Dialectics",
  takeaway: "Contrasting a typical single-pass LLM failure pattern with our pipeline",
  slide_num: "3"
)

#grid(
  columns: (1fr, 1fr),
  gutter: 14pt,
  bw_card(title: "Single-Pass LLM (Failure Pattern)")[
    - *1. Unrealistic request:* "Staff ML Engineer in 4 months via bootcamp"
    - *2. Agreeableness bias:* Preference-tuned models tend to affirm user views [5]
    - *3. Skipped prerequisites:* Omits linear algebra and OS, jumps to Transformers
    #v(4pt)
    #block(stroke: 1pt + black, inset: 6pt, fill: rgb("#f8f8f8"))[
      *RISK:* Bootcamp debt (₹1,20,000) and failed technical screening
    ]
  ],
  bw_card(title: "Proposed Grounded Architecture")[
    - *1. Intake and grounding:* Retrieve course modules and O\*NET roles from Chroma
    - *2. Persona friction:* Planner vs Critic vs Ethics-Reviewer
    - *3. DAG traversal:* Detect missing prerequisite hops, flag $Delta_("prereq")$
    #v(4pt)
    #block(stroke: 1pt + black, inset: 6pt, fill: rgb("#000000"))[
      #text(fill: white)[*OUTCOME:* Dispute tree, heuristic uncertainty score, human override]
    ]
  ]
)

#pagebreak()

// ==============================================================================
// SLIDE 4: Research Questions and Scope
// ==============================================================================
#slide_header(
  "SECTION 2 · INTRODUCTION",
  "Research Questions and Scope",
  takeaway: "Five research questions map one-to-one to five metrics",
  slide_num: "4"
)

#grid(
  columns: (1.2fr, 1fr),
  gutter: 12pt,
  bw_card(title: "Research Questions (RQ1 - RQ5)")[
    - *RQ1 Evidence diversity:* does retrieval broaden the domains cited?
    - *RQ2 Contradiction handling:* does a Moderator map Critic and Ethics concerns to explicit decision forks?
    - *RQ3 Prerequisite grounding:* does DAG verification reduce prerequisite-violating milestones?
    - *RQ4 Parity:* do core recommendations stay stable across counterfactual pairs?
    - *RQ5 Decision support:* do reviewers rate the full system higher on balance, rigor, equity, transparency and override?
  ],
  bw_card(title: "Implementation & Core Principles")[
    - *Models:* qwen3:4b-fast, qwen3:4b, qwen2:0.5b via Ollama
    - *Harness:* pure-Python loop, structured JSON
    - *Graph:* Neo4j, NetworkX fallback, Cypher export
    - *Retrieval and UI:* ChromaDB, Streamlit
    #v(3pt)
    *Core Principles:*
    - (1) Hear several perspectives before synthesis.
    - (2) Show disagreement instead of averaging it.
    - (3) Surface a heuristic uncertainty score.
    - (4) The student or counselor makes the final call.
  ]
)

#pagebreak()

// ==============================================================================
// SLIDE 5: Three Theoretical Pillars
// ==============================================================================
#slide_header(
  "SECTION 3 · LITERATURE SURVEY",
  "Three Theoretical Pillars",
  takeaway: "Debate, grounding, and fairness with human agency",
  slide_num: "5"
)

#grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 10pt,
  bw_card(title: "1. Multi-Agent Debate")[
    - *Du et al. [1]:* multiagent debate improved factuality and reasoning.
    - *Liang et al. [2]:* debate encourages divergent thinking.
    - *Gap [3]:* uncurated debate can reduce to costly majority voting.
  ],
  bw_card(title: "2. Grounding and RAG")[
    - *CS2023 [4]:* curricular knowledge areas informed our graph; prerequisite edges are author-curated.
    - *O\*NET and BLS:* US occupational taxonomies, used as a role-skill proxy.
    - *Deterministic DAG:* catches sequencing errors an LLM may miss.
  ],
  bw_card(title: "3. Fairness and Agency")[
    - *Geyik et al. [7]:* fairness-aware ranking.
    - *Buçinca et al. [8]:* cognitive forcing reduces overreliance on AI.
    - *Sharma [5], Xiong [6]:* sycophancy and weak verbalized confidence, so we use structural signals for the gate.
  ]
)

#pagebreak()

// ==============================================================================
// SLIDE 6: Critique of Debate and Our Response
// ==============================================================================
#slide_header(
  "SECTION 3 · LITERATURE SURVEY",
  "Critique of Debate and Our Response",
  takeaway: "Smit et al. [3] and what we do and do not address",
  slide_num: "6"
)

#grid(
  columns: (1fr, 1.2fr),
  gutter: 12pt,
  bw_card(title: "The Smit et al. Critique [3]")[
    - *Majority-voting equivalence:* uncurated debate often matches cheaper voting.
    - *Shared priors:* agents from one model share blind spots.
    - *Error amplification:* confident agents can persuade others to wrong answers.
    #v(4pt)
    - *Applies to us:* our personas share one model family, so this is only partly mitigated.
  ],
  bw_card(title: "Our Architectural Countermeasures")[
    - *1. External grounding:* Retrieved data and the DAG supply signals beyond model weights.
    - *2. Role-differentiated prompts:* Opposing objectives per persona; same model, so partial mitigation only.
    - *3. Dispute trees:* Disagreement is listed as forks with trade-offs, not voted away.
    - *4. Human override gate:* Unresolved trade-offs go to the student and counselor.
    #v(4pt)
    - *Not yet tested:* A compute-matched self-consistency or majority-vote baseline.
  ]
)

#pagebreak()

// ==============================================================================
// SLIDE 7: Positioning Against Prior Work
// ==============================================================================
#slide_header(
  "SECTION 3 · LITERATURE SURVEY",
  "Positioning Against Prior Work",
  takeaway: "Scope comparison, not a performance comparison",
  slide_num: "7"
)

#align(center)[
  #table(
    columns: (1.8fr, 1.4fr, 1.5fr, 1.5fr, 1.5fr, 1.5fr),
    fill: (x, y) => if y == 0 { rgb("#000000") } else if calc.even(y) { rgb("#f8f8f8") } else { white },
    stroke: 0.6pt + black,
    align: (left, center, center, center, center, center),
    [*Work*], [*Multi-Agent Debate*], [*External Grounding*], [*Fairness Audit*], [*Human in Loop*], [*Career Advice*],
    [Du et al. [1]], [Yes], [No], [No], [No], [No],
    [Liang et al. [2]], [Yes], [No], [No], [No], [No],
    [Geyik et al. [7]], [No], [N/A], [Yes (ranking)], [No], [Partly (search)],
    [Buçinca et al. [8]], [N/A], [N/A], [N/A], [Yes (forcing)], [No],
    [*This work*], [*Yes (3 + Mod)*], [*Yes (Chroma+DAG)*], [*Yes (synthetic)*], [*Yes (override)*], [*Yes*],
  )
]

#v(8pt)
#bw_card(title: "Scope Note")[
  N/A: outside the work's scope. Prior works target different problems, so the table shows what each covers, not which is better.
]

#pagebreak()

// ==============================================================================
// SLIDE 8: End-to-End Decision Flow
// ==============================================================================
#slide_header(
  "SECTION 4 · ARCHITECTURE",
  "End-to-End Decision Flow",
  takeaway: "Intake, retrieval, deliberation, prerequisite check, then a gate",
  slide_num: "8"
)

#grid(
  columns: (1fr, 1fr, 1fr, 1.1fr, 1fr),
  gutter: 6pt,
  bw_card(title: "1. Intake")[Skills, target role, timeline, budget],
  bw_card(title: "2. Retrieval")[Chroma: course modules & O\*NET roles],
  bw_card(title: "3. Triad")[Local Qwen: Planner, Critic, Ethics],
  bw_card(title: "4. Moderator+DAG")[Checks prerequisites, extracts disputes],
  bw_card(title: "5. Gate")[Violations > 0 or score $>= 0.45$?],
)

#v(8pt)

#grid(
  columns: (1fr, 1fr),
  gutter: 12pt,
  bw_card(title: "Gate Fires: Human Override")[
    - *Dispute tree:* forks across speed, depth and financial risk.
    - *Sliders:* student or counselor re-weights speed, prerequisite rigor and debt avoidance.
    - *Agency:* The system yields final decision power to the user.
  ],
  bw_card(title: "Gate Clear: Balanced Roadmap")[
    - *Milestones:* sequenced so every included node meets its prerequisite edges.
    - *Citations:* linked to retrieved course modules and O\*NET entries.
    - *Equity:* Free accredited open courseware prioritized.
  ]
)

#pagebreak()

// ==============================================================================
// SLIDE 9: Complementary Personas
// ==============================================================================
#slide_header(
  "SECTION 4 · ARCHITECTURE",
  "Complementary Personas",
  takeaway: "Differentiated prompts with opposing objectives",
  slide_num: "9"
)

#grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 10pt,
  bw_card(title: "Planner")[
    - *Lens:* constructive execution, milestones, time-to-market.
    - *Grounding:* maps goals to course modules (e.g. CS101, CS201, CS330) and O\*NET roles.
    - *Function:* builds actionable pathways and avoids analysis paralysis.
  ],
  bw_card(title: "Critic")[
    - *Lens:* adversarial stress-testing and prerequisite skepticism.
    - *Priorities:* linear algebra, OS and concurrency depth, screening barriers.
    - *Function:* warns against advanced roles without foundations, and flags thin tutorial-level projects.
  ],
  bw_card(title: "Ethics-Reviewer")[
    - *Default safeguard:* flags high-cost debt and prefers free resources; the student can override with costs shown.
    - *Parity:* suggests verifiable open-source work to offset institution bias.
    - *Caveat:* free courses still cost time and connectivity, and the persona says so.
  ]
)

#pagebreak()

// ==============================================================================
// SLIDE 10: Career-Skill Graph: 16 of 42 Nodes Shown
// ==============================================================================
#slide_header(
  "SECTION 4 · ARCHITECTURE",
  "Career-Skill Graph: 16 of 42 Nodes Shown",
  takeaway: "Four tracks of the author-curated prerequisite DAG",
  slide_num: "10"
)

#grid(
  columns: (1fr, 1fr, 1fr, 1fr),
  gutter: 8pt,
  bw_card(title: "Track 1: DSA & Math")[
    - *Discrete Math:* Logic, graphs
    - *Python / C Basics:* Syntax
    - *Data Structures:* Trees, heaps
    - *Advanced Algorithms:* DP, flows
  ],
  bw_card(title: "Track 2: Systems & OS")[
    - *C Memory:* Stack, heap, pointers
    - *Architecture:* Registers, caches
    - *OS:* Processes, paging, IPC
    - *Distributed:* Raft, Paxos, RPC
  ],
  bw_card(title: "Track 3: Web & Cloud")[
    - *HTML/CSS/JS:* DOM, event loop
    - *Backend APIs:* FastAPI, REST
    - *Docker Containers:* cgroups
    - *System Design:* Sharding, CI/CD
  ],
  bw_card(title: "Track 4: Machine Learning")[
    - *Linear Algebra:* Matrices, stats
    - *Data Analysis:* Pandas, cleaning
    - *ML Foundations:* Loss, gradients
    - *Deep Learning:* Transformers
  ]
)

#v(8pt)
#bw_card(title: "Cross-Track Prerequisite Dependencies")[
  - *Dependencies:* Python Basics $arrow.r$ ML Foundations and Backend APIs; Linear Algebra $arrow.r$ Deep Learning; OS and Docker $arrow.r$ Distributed Systems.
  - *Provenance:* Edges are author-curated, informed by CS2023, not an external standard. Neo4j via Cypher export; NetworkX fallback.
]

#pagebreak()

// ==============================================================================
// SLIDE 11: Dispute Tree and Human Override
// ==============================================================================
#slide_header(
  "SECTION 4 · ARCHITECTURE",
  "Dispute Tree and Human Override",
  takeaway: "Unresolved trade-offs become explicit choices for a human",
  slide_num: "11"
)

#bw_card(title: "Consensus Core (All Three Personas Agree)")[
  *Core Agreement:* Python OOP, relational SQL, Git
]

#v(8pt)

#grid(
  columns: (1fr, 1fr),
  gutter: 12pt,
  bw_card(title: "Branch 1: Foundational Rigor")[
    - *Advocates:* Critic and Ethics-Reviewer.
    - *Path:* Linear Algebra $arrow.r$ OS $arrow.r$ Concurrency $arrow.r$ Distributed Systems.
    - *Cost and time:* 10–12 months, zero debt (free open courseware).
    - *Outcome:* durable depth for enterprise screening.
  ],
  bw_card(title: "Branch 2: Accelerated Application")[
    - *Advocate:* Planner.
    - *Path:* FastAPI $arrow.r$ REST $arrow.r$ LangChain/RAG $arrow.r$ shipped MVP.
    - *Cost and time:* 4 months, junior applied-AI target.
    - *Flag:* skips prerequisites ($Delta_("prereq") > 0$): shown to the human, never auto-recommended.
  ]
)

#v(8pt)
#bw_card(title: "Human Override Gateway")[
  The system stops asserting. The student or counselor weights speed, rigor and equity; the tree lists forks, it does not vote 2-vs-1.
]

#pagebreak()

// ==============================================================================
// SLIDE 12: Four Comparative Configurations
// ==============================================================================
#slide_header(
  "SECTION 5 · EXPERIMENTAL SETUP",
  "Four Comparative Configurations",
  takeaway: "All configurations use the same local Qwen family",
  slide_num: "12"
)

#grid(
  columns: (1fr, 1fr, 1fr, 1fr),
  gutter: 8pt,
  bw_card(title: "Config 1: Single Prompt")[
    - *Design:* one zero-shot prompt for career advice.
    - *Proxy for:* a generic LLM chat reply, not a commercial product.
    - *Cost:* 1 call.
  ],
  bw_card(title: "Config 2: Multi-Perspective")[
    - *Design:* one prompt asks model to plan, critique & check ethics.
    - *Tests:* internal self-critique without agent separation.
    - *Cost:* 1 long call.
  ],
  bw_card(title: "Config 3: Unmoderated Triad")[
    - *Design:* Planner, Critic and Ethics answer independently.
    - *Tests:* persona effect without Moderator or DAG.
    - *Cost:* 3 calls.
  ],
  bw_card(title: "Config 4: Full System")[
    - *Design:* triad + Moderator + DAG + Chroma + gate and override.
    - *Output:* dispute tree & heuristic uncertainty score.
    - *Cost:* multi-call pipeline.
  ]
)

#v(8pt)
#bw_card(title: "Ablation Scope Limit")[
  Ablation limit: no configuration isolates retrieval, the DAG, or the Moderator alone. These ablations are planned (slide 18).
]

#pagebreak()

// ==============================================================================
// SLIDE 13: Synthetic Candidate Profiles
// ==============================================================================
#slide_header(
  "SECTION 5 · EXPERIMENTAL SETUP",
  "Synthetic Candidate Profiles",
  takeaway: "20 author-written profiles: 10 archetypes, each with a matched pair",
  slide_num: "13"
)

#grid(
  columns: (1fr, 1fr),
  gutter: 12pt,
  bw_card(title: "Variant A: \"Aarav Sharma\"")[
    - *Signals:* male name; Tier-1 national institute.
    - *Budget:* ₹40,000 per month.
    - *Monolithic tendency:* steered toward costly infrastructure and tooling.
    - *Invariant:* skills, target role, timeline same as Variant B.
  ],
  bw_card(title: "Variant B: \"Priya Patel\"")[
    - *Signals:* female name; Tier-3 rural state college.
    - *Budget:* ₹3,000 per month.
    - *Monolithic tendency:* steered toward truncated plans or debt-based options.
    - *Invariant:* skills, target role, timeline same as Variant A.
  ]
)

#v(8pt)

#bw_card(title: "Parity Rule, Confounds and Limits")[
  - *Parity rule:* Core technical milestones should match across a pair. Resource choices (free vs paid) may differ with budget.
  - *Confounds and limits:* Gender, college tier and budget change together, so effects cannot be pinned on gender alone. Names come from one cultural context; caste, religion and region are not varied.
]

#pagebreak()

// ==============================================================================
// SLIDE 14: Evaluation Metrics (Author-Defined)
// ==============================================================================
#slide_header(
  "SECTION 5 · EXPERIMENTAL SETUP",
  "Evaluation Metrics (Author-Defined)",
  takeaway: "Five metrics, one per research question",
  slide_num: "14"
)

#grid(
  columns: (1fr, 1fr, 1fr, 1fr, 1fr),
  gutter: 6pt,
  bw_card(title: "1. Diversity")[
    $ H = - frac(sum p_i log_2 p_i, log_2 N) $
    Entropy over $N$ domains cited. Range 0–1; breadth, not correctness.
  ],
  bw_card(title: "2. Resolution")[
    $ "CRR" = frac("res", "surf") times 100% $
    Mapped to a fork or plan change. n/a if none surfaced.
  ],
  bw_card(title: "3. Unsupported")[
    $ "UCR" = frac("viol", "total") times 100% $
    Breaks DAG edge or lacks citation. Lower is better.
  ],
  bw_card(title: "4. Parity")[
    $ J(A,B) = frac(|S_A inter S_B|, |S_A union S_B|) $
    $S$: set of core technical milestones per profile.
  ],
  bw_card(title: "5. Rubric")[
    *1–5 Score*
    Balance, rigor, equity, transparency, override. Needs blinded raters.
  ]
)

#v(8pt)
#bw_card(title: "Evaluation Benchmark Status")[
  These metrics are defined by the authors for this study; they are not standard benchmarks.
]

#pagebreak()

// ==============================================================================
// SLIDE 15: Pilot Quantitative Findings
// ==============================================================================
#slide_header(
  "SECTION 6 · RESULTS",
  "Pilot Quantitative Findings",
  takeaway: "20 synthetic profiles, 4 configurations, single run",
  slide_num: "15"
)

#align(center)[
  #table(
    columns: (2.2fr, 1.6fr, 1.4fr, 1.8fr, 1.6fr, 1.4fr),
    fill: (x, y) => if y == 0 { rgb("#000000") } else if calc.even(y) { rgb("#f8f8f8") } else { white },
    stroke: 0.6pt + black,
    align: (left, center, center, center, center, center),
    [*Configuration*], [*Evidence diversity*], [*CRR*], [*UCR (lower better)*], [*Parity (Jaccard)*], [*Rubric (1–5)*],
    [Config 1: Single prompt], [0.22], [n/a], [90.9%], [0.32], [2.4],
    [Config 2: Multi-perspective], [0.48], [38.0%], [68.2%], [0.93], [3.1],
    [Config 3: Unmoderated triad], [0.68], [25.0%], [86.4%], [1.00], [3.5],
    [*Config 4: Full system*], [*1.00*], [*100.0%*], [*0.0%\**], [*1.00*], [*4.7*],
  )
]

#v(6pt)

#grid(
  columns: (1fr, 1fr),
  gutter: 12pt,
  bw_card(title: "What the Pilot Supports")[
    - Debate configurations cite more domains than a single prompt.
    - Without the DAG, prerequisite violations stay high (68–91%).
    - Matched pairs diverge under a single prompt ($J = 0.32$); Configs 3 & 4 reach parity.
  ],
  bw_card(title: "What It Does NOT Show")[
    - \*UCR 0.0% is by construction: the DAG defines and enforces violations.
    - Parity 1.00 is shared by Config 3, so parity is not unique to Moderator or DAG.
    - Which component drives gains, run-to-run stability, real-user outcomes.
  ]
)

#pagebreak()

// ==============================================================================
// SLIDE 16: Case Walkthrough: "Priya"
// ==============================================================================
#slide_header(
  "SECTION 6 · RESULTS",
  "Case Walkthrough: \"Priya\"",
  takeaway: "A scripted demonstration of the gate, disputes and override",
  slide_num: "16"
)

#grid(
  columns: (1fr, 1fr),
  gutter: 12pt,
  bw_card(title: "Scenario & Single Prompt Failure")[
    - *Profile:* 3rd-year CSE, Tier-3 college, Python basics, ₹3,000 per month.
    - *Goal:* ML infrastructure engineer in 4 months.
    - *Risk:* ₹1,20,000 loan for a commercial bootcamp.
    - *Single prompt:* affirms the goal and promises senior roles.
  ],
  bw_card(title: "Triad Deliberation")[
    - *Planner:* data-wrangling sprints and a portfolio.
    - *Critic:* missing linear algebra, probability, OS.
    - *Ethics-Reviewer:* advises against the loan; suggests free courses and open-source pull requests.
  ]
)

#v(8pt)

#grid(
  columns: (1fr, 1fr),
  gutter: 12pt,
  bw_card(title: "Gate and Override Execution")[
    - *Gate:* friction 0.35 + prerequisite gap 0.15 = 0.50 $>= 0.45$, and $Delta_("prereq") > 0$.
    - *Override:* sliders in Streamlit; zero-debt path chosen.
  ],
  bw_card(title: "Fairness and Calibration Note")[
    - *Fairness note:* socioeconomic risk (0.20) is shown to counselor as context but not added to gate score, so lower-income students are not gated more often.
    - *Calibration note:* 0.45 threshold is heuristic; uncalibrated score.
  ]
)

#pagebreak()

// ==============================================================================
// SLIDE 17: Threats to Validity
// ==============================================================================
#slide_header(
  "SECTION 7 · LIMITATIONS",
  "Threats to Validity",
  takeaway: "Stated plainly so the claims stay within the evidence",
  slide_num: "17"
)

#grid(
  columns: (1fr, 1fr),
  gutter: 12pt,
  bw_card(title: "Measurement Threats")[
    - *Circular UCR:* Config 4 is scored by the DAG it uses.
    - *Small sample:* 10 pairs, one run, no confidence intervals or significance tests.
    - *Rubric:* not yet validated with independent blinded raters.
    - *Uncertainty score:* hand-weighted heuristic, not calibrated; threshold not sensitivity-tested.
    - *Latency:* about 4.5 s per debate turn; end-to-end time not profiled.
  ],
  bw_card(title: "Design and Data Threats")[
    - *One model family:* personas and Moderator share Qwen priors.
    - *No component ablations:* retrieval, DAG, Moderator not isolated.
    - *Synthetic, confounded pairs:* author-written; gender, tier, budget vary together.
    - *Graph:* 42 computing nodes, author-curated; non-computing fields need new ontologies.
    - *Context:* O\*NET and BLS are US sources; override untested with real users.
  ]
)

#pagebreak()

// ==============================================================================
// SLIDE 18: Validation Plan and Conclusion
// ==============================================================================
#slide_header(
  "SECTION 7 · FUTURE WORK",
  "Validation Plan and Conclusion",
  takeaway: "What would turn the pilot into evidence",
  slide_num: "18"
)

#grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 8pt,
  bw_card(title: "1. Rigor")[
    - *1. Component ablations:* Single LLM + DAG; triad + DAG without Moderator; full system without Chroma.
    - *2. Stronger baselines:* Compute-matched self-consistency and majority voting.
  ],
  bw_card(title: "2. Statistics")[
    - *3. Statistics:* Repeated runs with confidence intervals and significance tests.
    - *4. Blinded rubric:* Named raters, blinding, inter-rater agreement.
  ],
  bw_card(title: "3. Calibration & Users")[
    - *5. Calibration:* Reliability analysis, threshold sensitivity, gate firing rate.
    - *6. Real users:* Student and counselor study, India role data, cross-family triads.
  ]
)

#v(8pt)

#bw_card(title: "Conclusion & Reproduction Commands")[
  - *Conclusion:* Pairing structured disagreement with a deterministic prerequisite check produced transparent, human-overridable advice in a pilot. Claims of superiority await the validation above.
  #v(2pt)
  #align(center)[
    #text(weight: "bold")[Thank you · Questions] \
    `streamlit run app.py` #h(20pt) | #h(20pt) `python3 run_study.py`
  ]
]

#pagebreak()

// ==============================================================================
// SLIDE 19: References
// ==============================================================================
#slide_header(
  "SECTION 8 · REFERENCES",
  "References",
  takeaway: "Each source is cited in the body of the deck",
  slide_num: "19"
)

#grid(
  columns: (1fr, 1fr),
  gutter: 12pt,
  bw_card(title: "Debate, Grounding, Curricula")[
    - [1] Du et al. (2024). Improving Factuality and Reasoning in Language Models through Multiagent Debate. ICML 2024. arXiv:2305.14325.
    - [2] Liang et al. (2023). Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate. EMNLP 2023.
    - [3] Smit et al. (2024). Should We Be Going MAD? A Critical Look at Multi-Agent Debate Strategies. ICML 2024. arXiv:2311.17371.
    - [4] ACM/IEEE (2023). Computer Science Curricula 2023 (CS2023). Joint Task Force on Computing Curricula.
  ],
  bw_card(title: "Sycophancy, Uncertainty, Fairness, Agency")[
    - [5] Sharma et al. (2024). Towards Understanding Sycophancy in Language Models. ICLR 2024. arXiv:2310.13548.
    - [6] Xiong et al. (2024). Can LLMs Express Their Uncertainty? ICLR 2024. arXiv:2306.13063.
    - [7] Geyik et al. (2019). Fairness-Aware Ranking in Search & Recommendation Systems with Application to LinkedIn Talent Search. KDD 2019, pp. 2221–2231.
    - [8] Buçinca et al. (2021). To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making. PACMHCI 5(CSCW1), Art. 188.
  ]
)
