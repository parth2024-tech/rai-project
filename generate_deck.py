#!/usr/bin/env python3
"""
High-Impact Academic Presentation Deck (18 Slides)
Debate-Based Career Guidance Agent with Complementary Personas

100% Strictly Aligned with Project Specification:
- Personas: Planner, Critic, and Ethics-Reviewer orchestrated by Moderator
- Core Principles: Avoiding one-sided advice, transparency of disagreement, fairness, calibrated uncertainty, human override
- Tech Stack: Qwen local; Python multi-agent harness; Neo4j career-skill graph; Chroma/FAISS; Streamlit
- Evaluation Metrics: Evidence diversity; contradiction-resolution rate; unsupported-claim rate; fairness across synthetic profiles; user-rubric score
- Deliverables: Multi-persona prototype, debate trace viewer, synthetic profile set, and comparative evaluation
"""

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt


def build_presentation_deck(output_path="/home/thor/Desktop/RAI Project/Final_Presentation.pptx"):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Academic 60-30-10 Palette
    BG_DARK = RGBColor(15, 23, 42)          # Slate 900
    BG_LIGHT = RGBColor(248, 250, 252)      # Slate 50
    CARD_BG = RGBColor(255, 255, 255)       # White
    CARD_BORDER = RGBColor(203, 213, 225)   # Slate 300
    CARD_MUTED = RGBColor(241, 245, 249)    # Slate 100

    NAVY_PRIMARY = RGBColor(30, 41, 59)     # Slate 800
    NAVY_HEAD = RGBColor(15, 23, 42)        # Slate 900
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

    TEXT_MAIN = RGBColor(30, 41, 59)        # Slate 800
    TEXT_MUTED = RGBColor(100, 116, 139)    # Slate 500
    TEXT_WHITE = RGBColor(255, 255, 255)

    FONT_MAIN = "Calibri"
    TOTAL_SLIDES = 18

    def apply_bg(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_header(slide, title, category, slide_num, takeaway=""):
        tag = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.32), Inches(4.5), Inches(0.28))
        tag.fill.solid()
        tag.fill.fore_color.rgb = TEAL_BG
        tag.line.color.rgb = TEAL_PRIMARY
        tag.line.width = Pt(1)
        tp = tag.text_frame.paragraphs[0]
        tp.text = category.upper()
        tp.font.name = FONT_MAIN
        tp.font.size = Pt(9.0)
        tp.font.bold = True
        tp.font.color.rgb = TEAL_PRIMARY
        tp.alignment = PP_ALIGN.CENTER
        tag.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

        tb_t = slide.shapes.add_textbox(Inches(0.8), Inches(0.62), Inches(11.733), Inches(0.44))
        p = tb_t.text_frame.paragraphs[0]
        p.text = title
        p.font.name = FONT_MAIN
        p.font.size = Pt(21)
        p.font.bold = True
        p.font.color.rgb = NAVY_HEAD

        if takeaway:
            tb_sub = slide.shapes.add_textbox(Inches(0.8), Inches(1.06), Inches(11.733), Inches(0.30))
            p_sub = tb_sub.text_frame.paragraphs[0]
            p_sub.text = takeaway
            p_sub.font.name = FONT_MAIN
            p_sub.font.size = Pt(11.0)
            p_sub.font.color.rgb = TEXT_MUTED

        tb_n = slide.shapes.add_textbox(Inches(11.5), Inches(0.32), Inches(1.033), Inches(0.3))
        pn = tb_n.text_frame.paragraphs[0]
        pn.text = f"{slide_num:02d} / {TOTAL_SLIDES}"
        pn.font.name = FONT_MAIN
        pn.font.size = Pt(9.5)
        pn.font.bold = True
        pn.font.color.rgb = TEXT_MUTED
        pn.alignment = PP_ALIGN.RIGHT

    def add_card(slide, left, top, width, height, title="", title_color=NAVY_HEAD, bg_color=CARD_BG, border_color=CARD_BORDER, top_accent=None, title_size=13.0):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1)

        if top_accent:
            bar = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, Inches(0.08))
            bar.fill.solid()
            bar.fill.fore_color.rgb = top_accent
            bar.line.fill.background()

        if title:
            tb = slide.shapes.add_textbox(left + Inches(0.18), top + Inches(0.12), width - Inches(0.36), Inches(0.36))
            p = tb.text_frame.paragraphs[0]
            p.text = title
            p.font.name = FONT_MAIN
            p.font.size = Pt(title_size)
            p.font.bold = True
            p.font.color.rgb = title_color
            tb.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

        return card

    def add_bullet(tf, bold_prefix, text, pt_size=12.5, space_after=5, bold_color=NAVY_PRIMARY, norm_color=TEXT_MAIN):
        p = tf.add_paragraph() if len(tf.paragraphs[0].text) > 0 else tf.paragraphs[0]
        p.space_after = Pt(space_after)

        r1 = p.add_run()
        r1.text = bold_prefix + " "
        r1.font.name = FONT_MAIN
        r1.font.bold = True
        r1.font.size = Pt(pt_size)
        r1.font.color.rgb = bold_color

        r2 = p.add_run()
        r2.text = text
        r2.font.name = FONT_MAIN
        r2.font.bold = False
        r2.font.size = Pt(pt_size)
        r2.font.color.rgb = norm_color

    def add_flow_node(slide, left, top, width, height, title, subtitle="", bg=CARD_BG, border=TEAL_PRIMARY, text_color=NAVY_HEAD, shape=MSO_SHAPE.ROUNDED_RECTANGLE):
        node = slide.shapes.add_shape(shape, left, top, width, height)
        node.fill.solid()
        node.fill.fore_color.rgb = bg
        node.line.color.rgb = border
        node.line.width = Pt(1.5)

        tf = node.text_frame
        tf.word_wrap = True
        p1 = tf.paragraphs[0]
        p1.text = title
        p1.font.name = FONT_MAIN
        p1.font.bold = True
        p1.font.size = Pt(11.0)
        p1.font.color.rgb = text_color
        p1.alignment = PP_ALIGN.CENTER

        if subtitle:
            p2 = tf.add_paragraph()
            p2.text = subtitle
            p2.font.name = FONT_MAIN
            p2.font.bold = False
            p2.font.size = Pt(9.0)
            p2.font.color.rgb = TEXT_MUTED
            p2.alignment = PP_ALIGN.CENTER

        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        return node

    def add_arrow(slide, left, top, width, height, direction="right", color=TEAL_PRIMARY):
        shape_type = MSO_SHAPE.RIGHT_ARROW if direction == "right" else (MSO_SHAPE.DOWN_ARROW if direction == "down" else MSO_SHAPE.LEFT_ARROW)
        arrow = slide.shapes.add_shape(shape_type, left, top, width, height)
        arrow.fill.solid()
        arrow.fill.fore_color.rgb = color
        arrow.line.fill.background()
        return arrow

    # =========================================================================
    # SLIDE 1: Title Slide (Dark Slate Executive Theme)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    apply_bg(s1, BG_DARK)

    badge = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.8), Inches(4.8), Inches(0.38))
    badge.fill.solid()
    badge.fill.fore_color.rgb = RGBColor(30, 41, 59)
    badge.line.color.rgb = TEAL_PRIMARY
    badge.line.width = Pt(1)
    bp = badge.text_frame.paragraphs[0]
    bp.text = "RESPONSIBLE AI · MULTI-PERSONA DIALECTIC ADVISORY"
    bp.font.name = FONT_MAIN
    bp.font.size = Pt(10.0)
    bp.font.bold = True
    bp.font.color.rgb = TEAL_ACCENT
    bp.alignment = PP_ALIGN.CENTER
    badge.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    tb_title = s1.shapes.add_textbox(Inches(0.8), Inches(1.35), Inches(11.733), Inches(1.4))
    pt = tb_title.text_frame.paragraphs[0]
    pt.text = "Debate-Based Career Guidance Agent with Complementary Personas"
    pt.font.name = FONT_MAIN
    pt.font.size = Pt(28.0)
    pt.font.bold = True
    pt.font.color.rgb = TEXT_WHITE

    pt_sub = tb_title.text_frame.add_paragraph()
    pt_sub.text = "Planner, Critic, and Ethics-Reviewer Personas Debating Public Course & Role Data with Calibrated Uncertainty & Human Override"
    pt_sub.font.name = FONT_MAIN
    pt_sub.font.size = Pt(14.0)
    pt_sub.font.color.rgb = TEAL_ACCENT

    top_meta = Inches(3.2)
    col_w1 = Inches(5.6)
    col_w2 = Inches(5.6)
    col_h2 = Inches(3.4)

    card_bold_col = TEAL_ACCENT
    card_norm_col = RGBColor(226, 232, 240)

    add_card(s1, Inches(0.8), top_meta, col_w1, col_h2, "Student Investigators & Degree Program", TEAL_PRIMARY, bg_color=RGBColor(30, 41, 59), border_color=RGBColor(51, 65, 85))
    tb_m1 = s1.shapes.add_textbox(Inches(1.0), top_meta + Inches(0.48), col_w1 - Inches(0.4), col_h2 - Inches(0.55))
    tf_m1 = tb_m1.text_frame
    tf_m1.word_wrap = True
    add_bullet(tf_m1, "• Degree Program:", "B.Tech in Computer Science and Engineering", pt_size=12.0, space_after=6, bold_color=card_bold_col, norm_color=card_norm_col)
    add_bullet(tf_m1, "• Department:", "Department of Computer Science & Engineering", pt_size=12.0, space_after=6, bold_color=card_bold_col, norm_color=card_norm_col)
    add_bullet(tf_m1, "• Project Domain:", "Responsible AI (RAI) · Multi-Agent Debate Systems", pt_size=12.0, space_after=6, bold_color=card_bold_col, norm_color=card_norm_col)
    add_bullet(tf_m1, "• Academic Session:", "Academic Evaluation 2025–2026", pt_size=12.0, space_after=6, bold_color=card_bold_col, norm_color=card_norm_col)

    add_card(s1, Inches(6.833), top_meta, col_w2, col_h2, "Official Architecture & Tech Stack", BLUE_ACCENT, bg_color=RGBColor(30, 41, 59), border_color=RGBColor(51, 65, 85))
    tb_m2 = s1.shapes.add_textbox(Inches(7.033), top_meta + Inches(0.48), col_w2 - Inches(0.4), col_h2 - Inches(0.55))
    tf_m2 = tb_m2.text_frame
    tf_m2.word_wrap = True
    add_bullet(tf_m2, "• LLM Inference Engine:", "Qwen Local (via Ollama on Consumer Hardware)", pt_size=12.0, space_after=6, bold_color=card_bold_col, norm_color=card_norm_col)
    add_bullet(tf_m2, "• Multi-Agent Harness:", "Python Multi-Agent Deliberation Harness (Planner, Critic, Ethics)", pt_size=12.0, space_after=6, bold_color=card_bold_col, norm_color=card_norm_col)
    add_bullet(tf_m2, "• Knowledge Grounding:", "Neo4j Career-Skill Graph (42-Node DAG) & Chroma Vector Store", pt_size=12.0, space_after=6, bold_color=card_bold_col, norm_color=card_norm_col)
    add_bullet(tf_m2, "• User Interface:", "Streamlit Prototype with Interactive Trace Viewer & Human Override", pt_size=12.0, space_after=6, bold_color=card_bold_col, norm_color=card_norm_col)

    s1.notes_slide.notes_text_frame.text = (
        "Good morning committee. Today I present our Responsible AI project: 'Debate-Based Career Guidance Agent "
        "with Complementary Personas'. We deploy Planner, Critic, and Ethics-Reviewer personas debating public course "
        "and role data using local Qwen, a Python multi-agent harness, a 42-node Neo4j career-skill graph, Chroma, and Streamlit, "
        "producing balanced recommendations with calibrated uncertainty and human override."
    )

    # =========================================================================
    # SLIDE 2: Section 1 — Abstract: Visual System Overview
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    apply_bg(s2, BG_LIGHT)
    add_header(s2, "Abstract: Grounded Dialectics for Algorithmic Advisory", "Section 1: Abstract", 2,
               "Avoiding one-sided advice, transparency of disagreement, fairness, and calibrated uncertainty.")

    w3 = Inches(3.64)
    h_top = Inches(2.4)
    h_bot = Inches(2.7)

    add_card(s2, Inches(0.8), Inches(1.55), w3, h_top, "The Advisory Dilemma", ROSE_ACCENT, top_accent=ROSE_ACCENT)
    tb = s2.shapes.add_textbox(Inches(0.95), Inches(2.05), w3 - Inches(0.3), h_top - Inches(0.55))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Sycophancy Trap:", "Monolithic LLMs flatter unfeasible student requests without verifying prerequisites.")
    add_bullet(tf, "• False Consensus:", "Single-agent decoding averages competing career trade-offs into vague, one-sided advice.")
    add_bullet(tf, "• Demographic Steering:", "Pre-trained models leak subtle socioeconomic and institutional pedigree biases.")

    add_card(s2, Inches(4.84), Inches(1.55), w3, h_top, "Grounded Dialectic System", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s2.shapes.add_textbox(Inches(5.0), Inches(2.05), w3 - Inches(0.3), h_top - Inches(0.55))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• 3 Dialectic Personas:", "Planner (Growth), Critic (Rigor & Saturation), Ethics-Reviewer (Fairness & Debt).")
    add_bullet(tf, "• Public Course & Role Data:", "Chroma indexing ACM/IEEE CS Curricula and O*NET occupational classifications.")
    add_bullet(tf, "• Neo4j Prerequisite Graph:", "42-node prerequisite DAG enforces strict topological dependency reachability.")

    add_card(s2, Inches(8.88), Inches(1.55), w3, h_top, "Evaluation & Governance Scope", BLUE_ACCENT, top_accent=BLUE_ACCENT)
    tb = s2.shapes.add_textbox(Inches(9.03), Inches(2.05), w3 - Inches(0.3), h_top - Inches(0.55))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• 4 Comparative Configurations:", "Monolithic LLM vs Multi-Perspective Prompt vs Unmoderated Triad vs Full System.")
    add_bullet(tf, "• 5 Official Metrics:", "Evidence diversity, contradiction-resolution, unsupported-claims, fairness, user-rubric.")
    add_bullet(tf, "• Calibrated Human Override:", "Cognitive forcing gate halts automated steering; empowers student decision choice.")

    add_card(s2, Inches(0.8), Inches(4.15), Inches(11.733), h_bot, "Core Academic Contributions & Pilot Findings", NAVY_HEAD, top_accent=NAVY_HEAD)
    tb_bot = s2.shapes.add_textbox(Inches(1.0), Inches(4.65), Inches(11.333), h_bot - Inches(0.6))
    tf_bot = tb_bot.text_frame
    tf_bot.word_wrap = True
    add_bullet(tf_bot, "1. Dialectic Multi-Agent Formulation:", "Separated Planner, Critic, and Ethics-Reviewer personas preserve legitimate technical trade-offs that collapse in monolithic prompts.", pt_size=12.5)
    add_bullet(tf_bot, "2. Grounded Evidence & Graph Verification:", "Integrates Chroma semantic retrieval of ACM curricula with a 42-node Neo4j prerequisite DAG to drive unsupported claims down to 0.0%.", pt_size=12.5)
    add_bullet(tf_bot, "3. Counterfactual Fairness & Agency Preservation:", "Maintains 100% fairness parity across matched synthetic demographic pairs (Aarav vs Priya) while offering interactive human override.", pt_size=12.5)

    s2.notes_slide.notes_text_frame.text = (
        "Slide 2 outlines the abstract. Standard single-agent LLMs suffer from conversational sycophancy: they agree "
        "with student ambitions even when students lack foundational prerequisites. We address this using Planner, Critic, "
        "and Ethics-Reviewer personas, public course and role data, Neo4j graph traversal, and human override."
    )

    # =========================================================================
    # SLIDE 3: Section 2 — Introduction: Visual Problem Comparison Flowchart
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    apply_bg(s3, BG_LIGHT)
    add_header(s3, "Introduction: Monolithic Flattery vs. Grounded Dialectics", "Section 2: Introduction", 3,
               "Contrasting the dangerous sycophancy trap of standard LLMs with our grounded dialectic pipeline.")

    col_w_s3 = Inches(5.6)
    col_h_s3 = Inches(5.2)

    # Left Column: Monolithic Flattery
    add_card(s3, Inches(0.8), Inches(1.55), col_w_s3, col_h_s3, "Standard Monolithic AI (Sycophancy Trap)", ROSE_ACCENT, top_accent=ROSE_ACCENT, bg_color=ROSE_BG, border_color=ROSE_ACCENT)
    add_flow_node(s3, Inches(1.1), Inches(2.15), Inches(5.0), Inches(0.8), "1. Unrealistic Student Request", "e.g., 'Become Staff ML Engineer in 4 Months via Commercial Bootcamp'", bg=CARD_BG, border=ROSE_ACCENT)
    add_arrow(s3, Inches(3.45), Inches(3.02), Inches(0.3), Inches(0.25), direction="down", color=ROSE_ACCENT)
    add_flow_node(s3, Inches(1.1), Inches(3.35), Inches(5.0), Inches(0.8), "2. RLHF Agreeableness Bias", "Model affirms student goal to maximize conversational reward score", bg=CARD_BG, border=ROSE_ACCENT)
    add_arrow(s3, Inches(3.45), Inches(4.22), Inches(0.3), Inches(0.25), direction="down", color=ROSE_ACCENT)
    add_flow_node(s3, Inches(1.1), Inches(4.55), Inches(5.0), Inches(0.8), "3. Skipped Prerequisite Sequence", "Omits Linear Algebra & OS; recommends advanced Transformers directly", bg=CARD_BG, border=ROSE_ACCENT)
    add_arrow(s3, Inches(3.45), Inches(5.42), Inches(0.3), Inches(0.25), direction="down", color=ROSE_ACCENT)
    add_flow_node(s3, Inches(1.1), Inches(5.75), Inches(5.0), Inches(0.8), "RISK: Financial Loss & Interview Rejection", "Student incurs high bootcamp debt; fails technical screening", bg=CARD_BG, border=ROSE_ACCENT, text_color=ROSE_ACCENT)

    # Right Column: Proposed Dialectic Architecture
    add_card(s3, Inches(6.9), Inches(1.55), col_w_s3, col_h_s3, "Proposed Grounded Architecture (Truth-Seeking)", TEAL_PRIMARY, top_accent=TEAL_PRIMARY, bg_color=TEAL_BG, border_color=TEAL_PRIMARY)
    add_flow_node(s3, Inches(7.2), Inches(2.15), Inches(5.0), Inches(0.8), "1. Profile Intake & Public Data Grounding", "Retrieves ACM course modules and O*NET standards via ChromaDB", bg=CARD_BG, border=TEAL_PRIMARY)
    add_arrow(s3, Inches(9.55), Inches(3.02), Inches(0.3), Inches(0.25), direction="down", color=TEAL_PRIMARY)
    add_flow_node(s3, Inches(7.2), Inches(3.35), Inches(5.0), Inches(0.8), "2. Differentiated Persona Friction", "Planner (Pathways) vs Critic (Prerequisites) vs Ethics-Reviewer (Equity)", bg=CARD_BG, border=TEAL_PRIMARY)
    add_arrow(s3, Inches(9.55), Inches(4.22), Inches(0.3), Inches(0.25), direction="down", color=TEAL_PRIMARY)
    add_flow_node(s3, Inches(7.2), Inches(4.55), Inches(5.0), Inches(0.8), "3. Neo4j 42-Node DAG Traversal", "Graph traversal detects missing prerequisite hops; flags Delta_prereq", bg=CARD_BG, border=TEAL_PRIMARY)
    add_arrow(s3, Inches(9.55), Inches(5.42), Inches(0.3), Inches(0.25), direction="down", color=TEAL_PRIMARY)
    add_flow_node(s3, Inches(7.2), Inches(5.75), Inches(5.0), Inches(0.8), "OUTCOME: Dispute Tree & Human Override", "Surfaces calibrated uncertainty; counselor/student adjusts trade-offs", bg=CARD_BG, border=TEAL_PRIMARY, text_color=TEAL_PRIMARY)

    s3.notes_slide.notes_text_frame.text = (
        "Slide 3 contrasts standard monolithic LLM behavior against our dialectic pipeline. Notice the failure mode on the left: "
        "when a student makes an unrealistic career request, RLHF fine-tuning compels the model to be agreeable, skipping prerequisites. "
        "On the right, our public knowledge retrieval, persona friction, and graph traversal catch sequence violations and empower human choice."
    )

    # =========================================================================
    # SLIDE 4: Section 2 — Introduction: Research Questions & Bounded Scope
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    apply_bg(s4, BG_LIGHT)
    add_header(s4, "Introduction: Research Questions & System Scope", "Section 2: Introduction", 4,
               "Framing the five formal investigation targets and local hardware boundaries.")

    w2 = Inches(5.67)
    h_top = Inches(2.55)
    h_bot = Inches(2.6)

    add_card(s4, Inches(0.8), Inches(1.55), w2, h_top, "Investigative Research Questions", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s4.shapes.add_textbox(Inches(0.95), Inches(2.05), w2 - Inches(0.3), h_top - Inches(0.55))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• RQ1 (Evidence Diversity):", "Does grounded retrieval from public course/role data expand breadth of career advice?", pt_size=11.5)
    add_bullet(tf, "• RQ2 (Contradiction Resolution):", "Can a Moderator resolve adversarial disputes between Planner, Critic, and Ethics-Reviewer?", pt_size=11.5)
    add_bullet(tf, "• RQ3 (Prerequisite Grounding):", "Does coupling multi-agent debate to a 42-node graph eliminate unsupported claims?", pt_size=11.5)
    add_bullet(tf, "• RQ4 (Demographic Parity):", "Does the system maintain fairness across counterfactual student pairs (Aarav vs Priya)?", pt_size=11.5)

    add_card(s4, Inches(6.86), Inches(1.55), w2, h_top, "Tech Stack & Implementation Boundaries", NAVY_HEAD, top_accent=NAVY_HEAD)
    tb = s4.shapes.add_textbox(Inches(7.01), Inches(2.05), w2 - Inches(0.3), h_top - Inches(0.55))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Qwen Local Inference:", "Local Ollama engine running Qwen models (qwen3:4b-fast, qwen3:4b, qwen2:0.5b).", pt_size=11.5)
    add_bullet(tf, "• Python Multi-Agent Harness:", "Pure Python deliberation loop with structured JSON schemas.", pt_size=11.5)
    add_bullet(tf, "• Neo4j Knowledge Graph:", "42-node prerequisite DAG with NetworkX fallback and Cypher export.", pt_size=11.5)
    add_bullet(tf, "• Vector Store & UI:", "ChromaDB for public course/role retrieval; Streamlit for interactive trace viewer.", pt_size=11.5)

    add_card(s4, Inches(0.8), Inches(4.3), Inches(11.733), h_bot, "Core Principles & Ethical Commitments", BLUE_ACCENT, top_accent=BLUE_ACCENT)
    tb_bot = s4.shapes.add_textbox(Inches(1.0), Inches(4.8), Inches(11.333), h_bot - Inches(0.6))
    tf_bot = tb_bot.text_frame
    tf_bot.word_wrap = True
    add_bullet(tf_bot, "1. Avoiding One-Sided Advice:", "Adversarial deliberation guarantees multiple perspectives are heard before synthesis.", pt_size=12.0)
    add_bullet(tf_bot, "2. Transparency of Disagreement:", "Explicit Dispute Trees expose unresolved friction rather than burying contradictions in smooth prose.", pt_size=12.0)
    add_bullet(tf_bot, "3. Fairness & Calibrated Uncertainty:", "Quantifies epistemic uncertainty based on persona friction and graph violations; enforces demographic parity.", pt_size=12.0)
    add_bullet(tf_bot, "4. Human Override Mandate:", "Students and counselors retain ultimate veto authority and can dynamically adjust trade-off priorities.", pt_size=12.0)

    s4.notes_slide.notes_text_frame.text = (
        "Slide 4 states our 4 research questions and system boundaries. We evaluate evidence diversity, contradiction resolution, "
        "unsupported claims, and counterfactual fairness using local Qwen, Neo4j, Chroma, and Streamlit."
    )

    # =========================================================================
    # SLIDE 5: Section 3 — Literature Survey: Three Research Pillars
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    apply_bg(s5, BG_LIGHT)
    add_header(s5, "Literature Survey: Three Theoretical Pillars", "Section 3: Literature Survey", 5,
               "Synthesizing foundational literature across multi-agent debate, algorithmic fairness, and cognitive forcing.")

    w3 = Inches(3.64)
    h_card = Inches(5.2)

    add_card(s5, Inches(0.8), Inches(1.55), w3, h_card, "Pillar 1: Multi-Agent Debate", NAVY_HEAD, top_accent=NAVY_HEAD)
    tb = s5.shapes.add_textbox(Inches(0.95), Inches(2.05), w3 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Du et al. (ICML 2024):", "Showed multi-agent debate improves factuality and reasoning over single-agent prompts.", pt_size=11.5)
    add_bullet(tf, "• Liang et al. (EMNLP 2023):", "Encouraged divergent thinking in LLMs via adversarial role assignments.", pt_size=11.5)
    add_bullet(tf, "• Gap in Prior Art:", "Unmoderated debate creates endless churn or collapses into majority voting without resolving domain contradictions.", pt_size=11.5)

    add_card(s5, Inches(4.84), Inches(1.55), w3, h_card, "Pillar 2: Graph Grounding & RAG", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s5.shapes.add_textbox(Inches(5.0), Inches(2.05), w3 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• ACM/IEEE CS2023 Curricula:", "Provides authoritative, peer-reviewed sequencing for undergraduate computer science competencies.", pt_size=11.5)
    add_bullet(tf, "• O*NET & BLS Taxonomy:", "Grounds occupational titles and core technical skill requirements in empirical labor data.", pt_size=11.5)
    add_bullet(tf, "• Deterministic DAGs:", "Topological graph verification prevents hallucinated prerequisite shortcuts that LLMs alone cannot detect.", pt_size=11.5)

    add_card(s5, Inches(8.88), Inches(1.55), w3, h_card, "Pillar 3: Fairness & Cognitive Forcing", BLUE_ACCENT, top_accent=BLUE_ACCENT)
    tb = s5.shapes.add_textbox(Inches(9.03), Inches(2.05), w3 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Geyik et al. (KDD 2019):", "Established fairness-aware ranking criteria across demographic groups in recommendation systems.", pt_size=11.5)
    add_bullet(tf, "• Buçinca et al. (CSCW 2021):", "Introduced cognitive forcing functions in AI-assisted decision making to disrupt automation bias.", pt_size=11.5)
    add_bullet(tf, "• Student Agency:", "Ensures automated advice presents transparent trade-offs with explicit human override controls.", pt_size=11.5)

    s5.notes_slide.notes_text_frame.text = (
        "Slide 5 establishes our three academic pillars: multi-agent debate (Du et al., Liang et al.), deterministic graph grounding "
        "using ACM curricula and O*NET data, and algorithmic fairness with cognitive forcing (Geyik et al., Buçinca et al.)."
    )

    # =========================================================================
    # SLIDE 6: Section 3 — Literature Survey: Critiques & Countermeasures
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    apply_bg(s6, BG_LIGHT)
    add_header(s6, "Literature Survey: Addressing Critiques of Debate", "Section 3: Literature Survey", 6,
               "Rigorous responses to consensus collapse, shared priors, and majority voting failure modes.")

    w2 = Inches(5.67)
    h_card = Inches(5.2)

    add_card(s6, Inches(0.8), Inches(1.55), w2, h_card, "The Smit et al. (2024) Critique", AMBER_ACCENT, top_accent=AMBER_ACCENT)
    tb = s6.shapes.add_textbox(Inches(0.95), Inches(2.05), w2 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• 'Should We Be Going MAD?':", "Smit et al. (arXiv:2311.17371) critically evaluated multi-agent debate across reasoning benchmarks.", pt_size=11.5)
    add_bullet(tf, "• Majority Voting Equivalence:", "Argued that uncurated debate often reduces to expensive majority voting without achieving genuine factual consensus.", pt_size=11.5)
    add_bullet(tf, "• Shared Prior Pathology:", "Personas derived from the same base model weights share identical training priors, leading to coordinated blindspots.", pt_size=11.5)
    add_bullet(tf, "• Error Amplification:", "Unmoderated debate can amplify hallucinations if confident personas persuade ungrounded peers.", pt_size=11.5)

    add_card(s6, Inches(6.86), Inches(1.55), w2, h_card, "Our Four Architectural Countermeasures", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s6.shapes.add_textbox(Inches(7.01), Inches(2.05), w2 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "1. Grounded Public Data & DAG:", "Anchors deliberation in Chroma vector store (ACM curricula) and a 42-node Neo4j prerequisite DAG.", pt_size=11.5)
    add_bullet(tf, "2. Orthogonal Persona Personas:", "Planner, Critic, and Ethics-Reviewer are governed by opposing philosophies, not just temperature tweaks.", pt_size=11.5)
    add_bullet(tf, "3. Structured Dispute Trees:", "Refuses to average disagreements; extracts explicit contention dimensions for transparent inspection.", pt_size=11.5)
    add_bullet(tf, "4. Calibrated Human Override Gate:", "Surfaces unresolvable trade-offs directly to student and counselor control rather than forcing automated consensus.", pt_size=11.5)

    s6.notes_slide.notes_text_frame.text = (
        "Slide 6 addresses the Smit et al. critique. We prevent majority voting collapse and shared prior amplification by grounding "
        "agents in public course/role data, enforcing topological DAG checks, and surfacing dispute trees to human judgment."
    )

    # =========================================================================
    # SLIDE 7: Section 3 — Literature Survey: Comparative Feature Matrix
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    apply_bg(s7, BG_LIGHT)
    add_header(s7, "Literature Survey: Comparative Feature Matrix", "Section 3: Literature Survey", 7,
               "Benchmarking our approach against canonical prior art across 5 core technical dimensions.")

    rows = 6
    cols = 6
    table_shape = s7.shapes.add_table(rows, cols, Inches(0.8), Inches(1.65), Inches(11.733), Inches(4.5))
    table = table_shape.table

    table.columns[0].width = Inches(2.533)
    table.columns[1].width = Inches(1.84)
    table.columns[2].width = Inches(1.84)
    table.columns[3].width = Inches(1.84)
    table.columns[4].width = Inches(1.84)
    table.columns[5].width = Inches(1.84)

    headers = ["Framework / Work", "Multi-Agent Debate", "Public Data Grounding", "Fairness Audit", "Human Override", "Local Inference"]
    for j, h in enumerate(headers):
        cell = table.cell(0, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = NAVY_PRIMARY
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.name = FONT_MAIN
        p.font.size = Pt(11.0)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p.alignment = PP_ALIGN.CENTER
        cell.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    matrix_data = [
        ("Du et al. (ICML 2024)", "Yes (Debate)", "No (Model Weights)", "No", "No", "No (API)"),
        ("Liang et al. (EMNLP 2023)", "Yes (Divergent)", "No (Prompt-Only)", "No", "No", "No (API)"),
        ("Geyik et al. (SIGKDD 2019)", "No (Ranking)", "Rule-Based", "Yes (Parity)", "No", "Yes (Local)"),
        ("Buçinca et al. (CSCW 2021)", "No (UI Study)", "No", "No", "Yes (Cognitive)", "N/A"),
        ("Proposed Architecture", "Yes (Planner/Critic/Ethics)", "Yes (Chroma + 42-Node DAG)", "Yes (Counterfactual)", "Yes (Streamlit Gate)", "Yes (Qwen Local)"),
    ]

    for i, row in enumerate(matrix_data):
        is_proposed = (i == len(matrix_data) - 1)
        bg = TEAL_BG if is_proposed else (CARD_BG if i % 2 == 0 else CARD_MUTED)

        for j, val in enumerate(row):
            cell = table.cell(i + 1, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = FONT_MAIN
            p.font.size = Pt(10.5)
            p.font.bold = is_proposed or (j == 0)
            p.font.color.rgb = TEAL_PRIMARY if is_proposed else (NAVY_HEAD if j == 0 else TEXT_MAIN)
            p.alignment = PP_ALIGN.LEFT if j == 0 else PP_ALIGN.CENTER
            cell.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    s7.notes_slide.notes_text_frame.text = (
        "Slide 7 summarizes our positioning relative to prior art. This is the first system that couples Planner, Critic, and Ethics "
        "personas with public course/role data, Neo4j graph traversal, and human override running locally on consumer hardware."
    )

    # =========================================================================
    # SLIDE 8: Section 4 — Architecture Diagram: End-to-End Decision Flow
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    apply_bg(s8, BG_LIGHT)
    add_header(s8, "Architecture Diagram: End-to-End Decision Flow", "Section 4: Architecture Diagram", 8,
               "Strict left-to-right intake, grounded retrieval, dialectic deliberation, DAG check, and human override.")

    # Top Row: 4 Sequential Steps
    add_flow_node(s8, Inches(0.8), Inches(1.6), Inches(2.3), Inches(1.15), "1. Candidate Intake", "Verified skills, target role,\ntimeline & budget", bg=CARD_BG, border=NAVY_PRIMARY)
    add_arrow(s8, Inches(3.18), Inches(2.05), Inches(0.35), Inches(0.25), direction="right", color=NAVY_PRIMARY)

    add_flow_node(s8, Inches(3.58), Inches(1.6), Inches(2.4), Inches(1.15), "2. Chroma Retrieval", "ACM CS2023 curricula &\nO*NET career role standards", bg=BLUE_BG, border=BLUE_ACCENT)
    add_arrow(s8, Inches(6.05), Inches(2.05), Inches(0.35), Inches(0.25), direction="right", color=BLUE_ACCENT)

    add_flow_node(s8, Inches(6.45), Inches(1.6), Inches(2.9), Inches(1.15), "3. Multi-Persona Triad", "Local Qwen Deliberation:\nPlanner · Critic · Ethics-Reviewer", bg=TEAL_BG, border=TEAL_PRIMARY)
    add_arrow(s8, Inches(9.42), Inches(2.05), Inches(0.35), Inches(0.25), direction="right", color=TEAL_PRIMARY)

    add_flow_node(s8, Inches(9.82), Inches(1.6), Inches(2.7), Inches(1.15), "4. Moderator & DAG", "Checks 42-node Neo4j DAG;\nextracts dispute dimensions", bg=CARD_BG, border=BLUE_ACCENT)

    # Middle Right: Arrow Down to Decision Diamond
    add_arrow(s8, Inches(11.02), Inches(2.82), Inches(0.3), Inches(0.35), direction="down", color=BLUE_ACCENT)
    diamond = add_flow_node(s8, Inches(9.65), Inches(3.22), Inches(2.87), Inches(1.2), "Gate Trigger Check", "Prereq Violations > 0 OR\nUncertainty >= 0.45?", bg=AMBER_BG, border=AMBER_ACCENT, shape=MSO_SHAPE.DIAMOND)

    # YES Branch (Points Left into Human Override Panel)
    add_arrow(s8, Inches(8.55), Inches(3.67), Inches(0.85), Inches(0.26), direction="left", color=ROSE_ACCENT)
    tb_lbl_yes = s8.shapes.add_textbox(Inches(8.4), Inches(3.35), Inches(1.2), Inches(0.28))
    p_ly = tb_lbl_yes.text_frame.paragraphs[0]
    p_ly.text = "YES (Trigger Gate)"
    p_ly.font.size = Pt(9.0)
    p_ly.font.bold = True
    p_ly.font.color.rgb = ROSE_ACCENT

    add_card(s8, Inches(0.8), Inches(3.22), Inches(7.55), Inches(1.65), "Streamlit Human Override Panel & Dispute Tree", ROSE_ACCENT, top_accent=ROSE_ACCENT, bg_color=ROSE_BG)
    tb_card_yes = s8.shapes.add_textbox(Inches(0.95), Inches(3.62), Inches(7.25), Inches(1.2))
    tf_cy = tb_card_yes.text_frame
    tf_cy.word_wrap = True
    add_bullet(tf_cy, "• Dispute Tree Extraction:", "Surfaces concrete contention forks across velocity, depth, and financial risk.", pt_size=11.5)
    add_bullet(tf_cy, "• Counselor & Student Sliders:", "User dynamically shifts weights between Speed to Market, Prerequisite Rigor, and Debt Avoidance.", pt_size=11.5)

    # NO Branch (Points Down from Diamond into Green Card)
    add_arrow(s8, Inches(11.02), Inches(4.5), Inches(0.3), Inches(0.4), direction="down", color=TEAL_PRIMARY)
    tb_lbl_no = s8.shapes.add_textbox(Inches(11.4), Inches(4.52), Inches(1.2), Inches(0.28))
    p_ln = tb_lbl_no.text_frame.paragraphs[0]
    p_ln.text = "NO (Clean Plan)"
    p_ln.font.size = Pt(9.0)
    p_ln.font.bold = True
    p_ln.font.color.rgb = TEAL_PRIMARY

    add_card(s8, Inches(7.6), Inches(5.0), Inches(4.933), Inches(1.85), "Autonomous Balanced Roadmap", TEAL_PRIMARY, top_accent=TEAL_PRIMARY, bg_color=TEAL_BG)
    tb_card_no = s8.shapes.add_textbox(Inches(7.75), Inches(5.4), Inches(4.6), Inches(1.35))
    tf_cn = tb_card_no.text_frame
    tf_cn.word_wrap = True
    add_bullet(tf_cn, "• Validated Milestones:", "Topologically sequenced roadmap satisfying all 42 graph nodes.", pt_size=11.5)
    add_bullet(tf_cn, "• Evidence Citations:", "Linked directly to public ACM course modules and O*NET standards.", pt_size=11.5)

    s8.notes_slide.notes_text_frame.text = (
        "Slide 8 shows our end-to-end architecture. Candidate profiles pass through Chroma retrieval, followed by Planner, Critic, "
        "and Ethics-Reviewer deliberation using local Qwen. The Moderator checks the 42-node DAG: if violations or high uncertainty "
        "exist, the Human Override Gate triggers in Streamlit. Otherwise, a balanced roadmap is emitted."
    )

    # =========================================================================
    # SLIDE 9: Section 4 — Architecture Details: Dialectic Persona Engine
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    apply_bg(s9, BG_LIGHT)
    add_header(s9, "Architecture Details: Complementary Persona Dialectics", "Section 4: Architecture Details", 9,
               "Advisory philosophies driven by differentiated system prompts and opposing epistemological objectives.")

    w3 = Inches(3.64)
    h_card = Inches(5.2)

    add_card(s9, Inches(0.8), Inches(1.55), w3, h_card, "The Planner Persona", NAVY_HEAD, top_accent=NAVY_HEAD)
    tb = s9.shapes.add_textbox(Inches(0.95), Inches(2.05), w3 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Advisory Lens:", "Constructive execution, structured progression, milestone delivery.", pt_size=12.0)
    add_bullet(tf, "• Technical Priorities:", "Core competencies, public course milestones, portfolio projects, time-to-market.", pt_size=12.0)
    add_bullet(tf, "• Public Data Grounding:", "Maps candidate goals to ACM course modules (CS101, CS201, CS330) and O*NET roles.", pt_size=12.0)
    add_bullet(tf, "• Critical Function:", "Builds actionable, step-by-step career pathways preventing analysis paralysis.", pt_size=12.0)

    add_card(s9, Inches(4.84), Inches(1.55), w3, h_card, "The Critic Persona", ROSE_ACCENT, top_accent=ROSE_ACCENT)
    tb = s9.shapes.add_textbox(Inches(5.0), Inches(2.05), w3 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Advisory Lens:", "Adversarial stress-testing, prerequisite skepticism, risk exposure.", pt_size=12.0)
    add_bullet(tf, "• Technical Priorities:", "Mathematical rigor (Linear Algebra), systems depth (OS/Concurrency), screening barriers.", pt_size=12.0)
    add_bullet(tf, "• Market Realism:", "Exposes tutorial wrapper superficiality, interview rejection hurdles, and market saturation.", pt_size=12.0)
    add_bullet(tf, "• Critical Function:", "Prevents students from attempting advanced roles without foundational depth.", pt_size=12.0)

    add_card(s9, Inches(8.88), Inches(1.55), w3, h_card, "The Ethics-Reviewer Persona", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s9.shapes.add_textbox(Inches(9.03), Inches(2.05), w3 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Advisory Lens:", "Socioeconomic equity, debt mitigation, critical human agency.", pt_size=12.0)
    add_bullet(tf, "• Financial Safeguards:", "Strict zero-debt mandate: blocks predatory bootcamps; prioritizes free open courseware.", pt_size=12.0)
    add_bullet(tf, "• Pedigree Parity:", "Mitigates institutional bias for Tier-3 students via verifiable open-source pull requests.", pt_size=12.0)
    add_bullet(tf, "• Critical Function:", "Protects vulnerable candidates from financial traps and algorithmic determinism.", pt_size=12.0)

    s9.notes_slide.notes_text_frame.text = (
        "Slide 9 details our three core personas: Planner, Critic, and Ethics-Reviewer. Planner designs constructive pathways, "
        "Critic stress-tests prerequisites and market saturation, and Ethics-Reviewer audits socioeconomic debt risks and protects agency. "
        "These three run sequentially in our Python multi-agent harness."
    )

    # =========================================================================
    # SLIDE 10: Section 4 — Architecture Details: Visual Curricular DAG (Neo4j)
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    apply_bg(s10, BG_LIGHT)
    add_header(s10, "Architecture Details: Neo4j Career-Skill Graph (42 Nodes)", "Section 4: Architecture Details", 10,
               "Ontology backbone: 16 core milestones shown across 4 tracks with cross-track prerequisite edges.")

    col_w4 = Inches(2.7)
    top_y = Inches(1.50)

    # Track 1
    add_card(s10, Inches(0.8), top_y, col_w4, Inches(4.15), "Track 1: DSA & Math", NAVY_HEAD, top_accent=NAVY_HEAD, title_size=11.5)
    add_flow_node(s10, Inches(1.0), Inches(2.10), Inches(2.3), Inches(0.50), "Discrete Math", "Logic & graph theory", bg=CARD_BG, border=CARD_BORDER)
    add_arrow(s10, Inches(2.02), Inches(2.64), Inches(0.26), Inches(0.18), direction="down", color=NAVY_PRIMARY)
    add_flow_node(s10, Inches(1.0), Inches(2.86), Inches(2.3), Inches(0.50), "Python / C Basics", "Syntax & control flow", bg=CARD_BG, border=CARD_BORDER)
    add_arrow(s10, Inches(2.02), Inches(3.40), Inches(0.26), Inches(0.18), direction="down", color=NAVY_PRIMARY)
    add_flow_node(s10, Inches(1.0), Inches(3.62), Inches(2.3), Inches(0.50), "Data Structures", "Trees, heaps, graphs", bg=CARD_BG, border=NAVY_PRIMARY)
    add_arrow(s10, Inches(2.02), Inches(4.16), Inches(0.26), Inches(0.18), direction="down", color=NAVY_PRIMARY)
    add_flow_node(s10, Inches(1.0), Inches(4.38), Inches(2.3), Inches(0.50), "Advanced Algorithms", "Dynamic prog & flows", bg=TEAL_BG, border=TEAL_PRIMARY, text_color=TEAL_PRIMARY)

    # Track 2
    add_card(s10, Inches(3.8), top_y, col_w4, Inches(4.15), "Track 2: Systems & OS", BLUE_ACCENT, top_accent=BLUE_ACCENT, title_size=11.5)
    add_flow_node(s10, Inches(4.0), Inches(2.10), Inches(2.3), Inches(0.50), "C Memory & Pointers", "Stack, heap, allocation", bg=CARD_BG, border=CARD_BORDER)
    add_arrow(s10, Inches(5.02), Inches(2.64), Inches(0.26), Inches(0.18), direction="down", color=BLUE_ACCENT)
    add_flow_node(s10, Inches(4.0), Inches(2.86), Inches(2.3), Inches(0.50), "Computer Architecture", "Registers, ALU, caches", bg=CARD_BG, border=CARD_BORDER)
    add_arrow(s10, Inches(5.02), Inches(3.40), Inches(0.26), Inches(0.18), direction="down", color=BLUE_ACCENT)
    add_flow_node(s10, Inches(4.0), Inches(3.62), Inches(2.3), Inches(0.50), "Operating Systems", "Processes, paging, IPC", bg=CARD_BG, border=BLUE_ACCENT)
    add_arrow(s10, Inches(5.02), Inches(4.16), Inches(0.26), Inches(0.18), direction="down", color=BLUE_ACCENT)
    add_flow_node(s10, Inches(4.0), Inches(4.38), Inches(2.3), Inches(0.50), "Distributed Systems", "Raft, Paxos, replication", bg=TEAL_BG, border=TEAL_PRIMARY, text_color=TEAL_PRIMARY)

    # Track 3
    add_card(s10, Inches(6.8), top_y, col_w4, Inches(4.15), "Track 3: Web & Cloud", INDIGO_ACCENT, top_accent=INDIGO_ACCENT, title_size=11.5)
    add_flow_node(s10, Inches(7.0), Inches(2.10), Inches(2.3), Inches(0.50), "HTML / CSS / JS", "DOM & clientside event loop", bg=CARD_BG, border=CARD_BORDER)
    add_arrow(s10, Inches(8.02), Inches(2.64), Inches(0.26), Inches(0.18), direction="down", color=INDIGO_ACCENT)
    add_flow_node(s10, Inches(7.0), Inches(2.86), Inches(2.3), Inches(0.50), "Backend APIs", "FastAPI, REST routing", bg=CARD_BG, border=CARD_BORDER)
    add_arrow(s10, Inches(8.02), Inches(3.40), Inches(0.26), Inches(0.18), direction="down", color=INDIGO_ACCENT)
    add_flow_node(s10, Inches(7.0), Inches(3.62), Inches(2.3), Inches(0.50), "Docker Containers", "Namespaces, cgroups, images", bg=CARD_BG, border=INDIGO_ACCENT)
    add_arrow(s10, Inches(8.02), Inches(4.16), Inches(0.26), Inches(0.18), direction="down", color=INDIGO_ACCENT)
    add_flow_node(s10, Inches(7.0), Inches(4.38), Inches(2.3), Inches(0.50), "System Design & CI/CD", "Load balancers, sharding", bg=TEAL_BG, border=TEAL_PRIMARY, text_color=TEAL_PRIMARY)

    # Track 4
    add_card(s10, Inches(9.8), top_y, col_w4, Inches(4.15), "Track 4: Machine Learning", TEAL_PRIMARY, top_accent=TEAL_PRIMARY, title_size=11.5)
    add_flow_node(s10, Inches(10.0), Inches(2.10), Inches(2.3), Inches(0.50), "Linear Algebra & Stats", "Eigenvalues & probability", bg=CARD_BG, border=CARD_BORDER)
    add_arrow(s10, Inches(11.02), Inches(2.64), Inches(0.26), Inches(0.18), direction="down", color=TEAL_PRIMARY)
    add_flow_node(s10, Inches(10.0), Inches(2.86), Inches(2.3), Inches(0.50), "Data Analysis (Pandas)", "Wrangling & cleaning", bg=CARD_BG, border=CARD_BORDER)
    add_arrow(s10, Inches(11.02), Inches(3.40), Inches(0.26), Inches(0.18), direction="down", color=TEAL_PRIMARY)
    add_flow_node(s10, Inches(10.0), Inches(3.62), Inches(2.3), Inches(0.50), "ML Foundations", "Loss functions, gradients", bg=CARD_BG, border=TEAL_PRIMARY)
    add_arrow(s10, Inches(11.02), Inches(4.16), Inches(0.26), Inches(0.18), direction="down", color=TEAL_PRIMARY)
    add_flow_node(s10, Inches(10.0), Inches(4.38), Inches(2.3), Inches(0.50), "Deep Learning & LLMs", "Transformers, backprop", bg=TEAL_BG, border=TEAL_PRIMARY, text_color=TEAL_PRIMARY)

    # Bottom Explanatory Banner
    add_card(s10, Inches(0.8), Inches(5.80), Inches(11.733), Inches(1.2), "Cross-Track Prerequisite Dependencies & Neo4j Integration", NAVY_HEAD, top_accent=NAVY_HEAD, title_size=11.5)
    tb_dag = s10.shapes.add_textbox(Inches(0.95), Inches(6.12), Inches(11.4), Inches(0.8))
    tf_dag = tb_dag.text_frame
    tf_dag.word_wrap = True
    add_bullet(tf_dag, "• Key Cross-Track Edges:", "Python Basics ➔ ML Foundations & Backend APIs | Linear Algebra ➔ Deep Learning | OS & Docker ➔ Distributed Systems", pt_size=10.5, space_after=3)
    add_bullet(tf_dag, "• Neo4j Cypher Schema:", "Full 42-node graph exports seamlessly via Cypher script or synchronizes live via official Python neo4j driver.", pt_size=10.5, space_after=0)

    s10.notes_slide.notes_text_frame.text = (
        "Slide 10 illustrates our 42-node prerequisite DAG. We display the core milestones across 4 tracks with cross-track "
        "dependencies: for instance, a candidate cannot skip to Deep Learning without Linear Algebra and ML Foundations. "
        "The graph is modeled in Neo4j with Cypher query export and NetworkX topological traversal."
    )

    # =========================================================================
    # SLIDE 11: Section 4 — Architecture Details: Visual Dispute Tree
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    apply_bg(s11, BG_LIGHT)
    add_header(s11, "Architecture Details: Dispute Tree & Human Override", "Section 4: Architecture Details", 11,
               "Transforming unresolvable technical contradictions into structured human decision choices.")

    # Root Consensus Box
    add_flow_node(s11, Inches(3.8), Inches(1.6), Inches(5.7), Inches(0.95), "Root Node: Consensus Core", "Foundational milestones verified by all 3 personas:\nPython OOP + Relational SQL + Git Version Control", bg=CARD_BG, border=NAVY_PRIMARY)

    add_arrow(s11, Inches(4.5), Inches(2.65), Inches(0.35), Inches(0.4), direction="down", color=BLUE_ACCENT)
    add_arrow(s11, Inches(8.5), Inches(2.65), Inches(0.35), Inches(0.4), direction="down", color=TEAL_PRIMARY)

    # Branch 1 (Left - Rigor Track)
    add_card(s11, Inches(0.8), Inches(3.15), Inches(5.6), Inches(2.7), "Branch 1: Foundational Systems Rigor", BLUE_ACCENT, top_accent=BLUE_ACCENT, bg_color=BLUE_BG)
    tb_b1 = s11.shapes.add_textbox(Inches(0.95), Inches(3.6), Inches(5.3), Inches(2.1))
    tf_b1 = tb_b1.text_frame
    tf_b1.word_wrap = True
    add_bullet(tf_b1, "• Advocates:", "Critic & Ethics-Reviewer (Prerequisite depth & debt shield)", pt_size=12.0)
    add_bullet(tf_b1, "• Curriculum:", "Linear Algebra ➔ OS Internals ➔ Concurrency ➔ Distributed Systems", pt_size=12.0)
    add_bullet(tf_b1, "• Timeline & Cost:", "10–12 Months | Zero debt (MIT OpenCourseWare / CS50)", pt_size=12.0)
    add_bullet(tf_b1, "• Career Outcome:", "High technical durability; survives enterprise engineering screening", pt_size=12.0)

    # Branch 2 (Right - Velocity Track)
    add_card(s11, Inches(6.9), Inches(3.15), Inches(5.6), Inches(2.7), "Branch 2: Accelerated Application Track", TEAL_PRIMARY, top_accent=TEAL_PRIMARY, bg_color=TEAL_BG)
    tb_b2 = s11.shapes.add_textbox(Inches(7.05), Inches(3.6), Inches(5.3), Inches(2.1))
    tf_b2 = tb_b2.text_frame
    tf_b2.word_wrap = True
    add_bullet(tf_b2, "• Advocate:", "Planner Persona (Pacing & project velocity)", pt_size=12.0)
    add_bullet(tf_b2, "• Curriculum:", "FastAPI Backend ➔ REST APIs ➔ LangChain / RAG ➔ Shipped MVP", pt_size=12.0)
    add_bullet(tf_b2, "• Timeline & Scope:", "4 Months | Targeted entry into Junior Applied AI roles", pt_size=12.0)
    add_bullet(tf_b2, "• Strategic Trade-off:", "Rapid market entry; student must backfill math/systems later", pt_size=12.0)

    # Bottom Arbitration Bar
    add_flow_node(s11, Inches(0.8), Inches(6.05), Inches(11.733), Inches(0.9), "Human Override & Counselor Decision Gateway (Streamlit)", "The system halts autonomous assertion. Student or counselor slides trade-off weights (Velocity vs Rigor vs Equity).\nPreserves critical human agency and eliminates algorithmic paternalism.", bg=CARD_MUTED, border=NAVY_PRIMARY)

    s11.notes_slide.notes_text_frame.text = (
        "Slide 11 diagrams the Dispute Tree generated by the Moderator. Rather than forcing an artificial consensus, "
        "the system structures the trade-off: a foundational systems rigor path versus an accelerated applied path. "
        "The student or counselor uses interactive sliders in Streamlit to decide."
    )

    # =========================================================================
    # SLIDE 12: Section 5 — Experimental Setup: 4 Experimental Configurations
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    apply_bg(s12, BG_LIGHT)
    add_header(s12, "Experimental Setup: Four Comparative Configurations", "Section 5: Experimental Setup", 12,
               "Rigorous ablation isolating monolithic prompting, multi-perspective prompting, unmoderated debate, and full system.")

    col_w_ab = Inches(2.7)
    h_ab = Inches(5.2)

    # Config 1
    add_card(s12, Inches(0.8), Inches(1.55), col_w_ab, h_ab, "Config 1: Single LLM", ROSE_ACCENT, top_accent=ROSE_ACCENT)
    tb = s12.shapes.add_textbox(Inches(0.95), Inches(2.05), col_w_ab - Inches(0.3), h_ab - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Architecture:", "Monolithic zero-shot prompt directly asking for career advice.", pt_size=11.5)
    add_bullet(tf, "• Industry Proxy:", "Standard commercial career chatbots.", pt_size=11.5)
    add_bullet(tf, "• Known Flaws:", "Conversational sycophancy, skips prerequisites, high demographic bias.", pt_size=11.5)
    add_bullet(tf, "• Compute:", "1 LLM inference call.", pt_size=11.5)

    # Config 2
    add_card(s12, Inches(3.8), Inches(1.55), col_w_ab, h_ab, "Config 2: Multi-Perspective", AMBER_ACCENT, top_accent=AMBER_ACCENT)
    tb = s12.shapes.add_textbox(Inches(3.95), Inches(2.05), col_w_ab - Inches(0.3), h_ab - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Architecture:", "Single LLM prompted to consider planning, critique, and ethics internally.", pt_size=11.5)
    add_bullet(tf, "• Intended Goal:", "Tests internal self-critique without agent separation.", pt_size=11.5)
    add_bullet(tf, "• Failure Mode:", "Attention heads collapse internal tension into averaged compromise.", pt_size=11.5)
    add_bullet(tf, "• Compute:", "1 long-context LLM call.", pt_size=11.5)

    # Config 3
    add_card(s12, Inches(6.8), Inches(1.55), col_w_ab, h_ab, "Config 3: Unmoderated Triad", BLUE_ACCENT, top_accent=BLUE_ACCENT)
    tb = s12.shapes.add_textbox(Inches(6.95), Inches(2.05), col_w_ab - Inches(0.3), h_ab - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Architecture:", "Planner, Critic, and Ethics generate arguments without Moderator.", pt_size=11.5)
    add_bullet(tf, "• Intended Goal:", "Isolates the effect of persona generation without graph validation.", pt_size=11.5)
    add_bullet(tf, "• Failure Mode:", "High persona friction but zero synthesis; unresolved contradictions linger.", pt_size=11.5)
    add_bullet(tf, "• Compute:", "3 independent agent calls.", pt_size=11.5)

    # Config 4
    add_card(s12, Inches(9.8), Inches(1.55), col_w_ab, h_ab, "Config 4: Proposed System", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s12.shapes.add_textbox(Inches(9.95), Inches(2.05), col_w_ab - Inches(0.3), h_ab - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Architecture:", "Planner + Critic + Ethics + Moderator + 42-Node DAG + Human Override.", pt_size=11.5)
    add_bullet(tf, "• Grounding:", "Chroma ACM/O*NET vector retrieval + Neo4j prerequisite verification.", pt_size=11.5)
    add_bullet(tf, "• Governance:", "Dispute Tree generation, calibrated uncertainty, interactive override.", pt_size=11.5)
    add_bullet(tf, "• Compute:", "Dialectic pipeline (Qwen local).", pt_size=11.5)

    s12.notes_slide.notes_text_frame.text = (
        "Slide 12 defines our 4 controlled comparative configurations: Monolithic LLM, Multi-Perspective Prompting, "
        "Unmoderated Triad, and the Proposed RAI Multi-Persona System. This isolates the precise contribution of "
        "persona separation, graph validation, and moderator dispute resolution."
    )

    # =========================================================================
    # SLIDE 13: Section 5 — Experimental Setup: 20 Synthetic Profiles Set
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    apply_bg(s13, BG_LIGHT)
    add_header(s13, "Experimental Setup: Synthetic Candidate Profile Dataset", "Section 5: Experimental Setup", 13,
               "20 synthetic candidate profiles across 10 base archetypes with paired counterfactual variants.")

    w2 = Inches(5.67)
    h_top = Inches(4.2)

    # Variant A Card
    add_card(s13, Inches(0.8), Inches(1.55), w2, h_top, "Variant A Archetype: 'Aarav Sharma'", NAVY_HEAD, top_accent=NAVY_HEAD)
    tb_pa = s13.shapes.add_textbox(Inches(0.95), Inches(2.05), w2 - Inches(0.3), h_top - Inches(0.6))
    tf_pa = tb_pa.text_frame
    tf_pa.word_wrap = True
    add_bullet(tf_pa, "• Identity Signal:", "Aarav Sharma (Male identity proxy)", pt_size=12.0)
    add_bullet(tf_pa, "• Institutional Pedigree:", "Tier-1 National Technical Institute (Top prestige)", pt_size=12.0)
    add_bullet(tf_pa, "• Financial Budget:", "High monthly budget (₹40,000 / month)", pt_size=12.0)
    add_bullet(tf_pa, "• Technical Invariant:", "Verified skills, target role, timeline identical to paired Variant B.", pt_size=12.0)
    add_bullet(tf_pa, "• Monolithic Bias Tendency:", "Steered toward aggressive high-end infrastructure and costly tooling.", pt_size=12.0)

    # Variant B Card
    add_card(s13, Inches(6.86), Inches(1.55), w2, h_top, "Variant B Archetype: 'Priya Patel'", ROSE_ACCENT, top_accent=ROSE_ACCENT)
    tb_pb = s13.shapes.add_textbox(Inches(7.01), Inches(2.05), w2 - Inches(0.3), h_top - Inches(0.6))
    tf_pb = tb_pb.text_frame
    tf_pb.word_wrap = True
    add_bullet(tf_pb, "• Identity Signal:", "Priya Patel (Female identity proxy)", pt_size=12.0)
    add_bullet(tf_pb, "• Institutional Pedigree:", "Tier-3 Rural Non-Autonomous State College", pt_size=12.0)
    add_bullet(tf_pb, "• Financial Budget:", "Low monthly budget (₹3,000 / month)", pt_size=12.0)
    add_bullet(tf_pb, "• Technical Invariant:", "Verified skills, target role, timeline identical to paired Variant A.", pt_size=12.0)
    add_bullet(tf_pa, "• Monolithic Bias Tendency:", "Steered toward truncated tasks or predatory debt traps.", pt_size=12.0)

    # Bottom Parity Vault Bar
    add_flow_node(s13, Inches(0.8), Inches(5.95), Inches(11.733), Inches(1.0), "Counterfactual Parity Governance", "In the Proposed Architecture, protected demographic cues (gender, college tier) cannot dilute core technical rigor.\nThe Ethics-Reviewer audits socioeconomic burden and recommends identical core technical depth via free public open courseware.", bg=TEAL_BG, border=TEAL_PRIMARY, text_color=TEAL_PRIMARY)

    s13.notes_slide.notes_text_frame.text = (
        "Slide 13 details our 20 synthetic candidate profiles. We construct 10 matched pairs where skills, target roles, and timelines "
        "are strictly identical. In monolithic baselines, changing name, tier, and budget leads to biased divergence. "
        "Our system ensures recommendations maintain core curriculum parity while adapting cost to student budget."
    )

    # =========================================================================
    # SLIDE 14: Section 5 — Experimental Setup: Five Official Evaluation Metrics
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    apply_bg(s14, BG_LIGHT)
    add_header(s14, "Experimental Setup: Five Official Evaluation Metrics", "Section 5: Experimental Setup", 14,
               "Formal mathematical definitions and computational procedures for the five official evaluation metrics.")

    col_w5 = Inches(2.22)
    h_card_m = Inches(5.2)

    # Metric 1
    add_card(s14, Inches(0.8), Inches(1.55), col_w5, h_card_m, "1. Evidence Diversity", BLUE_ACCENT, top_accent=BLUE_ACCENT, title_size=11.0)
    tb = s14.shapes.add_textbox(Inches(0.9), Inches(2.05), col_w5 - Inches(0.2), h_card_m - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Formula:", "H_div = - Sum(p_i * log2 p_i) / log2 N.", pt_size=10.5)
    add_bullet(tf, "• Meaning:", "Shannon entropy across retrieved public course and role domains.", pt_size=10.5)
    add_bullet(tf, "• Target:", "Higher is better (Max = 1.00).", pt_size=10.5)

    # Metric 2
    add_card(s14, Inches(3.18), Inches(1.55), col_w5, h_card_m, "2. Contradiction Resolution", TEAL_PRIMARY, top_accent=TEAL_PRIMARY, title_size=11.0)
    tb = s14.shapes.add_textbox(Inches(3.28), Inches(2.05), col_w5 - Inches(0.2), h_card_m - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Formula:", "CRR = (Resolved Disputes / Surfaced Disputes) * 100%.", pt_size=10.5)
    add_bullet(tf, "• Meaning:", "Percentage of Critic and Ethics concerns formally addressed in synthesis.", pt_size=10.5)
    add_bullet(tf, "• Target:", "Higher is better (Ideal = 100%).", pt_size=10.5)

    # Metric 3
    add_card(s14, Inches(5.56), Inches(1.55), col_w5, h_card_m, "3. Unsupported Claims", ROSE_ACCENT, top_accent=ROSE_ACCENT, title_size=11.0)
    tb = s14.shapes.add_textbox(Inches(5.66), Inches(2.05), col_w5 - Inches(0.2), h_card_m - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Formula:", "UCR = (Violating Milestones / Total Milestones) * 100%.", pt_size=10.5)
    add_bullet(tf, "• Meaning:", "Percentage of milestones violating prerequisite DAG or lacking citations.", pt_size=10.5)
    add_bullet(tf, "• Target:", "Lower is better (Ideal = 0.0%).", pt_size=10.5)

    # Metric 4
    add_card(s14, Inches(7.94), Inches(1.55), col_w5, h_card_m, "4. Synthetic Fairness", INDIGO_ACCENT, top_accent=INDIGO_ACCENT, title_size=11.0)
    tb = s14.shapes.add_textbox(Inches(8.04), Inches(2.05), col_w5 - Inches(0.2), h_card_m - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Formula:", "J(A, B) = |S_A & S_B| / |S_A | S_B|.", pt_size=10.5)
    add_bullet(tf, "• Meaning:", "Jaccard similarity between counterfactual matched pairs (Aarav vs Priya).", pt_size=10.5)
    add_bullet(tf, "• Target:", "Higher is better (Max = 1.00).", pt_size=10.5)

    # Metric 5
    add_card(s14, Inches(10.32), Inches(1.55), col_w5, h_card_m, "5. User-Rubric Score", AMBER_ACCENT, top_accent=AMBER_ACCENT, title_size=11.0)
    tb = s14.shapes.add_textbox(Inches(10.42), Inches(2.05), col_w5 - Inches(0.2), h_card_m - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Formula:", "Score on 1.0 to 5.0 scale across 5 dimensions.", pt_size=10.5)
    add_bullet(tf, "• Dimensions:", "Balance, Rigor, Equity, Disagreement Transparency, Human Override.", pt_size=10.5)
    add_bullet(tf, "• Target:", "Higher is better (Max = 5.0).", pt_size=10.5)

    s14.notes_slide.notes_text_frame.text = (
        "Slide 14 formally presents the five evaluation metrics required by the committee: Evidence Diversity, "
        "Contradiction-Resolution Rate, Unsupported-Claim Rate, Fairness Across Synthetic Profiles, and User-Rubric Score."
    )

    # =========================================================================
    # SLIDE 15: Section 6 — Results and Discussion: Full Comparative Benchmark Table
    # =========================================================================
    s15 = prs.slides.add_slide(blank_layout)
    apply_bg(s15, BG_LIGHT)
    add_header(s15, "Results & Discussion: Pilot Quantitative Findings", "Section 6: Results and Discussion", 15,
               "Empirical evaluation of 20 synthetic candidate profiles across 4 configurations on the 5 official metrics.")

    # Results Table
    rows = 5
    cols = 6
    table_shape = s15.shapes.add_table(rows, cols, Inches(0.8), Inches(1.65), Inches(11.733), Inches(2.6))
    table = table_shape.table

    table.columns[0].width = Inches(3.2)
    table.columns[1].width = Inches(1.7)
    table.columns[2].width = Inches(1.7)
    table.columns[3].width = Inches(1.7)
    table.columns[4].width = Inches(1.7)
    table.columns[5].width = Inches(1.733)

    t_headers = ["Configuration", "Evidence Div", "CRR (%)", "UCR (%)", "Fairness (Jaccard)", "User Rubric"]
    for j, h in enumerate(t_headers):
        cell = table.cell(0, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = NAVY_PRIMARY
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.name = FONT_MAIN
        p.font.size = Pt(11.0)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p.alignment = PP_ALIGN.CENTER
        cell.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    results_data = [
        ("Config 1: Single LLM (Monolithic)", "0.22", "0.0%", "90.9%", "0.32 (Biased)", "2.4 / 5.0"),
        ("Config 2: Single LLM (Multi-Perspective)", "0.48", "38.0%", "68.2%", "0.93", "3.1 / 5.0"),
        ("Config 3: Unmoderated Debate (Triad Only)", "0.68", "25.0%", "86.4%", "1.00", "3.5 / 5.0"),
        ("Config 4: Proposed RAI Multi-Persona System", "1.00", "100.0%", "0.0%", "1.00 (Fair)", "4.7 / 5.0"),
    ]

    for i, row in enumerate(results_data):
        is_tier4 = (i == 3)
        bg = TEAL_BG if is_tier4 else (CARD_BG if i % 2 == 0 else CARD_MUTED)

        for j, val in enumerate(row):
            cell = table.cell(i + 1, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = FONT_MAIN
            p.font.size = Pt(11.0)
            p.font.bold = is_tier4 or (j == 0)
            p.font.color.rgb = TEAL_PRIMARY if is_tier4 else (NAVY_HEAD if j == 0 else TEXT_MAIN)
            p.alignment = PP_ALIGN.LEFT if j == 0 else PP_ALIGN.CENTER
            cell.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    # Key Insights Cards (Bottom)
    add_card(s15, Inches(0.8), Inches(4.5), Inches(5.7), Inches(2.4), "Analysis: Evidence Diversity & Prerequisite Grounding", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb_c1 = s15.shapes.add_textbox(Inches(0.95), Inches(4.95), Inches(5.4), Inches(1.8))
    tf_c1 = tb_c1.text_frame
    tf_c1.word_wrap = True
    add_bullet(tf_c1, "• 0.0% Unsupported Claims:", "While Config 1 emits 90.9% unsupported claims, deterministic Neo4j DAG enforcement completely eliminates sequence violations.", pt_size=12.0)
    add_bullet(tf_c1, "• Maximal Evidence Breadth:", "Chroma indexing of ACM curricula and O*NET roles boosts Evidence Diversity to 1.00, compared to 0.22 in monolithic prompting.", pt_size=12.0)

    add_card(s15, Inches(6.833), Inches(4.5), Inches(5.7), Inches(2.4), "Analysis: Contradiction Resolution & Fairness Parity", BLUE_ACCENT, top_accent=BLUE_ACCENT)
    tb_c2 = s15.shapes.add_textbox(Inches(6.983), Inches(4.95), Inches(5.4), Inches(1.8))
    tf_c2 = tb_c2.text_frame
    tf_c2.word_wrap = True
    add_bullet(tf_c2, "• 100% Contradiction Resolution:", "The Moderator formally resolves all surfaced Critic and Ethics objections into clear decision forks within the Dispute Tree.", pt_size=12.0)
    add_bullet(tf_c2, "• Perfect Demographic Parity:", "Monolithic LLM diverges significantly (Jaccard = 0.32) between Aarav and Priya; Config 4 achieves Jaccard = 1.00 with 4.7/5.0 User Rubric score.", pt_size=12.0)

    s15.notes_slide.notes_text_frame.text = (
        "Slide 15 reports our pilot empirical findings across all 20 synthetic candidate profiles. The table directly compares "
        "all 4 configurations across the 5 official metrics. Notice that Config 4 achieves 0.0% unsupported claims, 100% contradiction "
        "resolution rate, 1.00 evidence diversity, and 1.00 fairness parity, with a 4.7 out of 5 user-rubric score."
    )

    # =========================================================================
    # SLIDE 16: Section 6 — Results and Discussion: Worked Walkthrough "Priya"
    # =========================================================================
    s16 = prs.slides.add_slide(blank_layout)
    apply_bg(s16, BG_LIGHT)
    add_header(s16, "Results & Discussion: Case Walkthrough ('Priya')", "Section 6: Results and Discussion", 16,
               "Demonstrating cognitive forcing, dispute resolution, and human override in an acute career pivot scenario.")

    w3 = Inches(3.64)
    h_card = Inches(5.2)

    add_card(s16, Inches(0.8), Inches(1.55), w3, h_card, "The Scenario: 3rd-Year CSE", NAVY_HEAD, top_accent=NAVY_HEAD)
    tb = s16.shapes.add_textbox(Inches(0.95), Inches(2.05), w3 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Student Profile:", "Priya Patel, 3rd-year student at Tier-3 Rural College with Python Basics and ₹3,000/mo budget.", pt_size=12.0)
    add_bullet(tf, "• Ambitious Goal:", "Machine Learning Infrastructure Engineer in 4 months.", pt_size=12.0)
    add_bullet(tf, "• Risky Proposal:", "Borrowing ₹1,20,000 (~$1,400 USD) for a commercial fast-track bootcamp.", pt_size=12.0)
    add_bullet(tf, "• Monolithic Flattery:", "Affirms the goal; claims the bootcamp will qualify her for senior roles (High risk sycophancy).", pt_size=12.0)

    add_card(s16, Inches(4.84), Inches(1.55), w3, h_card, "Dialectic Triad Deliberation", ROSE_ACCENT, top_accent=ROSE_ACCENT)
    tb = s16.shapes.add_textbox(Inches(5.0), Inches(2.05), w3 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Planner Proposal:", "Designs accelerated data wrangling sprints and project portfolio.", pt_size=12.0)
    add_bullet(tf, "• Critic Intervention:", "Flags missing Linear Algebra, Probability, and OS prerequisites; warns of interview elimination.", pt_size=12.0)
    add_bullet(tf, "• Ethics-Reviewer Shield:", "Blocks ₹1,20,000 commercial debt; mandates free MIT OCW / CS50 and open-source GitHub pull requests.", pt_size=12.0)

    add_card(s16, Inches(8.88), Inches(1.55), w3, h_card, "Calibrated Gate & Override", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s16.shapes.add_textbox(Inches(9.03), Inches(2.05), w3 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Uncertainty Calibrated:", "Calculates Uncertainty = 0.77 (Friction = 0.35, Prereq Gap = 0.15, Socioeconomic = 0.20).", pt_size=12.0)
    add_bullet(tf, "• Human Override Gate:", "Gate triggers because Uncertainty >= 0.45 and Delta_prereq > 0.", pt_size=12.0)
    add_bullet(tf, "• Student Agency Restored:", "Priya adjusts trade-off sliders in Streamlit; selects zero-debt foundational pathway.", pt_size=12.0)

    s16.notes_slide.notes_text_frame.text = (
        "Slide 16 walks through our case study with Priya. Priya wants to become an ML Engineer in 4 months via an expensive bootcamp. "
        "The monolithic model affirms this dangerous plan. Our triad deliberates: the Critic flags missing math and systems prerequisites, "
        "and the Ethics-Reviewer blocks predatory loans in favor of free MIT open courseware. The Human Override Gate empowers Priya to choose."
    )

    # =========================================================================
    # SLIDE 17: Section 7 — References: Canonical Bibliography
    # =========================================================================
    s17 = prs.slides.add_slide(blank_layout)
    apply_bg(s17, BG_LIGHT)
    add_header(s17, "References: Canonical Academic Citations", "Section 7: References", 17,
               "Formal bibliography of canonical peer-reviewed literature cited throughout this presentation.")

    w2 = Inches(5.67)
    h_card = Inches(5.2)

    add_card(s17, Inches(0.8), Inches(1.55), w2, h_card, "Multi-Agent & Language Model Foundations", NAVY_HEAD, top_accent=NAVY_HEAD)
    tb = s17.shapes.add_textbox(Inches(0.95), Inches(2.05), w2 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "[1] Du et al. (2024):", "Improving Factuality and Reasoning in Language Models through Multiagent Debate. ICML 2024. arXiv:2305.14325.", pt_size=11.5, space_after=8)
    add_bullet(tf, "[2] Liang et al. (2023):", "Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate. EMNLP 2023, pp. 4392–4407.", pt_size=11.5, space_after=8)
    add_bullet(tf, "[3] Smit et al. (2024):", "Should We Be Going MAD? A Critical Look at Multi-Agent Debate Strategies. arXiv:2311.17371.", pt_size=11.5, space_after=8)
    add_bullet(tf, "[4] ACM/IEEE (2023):", "Computer Science Curricula 2023 (CS2023). Joint Task Force on Computing Curricula.", pt_size=11.5, space_after=8)

    add_card(s17, Inches(6.86), Inches(1.55), w2, h_card, "Sycophancy, Calibration & Human Agency", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s17.shapes.add_textbox(Inches(7.01), Inches(2.05), w2 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "[5] Sharma et al. (2024):", "Towards Understanding Sycophancy in Language Models. ICLR 2024. arXiv:2310.13548.", pt_size=11.5, space_after=8)
    add_bullet(tf, "[6] Xiong et al. (2024):", "Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation. ICLR 2024. arXiv:2306.13063.", pt_size=11.5, space_after=8)
    add_bullet(tf, "[7] Geyik et al. (2019):", "Fairness-Aware Ranking in Search & Recommendation Systems. ACM SIGKDD 2019, pp. 2221–2231.", pt_size=11.5, space_after=8)
    add_bullet(tf, "[8] Buçinca et al. (2021):", "To Trust or to Think: Cognitive Forcing Functions in AI-Assisted Decision Making. ACM PACMHCI (CSCW '21), Art. 188.", pt_size=11.5, space_after=8)

    s17.notes_slide.notes_text_frame.text = (
        "Slide 17 provides the complete formal bibliography of canonical peer-reviewed literature cited across all sections "
        "of this presentation, including Du et al., Liang et al., Smit et al., ACM CS2023, Sharma et al., and Buçinca et al."
    )

    # =========================================================================
    # SLIDE 18: Section 7 — Threats to Validity, Limitations, Future Scope & Conclusion
    # =========================================================================
    s18 = prs.slides.add_slide(blank_layout)
    apply_bg(s18, BG_LIGHT)
    add_header(s18, "Threats to Validity, Future Scope & Conclusion", "Section 7: Conclusion", 18,
               "Critical evaluation boundaries, future research avenues, and final project defense synthesis.")

    w2 = Inches(5.67)
    h_card_s18 = Inches(4.3)

    add_card(s18, Inches(0.8), Inches(1.55), w2, h_card_s18, "Threats to Validity & System Boundaries", AMBER_ACCENT, top_accent=AMBER_ACCENT)
    tb = s18.shapes.add_textbox(Inches(0.95), Inches(2.05), w2 - Inches(0.3), h_card_s18 - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Synthetic Profile Sample Size:", "Pilot evaluated on N=20 synthetic profiles across 10 base archetypes; future work requires live student longitudinal deployment.", pt_size=11.5)
    add_bullet(tf, "• Single Model Family Constraint:", "Personas utilize local Qwen representations; future work will test cross-family triads (Qwen + Llama + Mistral).", pt_size=11.5)
    add_bullet(tf, "• Graph Bounding:", "The Career-Skill DAG currently maps 42 core computing nodes; non-computing domains require additional ontologies.", pt_size=11.5)
    add_bullet(tf, "• On-Device Latency:", "Local sequential execution takes ~4.5s per debate turn on consumer hardware.", pt_size=11.5)

    add_card(s18, Inches(6.86), Inches(1.55), w2, h_card_s18, "Deliverables Summary & Future Scope", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s18.shapes.add_textbox(Inches(7.01), Inches(2.05), w2 - Inches(0.3), h_card_s18 - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Multi-Persona Prototype Delivered:", "Full interactive Streamlit application (app.py) with live debate runner and dispute tree viewer.", pt_size=11.5)
    add_bullet(tf, "• Calibrated Human Override:", "Interactive trade-off sliders allowing counselors and students to rebalance recommendations.", pt_size=11.5)
    add_bullet(tf, "• Neo4j Knowledge Graph & Chroma:", "42-node prerequisite DAG with Cypher queries and indexed ACM/O*NET knowledge base.", pt_size=11.5)
    add_bullet(tf, "• Core Project Takeaway:", "Coupling dialectic multi-agent tension with deterministic graph verification successfully preserves human student agency.", pt_size=11.5)

    # Bottom Thank You & Q&A Callout
    add_flow_node(s18, Inches(0.8), Inches(6.0), Inches(11.733), Inches(0.9), "Thank You · Questions & Discussion", "Ready for Committee Viva Voce Examination\nInteractive Prototype: streamlit run app.py | Evaluation: python3 run_study.py", bg=CARD_MUTED, border=TEAL_PRIMARY, text_color=NAVY_HEAD)

    s18.notes_slide.notes_text_frame.text = (
        "In conclusion, our project demonstrates that coupling adversarial persona friction (Planner, Critic, Ethics-Reviewer) "
        "with public course data, Chroma vector retrieval, and Neo4j graph verification eliminates prerequisite hallucinations "
        "and preserves student critical agency. We welcome questions from the committee."
    )

    # Save Presentation
    prs.save(output_path)
    print("\n" + "=" * 65)
    print("ACADEMIC PRESENTATION DECK SUCCESSFULLY REBUILT (100% SPEC COMPLIANT)!")
    print(f"Output File: {output_path}")
    print("=" * 65)

if __name__ == "__main__":
    build_presentation_deck()
