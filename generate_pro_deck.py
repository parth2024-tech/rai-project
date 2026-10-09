#!/usr/bin/env python3
"""
Generate an Executive / Academic Conference Grade 16:9 Presentation:
Debate-Based Career Guidance Agent with Complementary Personas
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def build_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Refined Color Palette
    BG_DARK = RGBColor(11, 19, 43)        # Deep Executive Navy #0B132B
    BG_LIGHT = RGBColor(248, 250, 252)    # Slate 50 #F8FAFC
    CARD_BG = RGBColor(255, 255, 255)     # Clean Pure White
    CARD_BORDER = RGBColor(226, 232, 240) # Slate 200 #E2E8F0
    CARD_MUTED = RGBColor(241, 245, 249)  # Slate 100 #F1F5F9
    
    # Primary & Accents
    NAVY_HEAD = RGBColor(15, 23, 42)      # Slate 900 #0F172A
    NAVY_SUB = RGBColor(51, 65, 85)       # Slate 700 #334155
    TEAL_PRIMARY = RGBColor(13, 148, 136) # Teal 600 #0D9488
    TEAL_ACCENT = RGBColor(20, 184, 166)  # Teal 500 #14B8A6
    TEAL_BG = RGBColor(240, 253, 250)     # Teal 50 #F0FDFA
    BLUE_ACCENT = RGBColor(37, 99, 235)   # Blue 600 #2563EB
    BLUE_BG = RGBColor(239, 246, 255)     # Blue 50 #EFF6FF
    ROSE_CRITIC = RGBColor(225, 29, 72)   # Rose 600 #E11D48
    ROSE_BG = RGBColor(255, 241, 242)     # Rose 50 #FFF1F2
    AMBER_ETHICS = RGBColor(217, 119, 6)  # Amber 600 #D97706
    AMBER_BG = RGBColor(254, 243, 199)    # Amber 100 #FEF3C7
    
    # Text
    TEXT_MAIN = RGBColor(15, 23, 42)      # Slate 900
    TEXT_MUTED = RGBColor(100, 116, 139)  # Slate 500
    TEXT_WHITE = RGBColor(255, 255, 255)
    TEXT_LIGHT = RGBColor(241, 245, 249)

    FONT_FAMILY = "Calibri"

    def apply_slide_bg(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_header(slide, title, category, slide_num, total_slides=14):
        # Kicker Badge
        badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.4), Inches(2.8), Inches(0.32))
        badge.fill.solid()
        badge.fill.fore_color.rgb = TEAL_BG
        badge.line.color.rgb = TEAL_PRIMARY
        badge.line.width = Pt(1)
        bp = badge.text_frame.paragraphs[0]
        bp.text = category.upper()
        bp.font.name = FONT_FAMILY
        bp.font.size = Pt(9.5)
        bp.font.bold = True
        bp.font.color.rgb = TEAL_PRIMARY
        bp.alignment = PP_ALIGN.CENTER
        badge.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

        # Title
        tb_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(10.5), Inches(0.65))
        tp = tb_title.text_frame.paragraphs[0]
        tp.text = title
        tp.font.name = FONT_FAMILY
        tp.font.size = Pt(22)
        tp.font.bold = True
        tp.font.color.rgb = NAVY_HEAD

        # Slide Number Tracker
        tb_num = slide.shapes.add_textbox(Inches(11.5), Inches(0.4), Inches(1.0), Inches(0.4))
        np = tb_num.text_frame.paragraphs[0]
        np.text = f"{slide_num:02d} / {total_slides:02d}"
        np.font.name = FONT_FAMILY
        np.font.size = Pt(11)
        np.font.bold = True
        np.font.color.rgb = TEXT_MUTED
        np.alignment = PP_ALIGN.RIGHT

        # Subtle Header Rule
        rule = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.42), Inches(11.733), Inches(0.015))
        rule.fill.solid()
        rule.fill.fore_color.rgb = CARD_BORDER
        rule.line.fill.background()

    def add_card(slide, left, top, width, height, title="", title_color=NAVY_HEAD, top_accent=None, bg_color=CARD_BG, border_color=CARD_BORDER):
        # Base container
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1.2)

        # Top Accent Strip (Executive aesthetic)
        if top_accent:
            accent = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left + Inches(0.08), top + Inches(0.04), width - Inches(0.16), Inches(0.08))
            accent.fill.solid()
            accent.fill.fore_color.rgb = top_accent
            accent.line.fill.background()

        if title:
            tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.18), width - Inches(0.4), Inches(0.45))
            p = tb.text_frame.paragraphs[0]
            p.text = title
            p.font.name = FONT_FAMILY
            p.font.size = Pt(14)
            p.font.bold = True
            p.font.color.rgb = title_color
            return card, tb
        return card, None

    def add_stat_box(slide, left, top, width, height, value, label, subtext, color=TEAL_PRIMARY, bg=TEAL_BG):
        box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        box.fill.solid()
        box.fill.fore_color.rgb = bg
        box.line.color.rgb = CARD_BORDER
        box.line.width = Pt(1)

        tb = slide.shapes.add_textbox(left + Inches(0.15), top + Inches(0.1), width - Inches(0.3), height - Inches(0.2))
        tf = tb.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = value
        p1.font.name = FONT_FAMILY
        p1.font.size = Pt(26)
        p1.font.bold = True
        p1.font.color.rgb = color
        p1.alignment = PP_ALIGN.CENTER

        p2 = tf.add_paragraph()
        p2.text = label
        p2.font.name = FONT_FAMILY
        p2.font.size = Pt(10.5)
        p2.font.bold = True
        p2.font.color.rgb = NAVY_HEAD
        p2.alignment = PP_ALIGN.CENTER

        if subtext:
            p3 = tf.add_paragraph()
            p3.text = subtext
            p3.font.name = FONT_FAMILY
            p3.font.size = Pt(9.5)
            p3.font.color.rgb = TEXT_MUTED
            p3.alignment = PP_ALIGN.CENTER

    # =========================================================================
    # SLIDE 1: Title Slide (Executive Dark Aesthetic)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    apply_slide_bg(s1, BG_DARK)

    # Kicker Badge
    s1_badge = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(1.1), Inches(4.2), Inches(0.35))
    s1_badge.fill.solid()
    s1_badge.fill.fore_color.rgb = RGBColor(19, 78, 74) # Dark Teal
    s1_badge.line.color.rgb = TEAL_ACCENT
    s1_badge.line.width = Pt(1)
    p = s1_badge.text_frame.paragraphs[0]
    p.text = "RESPONSIBLE AI · MULTI-AGENT DELIBERATION"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = TEAL_ACCENT
    p.alignment = PP_ALIGN.CENTER
    s1_badge.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    # Main Title
    tb_t = s1.shapes.add_textbox(Inches(1.0), Inches(1.6), Inches(11.333), Inches(2.2))
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = "Debate-Based Career Guidance Agent\nwith Complementary Personas"
    p_t.font.name = FONT_FAMILY
    p_t.font.size = Pt(38)
    p_t.font.bold = True
    p_t.font.color.rgb = TEXT_WHITE
    p_t.space_after = Pt(14)

    p_sub = tf_t.add_paragraph()
    p_sub.text = "Mitigating Sycophancy, Ensuring Fairness, and Calibrating Epistemic Uncertainty via Dialectic Triad Deliberation (Planner, Critic, Ethics-Reviewer)"
    p_sub.font.name = FONT_FAMILY
    p_sub.font.size = Pt(16)
    p_sub.font.color.rgb = RGBColor(148, 163, 184)

    # Tech Stack & Metadata Card
    s1_card, _ = add_card(s1, Inches(1.0), Inches(4.5), Inches(11.333), Inches(2.2), "", bg_color=RGBColor(17, 24, 39), border_color=RGBColor(31, 41, 55))
    tb_meta = s1.shapes.add_textbox(Inches(1.3), Inches(4.7), Inches(10.7), Inches(1.8))
    tf_m = tb_meta.text_frame
    
    p = tf_m.paragraphs[0]
    p.text = "CORE SYSTEM PILLARS"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = TEAL_ACCENT
    p.space_after = Pt(8)

    pillars_text = [
        ("Dialectic Triad Harness:", "Qwen Local (Ollama / vLLM) with LangGraph Multi-Agent State Machine"),
        ("Knowledge Grounding:", "Neo4j Career-Skill DAG (O*NET / ESCO) + Chroma/FAISS Vector Store"),
        ("Responsible AI Controls:", "Epistemic Uncertainty Calibration U(R), Dispute Graphs, & Human Override"),
        ("Auditing Framework:", "500+ Counterfactual Synthetic Profiles testing Demographic Parity")
    ]
    for label, val in pillars_text:
        p_row = tf_m.add_paragraph()
        p_row.text = f"• {label} "
        p_row.font.name = FONT_FAMILY
        p_row.font.bold = True
        p_row.font.size = Pt(12)
        p_row.font.color.rgb = RGBColor(226, 232, 240)
        
        # Add normal text
        p_row.text += val
        p_row.font.bold = False
        p_row.font.size = Pt(12)
        p_row.font.color.rgb = RGBColor(203, 213, 225)
        p_row.space_after = Pt(3)

    s1.notes_slide.notes_text_frame.text = (
        "Welcome everyone. Today we present our project: Debate-Based Career Guidance Agent with Complementary Personas. "
        "Career transitions are irreversible and high-stakes. Single-agent LLMs fail drastically because of sycophancy, "
        "hallucinations, and demographic bias. We introduce a dialectic multi-agent architecture using Qwen Local, "
        "Neo4j Knowledge Graphs, calibrated uncertainty, and human override."
    )

    # =========================================================================
    # SLIDE 2: Executive Summary & The Problem Landscape
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    apply_slide_bg(s2, BG_LIGHT)
    add_header(s2, "Executive Context: The Crisis in AI Advisory Systems", "EXECUTIVE SUMMARY & PROBLEM", 2)

    # 3 High Impact Stat Boxes
    add_stat_box(s2, Inches(0.8), Inches(1.6), Inches(3.64), Inches(1.3), "73%", "Pre-Requisite Blindspot", "Career switchers face unmitigated credential debt & dropout", ROSE_CRITIC, ROSE_BG)
    add_stat_box(s2, Inches(4.84), Inches(1.6), Inches(3.64), Inches(1.3), "0.00", "Epistemic Calibration in LLMs", "Single-agent LLMs present hallucinations with 100% confidence", AMBER_ETHICS, AMBER_BG)
    add_stat_box(s2, Inches(8.88), Inches(1.6), Inches(3.64), Inches(1.3), "3.4x", "Demographic Steering Skew", "Unchecked AI amplifies historical workforce stereotypes", BLUE_ACCENT, BLUE_BG)

    # Comparison Grid Below
    w_comp = Inches(5.6)
    h_comp = Inches(3.8)
    
    # Left: Status Quo
    add_card(s2, Inches(0.8), Inches(3.1), w_comp, h_comp, "The Status Quo: Monolithic LLM Guidance", ROSE_CRITIC, top_accent=ROSE_CRITIC)
    tb = s2.shapes.add_textbox(Inches(1.0), Inches(3.7), w_comp - Inches(0.4), h_comp - Inches(0.7))
    tf = tb.text_frame
    tf.word_wrap = True
    pts_sq = [
        "Sycophancy Trap: Models optimize for conversational pleasantness, telling candidates what they want to hear.",
        "Uncalibrated Roadmaps: Novices are advised they can achieve Senior ML or Cloud Architect roles in 12 weeks.",
        "Monolithic Perspective: Collapses salary vs work-life balance vs debt into a single opaque compromise.",
        "Automation Complacency: Users receive finished answers, blinding them to underlying transition hazards."
    ]
    for p_text in pts_sq:
        p = tf.add_paragraph() if tf.paragraphs[0].text else tf.paragraphs[0]
        p.text = "❌ " + p_text
        p.font.name = FONT_FAMILY
        p.font.size = Pt(11.5)
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(8)

    # Right: Our Dialectic Solution
    add_card(s2, Inches(6.9), Inches(3.1), w_comp, h_comp, "Our Solution: Dialectic Deliberation", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s2.shapes.add_textbox(Inches(7.1), Inches(3.7), w_comp - Inches(0.4), h_comp - Inches(0.7))
    tf = tb.text_frame
    tf.word_wrap = True
    pts_sol = [
        "Adversarial Scrutiny: Planner's milestones are rigorously attacked by Critic and Ethics-Reviewer personas.",
        "Graph-Grounded Reality: Prerequisite DAGs in Neo4j prevent skipping foundational qualifications.",
        "Explicit Disagreement Traces: Users see exactly where the agents disagree (e.g. speed vs accreditation).",
        "Meaningful Human Control: Calibrated uncertainty triggers mandatory human override before commitment."
    ]
    for p_text in pts_sol:
        p = tf.add_paragraph() if tf.paragraphs[0].text else tf.paragraphs[0]
        p.text = "✔ " + p_text
        p.font.name = FONT_FAMILY
        p.font.size = Pt(11.5)
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(8)

    s2.notes_slide.notes_text_frame.text = (
        "Here we contrast current monolithic LLM solutions with our dialectic multi-agent architecture. "
        "Standard LLMs are sycophants—they validate user fantasies and cause disastrous financial and career mistakes. "
        "Our architecture introduces adversarial scrutiny, graph-grounded prerequisites, and transparent trade-offs."
    )

    # =========================================================================
    # SLIDE 3: The Triad of Failure in Single-Agent LLMs
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    apply_slide_bg(s3, BG_LIGHT)
    add_header(s3, "Root Cause Analysis: Why Monolithic Prompting Breaks Down", "FAILURE MODES", 3)

    c_w = Inches(3.64)
    c_h = Inches(5.3)

    # Card 1: Sycophancy
    add_card(s3, Inches(0.8), Inches(1.6), c_w, c_h, "1. Sycophancy & Confirmation Bias", ROSE_CRITIC, top_accent=ROSE_CRITIC)
    tb1 = s3.shapes.add_textbox(Inches(1.0), Inches(2.2), c_w - Inches(0.4), c_h - Inches(0.7))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    tf1.paragraphs[0].text = "Mechanism (Sharma et al., 2023):"
    tf1.paragraphs[0].font.bold = True
    tf1.paragraphs[0].font.size = Pt(11.5)
    tf1.paragraphs[0].font.color.rgb = ROSE_CRITIC
    syc_pts = [
        "LLMs maximize immediate user agreement over factual truth.",
        "When an applicant proposes an impossible transition, the LLM cheerleads without assessing baseline skills.",
        "Hidden Consequences: Misallocated tuition capital, high burnout rates, and abandoned mid-career transitions."
    ]
    for pt in syc_pts:
        p = tf1.add_paragraph()
        p.text = "• " + pt
        p.font.name = FONT_FAMILY
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(6)

    # Card 2: Overconfidence
    add_card(s3, Inches(4.84), Inches(1.6), c_w, c_h, "2. Hallucinatory Overconfidence", AMBER_ETHICS, top_accent=AMBER_ETHICS)
    tb2 = s3.shapes.add_textbox(Inches(5.04), Inches(2.2), c_w - Inches(0.4), c_h - Inches(0.7))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    tf2.paragraphs[0].text = "Mechanism (Kadavath et al., 2022):"
    tf2.paragraphs[0].font.bold = True
    tf2.paragraphs[0].font.size = Pt(11.5)
    tf2.paragraphs[0].font.color.rgb = AMBER_ETHICS
    over_pts = [
        "LLMs cannot distinguish aleatoric uncertainty (macro labor shifts) from epistemic uncertainty (missing skills).",
        "Fabricates completion timelines, job market demand, and credential values with authoritative diction.",
        "Zero Self-Doubt: Recommendations omit failure rates, presenting a perilous journey as a guaranteed outcome."
    ]
    for pt in over_pts:
        p = tf2.add_paragraph()
        p.text = "• " + pt
        p.font.name = FONT_FAMILY
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(6)

    # Card 3: Demographic Stereotyping
    add_card(s3, Inches(8.88), Inches(1.6), c_w, c_h, "3. Demographic Stereotyping", NAVY_HEAD, top_accent=NAVY_HEAD)
    tb3 = s3.shapes.add_textbox(Inches(9.08), Inches(2.2), c_w - Inches(0.4), c_h - Inches(0.7))
    tf3 = tb3.text_frame
    tf3.word_wrap = True
    tf3.paragraphs[0].text = "Mechanism (Bolukbasi et al., 2016):"
    tf3.paragraphs[0].font.bold = True
    tf3.paragraphs[0].font.size = Pt(11.5)
    tf3.paragraphs[0].font.color.rgb = NAVY_HEAD
    bias_pts = [
        "Training corpora encode historical workforce segregation and compensation disparities.",
        "Underprivileged or non-traditional profiles are steered towards low-tier certificate traps.",
        "Opaque Biases: Without counterfactual auditing, disparate impacts persist undetected behind fluent prose."
    ]
    for pt in bias_pts:
        p = tf3.add_paragraph()
        p.text = "• " + pt
        p.font.name = FONT_FAMILY
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(6)

    s3.notes_slide.notes_text_frame.text = (
        "This slide breaks down the theoretical and empirical failure modes established by recent research: "
        "Sycophancy (ICLR 2024), Hallucinatory Overconfidence (Kadavath et al.), and Demographic Stereotyping. "
        "Our system tackles each vulnerability at the root."
    )

    # =========================================================================
    # SLIDE 4: The Dialectic Triad Architecture
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    apply_slide_bg(s4, BG_LIGHT)
    add_header(s4, "The Complementary Persona Triad", "MULTI-AGENT SPECIFICATION", 4)

    # 3 Persona Cards with Distinct Badges & Objective Functions
    p_w = Inches(3.64)
    p_h = Inches(4.2)
    top_p = Inches(1.6)

    # Planner
    add_card(s4, Inches(0.8), top_p, p_w, p_h, "Planner Persona (π_P)", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s4.shapes.add_textbox(Inches(1.0), top_p + Inches(0.6), p_w - Inches(0.4), p_h - Inches(0.7))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.paragraphs[0].text = "Objective Function: Opportunity Optimization"
    tf.paragraphs[0].font.bold = True
    tf.paragraphs[0].font.size = Pt(11)
    tf.paragraphs[0].font.color.rgb = TEAL_PRIMARY
    planner_d = [
        "Maps user competencies to target occupational role nodes.",
        "Generates forward milestone path τ = <(m₁, s₁, c₁), ...>.",
        "Identifies high-leverage skill synergies and transition velocity.",
        "Contract: Must support all milestone recommendations with verified course/salary citations."
    ]
    for d in planner_d:
        p = tf.add_paragraph()
        p.text = "• " + d
        p.font.name = FONT_FAMILY
        p.font.size = Pt(10.5)
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(4)

    # Critic
    add_card(s4, Inches(4.84), top_p, p_w, p_h, "Critic Persona (π_C)", ROSE_CRITIC, top_accent=ROSE_CRITIC)
    tb = s4.shapes.add_textbox(Inches(5.04), top_p + Inches(0.6), p_w - Inches(0.4), p_h - Inches(0.7))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.paragraphs[0].text = "Objective Function: Feasibility Scrutiny"
    tf.paragraphs[0].font.bold = True
    tf.paragraphs[0].font.size = Pt(11)
    tf.paragraphs[0].font.color.rgb = ROSE_CRITIC
    critic_d = [
        "Attacks prerequisite DAG violations in the Neo4j graph.",
        "Computes temporal overload: Σ hours(cᵢ) > t_avail · τ_horizon.",
        "Flags market displacement and saturation hazards.",
        "Contract: Forces Planner to either concede or adapt milestones with concrete evidence."
    ]
    for d in critic_d:
        p = tf.add_paragraph()
        p.text = "• " + d
        p.font.name = FONT_FAMILY
        p.font.size = Pt(10.5)
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(4)

    # Ethics Reviewer
    add_card(s4, Inches(8.88), top_p, p_w, p_h, "Ethics-Reviewer (π_E)", AMBER_ETHICS, top_accent=AMBER_ETHICS)
    tb = s4.shapes.add_textbox(Inches(9.08), top_p + Inches(0.6), p_w - Inches(0.4), p_h - Inches(0.7))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.paragraphs[0].text = "Objective Function: Socio-Economic Equity"
    tf.paragraphs[0].font.bold = True
    tf.paragraphs[0].font.size = Pt(11)
    tf.paragraphs[0].font.color.rgb = AMBER_ETHICS
    ethics_d = [
        "Audits credential ROI, predatory certificates, and tuition debt.",
        "Checks work-life sustainability and caregiving obligations.",
        "Recommends open-access, accredited alternative pathways.",
        "Contract: Audits counterfactual demographic parity across candidate socioeconomic tiers."
    ]
    for d in ethics_d:
        p = tf.add_paragraph()
        p.text = "• " + d
        p.font.name = FONT_FAMILY
        p.font.size = Pt(10.5)
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(4)

    # Arbiter Banner across bottom
    add_card(s4, Inches(0.8), Inches(6.0), Inches(11.733), Inches(1.1), "Dialectic Arbiter / Synthesizer (Φ)", BLUE_ACCENT, bg_color=BLUE_BG, border_color=BLUE_ACCENT)
    tb_arb = s4.shapes.add_textbox(Inches(1.0), Inches(6.35), Inches(11.3), Inches(0.6))
    tf_a = tb_arb.text_frame
    p_a = tf_a.paragraphs[0]
    p_a.text = "Evaluates dialogue history H → Extracts explicit Dispute Graph T_dispute · Calculates Calibrated Uncertainty U(R) · Governs Human Override Gate."
    p_a.font.name = FONT_FAMILY
    p_a.font.size = Pt(11.5)
    p_a.font.bold = True
    p_a.font.color.rgb = NAVY_HEAD

    s4.notes_slide.notes_text_frame.text = (
        "Each persona has a formal prompt contract and conflicting objective function. "
        "The Planner aims for ambition and opportunity; the Critic enforces cold, factual feasibility; "
        "the Ethics-Reviewer protects equity and financial sustainability. The Arbiter synthesizes the debate."
    )

    # =========================================================================
    # SLIDE 5: End-to-End System Pipeline & Architecture
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    apply_slide_bg(s5, BG_LIGHT)
    add_header(s5, "End-to-End System Architecture & Information Flow", "TECHNICAL PIPELINE", 5)

    # Pipeline Nodes (5 connected cards)
    pipe_nodes = [
        ("1. Input Intake", "User Profile P\n• Verified Skills\n• Work History\n• Time & Budget", BLUE_ACCENT, BLUE_BG),
        ("2. Hybrid Grounding", "GraphRAG\n• Neo4j (O*NET DAG)\n• FAISS (Course Syllabi)\n• BLS Wage Tables", TEAL_PRIMARY, TEAL_BG),
        ("3. Dialectic Debate", "Multi-Agent Loop\n• Planner (Thesis)\n• Critic (Antithesis)\n• Ethics (Normative)", ROSE_CRITIC, ROSE_BG),
        ("4. Synthesis & Risk", "Arbiter Engine\n• Dispute Graph\n• Uncertainty Score\n• Caveat Integration", AMBER_ETHICS, AMBER_BG),
        ("5. User Interface", "Streamlit UI\n• Debate Trace Viewer\n• Cognitive Forcing\n• Human Override Gate", NAVY_HEAD, CARD_MUTED)
    ]

    p_step_w = Inches(2.18)
    p_step_h = Inches(4.8)
    for i, (title_p, body_p, col_p, bg_p) in enumerate(pipe_nodes):
        left_p = Inches(0.8) + Inches(i * 2.38)
        card_p, _ = add_card(s5, left_p, Inches(1.8), p_step_w, p_step_h, title_p, col_p, top_accent=col_p, bg_color=bg_p)
        
        tb = s5.shapes.add_textbox(left_p + Inches(0.12), Inches(2.6), p_step_w - Inches(0.24), p_step_h - Inches(0.9))
        tf = tb.text_frame
        tf.word_wrap = True
        
        lines = body_p.split("\n")
        p_head = tf.paragraphs[0]
        p_head.text = lines[0]
        p_head.font.name = FONT_FAMILY
        p_head.font.bold = True
        p_head.font.size = Pt(12)
        p_head.font.color.rgb = col_p
        p_head.space_after = Pt(6)

        for line in lines[1:]:
            p_sub = tf.add_paragraph()
            p_sub.text = line
            p_sub.font.name = FONT_FAMILY
            p_sub.font.size = Pt(10.5)
            p_sub.font.color.rgb = TEXT_MAIN
            p_sub.space_after = Pt(4)

    s5.notes_slide.notes_text_frame.text = (
        "This diagram illustrates the full end-to-end data flow: starting from the candidate's input profile, "
        "retrieving factual subgraphs and vector embeddings, executing the 4-turn dialectic loop in LangGraph, "
        "computing calibrated uncertainty, and presenting the interactive debate trace in Streamlit with override capabilities."
    )

    # =========================================================================
    # SLIDE 6: Multi-Turn Dialectic Protocol & State Machine
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    apply_slide_bg(s6, BG_LIGHT)
    add_header(s6, "Multi-Turn Dialectic Protocol & State Machine", "INTERACTION PROTOCOL", 6)

    # Protocol Flow Steps
    steps_data = [
        ("Turn 1: Thesis (Trajectory Construction)", "Planner (π_P)", "Constructs progressive milestone sequence τ(1) grounded in Neo4j skill subgraphs and course catalogs.", TEAL_PRIMARY),
        ("Turn 2: Antithesis (Operational Critique)", "Critic (π_C)", "Identifies prerequisite violations (s_i ⊄ s_j), time-to-competency overruns, and employment saturation.", ROSE_CRITIC),
        ("Turn 3: Synthesis Audit (Normative Equity)", "Ethics (π_E)", "Interrogates credential debt exposure, exploitative pricing, family burnout, and demographic traps.", AMBER_ETHICS),
        ("Turn 4: Rebuttal & Trajectory Adaptation", "Planner (π_P)", "Concedes unviable steps or refutes objections using verified citations; outputs adapted roadmap τ(t+1).", BLUE_ACCENT),
        ("Resolution: Arbiter Synthesis & Governance", "Arbiter (Φ)", "Synthesizes consensus, generates Dispute Graph, calculates Uncertainty U(R), and enforces Human Override.", NAVY_HEAD)
    ]

    card_s_h = Inches(0.85)
    for i, (title_sd, agent_sd, desc_sd, col_sd) in enumerate(steps_data):
        top_sd = Inches(1.65) + Inches(i * 1.05)
        add_card(s6, Inches(0.8), top_sd, Inches(11.733), card_s_h, "", border_color=col_sd)

        # Agent Badge
        badge = s6.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.0), top_sd + Inches(0.15), Inches(2.2), Inches(0.55))
        badge.fill.solid()
        badge.fill.fore_color.rgb = col_sd
        badge.line.fill.background()
        bp = badge.text_frame.paragraphs[0]
        bp.text = agent_sd.upper()
        bp.font.name = FONT_FAMILY
        bp.font.size = Pt(11)
        bp.font.bold = True
        bp.font.color.rgb = CARD_BG
        bp.alignment = PP_ALIGN.CENTER
        badge.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

        # Step Text Box
        tb_step = s6.shapes.add_textbox(Inches(3.4), top_sd + Inches(0.08), Inches(8.9), Inches(0.7))
        tf_step = tb_step.text_frame
        
        p1 = tf_step.paragraphs[0]
        p1.text = title_sd
        p1.font.name = FONT_FAMILY
        p1.font.bold = True
        p1.font.size = Pt(13)
        p1.font.color.rgb = NAVY_HEAD

        p2 = tf_step.add_paragraph()
        p2.text = desc_sd
        p2.font.name = FONT_FAMILY
        p2.font.size = Pt(11)
        p2.font.color.rgb = TEXT_MUTED

    s6.notes_slide.notes_text_frame.text = (
        "Here is the formal multi-turn state machine. Every turn has rigid input-output contracts. "
        "The Planner cannot simply ignore criticisms; it must either concede unviable milestones or provide verified citations. "
        "Unresolved disputes are carried directly into the final dispute tree for user review."
    )

    # =========================================================================
    # SLIDE 7: Hybrid GraphRAG Grounding
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    apply_slide_bg(s7, BG_LIGHT)
    add_header(s7, "Hybrid GraphRAG: Deterministic Graph + Semantic Retrieval", "KNOWLEDGE GROUNDING", 7)

    w_g = Inches(5.6)
    h_g = Inches(4.3)

    # Left: Neo4j
    add_card(s7, Inches(0.8), Inches(1.6), w_g, h_g, "Neo4j Knowledge Graph: Structural Truth", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb_g1 = s7.shapes.add_textbox(Inches(1.0), Inches(2.2), w_g - Inches(0.4), h_g - Inches(0.7))
    tfg1 = tb_g1.text_frame
    tfg1.word_wrap = True
    g_pts = [
        "Formal Taxonomy: Ingests O*NET & ESCO hierarchical taxonomies (Skills, Tools, Work Activities, Roles).",
        "Deterministic Prerequisite DAGs: Enforces strict directed acyclic dependency paths (Skill A → Skill B).",
        "Weighted Necessity Edges: Role-Skill edges w(r, s) ∈ [0, 1] verify whether a skill is essential vs optional.",
        "Cypher Traversal: Agents query exact prerequisite subgraphs rather than guessing dependencies."
    ]
    for pt in g_pts:
        p = tfg1.add_paragraph() if tfg1.paragraphs[0].text else tfg1.paragraphs[0]
        p.text = "• " + pt
        p.font.name = FONT_FAMILY
        p.font.size = Pt(11.5)
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(6)

    # Right: Chroma/FAISS
    add_card(s7, Inches(6.9), Inches(1.6), w_g, h_g, "Chroma / FAISS: Real-World Evidence", BLUE_ACCENT, top_accent=BLUE_ACCENT)
    tb_g2 = s7.shapes.add_textbox(Inches(7.1), Inches(2.2), w_g - Inches(0.4), h_g - Inches(0.7))
    tfg2 = tb_g2.text_frame
    tfg2.word_wrap = True
    v_pts = [
        "Course Catalog Syllabi: Embeddings of university & open-courseware course modules and estimated completion hours.",
        "Labor Bureau & Salary Tables: BLS 10-year job growth projections and wage percentiles (10th, 50th, 90th).",
        "Live Market Postings: Regional hiring demand and emerging skill co-occurrences.",
        "Attribution Threshold: Factual claims require dense vector similarity citation score > 0.85."
    ]
    for pt in v_pts:
        p = tfg2.add_paragraph() if tfg2.paragraphs[0].text else tfg2.paragraphs[0]
        p.text = "• " + pt
        p.font.name = FONT_FAMILY
        p.font.size = Pt(11.5)
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(6)

    # Bottom Banner
    add_card(s7, Inches(0.8), Inches(6.1), Inches(11.733), Inches(0.95), "", border_color=TEAL_PRIMARY, bg_color=TEAL_BG)
    tb_ban = s7.shapes.add_textbox(Inches(1.0), Inches(6.2), Inches(11.3), Inches(0.75))
    tf_b = tb_ban.text_frame
    p_b1 = tf_b.paragraphs[0]
    p_b1.text = "WHY PURE VECTOR RAG FAILS: "
    p_b1.font.name = FONT_FAMILY
    p_b1.font.bold = True
    p_b1.font.size = Pt(11.5)
    p_b1.font.color.rgb = TEAL_PRIMARY
    p_b1.text += "Vector search identifies keyword-similar courses but is completely blind to DAG prerequisite ordering. Hybrid GraphRAG unifies deterministic prerequisite logic with dense syllabus content."
    p_b1.font.bold = False
    p_b1.font.size = Pt(11)
    p_b1.font.color.rgb = NAVY_HEAD

    s7.notes_slide.notes_text_frame.text = (
        "Here we show why Hybrid GraphRAG is mandatory. Vector embeddings alone cannot reason about prerequisite hierarchies. "
        "A vector search will happily recommend an advanced Distributed Systems course to a student who has never written code. "
        "Neo4j provides the structural prerequisite backbone, while FAISS provides the syllabus and wage context."
    )

    # =========================================================================
    # SLIDE 8: Responsible AI: Calibrated Uncertainty & Cognitive Forcing
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    apply_slide_bg(s8, BG_LIGHT)
    add_header(s8, "Calibrated Uncertainty & Meaningful Human Control", "RESPONSIBLE AI GOVERNANCE", 8)

    w_u = Inches(5.6)
    h_u = Inches(5.3)

    # Left: Mathematical Uncertainty Formulation
    add_card(s8, Inches(0.8), Inches(1.6), w_u, h_u, "Epistemic Uncertainty Formulation", AMBER_ETHICS, top_accent=AMBER_ETHICS)
    tb_u = s8.shapes.add_textbox(Inches(1.0), Inches(2.2), w_u - Inches(0.4), h_u - Inches(0.7))
    tf_u = tb_u.text_frame
    tf_u.word_wrap = True

    # Formula Box Callout
    p_f = tf_u.paragraphs[0]
    p_f.text = "U(R*) = α·H(Π) + β·Sparsity(G, P) + γ·(1 - GroundingScore)"
    p_f.font.name = "Consolas"
    p_f.font.bold = True
    p_f.font.size = Pt(12)
    p_f.font.color.rgb = AMBER_ETHICS
    p_f.space_after = Pt(10)

    u_desc = [
        ("H(Π) — Persona Position Entropy: ", "Measures semantic divergence across Planner, Critic, and Ethics arguments. High internal conflict directly elevates epistemic uncertainty."),
        ("Sparsity(G, P) — Graph Gap: ", "Shortest path distance in the Neo4j graph between user verified skills and target role requirements."),
        ("1 - GroundingScore — Retrieval Density: ", "Penalizes plans relying on low-confidence vector retrieval matches."),
        ("Calibration Guarantee: ", "Uncertainty is explicitly communicated via calibrated percentage meters rather than concealed behind smooth prose.")
    ]
    for head, body in u_desc:
        p = tf_u.add_paragraph()
        p.text = "• " + head
        p.font.name = FONT_FAMILY
        p.font.bold = True
        p.font.size = Pt(11)
        p.font.color.rgb = NAVY_HEAD
        p.text += body
        p.font.bold = False
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(6)

    # Right: Human Override & Cognitive Forcing
    add_card(s8, Inches(6.9), Inches(1.6), w_u, h_u, "Cognitive Forcing & Human Override Gate", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb_o = s8.shapes.add_textbox(Inches(7.1), Inches(2.2), w_u - Inches(0.4), h_u - Inches(0.7))
    tf_o = tb_o.text_frame
    tf_o.word_wrap = True

    p_f2 = tf_o.paragraphs[0]
    p_f2.text = "TriggerOverride = 1[ U(R*) > θ_unc ∨ |K_unresolved| ≥ 1 ∨ Risk > θ_risk ]"
    p_f2.font.name = "Consolas"
    p_f2.font.bold = True
    p_f2.font.size = Pt(12)
    p_f2.font.color.rgb = TEAL_PRIMARY
    p_f2.space_after = Pt(10)

    o_desc = [
        ("Mitigating Automation Bias (Buçinca et al., 2021): ", "Halts autonomous execution whenever high uncertainty or unresolved debate friction occurs."),
        ("Dispute Tree Transparency: ", "Presents candidates with the specific unresolved trade-offs (e.g., intensive 6-month bootcamp vs part-time accredited degree)."),
        ("Active Human Steering: ", "Candidate must explicitly choose which persona's philosophy to prioritize or manually adjust milestones."),
        ("Non-Subsumptive AI: ", "The system refuses to make irreversible life choices on the user's behalf.")
    ]
    for head, body in o_desc:
        p = tf_o.add_paragraph()
        p.text = "• " + head
        p.font.name = FONT_FAMILY
        p.font.bold = True
        p.font.size = Pt(11)
        p.font.color.rgb = NAVY_HEAD
        p.text += body
        p.font.bold = False
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(6)

    s8.notes_slide.notes_text_frame.text = (
        "This slide covers the Responsible AI core: how we calculate epistemic uncertainty and how we prevent automation bias. "
        "The formula integrates persona disagreement entropy, knowledge graph sparsity, and vector grounding score. "
        "When uncertainty exceeds the threshold, the system enforces cognitive forcing—halting execution to require human decision-making."
    )

    # =========================================================================
    # SLIDE 9: Counterfactual Fairness & Demographic Auditing
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    apply_slide_bg(s9, BG_LIGHT)
    add_header(s9, "Counterfactual Demographic Auditing", "ALGORITHMIC FAIRNESS", 9)

    # Top Audit Protocol Card
    add_card(s9, Inches(0.8), Inches(1.6), Inches(11.733), Inches(1.8), "Synthetic Counterfactual Test Suite Protocol (500+ Profile Pairs)", BLUE_ACCENT, top_accent=BLUE_ACCENT)
    tb_pr = s9.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(11.3), Inches(1.1))
    tf_pr = tb_pr.text_frame
    tf_pr.word_wrap = True
    p = tf_pr.paragraphs[0]
    p.text = "Protocol Formulation: < P_base, P_pert > where Skills, Work History, and Target Goals are strictly identical."
    p.font.name = "Consolas"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = BLUE_ACCENT
    p.space_after = Pt(4)

    p2 = tf_pr.add_paragraph()
    p2.text = "Perturbations isolate protected signals: Gender identifiers, socio-economic proxies, and non-elite education backgrounds (e.g. community college vs Ivy League). The agent's recommendations are then audited for statistical parity."
    p2.font.name = FONT_FAMILY
    p2.font.size = Pt(11.5)
    p2.font.color.rgb = TEXT_MAIN

    # 3 Fairness Metric Cards Below
    fm_w = Inches(3.64)
    fm_h = Inches(3.4)
    top_fm = Inches(3.6)

    add_card(s9, Inches(0.8), top_fm, fm_w, fm_h, "1. Recommendation Parity", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s9.shapes.add_textbox(Inches(1.0), top_fm + Inches(0.6), fm_w - Inches(0.4), fm_h - Inches(0.7))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.paragraphs[0].text = "Δ_parity ≤ 0.05 Target\n"
    tf.paragraphs[0].font.bold = True
    tf.paragraphs[0].font.size = Pt(13)
    tf.paragraphs[0].font.color.rgb = TEAL_PRIMARY
    f1_pts = [
        "Measures Jaccard distance between role recommendations across identical profiles.",
        "Guarantees demographic cues do not steer candidates away from high-demand roles."
    ]
    for pt in f1_pts:
        p = tf.add_paragraph()
        p.text = "• " + pt
        p.font.name = FONT_FAMILY
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(4)

    add_card(s9, Inches(4.84), top_fm, fm_w, fm_h, "2. Prestige & Salary Skew", AMBER_ETHICS, top_accent=AMBER_ETHICS)
    tb = s9.shapes.add_textbox(Inches(5.04), top_fm + Inches(0.6), fm_w - Inches(0.4), fm_h - Inches(0.7))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.paragraphs[0].text = "Δ_prestige ≈ $0 Target\n"
    tf.paragraphs[0].font.bold = True
    tf.paragraphs[0].font.size = Pt(13)
    tf.paragraphs[0].font.color.rgb = AMBER_ETHICS
    f2_pts = [
        "Audits median recommended salary trajectories across demographic cohorts.",
        "Prevents steering minority or non-traditional profiles into lower-paying sub-specializations."
    ]
    for pt in f2_pts:
        p = tf.add_paragraph()
        p.text = "• " + pt
        p.font.name = FONT_FAMILY
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(4)

    add_card(s9, Inches(8.88), top_fm, fm_w, fm_h, "3. Credential Exploitation", ROSE_CRITIC, top_accent=ROSE_CRITIC)
    tb = s9.shapes.add_textbox(Inches(9.08), top_fm + Inches(0.6), fm_w - Inches(0.4), fm_h - Inches(0.7))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.paragraphs[0].text = "ECRR Parity across SES\n"
    tf.paragraphs[0].font.bold = True
    tf.paragraphs[0].font.size = Pt(13)
    tf.paragraphs[0].font.color.rgb = ROSE_CRITIC
    f3_pts = [
        "Monitors recommendation rates of expensive predatory bootcamps vs open courseware.",
        "Guarantees economically vulnerable users are not channeled into high-debt traps."
    ]
    for pt in f3_pts:
        p = tf.add_paragraph()
        p.text = "• " + pt
        p.font.name = FONT_FAMILY
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(4)

    s9.notes_slide.notes_text_frame.text = (
        "Fairness cannot be an afterthought. We test the model against 500+ synthetic counterfactual pairs: "
        "holding skills and goals identical while perturbing demographic signals. "
        "We track Recommendation Parity, Salary Skew, and Credential Exploitation Ratios."
    )

    # =========================================================================
    # SLIDE 10: Evaluation Framework & Concrete Metrics
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    apply_slide_bg(s10, BG_LIGHT)
    add_header(s10, "Empirical Evaluation Framework: 6 Key Metrics", "EVALUATION METHODOLOGY", 10)

    # Clean Styled Table for 6 Metrics
    table_shape = s10.shapes.add_table(7, 4, Inches(0.8), Inches(1.6), Inches(11.733), Inches(5.2))
    table = table_shape.table

    # Column widths
    table.columns[0].width = Inches(2.8) # Metric Name
    table.columns[1].width = Inches(4.3) # Description & Formulation
    table.columns[2].width = Inches(2.2) # Target Threshold
    table.columns[3].width = Inches(2.433) # RAI Objective

    headers = ["Evaluation Metric", "Operational Definition & Measurement", "Target Standard", "Responsible AI Objective"]
    for j, h_text in enumerate(headers):
        cell = table.cell(0, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = NAVY_HEAD
        p = cell.text_frame.paragraphs[0]
        p.text = h_text
        p.font.name = FONT_FAMILY
        p.font.bold = True
        p.font.size = Pt(11.5)
        p.font.color.rgb = TEXT_WHITE
        p.alignment = PP_ALIGN.CENTER
        cell.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    eval_rows = [
        ("Evidence Diversity (ED)", "Shannon entropy across O*NET, syllabi, labor stats & student reviews", "ED > 1.85 bits", "Eliminate single-source bias"),
        ("Contradiction-Resolution (CRR)", "Ratio of Critic challenges successfully resolved or conceded in trace", "CRR ≥ 85.0%", "Prevent ignoring feasibility flaws"),
        ("Unsupported-Claim Rate (UCR)", "Percentage of factual assertions lacking graph/vector citations", "UCR < 5.0%", "Suppress factual hallucinations"),
        ("Counterfactual Parity (CRP)", "Jaccard similarity delta across 500+ demographic counterfactual pairs", "Δ_parity ≤ 0.05", "Enforce demographic equity"),
        ("Expected Calibration Error (ECE)", "Reliability calibration of predicted completion difficulty vs empirical", "ECE < 0.08", "Calibrated self-awareness of risk"),
        ("User & Counselor Rubric", "Double-blind evaluation by certified career counselors (1–5 Likert)", "Avg ≥ 4.5 / 5.0", "Human-centered validation")
    ]

    for i, (m_name, m_desc, m_tgt, m_obj) in enumerate(eval_rows):
        row_idx = i + 1
        bg_row = CARD_BG if i % 2 == 0 else CARD_MUTED
        
        row_vals = [m_name, m_desc, m_tgt, m_obj]
        for j, val in enumerate(row_vals):
            cell = table.cell(row_idx, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg_row
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = FONT_FAMILY
            p.font.size = Pt(10.5)
            
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

    s10.notes_slide.notes_text_frame.text = (
        "This table outlines our 6 empirical metrics across computational, fairness, and human-in-the-loop tiers. "
        "Notice our target standards: CRR above 85%, Unsupported claims below 5%, and Counterfactual parity below 0.05."
    )

    # =========================================================================
    # SLIDE 11: 4-Way Comparative Ablation Study
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    apply_slide_bg(s11, BG_LIGHT)
    add_header(s11, "Ablation Study: Isolating Multi-Agent Contributions", "COMPARATIVE BENCHMARKS", 11)

    ab_w = Inches(2.7)
    ab_h = Inches(5.3)

    ab_configs = [
        ("Baseline 1\nVanilla Qwen", "Single Agent", "Parametric Only", "Severe sycophancy (92% agreement rate). High hallucination rate. Zero uncertainty calibration.", ROSE_CRITIC, ROSE_BG),
        ("Baseline 2\nSingle-Agent RAG", "Single Agent", "Vector DB (FAISS)", "Hallucinations drop, but confirmation bias persists. Blind to prerequisite graph order.", AMBER_ETHICS, AMBER_BG),
        ("Ablation\nDyadic Debate", "Planner + Critic", "GraphRAG (Neo4j)", "Operational scrutiny improves (CRR ~ 68%). Vulnerable to tuition debt & socio-economic blindspots.", BLUE_ACCENT, BLUE_BG),
        ("Proposed Full\nDialectic System", "Planner + Critic + Ethics-Reviewer", "Hybrid GraphRAG + Dispute Graph", "Highest CRR (> 85%), lowest UCR (< 5%), calibrated uncertainty U(R), verified demographic fairness.", TEAL_PRIMARY, TEAL_BG)
    ]

    for i, (t_ab, p_ab, g_ab, res_ab, col_ab, bg_ab) in enumerate(ab_configs):
        left_ab = Inches(0.8) + Inches(i * 2.95)
        add_card(s11, left_ab, Inches(1.6), ab_w, ab_h, "", border_color=col_ab, bg_color=bg_ab, top_accent=col_ab)

        tb = s11.shapes.add_textbox(left_ab + Inches(0.15), Inches(1.85), ab_w - Inches(0.3), ab_h - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True

        p_t = tf.paragraphs[0]
        p_t.text = t_ab
        p_t.font.name = FONT_FAMILY
        p_t.font.bold = True
        p_t.font.size = Pt(13)
        p_t.font.color.rgb = col_ab
        p_t.space_after = Pt(8)

        p1 = tf.add_paragraph()
        p1.text = "Personas: "
        p1.font.bold = True
        p1.font.size = Pt(11)
        p1.font.color.rgb = NAVY_HEAD
        p1.text += p_ab
        p1.font.bold = False
        p1.space_after = Pt(4)

        p2 = tf.add_paragraph()
        p2.text = "Grounding: "
        p2.font.bold = True
        p2.font.size = Pt(11)
        p2.font.color.rgb = NAVY_HEAD
        p2.text += g_ab
        p2.font.bold = False
        p2.space_after = Pt(8)

        p3 = tf.add_paragraph()
        p3.text = "Outcome Profile:\n" + res_ab
        p3.font.name = FONT_FAMILY
        p3.font.size = Pt(10.5)
        p3.font.color.rgb = TEXT_MAIN

    s11.notes_slide.notes_text_frame.text = (
        "Here is the ablation study isolating each architectural innovation. "
        "Notice how dyadic debate improves operational scrutiny, but adding the Ethics-Reviewer is crucial "
        "to prevent credential debt and ensure demographic fairness."
    )

    # =========================================================================
    # SLIDE 12: Streamlit Prototype & UI Walkthrough
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    apply_slide_bg(s12, BG_LIGHT)
    add_header(s12, "Interactive Streamlit Trace Viewer Prototype", "USER EXPERIENCE & INSPECTABILITY", 12)

    ui_w = Inches(5.6)
    ui_h = Inches(2.55)

    features = [
        ("Side-by-Side Debate Stream", "Renders Planner, Critic, and Ethics arguments in synchronized columns, allowing candidates to inspect exactly how objections were challenged and answered.", TEAL_PRIMARY, Inches(0.8), Inches(1.6)),
        ("Interactive Dispute Tree Visualizer", "Renders the explicit consensus vs contention nodes (e.g. 6-month intensive vs 2-year part-time degree) so users understand trade-offs at a glance.", BLUE_ACCENT, Inches(6.9), Inches(1.6)),
        ("Calibrated Uncertainty & Risk Gauges", "Real-time risk meters displaying Epistemic Uncertainty U(R), completion drop probabilities, and regional hiring saturation levels.", AMBER_ETHICS, Inches(0.8), Inches(4.35)),
        ("Human-in-the-Loop Override Panel", "Interactive control drawer allowing candidates to veto specific steps, select persona priorities, or inject personal constraints before finalization.", NAVY_HEAD, Inches(6.9), Inches(4.35))
    ]

    for title_f, desc_f, col_f, l_f, t_f in features:
        add_card(s12, l_f, t_f, ui_w, ui_h, title_f, col_f, top_accent=col_f)
        tb = s12.shapes.add_textbox(l_f + Inches(0.2), t_f + Inches(0.6), ui_w - Inches(0.4), ui_h - Inches(0.7))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = desc_f
        p.font.name = FONT_FAMILY
        p.font.size = Pt(11.5)
        p.font.color.rgb = TEXT_MAIN

    s12.notes_slide.notes_text_frame.text = (
        "Our Streamlit UI is built specifically around cognitive forcing and transparency. "
        "Candidates see the debate stream side-by-side, inspect the dispute tree, view calibrated risk meters, "
        "and have full override power over every recommendation."
    )

    # =========================================================================
    # SLIDE 13: Local Privacy-First Infrastructure
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    apply_slide_bg(s13, BG_LIGHT)
    add_header(s13, "Local Privacy-Preserving Architecture", "DEPLOYMENT & SECURITY", 13)

    infra_w = Inches(3.64)
    infra_h = Inches(5.3)

    # 1. Local Qwen
    add_card(s13, Inches(0.8), Inches(1.6), infra_w, infra_h, "1. 100% On-Premise Inference", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb1 = s13.shapes.add_textbox(Inches(1.0), Inches(2.2), infra_w - Inches(0.4), infra_h - Inches(0.7))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    q_pts = [
        "Local LLM Engine: Powered by Qwen (Qwen2.5-7B / 14B) running on local Ollama or vLLM.",
        "Zero Cloud Leaks: Resumes, personal salaries, demographic data, and career goals never leave local storage.",
        "Deterministic Seed Control: Enables reproducible debate traces for scientific auditing."
    ]
    for pt in q_pts:
        p = tf1.add_paragraph() if tf1.paragraphs[0].text else tf1.paragraphs[0]
        p.text = "• " + pt
        p.font.name = FONT_FAMILY
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(6)

    # 2. Local Knowledge Graph
    add_card(s13, Inches(4.84), Inches(1.6), infra_w, infra_h, "2. Self-Hosted Neo4j Graph", BLUE_ACCENT, top_accent=BLUE_ACCENT)
    tb2 = s13.shapes.add_textbox(Inches(5.04), Inches(2.2), infra_w - Inches(0.4), infra_h - Inches(0.7))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    n_pts = [
        "Neo4j Community Edition: Runs entirely locally in Docker or bare metal.",
        "Pre-indexed O*NET/ESCO: Instant Cypher query response times (< 15ms) for prerequisite validation.",
        "Zero API Ingestion Costs: Decoupled from proprietary cloud graph databases."
    ]
    for pt in n_pts:
        p = tf2.add_paragraph() if tf2.paragraphs[0].text else tf2.paragraphs[0]
        p.text = "• " + pt
        p.font.name = FONT_FAMILY
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(6)

    # 3. Local Vector & UI
    add_card(s13, Inches(8.88), Inches(1.6), infra_w, infra_h, "3. Lightweight Local Vector & UI", NAVY_HEAD, top_accent=NAVY_HEAD)
    tb3 = s13.shapes.add_textbox(Inches(9.08), Inches(2.2), infra_w - Inches(0.4), infra_h - Inches(0.7))
    tf3 = tb3.text_frame
    tf3.word_wrap = True
    v_pts = [
        "Embedded Vector Store: Chroma / FAISS persistence stored locally without external telemetry.",
        "Quantized Embeddings: High efficiency sentence-transformers executing on consumer GPUs or CPUs.",
        "Streamlit Dashboard: Fast, reactive, responsive interface running on localhost."
    ]
    for pt in v_pts:
        p = tf3.add_paragraph() if tf3.paragraphs[0].text else tf3.paragraphs[0]
        p.text = "• " + pt
        p.font.name = FONT_FAMILY
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(6)

    s13.notes_slide.notes_text_frame.text = (
        "Privacy is paramount for career data. Our system runs 100% on-premise: "
        "Qwen local models via Ollama, local Neo4j Community Edition, and local FAISS vector stores. "
        "No confidential candidate data or corporate resumes ever hit commercial cloud APIs."
    )

    # =========================================================================
    # SLIDE 14: Conclusion & Strategic Takeaways (Dark Hero Closing)
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    apply_slide_bg(s14, BG_DARK)

    # Header Kicker
    s14_kicker = s14.shapes.add_textbox(Inches(1.0), Inches(0.8), Inches(11.333), Inches(0.4))
    kp = s14_kicker.text_frame.paragraphs[0]
    kp.text = "CONCLUSION & STRATEGIC IMPACT".upper()
    kp.font.name = FONT_FAMILY
    kp.font.size = Pt(11)
    kp.font.bold = True
    kp.font.color.rgb = TEAL_ACCENT

    # Title
    s14_t = s14.shapes.add_textbox(Inches(1.0), Inches(1.2), Inches(11.333), Inches(1.2))
    p_st = s14_t.text_frame.paragraphs[0]
    p_st.text = "Pioneering Responsible AI for High-Stakes Career Guidance"
    p_st.font.name = FONT_FAMILY
    p_st.font.size = Pt(28)
    p_st.font.bold = True
    p_st.font.color.rgb = TEXT_WHITE

    # 4 Pillar Cards
    p_w14 = Inches(2.7)
    p_h14 = Inches(4.3)
    c14_data = [
        ("Eliminates Sycophancy", "Replaces single-agent pleasantries with rigorous adversarial cross-examination across 3 complementary personas.", TEAL_PRIMARY),
        ("Hybrid Graph Grounding", "Integrates deterministic Neo4j skill DAGs with dense vector course data to eliminate prerequisite hallucinations.", BLUE_ACCENT),
        ("Calibrated Self-Awareness", "Replaces false certainty with calibrated epistemic uncertainty U(R) and explicit dispute graphs.", AMBER_ETHICS),
        ("Preserves Human Agency", "Enforces cognitive forcing functions and interactive override gates, eliminating automation complacency.", ROSE_CRITIC)
    ]
    for i, (head14, body14, col14) in enumerate(c14_data):
        l14 = Inches(1.0) + Inches(i * 2.88)
        card14, _ = add_card(s14, l14, Inches(2.5), p_w14, p_h14, head14, col14, top_accent=col14, bg_color=RGBColor(17, 24, 39), border_color=RGBColor(31, 41, 55))
        
        tb = s14.shapes.add_textbox(l14 + Inches(0.15), Inches(3.2), p_w14 - Inches(0.3), p_h14 - Inches(0.9))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = body14
        p.font.name = FONT_FAMILY
        p.font.size = Pt(11.5)
        p.font.color.rgb = RGBColor(203, 213, 225)

    s14.notes_slide.notes_text_frame.text = (
        "In conclusion, this project provides a concrete, reproducible blueprint for Responsible AI in career advisory. "
        "By replacing monolithic prompting with dialectic multi-agent debate, grounding on knowledge graphs, "
        "calibrating uncertainty, and safeguarding human agency, we turn AI from a dangerous sycophant into a trustworthy decision partner. "
        "Thank you, and I look forward to your questions."
    )

    # Save presentation to both professional filename and original filename
    out_pro = "/home/thor/Desktop/RAI Project/Debate_Career_Guidance_Agent_Professional.pptx"
    out_pres = "/home/thor/Desktop/RAI Project/Debate_Career_Guidance_Agent_Presentation.pptx"
    prs.save(out_pro)
    prs.save(out_pres)
    print(f"Professional presentation saved successfully to:\n- {out_pro}\n- {out_pres}")

if __name__ == "__main__":
    build_presentation()
