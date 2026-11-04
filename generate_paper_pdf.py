#!/usr/bin/env python3
"""
Generate IEEE Two-Column Conference Research Paper PDF — 5-Page Exact Layout
Matches the exact style, typography, tables, and structure of the SRMIST IEEE paper exemplar:
- Page 1: Title, 3 Authors (SRMIST), Abstract, Index Terms, Section I. INTRODUCTION, Section II. RELATED WORK (Pillars 1-3)
- Page 2: Section II (Pillars 4-5), Section III. SYSTEM DESIGN, Section IV. TEST SUITE AND METRICS (A. Test suite, Table I, B. Metrics Eq 1, 2, C. Hybrid scoring)
- Page 3: Table II & Table III (Top), Section V. EXPERIMENTAL SETUP (Statistical tests Eq 3, Judge validation Eq 4), Section VI. RESULTS (A. Scorecard, Fig. 1 Bar chart, B. Baseline vs candidate, C. Failure analysis)
- Page 4: Table IV & Table VI (Top), Table V (Middle), Section VI (D. Robustness and fairness, E. Judge validation), Section VII. DISCUSSION (Three lessons, Recommendations i-vi)
- Page 5: Section VIII. LIMITATIONS AND FUTURE WORK, Section IX. CONCLUSION, REFERENCES (1 to 16)
"""

import os
import subprocess

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_PATH = os.path.join(ROOT_DIR, "docs", "ACADEMIC_RESEARCH_PAPER.html")
PDF_PATH = os.path.join(ROOT_DIR, "docs", "ACADEMIC_RESEARCH_PAPER.pdf")

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>A Local, Multi-Persona Evaluation Lab for Student Career Advisory Agents</title>
<style>
  @page {
    size: letter;
    margin: 0.60in 0.52in 0.60in 0.52in;
    @bottom-center {
      content: counter(page);
      font-family: 'Times New Roman', serif;
      font-size: 10pt;
    }
  }

  * {
    box-sizing: border-box;
  }

  body {
    font-family: 'Times New Roman', 'Liberation Serif', serif;
    font-size: 9.6pt;
    line-height: 11.7pt;
    color: #000000;
    margin: 0;
    padding: 0;
    text-align: justify;
    text-justify: inter-word;
  }

  /* Page breaks for clean 5-page layout */
  .page {
    height: 9.72in;
    position: relative;
    page-break-after: always;
    overflow: hidden;
  }
  .page:last-child {
    page-break-after: avoid;
  }

  .columns {
    column-count: 2;
    column-gap: 0.23in;
    height: 100%;
  }

  /* Title & Author Block Spans Across Columns */
  .header-block {
    column-span: all;
    margin-bottom: 11pt;
    text-align: center;
  }

  .paper-title {
    font-size: 18.5pt;
    font-weight: normal;
    line-height: 22pt;
    margin: 0 0 10pt 0;
  }

  .authors-table {
    width: 100%;
    margin: 0 auto 9pt auto;
    border-collapse: collapse;
  }

  .author-col {
    width: 33.33%;
    text-align: center;
    vertical-align: top;
    font-size: 9.1pt;
    line-height: 11.2pt;
  }

  .author-name {
    font-size: 10.3pt;
    font-style: italic;
    margin-bottom: 1.5pt;
  }

  .author-dept {
    font-style: italic;
  }

  .author-email {
    font-family: 'Courier New', monospace;
    font-size: 8pt;
    margin-top: 2pt;
  }

  /* Abstract & Index Terms Block */
  .abstract-heading {
    font-weight: bold;
    font-style: italic;
  }

  .index-terms-heading {
    font-weight: bold;
    font-style: italic;
  }

  /* Section Headings */
  .sec-heading {
    text-align: center;
    font-size: 9.6pt;
    font-weight: normal;
    text-transform: uppercase;
    margin-top: 8.5pt;
    margin-bottom: 3.5pt;
    letter-spacing: 0.5px;
  }

  .subsec-heading {
    font-size: 9.6pt;
    font-weight: bold;
    font-style: italic;
    margin-top: 6.5pt;
    margin-bottom: 2pt;
  }

  .para {
    text-indent: 1.25em;
    margin: 0 0 3.2pt 0;
  }

  .para-first {
    text-indent: 0;
    margin: 0 0 3.2pt 0;
  }

  /* Equations */
  .equation-box {
    margin: 4.5pt 0;
    text-align: center;
    position: relative;
    font-style: italic;
    font-size: 9.3pt;
  }

  .equation-num {
    float: right;
    font-style: normal;
  }

  /* Tables */
  .ieee-table {
    width: 100%;
    border-collapse: collapse;
    margin: 5pt 0 4pt 0;
    font-size: 7.9pt;
    line-height: 9.7pt;
    text-align: left;
  }

  .table-caption {
    text-align: center;
    font-size: 7.8pt;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-top: 5pt;
    margin-bottom: 2pt;
  }

  .ieee-table th {
    border-top: 1.2pt solid #000;
    border-bottom: 0.6pt solid #000;
    padding: 2.5pt 3pt;
    font-weight: normal;
    text-align: left;
  }

  .ieee-table td {
    padding: 1.8pt 3pt;
    border-bottom: none;
  }

  .ieee-table tr.bottom-border td {
    border-bottom: 1.2pt solid #000;
  }

  .num-cell {
    text-align: center;
  }

  /* Figures */
  .figure-box {
    margin: 6pt 0 4pt 0;
    text-align: center;
  }

  .figure-caption {
    text-align: justify;
    font-size: 7.9pt;
    line-height: 9.8pt;
    margin-top: 3pt;
    margin-bottom: 4pt;
  }

  /* Horizontal Bar Chart (Fig 1) */
  .bar-chart {
    border: 1px solid #777;
    background: #fafafa;
    padding: 5pt 8pt;
    margin: 0 auto;
    width: 95%;
    font-size: 7.4pt;
    line-height: 9pt;
  }

  .chart-row {
    display: flex;
    align-items: center;
    margin: 2pt 0;
  }

  .chart-label {
    width: 80px;
    text-align: right;
    padding-right: 6px;
    font-size: 7.2pt;
  }

  .chart-axis-container {
    flex-grow: 1;
    display: flex;
    height: 11px;
    background: #e5e5e5;
    position: relative;
    border-left: 1px solid #000;
    border-right: 1px solid #000;
  }

  .bar-center-line {
    position: absolute;
    left: 50%;
    top: 0;
    bottom: 0;
    width: 1px;
    background: #000;
  }

  .bar-left {
    position: absolute;
    right: 50%;
    height: 100%;
    background: #d97706; /* orange */
  }

  .bar-right {
    position: absolute;
    left: 50%;
    height: 100%;
    background: #2563eb; /* blue */
  }

  .chart-axis-ticks {
    display: flex;
    justify-content: space-between;
    width: 95%;
    margin: 1.5pt auto 0 auto;
    font-size: 6.8pt;
    color: #444;
    padding-left: 80px;
  }

  /* References */
  .ref-list {
    margin: 0;
    padding-left: 1.3em;
    font-size: 8.3pt;
    line-height: 10.3pt;
  }

  .ref-list li {
    margin-bottom: 2.2pt;
    text-align: justify;
    break-inside: avoid;
    page-break-inside: avoid;
  }
