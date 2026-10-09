#!/usr/bin/env python3
"""
Generate the Audited, Conference-Grade 16-Slide Presentation Deck:
Debate-Based Career Guidance Agent with Complementary Personas

This script implements every point from the comprehensive audit:
1. Re-labels Slide 14 as an explicit Hypothesized/Target Evaluation Protocol.
2. Derives the Neo4j prerequisite DAG explicitly (curriculum mapping on O*NET 29.x / ESCO v1.2).
3. Resolves privacy/job-postings tension via offline snapshot corpora (zero live API exfiltration).
4. Strictly isolates a_demo from recommendation prompts into an isolated audit harness.
5. Replaces naive cosine similarity with NLI Cross-Encoder Entailment (P(Entailment) > 0.80).
6. Defines normalized Epistemic Uncertainty Indicator U_hat and defines all symbols (H, K_unresolved, ECRR, Risk).
7. Calibrates Evidence Diversity to a realistic ED > 1.40 bits and Counselor Rubric to >= 4.0 / 5.0 with kappa >= 0.70.
8. Disentangles the ablation matrix across 6 controlled rows (isolating GraphRAG, Specialist, and Moderator).
9. Adds dedicated Limitations, Ethical Failure Modes, and Technical Roadmap slides.
10. Corrects literature citations (Chen et al. FAccT '23, Sharma et al. ICLR '24) and unifies terminology.
11. Optimizes visual card heights, font hierarchy (13-15pt body), word wrapping, and color consistency.
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def build_audited_presentation():
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
    TOTAL_SLIDES = 16

    def apply_bg(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_header(slide, title, category, slide_num):
        # Category Tag
        tag = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.38), Inches(3.2), Inches(0.32))
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

        # Title
        tb_t = slide.shapes.add_textbox(Inches(0.8), Inches(0.72), Inches(10.5), Inches(0.65))
        p = tb_t.text_frame.paragraphs[0]
        p.text = title
        p.font.name = FONT_MAIN
        p.font.size = Pt(21)
        p.font.bold = True
        p.font.color.rgb = NAVY_HEAD

        # Slide Number
        tb_n = slide.shapes.add_textbox(Inches(11.5), Inches(0.38), Inches(1.0), Inches(0.4))
        p_n = tb_n.text_frame.paragraphs[0]
        p_n.text = f"{slide_num:02d} / {TOTAL_SLIDES:02d}"
        p_n.font.name = FONT_MAIN
        p_n.font.size = Pt(11)
        p_n.font.bold = True
        p_n.font.color.rgb = TEXT_MUTED
        p_n.alignment = PP_ALIGN.RIGHT

        # Divider Rule
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
            p.font.size = Pt(13)
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
    # SLIDE 1: Title Slide (Academic / System Engineering Defense)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    apply_bg(s1, BG_DARK)

    # Track Badge
    s1_badge = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(1.0), Inches(5.2), Inches(0.35))
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

    # Main Title
    tb_t = s1.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(11.333), Inches(2.2))
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = "Debate-Based Career Guidance Agent\nwith Complementary Personas"
    p_t.font.name = FONT_MAIN
    p_t.font.size = Pt(36)
    p_t.font.bold = True
    p_t.font.color.rgb = TEXT_WHITE
    p_t.space_after = Pt(10)

    p_sub = tf_t.add_paragraph()
    p_sub.text = "Surfacing Real-World Software Engineering Career Trade-offs via Conflicting Optimization Goals (Pragmatist, Builder, Specialist, and Moderator)"
    p_sub.font.name = FONT_MAIN
    p_sub.font.size = Pt(15.5)
    p_sub.font.color.rgb = RGBColor(148, 163, 184)

    # Author / Metadata Card
    s1_card, _ = add_card(s1, Inches(1.0), Inches(4.3), Inches(11.333), Inches(2.5), "", bg_color=RGBColor(17, 24, 39), border_color=RGBColor(51, 65, 85))
    tb_meta = s1.shapes.add_textbox(Inches(1.3), Inches(4.5), Inches(10.7), Inches(2.1))
    tf_m = tb_meta.text_frame
    tf_m.word_wrap = True
    
    p = tf_m.paragraphs[0]
    p.text = "PROJECT DEFENSE & TECHNICAL SPECIFICATION · OCTOBER 2026"
    p.font.name = FONT_MAIN
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = TEAL_ACCENT
    p.space_after = Pt(6)

    meta_items = [
        ("Core Architecture: ", "3 Career Philosophies (Pragmatic Traditionalist, Entrepreneurial Builder, Deep-Tech Specialist) + Moderator Synthesizer"),
        ("Orchestration Loop: ", "Rigid 5-Stage Protocol: Context Intake -> Parallel Openings -> Moderator Cross-Exam -> Rebuttals -> Hybrid Synthesis"),
        ("Local Privacy & Stack: ", "100% On-Premise Qwen-Local (Ollama/vLLM) · LangGraph State Machine · Derived Neo4j DAG · Offline Snapshot FAISS"),
        ("Target Scope: ", "Computer Science & Software Engineering (CSE Core Undergraduates, Software Roles, US/Global Tech Industry)")
    ]
    for label, val in meta_items:
        p_row = tf_m.add_paragraph()
        p_row.text = label
        p_row.font.name = FONT_MAIN
        p_row.font.bold = True
        p_row.font.size = Pt(11.5)
        p_row.font.color.rgb = RGBColor(226, 232, 240)
        p_row.text += val
        p_row.font.bold = False
        p_row.font.size = Pt(11.5)
        p_row.font.color.rgb = RGBColor(203, 213, 225)
        p_row.space_after = Pt(3)

    s1.notes_slide.notes_text_frame.text = (
        "Welcome everyone. Today we present our project: Debate-Based Career Guidance Agent with Complementary Personas. "
        "Standard LLMs offer one-dimensional, sycophantic career advice. We solve this by structuring a debate between "
        "three distinct career philosophies—the Pragmatic Traditionalist, Entrepreneurial Builder, and Deep-Tech Specialist—"
        "orchestrated by an impartial Moderator Synthesizer. Our stack runs 100% on-premise using local Qwen and offline "
        "snapshot knowledge graphs, specifically scoped to Computer Science and Software Engineering career transitions."
    )

    # =========================================================================
    # SLIDE 2: Executive Summary & Project Scope
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    apply_bg(s2, BG_LIGHT)
    add_header(s2, "Executive Summary: Scoped Problem & Architectural Solution", "EXECUTIVE SUMMARY", 2)

    w_half = Inches(5.6)
    h_box = Inches(5.3)

    # Left Card: Domain Scope & The Status Quo Crisis
    add_card(s2, Inches(0.8), Inches(1.6), w_half, h_box, "Domain Scoping & Problem Landscape", ROSE_ACCENT, top_accent=ROSE_ACCENT)
    tb_sl = s2.shapes.add_textbox(Inches(1.0), Inches(2.2), w_half - Inches(0.4), h_box - Inches(0.7))
    tf_sl = tb_sl.text_frame
    tf_sl.word_wrap = True

    pts_s2_left = [
        ("Explicit Target Domain: ", "Undergraduate Computer Science & Software Engineering transitions (navigating Big Tech corporate hiring vs startup SaaS vs low-level infrastructure engineering)."),
        ("The Sycophancy Vulnerability: ", "Standard LLMs act as conversational sycophants (Sharma et al., 2024), cheerleading impossible pivots without auditing prerequisite deficits."),
        ("The Illusion of False Certainty: ", "Monolithic prompts emit authoritative single-track roadmaps that conceal volatile hiring markets, completion dropout rates, and debt liabilities."),
        ("Demographic Steering Risks: ", "Unchecked LLMs mirror historical occupational segregation (Chen et al., 2023), channeling non-traditional candidates into lower-agency certifications.")
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

    # Right Card: The Dialectic Multi-Agent Solution
    add_card(s2, Inches(6.9), Inches(1.6), w_half, h_box, "The Dialectic Multi-Agent Solution", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb_sr = s2.shapes.add_textbox(Inches(7.1), Inches(2.2), w_half - Inches(0.4), h_box - Inches(0.7))
    tf_sr = tb_sr.text_frame
    tf_sr.word_wrap = True

    pts_s2_right = [
        ("Conflicting Advising Personas: ", "Pits the Pragmatic Traditionalist (corporate stability & DSA) against the Entrepreneurial Builder (startup SaaS & AI) and Deep-Tech Specialist (Linux & 5NF infrastructure)."),
        ("Moderator-Driven Friction: ", "A neutral Moderator identifies dialectic contradictions and injects probing cross-examination questions to prevent superficial consensus."),
        ("Derived GraphRAG Grounding: ", "Enforces structural prerequisite DAGs synthesized on O*NET 29.x and ESCO v1.2 taxonomies, backed by offline snapshot course syllabi."),
        ("Responsible AI Controls: ", "Computes an Epistemic Uncertainty Indicator and enforces Cognitive Forcing Gates, mandating human review before high-risk commitments.")
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
        "Here we define our project scope and executive summary. We focus explicitly on Computer Science and "
        "Software Engineering career guidance. Career advising is fundamentally different from casual chat: advice carries "
        "financial and professional irreversibility. Our architecture replaces monolithic cheerleading with structured multi-agent debate."
    )

    # =========================================================================
    # SLIDE 3: Literature Survey (Theoretical Foundations & Related Works)
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
        ("Chen et al. (ACM FAccT 2023)\nFairness in Job Recommendation", "Recommenders amplify demographic bias across gender/prestige", "Focused on static bipartite matching; no conversational multi-agent guidance", "Conducts counterfactual demographic audits across 500+ synthetic profile pairs"),
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
        "Our literature survey covers 7 foundational works across multi-agent systems, sycophancy, recommender fairness, "
        "and human-AI interaction. Notice we specifically include Chen et al. from ACM FAccT 2023 on algorithmic fairness in "
        "job recommendations, alongside Du et al., Liang et al., Sharma et al., Xiong et al., Buçinca et al., and Edge et al."
    )

    # =========================================================================
    # SLIDE 4: Problem Definition (High-Level Sociotechnical Stakes)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    apply_bg(s4, BG_LIGHT)
    add_header(s4, "Problem Definition (High-Level): Sociotechnical Advisory Pitfalls", "HIGH-LEVEL PROBLEM", 4)

    col_w = Inches(3.64)
    col_h = Inches(5.3)

    # 1. One-Dimensional Advice
    add_card(s4, Inches(0.8), Inches(1.6), col_w, col_h, "1. The Sycophancy Trap", ROSE_ACCENT, top_accent=ROSE_ACCENT)
    tb1 = s4.shapes.add_textbox(Inches(1.0), Inches(2.2), col_w - Inches(0.4), col_h - Inches(0.7))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    tf1.paragraphs[0].text = "Advisory Sycophancy (Sharma et al., 2024):"
    tf1.paragraphs[0].font.bold = True
    tf1.paragraphs[0].font.size = Pt(11)
    tf1.paragraphs[0].font.color.rgb = ROSE_ACCENT
    pts_p1 = [
        "LLMs naturally agree with user preconceptions to maximize conversational pleasantness.",
        "When an applicant proposes an impossible transition (e.g. novice to Staff ML Engineer in 12 weeks), single-agent models encourage it without verifying prerequisite depth.",
        "Impact: Unnecessary tuition debt, high dropout rates, and abandoned transitions."
    ]
    for pt in pts_p1:
        p = tf1.add_paragraph()
        p.text = "• " + pt
        p.font.name = FONT_MAIN
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(6)

    # 2. Illusion of False Certainty
    add_card(s4, Inches(4.84), Inches(1.6), col_w, col_h, "2. Illusion of False Certainty", AMBER_ACCENT, top_accent=AMBER_ACCENT)
    tb2 = s4.shapes.add_textbox(Inches(5.04), Inches(2.2), col_w - Inches(0.4), col_h - Inches(0.7))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    tf2.paragraphs[0].text = "Epistemic Failure (Kadavath et al., 2022):"
    tf2.paragraphs[0].font.bold = True
    tf2.paragraphs[0].font.size = Pt(11)
    tf2.paragraphs[0].font.color.rgb = AMBER_ACCENT
    pts_p2 = [
        "LLMs generate authoritative, deterministic roadmaps without expressing epistemic humility.",
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

    # 3. Demographic Stereotyping & Agency
    add_card(s4, Inches(8.88), Inches(1.6), col_w, col_h, "3. Equity & Agency Failures", NAVY_HEAD, top_accent=NAVY_HEAD)
    tb3 = s4.shapes.add_textbox(Inches(9.08), Inches(2.2), col_w - Inches(0.4), col_h - Inches(0.7))
    tf3 = tb3.text_frame
    tf3.word_wrap = True
    tf3.paragraphs[0].text = "Bias & Complacency (Chen et al., 2023):"
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
        "Here we define the sociotechnical failure modes: Sycophancy (Sharma et al., 2024), False Certainty, "
        "and Equity/Automation bias. Notice that Demographic Stereotyping is placed correctly under Equity & Fairness, "
        "highlighting how pre-trained LLMs risk perpetuating workforce stratification unless explicitly audited."
    )

    # =========================================================================
    # SLIDE 5: Problem Definition (Low-Level Mathematical Specification)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    apply_bg(s5, BG_LIGHT)
    add_header(s5, "Problem Definition (Low-Level): Mathematical Specification", "LOW-LEVEL FORMULATION", 5)

    w_half = Inches(5.6)
    h_box = Inches(5.3)

    # Left: Environment Tuple
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

    # Right: Conflicting Optimization Directives
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
        "Here is the low-level mathematical formulation. We explicitly address the audit: a_demo is excluded from "
        "the recommendation profile P to prevent bias, and is used solely in the audit harness. We define H as the debate "
        "transcript history, T_debate as 2 rounds, and clarify that persona goals are qualitative prompt directives."
    )

    # =========================================================================
    # SLIDE 6: Flowchart 1 - End-to-End System Architecture (With Labeled Loop)
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

    # Row 3: Moderator, Decision Gate, & Streamlit Output with Labeled Branches
    add_card(s6, Inches(0.8), Inches(5.75), Inches(3.5), Inches(1.3), "Moderator Synthesis (Φ)", BLUE_ACCENT, bg_color=BLUE_BG)
    tb = s6.shapes.add_textbox(Inches(0.9), Inches(6.15), Inches(3.3), Inches(0.8))
    tb.text_frame.paragraphs[0].text = "• Injects Probing Friction Points\n• Extracts Dispute Tree T_dispute\n• Computes Uncertainty Indicator U_hat"
    tb.text_frame.paragraphs[0].font.size = Pt(9.5)

    add_arrow(s6, Inches(4.4), Inches(6.25), Inches(0.5), Inches(0.25), "right", BLUE_ACCENT)

    # Decision Diamond with Labeled Branches
    gate = s6.shapes.add_shape(MSO_SHAPE.DIAMOND, Inches(5.0), Inches(5.75), Inches(3.3), Inches(1.3))
    gate.fill.solid()
    gate.fill.fore_color.rgb = AMBER_BG
    gate.line.color.rgb = AMBER_ACCENT
    gate.line.width = Pt(1.5)
    gp = gate.text_frame.paragraphs[0]
    gp.text = "Uncertainty > θ_unc\nOR |K_unresolved| ≥ 1?"
    gp.font.name = FONT_MAIN
    gp.font.size = Pt(9.5)
    gp.font.bold = True
    gp.font.color.rgb = NAVY_HEAD
    gp.alignment = PP_ALIGN.CENTER
    gate.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    # Branch: YES (Loop back or Prompt User)
    add_arrow(s6, Inches(6.5), Inches(5.65), Inches(0.25), Inches(0.4), "down", ROSE_ACCENT)
    tb_yes = s6.shapes.add_textbox(Inches(6.8), Inches(5.5), Inches(1.6), Inches(0.3))
    tb_yes.text_frame.paragraphs[0].text = "[YES: Trigger Override]"
    tb_yes.text_frame.paragraphs[0].font.size = Pt(8.5)
    tb_yes.text_frame.paragraphs[0].font.bold = True
    tb_yes.text_frame.paragraphs[0].font.color.rgb = ROSE_ACCENT

    # Branch: NO (Direct Streamlit output)
    add_arrow(s6, Inches(8.4), Inches(6.25), Inches(0.5), Inches(0.25), "right", TEAL_PRIMARY)
    tb_no = s6.shapes.add_textbox(Inches(8.3), Inches(5.95), Inches(0.9), Inches(0.3))
    tb_no.text_frame.paragraphs[0].text = "[NO: Pass]"
    tb_no.text_frame.paragraphs[0].font.size = Pt(8.5)
    tb_no.text_frame.paragraphs[0].font.bold = True
    tb_no.text_frame.paragraphs[0].font.color.rgb = TEAL_PRIMARY

    add_card(s6, Inches(9.0), Inches(5.75), Inches(3.5), Inches(1.3), "Streamlit UI & Override", TEAL_PRIMARY, bg_color=TEAL_BG)
    tb = s6.shapes.add_textbox(Inches(9.1), Inches(6.15), Inches(3.3), Inches(0.8))
    tb.text_frame.paragraphs[0].text = "• Interactive Dispute Trace Viewer\n• Mandatory Human Override Controls\n• Personalized Hybrid Action Plan"
    tb.text_frame.paragraphs[0].font.size = Pt(9.5)

    s6.notes_slide.notes_text_frame.text = (
        "Flowchart 1 addresses the auditor's visual and logical points: the decision diamond is now explicitly labeled with "
        "[YES: Trigger Override] and [NO: Pass] branches. The architecture details offline snapshot grounding "
        "and local Qwen inference, eliminating data exfiltration risks."
    )

    # =========================================================================
    # SLIDE 7: The 3 Career Philosophy Personas
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    apply_bg(s7, BG_LIGHT)
    add_header(s7, "The Complementary Personas: Conflicting Career Philosophies", "PERSONA DESIGN", 7)

    p_w = Inches(3.64)
    p_h = Inches(5.3)
    top_p = Inches(1.6)

    # 1. Pragmatic Traditionalist
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

    # 2. Entrepreneurial Builder
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

    # 3. Deep-Tech Specialist (Color-coded INDIGO for consistent palette)
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
        "Here are the three complementary advising personas with conflicting optimization goals. "
        "A common reviewer question is: 'Since all personas use Qwen-2.5-14B, how do you prevent persona collapse?' "
        "Answer: We enforce rigid system prompt directives, temperature differentiation (0.3 for Specialist, 0.7 for Builder), "
        "and few-shot exemplar grounding that locks each persona into its distinct philosophical archetype."
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
        ("Strict Directive: ", "You do NOT give direct career advice initially. Your job is to facilitate the debate between the Pragmatist, Entrepreneur, and Specialist. Ask probing follow-up questions to force agents to defend points against each other."),
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
        ("3. Uncertainty Indicator (U_hat): ", "Calculates composite epistemic uncertainty score based on persona entropy and graph distance."),
        ("4. Human Override Gate: ", "Triggers mandatory human intervention whenever uncertainty or unresolved disputes exceed safety thresholds.")
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
        "The Moderator does not issue top-down advice early on. Its primary role is to extract friction from opening claims, "
        "probe the three personas to defend their recommendations, and synthesize a hybrid plan with calibrated uncertainty. "
        "This completely resolves naming and rounds drift from the audit."
    )

    # =========================================================================
    # SLIDE 9: Flowchart 2 - The 5-Stage Debate Workflow (Execution Loop)
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    apply_bg(s9, BG_LIGHT)
    add_header(s9, "Flowchart: The 5-Stage Debate Workflow (Execution Loop)", "EXECUTION LOOP DIAGRAM", 9)

    stages = [
        ("1. Context Intake", "User provides verified skills, major (e.g. CSE Core), and vague career interests.", BLUE_ACCENT, BLUE_BG),
        ("2. Opening Statements", "3 advising agents process input in parallel; output 150-word opening philosophies.", TEAL_PRIMARY, TEAL_BG),
        ("3. Cross-Exam Friction", "Moderator identifies key contradiction and injects a probing cross-examination question.", ROSE_ACCENT, ROSE_BG),
        ("4. Rebuttals", "Agents defend their philosophy against the friction point and attack opposing assumptions.", INDIGO_ACCENT, INDIGO_BG),
        ("5. Hybrid Synthesis", "Moderator outputs conflict summary, personalized hybrid plan, and triggers override gate.", NAVY_HEAD, CARD_MUTED)
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
        "Flowchart 2 details the 5-stage execution loop. In Stage 1, the user inputs their background. "
        "In Stage 2, the three agents execute in parallel. In Stage 3, the Moderator injects a sharp friction probe. "
        "In Stage 4, the agents rebut each other. In Stage 5, the Moderator synthesizes the hybrid roadmap."
    )

    # =========================================================================
    # SLIDE 10: Hybrid Grounding: Derived GraphRAG & Offline Corpora
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    apply_bg(s10, BG_LIGHT)
    add_header(s10, "Hybrid Grounding: Derived Neo4j DAG & Offline Corpora", "KNOWLEDGE GROUNDING", 10)

    w_g = Inches(5.6)
    h_g = Inches(4.0)

    # Left: Neo4j Derived DAG (Explicitly addresses audit point 1.2)
    add_card(s10, Inches(0.8), Inches(1.6), w_g, h_g, "Neo4j: Derived Skill Prerequisite DAG", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb_g1 = s10.shapes.add_textbox(Inches(1.0), Inches(2.2), w_g - Inches(0.4), h_g - Inches(0.7))
    tfg1 = tb_g1.text_frame
    tfg1.word_wrap = True
    g_pts = [
        ("Taxonomy Foundation: ", "Ingests official O*NET 29.2 and ESCO v1.2 occupation-to-competency mappings."),
        ("Synthesized Prerequisite DAG: ", "O*NET/ESCO do not contain native skill-to-skill prerequisite edges. We explicitly derive DAG edges by projecting accredited CS curricular dependencies and Bloom's Taxonomy onto skill nodes."),
        ("Deterministic Cypher Queries: ", "Agents query strict dependency paths (e.g. Discrete Math -> Algorithms -> Distributed Systems) to verify feasibility deterministically.")
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

    # Right: Offline FAISS & NLI Entailment (Explicitly addresses audit point 1.3 & 1.5)
    add_card(s10, Inches(6.9), Inches(1.6), w_g, h_g, "FAISS & NLI Entailment Verification", BLUE_ACCENT, top_accent=BLUE_ACCENT)
    tb_g2 = s10.shapes.add_textbox(Inches(7.1), Inches(2.2), w_g - Inches(0.4), h_g - Inches(0.7))
    tfg2 = tb_g2.text_frame
    tfg2.word_wrap = True
    v_pts = [
        ("Offline Snapshot Corpus: ", "Embeds offline quarterly BLS wage distributions and curated CS syllabi (zero live network scraping during inference to guarantee local privacy)."),
        ("Beyond Cosine Similarity: ", "Replaces uncalibrated cosine thresholds with NLI Cross-Encoder Entailment Verification: claims must satisfy P(Entailment | Retrieved Premise) > 0.80."),
        ("Attribution Integrity: ", "Unsupported assertions lacking factual entailment are flagged for the Critic or Moderator to challenge.")
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

    # Bottom Banner (Carefully sized with word wrapping on)
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
    p_b.text += "Vector search retrieves semantically similar course descriptions but is blind to prerequisite DAG order. Hybrid GraphRAG unifies deterministic prerequisite logic with dense syllabus content, verified via NLI entailment."
    p_b.font.bold = False
    p_b.font.size = Pt(10.5)
    p_b.font.color.rgb = NAVY_HEAD

    s10.notes_slide.notes_text_frame.text = (
        "Slide 10 directly addresses two critical reviewer questions: First, we clarify that the prerequisite DAG is derived "
        "by mapping accredited curricula and Bloom's taxonomy onto O*NET 29.2 and ESCO v1.2 nodes. Second, we eliminate "
        "the privacy contradiction by stating that market data is an offline snapshot corpus. Third, we replace cosine similarity "
        "with NLI cross-encoder entailment (P > 0.80) for factual verification."
    )

    # =========================================================================
    # SLIDE 11: Responsible AI: Uncertainty Indicator & Cognitive Forcing
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    apply_bg(s11, BG_LIGHT)
    add_header(s11, "Responsible AI: Uncertainty Indicator & Cognitive Forcing", "RESPONSIBLE AI GOVERNANCE", 11)

    w_u = Inches(5.6)
    h_u = Inches(5.3)

    # Left: Epistemic Uncertainty Indicator Formula
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
        ("H_hat(Π) — Normalized Persona Entropy: ", "Measures semantic divergence across Pragmatist, Builder, and Specialist arguments. High friction directly elevates epistemic uncertainty."),
        ("D_hat(G, P) — Normalized Graph Distance: ", "Shortest path hop distance in Neo4j from candidate verified skills to target role requirements."),
        ("1 - NLI_entail — Entailment Deficit: ", "Penalizes plans whose milestone claims lack strict NLI entailment against retrieved evidence."),
        ("Normalized Weights: ", "Weights w_1 = 0.4, w_2 = 0.35, w_3 = 0.25 (sum = 1.0) bound U_hat ∈ [0, 1].")
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

    # Right: Cognitive Forcing Trigger Gate
    add_card(s11, Inches(6.9), Inches(1.6), w_u, h_u, "Cognitive Forcing Trigger Gate & Human Override", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb_o = s11.shapes.add_textbox(Inches(7.1), Inches(2.2), w_u - Inches(0.4), h_u - Inches(0.7))
    tf_o = tb_o.text_frame
    tf_o.word_wrap = True

    p_f2 = tf_o.paragraphs[0]
    p_f2.text = "TriggerOverride = 1[ U_hat(R*) > θ_unc ∨ |K_unresolved| ≥ 1 ∨ Risk > θ_risk ]"
    p_f2.font.name = FONT_CODE
    p_f2.font.bold = True
    p_f2.font.size = Pt(11)
    p_f2.font.color.rgb = TEAL_PRIMARY
    p_f2.space_after = Pt(8)

    o_desc = [
        ("Mitigating Automation Bias (Buçinca et al., 2021): ", "Halts automated progression whenever uncertainty U_hat > 0.65 or unresolved trade-offs exist."),
        ("K_unresolved — Unresolved Disputes: ", "Set of irreconcilable trade-offs remaining between personas (e.g. corporate security vs equity upside)."),
        ("Risk & θ_risk: ", "Quantifies financial and temporal liability (e.g. tuition cost > budget b_max or hours > t_avail)."),
        ("Mandatory Human Veto: ", "Candidate must explicitly choose which persona philosophy to prioritize before calendar roadmaps are generated.")
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
        "Slide 11 addresses the auditor's request to properly define U_hat and all symbols. We frame U_hat as a "
        "Composite Epistemic Uncertainty Indicator with normalized min-max components and explicit weights. "
        "We also rigorously define K_unresolved, Risk, and the threshold triggers governing cognitive forcing."
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
    p2.text = "Perturbations isolate demographic signals (gender markers, ethnic cues, non-elite college pedigree). To decouple demographic effects from stochastic LLM decoding noise, each profile pair undergoes N = 5 repeated temperature sampling runs."
    p2.font.name = FONT_MAIN
    p2.font.size = Pt(11)
    p2.font.color.rgb = TEXT_MAIN

    fm_w = Inches(3.64)
    fm_h = Inches(3.4)
    top_fm = Inches(3.6)

    # 1. Recommendation Parity
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
        "Aims to ensure changing demographic cues does not redirect candidates to different roles when qualifications match."
    ]
    for pt in f1_pts:
        p = tf.add_paragraph()
        p.text = "• " + pt
        p.font.name = FONT_MAIN
        p.font.size = Pt(10.5)
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(4)

    # 2. Prestige & Salary Skew (Grounded tolerance)
    add_card(s12, Inches(4.84), top_fm, fm_w, fm_h, "2. Prestige & Salary Skew", AMBER_ACCENT, top_accent=AMBER_ACCENT)
    tb = s12.shapes.add_textbox(Inches(5.04), top_fm + Inches(0.6), fm_w - Inches(0.4), fm_h - Inches(0.7))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.paragraphs[0].text = "Target: |Δ_prestige| < $2,500\n"
    tf.paragraphs[0].font.bold = True
    tf.paragraphs[0].font.size = Pt(12.5)
    tf.paragraphs[0].font.color.rgb = AMBER_ACCENT
    f2_pts = [
        "Tracks projected median starting compensation across demographic cohorts with a realistic tolerance (< 3% or < $2,500).",
        "Evaluated via two-sample t-test (target p > 0.05) to verify absence of statistically significant compensation steering."
    ]
    for pt in f2_pts:
        p = tf.add_paragraph()
        p.text = "• " + pt
        p.font.name = FONT_MAIN
        p.font.size = Pt(10.5)
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(4)

    # 3. Credential Exploitation Ratio (Defined explicitly)
    add_card(s12, Inches(8.88), top_fm, fm_w, fm_h, "3. Credential Exploitation", ROSE_ACCENT, top_accent=ROSE_ACCENT)
    tb = s12.shapes.add_textbox(Inches(9.08), top_fm + Inches(0.6), fm_w - Inches(0.4), fm_h - Inches(0.7))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.paragraphs[0].text = "Target: ECRR Ratio ≈ 1.0\n"
    tf.paragraphs[0].font.bold = True
    tf.paragraphs[0].font.size = Pt(12.5)
    tf.paragraphs[0].font.color.rgb = ROSE_ACCENT
    f3_pts = [
        "ECRR Defined: Ratio of unaccredited high-cost bootcamps to accredited low-cost alternatives.",
        "Audits recommendation distribution across socioeconomic tiers to prevent predatory debt steering."
    ]
    for pt in f3_pts:
        p = tf.add_paragraph()
        p.text = "• " + pt
        p.font.name = FONT_MAIN
        p.font.size = Pt(10.5)
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(4)

    s12.notes_slide.notes_text_frame.text = (
        "Slide 12 addresses the audit by: 1) Defining ECRR explicitly as the Exploitative Credential Recommendation Ratio; "
        "2) Setting a realistic salary tolerance |Δ_prestige| < $2,500 with t-test significance; and 3) Introducing "
        "N = 5 repeated sampling runs to separate stochastic decoding variance from demographic effects."
    )

    # =========================================================================
    # SLIDE 13: How to Measure Outcome (Evaluation Framework & Calibrated Targets)
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    apply_bg(s13, BG_LIGHT)
    add_header(s13, "How to Measure Outcome: Evaluation Framework & Standards", "OUTCOME MEASUREMENT", 13)

    tbl_shape = s13.shapes.add_table(7, 4, Inches(0.8), Inches(1.6), Inches(11.733), Inches(5.2))
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
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_WHITE
        p.alignment = PP_ALIGN.CENTER
        cell.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    eval_rows = [
        ("Evidence Diversity (ED)", "Shannon entropy across 4 sources: O*NET/ESCO, syllabi, wage tables, job posts", "ED > 1.40 bits\n(> 70% max entropy)", "Mitigate single-source retrieval bias"),
        ("Contradiction-Resolution (CRR)", "Ratio of Moderator friction challenges resolved or conceded in dialogue", "CRR ≥ 85.0%", "Prevent ignoring feasibility bottlenecks"),
        ("Unsupported-Claim Rate (UCR)", "Percentage of factual assertions lacking NLI Entailment (P < 0.80)", "UCR < 5.0%", "Suppress factual hallucinations"),
        ("Counterfactual Parity (CRP)", "Mean Jaccard distance delta across 500+ demographic counterfactual pairs", "Δ_parity ≤ 0.05", "Ensure demographic neutrality"),
        ("Prestige Compensation Delta", "Difference in median starting salary across demographic cohorts", "|Δ_prestige| < $2,500\n(t-test p > 0.05)", "Prevent compensation steering"),
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
            p.font.size = Pt(9.5)
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
        "Slide 13 directly fixes the unrealistic targets highlighted in the audit: "
        "1) Evidence Diversity target is set to ED > 1.40 bits (70% of theoretical maximum of 2.0 bits across 4 sources); "
        "2) Counselor rubric target is adjusted to a realistic >= 4.0 / 5.0 with Kendall's W >= 0.70 inter-rater agreement; "
        "and 3) Unsupported Claim Rate uses NLI entailment rather than arbitrary cosine distance."
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
        "Flowchart 3 illustrates the four-stage evaluation pipeline. Synthetic counterfactual pairs pass through "
        "the automated debate harness, are audited by automated NLI and entropy verifiers, and are evaluated in a "
        "double-blind study by certified career counselors."
    )

    # =========================================================================
    # SLIDE 15: Unconfounded Ablation Benchmark Matrix (Explicitly Hypothesized)
    # =========================================================================
    s15 = prs.slides.add_slide(blank_layout)
    apply_bg(s15, BG_LIGHT)
    add_header(s15, "Ablation Study: Controlled Hypotheses & Experimental Design", "ABLATION STUDY PROTOCOL", 15)

    # Clean 6-row unconfounded table addressing audit point 1.1 & 2.5
    tbl_ab = s15.shapes.add_table(7, 5, Inches(0.8), Inches(1.6), Inches(11.733), Inches(5.2)).table
    tbl_ab.columns[0].width = Inches(2.2) # Configuration
    tbl_ab.columns[1].width = Inches(2.0) # Agents / Personas
    tbl_ab.columns[2].width = Inches(2.2) # Knowledge Grounding
    tbl_ab.columns[3].width = Inches(2.4) # Hypothesized Failure Mode
    tbl_ab.columns[4].width = Inches(2.933) # Expected Outcome Profile

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
        ("1. Vanilla Baseline", "Single Agent (Qwen)", "Parametric Only", "Sycophancy & Hallucination", "Target CRR < 20%, High UCR (> 25%), 0% uncertainty calibration"),
        ("2. Vector RAG Baseline", "Single Agent (Qwen)", "FAISS Dense Syllabi", "Prerequisite Blindness", "Factual citations improve, but skips foundational prerequisite courses"),
        ("3. GraphRAG Baseline", "Single Agent (Qwen)", "Derived Neo4j + FAISS", "Monolithic Perspective", "Prerequisites enforced, but provides one-sided advice without trade-offs"),
        ("4. Dyadic Debate Ablation", "Pragmatist + Builder", "Derived Neo4j + FAISS", "Infrastructure Blindspot", "Target CRR ~ 65%; ignores low-level systems and database durability"),
        ("5. Unmoderated Triad", "3 Personas (No Moderator)", "Derived Neo4j + FAISS", "Unresolved Deadlock", "Agents talk past each other; lacks friction probes and hybrid roadmap"),
        ("6. Full Proposed System", "3 Personas + Moderator", "Derived Neo4j + FAISS + NLI", "None (Target Design)", "Target CRR ≥ 85%, UCR < 5%, verified demographic parity Δ_p ≤ 0.05")
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
            p.font.size = Pt(9.2)
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
        "Slide 15 addresses the critical audit finding regarding confounding in the ablation study. "
        "We disentangle agent count from grounding: Row 2 tests Vector RAG, Row 3 isolates GraphRAG on a single agent, "
        "Row 4 isolates dyadic debate, Row 5 isolates the Moderator's impact, and Row 6 tests the full system. "
        "All metrics are explicitly labeled as hypothesized targets for our empirical evaluation protocol."
    )

    # =========================================================================
    # SLIDE 16: Limitations, Ethical Risks & Strategic Conclusion
    # =========================================================================
    s16 = prs.slides.add_slide(blank_layout)
    apply_bg(s16, BG_DARK)

    # Kicker
    s16_kicker = s16.shapes.add_textbox(Inches(1.0), Inches(0.8), Inches(11.333), Inches(0.4))
    kp = s16_kicker.text_frame.paragraphs[0]
    kp.text = "LIMITATIONS, ETHICAL GOVERNANCE & RESEARCH ROADMAP".upper()
    kp.font.name = FONT_MAIN
    kp.font.size = Pt(11)
    kp.font.bold = True
    kp.font.color.rgb = TEAL_ACCENT

    # Title
    s16_t = s16.shapes.add_textbox(Inches(1.0), Inches(1.2), Inches(11.333), Inches(1.0))
    p_st = s16_t.text_frame.paragraphs[0]
    p_st.text = "A Grounded, Responsible AI Framework for Career Advisory"
    p_st.font.name = FONT_MAIN
    p_st.font.size = Pt(26)
    p_st.font.bold = True
    p_st.font.color.rgb = TEXT_WHITE

    p_w16 = Inches(2.7)
    p_h16 = Inches(4.5)
    c16_data = [
        ("Base Model Dependency", "All personas execute on local Qwen-2.5-14B. Prompting enforces divergence, but models share underlying pretraining priors; future work includes multi-model ensembles.", TEAL_PRIMARY),
        ("Derived DAG Limitations", "Prerequisite edges are derived from curriculum standards, which may lag rapidly emerging industry tools; requires periodic expert ontology updates.", BLUE_ACCENT),
        ("Cognitive Friction Burden", "Cognitive forcing gates mitigate automation bias but introduce user friction; candidates must actively arbitrate disputes rather than passively receiving answers.", AMBER_ACCENT),
        ("100% Local Privacy", "Runs entirely on-premise using local Qwen and offline snapshot corpora. Zero candidate resumes or salary records leave local storage.", ROSE_ACCENT)
    ]
    for i, (head16, body16, col16) in enumerate(c16_data):
        l16 = Inches(1.0) + Inches(i * 2.88)
        card16, _ = add_card(s16, l16, Inches(2.3), p_w16, p_h16, head16, col16, top_accent=col16, bg_color=RGBColor(17, 24, 39), border_color=RGBColor(51, 65, 85))
        
        tb = s16.shapes.add_textbox(l16 + Inches(0.15), Inches(3.0), p_w16 - Inches(0.3), p_h16 - Inches(0.9))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = body16
        p.font.name = FONT_MAIN
        p.font.size = Pt(11)
        p.font.color.rgb = RGBColor(203, 213, 225)

    s16.notes_slide.notes_text_frame.text = (
        "In conclusion, Slide 16 fulfills a vital Responsible AI requirement by explicitly presenting our system's limitations: "
        "shared base model priors, derived DAG maintenance, user cognitive friction, and privacy boundaries. "
        "By replacing monolithic sycophancy with dialectic multi-agent deliberation, we establish an inspectable, "
        "fair, and grounded partner for software engineering career decisions. Thank you, and I look forward to your questions."
    )

    out_path = "/home/thor/Desktop/RAI Project/Final_Presentation.pptx"
    prs.save(out_path)
    print(f"Audited presentation saved successfully to: {out_path}")

if __name__ == "__main__":
    build_audited_presentation()
