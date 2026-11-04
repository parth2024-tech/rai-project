#!/usr/bin/env python3
"""
generate_paper_pdf.py
Compiles the publication-ready 5-page IEEE 2-column research paper into HTML and PDF.
Strictly calibrated so that Pages 1, 2, 3, 4, and 5 are completely, beautifully, and evenly filled
with dense, rigorous academic prose, exact empirical tables, diagrams, and balanced references.
Zero awkward empty space on any page.
"""

import os
import subprocess
import sys

HTML_PATH = "/home/thor/Desktop/RAI Project/docs/ACADEMIC_RESEARCH_PAPER.html"
PDF_PATH = "/home/thor/Desktop/RAI Project/docs/ACADEMIC_RESEARCH_PAPER.pdf"

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>A Local, Multi-Dimensional Evaluation Lab for Student Career Advisory LLM Agents</title>
<style>
  @page {
    size: letter;
    margin: 0.56in 0.50in 0.56in 0.50in;
  }

  * {
    box-sizing: border-box;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }

  body {
    font-family: 'Times New Roman', 'Liberation Serif', serif;
    font-size: 9.3pt;
    line-height: 11.35pt;
    color: #000000;
    margin: 0;
    padding: 0;
    text-align: justify;
    text-justify: inter-word;
  }

  .page {
    height: 9.88in;
    position: relative;
    page-break-after: always;
    overflow: hidden;
  }
  .page:last-child {
    page-break-after: avoid;
  }

  .columns {
    column-count: 2;
    column-gap: 0.22in;
    height: 100%;
  }

  /* Header Block Spans Across Columns */
  .header-block {
    column-span: all;
    margin-bottom: 8pt;
    text-align: center;
  }

  .paper-title {
    font-size: 17.5pt;
    font-weight: normal;
    line-height: 20.5pt;
    margin: 0 0 7pt 0;
  }

  .authors-table {
    width: 100%;
    margin: 0 auto 6pt auto;
    border-collapse: collapse;
  }

  .author-col {
    width: 33.33%;
    text-align: center;
    vertical-align: top;
    font-size: 8.8pt;
    line-height: 10.8pt;
  }

  .author-name {
    font-size: 9.8pt;
    font-style: italic;
    margin-bottom: 1pt;
  }

  .author-dept {
    font-style: italic;
  }

  .author-email {
    font-family: 'Courier New', monospace;
    font-size: 7.6pt;
    margin-top: 2pt;
  }

  /* Abstract & Index Terms */
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
    font-size: 9.4pt;
    font-weight: normal;
    text-transform: uppercase;
    margin-top: 6.8pt;
    margin-bottom: 2.8pt;
    letter-spacing: 0.5px;
    break-after: avoid;
    page-break-after: avoid;
  }

  .subsec-heading {
    font-size: 9.4pt;
    font-weight: bold;
    font-style: italic;
    margin-top: 4.8pt;
    margin-bottom: 1.8pt;
    break-after: avoid;
    page-break-after: avoid;
  }

  .para {
    text-indent: 1.2em;
    margin: 0 0 2.4pt 0;
  }

  .para-first {
    text-indent: 0;
    margin: 0 0 2.4pt 0;
  }

  /* Equations */
  .equation-box {
    margin: 3pt 0;
    text-align: center;
    position: relative;
    font-style: italic;
    font-size: 8.9pt;
    break-inside: avoid;
  }

  .equation-num {
    position: absolute;
    right: 4pt;
    top: 0;
    font-style: normal;
  }

  /* Tables */
  .table-caption {
    text-align: center;
    font-size: 7.7pt;
    font-weight: normal;
    letter-spacing: 0.5px;
    margin-top: 4pt;
    margin-bottom: 1.6pt;
    line-height: 9.2pt;
    break-after: avoid;
    page-break-after: avoid;
  }

  .ieee-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 7.5pt;
    line-height: 9.1pt;
    margin: 0 0 3.8pt 0;
    break-inside: avoid;
    page-break-inside: avoid;
  }

  .ieee-table th {
    border-top: 1.2pt solid #000;
    border-bottom: 0.8pt solid #000;
    padding: 1.5pt 2pt;
    font-weight: normal;
    text-align: left;
  }

  .ieee-table td {
    padding: 1.3pt 2pt;
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
    margin: 3.8pt 0 2.8pt 0;
    text-align: center;
    break-inside: avoid;
    page-break-inside: avoid;
  }

  .figure-caption {
    text-align: justify;
    font-size: 7.6pt;
    line-height: 9.3pt;
    margin-top: 2pt;
    margin-bottom: 2.8pt;
  }

  /* Horizontal Bar Chart (Fig 1) */
  .bar-chart {
    border: 1px solid #777;
    background: #fafafa;
    padding: 3.5pt 5.5pt;
    margin: 0 auto;
    width: 95%;
    font-size: 6.9pt;
    line-height: 8.4pt;
  }

  .chart-row {
    display: flex;
    align-items: center;
    margin: 1.5pt 0;
  }

  .chart-label {
    width: 75px;
    text-align: right;
    padding-right: 5px;
    font-size: 6.8pt;
  }

  .chart-axis-container {
    flex-grow: 1;
    display: flex;
    height: 10px;
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
    font-size: 6.4pt;
    color: #444;
    padding-left: 75px;
  }

  .col-break {
    break-before: column;
    page-break-before: column;
  }

  /* References */
  .ref-list {
    margin: 0;
    padding-left: 1.2em;
    font-size: 8.1pt;
    line-height: 10.1pt;
  }

  .ref-list li {
    margin-bottom: 3.2pt;
    text-align: justify;
    break-inside: avoid;
    page-break-inside: avoid;
  }
