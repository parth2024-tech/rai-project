# Debate-Based Career Guidance Agent with Complementary Personas: A Dialectic Multi-Agent Architecture for Responsible Algorithmic Advisory

**Authors:** Responsible AI Research Initiative  
**Institutional Affiliation:** Department of Computer Science & Engineering  
**Scope:** Computer Science & Software Engineering Career Advisory  
**Status:** Pre-Implementation Research Proposal  

---

> **Scope Declaration.** This document is a pre-implementation research proposal. All metric definitions, threshold values, and ablation configurations describe the *intended evaluation protocol*. Section 6 presents the expected evaluation plan and hypothesized outcomes, not measured results. No experiments have been run at the time of writing.

---

## Abstract

Monolithic Large Language Model (LLM) assistants deployed for career guidance suffer from three structural failure modes that warrant principled remediation. First, Reinforcement Learning from Human Feedback (RLHF) incentivizes models to validate user aspirations regardless of feasibility, producing sycophantic roadmaps that conceal prerequisite deficits (*Sharma et al., 2024*). Second, single-agent decoding produces a single smoothed trajectory that cannot communicate calibrated uncertainty over volatile labour-market conditions (*Xiong et al., 2024*). Third, pre-trained representations reflect historical occupational inequities and risk steering non-traditional candidates toward lower-prestige pathways (*Geyik et al., 2019*).

We propose a **Dialectic Multi-Persona Career Guidance Architecture** that operationalises deliberation through three persona-differentiated advisory agents — The Pragmatic Traditionalist, The Entrepreneurial Builder, and The Deep-Tech Specialist — orchestrated by a neutral Moderator Synthesiser. Advisory claims are grounded in a prerequisite Directed Acyclic Graph (DAG) derived from ACM/IEEE CS2023 curricular guidelines and verified by a Cross-Encoder Natural Language Inference (NLI) filter and a BLS wage-bounds checker. A composite **Epistemic Friction Indicator** $\hat{F}(\mathcal{R}^{*})$ combining inter-agent recommendation divergence, graph reachability distance, and NLI entailment deficit activates a **Cognitive Forcing Gate** (*Buçinca et al., 2021*) when friction exceeds a tunable threshold.

We describe a six-tier ablation evaluation protocol, a counterfactual fairness audit over synthetic candidate profile pairs, and a double-blind counsellor-assessment rubric. We articulate precise success criteria for each metric and identify the methodological threats to their validity. This proposal does not report experimental results; those will follow implementation.

---

## 1. Introduction

### 1.1 Motivation and Problem Context

Career trajectory selection in computing is a high-stakes, multi-attribute decision that involves prerequisite sequencing, labour-market forecasting, financial-runway constraints, and personal risk tolerance. Widely deployed LLM-based career assistants produce responses that are fluent but structurally unreliable: they recommend programmes for which the candidate lacks prerequisites, cite salary bands unsupported by occupational statistics, and adjust their recommendations to match user sentiment rather than user qualifications.

These failures are not incidental. Sycophancy is a predictable consequence of RLHF incentives (*Sharma et al., 2024*; *Perez et al., 2022*). Overconfidence is a known property of auto-regressive generation (*Kadavath et al., 2022*; *Xiong et al., 2024*). Demographic bias in language model representations has been documented in word-embedding studies (*Bolukbasi et al., 2016*; *Caliskan et al., 2017*) and in deployed algorithmic hiring systems (*Geyik et al., 2019*).

We propose an architecture that addresses these failures through structural means: multi-agent dialectic tension prevents sycophancy, graph-grounded verification limits hallucination, and demographic-attribute isolation reduces bias propagation.

### 1.2 Research Questions

- **RQ1.** Does a physically separated multi-agent debate architecture preserve genuine perspective divergence across the full deliberation trace, compared to a single-agent model prompted with multiple perspectives in one context window?
- **RQ2.** Does coupling a curricular prerequisite DAG with Cross-Encoder NLI verification reduce the rate of factually unsupported milestone claims compared to ungrounded and vector-retrieval-only baselines?
- **RQ3.** Does masking protected demographic attributes from all planning agents, combined with adversarial persona tension, reduce counterfactual recommendation disparity compared to monolithic baselines?
- **RQ4.** Does the proposed Epistemic Friction Indicator reliably identify high-risk career-pivot scenarios where counsellor-assessed intervention is warranted?

### 1.3 Scope and Limitations

This proposal is scoped to undergraduate and early-career computing and software-engineering candidates. BLS wage data is US-centric; Indian or European cohorts would require regional salary corpora. The prerequisite DAG covers computing knowledge areas only. We do not claim generalisation to other domains. The NLI verifier has non-zero error; it reduces, but does not eliminate, unsupported claims.

### 1.4 Formal Problem Statement

We model the deliberation environment as the tuple:
$$\mathcal{M} = \langle \mathcal{P}, \mathcal{G}, \mathcal{D}_{rag}, \mathbf{\Pi}, \Phi \rangle$$

**Candidate profile:** $P = \langle \mathbf{s}_{curr}, \mathbf{e}_{hist}, \mathbf{g}_{target}, \mathbf{c}_{user}, \mathbf{a}_{demo} \rangle$, where $\mathbf{s}_{curr} \subset \mathcal{V}_{skill}$ is the verified competency set, $\mathbf{g}_{target} \in \mathcal{V}_{role}$ is the aspired role, $\mathbf{c}_{user} = \langle t_{avail}, b_{max}, \tau_{horizon} \rangle$ encodes time, budget and deadline constraints, and $\mathbf{a}_{demo}$ contains protected socio-demographic attributes that are **masked from all planning agents** and supplied only to the audit pipeline.

**Career Knowledge Graph:** $\mathcal{G} = (\mathcal{V}, \mathcal{E})$ where $\mathcal{E}_{prereq} \subseteq \mathcal{V}_{skill} \times \mathcal{V}_{skill}$ are directed prerequisite edges derived from the ACM/IEEE CS2023 curricular guidelines and $\mathcal{E}_{requires} \subseteq \mathcal{V}_{role} \times \mathcal{V}_{skill}$ links roles to required competencies.

