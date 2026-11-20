// ==============================================================================
// Exact 15-Slide Pure Black & White Presentation Deck
// Matches the user's exact consolidated project slides verbatim
// Strict Monochrome Theme (No colors, pure white background, crisp black borders)
// Typeset natively in Typst 0.15+
// ==============================================================================

#set document(
  title: "Debate-Based Career Guidance Agent: Exact 15-Slide Presentation",
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

// Helper: Header Component
#let slide_header(title, subtitle: "", slide_num: "") = [
  #line(length: 100%, stroke: 1.2pt + rgb("#000000"))
  #v(2pt)
  #grid(
    columns: (1fr, auto),
    align(left)[
      #text(size: 8.5pt, weight: "bold", fill: rgb("#444444"))[RESPONSIBLE AI · MULTI-PERSONA DIALECTIC ADVISORY]
    ],
    align(right)[
      #text(size: 8.5pt, weight: "bold", fill: rgb("#444444"))[#slide_num / 15]
    ]
  )
  #v(2pt)
  #text(size: 16pt, weight: "bold", fill: rgb("#000000"))[#title]
  #if subtitle != "" [
    \
    #v(1pt)
    #text(size: 10pt, style: "italic", fill: rgb("#333333"))[#subtitle]
  ]
  #v(8pt)
]

// Helper: Card Box Component
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
  Planner, Critic and Ethics-Reviewer personas debate public course and role data, with an uncertainty gate and human override
]

#v(12pt)

#grid(
  columns: (1.1fr, 1fr),
  gutter: 14pt,
  bw_card(title: "Project")[
    - *Presented by:* Parth Gupta, B.Tech CSE, SRMIST Kattankulathur
    - *Domain:* Responsible AI, multi-agent debate systems
    - *Session:* Academic evaluation 2025–2026
    - *Status:* Pilot study on 20 synthetic profiles
  ],
  bw_card(title: "Implementation")[
    - *LLM:* Qwen models run locally via Ollama
    - *Harness:* Python loop (Planner, Critic, Ethics, Moderator)
    - *Grounding:* Chroma vector store + 42-node prerequisite graph
    - *Interface:* Streamlit trace viewer with human override
  ]
)

#v(10pt)
#line(length: 100%, stroke: 0.8pt + rgb("#000000"))

#pagebreak()

// ==============================================================================
// SLIDE 2: Abstract
// ==============================================================================
#slide_header(
  "Abstract",
  subtitle: "Surface disagreement, check prerequisites, keep the student in control",
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
    - *Check:* 42-node author-curated prerequisite graph.
  ],
  bw_card(title: "Evaluation Scope")[
    - *Scope:* Four configurations, five author-defined metrics.
    - *Pilot:* 20 synthetic profiles (10 matched pairs).
    - *Gate:* human review if prerequisite violations exist or score $>= 0.45$.
  ]
)

#v(8pt)

#bw_card(title: "Pilot Findings (single run, synthetic data, preliminary)")[
  - *1. Graph Verification:* The full system emits no prerequisite violations. This holds by construction of the graph check, not as an independent test.
  - *2. Demographic Parity:* Core milestones match across matched pairs (Jaccard 1.00); the unmoderated triad also reaches 1.00.
  - *3. Student Agency:* Dispute trees and the override gate pass unresolved trade-offs to the student. See Limitations.
]

#pagebreak()

// ==============================================================================
// SLIDE 3: Problem: Single-Pass LLM vs. Proposed Pipeline
// ==============================================================================
#slide_header(
  "Problem: Single-Pass LLM vs. Proposed Pipeline",
  subtitle: "Contrasting a typical single-pass LLM failure pattern with our pipeline",
  slide_num: "3"
)

#grid(
  columns: (1fr, 1fr),
  gutter: 14pt,
  bw_card(title: "Single-Pass LLM (Failure Pattern)")[
    - *1. Unrealistic request:* "Staff ML Engineer in 4 months via bootcamp"
    - *2. Agreeableness bias:* Preference-tuned models tend to affirm user views [5]
    - *3. Skipped prerequisites:* Omits linear algebra and OS, jumps to Transformers
    #v(6pt)
    #block(stroke: 1pt + black, inset: 6pt, fill: rgb("#f8f8f8"))[
      *Risk:* Bootcamp debt (₹1,20,000) and failed technical screening
    ]
  ],
  bw_card(title: "Proposed Grounded Architecture")[
    - *1. Intake and grounding:* Retrieve course modules and O\*NET roles from Chroma
    - *2. Persona friction:* Planner vs. Critic vs. Ethics-Reviewer
    - *3. Graph traversal:* Detect missing prerequisite hops, flag $Delta_("prereq")$
    #v(6pt)
    #block(stroke: 1pt + black, inset: 6pt, fill: rgb("#000000"))[
      #text(fill: white)[*Outcome:* Dispute tree, uncertainty score, human override]
    ]
  ]
)