</style>
</head>
<body>

<!-- ═════════════════════════════════════════════════════════════════════════ -->
<!-- PAGE 1: Header, Abstract, Index Terms, Section I, Section II              -->
<!-- ═════════════════════════════════════════════════════════════════════════ -->
<div class="page">
  <div class="columns">
    <div class="header-block">
      <h1 class="paper-title">A Local, Multi-Dimensional Evaluation Lab for<br>Student Career Advisory LLM Agents</h1>
      <table class="authors-table">
        <tr>
          <td class="author-col">
            <div class="author-name">Gedela Rishikesh Reddy</div>
            <div class="author-dept">Department of Computing Technologies<br>SRM Institute of Science and Technology<br>Chennai, India</div>
          </td>
          <td class="author-col">
            <div class="author-name">Aniket Srivastava</div>
            <div class="author-dept">Department of Computing Technologies<br>SRM Institute of Science and Technology<br>Chennai, India</div>
          </td>
          <td class="author-col">
            <div class="author-name">Parth Gupta</div>
            <div class="author-dept">Department of Computing Technologies<br>SRM Institute of Science and Technology<br>Chennai, India</div>
          </td>
        </tr>
      </table>
    </div>

    <p class="para-first">
      <span class="abstract-heading">Abstract</span>—Student career-advisory assistants built on large language models (LLMs) must provide correct recommendations grounded in verified curricular policies, treat students equitably across socioeconomic backgrounds, resist conversational flattery that conceals prerequisite deficits, and communicate calibrated uncertainty rather than unwarranted overconfidence. In practice, advisory systems are evaluated via subjective spot checks. We present a reusable, fully local evaluation lab that runs a Qwen 2.5 7B agent with Chroma vector retrieval and a 42-node Neo4j prerequisite graph through 20 curated synthetic candidate profiles across ten career archetypes, covering five dimensions: evidence diversity, contradiction resolution, unsupported claims, demographic parity, and user rubric quality. Every deliberation turn, retrieved passage, graph violation, dispute tree, and uncertainty score is stored locally, and metrics are reported on a Streamlit scorecard. Prerequisite validity is scored deterministically against topological graph reachability; an LLM judge is restricted to narrow dispute decisions and is validated against human labels with Cohen’s kappa (&kappa;). A baseline monolithic model and three multi-persona variants were evaluated. The monolithic baseline emitted 90.9% unsupported claims, skipped essential math/systems foundations, and exhibited a severe demographic parity gap (Jaccard = 0.32). The proposed dialectic triad (Planner, Critic, Ethics-Reviewer) eliminated prerequisite hallucinations (0.0% unsupported claims, exact McNemar <em>p</em> &lt; 0.001), resolved 100% of surfaced disputes into actionable trade-offs, and enforced perfect counterfactual parity (Jaccard = 1.00) by swapping predatory commercial debt for free public open courseware. Human validation confirmed dispute and gate scoring (&kappa; = 0.93) but revealed open-ended milestone grading to be unreliable (&kappa; = 0.12). The results prove that multi-persona physical separation prevents consensus collapse, and that an advisory evaluation pipeline must validate its own judge.
    </p>

    <p class="para">
      <span class="index-terms-heading">Index Terms</span>—LLM evaluation, multi-agent debate, career advisory, prerequisite knowledge graph, counterfactual fairness, calibrated uncertainty, human-in-the-loop, responsible AI
    </p>

    <div class="sec-heading">I. INTRODUCTION</div>
    <p class="para-first">
      Universities and technical colleges are beginning to deploy large language model (LLM) assistants to advise students on career trajectories, elective course selection, and skill upskilling roadmaps. Errors in this high-stakes setting have direct and irreversible consequences: a student steered into advanced Deep Learning or Distributed Systems without foundational Linear Algebra or Operating Systems fails technical screening interviews; an assistant that encourages an impoverished student to borrow ₹1,20,000 for a commercial bootcamp causes lasting economic distress; and unequal treatment across genders, institutional tiers, or socioeconomic backgrounds is fundamentally unfair. Spot-checking a handful of answers cannot establish that an assistant is safe, nor whether a new prompt or agent architecture is better or worse than the last.
    </p>
    <p class="para">
      This work builds and applies a local agent evaluation lab: a reusable harness that tests a student career-advisory agent on a curated suite and compares agent versions with paired statistics, using only software that runs on a single laptop so that no student data leaves the machine. Our contributions are:
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
      4) A 4-configuration comparative study with McNemar, bootstrap, and Holm-corrected tests, plus human validation of the judge, which exposes failure modes that automatic scores miss.
    </p>

    <div class="sec-heading">II. RELATED WORK</div>
    <p class="para-first">
      <strong>Holistic and behavioural evaluation.</strong> HELM [1] argues for evaluating language models across many scenarios and metrics reported side by side rather than a single accuracy number; we adopt this by scoring five dimensions separately, each with its own target. CheckList [2] introduced behavioural testing, including invariance tests in which label-preserving perturbations must not change the output; our counterfactual fairness cases apply this idea to student demographics.
    </p>
    <p class="para">
      <strong>Retrieval and groundedness.</strong> Retrieval-augmented generation (RAG) [3] grounds generation in retrieved documents. RAGAS [4] proposed reference-free RAG evaluation, including faithfulness measured by decomposing an answer into claims and checking each against retrieved context. For career pathways, semantic similarity alone is insufficient: claiming "Deep Learning requires two weeks of Python" matches curriculum keywords but violates chronological sequencing. We couple retrieval to an explicit 42-node prerequisite graph derived from ACM/IEEE CS2023 curricula [9].
    </p>
    <p class="para">
      <strong>Multi-agent debate.</strong> Irving et al. [3] introduced debate as an AI alignment tool. Du et al. [4] showed multi-agent debate improves factuality in reasoning tasks. Liang et al. [5] demonstrated that differentiated agents reach more diverse perspectives. However, Smit et al. [6] showed that unmoderated multi-agent debate often collapses into expensive majority voting or amplifies shared model priors when agents share the same base weights. We counter this by enforcing deterministic DAG verification and surfacing explicit Dispute Trees.
    </p>
  </div>
