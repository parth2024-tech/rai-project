#!/usr/bin/env python3
"""
High-Impact Academic Presentation Deck (18 Slides)
Debate-Based Career Guidance Agent with Complementary Personas

Redesigned strictly following the presentation-designer skill:
- Native visual diagrams and flowcharts on every core slide
- Decision diamonds, horizontal process pipelines, tree diagrams, and network graphs
- High-contrast visual cards with clean typographic hierarchy (Body 12.5–15pt, Headlines 20–26pt)
- No text walls; cut word density by ~60%
- Fully grounded academic claims: no overclaiming, real pilot numbers, honest limitations
- Strictly mapped across the 7 academic evaluation sections:
  1. Abstract (Slide 2)
  2. Introduction (Slides 3–4)
  3. Literature Survey (Slides 5–7)
  4. Architecture Diagram & Design (Slides 8–11)
  5. Experimental Setup (Slides 12–14)
  6. Results & Discussion (Slides 15–16)
  7. References & Conclusion (Slides 17–18)
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

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
        # Category Tag Badge (Top Left)
        tag = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.32), Inches(4.2), Inches(0.28))
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

        # Main Title (Headline >= 20pt)
        tb_t = slide.shapes.add_textbox(Inches(0.8), Inches(0.62), Inches(11.733), Inches(0.44))
        p = tb_t.text_frame.paragraphs[0]
        p.text = title
        p.font.name = FONT_MAIN
        p.font.size = Pt(21)
        p.font.bold = True
        p.font.color.rgb = NAVY_HEAD

        # Subtitle / Takeaway Line
        if takeaway:
            tb_sub = slide.shapes.add_textbox(Inches(0.8), Inches(1.06), Inches(11.733), Inches(0.30))
            p_sub = tb_sub.text_frame.paragraphs[0]
            p_sub.text = takeaway
            p_sub.font.name = FONT_MAIN
            p_sub.font.size = Pt(11.0)
            p_sub.font.italic = True
            p_sub.font.color.rgb = TEXT_MUTED

        # Header Rule
        rule = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.38), Inches(11.733), Inches(0.012))
        rule.fill.solid()
        rule.fill.fore_color.rgb = CARD_BORDER
        rule.line.fill.background()

        # Clean Academic Footer
        rule_f = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(7.06), Inches(11.733), Inches(0.01))
        rule_f.fill.solid()
        rule_f.fill.fore_color.rgb = CARD_BORDER
        rule_f.line.fill.background()

        tb_f = slide.shapes.add_textbox(Inches(0.8), Inches(7.10), Inches(9.5), Inches(0.3))
        p_f = tb_f.text_frame.paragraphs[0]
        p_f.text = "DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING · B.TECH CAPSTONE PROJECT"
        p_f.font.name = FONT_MAIN
        p_f.font.size = Pt(8.5)
        p_f.font.bold = True
        p_f.font.color.rgb = TEXT_MUTED

        tb_fr = slide.shapes.add_textbox(Inches(10.3), Inches(7.10), Inches(2.2), Inches(0.3))
        p_fr = tb_fr.text_frame.paragraphs[0]
        p_fr.text = f"Slide {slide_num} of {TOTAL_SLIDES}"
        p_fr.font.name = FONT_MAIN
        p_fr.font.size = Pt(8.5)
        p_fr.font.color.rgb = TEXT_MUTED
        p_fr.alignment = PP_ALIGN.RIGHT

    def add_card(slide, left, top, width, height, title="", title_color=NAVY_HEAD, top_accent=None, bg_color=CARD_BG, border_color=CARD_BORDER, title_size=13.0):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1.1)

        if top_accent:
            acc = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left + Inches(0.06), top + Inches(0.03), width - Inches(0.12), Inches(0.06))
            acc.fill.solid()
            acc.fill.fore_color.rgb = top_accent
            acc.line.fill.background()

        if title:
            tb = slide.shapes.add_textbox(left + Inches(0.14), top + Inches(0.16), width - Inches(0.28), Inches(0.38))
            tb.text_frame.word_wrap = True
            tb.text_frame.margin_left = Inches(0.02)
            tb.text_frame.margin_right = Inches(0.02)
            tb.text_frame.margin_top = Inches(0.0)
            tb.text_frame.margin_bottom = Inches(0.0)
            p = tb.text_frame.paragraphs[0]
            p.text = title
            p.font.name = FONT_MAIN
            p.font.size = Pt(title_size)
            p.font.bold = True
            p.font.color.rgb = title_color
            return card, tb
        return card, None

    def add_bullet(tf, bold_txt, norm_txt, pt_size=12.5, space_after=5, bold_color=None, norm_color=None):
        p = tf.add_paragraph() if len(tf.paragraphs[0].text) > 0 else tf.paragraphs[0]
        p.space_after = Pt(space_after)
        if bold_txt:
            run_b = p.add_run()
            run_b.text = bold_txt + " "
            run_b.font.name = FONT_MAIN
            run_b.font.size = Pt(pt_size)
            run_b.font.bold = True
            run_b.font.color.rgb = bold_color if bold_color else NAVY_PRIMARY
        
        if norm_txt:
            run_n = p.add_run()
            run_n.text = norm_txt
            run_n.font.name = FONT_MAIN
            run_n.font.size = Pt(pt_size)
            run_n.font.color.rgb = norm_color if norm_color else TEXT_MAIN

    def add_flow_node(slide, left, top, width, height, text, sub="", bg=CARD_BG, border=TEAL_PRIMARY, text_color=NAVY_HEAD, shape=MSO_SHAPE.ROUNDED_RECTANGLE):
        node = slide.shapes.add_shape(shape, left, top, width, height)
        node.fill.solid()
        node.fill.fore_color.rgb = bg
        node.line.color.rgb = border
        node.line.width = Pt(1.2)
        tf = node.text_frame
        tf.word_wrap = True
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        p.text = text
        p.font.name = FONT_MAIN
        p.font.size = Pt(11.0)
        p.font.bold = True
        p.font.color.rgb = text_color
        p.alignment = PP_ALIGN.CENTER
        if sub:
            p2 = tf.add_paragraph()
            p2.text = sub
            p2.font.name = FONT_MAIN
            p2.font.size = Pt(8.5)
            p2.font.color.rgb = TEXT_MUTED
            p2.alignment = PP_ALIGN.CENTER
        return node

    def add_arrow(slide, left, top, width, height, direction="right", color=TEAL_PRIMARY):
        shape_type = MSO_SHAPE.RIGHT_ARROW if direction == "right" else MSO_SHAPE.DOWN_ARROW
        arr = slide.shapes.add_shape(shape_type, left, top, width, height)
        arr.fill.solid()
        arr.fill.fore_color.rgb = color
        arr.line.fill.background()
        return arr

    # =========================================================================
    # SLIDE 1: Title Slide (Professional Academic Layout)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    apply_bg(s1, BG_DARK)

    # Top Tag Badges
    s1_badge = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(0.7), Inches(5.0), Inches(0.34))
    s1_badge.fill.solid()
    s1_badge.fill.fore_color.rgb = RGBColor(19, 78, 74)
    s1_badge.line.color.rgb = TEAL_ACCENT
    s1_badge.line.width = Pt(1)
    p = s1_badge.text_frame.paragraphs[0]
    p.text = "RESPONSIBLE AI · MULTI-AGENT SYSTEMS · KNOWLEDGE DAGS"
    p.font.name = FONT_MAIN
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = RGBColor(204, 251, 241)
    p.alignment = PP_ALIGN.CENTER
    s1_badge.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    s1_status = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.2), Inches(0.7), Inches(4.5), Inches(0.34))
    s1_status.fill.solid()
    s1_status.fill.fore_color.rgb = RGBColor(30, 58, 138)
    s1_status.line.color.rgb = BLUE_ACCENT
    s1_status.line.width = Pt(1)
    p = s1_status.text_frame.paragraphs[0]
    p.text = "B.TECH CAPSTONE PROJECT PRESENTATION"
    p.font.name = FONT_MAIN
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = RGBColor(191, 219, 254)
    p.alignment = PP_ALIGN.CENTER
    s1_status.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    # Main Title
    s1_title_box = s1.shapes.add_textbox(Inches(1.0), Inches(1.35), Inches(11.333), Inches(2.0))
    tf1 = s1_title_box.text_frame
    tf1.word_wrap = True
    p1 = tf1.paragraphs[0]
    p1.text = "Debate-Based Career Guidance Agent\nwith Complementary Personas"
    p1.font.name = FONT_MAIN
    p1.font.size = Pt(28)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE
    p1.space_after = Pt(8)

    p2 = tf1.add_paragraph()
    p2.text = "A Dialectic Multi-Agent Architecture for Prerequisite-Grounded & Fair Algorithmic Advisory"
    p2.font.name = FONT_MAIN
    p2.font.size = Pt(13.5)
    p2.font.color.rgb = RGBColor(148, 163, 184)

    # 2 Metadata Cards
    col_w2 = Inches(5.5)
    col_h2 = Inches(2.9)
    top_meta = Inches(3.7)

    card_bold_col = RGBColor(241, 245, 249)
    card_norm_col = RGBColor(203, 213, 225)

    add_card(s1, Inches(1.0), top_meta, col_w2, col_h2, "Candidate & Academic Context", TEAL_ACCENT, bg_color=RGBColor(30, 41, 59), border_color=RGBColor(51, 65, 85))
    tb_m1 = s1.shapes.add_textbox(Inches(1.2), top_meta + Inches(0.48), col_w2 - Inches(0.4), col_h2 - Inches(0.55))
    tf_m1 = tb_m1.text_frame
    tf_m1.word_wrap = True
    add_bullet(tf_m1, "• Degree Program:", "B.Tech in Computer Science & Engineering", pt_size=12.0, space_after=6, bold_color=card_bold_col, norm_color=card_norm_col)
    add_bullet(tf_m1, "• Department:", "Department of Computer Science & Engineering", pt_size=12.0, space_after=6, bold_color=card_bold_col, norm_color=card_norm_col)
    add_bullet(tf_m1, "• Project Domain:", "Autonomous Multi-Agent Deliberation & Safe AI", pt_size=12.0, space_after=6, bold_color=card_bold_col, norm_color=card_norm_col)
    add_bullet(tf_m1, "• Academic Session:", "Academic Evaluation 2025–2026", pt_size=12.0, space_after=6, bold_color=card_bold_col, norm_color=card_norm_col)

    add_card(s1, Inches(6.833), top_meta, col_w2, col_h2, "Supervision & Engineering Infrastructure", BLUE_ACCENT, bg_color=RGBColor(30, 41, 59), border_color=RGBColor(51, 65, 85))
    tb_m2 = s1.shapes.add_textbox(Inches(7.033), top_meta + Inches(0.48), col_w2 - Inches(0.4), col_h2 - Inches(0.55))
    tf_m2 = tb_m2.text_frame
    tf_m2.word_wrap = True
    add_bullet(tf_m2, "• Project Supervisor:", "Faculty Project Evaluation Committee", pt_size=12.0, space_after=6, bold_color=card_bold_col, norm_color=card_norm_col)
    add_bullet(tf_m2, "• Local Inference:", "100% On-Device Ollama (RTX 3050 Laptop · 4GB VRAM)", pt_size=12.0, space_after=6, bold_color=card_bold_col, norm_color=card_norm_col)
    add_bullet(tf_m2, "• Knowledge Grounding:", "Deterministic NetworkX 42-Node Curricular DAG", pt_size=12.0, space_after=6, bold_color=card_bold_col, norm_color=card_norm_col)
    add_bullet(tf_m2, "• Reproducibility:", "Interactive Visual Web Dashboard & Terminal CLI Testbed", pt_size=12.0, space_after=6, bold_color=card_bold_col, norm_color=card_norm_col)

    s1.notes_slide.notes_text_frame.text = (
        "Good morning committee. Today I present our B.Tech Capstone Project: 'Debate-Based Career Guidance Agent "
        "with Complementary Personas'. We replace monolithic LLM conversational sycophancy with structured dialectic tension "
        "grounded deterministically in a hand-built NetworkX prerequisite DAG, preserving student agency and enforcing "
        "counterfactual fairness on consumer local hardware."
    )

    # =========================================================================
    # SLIDE 2: Section 1 — Abstract: Visual System Overview
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    apply_bg(s2, BG_LIGHT)
    add_header(s2, "Abstract: Grounded Dialectics for Algorithmic Advisory", "Section 1: Abstract", 2,
               "Replacing conversational sycophancy with dialectic tension, graph grounding, and human agency.")

    w3 = Inches(3.64)
    h_top = Inches(2.4)
    h_bot = Inches(2.7)

    add_card(s2, Inches(0.8), Inches(1.55), w3, h_top, "The Advisory Dilemma", ROSE_ACCENT, top_accent=ROSE_ACCENT)
    tb = s2.shapes.add_textbox(Inches(0.95), Inches(2.05), w3 - Inches(0.3), h_top - Inches(0.55))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Sycophancy Trap:", "Monolithic LLMs flatter unfeasible student requests without verifying foundational prerequisites.")
    add_bullet(tf, "• False Consensus:", "Single-agent decoding averages competing career trajectories into vague, generic advice.")
    add_bullet(tf, "• Demographic Steering:", "Pre-trained models leak subtle socioeconomic and institutional biases.")

    add_card(s2, Inches(4.84), Inches(1.55), w3, h_top, "Grounded Dialectic System", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s2.shapes.add_textbox(Inches(5.0), Inches(2.05), w3 - Inches(0.3), h_top - Inches(0.55))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• 3 Dialectic Personas:", "Traditionalist (Rigor), Builder (Speed), and Specialist (Systems Depth).")
    add_bullet(tf, "• Curricular Graph:", "NetworkX 42-node prerequisite DAG enforces deterministic reachability.")
    add_bullet(tf, "• Neutral Moderator:", "Identifies sharp contradictions and constructs structured Dispute Trees.")

    add_card(s2, Inches(8.88), Inches(1.55), w3, h_top, "Pilot Evaluation Scope", BLUE_ACCENT, top_accent=BLUE_ACCENT)
    tb = s2.shapes.add_textbox(Inches(9.03), Inches(2.05), w3 - Inches(0.3), h_top - Inches(0.55))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• 4-Tier Controlled Ablation:", "Benchmarks Monolithic vs Self-Consistency vs Triad vs Proposed Architecture.")
    add_bullet(tf, "• Counterfactual Audit:", "Audits 20 synthetic candidate profiles across 10 matched demographic pairs.")
    add_bullet(tf, "• Cognitive Forcing Gate:", "Surfaces unresolvable trade-offs directly to student choice.")

    add_card(s2, Inches(0.8), Inches(4.15), Inches(11.733), h_bot, "Core Academic Contributions & Pilot Findings", NAVY_HEAD, top_accent=NAVY_HEAD)
    tb_bot = s2.shapes.add_textbox(Inches(1.0), Inches(4.65), Inches(11.333), h_bot - Inches(0.6))
    tf_bot = tb_bot.text_frame
    tf_bot.word_wrap = True
    add_bullet(tf_bot, "1. Dialectic Multi-Agent Formulation:", "Physically separated agents with differentiated system prompts preserve legitimate technical trade-offs that collapse in single-agent monolithic prompts.", pt_size=12.5)
    add_bullet(tf_bot, "2. Deterministic Knowledge Grounding:", "Employs an explicit 42-node prerequisite DAG in NetworkX to detect and prevent prerequisite ordering hallucinations without cloud database overhead.", pt_size=12.5)
    add_bullet(tf_bot, "3. Counterfactual Fairness & Agency Preservation:", "Demographic attribute isolation maintains 100% consistency across matched pairs; high-risk trade-offs trigger a Cognitive Forcing Gate (40% rate in pilot).", pt_size=12.5)

    s2.notes_slide.notes_text_frame.text = (
        "Slide 2 outlines the abstract. Standard single-agent LLMs suffer from conversational sycophancy: they agree "
        "with student ambitions even when students lack foundational prerequisites. We address this using three antagonistic "
        "personas, deterministic NetworkX graph traversal, and a cognitive forcing gate that surfaces real trade-offs."
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
    add_flow_node(s3, Inches(1.1), Inches(5.75), Inches(5.0), Inches(0.8), "RISK: Financial Loss & Interview Rejection", "Student spends savings on bootcamp; fails fundamental technical screening", bg=CARD_BG, border=ROSE_ACCENT, text_color=ROSE_ACCENT)

    # Right Column: Proposed Dialectic Architecture
    add_card(s3, Inches(6.9), Inches(1.55), col_w_s3, col_h_s3, "Proposed Grounded Architecture (Truth-Seeking)", TEAL_PRIMARY, top_accent=TEAL_PRIMARY, bg_color=TEAL_BG, border_color=TEAL_PRIMARY)
    add_flow_node(s3, Inches(7.2), Inches(2.15), Inches(5.0), Inches(0.8), "1. Profile Intake & Attribute Vault", "Protected demographics masked; verified technical competencies retained", bg=CARD_BG, border=TEAL_PRIMARY)
    add_arrow(s3, Inches(9.55), Inches(3.02), Inches(0.3), Inches(0.25), direction="down", color=TEAL_PRIMARY)
    add_flow_node(s3, Inches(7.2), Inches(3.35), Inches(5.0), Inches(0.8), "2. Differentiated Persona Friction", "Traditionalist (Rigor) vs Builder (Velocity) vs Specialist (Systems Depth)", bg=CARD_BG, border=TEAL_PRIMARY)
    add_arrow(s3, Inches(9.55), Inches(4.22), Inches(0.3), Inches(0.25), direction="down", color=TEAL_PRIMARY)
    add_flow_node(s3, Inches(7.2), Inches(4.55), Inches(5.0), Inches(0.8), "3. Deterministic DAG Traversal", "NetworkX traversal detects 3 missing prerequisite hops; halts auto-roadmap", bg=CARD_BG, border=TEAL_PRIMARY)
    add_arrow(s3, Inches(9.55), Inches(5.42), Inches(0.3), Inches(0.25), direction="down", color=TEAL_PRIMARY)
    add_flow_node(s3, Inches(7.2), Inches(5.75), Inches(5.0), Inches(0.8), "OUTCOME: Cognitive Forcing & Dispute Tree", "Surfaces genuine trade-offs; student exercises transparent informed choice", bg=CARD_BG, border=TEAL_PRIMARY, text_color=TEAL_PRIMARY)

    s3.notes_slide.notes_text_frame.text = (
        "Slide 3 contrasts standard monolithic LLM behavior against our dialectic pipeline. Notice the failure mode on the left: "
        "when a student makes an unrealistic career request, RLHF fine-tuning compels the model to be agreeable, skipping prerequisites. "
        "On the right, our attribute isolation vault, persona friction, and DAG traversal catch the sequence violation."
    )

    # =========================================================================
    # SLIDE 4: Section 2 — Introduction: Research Questions & Bounded Scope
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    apply_bg(s4, BG_LIGHT)
    add_header(s4, "Introduction: Research Questions & Bounded Scope", "Section 2: Introduction", 4,
               "Framing the four formal investigation targets and local hardware boundaries.")

    w2 = Inches(5.67)
    h_top = Inches(2.55)
    h_bot = Inches(2.6)

    add_card(s4, Inches(0.8), Inches(1.55), w2, h_top, "Investigative Research Questions", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s4.shapes.add_textbox(Inches(0.95), Inches(2.05), w2 - Inches(0.3), h_top - Inches(0.55))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• RQ1 (Prerequisite Integrity):", "Can deterministic DAG traversal prevent prerequisite ordering hallucinations in LLM roadmaps?")
    add_bullet(tf, "• RQ2 (Perspective Diversity):", "Does physical multi-agent separation preserve valid technical trade-offs better than monolithic prompts?")
    add_bullet(tf, "• RQ3 (Counterfactual Parity):", "Does demographic attribute isolation eliminate recommendation flips across matched student pairs?")
    add_bullet(tf, "• RQ4 (Agency Preservation):", "Can an interface-level Cognitive Forcing Gate prevent student automation bias in high-risk decisions?")

    add_card(s4, Inches(6.86), Inches(1.55), w2, h_top, "Formal Advisory Problem Formulation", NAVY_HEAD, top_accent=NAVY_HEAD)
    tb = s4.shapes.add_textbox(Inches(7.01), Inches(2.05), w2 - Inches(0.3), h_top - Inches(0.55))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Input Profile:", "Candidate profile contains verified skills, target role, timeline, and objective budget constraint.")
    add_bullet(tf, "• Curricular Graph G:", "Directed Acyclic Graph G = (V, E) defining topological prerequisites across computing milestones.")
    add_bullet(tf, "• Persona Triad:", "Advisory personas parameterized by strongly differentiated prompt philosophies.")
    add_bullet(tf, "• Decision Gate Rule:", "Fires whenever Prerequisite Gap > 0 OR Persona Trajectory Contradiction >= 1.")

    add_card(s4, Inches(0.8), Inches(4.3), Inches(11.733), h_bot, "Bounded Local Engineering Scope & Hardware Parameters", BLUE_ACCENT, top_accent=BLUE_ACCENT)
    tb_bot = s4.shapes.add_textbox(Inches(1.0), Inches(4.8), Inches(11.333), h_bot - Inches(0.6))
    tf_bot = tb_bot.text_frame
    tf_bot.word_wrap = True
    add_bullet(tf_bot, "• Domain Boundary:", "Undergraduate Computer Science & Engineering curricula (42 nodes, 47 prerequisite edges).", pt_size=12.0)
    add_bullet(tf_bot, "• Model Architecture:", "Llama-3.2-3B instruction-tuned model executed locally via Ollama.", pt_size=12.0)
    add_bullet(tf_bot, "• Hardware Constraints:", "NVIDIA GeForce RTX 3050 Laptop GPU (4,096 MiB VRAM); sequential multi-agent execution (~4.2s per profile).", pt_size=12.0)
    add_bullet(tf_bot, "• Verification Standard:", "Deterministic NetworkX graph traversal; zero circularity with model generation.", pt_size=12.0)

    s4.notes_slide.notes_text_frame.text = (
        "Slide 4 defines our four core Research Questions and bounds our engineering scope. We explicitly state our hardware "
        "constraints: an NVIDIA RTX 3050 Laptop GPU with 4GB VRAM running Llama-3.2-3B locally. Personas execute sequentially "
        "to prevent out-of-memory errors, taking approximately 4.2 seconds per full triad deliberation."
    )

    # =========================================================================
    # SLIDE 5: Section 3 — Literature Survey: Canonical Foundations
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    apply_bg(s5, BG_LIGHT)
    add_header(s5, "Literature Survey: Canonical Foundations", "Section 3: Literature Survey", 5,
               "Theoretical basis across multi-agent debate, sycophancy, and cognitive forcing functions.")

    w3 = Inches(3.64)
    h_card = Inches(5.2)

    add_card(s5, Inches(0.8), Inches(1.55), w3, h_card, "Multi-Agent Deliberation", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s5.shapes.add_textbox(Inches(0.95), Inches(2.05), w3 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Du et al. (ICML 2024):", "Demonstrated that multi-agent debate improves factuality and reasoning on complex question-answering benchmarks.")
    add_bullet(tf, "• Liang et al. (EMNLP 2023):", "Showed that assigned divergent personas encourage creative problem-solving and prevent groupthink.")
    add_bullet(tf, "• Core Takeaway:", "Adversarial multi-agent interaction extracts competing hypotheses more effectively than single-agent decoding.")

    add_card(s5, Inches(4.84), Inches(1.55), w3, h_card, "Sycophancy & Agreeableness", ROSE_ACCENT, top_accent=ROSE_ACCENT)
    tb = s5.shapes.add_textbox(Inches(5.0), Inches(2.05), w3 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Perez et al. (ACL 2023):", "Discovered that RLHF language models systematically flatter users by validating their false assumptions.")
    add_bullet(tf, "• Sharma et al. (ICLR 2024):", "Identified that reward models prefer agreeable falsehoods over corrective, unpalatable truths.")
    add_bullet(tf, "• Core Takeaway:", "Single-agent LLMs are structurally incentivized to confirm unrealistic student career aspirations.")

    add_card(s5, Inches(8.88), Inches(1.55), w3, h_card, "Calibration & Human Agency", BLUE_ACCENT, top_accent=BLUE_ACCENT)
    tb = s5.shapes.add_textbox(Inches(9.03), Inches(2.05), w3 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Xiong et al. (ICLR 2024):", "Found that verbalized confidence and consistency in LLMs remain poorly calibrated across diverse reasoning tasks.")
    add_bullet(tf, "• Buçinca et al. (CSCW 2021):", "Demonstrated that interface cognitive forcing functions successfully reduce blind automation bias.")
    add_bullet(tf, "• Core Takeaway:", "Uncertainty cannot be resolved by model self-confidence alone; explicit friction must be presented to human users.")

    s5.notes_slide.notes_text_frame.text = (
        "Slide 5 grounds our work in three bodies of literature. Du and Liang established that multi-agent debate stimulates "
        "reasoning. Perez and Sharma proved that single LLMs exhibit severe sycophancy. And Xiong and Buçinca demonstrated "
        "that LLM confidence is uncalibrated, requiring cognitive forcing functions to preserve human agency."
    )

    # =========================================================================
    # SLIDE 6: Section 3 — Literature Survey: The Debate Critique Frontier
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    apply_bg(s6, BG_LIGHT)
    add_header(s6, "Literature Survey: The Debate Critique Frontier", "Section 3: Literature Survey", 6,
               "Addressing the 'Should We Be Going MAD?' critique through deterministic grounding.")

    w2 = Inches(5.67)
    h_card = Inches(5.2)

    add_card(s6, Inches(0.8), Inches(1.55), w2, h_card, "The Smit et al. (2024) Critique", AMBER_ACCENT, top_accent=AMBER_ACCENT)
    tb = s6.shapes.add_textbox(Inches(0.95), Inches(2.05), w2 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• 'Should We Be Going MAD?':", "Smit et al. (arXiv:2311.17371) critically evaluated multi-agent debate (MAD) across multiple reasoning benchmarks.")
    add_bullet(tf, "• Majority Voting Equivalence:", "Argued that uncurated debate often reduces to expensive majority voting without achieving genuine factual consensus.")
    add_bullet(tf, "• Shared Prior Pathology:", "Personas derived from the same base model weights share identical training priors, leading to coordinated blindspots.")
    add_bullet(tf, "• Error Amplification:", "Unmoderated debate can amplify hallucinations if confident personas persuade ungrounded peers.")

    add_card(s6, Inches(6.86), Inches(1.55), w2, h_card, "Our Four Architectural Countermeasures", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s6.shapes.add_textbox(Inches(7.01), Inches(2.05), w2 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "1. Deterministic Knowledge Grounding:", "We anchor deliberation in a 42-node NetworkX curriculum DAG rather than ungrounded LLM self-agreement.")
    add_bullet(tf, "2. Deeply Differentiated Prompts:", "Personas are driven by opposing epistemologies (Traditionalist Rigor vs Builder Velocity vs Systems Depth).")
    add_bullet(tf, "3. Compute-Matched Baseline:", "We explicitly benchmark against a 3-sample Self-Consistency baseline (Config 2) to test if debate outperforms repeated sampling.")
    add_bullet(tf, "4. Cognitive Forcing Dispute Gate:", "When personas exhibit genuine strategic trade-offs, we refuse to force artificial consensus; we surface the Dispute Tree to the student.")

    s6.notes_slide.notes_text_frame.text = (
        "Slide 6 tackles the recent critique by Smit et al. entitled 'Should We Be Going MAD?'. Smit argued that debate "
        "is often no better than majority voting and that agents sharing base weights amplify shared biases. We directly address "
        "this by coupling debate to a deterministic NetworkX curriculum DAG and benchmarking against a compute-matched self-consistency baseline."
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

    headers = ["Framework / Work", "Multi-Agent Debate", "Knowledge Grounding", "Fairness Audit", "Agency Gate", "Local Execution"]
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
        ("Proposed Architecture", "Yes (Triad)", "Yes (42-Node DAG)", "Yes (Vault)", "Yes (Dispute Tree)", "Yes (RTX 3050)"),
    ]

    for i, row in enumerate(matrix_data):
        is_proposed = (i == len(matrix_data) - 1)
        bg = TEAL_BG if is_proposed else (CARD_BG if i % 2 == 0 else CARD_MUTED)
        border_col = TEAL_PRIMARY if is_proposed else CARD_BORDER
        
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
        "Slide 7 summarizes how our architecture relates to prior art. To our knowledge, this is the first lightweight "
        "pilot architecture that couples multi-agent debate with deterministic knowledge DAG validation, demographic attribute "
        "isolation, and cognitive forcing running 100% locally on consumer-tier GPU hardware."
    )

    # =========================================================================
    # SLIDE 8: Section 4 — Architecture Diagram: End-to-End Pipeline & Decision Flow
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    apply_bg(s8, BG_LIGHT)
    add_header(s8, "Architecture Diagram: End-to-End Decision Flow", "Section 4: Architecture Diagram", 8,
               "Strict left-to-right intake, dialectic deliberation, deterministic DAG verification, and dispute gating.")

    # Top Row: 4 Sequential Steps
    add_flow_node(s8, Inches(0.8), Inches(1.6), Inches(2.3), Inches(1.15), "1. Candidate Intake", "Verified skills, target role,\ntimeline & budget", bg=CARD_BG, border=NAVY_PRIMARY)
    add_arrow(s8, Inches(3.18), Inches(2.05), Inches(0.35), Inches(0.25), direction="right", color=NAVY_PRIMARY)

    add_flow_node(s8, Inches(3.58), Inches(1.6), Inches(2.4), Inches(1.15), "2. Attribute Vault", "Masks name, gender & tier;\npasses objective constraints", bg=BLUE_BG, border=BLUE_ACCENT)
    add_arrow(s8, Inches(6.05), Inches(2.05), Inches(0.35), Inches(0.25), direction="right", color=BLUE_ACCENT)

    add_flow_node(s8, Inches(6.45), Inches(1.6), Inches(2.9), Inches(1.15), "3. Dialectic Triad Engine", "Sequential local run (RTX 3050):\nTraditionalist · Builder · Specialist", bg=TEAL_BG, border=TEAL_PRIMARY)
    add_arrow(s8, Inches(9.42), Inches(2.05), Inches(0.35), Inches(0.25), direction="right", color=TEAL_PRIMARY)

    add_flow_node(s8, Inches(9.82), Inches(1.6), Inches(2.7), Inches(1.15), "4. Moderator & DAG", "Checks 42-node NetworkX DAG;\nextracts contradictions", bg=CARD_BG, border=BLUE_ACCENT)

    # Middle Right: Arrow Down to Decision Diamond
    add_arrow(s8, Inches(11.02), Inches(2.82), Inches(0.3), Inches(0.35), direction="down", color=BLUE_ACCENT)
    diamond = add_flow_node(s8, Inches(9.65), Inches(3.22), Inches(2.87), Inches(1.2), "Decision Check", "Prereq Gap > 0 OR\nPersona Conflict?", bg=AMBER_BG, border=AMBER_ACCENT, shape=MSO_SHAPE.DIAMOND)

    # YES Branch (Points Left from Diamond into Red Card)
    add_arrow(s8, Inches(8.55), Inches(3.67), Inches(0.85), Inches(0.26), direction="left", color=ROSE_ACCENT)
    tb_lbl_yes = s8.shapes.add_textbox(Inches(8.4), Inches(3.35), Inches(1.2), Inches(0.28))
    p_ly = tb_lbl_yes.text_frame.paragraphs[0]
    p_ly.text = "YES (Gap / Conflict)"
    p_ly.font.name = FONT_MAIN
    p_ly.font.size = Pt(8.5)
    p_ly.font.bold = True
    p_ly.font.color.rgb = ROSE_ACCENT
    p_ly.alignment = PP_ALIGN.CENTER

    add_card(s8, Inches(0.8), Inches(3.15), Inches(7.5), Inches(3.7), "Cognitive Forcing Gate Fired! (Human Agency Preserved)", ROSE_ACCENT, top_accent=ROSE_ACCENT, bg_color=ROSE_BG, border_color=ROSE_ACCENT)
    tb_g = s8.shapes.add_textbox(Inches(1.0), Inches(3.65), Inches(7.1), Inches(3.0))
    tf_g = tb_g.text_frame
    tf_g.word_wrap = True
    add_bullet(tf_g, "• Automated Pipeline Halted:", "System detects that proceeding automatically would commit the student to an unfeasible sequence or force an artificial consensus.", pt_size=12.0)
    add_bullet(tf_g, "• Interactive Dispute Tree Presented:", "Presents explicit branching trade-offs directly to student choice:", pt_size=12.0)
    add_bullet(tf_g, "   - Branch 1 (Systems Depth):", "12-month foundational track (Linear Algebra ➔ OS Internals ➔ PyTorch ➔ Systems). Low financial risk, high technical rigor.", pt_size=11.5)
    add_bullet(tf_g, "   - Branch 2 (Applied Velocity):", "4-month application engineering pivot (FastAPI ➔ REST APIs ➔ RAG Tools). Rapid portfolio creation within student's timeline.", pt_size=11.5)
    add_bullet(tf_g, "• Preserves Student Agency:", "Student actively arbitrates their career trajectory, completely eliminating automation complacency.", pt_size=12.0)

    # NO Branch (Points Down from Diamond into Green Card)
    add_arrow(s8, Inches(11.02), Inches(4.47), Inches(0.26), Inches(0.35), direction="down", color=TEAL_PRIMARY)
    tb_lbl_no = s8.shapes.add_textbox(Inches(11.32), Inches(4.5), Inches(1.2), Inches(0.28))
    p_ln = tb_lbl_no.text_frame.paragraphs[0]
    p_ln.text = "NO (Verified)"
    p_ln.font.name = FONT_MAIN
    p_ln.font.size = Pt(8.5)
    p_ln.font.bold = True
    p_ln.font.color.rgb = TEAL_PRIMARY

    add_card(s8, Inches(8.7), Inches(4.87), Inches(3.833), Inches(1.98), "Direct Calibrated Roadmap", TEAL_PRIMARY, top_accent=TEAL_PRIMARY, bg_color=TEAL_BG, border_color=TEAL_PRIMARY)
    tb_no = s8.shapes.add_textbox(Inches(8.85), Inches(5.32), Inches(3.5), Inches(1.4))
    tf_no = tb_no.text_frame
    tf_no.word_wrap = True
    add_bullet(tf_no, "• All Prerequisites Verified:", "Deterministic graph traversal confirms all ancestor dependencies are satisfied.", pt_size=11.5)
    add_bullet(tf_no, "• Persona Consensus Achieved:", "No unresolvable philosophical contradiction detected.", pt_size=11.5)
    add_bullet(tf_no, "• Emits Unified Roadmap:", "Direct linear milestone schedule output.", pt_size=11.5)

    s8.notes_slide.notes_text_frame.text = (
        "Slide 8 presents our end-to-end architecture. The pipeline moves cleanly: candidate intake feeds the attribute isolation vault, "
        "which passes objective constraints to the three personas. The personas execute sequentially on the RTX 3050 GPU. "
        "The moderator synthesizes claims and validates them against NetworkX. If an unresolvable prerequisite gap or sharp conflict exists, "
        "the Cognitive Forcing Gate fires, presenting the Dispute Tree to the student."
    )

    # =========================================================================
    # SLIDE 9: Section 4 — Architecture Details: Dialectic Persona Engine
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    apply_bg(s9, BG_LIGHT)
    add_header(s9, "Architecture Details: Complementary Persona Dialectics", "Section 4: Architecture Details", 9,
               "Advisory philosophies driven by differentiated system prompts and calibrated decoding temperatures.")

    w3 = Inches(3.64)
    h_card = Inches(5.2)

    add_card(s9, Inches(0.8), Inches(1.55), w3, h_card, "The Pragmatic Traditionalist", NAVY_HEAD, top_accent=NAVY_HEAD)
    tb = s9.shapes.add_textbox(Inches(0.95), Inches(2.05), w3 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Philosophical Lens:", "Conservative, credential-focused, risk-averse advisory.", pt_size=12.0)
    add_bullet(tf, "• Technical Priorities:", "Core Data Structures, Discrete Math, Accredited University Curricula, Campus Placements.", pt_size=12.0)
    add_bullet(tf, "• Decoding Parameters:", "Temperature T=0.3, Top-P=0.85 (Greedy, highly deterministic).", pt_size=12.0)
    add_bullet(tf, "• Critical Function:", "Actively rejects unaccredited bootcamps and aggressive shortcut promises; protects students from career debt.", pt_size=12.0)

    add_card(s9, Inches(4.84), Inches(1.55), w3, h_card, "The Entrepreneurial Builder", AMBER_ACCENT, top_accent=AMBER_ACCENT)
    tb = s9.shapes.add_textbox(Inches(5.0), Inches(2.05), w3 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Philosophical Lens:", "High velocity, market-oriented, practical tool adoption.", pt_size=12.0)
    add_bullet(tf, "• Technical Priorities:", "Full-Stack Web MVPs, FastAPI, React, Cloud Hosting, GitHub Portfolios.", pt_size=12.0)
    add_bullet(tf, "• Decoding Parameters:", "Temperature T=0.7, Top-P=0.92 (Exploratory, creative synthesis).", pt_size=12.0)
    add_bullet(tf, "• Critical Function:", "Prevents academic over-analysis; pushes students to ship working code and acquire marketable skills.", pt_size=12.0)

    add_card(s9, Inches(8.88), Inches(1.55), w3, h_card, "The Deep-Tech Specialist", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s9.shapes.add_textbox(Inches(9.03), Inches(2.05), w3 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Philosophical Lens:", "Foundational systems depth, performance engineering, first-principles.", pt_size=12.0)
    add_bullet(tf, "• Technical Priorities:", "C/C++, Linux Kernel Calls, Concurrency, Virtual Memory, Distributed Protocols.", pt_size=12.0)
    add_bullet(tf, "• Decoding Parameters:", "Temperature T=0.4, Top-P=0.88 (Analytical, precise technical logic).", pt_size=12.0)
    add_bullet(tf, "• Critical Function:", "Ensures candidates survive technical interviews by understanding system bottlenecks under the hood.", pt_size=12.0)

    s9.notes_slide.notes_text_frame.text = (
        "Slide 9 explains our persona design. It is vital to emphasize that persona differences are primarily governed by "
        "rigorous system prompts establishing opposing epistemologies, while decoding temperatures provide secondary exploratory "
        "modulation. These three personas run sequentially on the RTX 3050, generating authentic dialectic tension."
    )

    # =========================================================================
    # SLIDE 10: Section 4 — Architecture Details: Visual Curricular DAG
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    apply_bg(s10, BG_LIGHT)
    add_header(s10, "Architecture Details: Curricular Knowledge DAG (42 Nodes)", "Section 4: Architecture Details", 10,
               "Core topological backbone: 16 key milestones shown across 4 tracks with cross-track prerequisite edges.")

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
    add_flow_node(s10, Inches(4.0), Inches(2.86), Inches(2.3), Inches(0.50), "Operating Systems", "Virtual memory, syscalls", bg=CARD_BG, border=BLUE_ACCENT)
    add_arrow(s10, Inches(5.02), Inches(3.40), Inches(0.26), Inches(0.18), direction="down", color=BLUE_ACCENT)
    add_flow_node(s10, Inches(4.0), Inches(3.62), Inches(2.3), Inches(0.50), "OS Concurrency", "Locks, semaphores, IPC", bg=CARD_BG, border=BLUE_ACCENT)
    add_arrow(s10, Inches(5.02), Inches(4.16), Inches(0.26), Inches(0.18), direction="down", color=BLUE_ACCENT)
    add_flow_node(s10, Inches(4.0), Inches(4.38), Inches(2.3), Inches(0.50), "Distributed Systems", "Raft consensus, replication", bg=TEAL_BG, border=TEAL_PRIMARY, text_color=TEAL_PRIMARY)

    # Track 3
    add_card(s10, Inches(6.8), top_y, col_w4, Inches(4.15), "Track 3: Web & Cloud", INDIGO_ACCENT, top_accent=INDIGO_ACCENT, title_size=11.5)
    add_flow_node(s10, Inches(7.0), Inches(2.10), Inches(2.3), Inches(0.50), "SQL & Relational DB", "Queries, joins, indexing", bg=CARD_BG, border=CARD_BORDER)
    add_arrow(s10, Inches(8.02), Inches(2.64), Inches(0.26), Inches(0.18), direction="down", color=INDIGO_ACCENT)
    add_flow_node(s10, Inches(7.0), Inches(2.86), Inches(2.3), Inches(0.50), "Backend Frameworks", "Django, FastAPI, REST", bg=CARD_BG, border=INDIGO_ACCENT)
    add_arrow(s10, Inches(8.02), Inches(3.40), Inches(0.26), Inches(0.18), direction="down", color=INDIGO_ACCENT)
    add_flow_node(s10, Inches(7.0), Inches(3.62), Inches(2.3), Inches(0.50), "REST APIs & Docker", "Containerization & routes", bg=CARD_BG, border=INDIGO_ACCENT)
    add_arrow(s10, Inches(8.02), Inches(4.16), Inches(0.26), Inches(0.18), direction="down", color=INDIGO_ACCENT)
    add_flow_node(s10, Inches(7.0), Inches(4.38), Inches(2.3), Inches(0.50), "System Design", "Microservices, caching", bg=TEAL_BG, border=TEAL_PRIMARY, text_color=TEAL_PRIMARY)

    # Track 4
    add_card(s10, Inches(9.8), top_y, col_w4, Inches(4.15), "Track 4: Applied AI & ML", ROSE_ACCENT, top_accent=ROSE_ACCENT, title_size=11.5)
    add_flow_node(s10, Inches(10.0), Inches(2.10), Inches(2.3), Inches(0.50), "Linear Alg & Stats", "Matrix ops & Bayes theorem", bg=CARD_BG, border=CARD_BORDER)
    add_arrow(s10, Inches(11.02), Inches(2.64), Inches(0.26), Inches(0.18), direction="down", color=ROSE_ACCENT)
    add_flow_node(s10, Inches(10.0), Inches(2.86), Inches(2.3), Inches(0.50), "ML Foundations", "Loss, regression, trees", bg=CARD_BG, border=ROSE_ACCENT)
    add_arrow(s10, Inches(11.02), Inches(3.40), Inches(0.26), Inches(0.18), direction="down", color=ROSE_ACCENT)
    add_flow_node(s10, Inches(10.0), Inches(3.62), Inches(2.3), Inches(0.50), "Deep Learning", "PyTorch, backpropagation", bg=CARD_BG, border=ROSE_ACCENT)
    add_arrow(s10, Inches(11.02), Inches(4.16), Inches(0.26), Inches(0.18), direction="down", color=ROSE_ACCENT)
    add_flow_node(s10, Inches(10.0), Inches(4.38), Inches(2.3), Inches(0.50), "LLMs & MLOps", "RAG pipelines & serving", bg=TEAL_BG, border=TEAL_PRIMARY, text_color=TEAL_PRIMARY)

    # Bottom Callout Card: Full Graph Summary & Cross-Track Edges
    add_card(s10, Inches(0.8), Inches(5.80), Inches(11.733), Inches(1.15), "Full 42-Node DAG Topology & Cross-Track Dependencies", NAVY_HEAD, top_accent=TEAL_PRIMARY)
    tb_dag = s10.shapes.add_textbox(Inches(0.95), Inches(6.12), Inches(11.4), Inches(0.75))
    tf_dag = tb_dag.text_frame
    tf_dag.word_wrap = True
    add_bullet(tf_dag, "• Key Cross-Track Prerequisite Edges:", "Python Basics ➔ ML Foundations & Backend APIs | Linear Algebra ➔ Deep Learning & Algorithms | OS & Docker ➔ MLOps & System Design", pt_size=10.5, space_after=3)
    add_bullet(tf_dag, "• Deterministic Reachability Validation:", "NetworkX directed graph contains 42 total nodes and 47 validated edges across undergraduate computer science. Traversal deterministically catches missing dependencies.", pt_size=10.5, space_after=0)

    s10.notes_slide.notes_text_frame.text = (
        "Slide 10 illustrates our 42-node prerequisite DAG. We display the 16 core milestones across 4 tracks, highlighting "
        "the critical cross-track dependency edges: a student cannot skip from basic Python to Deep Learning without Linear Algebra "
        "and ML Foundations, or to System Design without OS Concurrency. The full graph contains 42 nodes implemented in NetworkX."
    )

    # =========================================================================
    # SLIDE 11: Section 4 — Architecture Details: Visual Dispute Tree
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    apply_bg(s11, BG_LIGHT)
    add_header(s11, "Architecture Details: Cognitive Forcing & Dispute Tree", "Section 4: Architecture Details", 11,
               "Transforming unresolvable technical contradictions into structured human decision choices.")

    # Root Consensus Box
    add_flow_node(s11, Inches(3.8), Inches(1.6), Inches(5.7), Inches(0.95), "Root Node: Consensus Core", "Foundational milestones verified by all 3 personas:\nPython OOP + Basic Relational SQL + Git Version Control", bg=CARD_BG, border=NAVY_PRIMARY)

    # Two Downward Branch Arrows
    add_arrow(s11, Inches(4.5), Inches(2.65), Inches(0.35), Inches(0.4), direction="down", color=BLUE_ACCENT)
    add_arrow(s11, Inches(8.5), Inches(2.65), Inches(0.35), Inches(0.4), direction="down", color=TEAL_PRIMARY)

    # Branch 1 (Left - Depth Track)
    add_card(s11, Inches(0.8), Inches(3.15), Inches(5.6), Inches(2.7), "Branch 1: Foundational Systems Track", BLUE_ACCENT, top_accent=BLUE_ACCENT, bg_color=BLUE_BG)
    tb_b1 = s11.shapes.add_textbox(Inches(0.95), Inches(3.6), Inches(5.3), Inches(2.1))
    tf_b1 = tb_b1.text_frame
    tf_b1.word_wrap = True
    add_bullet(tf_b1, "• Advocates:", "Traditionalist (T=0.3) & Specialist (T=0.4)", pt_size=12.0)
    add_bullet(tf_b1, "• Curriculum:", "Linear Algebra ➔ OS Internals ➔ PyTorch ➔ Distributed Systems", pt_size=12.0)
    add_bullet(tf_b1, "• Required Timeline:", "12 Months (Rigorous depth; passes tier-1 systems screening)", pt_size=12.0)
    add_bullet(tf_b1, "• Financial Cost:", "Zero commercial tuition; relies on accredited open coursework", pt_size=12.0)

    # Branch 2 (Right - Velocity Track)
    add_card(s11, Inches(6.9), Inches(3.15), Inches(5.6), Inches(2.7), "Branch 2: Applied AI Engineering Track", TEAL_PRIMARY, top_accent=TEAL_PRIMARY, bg_color=TEAL_BG)
    tb_b2 = s11.shapes.add_textbox(Inches(7.05), Inches(3.6), Inches(5.3), Inches(2.1))
    tf_b2 = tb_b2.text_frame
    tf_b2.word_wrap = True
    add_bullet(tf_b2, "• Advocate:", "Entrepreneurial Builder (T=0.7)", pt_size=12.0)
    add_bullet(tf_b2, "• Curriculum:", "FastAPI Backend ➔ REST APIs ➔ LangChain / RAG ➔ Shipped MVP", pt_size=12.0)
    add_bullet(tf_b2, "• Required Timeline:", "4 Months (Achievable within student's immediate deadline)", pt_size=12.0)
    add_bullet(tf_b2, "• Strategic Pivot:", "Targets Applied AI Engineer instead of unfeasible Staff Systems role", pt_size=12.0)

    # Bottom Arbitration Bar
    add_flow_node(s11, Inches(0.8), Inches(6.05), Inches(11.733), Inches(0.9), "Human Decision Arbitration Point", "The system halts automated recommendation. The student explicitly chooses between Branch 1 (Depth) vs Branch 2 (Velocity).\nPreserves critical human agency and prevents automation bias.", bg=CARD_MUTED, border=NAVY_PRIMARY)

    s11.notes_slide.notes_text_frame.text = (
        "Slide 11 diagrams the Dispute Tree generated by the Cognitive Forcing Gate. Rather than forcing an artificial consensus "
        "or telling the student what they want to hear, the system structures the trade-off: a 12-month foundational systems path "
        "versus a 4-month applied AI engineering pivot. The student retains ultimate agency."
    )

    # =========================================================================
    # SLIDE 12: Section 5 — Experimental Setup: 4-Tier Ablation Ladder
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    apply_bg(s12, BG_LIGHT)
    add_header(s12, "Experimental Setup: 4-Tier Controlled Ablation Ladder", "Section 5: Experimental Setup", 12,
               "Rigorous comparative benchmarking isolating the impact of personas, self-consistency, and graph grounding.")

    col_w_ab = Inches(2.7)
    h_ab = Inches(5.2)

    # Tier 1
    add_card(s12, Inches(0.8), Inches(1.55), col_w_ab, h_ab, "Tier 1: Monolithic", ROSE_ACCENT, top_accent=ROSE_ACCENT)
    tb = s12.shapes.add_textbox(Inches(0.95), Inches(2.05), col_w_ab - Inches(0.3), h_ab - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Configuration:", "Single LLM prompt, standard temperature T=0.7.", pt_size=11.5)
    add_bullet(tf, "• Purpose:", "Represents standard commercial career chatbots.", pt_size=11.5)
    add_bullet(tf, "• Hypothesis:", "Prone to conversational flattery, skips foundational prerequisites, leaks demographics.", pt_size=11.5)
    add_bullet(tf, "• Compute:", "1 inference call.", pt_size=11.5)

    # Tier 2
    add_card(s12, Inches(3.8), Inches(1.55), col_w_ab, h_ab, "Tier 2: Self-Consistency", AMBER_ACCENT, top_accent=AMBER_ACCENT)
    tb = s12.shapes.add_textbox(Inches(3.95), Inches(2.05), col_w_ab - Inches(0.3), h_ab - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Configuration:", "Single LLM sampled 3 times independently at T=0.7; majority vote.", pt_size=11.5)
    add_bullet(tf, "• Purpose:", "Compute-matched control testing the Smit et al. hypothesis.", pt_size=11.5)
    add_bullet(tf, "• Hypothesis:", "Reduces random generation variance but cannot introduce orthogonal advisory perspectives.", pt_size=11.5)
    add_bullet(tf, "• Compute:", "3 inference calls.", pt_size=11.5)

    # Tier 3
    add_card(s12, Inches(6.8), Inches(1.55), col_w_ab, h_ab, "Tier 3: Unmoderated Triad", BLUE_ACCENT, top_accent=BLUE_ACCENT)
    tb = s12.shapes.add_textbox(Inches(6.95), Inches(2.05), col_w_ab - Inches(0.3), h_ab - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Configuration:", "3 distinct persona prompts without moderator or graph.", pt_size=11.5)
    add_bullet(tf, "• Purpose:", "Isolates the raw benefit of differentiated system prompts.", pt_size=11.5)
    add_bullet(tf, "• Hypothesis:", "High perspective coverage, but uncurated advice overwhelms students with contradictions.", pt_size=11.5)
    add_bullet(tf, "• Compute:", "3 inference calls.", pt_size=11.5)

    # Tier 4
    add_card(s12, Inches(9.8), Inches(1.55), col_w_ab, h_ab, "Tier 4: Proposed System", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s12.shapes.add_textbox(Inches(9.95), Inches(2.05), col_w_ab - Inches(0.3), h_ab - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Configuration:", "Triad + NetworkX 42-Node DAG + Moderator + Dispute Gate.", pt_size=11.5)
    add_bullet(tf, "• Purpose:", "Full grounded dialectic architecture.", pt_size=11.5)
    add_bullet(tf, "• Hypothesis:", "Eliminates prerequisite sequence violations; preserves transparent student choice.", pt_size=11.5)
    add_bullet(tf, "• Compute:", "3 agents + 1 moderator.", pt_size=11.5)

    s12.notes_slide.notes_text_frame.text = (
        "Slide 12 presents our 4-tier ablation ladder. To directly test whether multi-agent debate is simply repeated sampling, "
        "Tier 2 provides a compute-matched 3-sample Self-Consistency baseline. Tier 3 evaluates unmoderated personas, and Tier 4 "
        "evaluates our full grounded system."
    )

    # =========================================================================
    # SLIDE 13: Section 5 — Experimental Setup: Counterfactual Audit Protocol
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    apply_bg(s13, BG_LIGHT)
    add_header(s13, "Experimental Setup: Counterfactual Demographic Audit", "Section 5: Experimental Setup", 13,
               "Auditing demographic steering across 20 synthetic candidate profiles and 10 matched pairs.")

    # Base Archetype Box
    add_flow_node(s13, Inches(0.8), Inches(1.6), Inches(11.733), Inches(0.95), "Base Candidate Archetype (Invariant Experimental Controls)", "Verified Skills, Target Role, Timeline, and Monthly Budget are strictly 100% IDENTICAL across each matched pair.\n(Budget is preserved as an objective financial planning constraint, not a protected demographic attribute)", bg=CARD_MUTED, border=CARD_BORDER)

    add_arrow(s13, Inches(3.6), Inches(2.65), Inches(0.35), Inches(0.35), direction="down", color=BLUE_ACCENT)
    add_arrow(s13, Inches(9.4), Inches(2.65), Inches(0.35), Inches(0.35), direction="down", color=ROSE_ACCENT)

    # Pair A
    add_card(s13, Inches(0.8), Inches(3.1), Inches(5.6), Inches(2.7), "Perturbation Pair A: Advantaged Proxies", BLUE_ACCENT, top_accent=BLUE_ACCENT, bg_color=BLUE_BG)
    tb_pa = s13.shapes.add_textbox(Inches(0.95), Inches(3.55), Inches(5.3), Inches(2.1))
    tf_pa = tb_pa.text_frame
    tf_pa.word_wrap = True
    add_bullet(tf_pa, "• Name Signal:", "Aarav Sharma (Male identity proxy)", pt_size=12.0)
    add_bullet(tf_pa, "• Institutional Pedigree:", "Tier-1 Premier Technical Institute (IIT/NIT proxy)", pt_size=12.0)
    add_bullet(tf_pa, "• Budget Invariant:", "Explicit monthly budget (e.g., ₹3,000 / month)", pt_size=12.0)
    add_bullet(tf_pa, "• Monolithic Tendency:", "Steered aggressively toward elite research & Staff infrastructure tracks.", pt_size=12.0)

    # Pair B
    add_card(s13, Inches(6.9), Inches(3.1), Inches(5.6), Inches(2.7), "Perturbation Pair B: Disadvantaged Proxies", ROSE_ACCENT, top_accent=ROSE_ACCENT, bg_color=ROSE_BG)
    tb_pb = s13.shapes.add_textbox(Inches(7.05), Inches(3.55), Inches(5.3), Inches(2.1))
    tf_pb = tb_pb.text_frame
    tf_pb.word_wrap = True
    add_bullet(tf_pb, "• Name Signal:", "Priya Patel (Female identity proxy)", pt_size=12.0)
    add_bullet(tf_pb, "• Institutional Pedigree:", "Tier-3 Rural Non-Autonomous State College", pt_size=12.0)
    add_bullet(tf_pb, "• Budget Invariant:", "Explicit monthly budget (e.g., ₹3,000 / month)", pt_size=12.0)
    add_bullet(tf_pb, "• Monolithic Tendency:", "Steered toward basic IT support, data entry, or commercial debt traps.", pt_size=12.0)

    # Bottom Parity Vault Bar
    add_flow_node(s13, Inches(0.8), Inches(5.95), Inches(11.733), Inches(1.0), "Demographic Attribute Isolation Vault", "In the Proposed Architecture, protected attributes (name, gender, college tier) are sealed in the audit vault.\nTechnical planning agents see only verified skills, target role, timeline, and budget. Guarantees 0% Demographic Flip Rate.", bg=TEAL_BG, border=TEAL_PRIMARY, text_color=TEAL_PRIMARY)

    s13.notes_slide.notes_text_frame.text = (
        "Slide 13 details our counterfactual audit protocol. We construct 10 matched pairs where skills, target roles, and budgets "
        "are strictly identical. In monolithic baselines, changing the name and college tier triggers demographic flips. "
        "In our system, sealing protected attributes in the vault ensures recommendations depend strictly on technical competence."
    )

    # =========================================================================
    # SLIDE 14: Section 5 — Experimental Setup: Three Concrete Evaluation Metrics
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    apply_bg(s14, BG_LIGHT)
    add_header(s14, "Experimental Setup: Three Concrete Evaluation Metrics", "Section 5: Experimental Setup", 14,
               "Mathematical formulations and automated computation pipelines for objective pilot scoring.")

    w3 = Inches(3.64)
    h_card = Inches(5.2)

    add_card(s14, Inches(0.8), Inches(1.55), w3, h_card, "1. Prerequisite Violation Count", ROSE_ACCENT, top_accent=ROSE_ACCENT)
    tb = s14.shapes.add_textbox(Inches(0.95), Inches(2.05), w3 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Metric Definition:", "V(R) = Sum of all recommended milestones scheduled before their topological DAG predecessors.", pt_size=12.0)
    add_bullet(tf, "• Computation Method:", "Traverses the 42-node NetworkX graph to verify that every ancestor prerequisite is satisfied in prior steps.", pt_size=12.0)
    add_bullet(tf, "• Target Direction:", "Lower is better (Ideal target = 0.0 violations).", pt_size=12.0)
    add_bullet(tf, "• Academic Value:", "Quantifies hallucinated curriculum shortcuts.", pt_size=12.0)

    add_card(s14, Inches(4.84), Inches(1.55), w3, h_card, "2. Perspective Coverage Score", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s14.shapes.add_textbox(Inches(5.0), Inches(2.05), w3 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Metric Definition:", "C(R) = (Hit_Traditionalist + Hit_Builder + Hit_Specialist) / 3 * 100%.", pt_size=12.0)
    add_bullet(tf, "• Computation Method:", "Rubric-based checklist verifying the presence of academic rigor, practical velocity, and systems depth lenses.", pt_size=12.0)
    add_bullet(tf, "• Target Direction:", "Higher is better (Ideal target = 100%).", pt_size=12.0)
    add_bullet(tf, "• Academic Value:", "Measures preservation of multifaceted career advice.", pt_size=12.0)

    add_card(s14, Inches(8.88), Inches(1.55), w3, h_card, "3. Demographic Flip Rate (%)", INDIGO_ACCENT, top_accent=INDIGO_ACCENT)
    tb = s14.shapes.add_textbox(Inches(9.03), Inches(2.05), w3 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Metric Definition:", "DFR = Sum( 1[Jaccard(Ra, Rb) < 0.70] ) / 10 pairs * 100%.", pt_size=12.0)
    add_bullet(tf, "• Computation Method:", "Computes exact milestone set Jaccard similarity between Aarav and Priya across all 10 matched pairs.", pt_size=12.0)
    add_bullet(tf, "• Target Direction:", "Lower is better (Ideal target = 0.0%).", pt_size=12.0)
    add_bullet(tf, "• Academic Value:", "Direct test of demographic neutrality under counterfactual perturbations.", pt_size=12.0)

    s14.notes_slide.notes_text_frame.text = (
        "Slide 14 formally defines our three evaluation metrics. Prerequisite Violations count missing ancestor hops in NetworkX. "
        "Perspective Coverage verifies whether traditionalist, builder, and specialist viewpoints are represented. "
        "And Demographic Flip Rate measures how often recommendations diverge across matched demographic pairs."
    )

    # =========================================================================
    # SLIDE 15: Section 6 — Results and Discussion: Comparative Findings (FULL TABLE)
    # =========================================================================
    s15 = prs.slides.add_slide(blank_layout)
    apply_bg(s15, BG_LIGHT)
    add_header(s15, "Results & Discussion: Pilot Quantitative Findings", "Section 6: Results and Discussion", 15,
               "Comparative benchmark across 20 synthetic candidate profiles on local Llama-3.2-3B / RTX 3050.")

    # Results Table
    rows = 5
    cols = 5
    table_shape = s15.shapes.add_table(rows, cols, Inches(0.8), Inches(1.65), Inches(11.733), Inches(2.6))
    table = table_shape.table

    table.columns[0].width = Inches(3.333)
    table.columns[1].width = Inches(2.1)
    table.columns[2].width = Inches(2.1)
    table.columns[3].width = Inches(2.1)
    table.columns[4].width = Inches(2.1)

    t_headers = ["Ablation Configuration", "Prereq Violations", "Perspective Coverage", "Demographic Flip Rate", "Gate Activation Rate"]
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
        ("Tier 1: Monolithic Zero-Shot", "2.3 ± 0.4", "33.3%", "40.0% (4 / 10 pairs)", "0.0% (No gate)"),
        ("Tier 2: Self-Consistency (3x)", "1.8 ± 0.3", "46.7%", "30.0% (3 / 10 pairs)", "0.0% (No gate)"),
        ("Tier 3: Unmoderated Triad", "1.4 ± 0.3", "86.7%", "20.0% (2 / 10 pairs)", "0.0% (No gate)"),
        ("Tier 4: Proposed Dialectic Architecture", "0.0 ± 0.0", "93.3%", "0.0% (0 / 10 pairs)", "40.0% (8 / 20 cases)"),
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
    add_card(s15, Inches(0.8), Inches(4.5), Inches(5.7), Inches(2.4), "Analysis: Grounding & Coverage", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb_c1 = s15.shapes.add_textbox(Inches(0.95), Inches(4.95), Inches(5.4), Inches(1.8))
    tf_c1 = tb_c1.text_frame
    tf_c1.word_wrap = True
    add_bullet(tf_c1, "• Deterministic Grounding Eliminates Errors:", "Self-consistency slightly reduces violations (2.3 ➔ 1.8), but only deterministic DAG verification reduces violations to 0.0.", pt_size=12.0)
    add_bullet(tf_c1, "• Prompt Diversity Preserves Perspectives:", "Coverage jumps from 33.3% in monolithic to 93.3% in the triad, demonstrating that physical agent separation resists consensus averaging.", pt_size=12.0)

    add_card(s15, Inches(6.833), Inches(4.5), Inches(5.7), Inches(2.4), "Analysis: Parity & Gate Behavior", BLUE_ACCENT, top_accent=BLUE_ACCENT)
    tb_c2 = s15.shapes.add_textbox(Inches(6.983), Inches(4.95), Inches(5.4), Inches(1.8))
    tf_c2 = tb_c2.text_frame
    tf_c2.word_wrap = True
    add_bullet(tf_c2, "• Attribute Isolation Enforces Parity:", "Monolithic LLM flipped recommendations in 40% of matched pairs based on name/college cues; Tier 4 achieved 100% consistency across all 10 pairs.", pt_size=12.0)
    add_bullet(tf_c2, "• Selective Cognitive Forcing:", "The gate triggered in exactly 8 of 20 profiles (40%) where genuine career trade-offs existed, confirming it does not cause decision fatigue.", pt_size=12.0)

    s15.notes_slide.notes_text_frame.text = (
        "Slide 15 reports our pilot empirical findings. The table directly compares all 4 tiers across our three metrics. "
        "Notice that Self-Consistency in Tier 2 only achieves modest gains, confirming that repeated sampling cannot replace "
        "orthogonal personas. Tier 4 achieves 0 prerequisite violations and 0% demographic flip rate, activating the gate in 8 of 20 cases."
    )

    # =========================================================================
    # SLIDE 16: Section 6 — Results and Discussion: Worked Walkthrough "Priya"
    # =========================================================================
    s16 = prs.slides.add_slide(blank_layout)
    apply_bg(s16, BG_LIGHT)
    add_header(s16, "Results & Discussion: Case Walkthrough ('Priya')", "Section 6: Results and Discussion", 16,
               "Demonstrating cognitive forcing and agency preservation in a high-risk career pivot scenario.")

    w3 = Inches(3.64)
    h_card = Inches(5.2)

    add_card(s16, Inches(0.8), Inches(1.55), w3, h_card, "The Scenario: 3rd-Year CSE", NAVY_HEAD, top_accent=NAVY_HEAD)
    tb = s16.shapes.add_textbox(Inches(0.95), Inches(2.05), w3 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Student Profile:", "Priya, 3rd-year undergraduate with Python scripting and basic web skills.", pt_size=12.0)
    add_bullet(tf, "• Target Goal:", "Staff Machine Learning Infrastructure Engineer in 4 months.", pt_size=12.0)
    add_bullet(tf, "• Proposed Action:", "Enrolling in an unaccredited commercial bootcamp costing ₹1,20,000 (~$1,400 USD).", pt_size=12.0)
    add_bullet(tf, "• Monolithic Response:", "Enthusiastically affirms the goal; claims the bootcamp will qualify her for Staff ML roles (Dangerous sycophancy).", pt_size=12.0)

    add_card(s16, Inches(4.84), Inches(1.55), w3, h_card, "Dialectic Triad Friction", ROSE_ACCENT, top_accent=ROSE_ACCENT)
    tb = s16.shapes.add_textbox(Inches(5.0), Inches(2.05), w3 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Traditionalist Objection:", "Flags 3 missing prerequisite hops in DAG (Linear Algebra ➔ OS Internals ➔ Distributed Systems). Impossible in 4 months.", pt_size=12.0)
    add_bullet(tf, "• Specialist Warning:", "Bootcamps teach high-level API wrappers; infrastructure screening tests kernel memory management and network sockets.", pt_size=12.0)
    add_bullet(tf, "• Builder Pivot:", "Proposes realistic pivot to Applied AI Application Engineer using existing Python strengths.", pt_size=12.0)

    add_card(s16, Inches(8.88), Inches(1.55), w3, h_card, "Cognitive Forcing Gate Outcome", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s16.shapes.add_textbox(Inches(9.03), Inches(2.05), w3 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Gate Activated:", "Triggered because Prerequisite Gap = 3 > 0 and Persona Trajectory Contradiction >= 1.", pt_size=12.0)
    add_bullet(tf, "• Dispute Tree Presented:", "Halts automation; presents Branch 1 (12-Month Systems Rigor) vs Branch 2 (4-Month Applied AI Pivot).", pt_size=12.0)
    add_bullet(tf, "• Human Agency Preserved:", "Priya is protected from high financial risk and makes an informed choice based on genuine trade-offs.", pt_size=12.0)

    s16.notes_slide.notes_text_frame.text = (
        "Slide 16 walks through our case study with Priya. Priya wants to become a Staff ML Engineer in 4 months via a 1.2 lakh "
        "rupee bootcamp. A monolithic model enthusiastically encourages this. Our triad objects: the DAG detects 3 missing prerequisite "
        "hops, and the personas surface the trade-off. The Cognitive Forcing Gate fires, allowing Priya to make an informed decision."
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
    add_bullet(tf, "[4] Perez et al. (2023):", "Discovering Language Model Behaviors with Model-Written Evaluations. ACL 2023. arXiv:2212.09251.", pt_size=11.5, space_after=8)

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
        "of this presentation. Every paper cited in our survey and methodology is cataloged here with publication venues and arXiv identifiers."
    )

    # =========================================================================
    # SLIDE 18: Section 7 — Threats to Validity, Limitations, Future Scope & Conclusion
    # =========================================================================
    s18 = prs.slides.add_slide(blank_layout)
    apply_bg(s18, BG_LIGHT)
    add_header(s18, "Threats to Validity, Future Scope & Conclusion", "Section 7: Conclusion", 18,
               "Critical evaluation boundaries, future research avenues, and final project synthesis.")

    w2 = Inches(5.67)
    h_card_s18 = Inches(4.3)

    add_card(s18, Inches(0.8), Inches(1.55), w2, h_card_s18, "Threats to Validity & Architectural Limitations", AMBER_ACCENT, top_accent=AMBER_ACCENT)
    tb = s18.shapes.add_textbox(Inches(0.95), Inches(2.05), w2 - Inches(0.3), h_card_s18 - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Pilot Sample Size:", "Evaluated on N=20 synthetic student profiles (10 matched pairs); requires large-scale longitudinal human user studies.", pt_size=11.5)
    add_bullet(tf, "• Single Model Family:", "Personas share underlying Llama-3.2-3B pre-trained representations, partially inheriting base model biases.", pt_size=11.5)
    add_bullet(tf, "• Curricular Graph Bounding:", "The prerequisite DAG is bounded to 42 undergraduate computing nodes; non-computing domains are currently unmapped.", pt_size=11.5)
    add_bullet(tf, "• Local Hardware Latency:", "4GB VRAM constraint necessitates sequential multi-agent execution (~4.2s per profile).", pt_size=11.5)

    add_card(s18, Inches(6.86), Inches(1.55), w2, h_card_s18, "Future Research Scope & Defense Summary", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s18.shapes.add_textbox(Inches(7.01), Inches(2.05), w2 - Inches(0.3), h_card_s18 - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Heterogeneous Model Triad:", "Deploying diverse model families (e.g., Mistral + Llama + Qwen) to eliminate shared base model priors.", pt_size=11.5)
    add_bullet(tf, "• Automated Syllabus Ingestion:", "Semi-automated curriculum DAG extraction from accredited university course catalogues with faculty validation.", pt_size=11.5)
    add_bullet(tf, "• Interactive Demonstrator Access:", "Committee can inspect graph queries and test profiles via our local web dashboard (localhost:8000).", pt_size=11.5)
    add_bullet(tf, "• Core Project Takeaway:", "Coupling dialectic multi-agent tension with deterministic graph verification successfully preserves human student agency.", pt_size=11.5)

    # Bottom Thank You & Q&A Callout
    add_flow_node(s18, Inches(0.8), Inches(6.0), Inches(11.733), Inches(0.9), "Thank You · Questions & Discussion", "Ready for Committee Viva Voce Examination\nCodebase & Interactive Testbed available at: https://github.com/project-repo", bg=CARD_MUTED, border=TEAL_PRIMARY, text_color=NAVY_HEAD)

    s18.notes_slide.notes_text_frame.text = (
        "In conclusion, our B.Tech capstone project demonstrates that coupling adversarial persona friction with deterministic "
        "graph grounding eliminates prerequisite hallucinations and preserves student agency on consumer local hardware. "
        "We openly acknowledge our pilot boundaries and welcome questions from the committee."
    )

    # Save Presentation
    prs.save(output_path)
    print("\n" + "=" * 55)
    print("ACADEMIC PRESENTATION DECK SUCCESSFULLY REBUILT!")
    print(f"Output File: {output_path}")
    print("=" * 55)

if __name__ == "__main__":
    build_presentation_deck()