#pagebreak()

// ==============================================================================
// SLIDE 4: Literature Survey
// ==============================================================================
#slide_header(
  "Literature Survey",
  subtitle: "Debate, grounding, and fairness with human agency",
  slide_num: "4"
)

#grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 10pt,
  bw_card(title: "1. Multi-Agent Debate")[
    - *Du et al. [1]:* debate improved factuality and reasoning.
    - *Liang et al. [2]:* debate encourages divergent thinking.
    - *Smit et al. [3]:* uncurated debate can reduce to costly majority voting.
  ],
  bw_card(title: "2. Grounding and RAG")[
    - *CS2023 [4]:* curricular knowledge areas informed our graph; edges are author-curated.
    - *O\*NET and BLS:* US occupational taxonomies, used as a role-skill proxy.
    - *Prerequisite graph:* catches sequencing errors an LLM may miss.
  ],
  bw_card(title: "3. Fairness and Agency")[
    - *Geyik et al. [7]:* fairness-aware ranking.
    - *Buçinca et al. [8]:* cognitive forcing reduces overreliance on AI.
    - *Sharma [5], Xiong [6]:* sycophancy and weak verbalized confidence, so the gate uses structural signals.
  ]
)

#v(8pt)

#bw_card(title: "Critique of Debate (Smit et al. [3]) and Our Response")[
  - *Concerns:* debate may match majority voting, share priors, and amplify confident errors.
  - *Our response:* external grounding, role-differentiated prompts, dispute trees, human override gate.
  - *Limit:* personas share one model family (partial mitigation); no compute-matched majority-vote baseline yet.
]

#pagebreak()

// ==============================================================================
// SLIDE 5: Positioning Against Prior Work
// ==============================================================================
#slide_header(
  "Positioning Against Prior Work",
  subtitle: "Scope comparison, not a performance comparison",
  slide_num: "5"
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
    [Geyik et al. [7]], [No], [N/A], [Yes (ranking parity)], [No], [Partly (talent search)],
    [Buçinca et al. [8]], [N/A], [N/A], [N/A], [Yes (cognitive forcing)], [No],
    [*This work*], [*Yes (3 + Mod)*], [*Yes (Chroma + graph)*], [*Yes (synthetic)*], [*Yes (override gate)*], [*Yes*],
  )
]

#v(8pt)
#bw_card(title: "Scope Note")[
  N/A: outside the work's scope. Prior works target different problems, so this table shows what each covers, not which is better.
]

#pagebreak()

// ==============================================================================
// SLIDE 6: System Architecture: End-to-End Decision Flow
// ==============================================================================
#slide_header(
  "System Architecture: End-to-End Decision Flow",
  subtitle: "Intake, retrieval, deliberation, prerequisite check, then a gate",
  slide_num: "6"
)

#grid(
  columns: (1fr, 1fr, 1fr, 1.1fr, 1fr),
  gutter: 6pt,
  bw_card(title: "1. Intake")[Skills, role, timeline, budget],
  bw_card(title: "2. Retrieval")[Chroma: courses and O\*NET roles],
  bw_card(title: "3. Triad")[Local Qwen: Planner, Critic, Ethics],
  bw_card(title: "4. Moderator+Graph")[Checks prerequisites, extracts disputes],
  bw_card(title: "5. Gate")[Violations > 0 or score $>= 0.45$?],
)

#v(8pt)

#grid(
  columns: (1fr, 1fr),
  gutter: 12pt,
  bw_card(title: "Gate Fires: Human Override")[
    - *Dispute tree:* forks across speed, depth and financial risk.
    - *Sliders:* student or counselor re-weights speed, prerequisite rigor and debt avoidance.
  ],
  bw_card(title: "Gate Clear: Balanced Roadmap")[
    - *Milestones:* sequenced so every included node meets its prerequisite edges.
    - *Citations:* linked to retrieved course modules and O\*NET entries.
  ]
)