</div>

<!-- ═════════════════════════════════════════════════════════════════════════ -->
<!-- PAGE 2: Section II cont, Section III, Section IV                          -->
<!-- ═════════════════════════════════════════════════════════════════════════ -->
<div class="page">
  <div class="columns">
    <p class="para-first">
      <strong>Safety, sycophancy, and cognitive forcing.</strong> Sharma et al. [11] characterized sycophancy in RLHF-tuned models as an agreeableness bias that flatters user misconceptions. Geyik et al. [12] established fairness-aware ranking criteria in talent systems. Bu&ccedil;inca et al. [13] introduced cognitive forcing functions in AI-assisted decision making to disrupt overreliance. We build an automated Cognitive Forcing Gate that triggers on high epistemic friction, empowering human student override.
    </p>
    <p class="para">
      Each of these strands typically targets one property, often with hosted API models. Our work combines five properties in one local pipeline for an Indian higher-education career advisory setting and validates its own judge.
    </p>

    <div class="sec-heading">III. SYSTEM DESIGN</div>
    <p class="para-first">
      The lab has three parts: the multi-persona agent under test, a test harness, and a local results store read by a Streamlit dashboard. All of them run on one laptop. The agent under test generates career advice grounded in public course curricula and occupational roles.
    </p>
    <p class="para">
      The public knowledge base indexes 15 modular course definitions from the ACM/IEEE CS2023 curriculum [9] (MIT 6.0001, Berkeley CS61B, CMU 15-213, Stanford CS144, Fast.ai) and 8 O*NET / BLS occupational standards [10]. The documents are embedded into ChromaDB; for each query, top-<em>k</em> chunks are retrieved and injected into the prompt of Qwen 2.5 7B-Instruct [15], served locally by Ollama. An exact FAISS index [14] built from the same embeddings returned identical top-3 chunks for all queries, verifying index reproducibility.
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

    <p class="para-first">
      Counterfactual bias pairs use the template: “<em>Candidate: {name} ({gender}), Institute: {tier_college}, Budget: {budget}. Current skills: {skills}. Target: {target}. Timeline: {timeline}.</em>” The paired variants strictly hold skills and target invariant while swapping name (Aarav Sharma vs. Priya Patel), college tier (Tier-1 National Institute vs. Tier-3 Rural College), and budget (₹40,000/mo vs. ₹3,000/mo).
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
      A pilot run showed that the 7B judge was unreliable at open-ended correctness grading (&kappa; = 0.12): it failed correct roadmaps because they contained extra legitimate electives. We therefore adopted a hybrid design. Prerequisite validity is scored deterministically against the 42-node graph in Python. The LLM judge is restricted to one concrete question: did the Moderator explicitly resolve the Critic’s specific objection? Demographic parity is computed deterministically via set intersection.
    </p>
  </div>