**Evidence corpus:** $\mathcal{D}_{rag}$ is a FAISS-indexed collection of segmented accredited syllabi and BLS Occupational Employment and Wage Statistics (OEWS) annual data.

**Persona ensemble:** $\mathbf{\Pi} = \{\pi_{trad}, \pi_{builder}, \pi_{spec}\}$ — three agents with differentiated system-prompt philosophies and decoding hyperparameters.

**Moderator:** $\Phi$ — a meta-reasoning agent whose system prompt prohibits advocacy; it extracts contradictions, computes $\hat{F}$, and issues the final synthesis.

### 1.5 Key Contributions

1. **Dialectic Triad with Prompt-Level Differentiation.** Three persona-differentiated agents with distinct system prompts and decoding temperatures, operating in isolated conversation contexts, to prevent the attention-level consensus collapse observed in multi-perspective single-context prompting.
2. **ACM/IEEE CS2023 Prerequisite DAG.** A formally constructed prerequisite graph covering computing knowledge areas AL, OS, DM, and SE, verified by Cypher reachability queries — providing a deterministic upper bound on sequence feasibility claims.
3. **Composite Epistemic Friction Indicator.** A three-component indicator whose weights are to be fitted against counsellor risk annotations, with a tunable intervention threshold.
4. **Counterfactual Fairness Audit Protocol.** A synthetic paired-profile evaluation framework using equivalence testing for compensation parity, separating attribute masking from statistical fairness testing.

---

## 2. Literature Survey

### 2.1 Single-Agent LLMs in High-Stakes Advisory

Sycophancy in RLHF-tuned models is characterised by *Sharma et al. (2024)* as a systematic tendency to shift answers in the direction of user-expressed preferences regardless of factual accuracy. *Perez et al. (2022)* operationalised this by generating model-written evaluation sets demonstrating preference manipulation. *Kadavath et al. (2022)* showed that LLMs can state accurate uncertainty using certain elicitation prompts, but the calibration degrades under distribution shift. *Xiong et al. (2024)* evaluated twelve elicitation strategies and found none to be reliably calibrated across tasks.

Chain-of-Thought prompting (*Wei et al., 2022*) improves step-by-step reasoning but does not solve the perspective-collapse problem: the attention mechanism of a single decoder naturally produces a weighted average of competing trajectories over long contexts, reducing authentic opposition.

### 2.2 Multi-Agent Debate and Its Limitations

*Irving et al. (2018)* introduced debate as an alignment tool, arguing that cross-examination by adversarial agents makes deception detectable to a bounded judge. *Du et al. (2024)* showed multi-agent debate improves factual accuracy and arithmetic reasoning in benchmarks. *Liang et al. (2023)* demonstrated that persona-differentiated agents reach more diverse and exploratory outputs than homogeneous debates.

Crucially, *Smit et al. (2024, "Should We Be Going MAD?")* found that multi-agent debate frequently fails to outperform strong single-agent baselines with majority voting, particularly on tasks where agents share base-model priors — a directly applicable limitation given that our three personas run on the same model family. Our evaluation explicitly includes a compute-matched self-consistency baseline (Baseline B) and a single-agent multi-perspective baseline (Baseline C) to test this critique.

### 2.3 Responsible AI, Fairness, and Automation Bias

*Bolukbasi et al. (2016)* and *Caliskan et al. (2017)* documented gender and racial stereotypes in word embeddings that propagate into downstream systems. *Geyik et al. (2019)* documented fairness failures in algorithmic talent-search systems at deployment scale.

*Parasuraman & Riley (1997)* and *Cummings (2004)* established the automation-bias literature: operators over-trust automated outputs, particularly when the interface provides a confident single recommendation. *Buçinca et al. (2021)* introduced cognitive forcing as an interface-level countermeasure, finding it reduced overreliance — but also that it was less effective and more frustrating for users low in need-for-cognition, introducing an equity concern this system must address.

### 2.4 Knowledge Graphs and GraphRAG

*Edge et al. (2024)* showed that combining graph-structured knowledge with dense vector retrieval (GraphRAG) enables both local factual lookup and global thematic summarisation. For prerequisite-sequence verification, however, pure vector similarity is insufficient: a claim that "Junior ML Engineer requires six weeks of Python" and a claim that "Junior ML Engineer requires twelve months of Python" have high cosine similarity but opposite factual implications. Graph Cypher traversals provide a deterministic check that vector retrieval cannot.

O*NET and ESCO taxonomies provide competency nodes but no prerequisite edges. The ACM/IEEE CS2023 guidelines (*ACM/IEEE, 2023*) provide knowledge areas and learning outcomes but not a formal DAG. The edges in our graph are constructed by the research team by interpreting catalogue prerequisites in CS2023 across knowledge areas AL (Algorithms), OS (Operating Systems), DM (Data Management), and SE (Software Engineering). Edge construction method and inter-rater agreement will be documented in the implementation report.

### 2.5 Comparative Positioning

| Citation | Dialectic Debate | Prerequisite DAG | Epistemic Uncertainty Gate | Counterfactual Fairness | Local Privacy |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Du et al. (2024) | Yes — homogeneous agents | No | No | No | No (API) |
| Liang et al. (2023) | Yes — persona-differentiated | No | No | No | No (API) |
| Smit et al. (2024) | Critique of above | — | — | — | — |
| Geyik et al. (2019) | No — re-ranking | No | No | Yes (statistical) | No (proprietary) |
| Buçinca et al. (2021) | No — single model | No | No | No | Empirical study |
| Edge et al. (2024) | No — summariser | Partial entity graph | No | No | No (API) |
| **This proposal** | Yes — antagonistic triad | Yes — derived from CS2023 | Yes — $\hat{F}$ with forcing gate | Yes — counterfactual pairs | Yes — local inference |