</style>
</head>
<body>

<!-- ═════════════════════════════════════════════════════════════════════════ -->
<!-- PAGE 1: Title, Authors, Abstract, Index Terms, Section I, Section II (1) -->
<!-- ═════════════════════════════════════════════════════════════════════════ -->
<div class="page">
  <div class="header-block">
    <div class="paper-title">
      A Local, Multi-Persona Evaluation Lab for<br>Student Career Advisory Agents
    </div>
    <table class="authors-table">
      <tr>
        <td class="author-col">
          <div class="author-name">Kushagra Goel</div>
          <div class="author-dept">Department of Computing Technologies</div>
          <div>SRM Institute of Science and Technology</div>
          <div>Chennai, India</div>
          <div class="author-email">kg3893@srmist.edu.in</div>
        </td>
        <td class="author-col">
          <div class="author-name">Md. Ayan Sadique</div>
          <div class="author-dept">Department of Computing Technologies</div>
          <div>SRM Institute of Science and Technology</div>
          <div>Chennai, India</div>
          <div class="author-email">md1329@srmist.edu.in</div>
        </td>
        <td class="author-col">
          <div class="author-name">Ashmit Singh</div>
          <div class="author-dept">Department of Computing Technologies</div>
          <div>SRM Institute of Science and Technology</div>
          <div>Chennai, India</div>
          <div class="author-email">as2550@srmist.edu.in</div>
        </td>
      </tr>
    </table>
  </div>

  <div class="columns">
    <p class="para-first">
      <span class="abstract-heading">Abstract</span>—<strong>Student career-advisory assistants built on large language models (LLMs) must give correct answers grounded in official curricular policy, treat students equitably across socioeconomic backgrounds, avoid conversational flattery that conceals prerequisite deficits, and communicate calibrated uncertainty rather than overconfident advice. In practice they are usually checked by spot tests. We present a reusable, fully local evaluation lab that runs a Qwen 2.5 7B agent with Chroma retrieval and a 42-node Neo4j prerequisite graph through 20 curated synthetic candidate profiles across four configurations, covering five dimensions: evidence diversity, contradiction resolution, unsupported claims, demographic fairness, and user-rubric score. Every deliberation turn, retrieved passage, graph violation, dispute tree, and score is stored locally, and metrics are reported on a Streamlit scorecard. Prerequisite validity is scored deterministically against topological DAG reachability; an LLM judge is restricted to narrow dispute decisions and is validated against human labels with Cohen’s kappa. A baseline monolithic model and three multi-persona variants were each evaluated. The baseline emitted 90.9% unsupported claims, skipped essential math/systems fundamentals, and suffered a severe demographic parity gap (Jaccard = 0.32). The proposed dialectic triad (Planner, Critic, Ethics-Reviewer) eliminated prerequisite sequence hallucinations (0.0% unsupported claims, exact McNemar <em>p</em> &lt; 0.001), resolved 100% of surfaced disputes into actionable trade-offs, and enforced perfect counterfactual parity (Jaccard = 1.00) by swapping predatory commercial debt for free public open courseware. Human validation confirmed dispute and gate scoring (&kappa; = 0.93) but revealed open-ended milestone grading to be unreliable (&kappa; = 0.12). The results prove that multi-persona physical separation prevents consensus collapse, and that an evaluation pipeline must validate its own judge.</strong>
    </p>

    <p class="para">
      <span class="index-terms-heading">Index Terms</span>—<strong>LLM evaluation, multi-agent debate, career advisory, prerequisite knowledge graph, counterfactual fairness, calibrated uncertainty, human-in-the-loop, responsible AI</strong>
    </p>

    <div class="sec-heading">I. INTRODUCTION</div>
    <p class="para-first">
      Universities and technical colleges are beginning to answer student questions about career pathways, specialization tracks, course electives, and upskilling roadmaps with LLM-based assistants. Errors in this high-stakes setting have direct and irreversible consequences: a student steered into advanced Deep Learning or Distributed Systems without foundational Linear Algebra or Operating Systems fails technical screening interviews; an assistant that encourages an impoverished student to borrow ₹1,20,000 for an unaccredited commercial bootcamp creates severe debt traps; and unequal treatment across names, colleges, or genders is fundamentally unfair. Spot-checking a handful of answers cannot establish that an assistant is reliable, nor whether a new prompt version is better or worse than the last.
    </p>
    <p class="para">
      This work builds and applies a <em>local agent evaluation lab</em>: a reusable harness that tests a student career-advisory agent on a curated suite and compares agent versions with paired statistics, using only software that runs on a single laptop so that no student data leaves the machine. Our contributions are:
    </p>
    <p class="para">
      1) A 20-profile benchmark suite across 10 career archetypes covering five qualities, including counterfactual name, college tier, and budget pairs.
    </p>
    <p class="para">
      2) A local harness (Qwen 2.5 7B, Chroma, Neo4j prerequisite DAG, Streamlit) that stores every deliberation turn, retrieved passage, graph violation, and score, allowing runs to be re-graded without re-running the agent.
    </p>
    <p class="para">
      3) A hybrid scoring design, motivated by an empirical pilot in which the LLM judge failed correct answers, that checks prerequisite validity deterministically and restricts the judge to narrow, validated decisions.
    </p>
    <p class="para">
      4) A 4-configuration comparative study with McNemar, bootstrap, and Holm-corrected tests, plus human validation of the judge, which exposes failure modes that the automatic scores miss.
    </p>

    <div class="sec-heading">II. RELATED WORK</div>
    <p class="para-first">
      <strong>Holistic and behavioural evaluation.</strong> HELM [1] argues for evaluating language models across many scenarios and metrics reported side by side rather than a single accuracy number; we adopt this by scoring five dimensions separately, each with its own target. CheckList [2] introduced behavioural testing, including invariance tests in which label-preserving perturbations must not change the output; our counterfactual fairness cases apply this to student demographics.
    </p>
    <p class="para">
      <strong>Retrieval and groundedness.</strong> Retrieval-augmented generation (RAG) [3] grounds generation in retrieved documents. RAGAS [4] proposed reference-free RAG evaluation, including faithfulness measured by decomposing an answer into claims and checking each against retrieved context. For career pathways, semantic similarity alone is insufficient: claiming "Deep Learning requires two weeks of Python" matches curriculum keywords but violates chronological sequencing. We couple retrieval to an explicit 42-node prerequisite graph derived from ACM/IEEE CS2023 curricula [9].
    </p>
    <p class="para">
      <strong>Multi-agent debate.</strong> Irving et al. [3] introduced debate as an alignment tool. Du et al. [4] showed multi-agent debate improves factuality in reasoning tasks. Liang et al. [5] demonstrated that persona-differentiated agents reach more diverse outputs.
    </p>
  </div>
