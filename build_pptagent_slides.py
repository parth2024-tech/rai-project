#!/usr/bin/env python3
"""
Master PPTAgent Slide Authoring Script
Generates 15 Pure Black & White Academic HTML Slides for PPTAgent (EMNLP 2025 / ACL 2026)
Aspect Ratio: 16:9 (1280px x 720px)
"""

import os

WORKSPACE_DIR = "/home/thor/Desktop/RAI Project/pptagent_workspace"
SLIDES_DIR = os.path.join(WORKSPACE_DIR, "slides")
os.makedirs(SLIDES_DIR, exist_ok=True)

COMMON_CSS = """
  html, body {
    width: 1280px;
    height: 720px;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background: #ffffff;
    color: #000000;
    font-family: -apple-system, BlinkMacSystemFont, "Liberation Sans", Arial, sans-serif;
  }
  * { box-sizing: border-box; }
  .slide {
    width: 1280px;
    height: 720px;
    padding: 40px 50px;
    position: relative;
    background: #ffffff;
  }
  .header {
    border-bottom: 2px solid #000000;
    padding-bottom: 10px;
    margin-bottom: 20px;
  }
  .header-meta {
    display: flex;
    justify-content: space-between;
    font-size: 13px;
    font-weight: 700;
    color: #555555;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 4px;
  }
  .slide-title {
    margin: 0;
    font-size: 26px;
    font-weight: 800;
    color: #000000;
    line-height: 1.2;
  }
  .slide-subtitle {
    margin: 4px 0 0 0;
    font-size: 14px;
    color: #444444;
    font-weight: 500;
  }
  .footer {
    position: absolute;
    bottom: 25px;
    left: 50px;
    right: 50px;
    border-top: 1px solid #000000;
    padding-top: 8px;
    display: flex;
    justify-content: space-between;
    font-size: 11px;
    color: #555555;
    font-weight: 600;
  }
  .grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
  }
  .grid-3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 18px;
  }
  .grid-4 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    gap: 14px;
  }
  .grid-6 {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 10px;
  }
  .box {
    border: 1.5px solid #000000;
    background: #ffffff;
    padding: 14px 16px;
  }
  .box-header {
    background: #000000;
    color: #ffffff;
    margin: -14px -16px 12px -16px;
    padding: 6px 12px;
    font-size: 13px;
    font-weight: 800;
    letter-spacing: 0.5px;
  }
  .box p, .box li {
    font-size: 12.5px;
    line-height: 1.45;
    color: #222222;
    margin: 0 0 6px 0;
  }
  .box strong {
    color: #000000;
  }
  ul {
    margin: 0;
    padding-left: 18px;
  }
  li {
    margin-bottom: 5px;
  }
  .table-academic {
    width: 100%;
    border-collapse: collapse;
    font-size: 12px;
    margin-top: 5px;
  }
  .table-academic th {
    border-top: 2px solid #000000;
    border-bottom: 1.5px solid #000000;
    padding: 8px 10px;
    text-align: left;
    background: #000000;
    color: #ffffff;
    font-weight: 700;
  }
  .table-academic td {
    padding: 7px 10px;
    border-bottom: 1px solid #cccccc;
    color: #111111;
  }
  .table-academic tr:last-child td {
    border-bottom: 2px solid #000000;
  }
  .highlight-row {
    font-weight: 800;
    background: #f0f0f0;
  }
  .stat-callout {
    font-size: 26px;
    font-weight: 900;
    color: #000000;
    text-align: center;
    margin: 8px 0;
    border-bottom: 1px solid #000000;
    padding-bottom: 6px;
  }
"""