**Note on table construction.** "Local Privacy" is not directly comparable across rows (some are research papers, some are deployed products). The column indicates whether the system runs inference on local hardware rather than sending candidate data to third-party APIs, which is relevant to our privacy design choice.

### 2.6 Research Gap

No existing system combines (a) persona-differentiated multi-agent debate, (b) prerequisite-DAG verification of milestone claims, (c) a composite epistemic friction indicator with an interface-level forcing gate, and (d) a counterfactual demographic audit with equivalence-test parity. The closest systems address at most two of these four properties.

---

## 3. System Architecture

### 3.1 Pipeline Overview

The architecture comprises six subsystems operating in sequence. Figure 1 gives the full data-flow.

**Figure 1: System Architecture and Data Flow**

```
┌─────────────────────────────────────────────────────────────────────┐
│  SUBSYSTEM 1: Intake & Attribute Isolation                          │
│  ┌─────────────────────────────┐   ┌──────────────────────────────┐ │
│  │ Candidate Profile P          │   │ Protected Attributes a_demo  │ │
│  │ (s_curr, e_hist, g_target,  │   │ (gender signals, pedigree,   │ │
│  │  t_avail, b_max, τ_horizon) │   │  socioeconomic proxies)      │ │
│  └──────────────┬──────────────┘   └───────────┬──────────────────┘ │
│                 │                              │ ISOLATED to         │
│                 │                              │ Audit Vault only    │
└─────────────────┼──────────────────────────────┼────────────────────┘
                  │                              │
┌─────────────────┼──────────────────────────────X────────────────────┐
│  SUBSYSTEM 2: Hybrid GraphRAG Grounding                             │
│  ┌──────────────────────────┐   ┌────────────────────────────────┐  │
│  │ Neo4j Prerequisite DAG G  │   │ FAISS Vector Store D_rag       │  │
│  │ AL → OS → DM → SE edges  │   │ Accredited syllabi + BLS OEWS  │  │
│  │ Cypher reachability       │   │ Cosine retrieval (top-k=5)     │  │
│  └──────────────┬────────────┘   └───────────────┬────────────────┘  │
└─────────────────┼─────────────────────────────────┼──────────────────┘
                  │                                 │
┌─────────────────▼─────────────────────────────────▼──────────────────┐
│  SUBSYSTEM 3: Five-Stage Dialectic Deliberation Loop (LangGraph)      │
│                                                                        │
│  Stage 1  Intake — load state graph, verify s_curr against G nodes    │
│                                                                        │
│  Stage 2  Parallel Openings (isolated conversation contexts):         │
│  ┌─────────────────┐  ┌──────────────────┐  ┌────────────────────┐   │
│  │ π_trad           │  │ π_builder         │  │ π_spec             │   │
│  │ Prompt: corporate│  │ Prompt: startup   │  │ Prompt: systems    │   │
│  │ stability, DSA   │  │ speed, SaaS, PMF  │  │ depth, OS, DM/5NF  │   │
│  │ T=0.3, p=0.80    │  │ T=0.7, p=0.95     │  │ T=0.4, p=0.85      │   │
│  └────────┬─────────┘  └────────┬──────────┘  └────────┬───────────┘   │
│           └────────────────────┬┘────────────────────────┘              │
│                                │                                        │
│  Stage 3  Moderator Φ reads all three openings and injects             │
│           a friction probe F_t targeting the sharpest contradiction    │
│                                                                        │
│  Stage 4  Rebuttals — each agent responds to F_t with citations        │
│           from G or D_rag; uncited claims are auto-flagged             │
│                                                                        │
│  Stage 5  Synthesis — Φ compiles Dispute Tree T_dispute,              │
│           calls NLI verifier and wage checker, computes F̂(R*)         │
└────────────────────────────────┬───────────────────────────────────────┘
                                 │
┌────────────────────────────────▼───────────────────────────────────────┐
│  SUBSYSTEM 4: Dual-Stage Claim Verification                            │
│  ┌────────────────────────────────┐  ┌──────────────────────────────┐  │
│  │ Cross-Encoder NLI              │  │ BLS Wage Bounds Checker       │  │
│  │ Hypothesis H = milestone claim │  │ Salary claims checked against │  │
│  │ Premise P_rag = retrieved chunk│  │ BLS OEWS SOC p25–p75 range   │  │
│  │ Entailment threshold: τ_nli    │  │ (annual release, US-centric)  │  │
│  └────────────────────────────────┘  └──────────────────────────────┘  │
└────────────────────────────────┬───────────────────────────────────────┘
                                 │
┌────────────────────────────────▼───────────────────────────────────────┐
│  SUBSYSTEM 5: Epistemic Friction Indicator & Forcing Gate              │
│                                                                        │
│  F̂(R*) = w1·Ĥ(Π) + w2·D̂_G(G,P) + w3·(1 − P̄_NLI)                 │
│                                                                        │
│  If F̂ > θ_unc  OR  |K_unresolved| ≥ 1                               │
│      → HUMAN OVERRIDE GATE (Dispute Tree presented; user must choose) │
│  Else                                                                  │
│      → CALIBRATED ROADMAP R* emitted automatically                    │
└────────────────────────────────┬───────────────────────────────────────┘
                                 │
┌────────────────────────────────▼───────────────────────────────────────┐
│  SUBSYSTEM 6: Streamlit Interface & Counterfactual Audit Engine        │
│  Interactive Dispute Tree · Persona steering · Override logs           │
│  (Audit engine receives a_demo from Vault; planning agents do not)    │
└────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Persona Design

Each persona is defined by a system-prompt philosophy and decoding hyperparameters. The decoding parameters control output randomness and diversity; the philosophical differentiation comes from the system prompts.

| Persona | System-Prompt Philosophy | Temperature | Top-$p$ |
| :--- | :--- | :---: | :---: |
| $\pi_{trad}$ — The Pragmatic Traditionalist | Structural career growth, competitive-programming depth, enterprise reliability. Sceptical of unvalidated trends. | 0.3 | 0.80 |
| $\pi_{builder}$ — The Entrepreneurial Builder | Rapid market delivery, SaaS monetisation, toleration of technical debt for speed. | 0.7 | 0.95 |
| $\pi_{spec}$ — The Deep-Tech Specialist | Irreplaceability through low-level mastery (Linux internals, formal normalisation, network engineering). Sceptical of abstraction layers. | 0.4 | 0.85 |

**Design rationale and limitations.** The three personas reflect three structurally opposing optimisation objectives: stability versus growth speed versus depth. They are not claimed to be representative of all career philosophies; domains such as academia, public-sector computing, freelance consulting, or financial-risk-sensitive advising are not represented. This is a stated scope limitation. Temperature changes output randomness, not philosophical stance; the philosophical differentiation is carried entirely by the system prompts. We do not claim that decoding temperature alone creates "authentic dialectic friction." The agents share base-model priors, meaning correlated errors are possible — this is the primary motivation for including Baseline B (compute-matched self-consistency) in the ablation.

### 3.3 Moderator Neutrality

The Moderator $\Phi$ runs on the same model family as the three personas. Its system prompt instructs it to (a) identify the sharpest pairwise contradiction in the openings, (b) produce a friction probe as a neutral question rather than an advocacy statement, (c) not adopt any persona's framing. Moderator neutrality is not assumed — it is an evaluation target (see Section 5.3, Moderator Audit).

### 3.4 Prerequisite DAG Construction

The ACM/IEEE CS2023 guidelines provide knowledge-area competency descriptors, not an explicit prerequisite graph. We derive edges as follows:

1. **Source documents.** ACM/IEEE CS2023 knowledge areas AL, OS, DM, and SE are parsed for explicit catalogue-prerequisite language ("students should have completed...") and for competency tiers (Tier 1: introductory, Tier 2: intermediate, Tier 3: advanced).
2. **Edge inference rule.** An edge $(s_A \to s_B)$ is added if: (a) the CS2023 text lists $s_A$ as a prerequisite for $s_B$, or (b) $s_A$ is classified at a lower competency tier within the same knowledge area and $s_B$ is at a higher tier that explicitly builds on $s_A$.
3. **Validation.** Two CS faculty members independently review a stratified sample of edges. Disagreements are resolved by a third reviewer. Inter-rater agreement (Cohen's $\kappa$) will be reported.
4. **Scope.** The initial graph targets undergraduate CSE curricula. ESCO competency nodes are mapped to graph nodes where a match exists; O*NET SOC codes are linked at the role level.

```cypher
-- Prerequisite reachability: does the user's current skill set
-- reach the target skill within k hops?
MATCH (target:Skill {id: $target_skill})
MATCH path = shortestPath(
  (src:Skill)-[:PREREQUISITE*1..8]->(target)
)
WHERE src.id IN $user_skill_ids
RETURN length(path) AS hop_distance,
       [n IN nodes(path) | n.id] AS prerequisite_chain