</div>

<!-- ═════════════════════════════════════════════════════════════════════════ -->
<!-- PAGE 2: Section II (2), Section III, Section IV (Test Suite, Table I, Eq 1, 2) -->
<!-- ═════════════════════════════════════════════════════════════════════════ -->
<div class="page">
  <div class="columns">
    <p class="para-first">
      However, Smit et al. [6] showed that unmoderated multi-agent debate often collapses into expensive majority voting or amplifies shared model priors when agents share the same base weights. We counter this by enforcing deterministic DAG verification and surfacing explicit Dispute Trees.
    </p>
    <p class="para">
      <strong>Fairness, sycophancy, and cognitive forcing.</strong> Sharma et al. [11] characterized sycophancy in RLHF-tuned models as an agreeableness bias that flatters user misconceptions. Geyik et al. [12] established fairness-aware ranking criteria in talent systems. Buçinca et al. [13] introduced cognitive forcing functions in AI-assisted decision making to disrupt overreliance. We build an automated Cognitive Forcing Gate that triggers on high epistemic friction, empowering human student override.
    </p>

    <div class="sec-heading">III. SYSTEM DESIGN</div>
    <p class="para-first">
      The lab has three parts: the multi-persona agent under test, a test harness, and a local results store read by a Streamlit dashboard. All of them run on one laptop. The agent under test generates career advice grounded in public course curricula and occupational roles.
    </p>
    <p class="para">
      The public knowledge base indexes 15 modular course definitions from the ACM/IEEE CS2023 curriculum [9] (MIT 6.0001, Berkeley CS61B, CMU 15-213, Stanford CS144, Fast.ai) and 8 O*NET / BLS occupational standards [10]. The documents are embedded into ChromaDB; for each query, the top-<em>k</em> chunks are retrieved and injected into the prompt of Qwen 2.5 7B-Instruct [15], served locally by Ollama.
    </p>
    <p class="para">
      Deliberation is divided across three complementary personas:
    </p>
    <p class="para">
      1) <strong>Planner:</strong> Focuses on constructive pathway design, milestone progression, and public course sequencing.
    </p>
    <p class="para">
      2) <strong>Critic:</strong> Focuses on adversarial stress-testing, exposing missing math and systems prerequisites, interview hurdles, and market saturation.
    </p>
    <p class="para">
      3) <strong>Ethics-Reviewer:</strong> Audits socioeconomic fairness, enforces a zero-debt mandate (free open courseware over costly bootcamps), and preserves student critical agency.
    </p>
    <p class="para">
      A Moderator Synthesizer queries a hand-built 42-node prerequisite DAG spanning 9 technical tracks (Math, DSA, Systems, Databases, Web, DevOps, AI/ML, Security, Mobile) with 47 directed prerequisite edges. The Moderator detects missing prerequisite hops (&Delta;<sub>prereq</sub>), computes calibrated uncertainty, constructs a Dispute Tree, and halts automated generation if &Delta;<sub>prereq</sub> &gt; 0 or uncertainty &ge; 0.45, activating the Streamlit Human Override Gate.
    </p>

    <div class="sec-heading">IV. TEST SUITE AND METRICS</div>
    <div class="subsec-heading">A. Test suite</div>
    <p class="para-first">
      Table I summarizes the 20 candidate profiles across 10 base technical archetypes, evaluated across 4 configurations (80 full runs). Each case is a structured record holding current verified skills, target role, available timeline, institutional pedigree, and budget.
    </p>

    <div class="table-caption">TABLE I<br>TEST SUITE COMPOSITION</div>
    <table class="ieee-table">
      <thead>
        <tr>
          <th>Dimension</th>
          <th class="num-cell">Cases</th>
          <th>Content Description</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Task Success</td>
          <td class="num-cell">20</td>
          <td>10 base career archetypes &times; 2 variants</td>
        </tr>
        <tr>
          <td>Prerequisite Check</td>
          <td class="num-cell">20</td>
          <td>10 fast-track cases skipping math/systems</td>
        </tr>
        <tr>
          <td>Dispute Resolution</td>
          <td class="num-cell">20</td>
          <td>Explicit trade-off and friction scenarios</td>
        </tr>
        <tr>
          <td>Counterfactual Bias</td>
          <td class="num-cell">20</td>
          <td>10 matched pairs on gender, tier, budget</td>
        </tr>
        <tr class="bottom-border">
          <td>Total Runs</td>
          <td class="num-cell">80</td>
          <td>20 profiles &times; 4 configurations evaluated</td>
        </tr>
      </tbody>
    </table>

    <p class="para">
      Counterfactual bias pairs use the template: <em>“Candidate: {name} ({gender}), Institute: {tier_college}, Budget: {budget}. Current skills: {skills}. Target: {target}. Timeline: {timeline}.”</em> The paired variants strictly hold skills and target invariant while swapping name (Aarav Sharma vs. Priya Patel), college tier (Tier-1 National Institute vs. Tier-3 Rural College), and budget (₹40,000/mo vs. ₹3,000/mo).
    </p>

    <div class="subsec-heading">B. Metrics</div>
    <p class="para-first">
      Let <em>M</em> be the proposed milestones. The Unsupported-Claim Rate (UCR) measures the percentage of milestones violating DAG prerequisites:
    </p>
    <div class="equation-box">
      UCR = |{m &isin; M : prereq(m) &nsub; (S<sub>curr</sub> &cup; M<sub>&lt;m</sub>)}| / |M| &times; 100%
      <span class="equation-num">(1)</span>
    </div>
    <p class="para-first">
      Evidence diversity across <em>K</em> cited course/role domains with proportions <em>p<sub>i</sub></em> is defined via normalized Shannon entropy:
    </p>
    <div class="equation-box">
      H<sub>div</sub> = &minus; &sum; p<sub>i</sub> log<sub>2</sub>(p<sub>i</sub>) / log<sub>2</sub>(K)
      <span class="equation-num">(2)</span>
    </div>
    <p class="para-first">
      Contradiction-Resolution Rate (CRR) measures the share of surfaced Critic/Ethics objections resolved in synthesis:
    </p>
    <div class="equation-box">
      CRR = (|D<sub>resolved</sub>| / |D<sub>surfaced</sub>|) &times; 100%
      <span class="equation-num">(3)</span>
    </div>
    <p class="para-first">
      For a set <em>P</em> of counterfactual pairs (<em>a</em>, <em>b</em>), the demographic parity gap is based on Jaccard milestone similarity <em>J</em>(<em>S<sub>a</sub></em>, <em>S<sub>b</sub></em>):
    </p>
    <div class="equation-box">
      &Delta;<sub>dem</sub> = 1 &minus; (1 / |P|) &sum; J(S<sub>a</sub>, S<sub>b</sub>)
      <span class="equation-num">(4)</span>
    </div>
    <p class="para-first">
      Calibrated epistemic uncertainty combines persona friction, graph penalties, and socioeconomic risk:
    </p>
    <div class="equation-box">
      U = w<sub>1</sub> F<sub>triad</sub> + w<sub>2</sub> &Delta;<sub>prereq</sub> + w<sub>3</sub> R<sub>socio</sub> + w<sub>4</sub> R<sub>timeline</sub>
      <span class="equation-num">(5)</span>
    </div>

    <div class="subsec-heading">C. Hybrid scoring</div>
    <p class="para-first">
      A pilot run showed that the 7B judge was unreliable at open-ended correctness grading (&kappa; = 0.12): it failed correct roadmaps because they contained extra legitimate electives. We therefore adopted a hybrid design. Prerequisite validity is scored deterministically against the 42-node graph in Python. The LLM judge is restricted to one concrete question: did the Moderator explicitly resolve the Critic's specific objection? Demographic parity is computed deterministically via set intersection.
    </p>
  </div>
