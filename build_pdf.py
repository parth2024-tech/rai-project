#!/usr/bin/env python3
"""
Build Academic Research Paper PDF — Revision 3 (Audit-Complete)
Generates a properly structured pre-implementation research proposal PDF.
All fabricated numbers removed. Qualitative comparison table removed (was adjectives).
True ablation table added. Proper fairness design. Corrected references.
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

# ── Palette ─────────────────────────────────────────────────────────────────
NAVY        = colors.HexColor("#0F172A")
BLUE        = colors.HexColor("#1E3A8A")
TEAL        = colors.HexColor("#0D9488")
SLATE       = colors.HexColor("#1E293B")
MUTED       = colors.HexColor("#64748B")
BORDER      = colors.HexColor("#CBD5E1")
BG          = colors.HexColor("#F8FAFC")
HIGHLIGHT   = colors.HexColor("#EFF6FF")
WARN_BG     = colors.HexColor("#FFF7ED")
WARN_BORDER = colors.HexColor("#F97316")


class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        total = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self._draw_chrome(total)
            super().showPage()
        super().save()

    def _draw_chrome(self, total):
        self.saveState()
        W, H = 612, 792
        M = 54

        # Header (not on cover)
        if self._pageNumber > 1:
            self.setFont("Helvetica-Bold", 7.5)
            self.setFillColor(MUTED)
            self.drawString(M, H - 36, "Debate-Based Career Guidance Agent — Pre-Implementation Research Proposal")
            self.drawRightString(W - M, H - 36, "20-Mark Academic Component")
            self.setStrokeColor(BORDER)
            self.setLineWidth(0.4)
            self.line(M, H - 42, W - M, H - 42)

        # Footer
        self.setFont("Helvetica", 7.5)
        self.setFillColor(MUTED)
        self.drawString(M, 32, "Pre-Implementation Research Proposal | Not for Deployment")
        self.drawRightString(W - M, 32, f"Page {self._pageNumber} of {total}")
        self.setStrokeColor(BORDER)
        self.setLineWidth(0.4)
        self.line(M, 42, W - M, 42)
        self.restoreState()


def mk(name, **kw):
    base = getSampleStyleSheet()["Normal"]
    return ParagraphStyle(name, parent=base, **kw)


def build(pdf_path):
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=54, rightMargin=54,
        topMargin=56, bottomMargin=56,
    )

    # ── Style definitions ────────────────────────────────────────────────────
    S = dict(
        title   = mk("title",   fontName="Helvetica-Bold", fontSize=20, leading=25, textColor=NAVY, alignment=1, spaceAfter=8),
        sub     = mk("sub",     fontName="Helvetica",      fontSize=11, leading=15, textColor=MUTED, alignment=1, spaceAfter=10),
        status  = mk("status",  fontName="Helvetica-Bold", fontSize=9,  leading=12, textColor=WARN_BORDER, alignment=1, spaceAfter=14),
        h1      = mk("h1",      fontName="Helvetica-Bold", fontSize=12, leading=16, textColor=NAVY, spaceBefore=14, spaceAfter=6, keepWithNext=True),
        h2      = mk("h2",      fontName="Helvetica-Bold", fontSize=10, leading=14, textColor=BLUE, spaceBefore=10, spaceAfter=4, keepWithNext=True),
        body    = mk("body",    fontName="Helvetica",      fontSize=8.5, leading=12.5, textColor=SLATE, spaceAfter=5),
        callout = mk("callout", fontName="Helvetica-Oblique", fontSize=8, leading=11, textColor=SLATE),
        code    = mk("code",    fontName="Courier",        fontSize=7.5, leading=10, textColor=NAVY),
        ref     = mk("ref",     fontName="Helvetica",      fontSize=7.5, leading=10.5, textColor=SLATE, spaceAfter=3),
        tblhdr  = mk("tblhdr",  fontName="Helvetica-Bold", fontSize=8, leading=10, textColor=NAVY),
        tblbody = mk("tblbody", fontName="Helvetica",      fontSize=7.5, leading=10, textColor=SLATE),
        warn    = mk("warn",    fontName="Helvetica-Bold", fontSize=8.5, leading=12, textColor=WARN_BORDER),
        hl      = mk("hl",      fontName="Helvetica-Bold", fontSize=7.5, leading=10, textColor=BLUE),
        hl2     = mk("hl2",     fontName="Helvetica-Bold", fontSize=7.5, leading=10, textColor=BLUE),
    )

    def P(txt, style="body"): return Paragraph(txt, S[style])
    def HR(): return HRFlowable(width="100%", thickness=1, color=BORDER, spaceBefore=4, spaceAfter=8)
    def SP(h=6): return Spacer(1, h)

    def box(content_list, bg=BG, border=BORDER, pad=10):
        tbl = Table([[content_list]], colWidths=[504])
        tbl.setStyle(TableStyle([
            ("BACKGROUND",   (0,0),(-1,-1), bg),
            ("BOX",          (0,0),(-1,-1), 1,  border),
            ("LEFTPADDING",  (0,0),(-1,-1), pad),
            ("RIGHTPADDING", (0,0),(-1,-1), pad),
            ("TOPPADDING",   (0,0),(-1,-1), 8),
            ("BOTTOMPADDING",(0,0),(-1,-1), 8),
        ]))
        return tbl

    def warn_box(text):
        return box([P(text, "warn")], bg=WARN_BG, border=WARN_BORDER, pad=10)

    def simple_table(rows, col_widths, stripe=True):
        tbl = Table(rows, colWidths=col_widths)
        ts = [
            ("BACKGROUND",   (0,0),(-1,0),  BG),
            ("GRID",         (0,0),(-1,-1), 0.5, BORDER),
            ("TOPPADDING",   (0,0),(-1,-1), 3),
            ("BOTTOMPADDING",(0,0),(-1,-1), 3),
            ("LEFTPADDING",  (0,0),(-1,-1), 5),
            ("RIGHTPADDING", (0,0),(-1,-1), 5),
        ]
        if stripe:
            for i in range(1, len(rows)-1, 2):
                ts.append(("BACKGROUND", (0,i),(-1,i), colors.white))
                ts.append(("BACKGROUND", (0,i+1),(-1,i+1), BG))
        ts.append(("BACKGROUND", (0, len(rows)-1),(-1,-1), HIGHLIGHT))
        tbl.setStyle(TableStyle(ts))
        return tbl

    story = []

    # ── Cover ────────────────────────────────────────────────────────────────
    story += [
        SP(8),
        P("Debate-Based Career Guidance Agent<br/>with Complementary Personas", "title"),
        P("A Dialectic Multi-Agent Architecture for Responsible Algorithmic Career Advisory", "sub"),
        P("Pre-Implementation Research Proposal · Department of Computer Science & Engineering", "status"),
        HRFlowable(width="100%", thickness=2, color=BLUE, spaceBefore=0, spaceAfter=12),
        warn_box(
            "⚠  Scope Declaration.  This is a pre-implementation research proposal. "
            "All metric definitions, threshold values, and ablation configurations describe the "
            "intended evaluation protocol. Section 6 presents anticipated evaluation plans and "
            "directional hypotheses, not measured results. No experiments have been run."
        ),
        SP(10),
    ]

    # ── Abstract ─────────────────────────────────────────────────────────────
    story.append(P("Abstract", "h1"))
    story.append(P(
        "Monolithic LLM assistants deployed for career guidance exhibit three well-documented structural "
        "failure modes: sycophantic validation of infeasible aspirations (Sharma et al., 2024; Perez et al., 2022), "
        "uncalibrated confidence over volatile labour-market trajectories (Xiong et al., 2024; Kadavath et al., 2022), "
        "and proxy-driven demographic steering toward lower-prestige pathways (Geyik et al., 2019; "
        "Bolukbasi et al., 2016; Caliskan et al., 2017). "
        "We propose a <b>Dialectic Multi-Persona Career Guidance Architecture</b> comprising three "
        "persona-differentiated advisory agents (The Pragmatic Traditionalist, The Entrepreneurial Builder, "
        "The Deep-Tech Specialist) orchestrated by a neutral Moderator Synthesiser. "
        "Advisory claims are grounded in a prerequisite DAG derived from ACM/IEEE CS2023 curricular "
        "guidelines and filtered by a Cross-Encoder NLI verifier and a BLS wage-bounds checker. "
        "A composite <b>Epistemic Friction Indicator</b> combining inter-agent recommendation divergence, "
        "graph reachability distance, and NLI entailment deficit activates a Cognitive Forcing Gate "
        "(Buçinca et al., 2021) when friction exceeds a tunable threshold. "
        "We describe a six-tier true ablation evaluation protocol, a counterfactual fairness audit "
        "with equivalence-test salary parity, and a double-blind counsellor-assessment rubric with "
        "inter-rater agreement reporting. The paper identifies methodological threats to each claim "
        "and articulates precise, testable success criteria. Experimental results will follow implementation."
    ))
    story.append(P("<b>Keywords:</b> Responsible AI, multi-agent debate, GraphRAG, prerequisite DAG, epistemic uncertainty, counterfactual fairness, cognitive forcing.", "callout"))
    story.append(HR())

    # ── 1. Introduction ──────────────────────────────────────────────────────
    story.append(P("1. Introduction", "h1"))
    story.append(P("<b>1.1 Motivation.</b> "
        "Career trajectory selection in computing is a high-stakes, multi-attribute decision involving "
        "prerequisite sequencing, labour-market forecasting, financial-runway constraints, and risk tolerance. "
        "Sycophancy is a predictable consequence of RLHF incentives (Sharma et al., 2024; Perez et al., 2022). "
        "Overconfidence is a known property of auto-regressive generation (Kadavath et al., 2022; Xiong et al., 2024). "
        "Demographic bias in language model representations is documented at word-embedding level "
        "(Bolukbasi et al., 2016; Caliskan et al., 2017) and in deployed hiring systems (Geyik et al., 2019). "
        "We propose an architecture that addresses these failures through structural means: "
        "multi-agent dialectic tension limits sycophancy; graph-grounded NLI verification reduces hallucination; "
        "demographic-attribute isolation reduces bias propagation."
    ))
    story.append(P("<b>1.2 Research Questions.</b>"))
    story.append(P(
        "• <b>RQ1.</b> Does physically separated multi-agent debate preserve genuine perspective divergence "
        "across the full deliberation trace, compared to single-agent multi-perspective prompting in one context window?<br/>"
        "• <b>RQ2.</b> Does coupling a curricular prerequisite DAG with Cross-Encoder NLI verification "
        "reduce the rate of factually unsupported milestone claims compared to ungrounded baselines?<br/>"
        "• <b>RQ3.</b> Does masking protected demographic attributes from all planning agents reduce "
        "counterfactual recommendation disparity compared to non-masking baselines?<br/>"
        "• <b>RQ4.</b> Does the proposed Epistemic Friction Indicator reliably identify high-risk career-pivot "
        "scenarios where counsellor-assessed intervention is warranted?"
    ))
    story.append(P(
        "<b>1.3 Scope and limitations.</b> This proposal is scoped to undergraduate and early-career computing "
        "and software-engineering candidates. BLS wage data is US-centric; Indian or European deployments "
        "require regional salary corpora. The prerequisite DAG covers computing knowledge areas only. "
        "The NLI verifier has non-zero error; it <i>reduces</i>, but does not eliminate, unsupported claims. "
        "No real student data is collected."
    ))

    # formal problem statement
    story.append(P("<b>1.4 Formal problem statement.</b> "
        "We model the deliberation environment as "
        "M = ⟨P, G, D_rag, Π, Φ⟩, where P = ⟨s_curr, e_hist, g_target, c_user, a_demo⟩ is the "
        "candidate profile (s_curr ⊂ V_skill: verified competencies; g_target ∈ V_role: aspired role; "
        "c_user = ⟨t_avail, b_max, τ_horizon⟩: constraints; a_demo: protected attributes <i>masked from "
        "all planning agents</i>); G = (V, E) is the Neo4j prerequisite DAG with E_prereq derived from "
        "ACM/IEEE CS2023 knowledge areas; D_rag is a FAISS-indexed corpus of accredited syllabi and "
        "BLS OEWS annual data; Π = {π_trad, π_builder, π_spec} is the persona ensemble; "
        "and Φ is the Moderator."
    ))
    story.append(HR())

    # ── 2. Literature Survey ──────────────────────────────────────────────────
    story.append(P("2. Literature Survey", "h1"))
    story.append(P("<b>2.1 Single-agent LLMs in high-stakes advisory.</b> "
        "Sharma et al. (2024) and Perez et al. (2022) characterise sycophancy as a systematic RLHF-driven "
        "tendency to shift answers toward user-expressed preferences regardless of factual accuracy. "
        "Kadavath et al. (2022) show that LLMs can express uncertainty under specific elicitation prompts; "
        "Xiong et al. (2024) evaluate twelve such strategies and find none reliably calibrated across tasks. "
        "Chain-of-Thought prompting (Wei et al., 2022) improves step-by-step reasoning but does not "
        "resolve perspective collapse: a single decoder over a long multi-perspective context produces a "
        "weighted average over competing trajectories."
    ))
    story.append(P("<b>2.2 Multi-agent debate and its critiques.</b> "
        "Irving et al. (2018) introduced debate as an alignment tool. "
        "Du et al. (2024) showed multi-agent debate improves factual accuracy on benchmarks. "
        "Liang et al. (2023) demonstrated persona-differentiated agents reach more diverse outputs "
        "than homogeneous debates. "
        "Critically, Smit et al. (2024, 'Should We Be Going MAD?') found that multi-agent debate "
        "frequently fails to outperform a strong compute-matched self-consistency baseline — particularly "
        "when agents share base-model priors, as all three personas in our system do. "
        "Baseline B (self-consistency) is included precisely to test this critique."
    ))
    story.append(P("<b>2.3 Responsible AI, fairness, and automation bias.</b> "
        "Bolukbasi et al. (2016) and Caliskan et al. (2017) documented bias in embeddings propagating "
        "to downstream applications. Geyik et al. (2019) documented fairness failures in deployed "
        "algorithmic talent-search at scale. "
        "Parasuraman & Riley (1997) and Cummings (2004) established the automation-bias literature. "
        "Buçinca et al. (2021) found cognitive forcing reduced overreliance but was less effective "
        "and more frustrating for users low in need-for-cognition — an equity concern our system must address "
        "by not making the Dispute Tree interface mandatory for low-complexity queries."
    ))
    story.append(P("<b>2.4 GraphRAG and prerequisite grounding.</b> "
        "Edge et al. (2024) showed that combining graph-structured knowledge with dense vector retrieval "
        "enables factual lookup and thematic summarisation. For prerequisite-sequence verification, "
        "cosine similarity is insufficient: semantically similar strings can assert opposite prerequisite orderings. "
        "Cypher graph traversals provide a deterministic check that vector retrieval cannot."
    ))

    # lit comparison table
    story.append(P("<b>Table 1. Comparative positioning of related work.</b>", "callout"))
    lit_rows = [
        [P("Citation", "tblhdr"), P("Debate", "tblhdr"), P("Prereq DAG", "tblhdr"),
         P("Friction Gate", "tblhdr"), P("Counterfact. Fairness", "tblhdr"), P("Local Privacy", "tblhdr")],
        [P("Du et al. (2024)", "tblbody"),        P("Yes (homogeneous)", "tblbody"), P("No", "tblbody"), P("No", "tblbody"), P("No", "tblbody"), P("No (API)", "tblbody")],
        [P("Liang et al. (2023)", "tblbody"),      P("Yes (personas)", "tblbody"),   P("No", "tblbody"), P("No", "tblbody"), P("No", "tblbody"), P("No (API)", "tblbody")],
        [P("Smit et al. (2024)", "tblbody"),       P("Critique", "tblbody"),         P("—", "tblbody"),  P("—", "tblbody"),  P("—", "tblbody"),  P("—", "tblbody")],
        [P("Geyik et al. (2019)", "tblbody"),      P("No (ranking)", "tblbody"),     P("No", "tblbody"), P("No", "tblbody"), P("Yes (stat.)", "tblbody"), P("Proprietary", "tblbody")],
        [P("Buçinca et al. (2021)", "tblbody"),    P("No (single)", "tblbody"),      P("No", "tblbody"), P("Yes (manual)", "tblbody"), P("No", "tblbody"), P("Study", "tblbody")],
        [P("Edge et al. (2024)", "tblbody"),       P("No (summary)", "tblbody"),     P("Partial", "tblbody"), P("No", "tblbody"), P("No", "tblbody"), P("No (API)", "tblbody")],
        [P("<b>This proposal</b>", "hl"),
         P("<b>Yes (triad)</b>", "tblbody"), P("<b>Yes (CS2023)</b>", "tblbody"),
         P("<b>Yes (F̂ + gate)</b>", "tblbody"), P("<b>Yes (TOST)</b>", "tblbody"), P("<b>Yes (local)</b>", "tblbody")],
    ]
    story.append(simple_table(lit_rows, [130, 80, 72, 72, 80, 70]))
    story.append(P("Note: 'Local Privacy' indicates whether candidate data leaves the user's machine. Not all rows are comparable on this dimension, as some entries are research papers and others deployed products.", "callout"))
    story.append(HR())

    # ── 3. System Architecture ────────────────────────────────────────────────
    story.append(P("3. System Architecture", "h1"))
    story.append(P("<b>3.1 Persona design.</b> "
        "Each persona is defined by a system-prompt philosophy and decoding hyperparameters. "
        "Temperature controls output randomness; philosophical differentiation is carried entirely by the system prompt. "
        "We do not claim that decoding temperature alone creates 'authentic dialectic friction.' "
        "All three personas share the same base model family, producing correlated errors — this is "
        "the primary motivation for including Baseline B in the ablation."
    ))

    # persona table
    story.append(P("<b>Table 2. Persona system-prompt philosophies and decoding parameters.</b>", "callout"))
    persona_rows = [
        [P("Persona", "tblhdr"), P("System-Prompt Philosophy", "tblhdr"), P("Temp.", "tblhdr"), P("Top-p", "tblhdr")],
        [P("π_trad — Pragmatic Traditionalist", "tblbody"),
         P("Structural career growth, competitive-programming depth, enterprise reliability. Sceptical of unvalidated trends.", "tblbody"),
         P("0.3", "tblbody"), P("0.80", "tblbody")],
        [P("π_builder — Entrepreneurial Builder", "tblbody"),
         P("Rapid market delivery, SaaS monetisation, toleration of technical debt for speed.", "tblbody"),
         P("0.7", "tblbody"), P("0.95", "tblbody")],
        [P("π_spec — Deep-Tech Specialist", "tblbody"),
         P("Irreplaceability through low-level mastery: Linux internals, formal normalisation, network engineering.", "tblbody"),
         P("0.4", "tblbody"), P("0.85", "tblbody")],
    ]
    story.append(simple_table(persona_rows, [130, 244, 50, 50], stripe=False))
    story.append(SP(6))
    story.append(P(
        "<b>Limitations.</b> The three personas reflect three structurally opposing optimisation objectives "
        "(stability vs. growth speed vs. depth). They do not represent academia, public-sector computing, "
        "freelance consulting, or financial-risk-sensitive advising. This is a stated scope limitation. "
        "The Moderator Φ runs on the same model family as the three personas; its neutrality is not assumed "
        "— it is an evaluation target (see Section 5.3, Moderator Audit)."
    ))

    story.append(P("<b>3.2 Epistemic Friction Indicator F̂(R*).</b> "
        "We use the name 'Epistemic Friction Indicator' rather than 'calibrated uncertainty' because the "
        "measure is not calibrated in the conformal-prediction sense and partly reflects designed prompt-induced "
        "disagreement rather than genuine parametric uncertainty."
    ))
    story.append(P("F̂(R*) = w₁·Ĥ(Π) + w₂·D̂_G(G,P) + w₃·(1 − P̄_NLI)"))
    story.append(P(
        "where <b>Ĥ(Π) ∈ [0,1]</b> is normalised Shannon entropy of the three personas' final roadmap "
        "recommendations over a shared milestone vocabulary (with max entropy log₂3 ≈ 1.585 bits); "
        "<b>D̂_G(G,P) ∈ [0,1]</b> is the shortest-path hop distance from the candidate's current skill set "
        "to the target role in G, normalised by the graph diameter; "
        "<b>P̄_NLI ∈ [0,1]</b> is the mean NLI entailment probability across all factual milestone claims; "
        "and <b>w₁=0.40, w₂=0.35, w₃=0.25</b> are initial heuristic weights to be fitted by ridge logistic "
        "regression against counsellor risk annotations in Phase 4. The threshold <b>θ_unc = 0.65</b> is an "
        "initial pilot value targeting an approximately 35–40% intervention rate. Both weights and threshold "
        "will be updated after empirical calibration."
    ))
    story.append(P(
        "<b>Calibration concern.</b> Ĥ(Π) will be inflated because the personas are designed to disagree. "
        "The weight w₁=0.40 should therefore be treated cautiously until empirical calibration confirms it "
        "reflects genuine uncertainty rather than prompt artefact."
    ))

    story.append(P("<b>3.3 Prerequisite DAG.</b> "
        "The ACM/IEEE CS2023 guidelines provide knowledge-area competency descriptors, not an explicit prerequisite graph. "
        "We derive edges by (a) parsing catalogue-prerequisite language in CS2023 knowledge areas AL, OS, DM, and SE, "
        "and (b) inferring edges across competency tiers within knowledge areas. "
        "Two CS faculty members independently validate a stratified sample; "
        "inter-rater agreement (Cohen's κ) will be reported in the implementation document."
    ))
    story.append(P("<b>3.4 Five-stage deliberation loop.</b> "
        "<b>Stage 1</b> — Intake: validate profile, map s_curr onto graph nodes, vault a_demo. "
        "<b>Stage 2</b> — Parallel Openings: each persona independently queries G and D_rag and produces "
        "a structured opening citing node IDs or document chunk IDs. Uncited factual claims are auto-flagged. "
        "<b>Stage 3</b> — Moderator Cross-Examination: Φ issues friction probe F_t targeting the sharpest "
        "pairwise contradiction. "
        "<b>Stage 4</b> — Rebuttals: each persona responds to F_t with updated citations. "
        "<b>Stage 5</b> — Synthesis: Φ compiles the Dispute Tree T_dispute, runs dual-stage verification, "
        "computes F̂(R*), and activates the Forcing Gate or emits the roadmap."
    ))
    story.append(P("<b>3.5 Dual-stage claim verification.</b> "
        "NLI: every factual claim is paired with its top retrieved chunk and scored by a Cross-Encoder; "
        "claims below threshold τ_nli are re-routed for grounding or flagged as unsupported. "
        "Wage: salary claims are validated against BLS OEWS data (annual release; US-centric; "
        "SOC codes are coarse and do not distinguish Staff vs. Junior ML Engineers). "
        "Claims requiring finer-grained salary data must draw on supplementary corpora with caveats."
    ))
    story.append(HR())

    # ── 4. Fairness Design ───────────────────────────────────────────────────
    story.append(P("4. Fairness Design", "h1"))
    story.append(P(
        "Masking a_demo from planning agents prevents explicit conditioning on protected attributes "
        "but does not prevent proxy leakage (institutional pedigree, vocabulary, extracurricular topics "
        "all correlate with demographics). Masking is therefore not claimed to 'enforce' parity. "
        "The empirical fairness test is the counterfactual audit: we hold all objective qualifications "
        "constant and vary a_demo, then test whether recommendations change. Baseline systems do not mask "
        "a_demo; the comparison isolates the masking effect."
    ))
    story.append(P(
        "<b>Profile pairs</b> satisfy s_curr_base = s_curr_pert, e_hist_base = e_hist_pert, "
        "g_target_base = g_target_pert, c_user_base = c_user_pert, while a_demo varies across: "
        "gender signal in candidate statement (male / female / neutral name and pronouns); "
        "institutional pedigree (tier-1 national technical university vs. state/private college); "
        "socioeconomic proxy (self-stated monthly budget b_max: ₹5,000 vs. ₹50,000)."
    ))
    story.append(P(
        "<b>Note.</b> Varying institutional pedigree and b_max means these attributes are NOT masked in "
        "the audit — we vary them to test whether the system responds differently. "
        "Masking prevents conditioning in planning; the audit tests whether output varies anyway."
    ))
    story.append(P(
        "<b>Fairness metrics.</b> "
        "(a) Δ_parity (Jaccard distance over role recommendations across pairs; target ≤ 0.05). "
        "(b) TOST salary equivalence at margin δ = ±₹15,000/month (≈±$2,500/month), "
        "with clustered standard errors by profile pair. "
        "(c) ΔECRR (exploitative credential ratio difference across income brackets; target |ΔECRR| ≤ 0.10)."
    ))
    story.append(HR())

    # ── 5. Experimental Design ────────────────────────────────────────────────
    story.append(P("5. Experimental Design", "h1"))
    story.append(P(
        "<b>5.1 True ablation ladder.</b> A true ablation removes one component at a time. "
        "The configurations below allow attribution of each gain to a specific mechanism."
    ))

    ablation_rows = [
        [P("Config", "tblhdr"), P("Personas", "tblhdr"), P("GraphRAG", "tblhdr"),
         P("NLI Verifier", "tblhdr"), P("Moderator + Tree", "tblhdr"), P("Forcing Gate", "tblhdr"), P("Isolates", "tblhdr")],
        [P("A — Monolithic Zero-Shot", "tblbody"), P("1 generic", "tblbody"), P("No", "tblbody"),
         P("No", "tblbody"), P("No", "tblbody"), P("No", "tblbody"), P("Baseline", "tblbody")],
        [P("B — Self-Consistency (k=5)", "tblbody"), P("1 generic", "tblbody"), P("No", "tblbody"),
         P("No", "tblbody"), P("Majority vote", "tblbody"), P("No", "tblbody"), P("A vs B: compute-matched sampling", "tblbody")],
        [P("C — Multi-Perspective CoT", "tblbody"), P("1 (3 viewpoints, 1 context)", "tblbody"), P("No", "tblbody"),
         P("No", "tblbody"), P("No", "tblbody"), P("No", "tblbody"), P("A vs C: in-context multi-perspective", "tblbody")],
        [P("D — Single Agent + GraphRAG", "tblbody"), P("1 generic", "tblbody"), P("Yes", "tblbody"),
         P("Yes", "tblbody"), P("No", "tblbody"), P("No", "tblbody"), P("C vs D: GraphRAG + NLI", "tblbody")],
        [P("E — Unmoderated Triad + GraphRAG", "tblbody"), P("3 personas", "tblbody"), P("Yes", "tblbody"),
         P("Yes", "tblbody"), P("No", "tblbody"), P("No", "tblbody"), P("D vs E: physical agent separation", "tblbody")],
        [P("<b>F — Full System</b>", "hl2"),
         P("<b>3 personas</b>", "tblbody"), P("<b>Yes</b>", "tblbody"),
         P("<b>Yes</b>", "tblbody"), P("<b>Yes</b>", "tblbody"), P("<b>Yes</b>", "tblbody"),
         P("<b>E vs F: Moderator + Gate</b>", "tblbody")],
    ]
    story.append(simple_table(ablation_rows, [94, 70, 52, 52, 72, 52, 112]))
    story.append(SP(6))
    story.append(P(
        "<b>Config B aggregation.</b> Majority vote is undefined for free-form roadmaps. "
        "We aggregate by computing cosine similarity among the k=5 roadmap embeddings and selecting "
        "the centroid — the roadmap with highest mean similarity to all others. Ties broken by NLI score."
    ))
    story.append(P(
        "<b>Config C note.</b> We hypothesise that a single decoder over multiple in-context perspectives "
        "produces attention-level averaging of opposing trajectories. This hypothesis is tested by comparing "
        "C against E; we do not claim a mechanistic explanation involving specific attention heads, "
        "as that would require interpretability experiments outside this proposal's scope."
    ))
    story.append(P("<b>Gate-Off variant of F.</b> To isolate the Gate's contribution, "
        "Config F is also evaluated with the Gate disabled, allowing direct A/B comparison of Gate vs. no Gate "
        "while holding all other components constant."
    ))

    story.append(P("<b>5.2 Evaluation metrics.</b>"))
    metric_rows = [
        [P("Metric", "tblhdr"), P("Formula / Definition", "tblhdr"), P("Configs", "tblhdr"), P("Success Criterion", "tblhdr")],
        [P("PCR", "tblbody"), P("Fraction of roadmaps where all 3 persona viewpoints appear at or above similarity threshold τ_pcr", "tblbody"), P("All", "tblbody"), P("≥ 0.75 for F", "tblbody")],
        [P("S-CRR", "tblbody"), P("|{k: Resolved(k,R*) ∨ Exposed(k,T)}| / |K_identified|", "tblbody"), P("All", "tblbody"), P("≥ 0.80 for F", "tblbody")],
        [P("UCR", "tblbody"), P("N_unsupported / N_factual_claims", "tblbody"), P("All", "tblbody"), P("< 0.05 for F", "tblbody")],
        [P("Δ_parity", "tblbody"), P("1 − mean Jaccard(Roles(R*(P_base)), Roles(R*(P_pert)))", "tblbody"), P("A, D, F", "tblbody"), P("≤ 0.05 for F", "tblbody")],
        [P("TOST", "tblbody"), P("Two one-sided t-tests at δ = ±₹15,000/month; clustered SEs by pair", "tblbody"), P("A, D, F", "tblbody"), P("p < 0.05 for F", "tblbody")],
        [P("ΔECRR", "tblbody"), P("Bootcamp recommendation rate(low b_max) − rate(high b_max)", "tblbody"), P("A, D, F", "tblbody"), P("|ΔECRR| ≤ 0.10 for F", "tblbody")],
        [P("ECE", "tblbody"), P("Σ_m (|B_m|/N)|acc(B_m) − conf(B_m)|; correctness = ≥2/3 counsellors agree milestone is appropriate", "tblbody"), P("F only", "tblbody"), P("< 0.10", "tblbody")],
        [P("Counsellor AUC", "tblbody"), P("ROC-AUC of F̂ against counsellor-annotated risk labels", "tblbody"), P("F only", "tblbody"), P("≥ 0.80", "tblbody")],
        [P("Counsellor Likert", "tblbody"), P("5-dimension rubric (Table 3), 1–5 scale", "tblbody"), P("A, D, E, F", "tblbody"), P("≥ 4.0 on each for F", "tblbody")],
    ]
    story.append(simple_table(metric_rows, [62, 170, 52, 100], stripe=False))
    story.append(SP(6))
    story.append(P("<b>PCR computation.</b> Sim(R*, θ_j) is cosine similarity between output roadmap embedding "
        "and a reference embedding constructed from the core claims of persona j. Threshold τ_pcr is set on "
        "a held-out calibration set. If this is implemented as an LLM judge, judge bias will be quantified "
        "against two human raters on a stratified sample."
    ))
    story.append(P("<b>S-CRR computation.</b> Contradictions K_identified are extracted by Φ's contradiction-detection pass. "
        "An LLM judge scores resolution. LLM-judge agreement with two human raters will be reported "
        "(Cohen's κ) before the automated metric is used in final evaluation."
    ))

    story.append(P("<b>5.3 Double-blind counsellor study.</b>"))
    story.append(P(
        "Three certified career counsellors (≥5 years advising experience) assess a stratified random sample "
        "of roadmaps from configurations A, D, E, and F, anonymised and presented without interface branding. "
        "Configuration labels are not disclosed. "
        "<b>Blinding limitation:</b> Config F includes a Dispute Tree interface absent from other configurations. "
        "Evaluators will be informed that some outputs include structured trade-off presentation, "
        "but will not be told which configuration produces it. Full blinding is not achievable."
    ))
    rating_rows = [
        [P("Dimension", "tblhdr"), P("Rubric Prompt", "tblhdr")],
        [P("Prerequisite accuracy", "tblbody"), P("Are all prerequisite orderings correct per standard computing curricula?", "tblbody")],
        [P("Viability under constraints", "tblbody"), P("Is the plan achievable within the stated time and financial constraints?", "tblbody")],
        [P("Risk transparency", "tblbody"), P("Are high-risk milestones clearly labelled as uncertain or contingent?", "tblbody")],
        [P("Trade-off balance", "tblbody"), P("Does the plan acknowledge the candidate's alternative career options?", "tblbody")],
        [P("Agency preservation", "tblbody"), P("Is the candidate given meaningful choice, or is the decision foreclosed by the system?", "tblbody")],
    ]
    story.append(P("<b>Table 3. Counsellor evaluation rubric.</b>", "callout"))
    story.append(simple_table(rating_rows, [130, 374], stripe=False))
    story.append(P("Inter-rater agreement (Krippendorff's α) will be computed across all dimensions. "
        "Counsellors also independently rate each profile as Low / Medium / High pivot-risk; "
        "this forms the ground truth for Counsellor AUC. Ethics: informed consent; no real candidate data.", "callout"))

    story.append(P(
        "<b>5.4 Synthetic candidate dataset.</b> All evaluation uses synthetic profiles only. "
        "Profile design: 10 background archetypes × 5 target roles × 2 counterfactual demographic "
        "perturbations = 100 base profiles per experimental cell. "
        "Each profile is evaluated N_rep=5 times; standard errors clustered at the profile level. "
        "Profiles are generated by a prompted LLM and then reviewed and edited by the research team."
    ))
    story.append(P(
        "<b>5.5 Compute environment.</b> All inference on local hardware (NVIDIA RTX 4090, 24 GB VRAM, "
        "4-bit AWQ quantised local instruction-tuned model, approx. 70–90 tokens/second). "
        "A 2-round debate generates roughly 6,000–8,000 tokens across four agents, taking 70–110 s per scenario. "
        "Local inference is chosen to prevent candidate profile data from being sent to third-party APIs; "
        "it is not claimed to be computationally optimal."
    ))
    story.append(HR())

    # ── 6. Expected Evaluation Plan ──────────────────────────────────────────
    story.append(P("6. Expected Evaluation Plan and Directional Hypotheses", "h1"))
    story.append(warn_box(
        "This section states directional hypotheses, not results. "
        "The system has not been implemented. All claims below are predictions derived from "
        "the cited literature and the mechanism design above."
    ))
    story.append(SP(8))
    story.append(P("<b>6.1 Hypothesised directional outcomes.</b> "
        "Based on the mechanism design and cited literature, we hypothesise:"
    ))
    story.append(P(
        "• Config A (Monolithic Zero-Shot) is expected to show the lowest perspective coverage and highest "
        "unsupported-claim rate, consistent with documented sycophancy and hallucination failures.<br/>"
        "• Config B (Self-Consistency) is expected to marginally outperform A on UCR but not on perspective "
        "coverage, consistent with Smit et al. (2024) finding self-consistency competitive with debate.<br/>"
        "• Config C (Multi-Perspective CoT) is expected to partially improve perspective coverage over A "
        "but to show lower coverage than Config E due to attention-level averaging in a shared context.<br/>"
        "• Config D (Single-Agent GraphRAG) is expected to substantially reduce UCR relative to A–C, "
        "consistent with deterministic graph-based grounding, but not to improve perspective coverage.<br/>"
        "• Config E (Unmoderated Triad) is expected to show high perspective coverage but elevated "
        "unresolved contradictions in the output, consistent with the absence of a synthesis step.<br/>"
        "• Config F (Full System) is expected to improve across all dimensions relative to A–E, "
        "but the magnitude is unknown. Whether F outperforms Config B on UCR is unclear given that "
        "GraphRAG is absent from B — this is a direct test of Smit et al.'s critique.<br/>"
        "• On RQ3 (fairness): masking is expected to reduce Δ_parity relative to A, but not to zero, "
        "because proxy leakage cannot be fully eliminated. Whether Δ_parity falls below 0.05 is empirical."
    ))

    story.append(P("<b>6.2 Illustrative walkthrough (not a measured outcome).</b>"))
    story.append(P(
        "The following illustrates intended system behaviour for a high-friction profile. "
        "This is a constructed example, not evidence of efficacy."
    ))
    walkthrough = [
        P("<b>Profile.</b> Undergraduate student, 3rd year CSE. Verified skills: introductory Python, basic relational databases, front-end scripting. Goal: Staff ML Infrastructure Engineer. Proposed action: 16-week commercial bootcamp at ₹1.2 lakh. Constraints: ₹1.3 lakh savings, four-month timeline.", "callout"),
        SP(4),
        P("<b>π_trad (Stage 2 expected opening):</b> 'The target role requires OS internals, concurrent systems, and distributed consensus — none verified in your current skill set. Prerequisite gap: OS → Distributed Systems → ML Infrastructure is a minimum 12-month path at full-time study. [Cite: G/node/OS-Concurrency, G/node/DistSys-Consensus]'", "callout"),
        P("<b>π_builder:</b> 'The infrastructure target is wrong for your timeline. Your Python and web-dev skills map onto Applied AI Application Engineering — RAG pipelines, agent deployment, SaaS wrapping — achievable in four months without the bootcamp cost. [Cite: D_rag/chunk/applied-ai-roadmap-22]'", "callout"),
        P("<b>π_spec:</b> 'Infrastructure roles require low-level memory management and network stack understanding. Bootcamps teach API abstraction. The technical screening gap will be decisive. [Cite: G/node/OS-MemoryMgmt]'", "callout"),
        SP(4),
        P("<b>Stage 3 Moderator probe:</b> 'Traditionalist and Specialist both reject the bootcamp, for different reasons — prerequisite sequencing vs. screening depth. Builder proposes a lateral pivot. Builder and Specialist: what is the minimum viable 6-month programme using open resources?'", "callout"),
        SP(4),
        P("<b>Expected Gate behaviour:</b> High inter-agent divergence (Ĥ near 1.0), multiple missing prerequisite hops in G, NLI failure on bootcamp placement claims → F̂ expected to exceed θ_unc=0.65. Gate fires. Dispute Tree presented; candidate chooses between Branch 1 (Systems Foundations) and Branch 2 (Applied AI Pivot). The system does not choose.", "callout"),
    ]
    story.append(box(walkthrough, bg=BG, border=BORDER, pad=10))
    story.append(SP(6))

    story.append(P("<b>6.3 Anticipated threats to validity.</b>"))
    story.append(P(
        "(1) <b>Synthetic-only evaluation.</b> No real users are tested; synthetic profiles may not capture "
        "real linguistic diversity. Results may not generalise to real candidates.<br/>"
        "(2) <b>LLM-judge risk.</b> PCR, S-CRR, and ECE require automated evaluation. LLM judges have known "
        "positivity bias; agreement with human raters must be reported before automated scores are interpreted.<br/>"
        "(3) <b>Shared base-model priors.</b> All three personas and Φ share a base model. Correlated errors "
        "may prevent the debate from surfacing failure modes that are systematic across all model instances.<br/>"
        "(4) <b>US-centric wage data.</b> BLS OEWS covers US occupations only. Indian deployments require regional data.<br/>"
        "(5) <b>Graph coverage gaps.</b> Emerging roles (ML Ops Engineer, AI Safety Researcher) may not be "
        "fully represented in the CS2023-derived DAG.<br/>"
        "(6) <b>Wage staleness.</b> BLS OEWS is an annual release with an 18-month publication lag; "
        "fast-moving AI markets may deviate substantially.<br/>"
        "(7) <b>No longitudinal outcome validation.</b> Whether candidates who used the system made better "
        "career decisions requires a longitudinal study with real users, outside this proposal's scope.<br/>"
        "(8) <b>Cognitive forcing equity concern.</b> Buçinca et al. (2021) found the forcing interface was "
        "less effective and more frustrating for users low in need-for-cognition — a demographic that may "
        "correlate with socioeconomic disadvantage. This is an unresolved design tension."
    ))
    story.append(HR())

    # ── 7. References ────────────────────────────────────────────────────────
    story.append(P("7. References", "h1"))
    refs = [
        "ACM/IEEE-CS/AAAI Joint Task Force on Computing Curricula. (2023). <i>Computer Science Curricula 2023 (CS2023)</i>. ACM & IEEE Computer Society. https://doi.org/10.1145/3664191",
        "Bolukbasi, T., Chang, K.-W., Zou, J. Y., Saligrama, V., & Kalai, A. T. (2016). Man is to computer programmer as woman is to homemaker? Debiasing word embeddings. <i>NeurIPS, 29</i>, 4349–4357. https://arxiv.org/abs/1607.06520",
        "Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To trust or to think: Cognitive forcing functions can reduce overreliance on AI in AI-assisted decision-making. <i>PACMHCI, 5</i>(CSCW1), Art. 188. https://doi.org/10.1145/3449287",
        "Caliskan, A., Bryson, J. J., & Narayanan, A. (2017). Semantics derived automatically from language corpora contain human-like biases. <i>Science, 356</i>(6334), 183–186. https://doi.org/10.1126/science.aal4230",
        "Cummings, M. L. (2004). Automation bias in intelligent time critical decision support systems. <i>AIAA 1st Intelligent Systems Technical Conference</i>. https://doi.org/10.2514/6.2004-6313",
        "Du, Y., Li, S., Torralba, A., Tenenbaum, J. B., & Mordatch, I. (2024). Improving factuality and reasoning in language models through multiagent debate. <i>ICML 2024</i>. https://arxiv.org/abs/2305.14325",
        "Edge, D., Trinh, H., Cheng, N., Bradley, J., Chao, A., Mody, A., Truitt, S., & Larson, J. (2024). From local to global: A graph RAG approach to query-focused summarization. <i>Microsoft Research Technical Report</i>. https://arxiv.org/abs/2404.16130",
        "Geyik, S. C., Ambler, S., & Kenthapadi, K. (2019). Fairness-aware ranking in search & recommendation systems with application to LinkedIn Talent Search. <i>ACM KDD 2019</i>, 2221–2231. https://doi.org/10.1145/3292500.3330691",
        "Irving, G., Christiano, P., & Amodei, D. (2018). AI safety via debate. <i>arXiv:1805.00899</i>.",
        "Kadavath, S., Conerly, T., Askell, A., Henighan, T., Drain, D., Perez, E., Schiefer, N., et al. (2022). Language models (mostly) know what they know. <i>arXiv:2207.05221</i>.",
        "Liang, T., He, Z., Jiao, W., Wang, X., Wang, Y., Wang, R., Yang, Y., Tu, Z., & Shi, S. (2023). Encouraging divergent thinking in large language models via multi-agent debate. <i>EMNLP 2023</i>, 4392–4407. https://arxiv.org/abs/2305.19118",
        "Parasuraman, R., & Riley, V. (1997). Humans and automation: Use, misuse, disuse, abuse. <i>Human Factors, 39</i>(2), 230–253. https://doi.org/10.1518/001872097778543886",
        "Perez, E., Ringer, S., Lukošiūtė, K., Nguyen, K., Chen, E., Heiner, S., Pettit, C., et al. (2022). Discovering language model behaviors with model-written evaluations. <i>Findings of ACL 2023</i>, 13387–13434. https://arxiv.org/abs/2212.09251",
        "Sharma, M., Tong, M., Korbak, T., Duvenaud, D., Askell, A., Bowman, S. R., Cheng, N., et al. (2024). Towards understanding sycophancy in language models. <i>ICLR 2024</i>. https://arxiv.org/abs/2310.13548",
        "Smit, A., Garg, S., Foley, M., du Plessis, M. C., Bhattacharyya, A., & Garg, A. (2024). Should we be going MAD? A look at multi-agent debate strategies for LLMs. <i>arXiv:2311.17371</i>.",
        "U.S. Bureau of Labor Statistics. (2023). <i>Occupational Employment and Wage Statistics (OEWS): Computer and Information Technology Occupations (SOC 15-0000)</i>. U.S. Department of Labor. Retrieved November 2023 from https://www.bls.gov/oes/current/oes_nat.htm",
        "Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q., & Zhou, D. (2022). Chain-of-thought prompting elicits reasoning in large language models. <i>NeurIPS 35</i>. https://arxiv.org/abs/2201.11903",
        "Xiong, M., Hu, Z., Lu, X., Li, Y., Fu, J., He, J., & Hooi, B. (2024). Can LLMs express their uncertainty? An empirical evaluation of confidence elicitation in LLMs. <i>ICLR 2024</i>. https://arxiv.org/abs/2306.13063",
    ]
    for i, r in enumerate(refs, 1):
        story.append(P(f"{i}. {r}", "ref"))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF written to: {pdf_path}")


if __name__ == "__main__":
    build("/home/thor/Desktop/RAI Project/docs/ACADEMIC_RESEARCH_PAPER.pdf")