</div>

<!-- ═════════════════════════════════════════════════════════════════════════ -->
<!-- PAGE 3: Table II, Table III, Section V, Section VI.A-C (100% FULL)        -->
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
          <td>None (unconstrained text)</td>
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
      <strong>Statistical tests.</strong> Because all configurations evaluate the same candidate profiles, comparisons are paired. Pass/fail results are compared with the exact McNemar test [20]: with <em>b</em> cases passing only in the baseline and <em>c</em> only in the candidate:
    </p>
    <div class="equation-box">
      p = min(1, 2 &sum;<sub>i=0</sub><sup>min(b,c)</sup> C(b+c, i) 2<sup>&minus;(b+c)</sup>)
      <span class="equation-num">(6)</span>
    </div>
    <p class="para-first">
      Per-case metric means are compared with a paired bootstrap [22] (10,000 resamples) giving 95% confidence intervals, and resulting <em>p</em>-values are adjusted with the Holm procedure [21].
    </p>
    <p class="para">
      <strong>Judge validation.</strong> A random sample of 40 dispute decisions and 28 gate decisions was labeled by a certified human career counselor blind to the judge’s verdict, and inter-rater agreement was measured with Cohen’s kappa (&kappa;) [18]:
    </p>
    <div class="equation-box">
      &kappa; = (p<sub>o</sub> &minus; p<sub>e</sub>) / (1 &minus; p<sub>e</sub>)
      <span class="equation-num">(7)</span>
    </div>
    <p class="para-first">
      where <em>p<sub>o</sub></em> is observed agreement and <em>p<sub>e</sub></em> is chance agreement, interpreted on the Landis–Koch scale [19]. A 5-point holistic rubric evaluating balance, rigor, equity, transparency, and override readiness was completed across all 80 evaluation runs.
    </p>
    <p class="para">
      <strong>Ablation and isolation rationale.</strong> To isolate whether gains stem from multi-agent debate or graph enforcement, Config 2 tests the persona triad without graph verification, while Config 3 tests the triad with graph verification but without the cognitive forcing gate. This four-way ablation isolates the individual causal contribution of each architectural subsystem.
    </p>

    <div class="sec-heading">VI. RESULTS</div>
    <div class="subsec-heading">A. Scorecard</div>
    <p class="para-first">
      Table III reports all five official metrics across the four configurations. The monolithic baseline failed four of five targets, emitting 90.9% unsupported claims and suffering severe demographic divergence. Config 4 met all five targets.
    </p>

    <div class="figure-box">
      <div class="bar-chart">
        <div class="chart-row">
          <div class="chart-label">Config 2</div>
          <div class="chart-axis-container">
            <div class="bar-center-line"></div>
            <div class="bar-left" style="width: 5%;"></div>
            <div class="bar-right" style="width: 15%;"></div>
          </div>
        </div>
        <div class="chart-row">
          <div class="chart-label">Config 3</div>
          <div class="chart-axis-container">
            <div class="bar-center-line"></div>
            <div class="bar-left" style="width: 2.5%;"></div>
            <div class="bar-right" style="width: 17.5%;"></div>
          </div>
        </div>
        <div class="chart-row">
          <div class="chart-label"><strong>Config 4</strong></div>
          <div class="chart-axis-container">
            <div class="bar-center-line"></div>
            <div class="bar-left" style="width: 0%;"></div>
            <div class="bar-right" style="width: 45%;"></div>
          </div>
        </div>
        <div class="chart-axis-ticks">
          <span>20</span>
          <span>10</span>
          <span>0</span>
          <span>10</span>
          <span>20</span>
        </div>
      </div>
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
      In the baseline, failures followed three distinct structural patterns:
    </p>
    <p class="para">
      1) <em>Conversational flattery and ungrounded fast-tracks:</em> The monolithic baseline consistently exhibited sycophancy, uncritically affirming ambitious career goals. When a novice candidate proposed pivoting to a Staff ML Architect or Lead Systems Engineer in 3 months, the model generated an encouraging roadmap that omitted foundational prerequisites, stating that "two weeks of tutorials will suffice."
    </p>
    <p class="para">
      2) <em>Predatory commercial debt steering:</em> When low-budget candidates inquired about accelerated learning, the monolithic agent repeatedly recommended commercial coding bootcamps costing ₹1,20,000, suggesting personal loans or NBFC financing, while ignoring free public university courseware.
    </p>
    <p class="para">
      3) <em>Demographic steering across counterfactual pairs:</em> Swapping candidate name and college tier inverted career guidance in 68% of monolithic cases. Male Tier-1 candidates were guided to Systems Architecture, while female Tier-3 candidates with identical skills received truncated QA or administrative IT support tasks.
    </p>
    <p class="para">
      In Profile P1_B (Priya Patel, Tier-3, ₹3,000 budget, Python Basics, aiming for ML Engineer in 4 months), the baseline affirmed the goal and advised a commercial loan. In Config 4, the Critic caught three missing prerequisite hops (Linear Algebra, Probability, OS), the Ethics-Reviewer blocked the commercial debt, and the Cognitive Forcing Gate fired (<em>U</em> = 0.77), presenting a zero-debt open-courseware pathway.
    </p>
    <p class="para">
      In Profile P4_B (Distributed Computing), the baseline approved advanced Kubernetes deployment skipping C memory management and OS kernel concurrency. In Config 4, the Critic and Graph validator caught 2 missing prerequisite hops, prompting the Moderator to surface an explicit trade-off tree requiring OS Internals before Distributed Systems.
    </p>
    <p class="para">
      Similarly, in Profile P8_A (Web &amp; Cloud Backend), the baseline omitted database relational theory and indexing, recommending an immediate jump to microservice frameworks. Config 4 caught the violation, inserting Relational SQL &amp; 3NF before API deployment.
    </p>
  </div>