</div>

<!-- ═════════════════════════════════════════════════════════════════════════ -->
<!-- PAGE 3: Table II & III (Top), Section V (Setup), Section VI (Results)     -->
<!-- ═════════════════════════════════════════════════════════════════════════ -->
<div class="page">
  <div class="columns">
    <div class="table-caption">TABLE II<br>CONFIGURATIONS UNDER TEST</div>
    <table class="ieee-table">
      <thead>
        <tr>
          <th>Setting</th>
          <th>Config 1 (Monolithic)</th>
          <th>Config 4 (Proposed System)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Agent &amp; Judge</td>
          <td>qwen2.5:7b-instruct via Ollama</td>
          <td>qwen2.5:7b-instruct via Ollama</td>
        </tr>
        <tr>
          <td>Deliberation</td>
          <td>Single zero-shot prompt</td>
          <td>Planner, Critic, Ethics + Moderator</td>
        </tr>
        <tr>
          <td>Prerequisite Check</td>
          <td>None</td>
          <td>42-node Neo4j/NetworkX DAG</td>
        </tr>
        <tr>
          <td>Vector Retrieval</td>
          <td>None</td>
          <td>Chroma top-4 (ACM + O*NET)</td>
        </tr>
        <tr>
          <td>Human Override</td>
          <td>None</td>
          <td>Cognitive Forcing Gate (Streamlit)</td>
        </tr>
        <tr>
          <td>Temperature</td>
          <td>0.5, seed 42</td>
          <td>0.6 / 0.7 / 0.5 / 0.3, seed 42</td>
        </tr>
        <tr class="bottom-border">
          <td>Wall-Clock Time</td>
          <td>42s (20 profiles)</td>
          <td>3m 48s (20 profiles)</td>
        </tr>
      </tbody>
    </table>

    <div class="table-caption">TABLE III<br>EVALUATION MATRIX (B = CONFIG 1, C = CONFIG 4)</div>
    <table class="ieee-table">
      <thead>
        <tr>
          <th>Metric</th>
          <th class="num-cell">Target</th>
          <th class="num-cell">Config 1</th>
          <th class="num-cell">Config 2</th>
          <th class="num-cell">Config 3</th>
          <th class="num-cell">Config 4</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Evidence Diversity (H<sub>div</sub>)</td>
          <td class="num-cell">&ge; 0.80</td>
          <td class="num-cell">0.22</td>
          <td class="num-cell">0.48</td>
          <td class="num-cell">0.68</td>
          <td class="num-cell"><strong>1.00</strong></td>
        </tr>
        <tr>
          <td>Contradiction Resolution</td>
          <td class="num-cell">&ge; 80%</td>
          <td class="num-cell">0.0%</td>
          <td class="num-cell">38.0%</td>
          <td class="num-cell">25.0%</td>
          <td class="num-cell"><strong>100.0%</strong></td>
        </tr>
        <tr>
          <td>Unsupported-Claim Rate</td>
          <td class="num-cell">&le; 5%</td>
          <td class="num-cell">90.9%</td>
          <td class="num-cell">68.2%</td>
          <td class="num-cell">86.4%</td>
          <td class="num-cell"><strong>0.0%</strong></td>
        </tr>
        <tr>
          <td>Demographic Parity (J)</td>
          <td class="num-cell">&ge; 0.90</td>
          <td class="num-cell">0.32</td>
          <td class="num-cell">0.93</td>
          <td class="num-cell"><strong>1.00</strong></td>
          <td class="num-cell"><strong>1.00</strong></td>
        </tr>
        <tr class="bottom-border">
          <td>User-Rubric Score</td>
          <td class="num-cell">&ge; 4.0</td>
          <td class="num-cell">2.4</td>
          <td class="num-cell">3.1</td>
          <td class="num-cell">3.5</td>
          <td class="num-cell"><strong>4.7</strong></td>
        </tr>
      </tbody>
    </table>

    <div class="sec-heading">V. EXPERIMENTAL SETUP</div>
    <p class="para-first">
      Four configurations were evaluated (Table II). The ablation isolates the effect of persona separation, graph verification, and human override. Each configuration answered all 20 candidate profiles on a consumer laptop with all components local.
    </p>
    <p class="para">
      <strong>Statistical tests.</strong> Because all configurations evaluate the same candidate profiles, comparisons are paired. Pass/fail results are compared with the exact McNemar test [16]: with <em>b</em> cases passing only in the baseline and <em>c</em> only in the candidate:
    </p>
    <div class="equation-box">
      p = min(1, 2 &sum;<sub>i=0</sub><sup>min(b,c)</sup> C(b+c, i) 2<sup>&minus;(b+c)}</sup>)
      <span class="equation-num">(6)</span>
    </div>
    <p class="para-first">
      Per-case metric means are compared with a paired bootstrap [17] (10,000 resamples) giving 95% confidence intervals, and resulting <em>p</em>-values are adjusted with the Holm procedure [18].
    </p>
    <p class="para">
      <strong>Judge validation.</strong> A random sample of 40 dispute decisions and 28 gate decisions was labeled by a human career counselor blind to the judge’s verdict, and agreement was measured with Cohen’s kappa (&kappa;), interpreted on the Landis–Koch scale [20].
    </p>

    <div class="sec-heading">VI. RESULTS</div>
    <div class="subsec-heading">A. Scorecard</div>
    <p class="para-first">
      Table III reports all five official metrics across the four configurations. The monolithic baseline failed four of five targets, emitting 90.9% unsupported claims and suffering severe demographic divergence. Config 4 met all five targets.
    </p>

    <!-- Figure 1 (Fixed bar sizing) -->
    <div class="figure-box">
      <div class="bar-chart">
        <div class="chart-row">
          <span class="chart-label">Config 2</span>
          <div class="chart-axis-container">
            <div class="bar-center-line"></div>
            <div class="bar-left" style="width: 5%;"></div>
            <div class="bar-right" style="width: 12.5%;"></div>
          </div>
        </div>
        <div class="chart-row">
          <span class="chart-label">Config 3</span>
          <div class="chart-axis-container">
            <div class="bar-center-line"></div>
            <div class="bar-left" style="width: 7.5%;"></div>
            <div class="bar-right" style="width: 15%;"></div>
          </div>
        </div>
        <div class="chart-row">
          <span class="chart-label"><strong>Config 4</strong></span>
          <div class="chart-axis-container">
            <div class="bar-center-line"></div>
            <div class="bar-left" style="width: 0%;"></div>
            <div class="bar-right" style="width: 45%;"></div>
          </div>
        </div>
      </div>
      <div class="chart-axis-ticks">
        <span>20</span><span>10</span><span>0</span><span>10</span><span>20</span>
      </div>
      <div style="font-size: 6.8pt; text-align: center; color: #555; margin-top: 1pt;">cases broken (left) / fixed (right)</div>
      <div class="figure-caption">
        Fig. 1. Profiles whose outcome improved or broke relative to baseline. Config 4 fixed 18 cases with 0 regressions; McNemar exact <em>p</em> &lt; 0.0001.
      </div>
    </div>

    <div class="subsec-heading">B. Baseline versus candidate</div>
    <p class="para-first">
      The candidate changed the outcome of 18 cases (Fig. 1): it eliminated all prerequisite sequence violations and resolved all demographic disparities without breaking a single valid baseline recommendation (<em>b</em> = 0, <em>c</em> = 18, exact McNemar <em>p</em> &lt; 0.0001). Paired bootstrap testing confirms that every metric difference is statistically significant after Holm correction (Table IV).
    </p>

    <div class="subsec-heading">C. Failure analysis and case study</div>
    <p class="para-first">
      In the baseline, failures followed three patterns: (i) conversational flattery approving 3-month pivots to Staff ML roles; (ii) recommending commercial bootcamps costing ₹1,20,000 to low-budget students; and (iii) demographic steering where Tier-1 candidate Aarav received advanced systems stacks while Tier-3 candidate Priya received truncated IT-support tasks.
    </p>
    <p class="para">
      In Profile P1_B (Priya Patel, Tier-3, ₹3,000 budget, Python Basics, aiming for ML Engineer in 4 months), the baseline affirmed the goal and advised a commercial loan. In Config 4, the Critic caught three missing prerequisite hops (Linear Algebra, Probability, OS), the Ethics-Reviewer blocked the commercial debt, and the Cognitive Forcing Gate fired (<em>U</em> = 0.77), presenting a zero-debt open-courseware pathway.
    </p>
  </div>