#v(6pt)
#bw_card(title: "Implementation Details")[
  Models qwen3:4b-fast, qwen3:4b, qwen2:0.5b via Ollama · pure-Python loop with structured JSON · Neo4j graph (NetworkX fallback) · ChromaDB · Streamlit
]

#pagebreak()

// ==============================================================================
// SLIDE 7: Complementary Personas
// ==============================================================================
#slide_header(
  "Complementary Personas",
  subtitle: "Differentiated prompts with opposing objectives",
  slide_num: "7"
)

#align(center)[
  #table(
    columns: (1.2fr, 2.2fr, 2.2fr, 2.4fr),
    fill: (x, y) => if y == 0 { rgb("#000000") } else if calc.even(y) { rgb("#f8f8f8") } else { white },
    stroke: 0.6pt + black,
    align: (left, left, left, left),
    [*Persona*], [*Lens*], [*Focus*], [*Function*],
    [Planner], [Constructive execution, milestones, time-to-market], [Maps goals to course modules (e.g. CS101, CS201, CS330) and O\*NET roles], [Builds actionable pathways and avoids analysis paralysis],
    [Critic], [Adversarial stress-testing and prerequisite skepticism], [Linear algebra, OS and concurrency depth, screening barriers], [Warns against advanced roles without foundations; flags thin tutorial-level projects],
    [Ethics-Reviewer], [Equity and debt safeguards], [Flags high-cost debt and prefers free resources; student can override with costs shown], [Suggests verifiable open-source work to offset institution bias; notes free courses still cost time and connectivity],
  )
]

#pagebreak()

// ==============================================================================
// SLIDE 8: Career-Skill Graph: 16 of 42 Nodes Shown
// ==============================================================================
#slide_header(
  "Career-Skill Graph: 16 of 42 Nodes Shown",
  subtitle: "Four tracks of the author-curated prerequisite DAG",
  slide_num: "8"
)

#grid(
  columns: (1fr, 1fr, 1fr, 1fr),
  gutter: 8pt,
  bw_card(title: "Track 1: DSA and Math")[
    - *Discrete Math:* Logic, graph theory
    - *Python / C Basics:* Syntax, control flow
    - *Data Structures:* Trees, heaps, graphs
    - *Advanced Algorithms:* Dynamic programming
  ],
  bw_card(title: "Track 2: Systems and OS")[
    - *C Memory & Pointers:* Stack, heap, alloc
    - *Computer Architecture:* Registers, caches
    - *Operating Systems:* Processes, paging
    - *Distributed Systems:* Raft, Paxos
  ],
  bw_card(title: "Track 3: Web and Cloud")[
    - *HTML / CSS / JS:* DOM, event loop
    - *Backend APIs:* FastAPI, REST routing
    - *Docker Containers:* Namespaces, cgroups
    - *System Design, CI/CD:* Load balancing
  ],
  bw_card(title: "Track 4: Machine Learning")[
    - *Linear Algebra & Stats:* Eigenvalues
    - *Data Analysis (Pandas):* Wrangling
    - *ML Foundations:* Loss, gradients
    - *Deep Learning & LLMs:* Transformers
  ]
)

#v(8pt)
#bw_card(title: "Graph Navigation & Curricular Provenance")[
  Read each column top to bottom (prerequisite order). Cross-track edges: Python Basics $arrow.r$ ML Foundations and Backend APIs; Linear Algebra $arrow.r$ Deep Learning; OS and Docker $arrow.r$ Distributed Systems. Edges are author-curated, informed by CS2023, not an external standard.
]

#pagebreak()

// ==============================================================================
// SLIDE 9: Dispute Tree and Human Override
// ==============================================================================
#slide_header(
  "Dispute Tree and Human Override",
  subtitle: "Unresolved trade-offs become explicit choices for a human",
  slide_num: "9"
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
    - *Flag:* skips prerequisites ($Delta_("prereq") > 0$); shown to the human, never auto-recommended.
  ]
)

#v(8pt)
#bw_card(title: "Human Override Gateway")[
  The system stops asserting. The student or counselor weights speed, rigor and equity; the tree lists forks, it does not vote 2-vs-1.
]

#pagebreak()

// ==============================================================================
// SLIDE 10: Experimental Setup: Configurations and Profiles
// ==============================================================================
#slide_header(
  "Experimental Setup: Configurations and Profiles",
  subtitle: "Systematic benchmarking across 20 synthetic candidate profiles",
  slide_num: "10"
)