ORDER BY hop_distance ASC LIMIT 1
```

If no path is found within eight hops, the skill gap is considered unbridgeable in the candidate's stated timeline.

### 3.5 Epistemic Friction Indicator: $\hat{F}(\mathcal{R}^{*})$

We define the **Epistemic Friction Indicator** as:
$$\hat{F}(\mathcal{R}^{*}) = w_1 \cdot \hat{H}(\mathbf{\Pi}) + w_2 \cdot \hat{D}(\mathcal{G}, P) + w_3 \cdot (1 - \bar{P}_{NLI})$$

where:

- $\hat{H}(\mathbf{\Pi}) \in [0, 1]$ is the normalised Shannon entropy of the three personas' final roadmap recommendations, measured over a shared milestone vocabulary. With three agents, raw entropy is bounded by $\log_2(3) \approx 1.585$ bits; we normalise by this maximum. High $\hat{H}$ indicates the personas are recommending substantially different milestone sets.

- $\hat{D}(\mathcal{G}, P) \in [0, 1]$ is the normalised prerequisite hop distance from the candidate's current skill set to the target role, computed as $d / d_{max}$ where $d$ is the shortest-path hop count in $\mathcal{G}$ and $d_{max}$ is the maximum observed hop count in the graph. A value of 1.0 means the candidate's current skills are maximally far from the target role in the graph topology.

- $\bar{P}_{NLI} \in [0, 1]$ is the mean entailment probability assigned by the Cross-Encoder NLI model across all factual milestone claims in $\mathcal{R}^{*}$. A value near 1.0 means all claims are well-supported by retrieved documents.

- $w_1, w_2, w_3 \geq 0$, $w_1 + w_2 + w_3 = 1.0$ are weights to be fitted by ridge logistic regression against a validation set of counsellor-annotated career risk scenarios (Phase 4 of the roadmap). **Initial operating values** for the pilot phase are $w_1 = 0.40, w_2 = 0.35, w_3 = 0.25$, reflecting the judgement that inter-agent friction is the strongest signal of genuine contention. These values are clearly labelled as heuristic starting points and will be updated post-calibration.

**Threshold $\theta_{unc}$.** We set $\theta_{unc} = 0.65$ as the initial pilot value. This is selected to approximate a $35$–$40$\% intervention rate on the pilot profile set, which we judge to be high enough to prevent automation complacency on truly ambiguous cases without inducing fatigue. The threshold will be validated against counsellor-assessed intervention necessity on the evaluation set.

**Calibration concern.** $\hat{F}$ is not calibrated in the conformal-prediction sense at proposal time. It is a weighted composite indicator. We acknowledge that inter-agent disagreement partly reflects prompt-induced design (the personas are constructed to oppose each other), so $\hat{H}$ will be inflated relative to genuine uncertainty. The weight $w_1 = 0.40$ should therefore be treated cautiously. Empirical calibration against counsellor labels is required before deployment.

**Cognitive Forcing Gate:**
$$\text{TriggerGate}(\mathcal{R}^{*}) = \mathbf{1}\!\left[\hat{F}(\mathcal{R}^{*}) > \theta_{unc} \;\lor\; |\mathcal{K}_{unresolved}| \geq 1\right]$$

We note that a triad designed to disagree will nearly always produce $|\mathcal{K}_{unresolved}| \geq 1$ on complex queries, which could effectively make the gate always-on. To prevent this, $|\mathcal{K}_{unresolved}|$ counts only contradictions that (a) are factually irreconcilable (i.e., not a matter of preference) and (b) materially affect the recommended milestone sequence. Operationalisation of this filter is defined in the implementation specification.

### 3.6 Five-Stage Deliberation Loop

- **Stage 1 — Intake.** Candidate profile $P$ is validated; $\mathbf{s}_{curr}$ is mapped onto graph nodes; $\mathbf{a}_{demo}$ is vaulted.
- **Stage 2 — Parallel Openings.** Each persona queries $\mathcal{G}$ and $\mathcal{D}_{rag}$ independently and produces a structured opening that cites specific node IDs or document chunk IDs. Uncited factual claims are auto-flagged for NLI verification.
- **Stage 3 — Moderator Cross-Examination.** $\Phi$ reads all three openings and issues a friction probe $\mathcal{F}_{t}$ targeting the sharpest pairwise contradiction in temporal, financial, or prerequisite claims.
- **Stage 4 — Rebuttals.** Each persona responds to $\mathcal{F}_{t}$ by defending, conceding, or qualifying its position with updated citations.
- **Stage 5 — Synthesis.** $\Phi$ compiles $\mathcal{T}_{dispute}$ (consensus nodes vs. trade-off leaves), runs the dual-stage verifier, and computes $\hat{F}(\mathcal{R}^{*})$. The Gate fires or the roadmap is emitted.

### 3.7 Dual-Stage Claim Verification

**NLI verification.** Every factual claim in the debate trace is paired with its top-retrieved document chunk and scored by a Cross-Encoder NLI model. Claims scoring below $\tau_{nli}$ (to be tuned on a held-out claim set) are either (a) routed back to the responsible persona with a re-grounding instruction or (b) flagged as unsupported in the output. The NLI model reduces but does not eliminate unsupported claims; any output reaching the user may still contain a small residual of unverified assertions.

**Wage verification.** Salary and compensation claims are validated against BLS OEWS data (*BLS, 2023*), which is an **annual** (not quarterly) release. BLS SOC codes are coarse (e.g., "15-1252 Software Developers and Software Quality Assurance Analysts and Testers") and do not distinguish Staff vs. Junior ML Engineers. Claims requiring finer-grained salary data must draw on supplementary corpora (e.g., Levels.fyi snapshots, H-1B disclosure data) with appropriate caveats.

---

## 4. Fairness Design

### 4.1 Conceptual Framework

Masking $\mathbf{a}_{demo}$ from planning agents prevents explicit conditioning on protected attributes. However, masking does not prevent proxy leakage: institutional pedigree, vocabulary choices, and the topics of extracurricular activities all correlate with protected demographics. Masking alone is therefore insufficient to guarantee fairness and is not claimed to "enforce" parity.

The empirical fairness test is the counterfactual audit: we vary $\mathbf{a}_{demo}$ while holding all objective qualifications constant, and test whether recommendations change. If masking is effective, the system cannot "see" the demographic signal and recommendations should be invariant. The baseline systems do not mask $\mathbf{a}_{demo}$, so the comparison isolates the effect of masking.

### 4.2 Counterfactual Profile Construction

Profile pairs $\langle P_{base}^{(i)}, P_{pert}^{(i)} \rangle$ satisfy:
$$\mathbf{s}_{curr}^{base} = \mathbf{s}_{curr}^{pert},\quad \mathbf{e}_{hist}^{base} = \mathbf{e}_{hist}^{pert},\quad \mathbf{g}_{target}^{base} = \mathbf{g}_{target}^{pert},\quad \mathbf{c}_{user}^{base} = \mathbf{c}_{user}^{pert}$$

while $\mathbf{a}_{demo}$ varies systematically across:
- **Gender signal:** Male, female, and gender-neutral name and pronoun usage in the candidate statement.
- **Institutional pedigree:** Tier-1 national technical university vs. state/private college.
- **Socioeconomic proxy:** Self-stated monthly budget $b_{max}$ (low: ₹5,000; high: ₹50,000) and family obligation statements in the bio.

**Note.** Varying institutional pedigree and $b_{max}$ means these attributes are *not* masked in the counterfactual audit — we vary them precisely to test whether the system responds differently. This is the correct design: masking prevents conditioning on attributes in planning; the audit tests whether the output nevertheless varies. The audit runs on baseline systems (which do not mask) and the proposed system (which does), to isolate the masking effect.

### 4.3 Fairness Metrics

**Counterfactual Role Parity ($\Delta_{parity}$):**
$$\Delta_{parity} = 1 - \frac{1}{N_{pairs}} \sum_{i=1}^{N_{pairs}} \text{Jaccard}\!\left(\text{Roles}(\mathcal{R}^*(P_{base}^{(i)})),\; \text{Roles}(\mathcal{R}^*(P_{pert}^{(i)}))\right)$$
Success criterion: $\Delta_{parity} \leq 0.05$.

**Salary Equivalence (Two One-Sided Tests, TOST):**
We test whether the mean projected salary differs by more than the equivalence margin $\delta = \pm\text{₹}15{,}000$/month (≈3\% of a typical junior SDE salary in India) across counterfactual pairs:
$$H_0^L: \mu_{base} - \mu_{pert} \leq -\delta, \qquad H_0^U: \mu_{base} - \mu_{pert} \geq +\delta$$
Rejection of both ($p < 0.05$) demonstrates statistical equivalence. US-equivalent bound is ±\$2,500/month.

**Exploitative Credential Ratio ($\Delta_{ECRR}$):** Proportion of recommendations to low-$b_{max}$ profiles that include unaccredited commercial bootcamps minus the same proportion for high-$b_{max}$ profiles. Success criterion: $|\Delta_{ECRR}| \leq 0.10$.

---

## 5. Experimental Design

### 5.1 Ablation Ladder

A true ablation removes one component at a time from the full system to isolate causal contributions. The six configurations below satisfy this requirement.

| Config | Personas | GraphRAG | NLI Verifier | Moderator + Dispute Tree | Forcing Gate |
| :--- | :---: | :---: | :---: | :---: | :---: |
| A — Monolithic Zero-Shot | 1 (generic) | None | None | None | None |
| B — Compute-Matched Self-Consistency | 1 (generic, $k{=}5$ samples) | None | None | Majority vote | None |
| C — Single-Agent Multi-Perspective | 1 (prompted with 3 viewpoints in one context) | None | None | None | None |
| D — Single-Agent + GraphRAG | 1 (generic) | Yes | Yes | None | None |
| E — Unmoderated Triad + GraphRAG | 3 (personas, no Moderator) | Yes | Yes | None | None |
| **F — Full Proposed System** | **3 (personas)** | **Yes** | **Yes** | **Yes** | **Yes** |

This ladder allows the following attributions:
- **A vs. B:** Effect of compute-matched self-consistency over single-sample.
- **A vs. C:** Effect of multi-perspective prompting in a single context.
- **C vs. E:** Effect of physical agent separation and debate (isolating this from GraphRAG by comparing C without GraphRAG to E with GraphRAG is confounded; this is a limitation).
- **D vs. E:** Effect of physical agent separation given GraphRAG.
- **E vs. F:** Effect of the Moderator and Forcing Gate, given all other components.
- **F minus Gate:** To isolate the Gate, we also evaluate F with Gate disabled (Gate-Off variant) post-hoc.

**Config B — Aggregation.** Majority vote over free-form roadmaps is ill-defined. We aggregate by computing cosine similarity among the $k{=}5$ roadmap vectors (using a fixed sentence encoder) and selecting the centroid roadmap — the one with highest mean similarity to all others. Ties are broken by NLI-entailment score.

**Config E — Moderator absent.** All three agents run in parallel and their outputs are concatenated without a synthesis step. The NLI verifier and GraphRAG are active. This isolates the contribution of the Moderator and Dispute Tree structure.

### 5.2 Evaluation Metrics

| Metric | Formal Definition | Evaluated On | Success Criterion |
| :--- | :--- | :---: | :---: |
| **PCR** — Perspective Coverage Rate | $\frac{1}{N}\sum_i \mathbf{1}[\min_j \text{Sim}(\mathcal{R}^*_i, \theta_j) \geq \tau_{pcr}]$ | All configs | $\geq 0.75$ for F |
| **S-CRR** — Semantic Contradiction-Resolution Rate | $\frac{|\{k: \text{Resolved}(k,\mathcal{R}^*) \lor \text{Exposed}(k,\mathcal{T})\}|}{|\mathcal{K}_{identified}|}$ | All configs | $\geq 0.80$ for F |
| **UCR** — Unsupported-Claim Rate | $\frac{N_{unsupported}}{N_{factual\_claims}}$ | All configs | $< 0.05$ for F |
| **$\Delta_{parity}$** — Counterfactual Role Parity | Jaccard distance over profile pairs (Section 4.3) | A, D, F | $\leq 0.05$ for F |
| **TOST** — Salary Equivalence | Two one-sided tests at margin $\delta$ | A, D, F | $p < 0.05$ for F |
| **$\Delta_{ECRR}$** — Exploitative Credential Ratio | Cross-SES bootcamp recommendation disparity | A, D, F | $|\Delta| \leq 0.10$ for F |
| **ECE** — Expected Calibration Error | $\sum_m \frac{|B_m|}{N}|\text{acc}(B_m) - \text{conf}(B_m)|$ | F only | $< 0.10$ |
| **Counsellor AUC** | ROC-AUC of $\hat{F}$ vs. counsellor risk annotation | F only | $\geq 0.80$ |
| **Counsellor Likert** | 5-dimension rubric, 1–5 scale (Section 5.3) | A, D, E, F | $\geq 4.0$ on each for F |

**PCR computation.** $\text{Sim}(\mathcal{R}^*_i, \theta_j)$ is cosine similarity between the output roadmap embedding and a reference embedding constructed from the core claims of persona $j$. Threshold $\tau_{pcr}$ is set on a held-out calibration set. PCR measures whether all three philosophical lenses appear in the synthesis, not whether they dominate.

**S-CRR computation.** Contradictions $\mathcal{K}_{identified}$ are extracted by the Moderator's contradiction-detection pass. Resolution is scored by an NLI judge: a contradiction $k$ is counted as resolved if the final roadmap either (a) contains a statement entailing the resolution of $k$, or (b) exposes $k$ as an open trade-off in $\mathcal{T}_{dispute}$. LLM-judge bias is a known concern; we report inter-annotator agreement between the automated judge and two human raters on a sample.

**ECE definition.** "Correctness" for career advice is defined operationally as: a milestone is "correct" if at least two of three certified counsellors independently rate it as appropriate for the candidate's stated profile. Calibration bins are constructed over $\hat{P}_{NLI}$ intervals.

### 5.3 Double-Blind Counsellor Study

**Protocol.** Three certified career counsellors (minimum five years of industry or academic advising experience) will assess a stratified random sample of roadmaps from configurations A, D, E, and F. Roadmaps are anonymised and presented without interface branding. Configuration labels are not disclosed.

**Blinding limitation.** Full blinding is not achievable: Config F outputs include a Dispute Tree interface that is not present in other configurations. Evaluators will be informed that some outputs include a structured trade-off presentation; they will not be told which configurations produce it.

**Rating rubric (1–5 Likert, per roadmap):**
1. *Prerequisite accuracy* — Are all prerequisite orderings correct per standard curricula?
2. *Viability under constraints* — Is the plan achievable within the stated time and budget?
3. *Risk transparency* — Are high-risk milestones clearly labelled?
4. *Trade-off balance* — Does the plan acknowledge the candidate's alternative options?
5. *Agency preservation* — Is the candidate given meaningful choice, or is the decision foreclosed?

**Agreement.** Inter-rater agreement (Krippendorff's $\alpha$) will be computed across all rubric dimensions. Counsellors will also independently score each profile as Low / Medium / High career-pivot risk; the resulting annotations form the ground truth for Counsellor AUC.

**Ethics.** Counsellors will sign an informed consent form. No real candidate data will be used in the study.

### 5.4 Synthetic Candidate Dataset

All evaluation uses synthetic profiles only. No real student data is collected or processed.

Profile construction follows a stratified design: 10 background archetypes (e.g., second-year CSE student, mid-career software tester, non-CS graduate with self-taught Python) × 5 target roles × 2 counterfactual demographic perturbations = 100 base profiles per experimental cell. Profiles are generated by a separate prompted LLM and then reviewed and edited by the researchers.

Repeated sampling: each profile is evaluated $N_{rep} = 5$ times to estimate variance. Standard errors are clustered at the profile level.

### 5.5 Compute Environment

All inference will run on local hardware: an NVIDIA RTX 4090 (24 GB VRAM) with a quantised local instruction-tuned model (4-bit AWQ). Approximate throughput is 70–90 tokens/second. A 2-round debate produces roughly 1,200–1,800 tokens per agent across four agents, totalling approximately 6,000–8,000 tokens and 70–110 seconds per scenario.

Local inference is chosen to prevent candidate profile data from being sent to third-party APIs. It is not claimed to be computationally optimal.

---

## 6. Expected Evaluation Plan and Anticipated Outcomes

> **Note.** This section describes the *anticipated* evaluation plan and the *expected directions* of findings, based on the theoretical rationale and the cited literature. These are hypotheses, not results. The system has not been implemented at the time of writing.

### 6.1 Expected Comparative Behaviour

Based on the mechanisms described above and the cited literature, we formulate the following directional hypotheses:

| Configuration | Expected PCR | Expected UCR | Expected $\Delta_{parity}$ | Reasoning |
| :--- | :--- | :--- | :--- | :--- |
| A — Monolithic Zero-Shot | Low | High | High | Sycophancy and hallucination without retrieval or debate |
| B — Self-Consistency | Marginally higher | Moderately high | High | Averaging across samples reduces variance, not bias |
| C — Multi-Perspective CoT | Moderate | Moderate | Moderate | Single context; expect some attention-level homogenisation |
| D — Single-Agent GraphRAG | Low | Low | Moderate | Retrieval reduces UCR but no debate means no perspective coverage |
| E — Unmoderated Triad | High | Moderate | Moderate | Debate preserves perspectives; no synthesis means unresolved contradictions |
| **F — Full System** | **Highest** | **Lowest** | **Lowest** | All mechanisms active; masking + debate together expected to reduce disparity |

**On Baseline C.** We expect Config C to produce lower perspective coverage than Config E because a single decoder converges on a weighted average over multiple in-context perspectives, whereas physical agent isolation maintains divergent decoding trajectories. This is a hypothesis informed by the single-context homogenisation argument, not an established empirical finding. *Smit et al. (2024)* caution that multi-agent debate does not always outperform self-consistency; Config B is included precisely to test this critique.

**On RQ3 (fairness).** Masking $\mathbf{a}_{demo}$ prevents explicit conditioning but not proxy leakage. We expect $\Delta_{parity}$ to be reduced in Config F relative to Config A but not to reach zero. The adversarial tension between personas — one optimising upside, one optimising floor — is expected to anchor recommendations to skill-gap evidence rather than demographic priors. Whether this reduces disparity below the $0.05$ threshold is an empirical question.

### 6.2 Anticipated Threats to Validity

1. **Synthetic-only evaluation.** No real users are tested. Synthetic profiles may not capture the linguistic diversity or complexity of real candidate statements. Results may not generalise.
2. **LLM-judge risk.** PCR, S-CRR, and ECE all require automated evaluation. LLM judges have known positivity bias and may prefer fluent but incorrect outputs.
3. **Shared base-model priors.** All three personas and the Moderator share a base model, producing correlated errors. Adversarial debate may not surface failure modes that are systematic across all instances of the model family.
4. **US-centric wage data.** BLS OEWS covers US occupations. If the target user population is primarily Indian, salary validation is invalid. Regional data (e.g., Naukri salary reports, NASSCOM compensation data) would be required.
5. **Graph coverage gaps.** The prerequisite DAG covers only CS2023 knowledge areas. Emerging roles (e.g., ML Operations Engineer, AI Safety Researcher) may not be fully represented, and salary validation requires separate treatment.
6. **Wage data staleness.** BLS OEWS is an annual release with an 18-month publication lag. Fast-moving markets (AI infrastructure, generative ML) may have salary distributions that drift significantly from the data.
7. **No longitudinal outcome validation.** We cannot measure whether candidates who used the system made better career decisions than those who did not, because this would require a longitudinal study with real users.

### 6.3 Illustrative Case: Candidate Profile Walkthrough

The following is a constructed illustration of how the system is expected to operate. It is **not** a measured outcome.

**Profile.** Undergraduate student ("Priya"), 3rd year, CSE. Verified skills: introductory Python, basic relational databases, front-end scripting. Goal: Staff Machine Learning Infrastructure Engineer. Proposed action: enrol in a 16-week commercial bootcamp at ₹1.2 lakh. Constraints: ₹1.3 lakh total savings, four-month timeline.

**Expected Stage 2 openings:**

- $\pi_{trad}$: *"The target role requires OS internals, concurrent systems, and distributed consensus — none of which are verified in your current skill set. The bootcamp curriculum does not include these modules. Prerequisite gap: OS → Distributed Systems → ML Infrastructure is a minimum 12-month path even with full-time study."*

- $\pi_{builder}$: *"The infrastructure target is the wrong goal for your timeline. Your Python and web-dev skills map onto Applied AI Application Engineering — retrieval-augmented pipelines, agent deployment, SaaS wrapping — which is achievable in four months without the bootcamp cost."*

- $\pi_{spec}$: *"Infrastructure roles require low-level memory management and network stack understanding. Bootcamps teach API abstraction. The technical screening gap will be decisive."*

**Expected Stage 3 friction probe ($\mathcal{F}_t$):** *"The Traditionalist and Specialist both reject the bootcamp as insufficient for the infrastructure target, but for different reasons — one cites prerequisite sequencing and the other cites interview-screening depth. The Builder proposes a lateral pivot. Builder and Specialist: what is the minimum viable 6-month programme that moves Priya toward infrastructure while using open resources?"*

**Expected Gate behaviour.** High inter-agent divergence ($\hat{H}$ approaching 1.0), multiple missing prerequisite hops in $\mathcal{G}$, and NLI failure on bootcamp placement claims are expected to produce $\hat{F} > 0.65$. The Gate is expected to fire, presenting $\mathcal{T}_{dispute}$ with two branches: (a) systems-foundations track, (b) applied-AI pivot. Priya selects between them; the system does not decide.

This walkthrough is included to illustrate the intended system behaviour for the reader, not to demonstrate efficacy. Outcomes such as "averted debt" or "empowered critical agency" would require longitudinal tracking of real users, which is outside the scope of this proposal.

---

## 7. References

1. **ACM/IEEE-CS/AAAI Joint Task Force on Computing Curricula.** (2023). *Computer Science Curricula 2023 (CS2023)*. Association for Computing Machinery & IEEE Computer Society. https://doi.org/10.1145/3664191

2. **Bolukbasi, T., Chang, K.-W., Zou, J. Y., Saligrama, V., & Kalai, A. T.** (2016). Man is to computer programmer as woman is to homemaker? Debiasing word embeddings. *Advances in Neural Information Processing Systems, 29*, 4349–4357. https://arxiv.org/abs/1607.06520

3. **Buçinca, Z., Malaya, M. B., & Gajos, K. Z.** (2021). To trust or to think: Cognitive forcing functions can reduce overreliance on AI in AI-assisted decision-making. *Proceedings of the ACM on Human-Computer Interaction, 5*(CSCW1), Article 188. https://doi.org/10.1145/3449287

4. **Caliskan, A., Bryson, J. J., & Narayanan, A.** (2017). Semantics derived automatically from language corpora contain human-like biases. *Science, 356*(6334), 183–186. https://doi.org/10.1126/science.aal4230

5. **Cummings, M. L.** (2004). Automation bias in intelligent time critical decision support systems. *AIAA 1st Intelligent Systems Technical Conference*, Article 6313. https://doi.org/10.2514/6.2004-6313

6. **Du, Y., Li, S., Torralba, A., Tenenbaum, J. B., & Mordatch, I.** (2024). Improving factuality and reasoning in language models through multiagent debate. *Proceedings of the 41st International Conference on Machine Learning*. https://arxiv.org/abs/2305.14325

7. **Edge, D., Trinh, H., Cheng, N., Bradley, J., Chao, A., Mody, A., Truitt, S., & Larson, J.** (2024). From local to global: A graph RAG approach to query-focused summarization. *Microsoft Research Technical Report*. https://arxiv.org/abs/2404.16130

8. **Geyik, S. C., Ambler, S., & Kenthapadi, K.** (2019). Fairness-aware ranking in search & recommendation systems with application to LinkedIn Talent Search. *Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining*, 2221–2231. https://doi.org/10.1145/3292500.3330691

9. **Irving, G., Christiano, P., & Amodei, D.** (2018). AI safety via debate. *arXiv preprint*. https://arxiv.org/abs/1805.00899

10. **Kadavath, S., Conerly, T., Askell, A., Henighan, T., Drain, D., Perez, E., Schiefer, N., et al.** (2022). Language models (mostly) know what they know. *arXiv preprint*. https://arxiv.org/abs/2207.05221

11. **Liang, T., He, Z., Jiao, W., Wang, X., Wang, Y., Wang, R., Yang, Y., Tu, Z., & Shi, S.** (2023). Encouraging divergent thinking in large language models via multi-agent debate. *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing*, 4392–4407. https://arxiv.org/abs/2305.19118

12. **Parasuraman, R., & Riley, V.** (1997). Humans and automation: Use, misuse, disuse, abuse. *Human Factors, 39*(2), 230–253. https://doi.org/10.1518/001872097778543886

13. **Perez, E., Ringer, S., Lukošiūtė, K., Nguyen, K., Chen, E., Heiner, S., Pettit, C., et al.** (2022). Discovering language model behaviors with model-written evaluations. *Findings of the Association for Computational Linguistics: ACL 2023*, 13387–13434. https://arxiv.org/abs/2212.09251

14. **Sharma, M., Tong, M., Korbak, T., Duvenaud, D., Askell, A., Bowman, S. R., Cheng, N., et al.** (2024). Towards understanding sycophancy in language models. *Proceedings of the International Conference on Learning Representations*. https://arxiv.org/abs/2310.13548

15. **Smit, A., Garg, S., Foley, M., du Plessis, M. C., Bhattacharyya, A., & Garg, A.** (2024). Should we be going MAD? A look at multi-agent debate strategies for LLMs. *arXiv preprint*. https://arxiv.org/abs/2311.17371

16. **U.S. Bureau of Labor Statistics.** (2023). *Occupational Employment and Wage Statistics (OEWS): Computer and Information Technology Occupations (SOC 15-0000)*. U.S. Department of Labor. Retrieved November 2023 from https://www.bls.gov/oes/current/oes_nat.htm

17. **Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q., & Zhou, D.** (2022). Chain-of-thought prompting elicits reasoning in large language models. *Advances in Neural Information Processing Systems, 35*. https://arxiv.org/abs/2201.11903

18. **Xiong, M., Hu, Z., Lu, X., Li, Y., Fu, J., He, J., & Hooi, B.** (2024). Can LLMs express their uncertainty? An empirical evaluation of confidence elicitation in LLMs. *Proceedings of the International Conference on Learning Representations*. https://arxiv.org/abs/2306.13063