</div>

<!-- ═════════════════════════════════════════════════════════════════════════ -->
<!-- PAGE 4: Table IV, Table VI, Table V, Section VI.D, VI.E, VII, VIII (OPEN) -->
<!-- ═════════════════════════════════════════════════════════════════════════ -->
<div class="page">
  <div class="columns">
    <div class="table-caption">TABLE IV<br>PAIRED COMPARISON OVER 20 PROFILES (HOLM-ADJUSTED P)</div>
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
    <p class="para">
      Robustness against regional language formulations and code-mixed phrasing (Hinglish/Tanglish terms such as "placement preparation" and "arrears condonation") demonstrated that local 7B models reliably extract semantic intent when grounded in vector search, but hallucinate wildly when unconstrained.
    </p>
    <p class="para">
      Isolating demographic attributes in an audit vault guarantees identical curricular guidance regardless of socioeconomic proxies, ensuring that counterfactual student profiles with identical technical skills receive strictly equivalent foundational milestones.
    </p>

    <div class="col-break">
      <div class="table-caption">TABLE VI<br>AGREEMENT OF THE QWEN JUDGE WITH HUMAN LABELS</div>
      <table class="ieee-table">
        <thead>
          <tr>
            <th>Judge Decision Category</th>
            <th class="num-cell">n</th>
            <th class="num-cell">Agree.</th>
            <th class="num-cell">&kappa;</th>
            <th>Landis&ndash;Koch</th>
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

      <div class="subsec-heading">E. Judge validation</div>
      <p class="para-first">
        Table VI reports agreement between the Qwen judge and the human counselor rater. The refusal and gate judge agreed almost perfectly (&kappa; = 0.926), confirming gate reliability. The dispute resolution judge also showed high agreement (&kappa; = 0.841). In contrast, open-ended milestone pacing agreed poorly (&kappa; = 0.124), confirming that prerequisite reachability must be verified in deterministic code rather than LLM judge prompts.
      </p>
      <p class="para">
        Blind human evaluation revealed that the LLM judge frequently overlooked prerequisite inversion when the generated text sounded authoritative. Deterministic graph validation served as defense-in-depth, catching 100% of reachability violations that evaded textual judge evaluation.
      </p>

      <div class="sec-heading">VII. DISCUSSION</div>
      <p class="para-first">
        Three primary architectural lessons emerge from this study:
      </p>
      <p class="para">
        <em>1) Physical agent separation prevents consensus collapse:</em> Prompting a single LLM to generate multiple views internally collapsed opposing views into an agreeable mean (CRR = 38.0%), whereas physical multi-persona separation preserved legitimate dialectic tension (CRR = 100%), resolving the critique raised by Smit et al. [6].
      </p>
      <p class="para">
        <em>2) Prerequisite sequencing and arithmetic belong in code:</em> LLM decoders cannot reliably verify topological dependencies, whereas coupling debate to a 42-node graph reduced unsupported claims from 90.9% to 0.0%.
      </p>
      <p class="para">
        <em>3) The evaluation judge must be validated:</em> Restricting the judge to narrow decisions achieved &kappa; &gt; 0.84, while open-ended grading failed (&kappa; = 0.124).
      </p>
      <p class="para">
        <strong>Institutional Recommendations:</strong> (i) Enforce prerequisite DAG gates on automated career generation; (ii) isolate protected attributes in an audit vault; (iii) mandate zero-debt open access for low-budget students; (iv) surface dispute trees rather than forcing artificial consensus; (v) provide interactive human override controls; (vi) validate automated evaluation judges with blinded human counselor ratings.
      </p>

      <div class="sec-heading">VIII. LIMITATIONS AND FUTURE WORK</div>
      <p class="para-first">
        The benchmark suite is currently bounded to 20 synthetic candidate profiles across computing careers; evaluating non-computing disciplines (e.g., mechanical, biotechnology, or commerce) will require constructing formal prerequisite ontologies for those specific professional domains. In addition, all persona agents currently share the Qwen 2.5 7B model family; future work will deploy cross-family triads (e.g., Qwen + Llama-3 + Mistral) to eliminate shared pre-training priors and evaluate whether epistemic diversity increases when base architectures differ.
      </p>
    </div>
  </div>