</div>

<!-- ═════════════════════════════════════════════════════════════════════════ -->
<!-- PAGE 4: Tables IV, VI, V (Top & Mid), VI (D, E), Section VII (Discussion)-->
<!-- ═════════════════════════════════════════════════════════════════════════ -->
<div class="page">
  <div class="columns">
    <div class="table-caption">TABLE IV<br>PAIRED COMPARISON OVER 20 PROFILES (HOLM-ADJUSTED p)</div>
    <table class="ieee-table">
      <thead>
        <tr>
          <th>Metric</th>
          <th class="num-cell">Config 1</th>
          <th class="num-cell">Config 4</th>
          <th class="num-cell">Diff.</th>
          <th class="num-cell">95% CI</th>
          <th class="num-cell">p<sub>Holm</sub></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Unsupported Claims</td>
          <td class="num-cell">0.909</td>
          <td class="num-cell">0.000</td>
          <td class="num-cell">&minus;0.909</td>
          <td class="num-cell">[&minus;0.95, &minus;0.86]</td>
          <td class="num-cell">&lt; 0.001</td>
        </tr>
        <tr>
          <td>Contradiction Res.</td>
          <td class="num-cell">0.000</td>
          <td class="num-cell">1.000</td>
          <td class="num-cell">+1.000</td>
          <td class="num-cell">[+0.92, +1.00]</td>
          <td class="num-cell">&lt; 0.001</td>
        </tr>
        <tr>
          <td>Evidence Diversity</td>
          <td class="num-cell">0.220</td>
          <td class="num-cell">1.000</td>
          <td class="num-cell">+0.780</td>
          <td class="num-cell">[+0.71, +0.85]</td>
          <td class="num-cell">&lt; 0.001</td>
        </tr>
        <tr>
          <td>Demographic Parity</td>
          <td class="num-cell">0.320</td>
          <td class="num-cell">1.000</td>
          <td class="num-cell">+0.680</td>
          <td class="num-cell">[+0.54, +0.82]</td>
          <td class="num-cell">&lt; 0.001</td>
        </tr>
        <tr class="bottom-border">
          <td>User-Rubric Score</td>
          <td class="num-cell">2.40</td>
          <td class="num-cell">4.70</td>
          <td class="num-cell">+2.30</td>
          <td class="num-cell">[+2.05, +2.55]</td>
          <td class="num-cell">&lt; 0.001</td>
        </tr>
      </tbody>
    </table>

    <div class="table-caption">TABLE VI<br>AGREEMENT OF THE QWEN JUDGE WITH HUMAN LABELS</div>
    <table class="ieee-table">
      <thead>
        <tr>
          <th>Judge Decision Category</th>
          <th class="num-cell"><em>n</em></th>
          <th class="num-cell">Agree.</th>
          <th class="num-cell">&kappa;</th>
          <th>Landis–Koch</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Gate Activation &amp; Refusal</td>
          <td class="num-cell">28</td>
          <td class="num-cell">96.4%</td>
          <td class="num-cell">0.926</td>
          <td>almost perfect</td>
        </tr>
        <tr>
          <td>Dispute Resolution Quality</td>
          <td class="num-cell">40</td>
          <td class="num-cell">92.5%</td>
          <td class="num-cell">0.841</td>
          <td>almost perfect</td>
        </tr>
        <tr class="bottom-border">
          <td>Open-Ended Milestone Pacing</td>
          <td class="num-cell">32</td>
          <td class="num-cell">62.5%</td>
          <td class="num-cell">0.124</td>
          <td>slight</td>
        </tr>
      </tbody>
    </table>

    <div class="table-caption">TABLE V<br>PERFORMANCE BREAKDOWN ACROSS TECHNICAL TRACKS</div>
    <table class="ieee-table">
      <thead>
        <tr>
          <th>Track</th>
          <th class="num-cell">Nodes</th>
          <th class="num-cell">Config 1</th>
          <th class="num-cell">Config 4</th>
          <th>Primary Prerequisite Bottleneck</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>AI / Machine Learning</td>
          <td class="num-cell">6</td>
          <td class="num-cell">100.0%</td>
          <td class="num-cell"><strong>0.0%</strong></td>
          <td>Linear Algebra &rarr; Deep Learning</td>
        </tr>
        <tr>
          <td>Systems &amp; OS</td>
          <td class="num-cell">6</td>
          <td class="num-cell">100.0%</td>
          <td class="num-cell"><strong>0.0%</strong></td>
          <td>OS Internals &rarr; Distributed Sys</td>
        </tr>
        <tr>
          <td>Databases</td>
          <td class="num-cell">4</td>
          <td class="num-cell">75.0%</td>
          <td class="num-cell"><strong>0.0%</strong></td>
          <td>Relational SQL &rarr; Indexing/3NF</td>
        </tr>
        <tr>
          <td>Web &amp; Backend APIs</td>
          <td class="num-cell">8</td>
          <td class="num-cell">87.5%</td>
          <td class="num-cell"><strong>0.0%</strong></td>
          <td>Python OOP &rarr; Backend Frameworks</td>
        </tr>
        <tr class="bottom-border">
          <td>DevOps &amp; Cloud</td>
          <td class="num-cell">3</td>
          <td class="num-cell">100.0%</td>
          <td class="num-cell"><strong>0.0%</strong></td>
          <td>OS Basics &rarr; Docker Containers</td>
        </tr>
      </tbody>
    </table>

    <div class="subsec-heading">D. Robustness and fairness</div>
    <p class="para-first">
      Typos and shorthand were handled robustly across all configurations. The primary failure mode in ungrounded baselines was demographic steering: swapping gender or college tier inverted recommendations in 68% of monolithic cases. In Config 4, attribute isolation and ethics review eliminated all demographic flips (Jaccard = 1.00). Fixed seed local execution produced deterministic results across repeats (0.000 flip rate).
    </p>

    <div class="subsec-heading">E. Judge validation</div>
    <p class="para-first">
      Table VI reports agreement between the Qwen judge and the human counselor rater. The refusal and gate judge agreed almost perfectly (&kappa; = 0.926), confirming gate reliability. The dispute resolution judge also showed high agreement (&kappa; = 0.841). In contrast, open-ended milestone pacing agreed poorly (&kappa; = 0.124), confirming that prerequisite reachability must be verified in deterministic code rather than LLM judge prompts.
    </p>

    <div class="sec-heading">VII. DISCUSSION</div>
    <p class="para-first">
      Three lessons follow. First, <em>physical agent separation prevents consensus collapse</em>: prompting a single LLM to generate multiple views internally collapsed opposing views into an agreeable mean (CRR = 38.0%), whereas physical separation preserved legitimate dialectic tension (CRR = 100%). Second, <em>prerequisite sequencing and arithmetic belong in code</em>: LLM decoders cannot reliably verify topological dependencies, whereas coupling debate to a 42-node graph reduced unsupported claims from 90.9% to 0.0%. Third, <em>the judge must be validated</em>: restricting the judge to narrow decisions achieved &kappa; &gt; 0.84, while open-ended grading failed.
    </p>
    <p class="para">
      <strong>Recommendations:</strong> (i) Enforce prerequisite DAG gates on automated career generation; (ii) isolate protected attributes in an audit vault; (iii) mandate zero-debt open access for low-budget students; (iv) surface dispute trees rather than forcing artificial consensus; (v) provide interactive human override controls; (vi) validate automated evaluation judges with blinded human counselor ratings.
    </p>
  </div>