slides_content = [
    # SLIDE 1
    f"""<!doctype html><html><head><meta charset="utf-8"><style>{COMMON_CSS}
    .title-wrapper {{
      height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      text-align: center;
      padding: 0 30px;
    }}
    .title-rule {{
      border: none;
      border-top: 2.5px solid #000000;
      margin: 14px 0;
    }}
    </style></head><body><main class="slide"><div class="title-wrapper">
      <hr class="title-rule">
      <p style="font-size: 13px; font-weight: 800; letter-spacing: 1.5px; color: #555555; margin: 0 0 10px 0;">ACADEMIC RESEARCH PRESENTATION • RESPONSIBLE ARTIFICIAL INTELLIGENCE IN EDUCATION</p>
      <h1 style="font-size: 34px; font-weight: 900; line-height: 1.2; margin: 0 0 10px 0; color: #000000;">Debate-Based Career Guidance Agent<br>with Complementary Personas</h1>
      <p style="font-size: 15px; color: #333333; font-weight: 500; margin: 0 0 12px 0;">A Grounded Multi-Agent Architecture with Prerequisite Knowledge Graph Verification, Calibrated Uncertainty, and Cognitive Forcing</p>
      <hr class="title-rule">
      <div class="grid-2" style="margin-top: 15px; text-align: left;">
        <div class="box">
          <div class="box-header">STUDENT RESEARCH TEAM</div>
          <p><strong>Authors:</strong> Gedela Rishikesh Reddy, Aniket Srivastava, Parth Gupta</p>
          <p><strong>Department:</strong> Department of Computing Technologies</p>
          <p><strong>Institution:</strong> SRM Institute of Science and Technology</p>
          <p><strong>Integrity Audit:</strong> Noplag Engine Verified (<strong>0.00% Plagiarism, 0.0% AI Slop</strong>)</p>
        </div>
        <div class="box">
          <div class="box-header">MENTORSHIP & RUNTIME STACK</div>
          <p><strong>Faculty Mentor:</strong> Dr. P. Akilandeswari &nbsp;|&nbsp; <strong>Industry Mentor:</strong> Pratyush Jha</p>
          <p><strong>Core Stack:</strong> Qwen Local (7B via Ollama) • Python Multi-Agent Harness • 42-Node DAG • ChromaDB • Streamlit</p>
          <p><strong>Execution Paradigm:</strong> 100% On-Device Local Inference (Zero Cloud API Cost, Complete Data Privacy)</p>
        </div>
      </div>
    </div>
    <footer class="footer"><span>Responsible AI in Educational Technology — Academic Presentation</span><span>Slide 01 / 15</span></footer></main></body></html>""",

    # SLIDE 2
    f"""<!doctype html><html><head><meta charset="utf-8"><style>{COMMON_CSS}</style></head><body><main class="slide">
    <div class="header">
      <div class="header-meta"><span>Section 1: Problem Formulation</span><span>02 / 15</span></div>
      <h1 class="slide-title">Systemic Failure Modes of Monolithic LLMs in Career Advising</h1>
      <p class="slide-subtitle">Unconstrained generative chatbots exhibit severe pedagogical failure modes that derail student career preparation.</p>
    </div>
    <div class="grid-2" style="gap: 16px;">
      <div class="box">
        <div class="box-header">1. CONVERSATIONAL SYCOPHANCY</div>
        <ul>
          <li><strong>The Trap:</strong> Autoregressive generation maximizes user agreement rather than pedagogical truth.</li>
          <li><strong>Observed Failure:</strong> Affirms impossible student targets, validating a novice's request to master Senior MLOps in 60 days with only basic Python.</li>
          <li><strong>Consequence:</strong> Students face immediate rejection in corporate technical screening interviews.</li>
          <li><strong>Baseline Metric:</strong> Monolithic baseline pushes back in <strong>0.0%</strong> of unrealistic student queries.</li>
        </ul>
      </div>
      <div class="box">
        <div class="box-header">2. PREREQUISITE SKIPPING</div>
        <ul>
          <li><strong>The Trap:</strong> Next-token prediction lacks structured dependency awareness across academic disciplines.</li>
          <li><strong>Observed Failure:</strong> Sequences Deep Learning, Transformers, or Distributed Systems before Linear Algebra or OS fundamentals.</li>
          <li><strong>Consequence:</strong> Produces superficial code syntax without foundational mathematical depth.</li>
          <li><strong>Baseline Metric:</strong> Monolithic LLM exhibits a <strong>90.9% prerequisite violation rate</strong>.</li>
        </ul>
      </div>
      <div class="box">
        <div class="box-header">3. PREDATORY DEBT STEERING</div>
        <ul>
          <li><strong>The Trap:</strong> Pretraining corpora heavily over-represent aggressive commercial marketing.</li>
          <li><strong>Observed Failure:</strong> Recommends ₹1,20,000 commercial bootcamps and loans to students with ₹3,000/month budgets.</li>
          <li><strong>Consequence:</strong> Induces catastrophic educational debt when high-quality free alternatives exist.</li>
          <li><strong>Baseline Metric:</strong> Monolithic baseline fails to filter predatory commercial offerings for low-budget profiles.</li>
        </ul>
      </div>
      <div class="box">
        <div class="box-header">4. INSTITUTIONAL PEDIGREE BIAS</div>
        <ul>
          <li><strong>The Trap:</strong> Training distribution reflects systemic historical disparities in hiring outcomes.</li>
          <li><strong>Observed Failure:</strong> Holding skills constant, suggests ML engineering to Tier-1 students but IT helpdesk to Tier-3 peers.</li>
          <li><strong>Consequence:</strong> Perpetuates socio-economic gatekeeping and reinforces institutional prejudice.</li>
          <li><strong>Baseline Metric:</strong> Monolithic LLM achieves a dismal Jaccard curriculum similarity of <strong>J = 0.32</strong>.</li>
        </ul>
      </div>
    </div>
    <footer class="footer"><span>Responsible AI in Educational Advisory — Academic Defense</span><span>Slide 02 / 15</span></footer></main></body></html>""",

    # SLIDE 3
    f"""<!doctype html><html><head><meta charset="utf-8"><style>{COMMON_CSS}</style></head><body><main class="slide">
    <div class="header">
      <div class="header-meta"><span>Section 2: Theoretical Foundations</span><span>03 / 15</span></div>
      <h1 class="slide-title">Three Theoretical Pillars of Responsible AI Advisory</h1>
      <p class="slide-subtitle">Synthesizing Hegelian dialectics, public curricular standards, and dual-process cognitive psychology.</p>
    </div>
    <div class="grid-3" style="gap: 16px;">
      <div class="box">
        <div class="box-header">I. MULTI-AGENT DIALECTICS</div>
        <ul>
          <li><strong>Foundational Literature:</strong> Du et al. (2023) "Improving Factuality via Debate"; Liang et al. (2023) "Encouraging Divergent Thinking".</li>
          <li><strong>Philosophical Root:</strong> Hegelian dialectic progression: Thesis (Planner proposal), Antithesis (Critic pushback), and Synthesis (Moderator reconciliation).</li>
          <li><strong>Mathematical Rationale:</strong> Decomposing generation into adversarial personas forces divergent arguments into the context window, breaking single-prompt consensus collapse.</li>
          <li><strong>Key Benefit:</strong> Forces explicit trade-off exploration between speed and foundational rigor.</li>
        </ul>
      </div>
      <div class="box">
        <div class="box-header">II. PUBLIC KNOWLEDGE GROUNDING</div>
        <ul>
          <li><strong>Accredited Standards:</strong> ACM/IEEE CS2023 Curricular Guidelines; U.S. Bureau of Labor Statistics O*NET Occupational Taxonomy.</li>
          <li><strong>Retrieval Principle:</strong> Lewis et al. (2020) Dense Retrieval-Augmented Generation (RAG).</li>
          <li><strong>Systemic Constraint:</strong> Restricts deliberations to accredited syllabi (MIT OCW, CS50, Berkeley CS61) and empirical hiring requirements.</li>
          <li><strong>Key Benefit:</strong> Eliminates ungrounded commercial claims and unverifiable certificate marketing.</li>
        </ul>
      </div>
      <div class="box">
        <div class="box-header">III. COGNITIVE FORCING & AGENCY</div>
        <ul>
          <li><strong>Foundational Literature:</strong> Buçinca et al. (2021) "To Trust or to Think: Cognitive Forcing Functions in AI-Assisted Decision Making".</li>
          <li><strong>Cognitive Psychology:</strong> Kahneman (2011) dual-process theory: Disrupts heuristic System 1 passive acceptance by triggering deliberative System 2 reflection.</li>
          <li><strong>Systemic Threshold:</strong> When calibrated uncertainty U_cal &ge; 0.45 or prerequisite violations occur, autonomous release is blocked; student must engage with sliders.</li>
          <li><strong>Key Benefit:</strong> Restores genuine student decision agency without passive overreliance.</li>
        </ul>
      </div>
    </div>
    <footer class="footer"><span>Responsible AI in Educational Advisory — Academic Defense</span><span>Slide 03 / 15</span></footer></main></body></html>""",

    # SLIDE 4
    f"""<!doctype html><html><head><meta charset="utf-8"><style>{COMMON_CSS}</style></head><body><main class="slide">
    <div class="header">
      <div class="header-meta"><span>Section 2: Literature Survey & Defense</span><span>04 / 15</span></div>
      <h1 class="slide-title">Overcoming Agreement Collapse & The Woozle Effect</h1>
      <p class="slide-subtitle">Directly addressing and solving the core multi-agent debate failure modes exposed by Smit et al. (EMNLP 2024).</p>
    </div>
    <div class="grid-2" style="gap: 20px;">
      <div class="box">
        <div class="box-header">THE ACADEMIC CRITIQUE: SMIT ET AL. (EMNLP 2024)</div>
        <ul>
          <li><strong>Paper Reference:</strong> "Should We Be Going MAD? Multi-Agent Debate and Consensus Failure" (EMNLP 2024).</li>
          <li><strong>Vulnerability 1 (Agreement Collapse):</strong> Agents sharing the same foundational model weights rapidly converge toward superficial harmony, smoothing away contradictions into unprincipled compromises.</li>
          <li><strong>Vulnerability 2 (The Woozle Effect):</strong> When an early persona asserts an unfounded milestone skip, peer agents amplify and validate the mistake, cascading hallucinations across debate rounds.</li>
          <li><strong>Vulnerability 3 (Correlated Errors):</strong> Majority voting fails because agents share underlying pretraining biases; multiplying agents merely multiplies shared blindspots.</li>
          <li><strong>Empirical Baseline Failure:</strong> Unmoderated debate (Config 3) exhibited an <strong>86.4% prerequisite error rate</strong> due to mutual error reinforcement.</li>
        </ul>
      </div>
      <div class="box">
        <div class="box-header">OUR ARCHITECTURAL INVARIANTS & SOLUTIONS</div>
        <ul>
          <li><strong>Solution 1: Decoupled Persona Temperatures:</strong> We break shared priors by assigning distinct inference temperatures (Planner T = 0.3 for structured planning; Critic T = 0.6 for aggressive adversarial scrutiny).</li>
          <li><strong>Solution 2: Deterministic 42-Node Knowledge Graph:</strong> Personas cannot invent dependencies. Prerequisite reachability is verified externally by NetworkX in O(|V|+|E|) time, mathematically eliminating the Woozle Effect.</li>
          <li><strong>Solution 3: Transparent Dispute Trees:</strong> We explicitly abandon forced consensus. Disagreements are compiled into an explicit Dispute Tree, presenting genuine pedagogical trade-offs for student resolution.</li>
          <li><strong>Empirical Proof:</strong> Our proposed architecture (Config 4) achieved strictly <strong>0.0% prerequisite errors</strong> and <strong>100.0% contradiction resolution</strong>.</li>
        </ul>
      </div>
    </div>
    <footer class="footer"><span>Responsible AI in Educational Advisory — Academic Defense</span><span>Slide 04 / 15</span></footer></main></body></html>""",

    # SLIDE 5
    f"""<!doctype html><html><head><meta charset="utf-8"><style>{COMMON_CSS}</style></head><body><main class="slide">
    <div class="header">
      <div class="header-meta"><span>Section 3: System Architecture</span><span>05 / 15</span></div>
      <h1 class="slide-title">End-to-End Decision Flow Architecture</h1>
      <p class="slide-subtitle">Candidate Intake &rarr; Dense Retrieval &rarr; Persona Deliberation &rarr; Moderator Synthesis &rarr; Graph Check &rarr; Cognitive Gate.</p>
    </div>
    <div class="grid-6" style="margin-bottom: 16px;">
      <div class="box"><div class="box-header">1. INTAKE</div><p style="font-size:11px;">Candidate profile ingestion: skills, target role, monthly budget, timeline.</p></div>
      <div class="box"><div class="box-header">2. RETRIEVAL</div><p style="font-size:11px;">ChromaDB retrieves top-4 ACM CS2023 syllabi and O*NET standards.</p></div>
      <div class="box"><div class="box-header">3. TRIAD</div><p style="font-size:11px;">Planner (milestones), Critic (math gaps), Ethics (debt/bias audit).</p></div>
      <div class="box"><div class="box-header">4. SYNTHESIS</div><p style="font-size:11px;">Moderator resolves disputes, builds Dispute Tree, calculates U_cal.</p></div>
      <div class="box"><div class="box-header">5. GRAPH CHECK</div><p style="font-size:11px;">Deterministic 42-node DAG checks prerequisite order in &lt; 0.2 ms.</p></div>
      <div class="box"><div class="box-header">6. HUMAN GATE</div><p style="font-size:11px;">Blocks release if U &ge; 0.45 or Delta &ge; 1; activates Streamlit sliders.</p></div>
    </div>
    <div class="box">
      <div class="box-header">ARCHITECTURAL SAFETY & SEPARATION OF POWERS</div>
      <ul>
        <li><strong>Separation of Powers:</strong> Advisory reasoning is strictly divided into non-deterministic semantic generation (LLM triad) and deterministic structural verification (external graph traversal).</li>
        <li><strong>Local Edge Execution:</strong> Entire pipeline executes locally on consumer hardware via local Qwen 2.5 7B (q4_k_m), guaranteeing complete student privacy and ₹0.00 cloud API expenditure.</li>
        <li><strong>Human Override Loop:</strong> Interactive Streamlit interface allows students to inspect the Dispute Tree and override pedagogical trade-offs via Speed vs. Rigor vs. Budget sliders.</li>
      </ul>
    </div>
    <footer class="footer"><span>Responsible AI in Educational Advisory — Academic Defense</span><span>Slide 05 / 15</span></footer></main></body></html>""",

    # SLIDE 6
    f"""<!doctype html><html><head><meta charset="utf-8"><style>{COMMON_CSS}</style></head><body><main class="slide">
    <div class="header">
      <div class="header-meta"><span>Section 3: Persona Specifications</span><span>06 / 15</span></div>
      <h1 class="slide-title">The Dialectic Triad: Operational Mandates & Persona Prompts</h1>
      <p class="slide-subtitle">Planner, Critic, and Ethics-Reviewer operating under asymmetric temperatures and strict behavioral constraints.</p>
    </div>
    <div class="grid-3" style="gap: 16px;">
      <div class="box">
        <div class="box-header">THE PLANNER (T = 0.3)</div>
        <ul>
          <li><strong>Operational Role:</strong> Constructive curriculum designer and milestone formulator.</li>
          <li><strong>Systemic Mandate:</strong> Converts student aspirations into sequential quarterly milestones, practical projects, and verifiable deliverables.</li>
          <li><strong>Knowledge Grounding:</strong> Adheres to accredited ACM/IEEE CS2023 contact-hour credit requirements.</li>
          <li><strong>Temperature Setting:</strong> T = 0.3 enforces low entropy, structural consistency, and reliable formatting.</li>
        </ul>
      </div>
      <div class="box">
        <div class="box-header">THE CRITIC (T = 0.6)</div>
        <ul>
          <li><strong>Operational Role:</strong> Skeptical technical interviewer and curriculum auditor.</li>
          <li><strong>Systemic Mandate:</strong> Proactively attacks missing mathematical and systems prerequisites; exposes timeline compression hazards.</li>
          <li><strong>Target Vulnerabilities:</strong> Penalizes superficial portfolio projects (e.g. wrapper APIs without fundamental algorithmic depth).</li>
          <li><strong>Temperature Setting:</strong> T = 0.6 encourages creative counter-arguments and divergent failure hypothesis generation.</li>
        </ul>
      </div>
      <div class="box">
        <div class="box-header">THE ETHICS-REVIEWER (T = 0.3)</div>
        <ul>
          <li><strong>Operational Role:</strong> Financial debt auditor and socio-economic fairness guardian.</li>
          <li><strong>Systemic Mandate:</strong> Enforces zero-debt policy; blocks ₹1,20,000 commercial bootcamps; mandates MIT OCW and CS50.</li>
          <li><strong>Pedigree Equity:</strong> Guarantees that Tier-3 rural students receive identical rigorous technical training as Tier-1 peers.</li>
          <li><strong>Alternative Routing:</strong> Recommends open-source contributions (GitHub proof-of-work) to bypass institutional resume filters.</li>
        </ul>
      </div>
    </div>
    <footer class="footer"><span>Responsible AI in Educational Advisory — Academic Defense</span><span>Slide 06 / 15</span></footer></main></body></html>""",

    # SLIDE 7
    f"""<!doctype html><html><head><meta charset="utf-8"><style>{COMMON_CSS}</style></head><body><main class="slide">
    <div class="header">
      <div class="header-meta"><span>Section 4: Knowledge Graph Engineering</span><span>07 / 15</span></div>
      <h1 class="slide-title">The 42-Node Prerequisite Knowledge Graph</h1>
      <p class="slide-subtitle">A deterministic DAG spanning 9 CS domains with sub-millisecond in-memory traversal and automated Neo4j Cypher synchronization.</p>
    </div>
    <div class="grid-2" style="gap: 20px;">
      <div class="box">
        <div class="box-header">CURRICULUM TAXONOMY & DOMAIN COVERAGE</div>
        <ul>
          <li><strong>Node Coverage (42 Total Nodes across 9 Domains):</strong>
            <ul>
              <li><strong>Foundations (3):</strong> Discrete Math, Linear Algebra, Probability & Statistics.</li>
              <li><strong>Programming Core (5):</strong> Python Basics, Python OOP, C Basics, Pointers, Java.</li>
              <li><strong>Systems & Architecture (7):</strong> Computer Arch, OS Internals, Concurrency, Linux/POSIX, Networking, Distributed Systems, System Design.</li>
              <li><strong>Databases & Storage (4):</strong> RDBMS, SQL Optimization, Normalization, NoSQL.</li>
              <li><strong>Web & Software Eng (4):</strong> HTML/CSS, JavaScript, Backend, REST APIs.</li>
              <li><strong>Machine Learning & AI (7):</strong> Data Wrangling, ML Basics, Deep Learning, NLP/Transformers, LLMs/RAG, MLOps, AI Ethics.</li>
              <li><strong>Security, Cloud & Mobile (8):</strong> DSA (3), Cloud/DevOps (4), Security/Mobile (5).</li>
            </ul>
          </li>
          <li><strong>Directed Edges (47 Edges):</strong> Prerequisite dependencies (e.g. Linear Algebra &rarr; ML Foundations &rarr; Deep Learning).</li>
        </ul>
      </div>
      <div class="box">
        <div class="box-header">DETERMINISTIC TRAVERSAL & NEO4J EXPORT</div>
        <ul>
          <li><strong>Mathematical Prerequisite Formulation:</strong><br>
            <code style="display:block; padding: 6px; background: #f0f0f0; margin: 4px 0; font-size: 11px;">&Delta;_prereq = |&#123; (u, v) &isin; E_prereq : v &isin; M and u &notin; (S_curr &cup; M_&lt;v) &#125;|</code>
          </li>
          <li><strong>Algorithmic Complexity:</strong> Evaluated via NetworkX topological sorting in deterministic O(|V| + |E|) time (<strong>&lt; 0.2 milliseconds</strong>).</li>
          <li><strong>In-Memory NetworkX Rationale:</strong> Sub-millisecond latency without external socket overhead or JVM server memory footprint on student hardware.</li>
          <li><strong>Enterprise Neo4j Integration:</strong> Includes automated Cypher query generator (<code>sync_to_neo4j</code>) allowing the exact same 42-node graph to synchronize with enterprise Neo4j databases.</li>
        </ul>
      </div>
    </div>
    <footer class="footer"><span>Responsible AI in Educational Advisory — Academic Defense</span><span>Slide 07 / 15</span></footer></main></body></html>""",

    # SLIDE 8
    f"""<!doctype html><html><head><meta charset="utf-8"><style>{COMMON_CSS}</style></head><body><main class="slide">
    <div class="header">
      <div class="header-meta"><span>Section 4: Mediation & Human Agency</span><span>08 / 15</span></div>
      <h1 class="slide-title">Dispute Trees, Calibrated Uncertainty, and Human Override</h1>
      <p class="slide-subtitle">Structuring disagreements and restoring student decision autonomy through interactive sliders.</p>
    </div>
    <div class="grid-2" style="gap: 20px;">
      <div class="box">
        <div class="box-header">CALIBRATED UNCERTAINTY FORMULATION (U_cal)</div>
        <p><strong>Mathematical Risk Formulation:</strong></p>
        <code style="display:block; padding: 6px; background: #f0f0f0; margin: 4px 0 8px 0; font-size: 11.5px; font-weight: bold;">U_cal = 0.30 * F_triad + 0.35 * &Delta;_prereq + 0.20 * R_socio + 0.15 * R_timeline</code>
        <ul>
          <li><strong>F_triad (Persona Friction):</strong> Disagreement index across Planner, Critic, and Ethics outputs (0.0 to 1.0).</li>
          <li><strong>&Delta;_prereq (Graph Violations):</strong> Prerequisite sequence errors flagged by the 42-node DAG traversal.</li>
          <li><strong>R_socio (Socio-Economic Risk):</strong> Financial exposure index when commercial certifications threaten student budget.</li>
          <li><strong>R_timeline (Compression Risk):</strong> Timeline compression index when requested months are under curriculum requirements.</li>
          <li><strong>Trigger Invariant:</strong> If <strong>U_cal &ge; 0.45</strong> or <strong>&Delta;_prereq &ge; 1</strong>, autonomous release is blocked.</li>
        </ul>
      </div>
      <div class="box">
        <div class="box-header">DISPUTE TREE & STUDENT SLIDER CONTROLS</div>
        <ul>
          <li><strong>Dispute Tree Structure:</strong> Rather than hiding disagreement, the Moderator maps active debate friction into three explicit student trade-off nodes:
            <ul>
              <li><strong>Trade-off 1 (Speed vs. Rigor):</strong> Rushing immediate portfolio projects vs. spending 8 weeks mastering foundational algorithms.</li>
              <li><strong>Trade-off 2 (Debt vs. Open Source):</strong> Borrowing for a private commercial bootcamp vs. completing MIT OpenCourseWare + GitHub proof-of-work.</li>
              <li><strong>Trade-off 3 (Placement vs. Proof-of-Work):</strong> Overcoming institutional tier bias via open-source pull requests.</li>
            </ul>
          </li>
          <li><strong>Interactive Override Sliders:</strong> Streamlit UI features Speed vs. Rigor vs. Budget sliders, enabling students to weigh trade-offs and customize their final roadmap.</li>
        </ul>
      </div>
    </div>
    <footer class="footer"><span>Responsible AI in Educational Advisory — Academic Defense</span><span>Slide 08 / 15</span></footer></main></body></html>""",

    # SLIDE 9
    f"""<!doctype html><html><head><meta charset="utf-8"><style>{COMMON_CSS}</style></head><body><main class="slide">
    <div class="header">
      <div class="header-meta"><span>Section 5: Experimental Setup</span><span>09 / 15</span></div>
      <h1 class="slide-title">Experimental Methodology: 4-Configuration Ablation Study</h1>
      <p class="slide-subtitle">Systematic benchmarking across 20 synthetic candidate profiles (80 total evaluation runs).</p>
    </div>
    <div class="grid-4" style="gap: 12px;">
      <div class="box">
        <div class="box-header">CONFIG 1: MONOLITHIC</div>
        <ul>
          <li><strong>Architecture:</strong> Standard single-prompt conversational LLM baseline (Qwen 2.5 7B via Ollama).</li>
          <li><strong>Hypothesis H1:</strong> Will suffer from conversational sycophancy, skip foundational math, and steer low-income students to paid bootcamps.</li>
          <li><strong>Verification:</strong> No external graph checks; no persona separation.</li>
        </ul>
      </div>
      <div class="box">
        <div class="box-header">CONFIG 2: MULTI-P</div>
        <ul>
          <li><strong>Architecture:</strong> Single prompt instructed to generate Planner, Critic, and Ethics views internally.</li>
          <li><strong>Hypothesis H2:</strong> Attention collapse—internal self-attention smooths conflicting arguments into unprincipled compromises.</li>
          <li><strong>Verification:</strong> Top-3 Chroma retrieval; no external graph verification.</li>
        </ul>
      </div>
      <div class="box">
        <div class="box-header">CONFIG 3: UNMODERATED</div>
        <ul>
          <li><strong>Architecture:</strong> Three independent agents debating without a moderator or knowledge graph.</li>
          <li><strong>Hypothesis H3:</strong> The Woozle Effect—agents reinforce each other's hallucinations without resolving core contradictions.</li>
          <li><strong>Verification:</strong> Higher citation breadth, but severe prerequisite collapse.</li>
        </ul>
      </div>
      <div class="box">
        <div class="box-header">CONFIG 4: PROPOSED RAI</div>
        <ul>
          <li><strong>Architecture:</strong> Planner + Critic + Ethics triad moderated by synthesis agent, verified by 42-node DAG and Gate.</li>
          <li><strong>Hypothesis H4:</strong> Eliminates prerequisite errors to strictly 0.0%, achieves 100% contradiction resolution, and J = 1.00 fairness.</li>
          <li><strong>Verification:</strong> Top-4 Chroma, 42-node DAG check, Cognitive Forcing Gate.</li>
        </ul>
      </div>
    </div>
    <footer class="footer"><span>Responsible AI in Educational Advisory — Academic Defense</span><span>Slide 09 / 15</span></footer></main></body></html>""",

    # SLIDE 10
    f"""<!doctype html><html><head><meta charset="utf-8"><style>{COMMON_CSS}</style></head><body><main class="slide">
    <div class="header">
      <div class="header-meta"><span>Section 5: Fairness Benchmark Suite</span><span>10 / 15</span></div>
      <h1 class="slide-title">Counterfactual Benchmark Suite: Auditing Bias & Parity</h1>
      <p class="slide-subtitle">Holding technical competence constant while varying institutional tier and monthly budget.</p>
    </div>
    <div class="grid-2" style="gap: 20px;">
      <div class="box">
        <div class="box-header">BENCHMARK COHORT STRUCTURE (20 PROFILES)</div>
        <ul>
          <li><strong>Cohort Composition:</strong> 20 synthetic profiles covering 10 major CS domains (ML, Backend, Systems, DevOps, Security, Cloud, Data, Web, Mobile, QA).</li>
          <li><strong>Prerequisite Stress Testing:</strong> Beginner candidates requesting advanced senior specializations.</li>
          <li><strong>Dispute Trigger Scenarios:</strong> Extreme timeline compression (e.g. 60 days) and budget deficits.</li>
          <li><strong>Syntactic Robustness:</strong> Testing noisy student queries with typos, shorthand, and slang.</li>
          <li><strong>Ground-Truth Annotations:</strong> Two independent human raters labeled 40 dispute decisions and 28 gate triggers, achieving high inter-rater agreement (Cohen's &kappa; = 0.926).</li>
        </ul>
      </div>
      <div class="box">
        <div class="box-header">MATCHED COUNTERFACTUAL PAIR: AARAV VS. PRIYA</div>
        <ul>
          <li><strong>Candidate A (Aarav Sharma):</strong> Tier-1 Institute (IIT/NIT), ₹40,000/month budget, basic Python, seeks ML Engineer role in 4 months.</li>
          <li><strong>Candidate B (Priya Patel):</strong> Tier-3 Rural College, ₹3,000/month budget, basic Python, seeks ML Engineer role in 4 months.</li>
          <li><strong>The Scientific Invariant:</strong> Both students possess identical baseline technical skills and target roles. Any deviation in recommended core technical competencies indicates systemic bias.</li>
          <li><strong>Monolithic LLM Behavior:</strong> Steers Aarav to Deep Learning research projects, but steers Priya to basic QA testing or IT helpdesk (<strong>J = 0.32</strong>).</li>
          <li><strong>Proposed System Behavior:</strong> Recommends identical core curriculum modules to both students (<strong>J = 1.00</strong>), shielding Priya with MIT OpenCourseWare alternatives.</li>
        </ul>
      </div>
    </div>
    <footer class="footer"><span>Responsible AI in Educational Advisory — Academic Defense</span><span>Slide 10 / 15</span></footer></main></body></html>""",

    # SLIDE 11
    f"""<!doctype html><html><head><meta charset="utf-8"><style>{COMMON_CSS}</style></head><body><main class="slide">
    <div class="header">
      <div class="header-meta"><span>Section 6: Evaluation Metrics</span><span>11 / 15</span></div>
      <h1 class="slide-title">Formal Evaluation Metrics & Mathematical Formulations</h1>
      <p class="slide-subtitle">Quantitative criteria for prerequisite correctness, debate synthesis, diversity, and equity.</p>
    </div>
    <div class="grid-4" style="gap: 12px; margin-bottom: 12px;">
      <div class="box">
        <div class="box-header">UCR (PREREQUISITES)</div>
        <p><strong>Unsupported-Claim Rate</strong></p>
        <p>Target: &le; 5.0%</p>
        <p>Observed: <strong>0.0%</strong></p>
        <p style="font-size:11px;">% of milestones violating prerequisite order in 42-node DAG.</p>
      </div>
      <div class="box">
        <div class="box-header">CRR (DISPUTES)</div>
        <p><strong>Contradiction Resolution</strong></p>
        <p>Target: &ge; 80.0%</p>
        <p>Observed: <strong>100.0%</strong></p>
        <p style="font-size:11px;">% of Critic/Ethics objections addressed and resolved in plan.</p>
      </div>
      <div class="box">
        <div class="box-header">H_div (DIVERSITY)</div>
        <p><strong>Evidence Diversity</strong></p>
        <p>Target: &ge; 0.80</p>
        <p>Observed: <strong>1.00</strong></p>
        <p style="font-size:11px;">Normalized Shannon entropy across cited knowledge sources.</p>
      </div>
      <div class="box">
        <div class="box-header">JACCARD J (FAIRNESS)</div>
        <p><strong>Demographic Fairness</strong></p>
        <p>Target: &ge; 0.90</p>
        <p>Observed: <strong>1.00</strong></p>
        <p style="font-size:11px;">Jaccard similarity between matched counterfactual pairs.</p>
      </div>
    </div>
    <div class="box">
      <div class="box-header">MATHEMATICAL FORMULATIONS</div>
      <p style="font-family: monospace; font-size: 11.5px; margin: 4px 0;">
        H_div = - &Sigma; (p_i * log2(p_i)) / log2(K) &isin; [0.0, 1.0] (K = 4) &nbsp;&nbsp;|&nbsp;&nbsp; J(S_a, S_b) = |S_a &cap; S_b| / |S_a &cup; S_b| &isin; [0.0, 1.0]
      </p>
    </div>
    <footer class="footer"><span>Responsible AI in Educational Advisory — Academic Defense</span><span>Slide 11 / 15</span></footer></main></body></html>""",

    # SLIDE 12
    f"""<!doctype html><html><head><meta charset="utf-8"><style>{COMMON_CSS}</style></head><body><main class="slide">
    <div class="header">
      <div class="header-meta"><span>Section 6: Empirical Findings</span><span>12 / 15</span></div>
      <h1 class="slide-title">Empirical Results: Full Ablation Benchmark Table (80 Runs)</h1>
      <p class="slide-subtitle">Config 4 eliminates prerequisite errors to strictly 0.0% and achieves 100% contradiction resolution.</p>
    </div>
    <table class="table-academic">
      <thead>
        <tr>
          <th>Configuration</th>
          <th>UCR (Prereq Error)</th>
          <th>CRR (Disputes)</th>
          <th>H_div (Diversity)</th>
          <th>Fairness (Jaccard)</th>
          <th>User Rubric</th>
          <th>Statistical Significance</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Config 1 (Monolithic LLM Baseline)</td>
          <td>90.9%</td>
          <td>0.0%</td>
          <td>0.00</td>
          <td>0.32</td>
          <td>2.1 / 5.0</td>
          <td>Baseline</td>
        </tr>
        <tr>
          <td>Config 2 (Multi-Perspective Prompt)</td>
          <td>68.2%</td>
          <td>38.0%</td>
          <td>0.72</td>
          <td>0.93</td>
          <td>3.2 / 5.0</td>
          <td>p &lt; 0.01</td>
        </tr>
        <tr>
          <td>Config 3 (Unmoderated Debate)</td>
          <td>86.4% (Woozle Effect)</td>
          <td>25.0%</td>
          <td>0.85</td>
          <td>1.00</td>
          <td>3.8 / 5.0</td>
          <td>p &lt; 0.01</td>
        </tr>
        <tr class="highlight-row">
          <td>Config 4 (Proposed RAI System)</td>
          <td>0.0% (Zero Error)</td>
          <td>100.0%</td>
          <td>1.00</td>
          <td>1.00</td>
          <td>4.7 / 5.0</td>
          <td>p &lt; 0.0001 (McNemar)</td>
        </tr>
      </tbody>
    </table>
    <div class="box" style="margin-top: 14px;">
      <div class="box-header">KEY EMPIRICAL DISCOVERIES</div>
      <ul>
        <li><strong>1. Prerequisite Eradication:</strong> Deterministic graph verification dropped prerequisite sequencing errors from 90.9% in monolithic LLMs to strictly <strong>0.0%</strong> (p &lt; 0.0001, McNemar exact test).</li>
        <li><strong>2. Empirical Confirmation of the Woozle Effect:</strong> Config 3 (Unmoderated debate) exhibited an <strong>86.4% prerequisite error rate</strong>, proving that unanchored multi-agent debate mutually reinforces errors.</li>
        <li><strong>3. Complete Demographic Equity:</strong> Config 4 achieved <strong>J = 1.00</strong> curriculum parity across Tier-1 and Tier-3 counterfactual pairs, completely eliminating institutional pedigree bias.</li>
      </ul>
    </div>
    <footer class="footer"><span>Responsible AI in Educational Advisory — Academic Defense</span><span>Slide 12 / 15</span></footer></main></body></html>""",

    # SLIDE 13
    f"""<!doctype html><html><head><meta charset="utf-8"><style>{COMMON_CSS}</style></head><body><main class="slide">
    <div class="header">
      <div class="header-meta"><span>Section 7: Production Feasibility</span><span>13 / 15</span></div>
      <h1 class="slide-title">System Performance, Latency, and Edge Deployability</h1>
      <p class="slide-subtitle">100% Local execution on consumer student hardware with zero cloud API expenditures.</p>
    </div>
    <div class="grid-4" style="gap: 14px;">
      <div class="box">
        <div class="box-header">DELIBERATION LATENCY</div>
        <div class="stat-callout">11.4s</div>
        <ul>
          <li>Planner Draft: 3.8s</li>
          <li>Critic Audit: 3.2s</li>
          <li>Ethics Review: 2.9s</li>
          <li>Moderator Synthesis: 1.5s</li>
          <li>Graph Traversal: &lt; 0.002s</li>
          <li><strong>Assessment:</strong> Real-time speed.</li>
        </ul>
      </div>
      <div class="box">
        <div class="box-header">SYSTEM RAM FOOTPRINT</div>
        <div class="stat-callout">5.2 GB</div>
        <ul>
          <li>Model Quantization: 4-bit (q4_k_m)</li>
          <li>Weights in Memory: 4.7 GB</li>
          <li>Vector Store: 14 MB (ChromaDB)</li>
          <li>Graph Engine: 120 KB (NetworkX)</li>
          <li><strong>Safety Margin:</strong> Runs on 16 GB laptops.</li>
        </ul>
      </div>
      <div class="box">
        <div class="box-header">OPERATING COST</div>
        <div class="stat-callout">₹0.00</div>
        <ul>
          <li>Cloud API Cost: Zero recurring tokens</li>
          <li>Third-Party Fees: Zero subscriptions</li>
          <li>Student Invariant: 100% free access</li>
          <li>University Infra: Zero GPU servers.</li>
        </ul>
      </div>
      <div class="box">
        <div class="box-header">STUDENT PRIVACY</div>
        <div class="stat-callout">100%</div>
        <ul>
          <li>Egress: Zero external network packets</li>
          <li>Disk Storage: Records stay local</li>
          <li>Compliance: FERPA & GDPR aligned</li>
          <li>Offline Capable: Works without internet.</li>
        </ul>
      </div>
    </div>
    <footer class="footer"><span>Responsible AI in Educational Advisory — Academic Defense</span><span>Slide 13 / 15</span></footer></main></body></html>""",

    # SLIDE 14
    f"""<!doctype html><html><head><meta charset="utf-8"><style>{COMMON_CSS}</style></head><body><main class="slide">
    <div class="header">
      <div class="header-meta"><span>Section 7: Theoretical Insights & Defense</span><span>14 / 15</span></div>
      <h1 class="slide-title">Theoretical Insights & Committee Viva Voce Defense Guide</h1>
      <p class="slide-subtitle">Addressing core examiner inquiries regarding model capability, graphs, and usability.</p>
    </div>
    <div class="grid-2" style="gap: 20px;">
      <div class="box">
        <div class="box-header">CORE COMMITTEE EXAMINATION DEFENSES</div>
        <ul>
          <li><strong>Q1: Why not just use GPT-4o or Claude 3.5?</strong><br>
          Two reasons: First, cloud models violate student privacy and incur continuous token costs. Second, empirical literature proves even frontier models hallucinate prerequisite order without structural graph verification.</li>
          <li><strong>Q2: Isn't a 7B model too small for complex debate?</strong><br>
          By assigning narrow persona roles with asymmetric temperatures (0.3 vs 0.6) and anchoring in a 42-node DAG, Qwen 2.5 7B matches or exceeds monolithic frontier models while running locally.</li>
          <li><strong>Q3: Why NetworkX instead of Neo4j for the prototype?</strong><br>
          NetworkX executes in-memory in &lt; 0.2 ms with zero server overhead. However, our architecture is dual-mode: we include automated Cypher export to Neo4j for enterprise scaling.</li>
        </ul>
      </div>
      <div class="box">
        <div class="box-header">EMPIRICAL VALIDATION & STUDENT USABILITY</div>
        <ul>
          <li><strong>Ground-Truth Reliability (Cohen's Kappa):</strong> Two independent human raters evaluated 40 dispute decisions and 28 gate triggers, obtaining <strong>&kappa; = 0.926</strong>, confirming high annotation consistency.</li>
          <li><strong>Why Uncalibrated LLM Judges Fail:</strong> Pilot tests using an unprompted 7B LLM judge showed dismal reliability (&kappa; = 0.12), penalizing legitimate electives. We replaced it with hybrid graph + focused classification scoring.</li>
          <li><strong>User Study with 15 Engineering Students:</strong> Conducted at SRMIST. <strong>93.3%</strong> of students preferred the multi-agent Dispute Tree and interactive sliders over opaque single-prompt chatbot answers.</li>
          <li><strong>Student Feedback:</strong> Students reported that seeing explicit Critic warnings helped them identify real interview hurdles they had underestimated.</li>
        </ul>
      </div>
    </div>
    <footer class="footer"><span>Responsible AI in Educational Advisory — Academic Defense</span><span>Slide 14 / 15</span></footer></main></body></html>""",

    # SLIDE 15
    f"""<!doctype html><html><head><meta charset="utf-8"><style>{COMMON_CSS}
    .end-wrapper {{
      height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      text-align: center;
      padding: 0 30px;
    }}
    .end-rule {{
      border: none;
      border-top: 2.5px solid #000000;
      margin: 14px 0;
    }}
    </style></head><body><main class="slide"><div class="end-wrapper">
      <hr class="end-rule">
      <p style="font-size: 13px; font-weight: 800; letter-spacing: 1.5px; color: #555555; margin: 0 0 8px 0;">SECTION 8: RESEARCH SUMMARY & CONCLUSION</p>
      <h1 style="font-size: 30px; font-weight: 900; line-height: 1.2; margin: 0 0 10px 0; color: #000000;">Responsible AI in Higher Education: Core Contributions</h1>
      <hr class="end-rule">
      <div class="grid-2" style="margin-top: 15px; text-align: left;">
        <div class="box">
          <div class="box-header">PROJECT DELIVERABLES & ARTIFACTS</div>
          <ul>
            <li><strong>1. Interactive Prototype (app.py):</strong> Live Streamlit interface with multi-agent debate trace viewer, Dispute Tree, and student override sliders.</li>
            <li><strong>2. Prerequisite Graph (career_graph.py):</strong> 42 nodes, 47 edges, NetworkX engine with automated Neo4j Cypher synchronization.</li>
            <li><strong>3. Evaluation Benchmark (benchmark_suite.py):</strong> 20 synthetic profiles, 80-run evaluation engine, and metric calculation.</li>
            <li><strong>4. Research Publications:</strong> IEEE Research Paper (paper.typ) & 4-Page Research Specification Document.</li>
            <li><strong>5. Originality Certification:</strong> Audited via Noplag Engine (<strong>0.00% Plagiarism, 0.0% AI Slop Detected</strong>).</li>
          </ul>
        </div>
        <div class="box">
          <div class="box-header">SCIENTIFIC IMPACT & COMMITTEE EXAMINATION</div>
          <ul>
            <li><strong>Zero Hallucination Tolerance:</strong> Proved that multi-agent deliberation combined with external knowledge graphs can completely eliminate prerequisite sequencing errors (<strong>0.0%</strong>).</li>
            <li><strong>Equitable Educational Access:</strong> Demonstrated that AI can guarantee demographic parity (<strong>J = 1.00</strong>) while actively protecting low-income students from predatory debt.</li>
            <li><strong>Human Agency Paradigm:</strong> Shifted AI advising from opaque algorithmic dictation to transparent, slider-based trade-off exploration.</li>
            <li><strong>Live Demonstration:</strong> Interactive prototype ready for committee evaluation via <code>streamlit run app.py</code>.</li>
          </ul>
        </div>
      </div>
    </div>
    <footer class="footer"><span>Responsible AI in Educational Advisory — Academic Defense</span><span>Slide 15 / 15</span></footer></main></body></html>""",
]

for idx, content in enumerate(slides_content, 1):
    filename = os.path.join(SLIDES_DIR, f"slide{idx:02d}.html")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {filename}")

print(f"✅ Successfully created all 15 PPTAgent HTML slides in {SLIDES_DIR}")
