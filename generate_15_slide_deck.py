#!/usr/bin/env python3
"""
Master Academic Presentation Generator (15 Slides)
Debate-Based Career Guidance Agent with Complementary Personas
Inspired by Presenton's Executive Design Architecture & The Antigravity Presentation Designer Standard

Constraints:
- Exactly 15 slides (Maximum 15 pages)
- In-depth theoretical rigor & complete empirical numerical results
- Corporate/Academic Executive aesthetic (16:9 widescreen, clean cards, KPI metrics, badges)
- Verified Faculty & Industry Mentors, Authors, Department, and University
- Complete presenter notes for every slide
"""

import os
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt


def build_deck(output_pptx="docs/FINAL_PRESENTATION_15_SLIDES.pptx"):
    os.makedirs(os.path.dirname(output_pptx), exist_ok=True)
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Executive Palette (60-30-10 Rule)
    DARK_BG = RGBColor(15, 23, 42)          # Slate 900
    LIGHT_BG = RGBColor(248, 250, 252)      # Slate 50
    CARD_BG = RGBColor(255, 255, 255)       # White
    CARD_BORDER = RGBColor(203, 213, 225)   # Slate 300
    CARD_MUTED = RGBColor(241, 245, 249)    # Slate 100

    NAVY_HEAD = RGBColor(15, 23, 42)        # Slate 900
    NAVY_PRIMARY = RGBColor(30, 41, 59)     # Slate 800
    TEAL_PRIMARY = RGBColor(13, 148, 136)   # Teal 600
    TEAL_ACCENT = RGBColor(20, 184, 166)    # Teal 500
    TEAL_BG = RGBColor(240, 253, 250)       # Teal 50
    BLUE_ACCENT = RGBColor(37, 99, 235)     # Blue 600
    BLUE_BG = RGBColor(239, 246, 255)       # Blue 50
    ROSE_ACCENT = RGBColor(225, 29, 72)     # Rose 600
    ROSE_BG = RGBColor(255, 241, 242)       # Rose 50
    AMBER_ACCENT = RGBColor(217, 119, 6)    # Amber 600
    AMBER_BG = RGBColor(254, 243, 199)      # Amber 100
    INDIGO_ACCENT = RGBColor(79, 70, 229)   # Indigo 600
    INDIGO_BG = RGBColor(238, 242, 255)     # Indigo 50
    EMERALD_ACCENT = RGBColor(5, 150, 105)  # Emerald 600

    TEXT_MAIN = RGBColor(51, 65, 85)        # Slate 700
    TEXT_MUTED = RGBColor(100, 116, 139)    # Slate 500
    TEXT_WHITE = RGBColor(255, 255, 255)

    FONT_FAMILY = "Liberation Sans"
    TOTAL_SLIDES = 15

    def set_bg(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_header(slide, title, category, slide_num, takeaway=""):
        tag = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.30), Inches(4.5), Inches(0.26))
        tag.fill.solid()
        tag.fill.fore_color.rgb = TEAL_BG
        tag.line.color.rgb = TEAL_PRIMARY
        tag.line.width = Pt(1)
        tp = tag.text_frame.paragraphs[0]
        tp.text = category.upper()
        tp.font.name = FONT_FAMILY
        tp.font.size = Pt(8.5)
        tp.font.bold = True
        tp.font.color.rgb = TEAL_PRIMARY
        tp.alignment = PP_ALIGN.CENTER
        tag.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

        tb_t = slide.shapes.add_textbox(Inches(0.8), Inches(0.58), Inches(11.733), Inches(0.42))
        p = tb_t.text_frame.paragraphs[0]
        p.text = title
        p.font.name = FONT_FAMILY
        p.font.size = Pt(20)
        p.font.bold = True
        p.font.color.rgb = NAVY_HEAD

        if takeaway:
            tb_sub = slide.shapes.add_textbox(Inches(0.8), Inches(1.00), Inches(11.733), Inches(0.28))
            p_sub = tb_sub.text_frame.paragraphs[0]
            p_sub.text = takeaway
            p_sub.font.name = FONT_FAMILY
            p_sub.font.size = Pt(10.5)
            p_sub.font.color.rgb = TEXT_MUTED

        tb_n = slide.shapes.add_textbox(Inches(11.5), Inches(0.30), Inches(1.033), Inches(0.28))
        pn = tb_n.text_frame.paragraphs[0]
        pn.text = f"{slide_num:02d} / {TOTAL_SLIDES}"
        pn.font.name = FONT_FAMILY
        pn.font.size = Pt(9.5)
        pn.font.bold = True
        pn.font.color.rgb = TEXT_MUTED
        pn.alignment = PP_ALIGN.RIGHT

    def add_card(slide, left, top, width, height, title="", title_color=NAVY_HEAD, bg_color=CARD_BG, border_color=CARD_BORDER, top_accent=None, title_size=12.5):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1)

        if top_accent:
            bar = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, Inches(0.06))
            bar.fill.solid()
            bar.fill.fore_color.rgb = top_accent
            bar.line.fill.background()

        if title:
            tb = slide.shapes.add_textbox(left + Inches(0.16), top + Inches(0.10), width - Inches(0.32), Inches(0.32))
            p = tb.text_frame.paragraphs[0]
            p.text = title
            p.font.name = FONT_FAMILY
            p.font.size = Pt(title_size)
            p.font.bold = True
            p.font.color.rgb = title_color
            tb.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

        return card

    def add_bullet(tf, bold_prefix, text, pt_size=10.8, space_after=4, bold_color=NAVY_PRIMARY, norm_color=TEXT_MAIN):
        p = tf.add_paragraph() if len(tf.paragraphs[0].text) > 0 else tf.paragraphs[0]
        p.space_after = Pt(space_after)
        if bold_prefix:
            r1 = p.add_run()
            r1.text = bold_prefix + " "
            r1.font.name = FONT_FAMILY
            r1.font.bold = True
            r1.font.size = Pt(pt_size)
            r1.font.color.rgb = bold_color
        r2 = p.add_run()
        r2.text = text
        r2.font.name = FONT_FAMILY
        r2.font.bold = False
        r2.font.size = Pt(pt_size)
        r2.font.color.rgb = norm_color

    def add_notes(slide, text):
        notes_slide = slide.notes_slide
        tf = notes_slide.notes_text_frame
        tf.text = text

    # =========================================================================
    # SLIDE 1: Title Slide (Executive Dark)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_bg(s1, DARK_BG)

    badge = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.8), Inches(4.8), Inches(0.35))
    badge.fill.solid()
    badge.fill.fore_color.rgb = RGBColor(30, 41, 59)
    badge.line.color.rgb = TEAL_ACCENT
    badge.line.width = Pt(1)
    bp = badge.text_frame.paragraphs[0]
    bp.text = "RESPONSIBLE ARTIFICIAL INTELLIGENCE IN EDUCATION"
    bp.font.name = FONT_FAMILY
    bp.font.size = Pt(9.0)
    bp.font.bold = True
    bp.font.color.rgb = TEAL_ACCENT
    bp.alignment = PP_ALIGN.CENTER
    badge.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    tb1 = s1.shapes.add_textbox(Inches(0.8), Inches(1.3), Inches(11.733), Inches(1.6))
    p1 = tb1.text_frame.paragraphs[0]
    p1.text = "Debate-Based Career Guidance Agent\nwith Complementary Personas"
    p1.font.name = FONT_FAMILY
    p1.font.size = Pt(30)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE

    tb1_sub = s1.shapes.add_textbox(Inches(0.8), Inches(3.05), Inches(11.733), Inches(0.6))
    p1_sub = tb1_sub.text_frame.paragraphs[0]
    p1_sub.text = "A Grounded Multi-Agent Architecture with Prerequisite Knowledge Graph Verification, Calibrated Uncertainty, and Cognitive Forcing"
    p1_sub.font.name = FONT_FAMILY
    p1_sub.font.size = Pt(13)
    p1_sub.font.color.rgb = RGBColor(148, 163, 184)

    div = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(3.85), Inches(11.733), Inches(0.02))
    div.fill.solid()
    div.fill.fore_color.rgb = RGBColor(51, 65, 85)
    div.line.fill.background()

    # Author Card
    c_auth = add_card(s1, Inches(0.8), Inches(4.1), Inches(5.6), Inches(2.0), title="Student Research Team", title_color=TEAL_ACCENT, bg_color=RGBColor(30, 41, 59), border_color=RGBColor(51, 65, 85), title_size=12)
    tf_auth = s1.shapes.add_textbox(Inches(1.0), Inches(4.55), Inches(5.2), Inches(1.4)).text_frame
    add_bullet(tf_auth, "Authors:", "Gedela Rishikesh Reddy, Aniket Srivastava, Parth Gupta", pt_size=11, norm_color=TEXT_WHITE)
    add_bullet(tf_auth, "Department:", "Computing Technologies", pt_size=10.5, norm_color=RGBColor(203, 213, 225))
    add_bullet(tf_auth, "Institution:", "SRM Institute of Science and Technology", pt_size=10.5, norm_color=RGBColor(203, 213, 225))

    # Mentors & Stack Card
    c_ment = add_card(s1, Inches(6.8), Inches(4.1), Inches(5.733), Inches(2.0), title="Project Mentorship & Runtime Stack", title_color=BLUE_ACCENT, bg_color=RGBColor(30, 41, 59), border_color=RGBColor(51, 65, 85), title_size=12)
    tf_ment = s1.shapes.add_textbox(Inches(7.0), Inches(4.55), Inches(5.333), Inches(1.4)).text_frame
    add_bullet(tf_ment, "Faculty Mentor:", "Dr. P. Akilandeswari", pt_size=11, bold_color=RGBColor(147, 197, 253), norm_color=TEXT_WHITE)
    add_bullet(tf_ment, "Industry Mentor:", "Pratyush Jha", pt_size=11, bold_color=RGBColor(147, 197, 253), norm_color=TEXT_WHITE)
    add_bullet(tf_ment, "Core Stack:", "Qwen Local (7B) • Python Harness • Neo4j / NetworkX DAG • ChromaDB • Streamlit", pt_size=10, norm_color=RGBColor(203, 213, 225))

    add_notes(s1, "Good morning respected committee members and mentors. Today we present our research on a Debate-Based Career Guidance Agent using Complementary Personas and deterministic Knowledge Graph Verification. Our architecture addresses the critical hazards of unconstrained LLMs in educational advising by introducing dialectic debate, calibrated uncertainty, and human-in-the-loop cognitive forcing.")

    # =========================================================================
    # SLIDE 2: Problem Statement & Advisory Hazards
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_bg(s2, LIGHT_BG)
    add_header(s2, "Why Monolithic LLMs Fail in Career Advising", "Section 1: Problem Formulation", 2, "Unconstrained generative chatbots exhibit systemic failure modes that jeopardize student career trajectories.")

    # 4 Cards for Hazards
    w4 = Inches(2.78)
    h4 = Inches(5.6)
    t4 = Inches(1.45)

    c1 = add_card(s2, Inches(0.8), t4, w4, h4, title="Conversational Sycophancy", title_color=ROSE_ACCENT, top_accent=ROSE_ACCENT)
    tf1 = s2.shapes.add_textbox(Inches(0.95), t4 + Inches(0.45), w4 - Inches(0.3), h4 - Inches(0.6)).text_frame
    add_bullet(tf1, "The Trap:", "Standard LLMs maximize conversational agreement and praise rather than truthfulness.")
    add_bullet(tf1, "Observed Behavior:", "Affirms impossible student targets, such as mastering Senior MLOps in 60 days with only basic Python.")
    add_bullet(tf1, "Consequence:", "Students enter specialized job interviews grossly underprepared, resulting in early interview screening failure.")

    c2 = add_card(s2, Inches(3.78), t4, w4, h4, title="Prerequisite Skipping", title_color=AMBER_ACCENT, top_accent=AMBER_ACCENT)
    tf2 = s2.shapes.add_textbox(Inches(3.93), t4 + Inches(0.45), w4 - Inches(0.3), h4 - Inches(0.6)).text_frame
    add_bullet(tf2, "The Trap:", "LLM next-token generation hallucinates plausible-sounding courses without checking dependency graphs.")
    add_bullet(tf2, "Observed Behavior:", "Recommends Deep Learning and Transformer fine-tuning before Linear Algebra or Multivariable Calculus.")
    add_bullet(tf2, "Baseline Metric:", "Monolithic LLM exhibits a staggering 90.9% prerequisite violation rate across curriculum paths.")

    c3 = add_card(s2, Inches(6.76), t4, w4, h4, title="Predatory Debt Steering", title_color=INDIGO_ACCENT, top_accent=INDIGO_ACCENT)
    tf3 = s2.shapes.add_textbox(Inches(6.91), t4 + Inches(0.45), w4 - Inches(0.3), h4 - Inches(0.6)).text_frame
    add_bullet(tf3, "The Trap:", "Pretraining corpora heavily over-represent commercial bootcamp marketing and paid sponsorships.")
    add_bullet(tf3, "Observed Behavior:", "Advises low-income students (₹3,000/month budget) to take ₹1,20,000 high-interest commercial bootcamp loans.")
    add_bullet(tf3, "Consequence:", "Pushes vulnerable students into predatory educational debt when free open courseware is readily available.")

    c4 = add_card(s2, Inches(9.74), t4, w4, h4, title="Institutional Pedigree Bias", title_color=BLUE_ACCENT, top_accent=BLUE_ACCENT)
    tf4 = s2.shapes.add_textbox(Inches(9.89), t4 + Inches(0.45), w4 - Inches(0.3), h4 - Inches(0.6)).text_frame
    add_bullet(tf4, "The Trap:", "Historical data embeds deep socio-economic stereotyping regarding college tiers.")
    add_bullet(tf4, "Observed Behavior:", "When skills are 100% identical, steers Tier-1 students to ML Engineering, but Tier-3 students to IT helpdesk support.")
    add_bullet(tf4, "Baseline Fairness:", "Monolithic LLM achieves a dismal Jaccard curriculum similarity of J = 0.32 between matched pairs.")

    add_notes(s2, "Slide 2 outlines the 4 critical failure modes observed in single-prompt LLM career counselors: Sycophancy, Prerequisite Skipping, Predatory Debt Steering, and Institutional Pedigree Bias. Unconstrained models lack a grounding mechanism, resulting in 90.9% prerequisite errors and deep socio-economic bias.")

    # =========================================================================
    # SLIDE 3: Theoretical Foundations & Literature Survey
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_bg(s3, LIGHT_BG)
    add_header(s3, "Three Theoretical Pillars of Responsible Advisory", "Section 2: Theoretical Foundations", 3, "Bridging Multi-Agent Dialectics, Public Knowledge Grounding, and Cognitive Forcing.")

    w3 = Inches(3.78)
    h3 = Inches(5.6)
    t3 = Inches(1.45)

    p1 = add_card(s3, Inches(0.8), t3, w3, h3, title="1. Multi-Agent Dialectics", title_color=TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tf_p1 = s3.shapes.add_textbox(Inches(0.96), t3 + Inches(0.45), w3 - Inches(0.32), h3 - Inches(0.6)).text_frame
    add_bullet(tf_p1, "Foundational Literature:", "Du et al. (2023) 'Improving Factuality via Multi-Agent Debate'; Liang et al. (2023) 'Encouraging Divergent Thinking'.")
    add_bullet(tf_p1, "Philosophical Root:", "Hegelian dialectic structure (Thesis: Planner, Antithesis: Critic, Synthesis: Moderator).")
    add_bullet(tf_p1, "Mechanism:", "Splitting reasoning into specialized, adversarial personas forces divergent arguments to surface rather than collapsing into single-prompt average probabilities.")
    add_bullet(tf_p1, "Key Benefit:", "Forces explicit trade-off exploration between speed and foundational rigor.")

    p2 = add_card(s3, Inches(4.78), t3, w3, h3, title="2. Public Knowledge Grounding", title_color=BLUE_ACCENT, top_accent=BLUE_ACCENT)
    tf_p2 = s3.shapes.add_textbox(Inches(4.94), t3 + Inches(0.45), w3 - Inches(0.32), h3 - Inches(0.6)).text_frame
    add_bullet(tf_p2, "Foundational Standards:", "ACM/IEEE CS2023 Curricular Guidelines for Undergraduate Degree Programs; U.S. Dept of Labor O*NET Standard Occupational Taxonomy.")
    add_bullet(tf_p2, "Retrieval Principle:", "Lewis et al. (2020) Retrieval-Augmented Generation (RAG).")
    add_bullet(tf_p2, "Mechanism:", "Grounding personas strictly in accredited course syllabi (MIT OCW, CS50, Berkeley CS61) and empirical hiring requirements.")
    add_bullet(tf_p2, "Key Benefit:", "Prevents the model from hallucinating proprietary courses or unverified corporate certifications.")

    p3 = add_card(s3, Inches(8.76), t3, w3, h3, title="3. Cognitive Forcing & Agency", title_color=INDIGO_ACCENT, top_accent=INDIGO_ACCENT)
    tf_p3 = s3.shapes.add_textbox(Inches(8.92), t3 + Inches(0.45), w3 - Inches(0.32), h3 - Inches(0.6)).text_frame
    add_bullet(tf_p3, "Foundational Literature:", "Buçinca et al. (2021) 'To Trust or to Think: Cognitive Forcing Functions in AI-Assisted Decision Making'.")
    add_bullet(tf_p3, "Decision Psychology:", "Kahneman (2011) System 1 (heuristic fast acceptance) vs. System 2 (deliberative analytical thinking).")
    add_bullet(tf_p3, "Mechanism:", "When calibrated uncertainty U >= 0.45 or prerequisite violations occur, autonomous release is blocked; student must engage with Dispute Tree sliders.")
    add_bullet(tf_p3, "Key Benefit:", "Restores genuine student agency without passive overreliance on AI recommendations.")

    add_notes(s3, "Slide 3 grounds our research in three established theoretical bodies: Hegelian multi-agent dialectics from Du and Liang et al., curriculum grounding via ACM/IEEE CS2023 and O*NET standards, and cognitive forcing functions from Bucinca et al. to prevent passive student overreliance.")

    # =========================================================================
    # SLIDE 4: Countering Critiques of Multi-Agent Debate
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_bg(s4, LIGHT_BG)
    add_header(s4, "Overcoming Agreement Collapse & The Woozle Effect", "Section 2: Literature Survey & Defense", 4, "Directly resolving the core failure modes exposed by Smit et al. (2024).")

    w_crit = Inches(5.7)
    h_crit = Inches(5.6)
    t_crit = Inches(1.45)

    c_left = add_card(s4, Inches(0.8), t_crit, w_crit, h_crit, title="The Academic Critique: Smit et al. (2024)", title_color=ROSE_ACCENT, top_accent=ROSE_ACCENT)
    tf_cl = s4.shapes.add_textbox(Inches(1.0), t_crit + Inches(0.45), w_crit - Inches(0.4), h_crit - Inches(0.6)).text_frame
    add_bullet(tf_cl, "The Paper:", "'Should We Be Going MAD? Multi-Agent Debate and Consensus Failure' (EMNLP 2024).")
    add_bullet(tf_cl, "Core Vulnerability 1 (Agreement Collapse):", "Debating agents sharing the same base model weights rapidly converge toward superficial harmony, smoothing away genuine contradictions into unprincipled compromises.")
    add_bullet(tf_cl, "Core Vulnerability 2 (The Woozle Effect):", "When an early agent asserts an unfounded claim, peer agents frequently amplify and validate the mistake, cascading hallucinations across rounds.")
    add_bullet(tf_cl, "Core Vulnerability 3 (Majority Voting Flaw):", "Unmoderated voting assumes independent errors; however, shared pretraining priors produce correlated systemic blindspots.")

    c_right = add_card(s4, Inches(6.8), t_crit, w_crit, h_crit, title="Our Architectural Invariants & Solutions", title_color=EMERALD_ACCENT, top_accent=EMERALD_ACCENT)
    tf_cr = s4.shapes.add_textbox(Inches(7.0), t_crit + Inches(0.45), w_crit - Inches(0.4), h_crit - Inches(0.6)).text_frame
    add_bullet(tf_cr, "Invariant 1: Asymmetric Persona Temperatures:", "We decouple priors by assigning distinct temperatures (Planner T = 0.3 for structured planning; Critic T = 0.6 for aggressive adversarial scrutiny).")
    add_bullet(tf_cr, "Invariant 2: Deterministic 42-Node DAG Anchor:", "Personas cannot validate arbitrary milestones. Graph reachability is checked externally via NetworkX in O(|V|+|E|) time, mathematically breaking the Woozle Effect.")
    add_bullet(tf_cr, "Invariant 3: Structured Dispute Trees:", "We explicitly abandon forced consensus. Disagreements are compiled into explicit Dispute Trees, exposing trade-offs for student resolution.")
    add_bullet(tf_cr, "Empirical Validation:", "Unmoderated debate (Config 3) had 86.4% prerequisite errors; our proposed system (Config 4) achieved strictly 0.0%.")

    add_notes(s4, "Slide 4 is crucial for our academic defense. We directly address the prominent EMNLP 2024 critique by Smit et al. titled 'Should We Be Going MAD?'. We demonstrate how our decoupled inference temperatures, external knowledge graph anchor, and explicit dispute trees eliminate agreement collapse and the Woozle effect.")

    # =========================================================================
    # SLIDE 5: End-to-End System Architecture
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_bg(s5, LIGHT_BG)
    add_header(s5, "End-to-End Decision Flow Architecture", "Section 3: System Architecture", 5, "Candidate Intake -> Dense Retrieval -> Persona Debate -> Moderator Synthesis -> Graph Verification -> Cognitive Gate.")

    # 6-Step Process Grid
    w_box = Inches(1.8)
    h_box = Inches(3.6)
    t_box = Inches(1.5)
    spacing = Inches(0.18)

    steps = [
        ("1. Candidate Intake", "Student profile intake: technical skills, target role, monthly budget, timeline constraints.", BLUE_ACCENT, BLUE_BG),
        ("2. Dense Retrieval", "ChromaDB indexes 15 ACM CS2023 course syllabi and 8 O*NET role profiles with metadata.", TEAL_PRIMARY, TEAL_BG),
        ("3. Persona Triad", "Planner (milestones), Critic (systems & math gaps), Ethics (zero-debt & pedigree audit).", INDIGO_ACCENT, INDIGO_BG),
        ("4. Moderator Agent", "Synthesizes roadmaps, constructs Dispute Tree, and calculates calibrated uncertainty U.", AMBER_ACCENT, AMBER_BG),
        ("5. 42-Node DAG", "Deterministic NetworkX prerequisite check flags milestone order violations (Delta_prereq).", ROSE_ACCENT, ROSE_BG),
        ("6. Cognitive Gate", "Blocks release if U >= 0.45 or Delta >= 1; activates Streamlit sliders for student override.", EMERALD_ACCENT, TEAL_BG),
    ]

    for i, (title, desc, accent, bg) in enumerate(steps):
        x = Inches(0.8) + i * (w_box + spacing)
        b = add_card(s5, x, t_box, w_box, h_box, title=title, title_color=accent, bg_color=bg, border_color=accent, top_accent=accent, title_size=10.5)
        tf = s5.shapes.add_textbox(x + Inches(0.1), t_box + Inches(0.45), w_box - Inches(0.2), h_box - Inches(0.6)).text_frame
        add_bullet(tf, "", desc, pt_size=9.8, norm_color=TEXT_MAIN)

    # Lower Architecture Summary Card
    c_bot = add_card(s5, Inches(0.8), Inches(5.3), Inches(11.733), Inches(1.7), title="Architectural Safety Guarantees", title_color=NAVY_HEAD, top_accent=NAVY_PRIMARY)
    tf_bot = s5.shapes.add_textbox(Inches(1.0), Inches(5.65), Inches(11.333), Inches(1.2)).text_frame
    add_bullet(tf_bot, "Local Privacy & Zero Cloud Exposure:", "Runs entirely on-device via local Qwen 2.5 7B with zero external API calls, protecting sensitive student educational data.", pt_size=10.5)
    add_bullet(tf_bot, "Deterministic Verification Separation:", "Advisory reasoning is separated into non-deterministic semantic generation (LLM) and deterministic structural verification (DAG).", pt_size=10.5)

    add_notes(s5, "Slide 5 details our end-to-end operational pipeline. From student intake and ChromaDB retrieval to three-agent deliberation, moderator synthesis, deterministic graph verification, and the interactive cognitive forcing gate. Advisory generation and structural verification remain strictly decoupled.")

    # =========================================================================
    # SLIDE 6: Complementary Persona Specifications
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_bg(s6, LIGHT_BG)
    add_header(s6, "The Dialectic Triad: Roles & Operational Constraints", "Section 3: Persona Specifications", 6, "Planner, Critic, and Ethics-Reviewer operating under asymmetric temperatures.")

    w_tri = Inches(3.78)
    h_tri = Inches(5.6)
    t_tri = Inches(1.45)

    c_plan = add_card(s6, Inches(0.8), t_tri, w_tri, h_tri, title="The Planner Persona (T = 0.3)", title_color=BLUE_ACCENT, top_accent=BLUE_ACCENT)
    tf_plan = s6.shapes.add_textbox(Inches(0.96), t_tri + Inches(0.45), w_tri - Inches(0.32), h_tri - Inches(0.6)).text_frame
    add_bullet(tf_plan, "Core Mission:", "Constructive curriculum architecture and sequential milestone formulation.")
    add_bullet(tf_plan, "Behavioral Mandate:", "Translates raw career ambitions into realistic quarterly learning objectives, practical projects, and verifiable technical deliverables.")
    add_bullet(tf_plan, "Knowledge Grounding:", "Adheres to accredited ACM/IEEE CS2023 module credit-hour guidelines.")
    add_bullet(tf_plan, "Inference Setting:", "Operates at T = 0.3 for low entropy, high structural consistency, and reliable formatting.")

    c_crit = add_card(s6, Inches(4.78), t_tri, w_tri, h_tri, title="The Critic Persona (T = 0.6)", title_color=ROSE_ACCENT, top_accent=ROSE_ACCENT)
    tf_crit = s6.shapes.add_textbox(Inches(4.94), t_tri + Inches(0.45), w_tri - Inches(0.32), h_tri - Inches(0.6)).text_frame
    add_bullet(tf_crit, "Core Mission:", "Adversarial auditing, technical screening risk, and prerequisite integrity.")
    add_bullet(tf_crit, "Behavioral Mandate:", "Acts as a cynical technical interviewer. Proactively flags missing mathematical/systems foundations and unrealistic timeline compression.")
    add_bullet(tf_crit, "Target Vulnerabilities:", "Exposes superficial portfolio projects (e.g. copying an API wrapper without understanding backpropagation).")
    add_bullet(tf_crit, "Inference Setting:", "Operates at T = 0.6 for creative counter-arguments and divergent failure hypothesis generation.")

    c_eth = add_card(s6, Inches(8.76), t_tri, w_tri, h_tri, title="The Ethics-Reviewer (T = 0.3)", title_color=EMERALD_ACCENT, top_accent=EMERALD_ACCENT)
    tf_eth = s6.shapes.add_textbox(Inches(8.92), t_tri + Inches(0.45), w_tri - Inches(0.32), h_tri - Inches(0.6)).text_frame
    add_bullet(tf_eth, "Core Mission:", "Zero-debt enforcement, pedigree parity, and genuine student agency.")
    add_bullet(tf_eth, "Behavioral Mandate:", "Strictly audits financial viability. Rejects commercial bootcamps and loan-financed credentials for low-budget profiles.")
    add_bullet(tf_eth, "Pedigree Parity:", "Ensures students from Tier-3 colleges receive identical rigorous core technical recommendations as Tier-1 peers.")
    add_bullet(tf_eth, "Alternative Routing:", "Mandates high-quality open courseware (MIT OpenCourseWare, Harvard CS50, GitHub proof-of-work).")

    add_notes(s6, "Slide 6 defines the operational mandates and prompt configurations of our dialectic triad. The Planner builds constructive milestones at temperature 0.3; the Critic attacks gaps and timeline assumptions at temperature 0.6; and the Ethics-Reviewer guarantees financial safety and institutional fairness.")

    # =========================================================================
    # SLIDE 7: The 42-Node Knowledge Graph
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_bg(s7, LIGHT_BG)
    add_header(s7, "The 42-Node Prerequisite Knowledge Graph", "Section 4: Knowledge Graph Engineering", 7, "A deterministic DAG spanning 9 CS domains with automated Neo4j Cypher synchronization.")

    w_kg = Inches(5.7)
    h_kg = Inches(5.6)
    t_kg = Inches(1.45)

    c_tax = add_card(s7, Inches(0.8), t_kg, w_kg, h_kg, title="Taxonomy & Prerequisite Structure", title_color=NAVY_HEAD, top_accent=NAVY_PRIMARY)
    tf_tax = s7.shapes.add_textbox(Inches(1.0), t_kg + Inches(0.45), w_kg - Inches(0.4), h_kg - Inches(0.6)).text_frame
    add_bullet(tf_tax, "Node Coverage (42 Total Nodes):", "Covers 9 core ACM/IEEE CS2023 domains:")
    add_bullet(tf_tax, "1. Foundations (3):", "Discrete Math, Linear Algebra, Probability & Statistics.")
    add_bullet(tf_tax, "2. Programming Core (5):", "Python Basics, Python OOP, C Basics, Pointers & Memory, Java.")
    add_bullet(tf_tax, "3. Systems & Architecture (7):", "Computer Architecture, OS Internals, Concurrency, Linux/POSIX, Networking, Distributed Systems, System Design.")
    add_bullet(tf_tax, "4. Databases & Storage (4):", "RDBMS, SQL Optimization, Indexing/Normalization, NoSQL.")
    add_bullet(tf_tax, "5. Web & Engineering (4):", "HTML/CSS, JavaScript, Backend Frameworks, REST APIs.")
    add_bullet(tf_tax, "6. Machine Learning (7):", "Data Wrangling, ML Foundations, Deep Learning, NLP/Transformers, LLMs/RAG, MLOps, AI Ethics.")
    add_bullet(tf_tax, "7. Security & Cloud (8):", "DSA (3), DevOps/Cloud (4), Security & Mobile (5).")
    add_bullet(tf_tax, "Validated Edges (47 Edges):", "Directed dependencies (e.g. Linear Algebra -> ML Foundations -> Deep Learning).")

    c_tra = add_card(s7, Inches(6.8), t_kg, w_kg, h_kg, title="Deterministic Traversal & Neo4j Export", title_color=INDIGO_ACCENT, top_accent=INDIGO_ACCENT)
    tf_tra = s7.shapes.add_textbox(Inches(7.0), t_kg + Inches(0.45), w_kg - Inches(0.4), h_kg - Inches(0.6)).text_frame
    add_bullet(tf_tra, "Mathematical Violation Formulation:", "A milestone v violates prerequisite ordering if prerequisite u is neither completed nor scheduled earlier:")
    add_bullet(tf_tra, "Delta_prereq:", "|{ (u, v) in E_prereq : v in M and u not in (S_curr union M_<v) }|", pt_size=10.0, bold_color=ROSE_ACCENT)
    add_bullet(tf_tra, "Runtime Complexity:", "Evaluated via NetworkX topological sorting in deterministic O(|V| + |E|) time (< 0.2 milliseconds).")
    add_bullet(tf_tra, "Why In-Memory NetworkX:", "Sub-millisecond traversal without external socket overhead or JVM server footprint on student hardware.")
    add_bullet(tf_tra, "Dual-Mode Neo4j Integration:", "Includes automated Cypher query generator (sync_to_neo4j) allowing the exact same 42-node graph to synchronize with enterprise Neo4j databases.")

    add_notes(s7, "Slide 7 outlines the 42-node prerequisite knowledge graph. Spanning 9 computer science domains with 47 directed edges, our NetworkX engine checks topological reachability in under 0.2 milliseconds. We also support seamless synchronization with Neo4j via automated Cypher query exports.")

    # =========================================================================
    # SLIDE 8: Dispute Tree & Cognitive Forcing Gate
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_bg(s8, LIGHT_BG)
    add_header(s8, "Dispute Trees, Calibrated Risk, and Human Override", "Section 4: Mediation & Human Agency", 8, "Structuring disagreements and restoring student decision autonomy through interactive sliders.")

    w_disp = Inches(5.7)
    h_disp = Inches(5.6)
    t_disp = Inches(1.45)

    c_form = add_card(s8, Inches(0.8), t_disp, w_disp, h_disp, title="Calibrated Uncertainty Formulation (U_cal)", title_color=AMBER_ACCENT, top_accent=AMBER_ACCENT)
    tf_form = s8.shapes.add_textbox(Inches(1.0), t_disp + Inches(0.45), w_disp - Inches(0.4), h_disp - Inches(0.6)).text_frame
    add_bullet(tf_form, "Mathematical Formulation:", "The Moderator calculates calibrated risk via weighted linear combination across four advisory friction dimensions:")
    add_bullet(tf_form, "U_cal =", "0.30 * F_triad + 0.35 * Delta_prereq + 0.20 * R_socio + 0.15 * R_timeline", pt_size=10.5, bold_color=AMBER_ACCENT)
    add_bullet(tf_form, "F_triad (Persona Friction):", "Disagreement index across Planner, Critic, and Ethics (0.0 to 1.0).")
    add_bullet(tf_form, "Delta_prereq (Graph Violations):", "Normalized prerequisite sequence errors from the 42-node DAG.")
    add_bullet(tf_form, "R_socio (Socio-Economic Risk):", "Financial exposure index when commercial options threaten student budget.")
    add_bullet(tf_form, "R_timeline (Compression Risk):", "Timeline compression index when requested months are under curriculum requirements.")
    add_bullet(tf_form, "Trigger Invariant:", "If U_cal >= 0.45 or Delta_prereq >= 1, autonomous roadmap release is halted.")

    c_tree = add_card(s8, Inches(6.8), t_disp, w_disp, h_disp, title="Dispute Tree & Student Slider Controls", title_color=TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tf_tree = s8.shapes.add_textbox(Inches(7.0), t_disp + Inches(0.45), w_disp - Inches(0.4), h_disp - Inches(0.6)).text_frame
    add_bullet(tf_tree, "Dispute Tree Structure:", "Rather than hiding dissensus, the Moderator maps active debate friction into three explicit student trade-off nodes:")
    add_bullet(tf_tree, "Trade-off 1 (Speed vs. Rigor):", "Rushing immediate portfolio projects vs. spending 8 weeks mastering foundational algorithms.")
    add_bullet(tf_tree, "Trade-off 2 (Debt vs. Open Source):", "Borrowing for a private commercial bootcamp vs. completing MIT OpenCourseWare + GitHub proof-of-work.")
    add_bullet(tf_tree, "Trade-off 3 (Placement vs. Proof-of-Work):", "Overcoming institutional tier bias via open-source pull requests.")
    add_bullet(tf_tree, "Interactive Override Sliders:", "Streamlit UI features Speed vs. Rigor vs. Budget sliders, enabling students to weigh trade-offs and customize their final roadmap.")

    add_notes(s8, "Slide 8 details our calibrated uncertainty formula and interactive Dispute Tree. When risk exceeds 0.45 or a prerequisite error occurs, the Cognitive Forcing Gate halts release. Students adjust three sliders—Speed, Rigor, and Budget—restoring human-in-the-loop decision agency.")

    # =========================================================================
    # SLIDE 9: Experimental Methodology & 4 Configurations
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_bg(s9, LIGHT_BG)
    add_header(s9, "Experimental Methodology: 4-Configuration Ablation", "Section 5: Experimental Setup", 9, "Systematic benchmarking across 20 synthetic candidate profiles (80 total evaluation runs).")

    w_conf = Inches(2.78)
    h_conf = Inches(5.6)
    t_conf = Inches(1.45)

    cf1 = add_card(s9, Inches(0.8), t_conf, w_conf, h_conf, title="Config 1: Monolithic LLM", title_color=TEXT_MUTED, top_accent=TEXT_MUTED)
    tf_cf1 = s9.shapes.add_textbox(Inches(0.95), t_conf + Inches(0.45), w_conf - Inches(0.3), h_conf - Inches(0.6)).text_frame
    add_bullet(tf_cf1, "Architecture:", "Standard single-prompt LLM baseline (Qwen 2.5 7B via Ollama).")
    add_bullet(tf_cf1, "Hypothesis H1:", "Will suffer from conversational sycophancy, skip foundational math, and steer low-income students to paid bootcamps.")
    add_bullet(tf_cf1, "Verification:", "No external graph checks; no persona separation.")

    cf2 = add_card(s9, Inches(3.78), t_conf, w_conf, h_conf, title="Config 2: Multi-Perspective", title_color=BLUE_ACCENT, top_accent=BLUE_ACCENT)
    tf_cf2 = s9.shapes.add_textbox(Inches(3.93), t_conf + Inches(0.45), w_conf - Inches(0.3), h_conf - Inches(0.6)).text_frame
    add_bullet(tf_cf2, "Architecture:", "Single prompt instructed to generate Planner, Critic, and Ethics views internally.")
    add_bullet(tf_cf2, "Hypothesis H2:", "Attention collapse—internal self-attention smooths conflicting arguments into unprincipled compromises.")
    add_bullet(tf_cf2, "Verification:", "Top-3 Chroma retrieval; no external graph verification.")

    cf3 = add_card(s9, Inches(6.76), t_conf, w_conf, h_conf, title="Config 3: Unmoderated", title_color=AMBER_ACCENT, top_accent=AMBER_ACCENT)
    tf_cf3 = s9.shapes.add_textbox(Inches(6.91), t_conf + Inches(0.45), w_conf - Inches(0.3), h_conf - Inches(0.6)).text_frame
    add_bullet(tf_cf3, "Architecture:", "Three independent agents debating without a moderator or knowledge graph.")
    add_bullet(tf_cf3, "Hypothesis H3:", "The Woozle Effect—agents reinforce each other's hallucinations without resolving core contradictions.")
    add_bullet(tf_cf3, "Verification:", "Higher citation breadth, but severe prerequisite collapse.")

    cf4 = add_card(s9, Inches(9.74), t_conf, w_conf, h_conf, title="Config 4: Proposed System", title_color=EMERALD_ACCENT, top_accent=EMERALD_ACCENT)
    tf_cf4 = s9.shapes.add_textbox(Inches(9.89), t_conf + Inches(0.45), w_conf - Inches(0.3), h_conf - Inches(0.6)).text_frame
    add_bullet(tf_cf4, "Architecture:", "Planner + Critic + Ethics triad moderated by synthesis agent, verified by 42-node DAG and Gate.")
    add_bullet(tf_cf4, "Hypothesis H4:", "Eliminates prerequisite errors to strictly 0.0%, achieves 100% contradiction resolution, and J = 1.00 fairness.")
    add_bullet(tf_cf4, "Verification:", "Top-4 Chroma, 42-node DAG check, Cognitive Forcing Gate.")

    add_notes(s9, "Slide 9 defines our experimental ablation methodology. We test 4 architectures: C1 Monolithic baseline, C2 Single-prompt multi-perspective, C3 Unmoderated debate, and C4 our Proposed RAI System. Each configuration is evaluated across 20 synthetic candidate profiles, yielding 80 complete deliberation traces.")

    # =========================================================================
    # SLIDE 10: Counterfactual Benchmark Suite
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_bg(s10, LIGHT_BG)
    add_header(s10, "Counterfactual Benchmark Suite: Auditing Bias", "Section 5: Fairness Benchmark Suite", 10, "Holding technical skills constant while varying institutional tier and budget.")

    w_bench = Inches(5.7)
    h_bench = Inches(5.6)
    t_bench = Inches(1.45)

    c_prof = add_card(s10, Inches(0.8), t_bench, w_bench, h_bench, title="Benchmark Cohort Structure (20 Profiles)", title_color=NAVY_HEAD, top_accent=NAVY_PRIMARY)
    tf_prof = s10.shapes.add_textbox(Inches(1.0), t_bench + Inches(0.45), w_bench - Inches(0.4), h_bench - Inches(0.6)).text_frame
    add_bullet(tf_prof, "Cohort Composition:", "20 synthetic profiles covering 10 major CS domains (ML, Backend, Systems, DevOps, Security, Cloud, Data, Web, Mobile, QA).")
    add_bullet(tf_prof, "Prerequisite Stress Testing:", "Beginner candidates requesting advanced senior specializations.")
    add_bullet(tf_prof, "Dispute Trigger Scenarios:", "Extreme timeline compression (e.g. 60 days) and budget deficits.")
    add_bullet(tf_prof, "Syntactic Robustness:", "Testing noisy student queries with typos, shorthand, and slang.")
    add_bullet(tf_prof, "Ground-Truth Annotations:", "Two independent human raters labeled 40 dispute decisions and 28 gate triggers, achieving high inter-rater agreement (Cohen's kappa = 0.926).")

    c_aarav = add_card(s10, Inches(6.8), t_bench, w_bench, h_bench, title="Matched Counterfactual Pair: Aarav vs. Priya", title_color=BLUE_ACCENT, top_accent=BLUE_ACCENT)
    tf_aarav = s10.shapes.add_textbox(Inches(7.0), t_bench + Inches(0.45), w_bench - Inches(0.4), h_bench - Inches(0.6)).text_frame
    add_bullet(tf_aarav, "Candidate A (Aarav Sharma):", "Tier-1 Institute (IIT/NIT), ₹40,000/month budget, basic Python, seeks ML Engineer role in 4 months.")
    add_bullet(tf_aarav, "Candidate B (Priya Patel):", "Tier-3 Rural College, ₹3,000/month budget, basic Python, seeks ML Engineer role in 4 months.")
    add_bullet(tf_aarav, "The Scientific Invariant:", "Both students possess identical baseline technical skills and target roles. Any deviation in recommended core technical competencies indicates systemic bias.")
    add_bullet(tf_aarav, "Monolithic LLM Behavior:", "Steers Aarav to Deep Learning research projects, but steers Priya to basic QA testing or IT helpdesk (J = 0.32).")
    add_bullet(tf_aarav, "Proposed System Behavior:", "Recommends identical core curriculum modules to both students (J = 1.00), shielding Priya with MIT OpenCourseWare alternatives.")

    add_notes(s10, "Slide 10 presents our counterfactual fairness testing methodology. We pair candidates with identical skills but starkly different economic and institutional backgrounds—such as Aarav from a Tier-1 college and Priya from a rural Tier-3 college. Our proposed system guarantees identical core technical curricula with Jaccard parity of 1.00.")

    # =========================================================================
    # SLIDE 11: Formal Evaluation Metrics
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_bg(s11, LIGHT_BG)
    add_header(s11, "Formal Evaluation Metrics & Mathematical Formulations", "Section 6: Evaluation Metrics", 11, "Quantitative criteria for prerequisite correctness, debate synthesis, diversity, and equity.")

    w_m = Inches(2.22)
    h_m = Inches(5.6)
    t_m = Inches(1.45)
    spacing_m = Inches(0.16)

    metrics = [
        ("UCR (Prerequisites)", "Unsupported-Claim Rate", "<= 5.0%", "0.0%", ROSE_ACCENT, "Percentage of recommended milestones violating prerequisite ordering in the 42-node DAG."),
        ("CRR (Contradictions)", "Contradiction Resolution", ">= 80.0%", "100.0%", TEAL_PRIMARY, "Percentage of Critic and Ethics objections addressed and resolved in the final synthesized plan."),
        ("H_div (Diversity)", "Evidence Diversity", ">= 0.80", "1.00", BLUE_ACCENT, "Normalized Shannon entropy across cited knowledge categories (MIT OCW, CS50, O*NET, IEEE)."),
        ("J (Fairness)", "Demographic Fairness", ">= 0.90", "1.00", INDIGO_ACCENT, "Jaccard similarity of core curriculum recommendations between matched counterfactual pairs."),
        ("User Rubric", "Pedagogical Score", ">= 4.0 / 5.0", "4.7 / 5.0", EMERALD_ACCENT, "Standardized evaluation across 5 dimensions: Balance, Rigor, Equity, Transparency, Feasibility."),
    ]

    for i, (code, name, target, obs, color, desc) in enumerate(metrics):
        x = Inches(0.8) + i * (w_m + spacing_m)
        card = add_card(s11, x, t_m, w_m, h_m, title=code, title_color=color, top_accent=color, title_size=11)
        tf = s11.shapes.add_textbox(x + Inches(0.1), t_m + Inches(0.42), w_m - Inches(0.2), h_m - Inches(0.55)).text_frame
        add_bullet(tf, "Metric:", name, pt_size=9.5)
        add_bullet(tf, "Target:", target, pt_size=9.5, bold_color=TEXT_MUTED)
        add_bullet(tf, "Observed:", obs, pt_size=11.5, bold_color=color)
        add_bullet(tf, "Definition:", desc, pt_size=9.0, norm_color=TEXT_MAIN)

    add_notes(s11, "Slide 11 formalizes our five quantitative evaluation metrics: Unsupported-Claim Rate (UCR), Contradiction-Resolution Rate (CRR), Evidence Diversity (H_div), Demographic Fairness (Jaccard J), and the standardized 5-point User Rubric score. All targets were comfortably achieved or exceeded.")

    # =========================================================================
    # SLIDE 12: Empirical Results & Comparative Analysis
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    set_bg(s12, LIGHT_BG)
    add_header(s12, "Empirical Results: Full Ablation Benchmark Table", "Section 6: Empirical Findings", 12, "Config 4 eliminates prerequisite errors to strictly 0.0% and achieves 100% contradiction resolution.")

    # Big Benchmark Table
    rows = 5
    cols = 7
    table_shape = s12.shapes.add_table(rows, cols, Inches(0.8), Inches(1.5), Inches(11.733), Inches(3.2))
    table = table_shape.table

    table.columns[0].width = Inches(2.3)
    table.columns[1].width = Inches(1.6)
    table.columns[2].width = Inches(1.6)
    table.columns[3].width = Inches(1.6)
    table.columns[4].width = Inches(1.6)
    table.columns[5].width = Inches(1.5)
    table.columns[6].width = Inches(1.533)

    headers = ["Configuration", "UCR (Prereq Error)", "CRR (Contradictions)", "H_div (Diversity)", "Fairness (Jaccard)", "User Rubric", "Statistical p-val"]
    data = [
        ["Config 1 (Monolithic LLM)", "90.9%", "0.0%", "0.00", "0.32", "2.1 / 5.0", "Baseline"],
        ["Config 2 (Multi-Perspective)", "68.2%", "38.0%", "0.72", "0.93", "3.2 / 5.0", "p < 0.01"],
        ["Config 3 (Unmoderated Debate)", "86.4% (Woozle)", "25.0%", "0.85", "1.00", "3.8 / 5.0", "p < 0.01"],
        ["Config 4 (Proposed RAI)", "0.0% (Zero Error)", "100.0%", "1.00", "1.00", "4.7 / 5.0", "p < 0.0001 (McNemar)"],
    ]

    for col_idx, text in enumerate(headers):
        cell = table.cell(0, col_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = NAVY_HEAD
        p = cell.text_frame.paragraphs[0]
        p.text = text
        p.font.name = FONT_FAMILY
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p.alignment = PP_ALIGN.CENTER

    for row_idx, row_data in enumerate(data):
        is_c4 = row_idx == 3
        bg_col = RGBColor(240, 253, 250) if is_c4 else (CARD_BG if row_idx % 2 == 0 else CARD_MUTED)
        for col_idx, val in enumerate(row_data):
            cell = table.cell(row_idx + 1, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg_col
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = FONT_FAMILY
            p.font.size = Pt(9.5)
            p.font.bold = is_c4
            p.font.color.rgb = TEAL_PRIMARY if (is_c4 and col_idx in [1, 2, 3, 4, 5]) else TEXT_MAIN
            p.alignment = PP_ALIGN.CENTER if col_idx > 0 else PP_ALIGN.LEFT

    # Explanatory Callout Card
    c_res = add_card(s12, Inches(0.8), Inches(4.9), Inches(11.733), Inches(2.1), title="Key Empirical Discoveries", title_color=NAVY_HEAD, top_accent=EMERALD_ACCENT)
    tf_res = s12.shapes.add_textbox(Inches(1.0), Inches(5.25), Inches(11.333), Inches(1.6)).text_frame
    add_bullet(tf_res, "1. Prerequisite Eradication:", "Deterministic graph verification dropped prerequisite sequencing errors from 90.9% in monolithic LLMs to strictly 0.0% (p < 0.0001, McNemar exact test).", pt_size=10.0)
    add_bullet(tf_res, "2. Confirmation of the Woozle Effect:", "Config 3 (Unmoderated debate) exhibited an 86.4% prerequisite error rate, empirically confirming that debate without external graph anchors mutually validates errors.", pt_size=10.0)
    add_bullet(tf_res, "3. Complete Demographic Equity:", "Config 4 achieved J = 1.00 curriculum parity across Tier-1 and Tier-3 counterfactual pairs, completely eliminating institutional pedigree bias.", pt_size=10.0)

    add_notes(s12, "Slide 12 presents our definitive numerical findings across 80 experimental runs. Config 4 achieved 0.0% prerequisite errors, 100% contradiction resolution, 1.00 evidence diversity, and 1.00 fairness parity. McNemar's test confirms statistical significance at p < 0.0001 over the baseline.")

    # =========================================================================
    # SLIDE 13: System Performance & Resource Footprint
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    set_bg(s13, LIGHT_BG)
    add_header(s13, "System Performance, Latency, and Edge Deployability", "Section 7: Production Feasibility", 13, "100% Local execution on consumer student hardware with zero API expenditures.")

    w_perf = Inches(2.78)
    h_perf = Inches(5.6)
    t_perf = Inches(1.45)

    p_cards = [
        ("Total Deliberation Latency", "11.4 Seconds", BLUE_ACCENT, [
            ("Planner Draft:", "3.8 seconds"),
            ("Critic Audit:", "3.2 seconds"),
            ("Ethics Review:", "2.9 seconds"),
            ("Moderator Synthesis:", "1.5 seconds"),
            ("Graph Traversal:", "< 0.002 seconds"),
            ("Assessment:", "Acceptable for real-time advisory."),
        ]),
        ("System RAM Footprint", "5.2 GB Peak", TEAL_PRIMARY, [
            ("Quantization:", "4-bit (q4_k_m)"),
            ("Model Weights:", "4.7 GB in memory"),
            ("Vector Store:", "14 MB ChromaDB"),
            ("Graph Engine:", "120 KB NetworkX DAG"),
            ("Safety Margin:", "Leaves ample RAM on standard 16 GB laptops."),
        ]),
        ("Operational Financial Cost", "₹0.00 / Query", EMERALD_ACCENT, [
            ("Cloud API Cost:", "Zero ongoing API tokens"),
            ("Third-Party Fees:", "Zero SaaS subscriptions"),
            ("Student Invariant:", "100% free access for all students regardless of wealth"),
            ("University Infra:", "No expensive GPU clusters required."),
        ]),
        ("Student Data Privacy", "100% Private", INDIGO_ACCENT, [
            ("Transmission:", "Zero packets sent externally"),
            ("FERPA/GDPR Compliance:", "Student transcripts & aspirations stay entirely on-device"),
            ("Offline Capable:", "Functions seamlessly without an active internet connection."),
        ]),
    ]

    for i, (title, stat, color, bullets) in enumerate(p_cards):
        x = Inches(0.8) + i * (w_perf + Inches(0.2))
        add_card(s13, x, t_perf, w_perf, h_perf, title=title, title_color=color, top_accent=color, title_size=11)
        tf = s13.shapes.add_textbox(x + Inches(0.12), t_perf + Inches(0.45), w_perf - Inches(0.24), h_perf - Inches(0.55)).text_frame
        # Stat callout
        p_stat = tf.paragraphs[0]
        p_stat.text = stat
        p_stat.font.name = FONT_FAMILY
        p_stat.font.size = Pt(17)
        p_stat.font.bold = True
        p_stat.font.color.rgb = color
        p_stat.alignment = PP_ALIGN.CENTER
        p_stat.space_after = Pt(10)

        for b_bold, b_txt in bullets:
            add_bullet(tf, b_bold, b_txt, pt_size=9.2, space_after=3)

    add_notes(s13, "Slide 13 confirms production viability on standard student hardware: an end-to-end deliberation cycle of 11.4 seconds, peak RAM of 5.2 GB, zero cloud API costs, and complete student data privacy with 100% on-device local execution.")

    # =========================================================================
    # SLIDE 14: Key Theoretical Insights & Viva Voce Q&A
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    set_bg(s14, LIGHT_BG)
    add_header(s14, "Theoretical Insights & Viva Voce Defense Guide", "Section 7: Theoretical Insights & Defense", 14, "Addressing core examiner inquiries regarding model capability, graphs, and usability.")

    w_viva = Inches(5.7)
    h_viva = Inches(5.6)
    t_viva = Inches(1.45)

    c_vl = add_card(s14, Inches(0.8), t_viva, w_viva, h_viva, title="Core Examination Defenses", title_color=NAVY_HEAD, top_accent=NAVY_PRIMARY)
    tf_vl = s14.shapes.add_textbox(Inches(1.0), t_viva + Inches(0.45), w_viva - Inches(0.4), h_viva - Inches(0.6)).text_frame
    add_bullet(tf_vl, "Q1: Why not just use GPT-4o or Claude 3.5?", "Two reasons: First, cloud models violate student privacy and incur continuous token costs. Second, empirical literature proves even frontier models hallucinate prerequisite order without structural graph verification.")
    add_bullet(tf_vl, "Q2: Isn't a 7B model too small for complex debate?", "By assigning narrow persona roles with asymmetric temperatures (0.3 vs 0.6) and anchoring in a 42-node DAG, Qwen 2.5 7B matches or exceeds monolithic frontier models while running locally.")
    add_bullet(tf_vl, "Q3: Why NetworkX instead of Neo4j for the prototype?", "NetworkX executes in-memory in < 0.2 ms with zero server overhead. However, our architecture is dual-mode: we include automated Cypher export to Neo4j for enterprise scaling.")

    c_vr = add_card(s14, Inches(6.8), t_viva, w_viva, h_viva, title="Empirical Validation & Student Usability", title_color=INDIGO_ACCENT, top_accent=INDIGO_ACCENT)
    tf_vr = s14.shapes.add_textbox(Inches(7.0), t_viva + Inches(0.45), w_viva - Inches(0.4), h_viva - Inches(0.6)).text_frame
    add_bullet(tf_vr, "Ground-Truth Reliability (Cohen's Kappa):", "Two independent human raters evaluated 40 dispute decisions and 28 gate triggers, obtaining kappa = 0.926, confirming high annotation consistency.")
    add_bullet(tf_vr, "Why Uncalibrated LLM Judges Fail:", "Pilot tests using an unprompted 7B LLM judge showed dismal reliability (kappa = 0.12), penalizing legitimate electives. We replaced it with hybrid graph + focused classification scoring.")
    add_bullet(tf_vr, "User Study with 15 Engineering Students:", "Conducted at SRMIST. 93.3% of students preferred the multi-agent Dispute Tree and interactive sliders over opaque single-prompt chatbot answers.")
    add_bullet(tf_vr, "Student Feedback:", "Students reported that seeing explicit Critic warnings helped them identify real interview hurdles they had underestimated.")

    add_notes(s14, "Slide 14 prepares us for tough viva voce questions. We explain why local 7B models with external graphs outperform cloud models, defend our NetworkX/Neo4j dual-mode architecture, and highlight our student study where 93.3% of participants preferred explicit dispute trees over chatbot flattery.")

    # =========================================================================
    # SLIDE 15: Conclusion & Future Directions (Executive Dark)
    # =========================================================================
    s15 = prs.slides.add_slide(blank_layout)
    set_bg(s15, DARK_BG)

    badge_end = s15.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.8), Inches(4.5), Inches(0.32))
    badge_end.fill.solid()
    badge_end.fill.fore_color.rgb = RGBColor(30, 41, 59)
    badge_end.line.color.rgb = TEAL_ACCENT
    badge_end.line.width = Pt(1)
    bep = badge_end.text_frame.paragraphs[0]
    bep.text = "SECTION 8: RESEARCH SUMMARY & CONCLUSION"
    bep.font.name = FONT_FAMILY
    bep.font.size = Pt(8.5)
    bep.font.bold = True
    bep.font.color.rgb = TEAL_ACCENT
    bep.alignment = PP_ALIGN.CENTER
    badge_end.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    tb_end = s15.shapes.add_textbox(Inches(0.8), Inches(1.25), Inches(11.733), Inches(0.8))
    p_end = tb_end.text_frame.paragraphs[0]
    p_end.text = "Responsible AI in Higher Education: Core Contributions"
    p_end.font.name = FONT_FAMILY
    p_end.font.size = Pt(24)
    p_end.font.bold = True
    p_end.font.color.rgb = TEXT_WHITE

    div_end = s15.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(2.15), Inches(11.733), Inches(0.02))
    div_end.fill.solid()
    div_end.fill.fore_color.rgb = RGBColor(51, 65, 85)
    div_end.line.fill.background()

    # Left Deliverables Card
    c_del = add_card(s15, Inches(0.8), Inches(2.4), Inches(5.6), Inches(4.3), title="Project Deliverables & Artifacts", title_color=TEAL_ACCENT, bg_color=RGBColor(30, 41, 59), border_color=RGBColor(51, 65, 85), title_size=12)
    tf_del = s15.shapes.add_textbox(Inches(1.0), Inches(2.85), Inches(5.2), Inches(3.7)).text_frame
    add_bullet(tf_del, "1. Streamlit Prototype (app.py):", "Live interactive multi-agent debate trace viewer, dynamic Dispute Tree, and student override sliders.", pt_size=10.5, norm_color=RGBColor(203, 213, 225))
    add_bullet(tf_del, "2. Prerequisite Graph (career_graph.py):", "42 nodes, 47 edges, NetworkX engine + automated Neo4j Cypher synchronization.", pt_size=10.5, norm_color=RGBColor(203, 213, 225))
    add_bullet(tf_del, "3. Evaluation Engine (benchmark_suite.py):", "20 synthetic profiles, 80-run ablation suite, and metrics logging.", pt_size=10.5, norm_color=RGBColor(203, 213, 225))
    add_bullet(tf_del, "4. Academic Publications:", "IEEE Research Paper (paper.typ) & 4-Page Research Specification Document.", pt_size=10.5, norm_color=RGBColor(203, 213, 225))
    add_bullet(tf_del, "5. Originality Certification:", "Audited via Noplag Engine (0.00% Plagiarism, 0.0% AI Slop).", pt_size=10.5, norm_color=RGBColor(203, 213, 225))

    # Right Contributions Card
    c_con = add_card(s15, Inches(6.8), Inches(2.4), Inches(5.733), Inches(4.3), title="Scientific Impact & Committee Q&A", title_color=BLUE_ACCENT, bg_color=RGBColor(30, 41, 59), border_color=RGBColor(51, 65, 85), title_size=12)
    tf_con = s15.shapes.add_textbox(Inches(7.0), Inches(2.85), Inches(5.333), Inches(3.7)).text_frame
    add_bullet(tf_con, "Zero Hallucination Tolerance:", "Proved that multi-agent deliberation combined with external knowledge graphs can completely eliminate prerequisite sequencing errors (0.0%).", pt_size=10.5, norm_color=RGBColor(203, 213, 225))
    add_bullet(tf_con, "Equitable Educational Access:", "Demonstrated that AI can guarantee demographic parity (J = 1.00) while actively protecting low-income students from predatory debt.", pt_size=10.5, norm_color=RGBColor(203, 213, 225))
    add_bullet(tf_con, "Human Agency Paradigm:", "Shifted AI advising from opaque dictation to transparent, slider-based trade-off exploration.", pt_size=10.5, norm_color=RGBColor(203, 213, 225))
    add_bullet(tf_con, "Demonstration & Viva Voce:", "System is live and ready for interactive demonstration via `streamlit run app.py`.", pt_size=10.5, bold_color=TEAL_ACCENT, norm_color=TEXT_WHITE)

    add_notes(s15, "In conclusion, our research demonstrates that multi-agent debate anchored by deterministic knowledge graphs eliminates hallucinated prerequisites, ensures counterfactual equity, and restores student agency. We thank our mentors Dr. P. Akilandeswari and Pratyush Jha, and now welcome questions from the committee.")

    prs.save(output_pptx)
    print(f"✅ Successfully generated master presentation deck (15 slides) at: {output_pptx}")


if __name__ == "__main__":
    build_deck()
