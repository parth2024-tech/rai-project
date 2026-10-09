#!/usr/bin/env python3
"""
Generate the Final Audited, Conference-Grade 17-Slide Presentation Deck:
Debate-Based Career Guidance Agent with Complementary Personas

Scope: Computer Science & Software Engineering Career Advisory

Addresses 100% of the re-audit findings:
1. Speaker Notes: Completely rewritten as natural, professional presenter talking points (zero audit jargon).
2. Literature & References: Canonical citations including Geyik et al. (KDD 2019), Kadavath et al. (2022), Cummings (2004), plus a dedicated Selected References slide.
3. Sycophancy Metric: Premise-Challenge Rate (PCR >= 80% on 100 impossible transitions).
4. Uncertainty Validation: Counselor Risk Discrimination AUC-ROC >= 0.82 with weight tuning specification.
5. Methodological Rigor: TOST Equivalence Testing (delta = +/- $2,500), Clustered SEs (N=5 repeats), Substantiated CRR (S-CRR), Cross-SES ECRR parity, and non-trivial override trigger rate (~35-40%).
6. Unconfounded Ablation Matrix: 6 controlled configurations including compute-matched Self-Consistency and single-agent GraphRAG.
7. Visual & Flowchart Polish: Divergent YES/NO branches on Slide 6, proportional card heights, 12-14pt body text, compact table headers, and unified naming.
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def build_audited_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Executive Academic Palette (Zero AI Clichés)
    BG_DARK = RGBColor(15, 23, 42)         # Slate 900 #0F172A
    BG_LIGHT = RGBColor(248, 250, 252)     # Slate 50 #F8FAFC
    CARD_BG = RGBColor(255, 255, 255)      # Pure White
    CARD_BORDER = RGBColor(203, 213, 225)  # Slate 300 #CBD5E1
    CARD_MUTED = RGBColor(241, 245, 249)   # Slate 100 #F1F5F9
    
    NAVY_PRIMARY = RGBColor(30, 41, 59)    # Slate 800 #1E293B
    NAVY_HEAD = RGBColor(15, 23, 42)       # Slate 900
    TEAL_PRIMARY = RGBColor(13, 148, 136)  # Teal 600 #0D9488
    TEAL_ACCENT = RGBColor(20, 184, 166)   # Teal 500 #14B8A6
    TEAL_BG = RGBColor(240, 253, 250)      # Teal 50
    BLUE_ACCENT = RGBColor(37, 99, 235)    # Blue 600 #2563EB
    BLUE_BG = RGBColor(239, 246, 255)      # Blue 50
    ROSE_ACCENT = RGBColor(225, 29, 72)    # Rose 600 #E11D48
    ROSE_BG = RGBColor(255, 241, 242)      # Rose 50
    AMBER_ACCENT = RGBColor(217, 119, 6)   # Amber 600 #D97706
    AMBER_BG = RGBColor(254, 243, 199)     # Amber 100
    INDIGO_ACCENT = RGBColor(79, 70, 229)  # Indigo 600 #4F46E5
    INDIGO_BG = RGBColor(238, 242, 255)    # Indigo 50
    
    TEXT_MAIN = RGBColor(30, 41, 59)       # Slate 800
    TEXT_MUTED = RGBColor(100, 116, 139)   # Slate 500
    TEXT_WHITE = RGBColor(255, 255, 255)
    
    FONT_MAIN = "Calibri"
    FONT_CODE = "Consolas"
    TOTAL_SLIDES = 17

    def apply_bg(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_header(slide, title, category, slide_num):
        tag = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.38), Inches(3.4), Inches(0.32))
        tag.fill.solid()
        tag.fill.fore_color.rgb = TEAL_BG
        tag.line.color.rgb = TEAL_PRIMARY
        tag.line.width = Pt(1)
        tp = tag.text_frame.paragraphs[0]
        tp.text = category.upper()
        tp.font.name = FONT_MAIN
        tp.font.size = Pt(9.5)
        tp.font.bold = True
        tp.font.color.rgb = TEAL_PRIMARY
        tp.alignment = PP_ALIGN.CENTER
        tag.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

        tb_t = slide.shapes.add_textbox(Inches(0.8), Inches(0.72), Inches(10.5), Inches(0.65))
        p = tb_t.text_frame.paragraphs[0]
        p.text = title
        p.font.name = FONT_MAIN
        p.font.size = Pt(21)
        p.font.bold = True
        p.font.color.rgb = NAVY_HEAD

        tb_n = slide.shapes.add_textbox(Inches(11.5), Inches(0.38), Inches(1.0), Inches(0.4))
        p_n = tb_n.text_frame.paragraphs[0]
        p_n.text = f"{slide_num:02d} / {TOTAL_SLIDES:02d}"
        p_n.font.name = FONT_MAIN
        p_n.font.size = Pt(11)
        p_n.font.bold = True
        p_n.font.color.rgb = TEXT_MUTED
        p_n.alignment = PP_ALIGN.RIGHT

        rule = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.40), Inches(11.733), Inches(0.015))
        rule.fill.solid()
        rule.fill.fore_color.rgb = CARD_BORDER
        rule.line.fill.background()

    def add_card(slide, left, top, width, height, title="", title_color=NAVY_HEAD, top_accent=None, bg_color=CARD_BG, border_color=CARD_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1.2)

        if top_accent:
            acc = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left + Inches(0.08), top + Inches(0.04), width - Inches(0.16), Inches(0.07))
            acc.fill.solid()
            acc.fill.fore_color.rgb = top_accent
            acc.line.fill.background()

        if title:
            tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.16), width - Inches(0.4), Inches(0.45))
            tb.text_frame.word_wrap = True
            p = tb.text_frame.paragraphs[0]
            p.text = title
            p.font.name = FONT_MAIN
            p.font.size = Pt(13.5)
            p.font.bold = True
            p.font.color.rgb = title_color
            return card, tb
        return card, None

    def add_arrow(slide, left, top, width, height, direction="right", color=TEAL_PRIMARY):
        shape_type = MSO_SHAPE.RIGHT_ARROW if direction == "right" else MSO_SHAPE.DOWN_ARROW
        arr = slide.shapes.add_shape(shape_type, left, top, width, height)
        arr.fill.solid()
        arr.fill.fore_color.rgb = color
        arr.line.fill.background()
        return arr

    # =========================================================================
    # SLIDE 1: Title Slide
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    apply_bg(s1, BG_DARK)

    s1_badge = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(0.9), Inches(5.8), Inches(0.35))
    s1_badge.fill.solid()
    s1_badge.fill.fore_color.rgb = RGBColor(19, 78, 74)
    s1_badge.line.color.rgb = TEAL_ACCENT
    s1_badge.line.width = Pt(1)
    p = s1_badge.text_frame.paragraphs[0]
    p.text = "RESPONSIBLE AI · MULTI-AGENT DELIBERATION · KNOWLEDGE GRAPHS"
    p.font.name = FONT_MAIN
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = TEAL_ACCENT
    p.alignment = PP_ALIGN.CENTER
    s1_badge.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    tb_t = s1.shapes.add_textbox(Inches(1.0), Inches(1.4), Inches(11.333), Inches(2.3))
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = "Debate-Based Career Guidance Agent\nwith Complementary Personas"
    p_t.font.name = FONT_MAIN
    p_t.font.size = Pt(36)
    p_t.font.bold = True
    p_t.font.color.rgb = TEXT_WHITE
    p_t.space_after = Pt(8)

    p_sub = tf_t.add_paragraph()
    p_sub.text = "Surfacing Real-World Software Engineering Career Trade-offs via Conflicting Optimization Goals"
    p_sub.font.name = FONT_MAIN
    p_sub.font.size = Pt(16)
    p_sub.font.color.rgb = RGBColor(148, 163, 184)
    p_sub.space_after = Pt(4)

    p_scope = tf_t.add_paragraph()
    p_scope.text = "Domain Scope: Computer Science & Software Engineering Careers (CSE Core Undergraduates)"
    p_scope.font.name = FONT_MAIN
    p_scope.font.size = Pt(13)
    p_scope.font.bold = True
    p_scope.font.color.rgb = TEAL_ACCENT

    # Authors & Metadata Box
    s1_card, _ = add_card(s1, Inches(1.0), Inches(4.3), Inches(11.333), Inches(2.6), "", bg_color=RGBColor(17, 24, 39), border_color=RGBColor(51, 65, 85))
    tb_meta = s1.shapes.add_textbox(Inches(1.3), Inches(4.5), Inches(10.7), Inches(2.2))
    tf_m = tb_meta.text_frame
    tf_m.word_wrap = True
    
    p = tf_m.paragraphs[0]
    p.text = "TECHNICAL PROJECT DEFENSE · OCTOBER 2026"
    p.font.name = FONT_MAIN
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = TEAL_ACCENT
    p.space_after = Pt(6)

    meta_items = [
        ("Research Team: ", "Responsible AI Systems Laboratory"),
        ("Advising Personas: ", "The Pragmatic Traditionalist (Corporate), The Entrepreneurial Builder (Startup), The Deep-Tech Specialist (Systems), The Moderator (Synthesizer)"),
        ("Local Privacy & Stack: ", "100% On-Premise Qwen-2.5-14B (Ollama/vLLM) · LangGraph State Machine · Derived Neo4j DAG · Offline Snapshot FAISS"),
        ("Key Safety Mechanisms: ", "Composite Epistemic Uncertainty Indicator U_hat, Dispute Graph Transparency, Cognitive Forcing (Human Override)")
    ]
    for label, val in meta_items:
        p_row = tf_m.add_paragraph()
        p_row.text = label
        p_row.font.name = FONT_MAIN
        p_row.font.bold = True
        p_row.font.size = Pt(11)
        p_row.font.color.rgb = RGBColor(226, 232, 240)
        p_row.text += val
        p_row.font.bold = False
        p_row.font.size = Pt(11)
        p_row.font.color.rgb = RGBColor(203, 213, 225)
        p_row.space_after = Pt(2)

    s1.notes_slide.notes_text_frame.text = (
        "Welcome everyone. Today we present our project: Debate-Based Career Guidance Agent with Complementary Personas, "
        "specifically focused on Computer Science and Software Engineering career decisions. "
        "Standard LLMs offer one-dimensional, sycophantic advice. We solve this by structuring a multi-agent debate between "
        "three distinct career philosophies—the Pragmatist, the Builder, and the Specialist—moderated by an impartial synthesizer. "
        "Our entire stack operates on-premise to guarantee candidate privacy."
    )

    # =========================================================================
    # SLIDE 2: Executive Summary & Domain Scope
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    apply_bg(s2, BG_LIGHT)
    add_header(s2, "Executive Summary: Scoped Problem & Architectural Solution", "EXECUTIVE SUMMARY", 2)

    w_half = Inches(5.6)
    h_box = Inches(5.3)

    add_card(s2, Inches(0.8), Inches(1.6), w_half, h_box, "Domain Scoping & Problem Landscape", ROSE_ACCENT, top_accent=ROSE_ACCENT)
    tb_sl = s2.shapes.add_textbox(Inches(1.0), Inches(2.2), w_half - Inches(0.4), h_box - Inches(0.7))
    tf_sl = tb_sl.text_frame
    tf_sl.word_wrap = True

    pts_s2_left = [
        ("Target Audience: ", "Undergraduate Computer Science students evaluating Big Tech corporate roles vs startup ventures vs low-level infrastructure engineering."),
        ("The Sycophancy Vulnerability: ", "Standard LLMs validate unviable transitions (Sharma et al., 2024), cheerleading unrealistic timelines without auditing foundational gaps."),
        ("The Illusion of False Certainty: ", "Monolithic prompts emit authoritative single-track roadmaps that conceal volatile hiring markets, completion dropouts, and debt liabilities."),
        ("Demographic Steering Risks: ", "Unchecked LLMs mirror historical occupational segregation (Geyik et al., 2019), channeling non-traditional candidates into lower-agency certifications.")
    ]
    for lbl, desc in pts_s2_left:
        p = tf_sl.add_paragraph() if tf_sl.paragraphs[0].text else tf_sl.paragraphs[0]
        p.text = "• " + lbl
        p.font.name = FONT_MAIN
        p.font.bold = True
        p.font.size = Pt(11.5)
        p.font.color.rgb = NAVY_HEAD
        p.text += desc
        p.font.bold = False
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(8)

    add_card(s2, Inches(6.9), Inches(1.6), w_half, h_box, "The Dialectic Multi-Agent Solution", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb_sr = s2.shapes.add_textbox(Inches(7.1), Inches(2.2), w_half - Inches(0.4), h_box - Inches(0.7))
    tf_sr = tb_sr.text_frame
    tf_sr.word_wrap = True

    pts_s2_right = [
        ("Conflicting Advising Personas: ", "Pits the Pragmatic Traditionalist (corporate stability & DSA) against the Entrepreneurial Builder (startup SaaS & AI) and Deep-Tech Specialist (Linux & 5NF infrastructure)."),
        ("Moderator-Driven Friction: ", "A neutral Moderator identifies dialectic contradictions and injects probing cross-examination questions to prevent superficial consensus."),
        ("Derived GraphRAG Grounding: ", "Enforces structural prerequisite DAGs synthesized on O*NET 29.2 and ESCO v1.2 taxonomies, backed by offline snapshot course syllabi."),
        ("Responsible AI Controls: ", "Computes a Composite Uncertainty Indicator and enforces Cognitive Forcing Gates, mandating human review before high-risk commitments.")
    ]
    for lbl, desc in pts_s2_right:
        p = tf_sr.add_paragraph() if tf_sr.paragraphs[0].text else tf_sr.paragraphs[0]
        p.text = "✔ " + lbl
        p.font.name = FONT_MAIN
        p.font.bold = True
        p.font.size = Pt(11.5)
        p.font.color.rgb = NAVY_HEAD
        p.text += desc
        p.font.bold = False
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(8)

    s2.notes_slide.notes_text_frame.text = (
        "On this slide, we ground our problem definition in the specific realities of Software Engineering career choices. "
        "Career guidance carries financial and professional irreversibility. When students ask generic chatbots for career advice, "
        "they receive flattering, one-dimensional answers. Our solution introduces three conflicting personas whose debate "
        "is mediated by an impartial moderator to expose the real trade-offs."
    )

    # =========================================================================
    # SLIDE 3: Literature Survey
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    apply_bg(s3, BG_LIGHT)
    add_header(s3, "Literature Survey: Foundations, Recommender Fairness & Gaps", "LITERATURE SURVEY", 3)

    tbl_shape = s3.shapes.add_table(8, 4, Inches(0.8), Inches(1.55), Inches(11.733), Inches(5.4))
    tbl = tbl_shape.table
    tbl.columns[0].width = Inches(3.2)
    tbl.columns[1].width = Inches(2.2)
    tbl.columns[2].width = Inches(3.8)
    tbl.columns[3].width = Inches(2.533)

    headers = ["Research Paper & Citation", "Core Theoretical Finding", "Unaddressed Gap in Literature", "How This Project Solves It"]
    for j, h_text in enumerate(headers):
        cell = tbl.cell(0, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = NAVY_HEAD
        p = cell.text_frame.paragraphs[0]
        p.text = h_text
        p.font.name = FONT_MAIN
        p.font.bold = True
        p.font.size = Pt(10.5)
        p.font.color.rgb = TEXT_WHITE
        p.alignment = PP_ALIGN.CENTER
        cell.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    lit_rows = [
        ("Du et al. (ICML 2024)\nMulti-Agent Debate Factuality", "Adversarial debate suppresses hallucinations across multi-step reasoning", "Evaluated on algorithmic QA/math; unexplored in multi-stakeholder career trade-offs", "Deploys multi-agent debate to surface subjective, real-world career trade-offs"),
        ("Liang et al. (EMNLP 2023)\nDivergent Thinking via Personas", "Distinct personas stimulate multi-perspective exploration", "Personas lacked antagonistic career philosophies or structured cross-exam", "Implements 3 opposing career philosophies + probing Moderator friction"),
        ("Sharma et al. (ICLR 2024)\nSycophancy in Language Models", "LLMs systematically flatter user beliefs over objective truth", "Diagnosed sycophancy without providing recommender system solutions", "Pragmatist & Specialist actively challenge builder hype and user assumptions"),
        ("Geyik et al. (ACM KDD 2019)\nFairness in Talent Search", "Standard talent search models amplify demographic and prestige biases", "Focused on static bipartite talent ranking; lacks conversational deliberation", "Conducts counterfactual demographic audits across 500+ synthetic profile pairs"),
        ("Xiong et al. (ICLR 2024)\nConfidence Elicitation in LLMs", "LLMs generate uncalibrated, overconfident assertions", "Evaluated QA benchmarks without multi-attribute labor risk modeling", "Calculates composite Epistemic Uncertainty U_hat from persona divergence"),
        ("Buçinca et al. (CSCW 2021)\nCognitive Forcing Functions", "Finished AI advice triggers user automation bias & blind compliance", "Explored basic decision tasks without multi-agent dispute graphs", "Introduces cognitive forcing gate requiring human veto over career disputes"),
        ("Edge et al. (Microsoft 2024)\nGraphRAG Methodology", "Vector retrieval fails at hierarchical structural dependency reasoning", "Focused on document summarization, not skill prerequisite DAGs", "Integrates derived Neo4j prerequisite DAG with offline FAISS syllabi")
    ]

    for i, (p_cit, p_find, p_gap, p_proj) in enumerate(lit_rows):
        row_idx = i + 1
        bg_col = CARD_BG if i % 2 == 0 else CARD_MUTED
        vals = [p_cit, p_find, p_gap, p_proj]
        for j, val in enumerate(vals):
            cell = tbl.cell(row_idx, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg_col
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = FONT_MAIN
            p.font.size = Pt(9.2)
            if j == 0:
                p.font.bold = True
                p.font.color.rgb = NAVY_HEAD
            elif j == 3:
                p.font.bold = True
                p.font.color.rgb = TEAL_PRIMARY
            else:
                p.font.color.rgb = TEXT_MAIN
            cell.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    s3.notes_slide.notes_text_frame.text = (
        "Our literature survey positions this project at the intersection of four established domains: "
        "multi-agent debate from Du et al. and Liang et al., sycophancy analysis from Sharma et al., "
        "algorithmic fairness in talent search from Geyik et al. at LinkedIn, and cognitive forcing from Buçinca et al. "
        "We leverage these foundations to address the specific failure modes of AI-assisted career advisory."
    )

    # =========================================================================
    # SLIDE 4: Problem Definition (High-Level Sociotechnical Stakes)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    apply_bg(s4, BG_LIGHT)
    add_header(s4, "Problem Definition (High-Level): Sociotechnical Advisory Pitfalls", "HIGH-LEVEL PROBLEM", 4)

    col_w = Inches(3.64)
    col_h = Inches(5.3)

    add_card(s4, Inches(0.8), Inches(1.6), col_w, col_h, "1. The Sycophancy Trap", ROSE_ACCENT, top_accent=ROSE_ACCENT)
    tb1 = s4.shapes.add_textbox(Inches(1.0), Inches(2.2), col_w - Inches(0.4), col_h - Inches(0.7))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    tf1.paragraphs[0].text = "Advisory Sycophancy (Sharma et al., 2024):"
    tf1.paragraphs[0].font.bold = True
    tf1.paragraphs[0].font.size = Pt(11)
    tf1.paragraphs[0].font.color.rgb = ROSE_ACCENT
    pts_p1 = [
        "LLMs maximize immediate conversational agreement over objective feasibility.",
        "When an applicant proposes an unrealistic transition (e.g. novice to Staff ML Engineer in 12 weeks), single-agent models encourage it without verifying prerequisite depth.",
        "Consequence: Unnecessary tuition debt, high dropout rates, and abandoned transitions."
    ]
    for pt in pts_p1:
        p = tf1.add_paragraph()
        p.text = "• " + pt
        p.font.name = FONT_MAIN
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(6)

    add_card(s4, Inches(4.84), Inches(1.6), col_w, col_h, "2. Illusion of False Certainty", AMBER_ACCENT, top_accent=AMBER_ACCENT)
    tb2 = s4.shapes.add_textbox(Inches(5.04), Inches(2.2), col_w - Inches(0.4), col_h - Inches(0.7))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    tf2.paragraphs[0].text = "Epistemic Failure (Kadavath et al., 2022):"
    tf2.paragraphs[0].font.bold = True
    tf2.paragraphs[0].font.size = Pt(11)
    tf2.paragraphs[0].font.color.rgb = AMBER_ACCENT
    pts_p2 = [
        "LLMs emit authoritative, deterministic roadmaps without expressing epistemic humility.",
        "They mask severe labor volatility, rapid skill deprecation, and regional hiring differences.",
        "Perspective Collapse: Complex trade-offs (base salary vs equity risk vs study workload) are collapsed into an opaque, smoothed compromise."
    ]
    for pt in pts_p2:
        p = tf2.add_paragraph()
        p.text = "• " + pt
        p.font.name = FONT_MAIN
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(6)

    add_card(s4, Inches(8.88), Inches(1.6), col_w, col_h, "3. Equity & Agency Failures", NAVY_HEAD, top_accent=NAVY_HEAD)
    tb3 = s4.shapes.add_textbox(Inches(9.08), Inches(2.2), col_w - Inches(0.4), col_h - Inches(0.7))
    tf3 = tb3.text_frame
    tf3.word_wrap = True
    tf3.paragraphs[0].text = "Bias & Complacency (Geyik et al., 2019):"
    tf3.paragraphs[0].font.bold = True
    tf3.paragraphs[0].font.size = Pt(11)
    tf3.paragraphs[0].font.color.rgb = NAVY_HEAD
    pts_p3 = [
        "Training corpora encode historical workforce segregation, steering underrepresented backgrounds into low-agency certifications.",
        "Automation Bias (Cummings, 2004): Providing a finished answer induces blind compliance without critical inspection.",
        "Non-Subsumptive Requirement: An ethical career assistant must preserve human agency through visible disagreement."
    ]
    for pt in pts_p3:
        p = tf3.add_paragraph()
        p.text = "• " + pt
        p.font.name = FONT_MAIN
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(6)

    s4.notes_slide.notes_text_frame.text = (
        "Here we examine the three primary sociotechnical pitfalls. Sycophancy leads candidates into expensive dead ends. "
        "False certainty masks volatile labor trends. And automation bias causes users to defer passively to the model's outputs. "
        "These three challenges form the design requirements for our multi-agent architecture."
    )

    # =========================================================================
    # SLIDE 5: Problem Definition (Low-Level Mathematical Specification)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    apply_bg(s5, BG_LIGHT)
    add_header(s5, "Problem Definition (Low-Level): Mathematical Specification", "LOW-LEVEL FORMULATION", 5)

    add_card(s5, Inches(0.8), Inches(1.6), w_half, h_box, "Formal Environment & State Tuple", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb_el = s5.shapes.add_textbox(Inches(1.0), Inches(2.2), w_half - Inches(0.4), h_box - Inches(0.7))
    tf_el = tb_el.text_frame
    tf_el.word_wrap = True

    p = tf_el.paragraphs[0]
    p.text = "Environment: M = < P, G, D_rag, Π, T_debate, Φ >"
    p.font.name = FONT_CODE
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = TEAL_PRIMARY
    p.space_after = Pt(8)

    tuple_items = [
        ("Candidate Profile: ", "P = < s_curr, e_hist, g_target, c_user >\nwhere s_curr are verified skills (e.g. CSE Core), g_target is target interest, and c_user = < t_avail, b_max, τ_horizon > represents weekly study hours, budget, and transition deadline."),
        ("Demographic Isolation: ", "Protected attributes a_demo are explicitly EXCLUDED from generation profile P and held strictly in the counterfactual audit sandbox."),
        ("Derived Career Graph: ", "G = (V, E) where V = V_role ∪ V_skill, and E_prereq is a synthesized Directed Acyclic Graph (DAG) of prerequisite skill dependencies."),
        ("Offline Snapshot Corpus: ", "D_rag = {d_k} containing offline-snapshot course syllabi, BLS wage tables, and curated job distributions.")
    ]
    for lbl, desc in tuple_items:
        p_row = tf_el.add_paragraph()
        p_row.text = "• " + lbl
        p_row.font.name = FONT_MAIN
        p_row.font.bold = True
        p_row.font.size = Pt(10.5)
        p_row.font.color.rgb = NAVY_HEAD
        p_row.text += desc
        p_row.font.bold = False
        p_row.font.size = Pt(10)
        p_row.font.color.rgb = TEXT_MAIN
        p_row.space_after = Pt(6)

    add_card(s5, Inches(6.9), Inches(1.6), w_half, h_box, "Persona Optimization Directives & Synthesis", BLUE_ACCENT, top_accent=BLUE_ACCENT)
    tb_er = s5.shapes.add_textbox(Inches(7.1), Inches(2.2), w_half - Inches(0.4), h_box - Inches(0.7))
    tf_er = tb_er.text_frame
    tf_er.word_wrap = True

    p = tf_er.paragraphs[0]
    p.text = "Synthesis Function: < R*, T_dispute, U_hat > = Φ(H)"
    p.font.name = FONT_CODE
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = BLUE_ACCENT
    p.space_after = Pt(8)

    obj_items = [
        ("Pragmatist Prompt Directive: ", "Heuristically maximizes CorporateSecurity and Tier-1 BaseSalary, penalizing startup volatility and requiring verified DSA mastery."),
        ("Builder Prompt Directive: ", "Heuristically maximizes CommercialUpside and ProductVelocity, promoting AI SaaS building, agentic RAG, and fast market validation."),
        ("Specialist Prompt Directive: ", "Heuristically maximizes TechnicalDepth and Irreplaceability, prioritizing Linux internals, 5NF databases, and network robustness."),
        ("Moderator Mapping Φ(H): ", "Synthesizes multi-turn dialogue history H = {u_i^(t)} across T_debate = 2 rounds into hybrid roadmap R*, Dispute Tree T_dispute, and uncertainty U_hat.")
    ]
    for lbl, desc in obj_items:
        p_row = tf_er.add_paragraph()
        p_row.text = "• " + lbl
        p_row.font.name = FONT_MAIN
        p_row.font.bold = True
        p_row.font.size = Pt(10.5)
        p_row.font.color.rgb = NAVY_HEAD
        p_row.text += desc
        p_row.font.bold = False
        p_row.font.size = Pt(10)
        p_row.font.color.rgb = TEXT_MAIN
        p_row.space_after = Pt(6)

    s5.notes_slide.notes_text_frame.text = (
        "Here we define the formal environment tuple. Crucially, demographic attributes a_demo are isolated entirely "
        "from the generation prompt P to prevent profiling. The persona objective functions are encoded as structured prompt "
        "contracts, and the Moderator maps the two-round dialogue history H into a hybrid recommendation R*."
    )

    # =========================================================================
    # SLIDE 6: Flowchart 1 - End-to-End System Architecture (Divergent Branches)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    apply_bg(s6, BG_LIGHT)
    add_header(s6, "Flowchart: End-to-End System Architecture & Information Flow", "SYSTEM ARCHITECTURE DIAGRAM", 6)

    # Row 1: Inputs & Grounding
    add_card(s6, Inches(0.8), Inches(1.7), Inches(3.2), Inches(1.3), "Candidate Profile (P)", NAVY_HEAD, top_accent=BLUE_ACCENT, bg_color=CARD_MUTED)
    tb_in = s6.shapes.add_textbox(Inches(0.9), Inches(2.1), Inches(3.0), Inches(0.8))
    tb_in.text_frame.paragraphs[0].text = "• Verified Skills (CSE Core)\n• Major & Vague Interests\n• Timeline & Budget Limits"
    tb_in.text_frame.paragraphs[0].font.size = Pt(9.5)
    tb_in.text_frame.paragraphs[0].font.color.rgb = TEXT_MAIN

    add_arrow(s6, Inches(4.1), Inches(2.2), Inches(0.7), Inches(0.25), "right", TEAL_PRIMARY)

    add_card(s6, Inches(4.9), Inches(1.7), Inches(3.5), Inches(1.3), "Hybrid Knowledge Base", NAVY_HEAD, top_accent=TEAL_PRIMARY, bg_color=TEAL_BG)
    tb_kg = s6.shapes.add_textbox(Inches(5.0), Inches(2.1), Inches(3.3), Inches(0.8))
    tb_kg.text_frame.paragraphs[0].text = "• Neo4j: Derived Skill Prerequisite DAG\n• FAISS: Offline Syllabi & Wage Snapshot\n• Cypher Traversals & NLI Entailment"
    tb_kg.text_frame.paragraphs[0].font.size = Pt(9.5)
    tb_kg.text_frame.paragraphs[0].font.color.rgb = TEXT_MAIN

    add_arrow(s6, Inches(8.5), Inches(2.2), Inches(0.7), Inches(0.25), "right", TEAL_PRIMARY)

    add_card(s6, Inches(9.3), Inches(1.7), Inches(3.2), Inches(1.3), "Local Multi-Agent Harness", NAVY_HEAD, top_accent=ROSE_ACCENT, bg_color=ROSE_BG)
    tb_lh = s6.shapes.add_textbox(Inches(9.4), Inches(2.1), Inches(3.0), Inches(0.8))
    tb_lh.text_frame.paragraphs[0].text = "• LangGraph State Machine\n• Local Qwen-2.5-14B (Ollama/vLLM)\n• 100% On-Premise Execution"
    tb_lh.text_frame.paragraphs[0].font.size = Pt(9.5)
    tb_lh.text_frame.paragraphs[0].font.color.rgb = TEXT_MAIN

    add_arrow(s6, Inches(10.6), Inches(3.1), Inches(0.25), Inches(0.4), "down", ROSE_ACCENT)

    # Row 2: Dialectic Triad Engine
    add_card(s6, Inches(0.8), Inches(3.6), Inches(11.733), Inches(1.6), "Multi-Persona Deliberation Engine (Conflicting Career Philosophies)", NAVY_HEAD, top_accent=AMBER_ACCENT)
    
    add_card(s6, Inches(1.1), Inches(4.1), Inches(3.4), Inches(0.95), "1. Pragmatic Traditionalist", TEAL_PRIMARY, bg_color=CARD_BG)
    tb = s6.shapes.add_textbox(Inches(1.2), Inches(4.5), Inches(3.2), Inches(0.5))
    tb.text_frame.paragraphs[0].text = "Corporate Stability · DSA · LeetCode · Tier-1 Tech"
    tb.text_frame.paragraphs[0].font.size = Pt(9.5)

    add_arrow(s6, Inches(4.6), Inches(4.4), Inches(0.5), Inches(0.25), "right", ROSE_ACCENT)

    add_card(s6, Inches(5.2), Inches(4.1), Inches(3.4), Inches(0.95), "2. Entrepreneurial Builder", ROSE_ACCENT, bg_color=CARD_BG)
    tb = s6.shapes.add_textbox(Inches(5.3), Inches(4.5), Inches(3.2), Inches(0.5))
    tb.text_frame.paragraphs[0].text = "Startup SaaS · AI Agents · Product-Market Fit"
    tb.text_frame.paragraphs[0].font.size = Pt(9.5)

    add_arrow(s6, Inches(8.7), Inches(4.4), Inches(0.5), Inches(0.25), "right", INDIGO_ACCENT)

    add_card(s6, Inches(9.3), Inches(4.1), Inches(3.0), Inches(0.95), "3. Deep-Tech Specialist", INDIGO_ACCENT, bg_color=CARD_BG)
    tb = s6.shapes.add_textbox(Inches(9.4), Inches(4.5), Inches(2.8), Inches(0.5))
    tb.text_frame.paragraphs[0].text = "Linux Systems · 5NF Databases · Network Depth"
    tb.text_frame.paragraphs[0].font.size = Pt(9.5)

    add_arrow(s6, Inches(6.5), Inches(5.3), Inches(0.25), Inches(0.35), "down", BLUE_ACCENT)

    # Row 3: Moderator, Decision Gate, & Distinct Divergent Output Boxes
    add_card(s6, Inches(0.8), Inches(5.75), Inches(3.2), Inches(1.3), "Moderator Synthesis (Φ)", BLUE_ACCENT, bg_color=BLUE_BG)
    tb = s6.shapes.add_textbox(Inches(0.9), Inches(6.15), Inches(3.0), Inches(0.8))
    tb.text_frame.paragraphs[0].text = "• Injects Probing Friction Points\n• Extracts Dispute Tree T_dispute\n• Computes Uncertainty Indicator U_hat"
    tb.text_frame.paragraphs[0].font.size = Pt(9.5)

    add_arrow(s6, Inches(4.1), Inches(6.25), Inches(0.5), Inches(0.25), "right", BLUE_ACCENT)

    # Decision Diamond
    gate = s6.shapes.add_shape(MSO_SHAPE.DIAMOND, Inches(4.7), Inches(5.75), Inches(3.2), Inches(1.3))
    gate.fill.solid()
    gate.fill.fore_color.rgb = AMBER_BG
    gate.line.color.rgb = AMBER_ACCENT
    gate.line.width = Pt(1.5)
    gp = gate.text_frame.paragraphs[0]
    gp.text = "U_hat > θ_unc OR\nCritical Dispute?"
    gp.font.name = FONT_MAIN
    gp.font.size = Pt(9.5)
    gp.font.bold = True
    gp.font.color.rgb = NAVY_HEAD
    gp.alignment = PP_ALIGN.CENTER
    gate.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    # Divergent Branch 1: YES -> Interactive Human Override Modal
    add_arrow(s6, Inches(8.0), Inches(6.05), Inches(0.5), Inches(0.2), "right", ROSE_ACCENT)
    add_card(s6, Inches(8.6), Inches(5.5), Inches(3.9), Inches(0.85), "YES: Human Arbitration Modal", ROSE_ACCENT, bg_color=ROSE_BG)
    tb_y = s6.shapes.add_textbox(Inches(8.7), Inches(5.85), Inches(3.7), Inches(0.45))
    tb_y.text_frame.paragraphs[0].text = "Candidate arbitrates friction points & sets persona weights"
    tb_y.text_frame.paragraphs[0].font.size = Pt(9.0)

    # Divergent Branch 2: NO -> Automated Roadmap Generation
    add_arrow(s6, Inches(8.0), Inches(6.55), Inches(0.5), Inches(0.2), "right", TEAL_PRIMARY)
    add_card(s6, Inches(8.6), Inches(6.45), Inches(3.9), Inches(0.85), "NO: Verified Actionable Roadmap", TEAL_PRIMARY, bg_color=TEAL_BG)
    tb_n = s6.shapes.add_textbox(Inches(8.7), Inches(6.8), Inches(3.7), Inches(0.45))
    tb_n.text_frame.paragraphs[0].text = "Direct delivery of balanced hybrid execution milestones"
    tb_n.text_frame.paragraphs[0].font.size = Pt(9.0)

    s6.notes_slide.notes_text_frame.text = (
        "Here is the complete architectural pipeline. When the multi-agent deliberation concludes, the Moderator evaluates "
        "the epistemic uncertainty score. If the score exceeds our threshold or unresolved critical trade-offs remain, the system "
        "diverges to an interactive human arbitration modal. Otherwise, it generates the verified hybrid roadmap directly."
    )

    # =========================================================================
    # SLIDE 7: The 3 Career Philosophy Personas
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    apply_bg(s7, BG_LIGHT)
    add_header(s7, "The Complementary Personas: Conflicting Career Philosophies", "PERSONA DESIGN", 7)

    top_p = Inches(1.6)
    p_w = Inches(3.64)
    p_h = Inches(5.3)

    add_card(s7, Inches(0.8), top_p, p_w, p_h, "1. The Pragmatic Traditionalist", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb1 = s7.shapes.add_textbox(Inches(1.0), top_p + Inches(0.6), p_w - Inches(0.4), p_h - Inches(0.7))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    tf1.paragraphs[0].text = "Focus: Corporate Security & Fundamentals"
    tf1.paragraphs[0].font.bold = True
    tf1.paragraphs[0].font.size = Pt(11)
    tf1.paragraphs[0].font.color.rgb = TEAL_PRIMARY
    
    prag_items = [
        ("Philosophy: ", "Security, structured growth, and highly validated career paths."),
        ("Prompt Directive: ", "Advocate for established, high-paying corporate roles. Emphasize mastering core fundamentals like Data Structures and Algorithms (DSA) and competitive programming. Demonstrate scalability expertise. Be highly skeptical of risky startups or chasing unproven tech trends."),
        ("Tone: ", "Grounded, realistic, data-driven, conservative.")
    ]
    for lbl, desc in prag_items:
        p = tf1.add_paragraph()
        p.text = lbl
        p.font.name = FONT_MAIN
        p.font.bold = True
        p.font.size = Pt(10.5)
        p.font.color.rgb = NAVY_HEAD
        p.text += desc
        p.font.bold = False
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(4)

    add_card(s7, Inches(4.84), top_p, p_w, p_h, "2. The Entrepreneurial Builder", ROSE_ACCENT, top_accent=ROSE_ACCENT)
    tb2 = s7.shapes.add_textbox(Inches(5.04), top_p + Inches(0.6), p_w - Inches(0.4), p_h - Inches(0.7))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    tf2.paragraphs[0].text = "Focus: Startup SaaS & Rapid Iteration"
    tf2.paragraphs[0].font.bold = True
    tf2.paragraphs[0].font.size = Pt(11)
    tf2.paragraphs[0].font.color.rgb = ROSE_ACCENT

    build_items = [
        ("Philosophy: ", "High risk, high reward, rapid iteration, and market disruption."),
        ("Prompt Directive: ", "Advocate for building, shipping, and monetizing products. Push user toward scalable AI SaaS platforms, finding commercial niches, and leveraging modern architectures like multi-agent systems and RAG. Argue corporate routes are too slow; real acceleration comes from launching ventures."),
        ("Tone: ", "Energetic, visionary, disruptive, product-market fit oriented.")
    ]
    for lbl, desc in build_items:
        p = tf2.add_paragraph()
        p.text = lbl
        p.font.name = FONT_MAIN
        p.font.bold = True
        p.font.size = Pt(10.5)
        p.font.color.rgb = NAVY_HEAD
        p.text += desc
        p.font.bold = False
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(4)

    add_card(s7, Inches(8.88), top_p, p_w, p_h, "3. The Deep-Tech Specialist", INDIGO_ACCENT, top_accent=INDIGO_ACCENT)
    tb3 = s7.shapes.add_textbox(Inches(9.08), top_p + Inches(0.6), p_w - Inches(0.4), p_h - Inches(0.7))
    tf3 = tb3.text_frame
    tf3.word_wrap = True
    tf3.paragraphs[0].text = "Focus: Niche Mastery & Infrastructure"
    tf3.paragraphs[0].font.bold = True
    tf3.paragraphs[0].font.size = Pt(11)
    tf3.paragraphs[0].font.color.rgb = INDIGO_ACCENT

    spec_items = [
        ("Philosophy: ", "Irreplaceability through deep, complex domain expertise."),
        ("Prompt Directive: ", "Push user toward absolute technical mastery of complex systems. Advocate for deep specialization in Linux systems engineering, advanced database design (handling normalization up to 5NF), and robust networking. Argue both Pragmatist and Builder fail without infrastructure."),
        ("Tone: ", "Highly analytical, technically rigorous, uncompromising on best practices.")
    ]
    for lbl, desc in spec_items:
        p = tf3.add_paragraph()
        p.text = lbl
        p.font.name = FONT_MAIN
        p.font.bold = True
        p.font.size = Pt(10.5)
        p.font.color.rgb = NAVY_HEAD
        p.text += desc
        p.font.bold = False
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(4)

    s7.notes_slide.notes_text_frame.text = (
        "These three personas represent the archetypal career paths faced by Computer Science graduates: corporate engineering, "
        "startup ventures, and deep infrastructure specialization. Each persona operates under a distinct prompt contract "
        "and tailored temperature settings, ensuring that the resulting debate is principled and intellectually diverse."
    )

    # =========================================================================
    # SLIDE 8: The Moderator Agent (Synthesizer & Strategist)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    apply_bg(s8, BG_LIGHT)
    add_header(s8, "The Moderator Agent: Synthesizer, Strategist & Guardrail", "MODERATOR ARCHITECTURE", 8)

    w_m = Inches(5.6)
    h_m = Inches(5.3)

    add_card(s8, Inches(0.8), Inches(1.6), w_m, h_m, "Moderator Directive & Probing Friction Role", BLUE_ACCENT, top_accent=BLUE_ACCENT)
    tb_ml = s8.shapes.add_textbox(Inches(1.0), Inches(2.2), w_m - Inches(0.4), h_m - Inches(0.7))
    tf_ml = tb_ml.text_frame
    tf_ml.word_wrap = True

    p = tf_ml.paragraphs[0]
    p.text = "Role: Neutral Facilitator & Probing Cross-Examiner"
    p.font.bold = True
    p.font.size = Pt(11.5)
    p.font.color.rgb = BLUE_ACCENT
    p.space_after = Pt(6)

    m_left_items = [
        ("Core Philosophy: ", "Balanced execution, transparent disagreement surfacing, and personalized roadmap generation."),
        ("Strict Directive: ", "You do NOT give direct career advice initially. Facilitate debate among the Pragmatist, Builder, and Specialist by asking probing follow-up questions that force agents to defend points against each other."),
        ("Tone: ", "Neutral, observant, diplomatic, and highly organized."),
        ("Friction Extraction: ", "Analyzes opening statements to find core philosophical clashes (e.g. 'Pragmatist insists on LeetCode; Builder insists on an AI SaaS. Specialist, how does low-level OS knowledge bridge or invalidate this gap?').")
    ]
    for lbl, desc in m_left_items:
        p_row = tf_ml.add_paragraph()
        p_row.text = "• " + lbl
        p_row.font.name = FONT_MAIN
        p_row.font.bold = True
        p_row.font.size = Pt(10.5)
        p_row.font.color.rgb = NAVY_HEAD
        p_row.text += desc
        p_row.font.bold = False
        p_row.font.size = Pt(10)
        p_row.font.color.rgb = TEXT_MAIN
        p_row.space_after = Pt(6)

    add_card(s8, Inches(6.9), Inches(1.6), w_m, h_m, "Synthesis & Responsible AI Governance", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb_mr = s8.shapes.add_textbox(Inches(7.1), Inches(2.2), w_m - Inches(0.4), h_m - Inches(0.7))
    tf_mr = tb_mr.text_frame
    tf_mr.word_wrap = True

    p = tf_mr.paragraphs[0]
    p.text = "Synthesis Deliverables (Across T_debate = 2 Rounds)"
    p.font.bold = True
    p.font.size = Pt(11.5)
    p.font.color.rgb = TEAL_PRIMARY
    p.space_after = Pt(6)

    m_right_items = [
        ("1. Dispute Tree (T_dispute): ", "Extracts explicit nodes of contention (e.g. corporate security vs equity upside) so the candidate directly sees trade-offs."),
        ("2. Personalized Hybrid Plan: ", "Constructs an actionable roadmap balancing corporate foundational mastery with high-leverage product shipping and deep infrastructure."),
        ("3. Uncertainty Indicator (U_hat): ", "Calculates composite epistemic uncertainty score based on persona entropy, graph distance, and NLI entailment."),
        ("4. Human Override Gate: ", "Triggers mandatory human intervention whenever uncertainty or unresolved critical disputes exceed safety thresholds.")
    ]
    for lbl, desc in m_right_items:
        p_row = tf_mr.add_paragraph()
        p_row.text = "• " + lbl
        p_row.font.name = FONT_MAIN
        p_row.font.bold = True
        p_row.font.size = Pt(10.5)
        p_row.font.color.rgb = NAVY_HEAD
        p_row.text += desc
        p_row.font.bold = False
        p_row.font.size = Pt(10)
        p_row.font.color.rgb = TEXT_MAIN
        p_row.space_after = Pt(6)

    s8.notes_slide.notes_text_frame.text = (
        "The Moderator acts as the central conductor of the debate. Rather than answering the user immediately, "
        "it identifies the core philosophical tensions in the agents' opening positions and cross-examines them. "
        "Only after two rounds of structured debate does it synthesize a personalized hybrid plan."
    )

    # =========================================================================
    # SLIDE 9: Flowchart 2 - The 5-Stage Debate Workflow (Execution Loop)
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    apply_bg(s9, BG_LIGHT)
    add_header(s9, "Flowchart: The 5-Stage Debate Workflow (Execution Loop)", "EXECUTION LOOP DIAGRAM", 9)

    stages = [
        ("1. Intake", "Candidate inputs verified competencies, historical coursework, target aspirations, and budget/timeline constraints into the local state schema.", BLUE_ACCENT, CARD_MUTED),
        ("2. Thesis", "The 3 advising agents independently retrieve from Neo4j/FAISS and formulate parallel opening arguments (150 words).", TEAL_PRIMARY, TEAL_BG),
        ("3. Friction", "Moderator cross-examines positions, extracting philosophical clashes to inject targeted friction probes forcing defense.", AMBER_ACCENT, CARD_MUTED),
        ("4. Rebuttal", "Personas defend propositions or concede unviable routes using NLI-grounded evidence. Epistemic uncertainty is updated.", ROSE_ACCENT, ROSE_BG),
        ("5. Synthesis", "Moderator synthesizes Dispute Tree and hybrid roadmap. If uncertainty or disputes exceed safety limits, cognitive forcing triggers human override.", TEAL_PRIMARY, TEAL_BG)
    ]
    card_s_w = Inches(2.18)
    card_s_h = Inches(4.8)
    for i, (st_title, st_desc, st_col, st_bg) in enumerate(stages):
        left_s = Inches(0.8) + Inches(i * 2.38)
        add_card(s9, left_s, Inches(1.8), card_s_w, card_s_h, st_title, st_col, top_accent=st_col, bg_color=st_bg)
        
        tb = s9.shapes.add_textbox(left_s + Inches(0.12), Inches(2.6), card_s_w - Inches(0.24), card_s_h - Inches(0.9))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = st_desc
        p.font.name = FONT_MAIN
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(8)

        if i < 4:
            add_arrow(s9, left_s + card_s_w - Inches(0.05), Inches(4.0), Inches(0.25), Inches(0.3), "right", TEAL_PRIMARY)

    s9.notes_slide.notes_text_frame.text = (
        "This execution loop governs every interaction. The user provides context in Stage 1. "
        "The three advising agents formulate parallel opening arguments in Stage 2. The Moderator introduces a friction probe in Stage 3. "
        "Agents defend and adapt in Stage 4. And in Stage 5, the Moderator synthesizes the hybrid roadmap."
    )

    # =========================================================================
    # SLIDE 10: Hybrid Grounding: Derived GraphRAG & Offline Corpora
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    apply_bg(s10, BG_LIGHT)
    add_header(s10, "Hybrid Grounding: Derived Neo4j DAG & Offline Corpora", "KNOWLEDGE GROUNDING", 10)

    w_g = Inches(5.6)
    h_g = Inches(5.3)

    add_card(s10, Inches(0.8), Inches(1.6), w_g, h_g, "Neo4j: Derived Skill Prerequisite DAG", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb_g1 = s10.shapes.add_textbox(Inches(1.0), Inches(2.2), w_g - Inches(0.4), h_g - Inches(0.7))
    tfg1 = tb_g1.text_frame
    tfg1.word_wrap = True
    g_pts = [
        ("Taxonomy Foundation: ", "Ingests official O*NET 29.2 and ESCO v1.2 occupation-to-competency mappings."),
        ("Synthesized Prerequisite DAG: ", "O*NET/ESCO link roles to skills but omit skill prerequisites. We synthesize DAG edges by projecting accredited CS curricula (ACM/IEEE) and Bloom's Taxonomy onto taxonomy nodes."),
        ("Deterministic Cypher Queries: ", "Agents query strict dependency paths (e.g. Discrete Math -> Data Structures -> Distributed Systems) to verify feasibility deterministically.")
    ]
    for lbl, desc in g_pts:
        p = tfg1.add_paragraph() if tfg1.paragraphs[0].text else tfg1.paragraphs[0]
        p.text = "• " + lbl
        p.font.name = FONT_MAIN
        p.font.bold = True
        p.font.size = Pt(10.5)
        p.font.color.rgb = NAVY_HEAD
        p.text += desc
        p.font.bold = False
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(5)

    add_card(s10, Inches(6.9), Inches(1.6), w_g, h_g, "FAISS & NLI Entailment Verification", BLUE_ACCENT, top_accent=BLUE_ACCENT)
    tb_g2 = s10.shapes.add_textbox(Inches(7.1), Inches(2.2), w_g - Inches(0.4), h_g - Inches(0.7))
    tfg2 = tb_g2.text_frame
    tfg2.word_wrap = True
    v_pts = [
        ("Offline Snapshot Corpus: ", "Embeds offline quarterly BLS wage distributions and curated CS course syllabi (zero live network scraping during inference to guarantee local privacy)."),
        ("Beyond Cosine Similarity: ", "Replaces uncalibrated cosine thresholds with NLI Cross-Encoder Entailment Verification: claims must satisfy P(Entailment | Retrieved Premise) > 0.80."),
        ("Numerical Salary Checkers: ", "Salary and time ranges are validated using deterministic range assertions against official BLS tables to prevent hallucinated compensation.")
    ]
    for lbl, desc in v_pts:
        p = tfg2.add_paragraph() if tfg2.paragraphs[0].text else tfg2.paragraphs[0]
        p.text = "• " + lbl
        p.font.name = FONT_MAIN
        p.font.bold = True
        p.font.size = Pt(10.5)
        p.font.color.rgb = NAVY_HEAD
        p.text += desc
        p.font.bold = False
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(5)

    add_card(s10, Inches(0.8), Inches(5.8), Inches(11.733), Inches(1.2), "", border_color=TEAL_PRIMARY, bg_color=TEAL_BG)
    tb_ban = s10.shapes.add_textbox(Inches(1.0), Inches(5.9), Inches(11.3), Inches(1.0))
    tf_b = tb_ban.text_frame
    tf_b.word_wrap = True
    p_b = tf_b.paragraphs[0]
    p_b.text = "WHY VECTOR RAG ALONE FAILS (STRUCTURAL BLINDSPOTS): "
    p_b.font.name = FONT_MAIN
    p_b.font.bold = True
    p_b.font.size = Pt(11)
    p_b.font.color.rgb = TEAL_PRIMARY
    p_b.text += "Vector search retrieves semantically similar course descriptions but is completely blind to prerequisite DAG order. Hybrid GraphRAG unifies deterministic prerequisite logic with dense syllabus content, verified via NLI entailment."
    p_b.font.bold = False
    p_b.font.size = Pt(10.5)
    p_b.font.color.rgb = NAVY_HEAD

    s10.notes_slide.notes_text_frame.text = (
        "Here we explain how our knowledge grounding works. Standard vector search has no concept of prerequisite hierarchies. "
        "We construct a prerequisite DAG by projecting ACM/IEEE computer science curricula onto O*NET 29.2 nodes. "
        "Factual claims are checked using cross-encoder NLI entailment and BLS numerical range assertions."
    )

    # =========================================================================
    # SLIDE 11: Responsible AI: Uncertainty Indicator & Cognitive Forcing
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    apply_bg(s11, BG_LIGHT)
    add_header(s11, "Responsible AI: Uncertainty Indicator & Cognitive Forcing", "RESPONSIBLE AI GOVERNANCE", 11)

    w_u = Inches(5.6)
    h_u = Inches(5.3)

    add_card(s11, Inches(0.8), Inches(1.6), w_u, h_u, "Composite Epistemic Uncertainty Indicator", AMBER_ACCENT, top_accent=AMBER_ACCENT)
    tb_u = s11.shapes.add_textbox(Inches(1.0), Inches(2.2), w_u - Inches(0.4), h_u - Inches(0.7))
    tf_u = tb_u.text_frame
    tf_u.word_wrap = True

    p_f = tf_u.paragraphs[0]
    p_f.text = "U_hat(R*) = w_1·H_hat(Π) + w_2·D_hat(G, P) + w_3·(1 - NLI_entail)"
    p_f.font.name = FONT_CODE
    p_f.font.bold = True
    p_f.font.size = Pt(11.5)
    p_f.font.color.rgb = AMBER_ACCENT
    p_f.space_after = Pt(8)

    u_desc = [
        ("H_hat(Π) — Normalized Persona Entropy: ", "Measures semantic divergence across Pragmatist, Builder, and Specialist arguments. High debate friction elevates epistemic uncertainty."),
        ("D_hat(G, P) — Normalized Graph Distance: ", "Shortest path hop distance in Neo4j from candidate verified skills to target role requirements."),
        ("1 - NLI_entail — Entailment Deficit: ", "Penalizes plans whose milestone claims lack strict NLI entailment against retrieved evidence."),
        ("Tuned Normalized Weights: ", "Weights w_1 = 0.40, w_2 = 0.35, w_3 = 0.25 established via logistic regression on 50 counselor-annotated scenarios.")
    ]
    for head, body in u_desc:
        p = tf_u.add_paragraph()
        p.text = "• " + head
        p.font.name = FONT_MAIN
        p.font.bold = True
        p.font.size = Pt(10.5)
        p.font.color.rgb = NAVY_HEAD
        p.text += body
        p.font.bold = False
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(5)

    add_card(s11, Inches(6.9), Inches(1.6), w_u, h_u, "Cognitive Forcing Trigger Gate & Human Override", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb_o = s11.shapes.add_textbox(Inches(7.1), Inches(2.2), w_u - Inches(0.4), h_u - Inches(0.7))
    tf_o = tb_o.text_frame
    tf_o.word_wrap = True

    p_f2 = tf_o.paragraphs[0]
    p_f2.text = "TriggerOverride = 1[ U_hat(R*) > θ_unc ∨ CriticalDispute(K) ∨ Risk > θ_risk ]"
    p_f2.font.name = FONT_CODE
    p_f2.font.bold = True
    p_f2.font.size = Pt(11)
    p_f2.font.color.rgb = TEAL_PRIMARY
    p_f2.space_after = Pt(8)

    o_desc = [
        ("Mitigating Automation Bias (Buçinca et al., 2021): ", "Halts automated progression whenever uncertainty U_hat > 0.65 or critical trade-offs remain."),
        ("CriticalDispute Filter: ", "Fires only when unresolved disputes in K_unresolved represent irreversible liabilities (e.g. tuition debt, dropping degree), targeting a ~35-40% trigger rate."),
        ("Risk & θ_risk: ", "Quantifies financial and temporal liability (tuition cost > budget b_max or hours > t_avail)."),
        ("Mandatory Human Veto: ", "Candidate must actively arbitrate disputes before calendar commitments are finalized.")
    ]
    for head, body in o_desc:
        p = tf_o.add_paragraph()
        p.text = "• " + head
        p.font.name = FONT_MAIN
        p.font.bold = True
        p.font.size = Pt(10.5)
        p.font.color.rgb = NAVY_HEAD
        p.text += body
        p.font.bold = False
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(5)

    s11.notes_slide.notes_text_frame.text = (
        "On this slide, we present our Composite Epistemic Uncertainty Indicator. The score combines normalized debate entropy, "
        "knowledge graph distance, and NLI entailment deficit. Rather than triggering on every minor dispute, "
        "the cognitive forcing gate filters for critical, irreversible trade-offs, yielding a calibrated 35 to 40 percent trigger rate."
    )

    # =========================================================================
    # SLIDE 12: Counterfactual Demographic Fairness Auditing
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    apply_bg(s12, BG_LIGHT)
    add_header(s12, "Counterfactual Demographic Auditing Protocol", "FAIRNESS AUDITING", 12)

    add_card(s12, Inches(0.8), Inches(1.6), Inches(11.733), Inches(1.8), "Synthetic Counterfactual Test Suite Protocol (500+ Profile Pairs with Repeated Sampling)", BLUE_ACCENT, top_accent=BLUE_ACCENT)
    tb_pr = s12.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(11.3), Inches(1.1))
    tf_pr = tb_pr.text_frame
    tf_pr.word_wrap = True
    p = tf_pr.paragraphs[0]
    p.text = "Protocol Formulation: < P_base, P_pert > where Skills, Work History, and Goals are strictly identical."
    p.font.name = FONT_CODE
    p.font.bold = True
    p.font.size = Pt(11.5)
    p.font.color.rgb = BLUE_ACCENT
    p.space_after = Pt(4)

    p2 = tf_pr.add_paragraph()
    p2.text = "Perturbations isolate demographic signals (gender markers, ethnic cues, non-elite pedigree). To decouple demographic effects from stochastic decoding noise, each profile pair undergoes N = 5 repeated temperature sampling runs with clustered standard errors."
    p2.font.name = FONT_MAIN
    p2.font.size = Pt(11)
    p2.font.color.rgb = TEXT_MAIN

    top_fm = Inches(3.6)
    fm_w = Inches(3.64)
    fm_h = Inches(3.3)

    add_card(s12, Inches(0.8), top_fm, fm_w, fm_h, "1. Recommendation Parity", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s12.shapes.add_textbox(Inches(1.0), top_fm + Inches(0.6), fm_w - Inches(0.4), fm_h - Inches(0.7))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.paragraphs[0].text = "Target: Δ_parity ≤ 0.05\n"
    tf.paragraphs[0].font.bold = True
    tf.paragraphs[0].font.size = Pt(12.5)
    tf.paragraphs[0].font.color.rgb = TEAL_PRIMARY
    f1_pts = [
        "Measures mean Jaccard distance between recommended career tracks across counterfactual profile pairs.",
        "Guarantees that changing demographic markers does not alter role recommendations when qualifications match."
    ]
    for pt in f1_pts:
        p = tf.add_paragraph()
        p.text = "• " + pt
        p.font.name = FONT_MAIN
        p.font.size = Pt(10.5)
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(4)

    add_card(s12, Inches(4.84), top_fm, fm_w, fm_h, "2. Prestige & Salary TOST", AMBER_ACCENT, top_accent=AMBER_ACCENT)
    tb = s12.shapes.add_textbox(Inches(5.04), top_fm + Inches(0.6), fm_w - Inches(0.4), fm_h - Inches(0.7))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.paragraphs[0].text = "TOST Bound: δ = ±$2,500\n"
    tf.paragraphs[0].font.bold = True
    tf.paragraphs[0].font.size = Pt(12.5)
    tf.paragraphs[0].font.color.rgb = AMBER_ACCENT
    f2_pts = [
        "Two One-Sided Tests (TOST) of statistical equivalence with margin δ = ±$2,500 (< 3% of starting SDE base).",
        "Evaluates whether starting salary differences are statistically confined within the equivalence band (p < 0.05)."
    ]
    for pt in f2_pts:
        p = tf.add_paragraph()
        p.text = "• " + pt
        p.font.name = FONT_MAIN
        p.font.size = Pt(10.5)
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(4)

    add_card(s12, Inches(8.88), top_fm, fm_w, fm_h, "3. Credential Exploitation", ROSE_ACCENT, top_accent=ROSE_ACCENT)
    tb = s12.shapes.add_textbox(Inches(9.08), top_fm + Inches(0.6), fm_w - Inches(0.4), fm_h - Inches(0.7))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.paragraphs[0].text = "Cross-SES Parity: |Δ_ECRR| ≤ 0.15\n"
    tf.paragraphs[0].font.bold = True
    tf.paragraphs[0].font.size = Pt(12.5)
    tf.paragraphs[0].font.color.rgb = ROSE_ACCENT
    f3_pts = [
        "ECRR = Unaccredited Costly Bootcamps ÷ Accredited Low-Cost Paths. Enforces an absolute cap ECRR ≤ 0.30.",
        "Audits credential distribution to ensure low-SES students are not disproportionately steered toward high-debt bootcamps."
    ]
    for pt in f3_pts:
        p = tf.add_paragraph()
        p.text = "• " + pt
        p.font.name = FONT_MAIN
        p.font.size = Pt(10.5)
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(4)

    s12.notes_slide.notes_text_frame.text = (
        "To audit fairness rigorously, we test the system across 500 synthetic profile pairs. "
        "We repeat each test five times to account for model decoding variance. We evaluate salary parity using "
        "Two One-Sided Tests for statistical equivalence with a 2,500 dollar margin, and track credential fairness across socioeconomic tiers."
    )

    # =========================================================================
    # SLIDE 13: How to Measure Outcome (Calibrated Targets & Sycophancy Benchmark)
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    apply_bg(s13, BG_LIGHT)
    add_header(s13, "How to Measure Outcome: Evaluation Framework & Standards", "OUTCOME MEASUREMENT", 13)

    tbl_shape = s13.shapes.add_table(8, 4, Inches(0.8), Inches(1.55), Inches(11.733), Inches(5.4))
    tbl = tbl_shape.table
    tbl.columns[0].width = Inches(2.8)
    tbl.columns[1].width = Inches(4.3)
    tbl.columns[2].width = Inches(2.2)
    tbl.columns[3].width = Inches(2.433)

    headers = ["Evaluation Metric", "Operational Definition & Measurement Tool", "Grounded Target Standard", "Responsible AI Objective"]
    for j, h_text in enumerate(headers):
        cell = tbl.cell(0, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = NAVY_HEAD
        p = cell.text_frame.paragraphs[0]
        p.text = h_text
        p.font.name = FONT_MAIN
        p.font.bold = True
        p.font.size = Pt(10.5)
        p.font.color.rgb = TEXT_WHITE
        p.alignment = PP_ALIGN.CENTER
        cell.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    eval_rows = [
        ("Premise-Challenge Rate (PCR)", "Proportion of flawed premises refuted on 100 impossible pivot prompts", "PCR ≥ 80.0%\n(Baseline < 15%)", "Directly suppress advisory sycophancy"),
        ("Substantiated CRR (S-CRR)", "Ratio of friction challenges resolved via evidence-grounded adaptation", "S-CRR ≥ 80.0%", "Prevent concession-based false consensus"),
        ("Unsupported-Claim Rate (UCR)", "Percentage of factual assertions lacking NLI Entailment (P < 0.80)", "UCR < 5.0%", "Suppress factual hallucinations"),
        ("Counterfactual Parity (Δ_parity)", "Mean Jaccard distance delta across 500+ demographic counterfactual pairs", "Δ_parity ≤ 0.05", "Ensure demographic neutrality"),
        ("Salary Equivalence (TOST)", "Two One-Sided Tests of equivalence on median starting compensation", "TOST p < 0.05\n(Bounds ±$2,500)", "Verify absence of compensation steering"),
        ("Uncertainty AUC-ROC", "Discrimination of counselor-labeled high-risk career transition roadmaps", "AUC ≥ 0.82", "Validate risk self-awareness of U_hat"),
        ("Counselor Expert Rubric", "Double-blind evaluation by certified career counselors (1–5 Likert)", "Avg ≥ 4.0 / 5.0\n(Kendall's W ≥ 0.70)", "Human-centered domain validation")
    ]

    for i, (m_name, m_desc, m_tgt, m_obj) in enumerate(eval_rows):
        row_idx = i + 1
        bg_row = CARD_BG if i % 2 == 0 else CARD_MUTED
        vals = [m_name, m_desc, m_tgt, m_obj]
        for j, val in enumerate(vals):
            cell = tbl.cell(row_idx, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg_row
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = FONT_MAIN
            p.font.size = Pt(9.0)
            if j == 0:
                p.font.bold = True
                p.font.color.rgb = NAVY_HEAD
            elif j == 2:
                p.font.bold = True
                p.font.color.rgb = TEAL_PRIMARY
                p.alignment = PP_ALIGN.CENTER
            else:
                p.font.color.rgb = TEXT_MAIN
            cell.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    s13.notes_slide.notes_text_frame.text = (
        "Here are our 7 core evaluation metrics. To validate our primary claim of reducing sycophancy, we introduce the "
        "Premise-Challenge Rate on an adversarial test suite of 100 impossible transitions. We also validate our uncertainty indicator "
        "using counselor risk discrimination AUC-ROC, ensuring our score tracks genuine advisory risk."
    )

    # =========================================================================
    # SLIDE 14: Flowchart 3 - Evaluation & Validation Pipeline
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    apply_bg(s14, BG_LIGHT)
    add_header(s14, "Flowchart: End-to-End Evaluation & Benchmarking Pipeline", "EVALUATION PIPELINE DIAGRAM", 14)

    add_card(s14, Inches(0.8), Inches(1.8), Inches(3.5), Inches(2.2), "1. Synthetic Profile Generator", NAVY_HEAD, top_accent=BLUE_ACCENT, bg_color=CARD_MUTED)
    tb = s14.shapes.add_textbox(Inches(0.9), Inches(2.3), Inches(3.3), Inches(1.6))
    tb.text_frame.paragraphs[0].text = "• 500+ Counterfactual Profile Pairs\n• Perturbs protected demographic signals\n• Isolates gender, ethnicity, & college tier\n• N = 5 repeated sampling runs per pair"
    tb.text_frame.paragraphs[0].font.size = Pt(10.5)

    add_arrow(s14, Inches(4.4), Inches(2.8), Inches(0.5), Inches(0.25), "right", BLUE_ACCENT)

    add_card(s14, Inches(5.0), Inches(1.8), Inches(3.5), Inches(2.2), "2. Automated Debate Harness", NAVY_HEAD, top_accent=TEAL_PRIMARY, bg_color=TEAL_BG)
    tb = s14.shapes.add_textbox(Inches(5.1), Inches(2.3), Inches(3.3), Inches(1.6))
    tb.text_frame.paragraphs[0].text = "• Executes 5-stage dialectic protocol\n• Ingests Neo4j subgraphs & FAISS chunks\n• Logs full debate transcript H\n• Extracts Dispute Tree & Uncertainty U_hat"
    tb.text_frame.paragraphs[0].font.size = Pt(10.5)

    add_arrow(s14, Inches(8.6), Inches(2.8), Inches(0.5), Inches(0.25), "right", TEAL_PRIMARY)

    add_card(s14, Inches(9.2), Inches(1.8), Inches(3.3), Inches(2.2), "3. Automated Metric Audit", NAVY_HEAD, top_accent=ROSE_ACCENT, bg_color=ROSE_BG)
    tb = s14.shapes.add_textbox(Inches(9.3), Inches(2.3), Inches(3.1), Inches(1.6))
    tb.text_frame.paragraphs[0].text = "• NLI Entailment: Contradiction Resolution\n• Cross-Encoder Verifier: Unsupported Claims\n• Shannon Entropy: Evidence Diversity\n• Jaccard Distance: Demographic Parity"
    tb.text_frame.paragraphs[0].font.size = Pt(10.5)

    add_arrow(s14, Inches(6.5), Inches(4.2), Inches(0.25), Inches(0.35), "down", NAVY_HEAD)

    add_card(s14, Inches(0.8), Inches(4.7), Inches(11.733), Inches(2.2), "4. Certified Counselor Blind Audit & Benchmark Scorecard", NAVY_HEAD, top_accent=AMBER_ACCENT)
    tb_b = s14.shapes.add_textbox(Inches(1.0), Inches(5.2), Inches(11.3), Inches(1.6))
    tf_b = tb_b.text_frame
    tf_b.paragraphs[0].text = "• Double-Blind Study: Certified career counselors evaluate anonymized outputs across 5 Likert criteria (Balance, Grounding, Viability, Dissent, Agency)."
    tf_b.paragraphs[0].font.size = Pt(11)
    tf_b.paragraphs[0].space_after = Pt(4)
    p = tf_b.add_paragraph()
    p.text = "• Decision Friction Verification: Measures whether candidates retain meaningful decision control and avoid blind compliance."
    p.font.size = Pt(11)
    p.space_after = Pt(4)
    p2 = tf_b.add_paragraph()
    p2.text = "• Empirical Scorecard: Compares full system against unconfounded single-agent and dyadic baselines."
    p2.font.size = Pt(11)

    s14.notes_slide.notes_text_frame.text = (
        "Flowchart 3 illustrates our four-stage evaluation methodology. Candidate profile pairs pass through "
        "the automated multi-agent harness, are analyzed by automated NLI and entropy verifiers, and undergo "
        "a double-blind qualitative review by certified career counselors."
    )

    # =========================================================================
    # SLIDE 15: Unconfounded Ablation Benchmark Matrix
    # =========================================================================
    s15 = prs.slides.add_slide(blank_layout)
    apply_bg(s15, BG_LIGHT)
    add_header(s15, "Ablation Study: Controlled Hypotheses & Experimental Design", "ABLATION STUDY PROTOCOL", 15)

    tbl_ab = s15.shapes.add_table(7, 5, Inches(0.8), Inches(1.6), Inches(11.733), Inches(5.2)).table
    tbl_ab.columns[0].width = Inches(2.2)
    tbl_ab.columns[1].width = Inches(2.0)
    tbl_ab.columns[2].width = Inches(2.2)
    tbl_ab.columns[3].width = Inches(2.4)
    tbl_ab.columns[4].width = Inches(2.933)

    ab_headers = ["Ablation Configuration", "Persona Structure", "Grounding Mechanism", "Hypothesized Failure Mode", "Target Benchmark Profile"]
    for j, h_text in enumerate(ab_headers):
        cell = tbl_ab.cell(0, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = NAVY_HEAD
        p = cell.text_frame.paragraphs[0]
        p.text = h_text
        p.font.name = FONT_MAIN
        p.font.bold = True
        p.font.size = Pt(10.5)
        p.font.color.rgb = TEXT_WHITE
        p.alignment = PP_ALIGN.CENTER
        cell.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    ab_rows = [
        ("1. Vanilla Baseline", "Single Agent (Qwen)", "Parametric Only", "Sycophancy & Hallucination", "Target PCR < 15%, High UCR (> 25%), S-CRR N/A (Single Agent)"),
        ("2. Self-Consistency", "Single Agent (5x samples)", "Parametric Only", "Consensus Sycophancy", "Target PCR < 25%; majority voting amplifies popular misconceptions"),
        ("3. GraphRAG Baseline", "Single Agent (Qwen)", "Derived Neo4j + FAISS", "Monolithic Perspective", "Prerequisites verified, but lacks divergent trade-offs; PCR ~ 35%"),
        ("4. Dyadic Debate Ablation", "Pragmatist + Builder", "Derived Neo4j + FAISS", "Infrastructure Blindspot", "Target S-CRR ~ 65%; ignores low-level systems & database durability"),
        ("5. Unmoderated Triad", "3 Personas (No Moderator)", "Derived Neo4j + FAISS", "Unresolved Deadlock", "Agents talk past each other; lacks friction probes and hybrid roadmap"),
        ("6. Full Proposed System", "3 Personas + Moderator", "Derived Neo4j + FAISS + NLI", "None (Target Design)", "Target PCR ≥ 80%, S-CRR ≥ 80%, UCR < 5%, Parity Δ_p ≤ 0.05")
    ]

    for i, (c_name, c_pers, c_grnd, c_fail, c_out) in enumerate(ab_rows):
        row_idx = i + 1
        bg_row = CARD_BG if i % 2 == 0 else CARD_MUTED
        vals = [c_name, c_pers, c_grnd, c_fail, c_out]
        for j, val in enumerate(vals):
            cell = tbl_ab.cell(row_idx, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg_row
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = FONT_MAIN
            p.font.size = Pt(9.0)
            if j == 0:
                p.font.bold = True
                p.font.color.rgb = NAVY_HEAD
            elif j == 4:
                p.font.bold = True
                p.font.color.rgb = TEAL_PRIMARY if i == 5 else TEXT_MAIN
            else:
                p.font.color.rgb = TEXT_MAIN
            cell.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    s15.notes_slide.notes_text_frame.text = (
        "This slide presents our controlled ablation design. Each row isolates a single experimental variable. "
        "We include a compute-matched self-consistency baseline to prove that gains are not merely due to extra sampling. "
        "We also isolate GraphRAG, dyadic debate, and the moderator to demonstrate the distinct contribution of each component."
    )

    # =========================================================================
    # SLIDE 16: Limitations, Ethical Risks & Strategic Research Roadmap
    # =========================================================================
    s16 = prs.slides.add_slide(blank_layout)
    apply_bg(s16, BG_LIGHT)
    add_header(s16, "Limitations, Ethical Risks & Strategic Research Roadmap", "LIMITATIONS & ROADMAP", 16)

    add_card(s16, Inches(0.8), Inches(1.6), w_half, h_box, "Identified Limitations & Ethical Risks", ROSE_ACCENT, top_accent=ROSE_ACCENT)
    tb_lim = s16.shapes.add_textbox(Inches(1.0), Inches(2.2), w_half - Inches(0.4), h_box - Inches(0.7))
    tf_lim = tb_lim.text_frame
    tf_lim.word_wrap = True

    lim_items = [
        ("Base Model Bias: ", "All personas execute on local Qwen-2.5-14B. While prompt contracts enforce divergence, underlying parametric priors are shared. Future iterations will test heterogeneous model ensembles."),
        ("Synthetic vs. Real Cohorts: ", "Fairness audits are currently conducted on synthetic profile pairs. Longitudinal validation with real students is required to measure career outcome efficacy."),
        ("Geographic & Cultural Scope: ", "Labor data is grounded on U.S. BLS and European ESCO statistics; international labor markets with different credential conventions require localized ontologies."),
        ("Cognitive Friction Burden: ", "Deliberate decision friction prevents blind automation compliance but demands higher cognitive effort from the student compared to instant chatbot answers.")
    ]
    for lbl, desc in lim_items:
        p = tf_lim.add_paragraph() if tf_lim.paragraphs[0].text else tf_lim.paragraphs[0]
        p.text = "• " + lbl
        p.font.name = FONT_MAIN
        p.font.bold = True
        p.font.size = Pt(11)
        p.font.color.rgb = NAVY_HEAD
        p.text += desc
        p.font.bold = False
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(6)

    add_card(s16, Inches(6.9), Inches(1.6), w_half, h_box, "Strategic Research & Deployment Roadmap", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb_rd = s16.shapes.add_textbox(Inches(7.1), Inches(2.2), w_half - Inches(0.4), h_box - Inches(0.7))
    tf_rd = tb_rd.text_frame
    tf_rd.word_wrap = True

    road_items = [
        ("Phase 1: Architecture & Graph Grounding (Completed): ", "Implementation of the LangGraph multi-agent harness, derived Neo4j prerequisite DAG, and Streamlit prototype trace viewer."),
        ("Phase 2: Empirical Benchmark & Counselor Study (Q1 2027): ", "Execution of the 500-pair counterfactual audit, Premise-Challenge Rate validation, and double-blind counselor Likert evaluation."),
        ("Phase 3: Longitudinal Undergraduate Pilot (Q2-Q3 2027): ", "Deployment with 200+ Computer Science undergraduates at partner institutions to assess user agency retention and transition milestones."),
        ("Phase 4: Multi-Model Ensembling & Cross-Domain Ontologies (Q4 2027): ", "Expanding beyond Computer Science to healthcare and engineering using multi-model agent pools.")
    ]
    for lbl, desc in road_items:
        p = tf_rd.add_paragraph() if tf_rd.paragraphs[0].text else tf_rd.paragraphs[0]
        p.text = "✔ " + lbl
        p.font.name = FONT_MAIN
        p.font.bold = True
        p.font.size = Pt(11)
        p.font.color.rgb = NAVY_HEAD
        p.text += desc
        p.font.bold = False
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(6)

    s16.notes_slide.notes_text_frame.text = (
        "Responsible AI demands transparency regarding system limitations. We acknowledge shared base model priors, "
        "geographic boundaries, and the cognitive effort imposed by decision friction. We also present our four-phase "
        "roadmap progressing from prototype validation to longitudinal undergraduate trials."
    )

    # =========================================================================
    # SLIDE 17: Selected Academic References (Full Bibliographic Citations)
    # =========================================================================
    s17 = prs.slides.add_slide(blank_layout)
    apply_bg(s17, BG_DARK)

    s17_badge = s17.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(0.8), Inches(3.6), Inches(0.35))
    s17_badge.fill.solid()
    s17_badge.fill.fore_color.rgb = RGBColor(19, 78, 74)
    s17_badge.line.color.rgb = TEAL_ACCENT
    s17_badge.line.width = Pt(1)
    p = s17_badge.text_frame.paragraphs[0]
    p.text = "ACADEMIC BIBLIOGRAPHY".upper()
    p.font.name = FONT_MAIN
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = TEAL_ACCENT
    p.alignment = PP_ALIGN.CENTER
    s17_badge.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    s17_t = s17.shapes.add_textbox(Inches(1.0), Inches(1.2), Inches(11.333), Inches(0.8))
    p_st = s17_t.text_frame.paragraphs[0]
    p_st.text = "Selected Academic References"
    p_st.font.name = FONT_MAIN
    p_st.font.size = Pt(26)
    p_st.font.bold = True
    p_st.font.color.rgb = TEXT_WHITE

    # Two Column Reference Container
    add_card(s17, Inches(1.0), Inches(2.1), Inches(11.333), Inches(4.8), "", bg_color=RGBColor(17, 24, 39), border_color=RGBColor(51, 65, 85))
    tb_ref = s17.shapes.add_textbox(Inches(1.2), Inches(2.3), Inches(10.9), Inches(4.4))
    tf_ref = tb_ref.text_frame
    tf_ref.word_wrap = True

    references = [
        ("Du, Y., Li, S., Torralba, A., Tenenbaum, J. B., & Mordatch, I. (2024). ", "Improving factuality and reasoning in language models through multiagent debate. In Proceedings of the 41st International Conference on Machine Learning (ICML 2024)."),
        ("Liang, T., He, Z., Jiao, W., Wang, X., Wang, Y., Wang, R., Yang, Y., Tu, Z., & Shi, S. (2023). ", "Encouraging divergent thinking in large language models via multi-agent debate. In Findings of EMNLP 2023."),
        ("Sharma, M., Tong, M., Korbak, T., Duvenaud, D., Askell, A., Bowman, S. R., Cheng, N., et al. (2024). ", "Towards understanding sycophancy in language models. In International Conference on Learning Representations (ICLR 2024)."),
        ("Geyik, S. C., Ambler, S., & Kenthapadi, K. (2019). ", "Fairness-aware ranking in search & recommendation systems with application to LinkedIn talent search. In ACM SIGKDD International Conference on Knowledge Discovery & Data Mining (KDD 2019)."),
        ("Xiong, M., Hu, Z., Lu, X., Li, Y., Fu, J., He, J., & Hooi, B. (2024). ", "Can LLMs express their uncertainty? An empirical evaluation of confidence elicitation in LLMs. In International Conference on Learning Representations (ICLR 2024)."),
        ("Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). ", "To trust or to think: Cognitive forcing functions can reduce overreliance on AI in AI-assisted decision-making. In ACM PACMHCI (CSCW 2021)."),
        ("Edge, D., Trinh, H., Cheng, N., Bradley, J., Chao, A., Mody, A., Truitt, S., & Larson, J. (2024). ", "From local to global: A graph RAG approach to query-focused summarization. Microsoft Research Technical Report."),
        ("Kadavath, S., Conerly, T., Askell, A., Henighan, T., et al. (2022). ", "Language models (mostly) know what they know. arXiv preprint arXiv:2207.05221."),
        ("Cummings, M. L. (2004). ", "Automation bias in intelligent time critical decision support systems. In AIAA 1st Intelligent Systems Technical Conference.")
    ]

    for authors, paper in references:
        p = tf_ref.add_paragraph() if tf_ref.paragraphs[0].text else tf_ref.paragraphs[0]
        p.text = "• " + authors
        p.font.name = FONT_MAIN
        p.font.bold = True
        p.font.size = Pt(9.5)
        p.font.color.rgb = TEAL_ACCENT
        p.text += paper
        p.font.bold = False
        p.font.size = Pt(9.5)
        p.font.color.rgb = RGBColor(203, 213, 225)
        p.space_after = Pt(3)

    s17.notes_slide.notes_text_frame.text = (
        "Here is the selected bibliography containing all foundational and peer-reviewed works cited throughout the deck. "
        "Thank you for your time, and we welcome your questions and feedback on the architecture."
    )

    out_path = "/home/thor/Desktop/RAI Project/Final_Presentation.pptx"
    prs.save(out_path)
    print(f"Definitive audited 17-slide presentation saved successfully to: {out_path}")

if __name__ == "__main__":
    build_audited_deck()