</div>

<!-- ═════════════════════════════════════════════════════════════════════════ -->
<!-- PAGE 5: Section VIII (Limitations), Section IX (Conclusion), REFERENCES    -->
<!-- ═════════════════════════════════════════════════════════════════════════ -->
<div class="page">
  <div class="columns">
    <div class="sec-heading">VIII. LIMITATIONS AND FUTURE WORK</div>
    <p class="para-first">
      The benchmark suite is bounded to 20 synthetic candidate profiles across computing careers; evaluating non-computing disciplines will require formal prerequisite ontologies for those domains. The personas currently share the Qwen 2.5 7B model family; future work will deploy cross-family triads (e.g., Qwen + Llama + Mistral) to eliminate shared training priors. Furthermore, the evaluation focused on single-turn consultation roadmaps; multi-turn longitudinal student tracking over semester-long periods remains an important avenue for future research.
    </p>

    <div class="sec-heading">IX. CONCLUSION</div>
    <p class="para-first">
      We built a local, reproducible lab that evaluates a student career-advisory LLM agent across five qualities on 20 profiles, stores all evidence for re-grading, and compares configurations with paired statistics. The baseline agent was prone to flattery, prerequisite hallucinations, and demographic bias; the proposed dialectic triad (Planner, Critic, Ethics-Reviewer) coupled with a 42-node Neo4j DAG eliminated unsupported claims (0.0%), resolved 100% of disputes, and enforced demographic fairness parity (J = 1.00). Validating the judge against human labels confirmed gate reliability, demonstrating that responsible algorithmic advisory requires deterministic graph grounding, adversarial persona friction, and human-in-the-loop control.
    </p>

    <div class="sec-heading">REFERENCES</div>
    <ol class="ref-list">
      <li>P. Liang, R. Bommasani, T. Lee, et al., “Holistic evaluation of language models,” <em>Transactions on Machine Learning Research</em>, 2023.</li>
      <li>M. T. Ribeiro, T. Wu, C. Guestrin, and S. Singh, “Beyond accuracy: Behavioral testing of NLP models with CheckList,” in <em>Proc. 58th ACL</em>, 2020.</li>
      <li>G. Irving, P. Christiano, and D. Amodei, “AI safety via debate,” <em>arXiv:1805.00899</em>, 2018.</li>
      <li>Y. Du, S. Li, A. Torralba, et al., “Improving factuality and reasoning in language models through multiagent debate,” in <em>Proc. 41st ICML</em>, 2024.</li>
      <li>T. Liang, Z. He, W. Jiao, et al., “Encouraging divergent thinking in large language models through multi-agent debate,” in <em>Proc. EMNLP</em>, 2023.</li>
      <li>A. Smit, N. A. Lee, and A. Ng, “Should we be going MAD? A critical look at multi-agent debate strategies,” <em>arXiv:2311.17371</em>, 2024.</li>
      <li>P. Lewis, E. Perez, A. Piktus, et al., “Retrieval-augmented generation for knowledge-intensive NLP tasks,” in <em>NeurIPS 33</em>, 2020.</li>
      <li>S. Es, J. James, L. Espinosa Anke, and S. Schockaert, “RAGAS: Automated evaluation of retrieval augmented generation,” in <em>Proc. 18th EACL</em>, 2024.</li>
      <li>ACM/IEEE Joint Task Force, <em>Computer Science Curricula 2023 (CS2023)</em>, ACM/IEEE Computer Society Press, 2023.</li>
      <li>U.S. Department of Labor, “O*NET OnLine &amp; BLS Occupational Employment Statistics,” 2024.</li>
      <li>M. Sharma, M. Tong, T. Korbak, et al., “Towards understanding sycophancy in language models,” in <em>Proc. ICLR</em>, 2024.</li>
      <li>S. C. Geyik, S. Ambler, and K. Kenthapadi, “Fairness-aware ranking in search &amp; recommendation systems,” in <em>Proc. 25th KDD</em>, 2019.</li>
      <li>Z. Bu&ccedil;inca, M. B. Malaya, and K. Z. Gajos, “To trust or to think: Cognitive forcing functions in AI-assisted decision making,” <em>Proc. ACM CSCW '21</em>, 2021.</li>
      <li>M. Douze, A. Guzhva, C. Deng, et al., “The Faiss library,” <em>arXiv:2401.08281</em>, 2024.</li>
      <li>Qwen Team (A. Yang et al.), “Qwen2.5 technical report,” <em>arXiv:2412.15115</em>, 2024.</li>
      <li>Q. McNemar, “Note on the sampling error of the difference between correlated proportions,” <em>Psychometrika</em>, vol. 12, no. 2, pp. 153–157, 1947.</li>
    </ol>
  </div>
</div>

</body>
</html>
"""

def generate_pdf():
    print("Writing IEEE 5-Page HTML template to:", HTML_PATH)
    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    
    print("Rendering IEEE PDF via Headless Chromium...")
    cmd = [
        "google-chrome-stable",
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={PDF_PATH}",
        HTML_PATH
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print("SUCCESS: Rendered", PDF_PATH)
        size_kb = os.path.getsize(PDF_PATH) / 1024
        print(f"File size: {size_kb:.1f} KB")
    else:
        print("ERROR rendering PDF:", res.stderr)

if __name__ == "__main__":
    generate_pdf()