#align(center)[
  #table(
    columns: (2.2fr, 4.4fr, 2.4fr),
    fill: (x, y) => if y == 0 { rgb("#000000") } else if calc.even(y) { rgb("#f8f8f8") } else { white },
    stroke: 0.6pt + black,
    align: (left, left, left),
    [*Configuration*], [*Design*], [*Tests / Cost*],
    [Config 1: Single prompt], [One zero-shot prompt for career advice (proxy for generic chat reply)], [1 call],
    [Config 2: Multi-perspective], [One prompt asks model to plan, critique and check ethics], [Internal self-critique; 1 long call],
    [Config 3: Unmoderated triad], [Planner, Critic and Ethics answer independently], [Persona effect without Moderator or graph; 3 calls],
    [*Config 4: Full system*], [*Triad + Moderator + graph + Chroma + gate and override*], [*Dispute tree & uncertainty score; multi-call*],
  )
]

#v(6pt)
#bw_card(title: "Synthetic Profiles: 20 Author-Written (10 Archetypes, Each with a Matched Pair)")[
  - *Variant A "Aarav Sharma":* male name, Tier-1 national institute, ₹40,000 per month.
  - *Variant B "Priya Patel":* female name, Tier-3 rural state college, ₹3,000 per month.
  - *Parity rule:* skills, target role and timeline are identical; core milestones should match, free vs. paid resources may differ.
  - *Confounds:* gender, tier and budget change together; names come from one cultural context.
]

#pagebreak()

// ==============================================================================
// SLIDE 11: Research Questions and Evaluation Metrics
// ==============================================================================
#slide_header(
  "Research Questions and Evaluation Metrics",
  subtitle: "Five research questions map one-to-one to five metrics",
  slide_num: "11"
)

#align(center)[
  #table(
    columns: (2.4fr, 2.2fr, 3.4fr),
    fill: (x, y) => if y == 0 { rgb("#000000") } else if calc.even(y) { rgb("#f8f8f8") } else { white },
    stroke: 0.6pt + black,
    align: (left, left, left),
    [*Research Question*], [*Metric*], [*Definition*],
    [RQ1: Does retrieval broaden domains cited?], [Evidence diversity: $H = - frac(sum p_i log_2 p_i, log_2 N)$], [Entropy over $N$ domains cited; range 0–1; breadth, not correctness],
    [RQ2: Does Moderator map concerns to forks?], [$"CRR" = frac("resolved", "surfaced") times 100%$], [Resolved: concern mapped to a fork or plan change],
    [RQ3: Does graph verification reduce violations?], [$"UCR" = frac("violating", "total") times 100%$], [Violating: breaks graph edge or lacks citation; lower is better],
    [RQ4: Do core recommendations stay stable?], [Parity: $J(A,B) = frac(|S_A inter S_B|, |S_A union S_B|)$], [$S$: set of core technical milestones for each profile in a pair],
    [RQ5: Do reviewers rate full system higher?], [Rubric score, 1–5], [Balance, rigor, equity, transparency, override; needs blinded raters],
  )
]

#v(8pt)
#bw_card(title: "Metric Provenance Note")[
  These metrics are defined by the authors for this study; they are not standard benchmarks.
]

#pagebreak()

// ==============================================================================
// SLIDE 12: Pilot Quantitative Results
// ==============================================================================
#slide_header(
  "Pilot Quantitative Results",
  subtitle: "20 synthetic profiles, 4 configurations, single run",
  slide_num: "12"
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

#v(4pt)
#text(size: 8.5pt, fill: rgb("#333333"))[
  20 synthetic profiles, 4 configurations, single run. \*UCR 0.0% holds by construction: the graph defines and enforces violations.
]

#v(4pt)

#grid(
  columns: (1fr, 1fr),
  gutter: 12pt,
  bw_card(title: "What the Pilot Supports")[
    - Debate configurations cite more domains than a single prompt.
    - Without the graph, prerequisite violations stay high (68–91%).
    - Matched pairs diverge under a single prompt ($J = 0.32$); Configs 3 and 4 reach parity.
  ],
  bw_card(title: "What It Does NOT Show")[
    - Parity 1.00 is shared by Config 3, so it is not unique to the Moderator or graph.
    - Which component drives the gains.
    - Run-to-run stability and real-user outcomes.
  ]
)

#pagebreak()

// ==============================================================================
// SLIDE 13: Case Walkthrough: "Priya"
// ==============================================================================
#slide_header(
  "Case Walkthrough: \"Priya\"",
  subtitle: "A scripted demonstration of the gate, disputes and override",
  slide_num: "13"
)

#grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 10pt,
  bw_card(title: "Scenario")[
    - *Profile:* 3rd-year CSE, Tier-3 college, Python basics, ₹3,000 per month.
    - *Goal:* ML infrastructure engineer in 4 months.
    - *Risk:* ₹1,20,000 loan for a bootcamp.
    - *Single prompt:* affirms the goal and promises senior roles.
  ],
  bw_card(title: "Triad Deliberation")[
    - *Planner:* data-wrangling sprints and a portfolio.
    - *Critic:* missing linear algebra, probability, OS.
    - *Ethics-Reviewer:* advises against the loan; suggests free courses and open-source pull requests.
  ],
  bw_card(title: "Gate and Override")[
    - *Gate:* friction 0.35 + prerequisite gap 0.15 = 0.50 $>= 0.45$, and $Delta_("prereq") > 0$.
    - *Override:* sliders in Streamlit; zero-debt path chosen.
  ]
)

#v(8pt)

#bw_card(title: "Fairness and Calibration Note")[
  - *Fairness note:* socioeconomic risk (0.20) is shown to the counselor as context but is not added to the gate score, so lower-income students are not gated more often.
  - *Calibration note:* The 0.45 threshold is a heuristic setting and the score is uncalibrated.
]

#pagebreak()

// ==============================================================================
// SLIDE 14: Limitations, Future Work and Conclusion
// ==============================================================================
#slide_header(
  "Limitations, Future Work and Conclusion",
  subtitle: "Threats to validity, empirical validation plan, and research summary",
  slide_num: "14"
)

#grid(
  columns: (1fr, 1fr),
  gutter: 12pt,
  bw_card(title: "Threats to Validity")[
    - *Circular UCR:* Config 4 is scored by the graph it uses.
    - *Small sample:* 10 pairs, one run, no confidence intervals.
    - *Rubric:* not validated with blinded raters.
    - *Uncertainty score:* is hand-weighted and uncalibrated.
    - *One model family:* no component ablations.
    - *Data:* Synthetic, confounded pairs; US-based O\*NET and BLS data.
    - *Users:* Override untested with real users; latency ~4.5 s per turn.
  ],
  bw_card(title: "Validation Plan")[
    - *Ablations:* Component ablations (graph only, no Moderator, no Chroma).
    - *Baselines:* Compute-matched majority-vote baselines.
    - *Statistics:* Repeated runs with confidence intervals and significance tests.
    - *Blinded rubric:* with inter-rater agreement.
    - *Calibration:* and threshold sensitivity.
    - *Real users:* Student and counselor study, India-specific role data.
  ]
)

#v(6pt)

#bw_card(title: "Conclusion & Closing")[
  - *Conclusion:* Pairing structured disagreement with a deterministic prerequisite check produced transparent, human-overridable advice in a pilot. Claims of superiority await the validation above.
  #v(2pt)
  #align(center)[#text(weight: "bold")[Thank you · Questions]]
]

#pagebreak()

// ==============================================================================
// SLIDE 15: References
// ==============================================================================
#slide_header(
  "References",
  subtitle: "Each source is cited in the body of the deck",
  slide_num: "15"
)

#grid(
  columns: (1fr, 1fr),
  gutter: 12pt,
  bw_card(title: "References [1] - [4]")[
    - [1] Du et al. (2024). Improving Factuality and Reasoning in Language Models through Multiagent Debate. ICML 2024. arXiv:2305.14325.
    - [2] Liang et al. (2023). Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate. EMNLP 2023.
    - [3] Smit et al. (2024). Should We Be Going MAD? A Critical Look at Multi-Agent Debate Strategies. ICML 2024. arXiv:2311.17371.
    - [4] ACM/IEEE (2023). Computer Science Curricula 2023 (CS2023). Joint Task Force on Computing Curricula.
  ],
  bw_card(title: "References [5] - [8]")[
    - [5] Sharma et al. (2024). Towards Understanding Sycophancy in Language Models. ICLR 2024. arXiv:2310.13548.
    - [6] Xiong et al. (2024). Can LLMs Express Their Uncertainty? ICLR 2024. arXiv:2306.13063.
    - [7] Geyik et al. (2019). Fairness-Aware Ranking in Search & Recommendation Systems with Application to LinkedIn Talent Search. KDD 2019, pp. 2221–2231.
    - [8] Buçinca et al. (2021). To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making. PACMHCI 5(CSCW1), Art. 188.
  ]
)