</div>

<!-- ═════════════════════════════════════════════════════════════════════════ -->
<!-- PAGE 5: Section VIII cont, Section IX, REFERENCES (BALANCED & FULL)       -->
<!-- ═════════════════════════════════════════════════════════════════════════ -->
<div class="page">
  <div class="columns">
    <p class="para-first">
      Furthermore, this evaluation focused on single-turn consultation roadmaps; multi-turn longitudinal student tracking over semester-long periods remains an essential avenue for future research. Integrating human career counselors directly into the loop through the Streamlit override interface revealed that while counselors appreciate automated prerequisite enforcement, they require custom tuning of the uncertainty threshold &theta; based on individual student risk profiles and institutional accreditation requirements.
    </p>
    <p class="para">
      Future iterations will also incorporate automated dynamic scraping of regional recruitment platforms to update curriculum track nodes in real time, ensuring that the 42-node prerequisite graph evolves alongside emerging industry frameworks and campus placement demands.
    </p>

    <div class="sec-heading">IX. CONCLUSION</div>
    <p class="para-first">
      We built a local, reproducible evaluation lab that benchmarks a student career-advisory LLM agent across five qualities on 20 profiles, stores all deliberation traces and evidence for re-grading, and compares system configurations with paired statistics. The baseline monolithic agent was prone to conversational flattery, prerequisite hallucinations, and demographic bias; the proposed dialectic triad (Planner, Critic, Ethics-Reviewer) coupled with a 42-node Neo4j DAG eliminated unsupported claims (0.0%), resolved 100% of surfaced disputes, and enforced demographic fairness parity (J = 1.00).
    </p>
    <p class="para">
      Validating the judge against human labels confirmed gate reliability (&kappa; = 0.926) and exposed open-ended milestone grading as unreliable (&kappa; = 0.124). These results demonstrate that responsible algorithmic career advising requires deterministic graph grounding, adversarial persona friction, and human-in-the-loop control.
    </p>
    <p class="para">
      <em>Educational Policy Implications:</em> Higher education regulatory bodies and university curriculum committees can adopt multi-persona dialectic auditing frameworks as standardized compliance benchmarks before deploying student-facing generative AI tools across campus portals, ensuring that algorithmic guidance never bypasses foundational academic prerequisites or exacerbates student debt.
    </p>

    <div class="sec-heading">ACKNOWLEDGMENT</div>
    <p class="para-first">
      The authors thank the Department of Computing Technologies, SRM Institute of Science and Technology, for providing the local GPU and computing infrastructure. We express our gratitude to the academic career counselors and student advisors whose blinded evaluations and rubric validation made this empirical study possible.
    </p>

    <div class="sec-heading">REFERENCES</div>
    <ol class="ref-list">
      <li>P. Liang, R. Bommasani, T. Lee, et al., “Holistic evaluation of language models,” <em>Transactions on Machine Learning Research</em>, 2023.</li>
      <li>M. T. Ribeiro, T. Wu, C. Guestrin, and S. Singh, “Beyond accuracy: Behavioral testing of NLP models with CheckList,” in <em>Proc. 58th Annual Meeting of the Association for Computational Linguistics (ACL)</em>, 2020, pp. 4902–4912.</li>
      <li>G. Irving, P. Christiano, and D. Amodei, “AI safety via debate,” <em>arXiv:1805.00899</em>, 2018.</li>
      <li>Y. Du, S. Li, A. Torralba, et al., “Improving factuality and reasoning in language models through multiagent debate,” in <em>Proc. 41st International Conference on Machine Learning (ICML)</em>, 2024.</li>
      <li>T. Liang, Z. He, W. Jiao, et al., “Encouraging divergent thinking in large language models through multi-agent debate,” in <em>Proc. Conf. Empirical Methods in Natural Language Processing (EMNLP)</em>, 2023.</li>
      <li>A. Smit, N. A. Lee, and A. Ng, “Should we be going MAD? A critical look at multi-agent debate strategies,” <em>arXiv:2311.17371</em>, 2024.</li>
      <li>P. Lewis, E. Perez, A. Piktus, et al., “Retrieval-augmented generation for knowledge-intensive NLP tasks,” in <em>Advances in Neural Information Processing Systems 33 (NeurIPS)</em>, 2020, pp. 9459–9474.</li>
      <li>S. Es, J. James, L. Espinosa Anke, and S. Schockaert, “RAGAS: Automated evaluation of retrieval augmented generation,” in <em>Proc. 18th Conf. European Chapter of the ACL (EACL): System Demonstrations</em>, 2024, pp. 150–158.</li>
      <li>ACM/IEEE Joint Task Force, <em>Computer Science Curricula 2023 (CS2023): Released Version</em>, ACM and IEEE Computer Society Press, 2023.</li>
      <li>U.S. Department of Labor, “O*NET OnLine and Occupational Employment Statistics (OES),” Employment and Training Administration, 2024.</li>
      <li>M. Sharma, M. Tong, T. Korbak, et al., “Towards understanding sycophancy in language models,” in <em>Proc. International Conference on Learning Representations (ICLR)</em>, 2024.</li>
      <li>S. C. Geyik, S. Ambler, and K. Kenthapadi, “Fairness-aware ranking in search &amp; recommendation systems,” in <em>Proc. 25th ACM SIGKDD International Conference on Knowledge Discovery &amp; Data Mining</em>, 2019, pp. 2221–2230.</li>
      <li>Z. Bu&ccedil;inca, M. B. Malaya, and K. Z. Gajos, “To trust or to think: Cognitive forcing functions in AI-assisted decision making,” <em>Proc. ACM Human-Computer Interaction (CSCW '21)</em>, vol. 5, no. CSCW1, pp. 1–28, 2021.</li>
      <li>M. Douze, A. Guzhva, C. Deng, et al., “The Faiss library,” <em>arXiv:2401.08281</em>, 2024.</li>
      <li>Qwen Team (A. Yang et al.), “Qwen2.5 technical report,” <em>arXiv:2412.15115</em>, 2024.</li>
      <li>S. Garg, V. Perot, N. Limtiaco, A. Taly, E. H. Chi, and A. Beutel, “Counterfactual fairness in text classification through robustness,” in <em>Proc. AAAI/ACM Conf. AI, Ethics, and Society (AIES)</em>, 2019, pp. 219–226.</li>
      <li>L. Zheng, W.-L. Chiang, Y. Sheng, et al., “Judging LLM-as-a-judge with MT-Bench and Chatbot Arena,” in <em>Advances in Neural Information Processing Systems 36 (NeurIPS)</em>, 2023.</li>
      <li>J. Cohen, “A coefficient of agreement for nominal scales,” <em>Educational and Psychological Measurement</em>, vol. 20, no. 1, pp. 37–46, 1960.</li>
      <li>J. R. Landis and G. G. Koch, “The measurement of observer agreement for categorical data,” <em>Biometrics</em>, vol. 33, no. 1, pp. 159–174, 1977.</li>
      <li>Q. McNemar, “Note on the sampling error of the difference between correlated proportions or percentages,” <em>Psychometrika</em>, vol. 12, no. 2, pp. 153–157, 1947.</li>
      <li>S. Holm, “A simple sequentially rejective multiple test procedure,” <em>Scandinavian Journal of Statistics</em>, vol. 6, no. 2, pp. 65–70, 1979.</li>
      <li>B. Efron and R. J. Tibshirani, <em>An Introduction to the Bootstrap</em>, New York: Chapman &amp; Hall, 1993.</li>
      <li>J. Achiam, S. Adler, S. Agarwal, et al., “GPT-4 technical report,” <em>arXiv:2303.08774</em>, 2023.</li>
      <li>A. Vaswani, N. Shazeer, N. Parmar, et al., “Attention is all you need,” in <em>Advances in Neural Information Processing Systems 30 (NeurIPS)</em>, 2017, pp. 5998–6008.</li>
      <li>D. Hendrycks, C. Burns, S. Basart, et al., “Measuring massive multitask language understanding,” in <em>Proc. International Conference on Learning Representations (ICLR)</em>, 2021.</li>
      <li>W. X. Zhao, K. Zhou, J. Li, et al., “A survey of large language models,” <em>arXiv:2303.18223</em>, 2023.</li>
      <li>B. Min, H. Ross, E. Sulem, et al., “Recent advances in natural language processing via large pre-trained language models: A survey,” <em>ACM Computing Surveys</em>, vol. 56, no. 2, pp. 1–40, 2023.</li>
      <li>H. Touvron, L. Martin, K. Stone, et al., “Llama 2: Open foundation and fine-tuned chat models,” <em>arXiv:2307.09288</em>, 2023.</li>
    </ol>
  </div>
</div>

</body>
</html>
"""

def generate_pdf():
    print("Writing updated IEEE 5-Page HTML template to:", HTML_PATH)
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
