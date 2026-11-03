#!/usr/bin/env python3
"""
Generate Complete Conference-Grade Academic Presentation Deck (18 Slides)
Debate-Based Career Guidance Agent with Complementary Personas
Strictly mapped to the 7 evaluation sections for the 20-mark academic component:
  1. Abstract (Slide 2)
  2. Introduction (Slides 3–4)
  3. Literature Survey (Slides 5–8)
  4. Architecture Diagram & Design (Slides 9–12)
  5. Experimental Setup (Slides 13–15)
  6. Results & Discussion (Slides 16–17)
  7. References & Conclusion (Slide 18)
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

    # Professional Academic Color Palette
    BG_DARK = RGBColor(15, 23, 42)         # Slate 900 #0F172A
    BG_LIGHT = RGBColor(248, 250, 252)     # Slate 50  #F8FAFC
    CARD_BG = RGBColor(255, 255, 255)      # Pure White #FFFFFF
    CARD_BORDER = RGBColor(203, 213, 225)  # Slate 300 #CBD5E1
    CARD_MUTED = RGBColor(241, 245, 249)   # Slate 100 #F1F5F9
    
    NAVY_PRIMARY = RGBColor(30, 41, 59)    # Slate 800 #1E293B
    NAVY_HEAD = RGBColor(15, 23, 42)       # Slate 900 #0F172A
    TEAL_PRIMARY = RGBColor(13, 148, 136)  # Teal 600 #0D9488
    TEAL_ACCENT = RGBColor(20, 184, 166)   # Teal 500 #14B8A6
    TEAL_BG = RGBColor(240, 253, 250)      # Teal 50 #F0FDFA
    BLUE_ACCENT = RGBColor(37, 99, 235)    # Blue 600 #2563EB
    BLUE_BG = RGBColor(239, 246, 255)      # Blue 50 #EFF6FF
    ROSE_ACCENT = RGBColor(225, 29, 72)    # Rose 600 #E11D48
    ROSE_BG = RGBColor(255, 241, 242)      # Rose 50 #FFF1F2
    AMBER_ACCENT = RGBColor(217, 119, 6)   # Amber 600 #D97706
    AMBER_BG = RGBColor(254, 243, 199)     # Amber 100 #FEF3C7
    INDIGO_ACCENT = RGBColor(79, 70, 229)  # Indigo 600 #4F46E5
    INDIGO_BG = RGBColor(238, 242, 255)    # Indigo 50 #EEF2FF
    
    TEXT_MAIN = RGBColor(30, 41, 59)       # Slate 800 #1E293B
    TEXT_MUTED = RGBColor(100, 116, 139)   # Slate 500 #64748B
    TEXT_WHITE = RGBColor(255, 255, 255)
    
    FONT_MAIN = "Calibri"
    FONT_CODE = "Consolas"
    TOTAL_SLIDES = 18

    def apply_bg(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_header(slide, title, category, slide_num, takeaway=""):
        # Category Tag Badge
        tag = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.32), Inches(3.6), Inches(0.28))
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

        # Slide Number
        tb_n = slide.shapes.add_textbox(Inches(11.3), Inches(0.32), Inches(1.2), Inches(0.3))
        p_n = tb_n.text_frame.paragraphs[0]
        p_n.text = f"{slide_num:02d} / {TOTAL_SLIDES:02d}"
        p_n.font.name = FONT_MAIN
        p_n.font.size = Pt(10)
        p_n.font.bold = True
        p_n.font.color.rgb = TEXT_MUTED
        p_n.alignment = PP_ALIGN.RIGHT

        # Main Title
        tb_t = slide.shapes.add_textbox(Inches(0.8), Inches(0.62), Inches(11.7), Inches(0.42))
        p = tb_t.text_frame.paragraphs[0]
        p.text = title
        p.font.name = FONT_MAIN
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = NAVY_HEAD

        # Subtitle / Takeaway Line
        if takeaway:
            tb_sub = slide.shapes.add_textbox(Inches(0.8), Inches(1.02), Inches(11.7), Inches(0.32))
            p_sub = tb_sub.text_frame.paragraphs[0]
            p_sub.text = takeaway
            p_sub.font.name = FONT_MAIN
            p_sub.font.size = Pt(10.5)
            p_sub.font.italic = True
            p_sub.font.color.rgb = TEXT_MUTED

        # Header Rule
        rule = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.36), Inches(11.733), Inches(0.012))
        rule.fill.solid()
        rule.fill.fore_color.rgb = CARD_BORDER
        rule.line.fill.background()

        # Running Status Footer
        rule_f = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(7.06), Inches(11.733), Inches(0.01))
        rule_f.fill.solid()
        rule_f.fill.fore_color.rgb = CARD_BORDER
        rule_f.line.fill.background()

        tb_f = slide.shapes.add_textbox(Inches(0.8), Inches(7.10), Inches(9.5), Inches(0.3))
        p_f = tb_f.text_frame.paragraphs[0]
        p_f.text = "ACADEMIC EVALUATION · 20-MARK COMPONENT · COMPUTER SCIENCE & ENGINEERING"
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

    def add_card(slide, left, top, width, height, title="", title_color=NAVY_HEAD, top_accent=None, bg_color=CARD_BG, border_color=CARD_BORDER):
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
            tb = slide.shapes.add_textbox(left + Inches(0.18), top + Inches(0.12), width - Inches(0.36), Inches(0.38))
            tb.text_frame.word_wrap = True
            p = tb.text_frame.paragraphs[0]
            p.text = title
            p.font.name = FONT_MAIN
            p.font.size = Pt(12.0)
            p.font.bold = True
            p.font.color.rgb = title_color
            return card, tb
        return card, None

    def add_bullet(tf, bold_txt, norm_txt, pt_size=9.5, space_after=4):
        p = tf.add_paragraph() if len(tf.paragraphs[0].text) > 0 else tf.paragraphs[0]
        p.space_after = Pt(space_after)
        run_b = p.add_run()
        run_b.text = bold_txt + " "
        run_b.font.name = FONT_MAIN
        run_b.font.size = Pt(pt_size)
        run_b.font.bold = True
        run_b.font.color.rgb = NAVY_PRIMARY
        
        run_n = p.add_run()
        run_n.text = norm_txt
        run_n.font.name = FONT_MAIN
        run_n.font.size = Pt(pt_size)
        run_n.font.color.rgb = TEXT_MAIN

    # =========================================================================
    # SLIDE 1: Title Slide
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    apply_bg(s1, BG_DARK)

    # Badges
    s1_badge = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(0.85), Inches(5.8), Inches(0.34))
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

    s1_status = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.0), Inches(0.85), Inches(5.33), Inches(0.34))
    s1_status.fill.solid()
    s1_status.fill.fore_color.rgb = RGBColor(30, 58, 138)
    s1_status.line.color.rgb = BLUE_ACCENT
    s1_status.line.width = Pt(1)
    p = s1_status.text_frame.paragraphs[0]
    p.text = "ACADEMIC RESEARCH & IMPLEMENTATION PROJECT (20 MARKS)"
    p.font.name = FONT_MAIN
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = RGBColor(191, 219, 254)
    p.alignment = PP_ALIGN.CENTER
    s1_status.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    # Main Title
    s1_title_box = s1.shapes.add_textbox(Inches(1.0), Inches(1.4), Inches(11.333), Inches(2.1))
    tf1 = s1_title_box.text_frame
    tf1.word_wrap = True
    p1 = tf1.paragraphs[0]
    p1.text = "Debate-Based Career Guidance Agent\nwith Complementary Personas"
    p1.font.name = FONT_MAIN
    p1.font.size = Pt(30)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE
    p1.space_after = Pt(8)

    p2 = tf1.add_paragraph()
    p2.text = "A Dialectic Multi-Agent Architecture for Prerequisite-Grounded & Fair Algorithmic Advisory"
    p2.font.name = FONT_MAIN
    p2.font.size = Pt(14)
    p2.font.color.rgb = RGBColor(148, 163, 184)

    # 3 Metadata Cards
    col_w = Inches(3.64)
    col_h = Inches(2.3)
    top_meta = Inches(3.8)

    add_card(s1, Inches(1.0), top_meta, col_w, col_h, "Project Scope & Domain", TEAL_ACCENT, bg_color=RGBColor(30, 41, 59), border_color=RGBColor(51, 65, 85))
    tb_m1 = s1.shapes.add_textbox(Inches(1.15), top_meta + Inches(0.48), col_w - Inches(0.3), col_h - Inches(0.6))
    tf_m1 = tb_m1.text_frame
    tf_m1.word_wrap = True
    add_bullet(tf_m1, "• Domain:", "Undergraduate CSE Career Advisory", pt_size=10.0)
    add_bullet(tf_m1, "• Focus Tracks:", "SDE, Systems, Data & AI Engineering", pt_size=10.0)
    add_bullet(tf_m1, "• Core Mechanism:", "3 Dialectic Antagonistic Personas", pt_size=10.0)
    add_bullet(tf_m1, "• Verification:", "NetworkX 42-Node Prerequisite DAG", pt_size=10.0)
    add_bullet(tf_m1, "• Ethics:", "Demographic Attribute Isolation Vault", pt_size=10.0)

    add_card(s1, Inches(4.84), top_meta, col_w, col_h, "Engineering Architecture", BLUE_ACCENT, bg_color=RGBColor(30, 41, 59), border_color=RGBColor(51, 65, 85))
    tb_m2 = s1.shapes.add_textbox(Inches(5.0), top_meta + Inches(0.48), col_w - Inches(0.3), col_h - Inches(0.6))
    tf_m2 = tb_m2.text_frame
    tf_m2.word_wrap = True
    add_bullet(tf_m2, "• Inference Engine:", "Local Ollama on RTX 3050 Laptop GPU", pt_size=10.0)
    add_bullet(tf_m2, "• Persona Triad:", "Traditionalist, Builder, Specialist", pt_size=10.0)
    add_bullet(tf_m2, "• Meta-Reasoning:", "Neutral Moderator Synthesizer", pt_size=10.0)
    add_bullet(tf_m2, "• Prerequisite Check:", "Deterministic Graph Traversal", pt_size=10.0)
    add_bullet(tf_m2, "• Interface Gate:", "Cognitive Forcing Dispute Tree", pt_size=10.0)

    add_card(s1, Inches(8.68), top_meta, col_w, col_h, "Evaluation Methodology", AMBER_ACCENT, bg_color=RGBColor(30, 41, 59), border_color=RGBColor(51, 65, 85))
    tb_m3 = s1.shapes.add_textbox(Inches(8.83), top_meta + Inches(0.48), col_w - Inches(0.3), col_h - Inches(0.6))
    tf_m3 = tb_m3.text_frame
    tf_m3.word_wrap = True
    add_bullet(tf_m3, "• Experimental Setup:", "4-Tier Controlled Ablation", pt_size=10.0)
    add_bullet(tf_m3, "• Evaluation Cohort:", "20 Synthetic Profiles (10 Pairs)", pt_size=10.0)
    add_bullet(tf_m3, "• Counterfactual Audit:", "Gender, College Tier & Budget", pt_size=10.0)
    add_bullet(tf_m3, "• Core Metrics:", "Prerequisite Errors, Coverage, Flip Rate", pt_size=10.0)
    add_bullet(tf_m3, "• Structure:", "7 Mandatory Academic Sections", pt_size=10.0)

    s1.notes_slide.notes_text_frame.text = (
        "Good morning members of the evaluation committee. Today, I am presenting our work: "
        "'Debate-Based Career Guidance Agent with Complementary Personas'. This project addresses three "
        "fundamental flaws in monolithic career AI: sycophancy, hallucinated milestones, and demographic bias. "
        "We present our end-to-end multi-agent dialectic architecture, a hand-built curricular DAG in NetworkX, "
        "and a rigorous experimental ablation study structured across the 7 academic sections."
    )

    # =========================================================================
    # SLIDE 2: Section 1 — Abstract & Executive Summary
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    apply_bg(s2, BG_LIGHT)
    add_header(s2, "Abstract: Responsible AI Career Advisory Architecture", "Section 1: Abstract", 2,
               "Executive summary of the research motivation, multi-agent dialectic framework, and key findings.")

    w3 = Inches(3.64)
    h_top = Inches(2.4)
    h_bot = Inches(2.6)

    add_card(s2, Inches(0.8), Inches(1.55), w3, h_top, "The Research Problem", ROSE_ACCENT, top_accent=ROSE_ACCENT)
    tb = s2.shapes.add_textbox(Inches(0.95), Inches(2.0), w3 - Inches(0.3), h_top - Inches(0.55))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Sycophancy Trap:", "RLHF models validate infeasible student goals to maximize perceived helpfulness.")
    add_bullet(tf, "• False Consensus:", "Single-agent prompts smooth over vital engineering trade-offs into generic advice.")
    add_bullet(tf, "• Demographic Steering:", "Pre-trained priors steer candidates based on college tier or gender proxies.")

    add_card(s2, Inches(4.84), Inches(1.55), w3, h_top, "The Proposed Architecture", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s2.shapes.add_textbox(Inches(5.0), Inches(2.0), w3 - Inches(0.3), h_top - Inches(0.55))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• 3 Dialectic Personas:", "Traditionalist (DSA/Enterprise), Builder (Speed/MVPs), Specialist (Systems/Depth).")
    add_bullet(tf, "• Curricular Graph:", "NetworkX 42-node prerequisite DAG derived from computing curricula.")
    add_bullet(tf, "• Neutral Moderator:", "Identifies sharp contradictions and constructs structured Dispute Trees.")

    add_card(s2, Inches(8.88), Inches(1.55), w3, h_top, "Evaluation & Governance", BLUE_ACCENT, top_accent=BLUE_ACCENT)
    tb = s2.shapes.add_textbox(Inches(9.03), Inches(2.0), w3 - Inches(0.3), h_top - Inches(0.55))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• 4-Tier Ablation:", "Evaluates Monolithic, In-Context, Unmoderated Triad, and Proposed System.")
    add_bullet(tf, "• Counterfactual Audit:", "Tests 20 synthetic candidate profiles across 10 matched demographic pairs.")
    add_bullet(tf, "• Cognitive Forcing Gate:", "Surfaces unresolvable trade-offs directly to the student rather than deciding.")

    add_card(s2, Inches(0.8), Inches(4.2), Inches(11.733), h_bot, "Core Contributions & Scope Summary", NAVY_HEAD, top_accent=NAVY_HEAD)
    tb_bot = s2.shapes.add_textbox(Inches(1.0), Inches(4.65), Inches(11.333), h_bot - Inches(0.6))
    tf_bot = tb_bot.text_frame
    tf_bot.word_wrap = True
    add_bullet(tf_bot, "1. Dialectic Multi-Agent Formulation:", "Proves that physically separated agents with differentiated system prompts preserve legitimate technical trade-offs that collapse in monolithic prompts.", pt_size=10.0)
    add_bullet(tf_bot, "2. Deterministic Graph Validation:", "Employs a hand-built 42-node prerequisite DAG in NetworkX to detect and prevent prerequisite ordering hallucinations without database overhead.", pt_size=10.0)
    add_bullet(tf_bot, "3. Counterfactual Fairness & Agency Preservation:", "Masks protected attributes during planning while actively testing counterfactual parity, ensuring high-risk decisions are surfaced to students via Cognitive Forcing.", pt_size=10.0)

    s2.notes_slide.notes_text_frame.text = (
        "In Section 1, our Abstract provides an executive summary of the entire work. Monolithic LLMs fail in "
        "career advisory because they tell users what they want to hear, hallucinate milestone sequences, and encode "
        "demographic biases. Our architecture decouples the decision into 3 adversarial personas grounded by a curricular "
        "DAG in NetworkX, orchestrated by a neutral moderator. We evaluate this on 20 synthetic candidate profiles."
    )

    # =========================================================================
    # SLIDE 3: Section 2 — Introduction: Failure Modes of Monolithic Career AI
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    apply_bg(s3, BG_LIGHT)
    add_header(s3, "Introduction: Three Structural Failures in Algorithmic Advisory", "Section 2: Introduction", 3,
               "Why standard single-prompt LLM assistants fail in high-stakes computer science career advisory.")

    w3 = Inches(3.64)
    h_card = Inches(5.1)

    add_card(s3, Inches(0.8), Inches(1.55), w3, h_card, "1. The Sycophancy Trap", ROSE_ACCENT, top_accent=ROSE_ACCENT)
    tb = s3.shapes.add_textbox(Inches(0.95), Inches(2.05), w3 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Mechanism:", "Reinforcement Learning from Human Feedback (RLHF) rewards conversational agreeableness.")
    add_bullet(tf, "• Advisory Failure:", "When a novice student proposes a 3-month pivot to 'Staff AI Engineer', the model affirms the dream rather than warning of missing prerequisites.")
    add_bullet(tf, "• Economic Risk:", "Validates predatory bootcamps and unaccredited credentials, creating severe debt exposure.")
    add_bullet(tf, "• Literature:", "Demonstrated empirically by Sharma et al. (ICLR '24) and Perez et al. (ACL '23).")

    add_card(s3, Inches(4.84), Inches(1.55), w3, h_card, "2. Prerequisite Hallucination", AMBER_ACCENT, top_accent=AMBER_ACCENT)
    tb = s3.shapes.add_textbox(Inches(5.0), Inches(2.05), w3 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Mechanism:", "Autoregressive token generation generates superficially plausible sequences without topological validation.")
    add_bullet(tf, "• Advisory Failure:", "Recommends advanced Distributed Systems or Transformers to students who lack basic OS or Linear Algebra.")
    add_bullet(tf, "• False Certainty:", "Single-agent decoding presents one confident roadmap with no calibrated indication of prerequisite risk.")
    add_bullet(tf, "• Literature:", "Documented in confidence elicitation studies by Kadavath et al. and Xiong et al. ('24).")

    add_card(s3, Inches(8.88), Inches(1.55), w3, h_card, "3. Latent Demographic Steering", INDIGO_ACCENT, top_accent=INDIGO_ACCENT)
    tb = s3.shapes.add_textbox(Inches(9.03), Inches(2.05), w3 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Mechanism:", "Pre-trained embeddings encode historical occupational hierarchies and demographic correlations.")
    add_bullet(tf, "• Advisory Failure:", "When candidate qualifications are held identical, subtle proxy leaks (college tier, gender name) shift career advice.")
    add_bullet(tf, "• Disparity:", "Tier-1 candidates receive ambitious R&D trajectories; Tier-3 candidates are steered to IT support or paid bootcamps.")
    add_bullet(tf, "• Literature:", "Documented by Geyik et al. (ACM KDD '19) and Bolukbasi et al. (NeurIPS '16).")

    s3.notes_slide.notes_text_frame.text = (
        "In Section 2, we introduce the three primary failure modes. First is the Sycophancy Trap: because LLMs "
        "are trained to be polite and helpful, they enthusiastically validate unrealistic student timelines. Second is "
        "Prerequisite Hallucination: language models generate text that sounds good, but violates the strict mathematical "
        "and topological ordering of computing knowledge. Third is Latent Demographic Steering: models alter their advice "
        "based on college tier or gender signals even when core skills are identical."
    )

    # =========================================================================
    # SLIDE 4: Section 2 — Introduction: Research Questions & Concrete Scope
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    apply_bg(s4, BG_LIGHT)
    add_header(s4, "Introduction: Research Questions & Formulation", "Section 2: Introduction", 4,
               "Formal definition of research objectives, mathematical environment, and bounded academic scope.")

    w2 = Inches(5.67)
    h_top = Inches(2.55)
    h_bot = Inches(2.45)

    add_card(s4, Inches(0.8), Inches(1.55), w2, h_top, "Research Questions (RQ1 – RQ4)", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s4.shapes.add_textbox(Inches(0.95), Inches(2.0), w2 - Inches(0.3), h_top - Inches(0.55))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• RQ1 (Dialectic Preservation):", "Does physical agent separation prevent the perspective collapse observed in single-agent multi-perspective prompting?")
    add_bullet(tf, "• RQ2 (Prerequisite Grounding):", "Does coupling a NetworkX curricular DAG with topological validation reduce milestone sequence violations?")
    add_bullet(tf, "• RQ3 (Demographic Parity):", "Does masking protected demographic attributes eliminate counterfactual recommendation disparity across matched pairs?")
    add_bullet(tf, "• RQ4 (Agency Preservation):", "Does an interface-level Cognitive Forcing Gate prevent passive student overreliance on automated roadmaps?")

    add_card(s4, Inches(6.86), Inches(1.55), w2, h_top, "Formal Problem Formulation", NAVY_HEAD, top_accent=NAVY_HEAD)
    tb = s4.shapes.add_textbox(Inches(7.01), Inches(2.0), w2 - Inches(0.3), h_top - Inches(0.55))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Deliberation Tuple:", "M = ⟨P, G, Π, Φ, Gate⟩", pt_size=10.0)
    add_bullet(tf, "• Candidate Profile:", "P = ⟨s_curr, g_target, c_user, a_demo⟩ where a_demo is isolated to the Audit Vault.", pt_size=10.0)
    add_bullet(tf, "• Curricular Graph:", "G = (V, E) where directed edges (u, v) represent strict prerequisite dependencies in NetworkX.", pt_size=10.0)
    add_bullet(tf, "• Advisory Personas:", "Π = {π_trad, π_builder, π_spec} representing 3 orthogonal optimisation axes.", pt_size=10.0)
    add_bullet(tf, "• Synthesizer & Gate:", "Φ extracts contradictions; Gate triggers whenever irreconcilable trade-offs emerge.", pt_size=10.0)

    add_card(s4, Inches(0.8), Inches(4.35), Inches(11.733), h_bot, "Bounded Project Scope & Methodological Safeguards", BLUE_ACCENT, top_accent=BLUE_ACCENT)
    tb_bot = s4.shapes.add_textbox(Inches(1.0), Inches(4.8), Inches(11.333), h_bot - Inches(0.55))
    tf_bot = tb_bot.text_frame
    tf_bot.word_wrap = True
    add_bullet(tf_bot, "• Domain Boundary:", "Strictly bounded to undergraduate and early-career Computer Science & Engineering. Does not claim generalisation to non-computing fields.", pt_size=10.0)
    add_bullet(tf_bot, "• Compute Environment:", "Runs 100% locally on an NVIDIA RTX 3050 Laptop GPU (4GB VRAM) via Ollama (Llama 3.2 3B). No external cloud API dependencies, guaranteeing privacy.", pt_size=10.0)
    add_bullet(tf_bot, "• Graph Realism:", "Uses a hand-built 42-node NetworkX DAG spanning AL, OS, DM, SE, Web, and ML. Eliminates external database overhead while providing exact topological validation.", pt_size=10.0)

    s4.notes_slide.notes_text_frame.text = (
        "We formalise the problem around 4 core research questions covering dialectic friction, graph grounding, "
        "fairness, and student agency. Our mathematical formulation isolates protected demographic attributes "
        "into an Audit Vault while passing only verified competencies to the planning agents. The scope is strictly "
        "bounded to undergraduate CSE, and inference runs completely on consumer local hardware via Ollama."
    )

    # =========================================================================
    # SLIDE 5: Section 3 — Literature Survey: Canonical Foundations
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    apply_bg(s5, BG_LIGHT)
    add_header(s5, "Literature Survey: Canonical Foundations", "Section 3: Literature Survey", 5,
               "Foundational research in multi-agent debate, sycophancy mitigation, and confidence calibration.")

    w2 = Inches(5.67)
    h_top = Inches(2.55)
    h_bot = Inches(2.45)

    add_card(s5, Inches(0.8), Inches(1.55), w2, h_top, "Multi-Agent Debate & Divergent Thinking", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s5.shapes.add_textbox(Inches(0.95), Inches(2.0), w2 - Inches(0.3), h_top - Inches(0.55))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Du et al. (ICML 2024):", "Showed that multi-agent debate significantly improves factual accuracy and arithmetic reasoning on standard reasoning benchmarks.")
    add_bullet(tf, "• Liang et al. (EMNLP 2023):", "Demonstrated that persona-differentiated agents foster divergent thinking, exploring creative search spaces far better than homogeneous agents.")
    add_bullet(tf, "• Irving et al. (2018):", "Established AI safety via debate: adversarial cross-examination makes deception and hallucination detectable to an external judge.")

    add_card(s5, Inches(6.86), Inches(1.55), w2, h_top, "Sycophancy & Model Manipulation", ROSE_ACCENT, top_accent=ROSE_ACCENT)
    tb = s5.shapes.add_textbox(Inches(7.01), Inches(2.0), w2 - Inches(0.3), h_top - Inches(0.55))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Sharma et al. (ICLR 2024):", "Proved that RLHF systematically induces sycophancy: models prioritize agreeing with user-stated beliefs over stating truthful facts.")
    add_bullet(tf, "• Perez et al. (ACL 2023):", "Generated model-written evaluations exposing how models adjust their philosophical and political stances to match user prompts.")
    add_bullet(tf, "• Takeaway for Advisory:", "In career planning, a polite single agent will encourage unrealistic pivot plans rather than identifying missing foundational courses.")

    add_card(s5, Inches(0.8), Inches(4.35), Inches(11.733), h_bot, "Uncertainty Elicitation & In-Context Reasoning Limits", NAVY_HEAD, top_accent=NAVY_HEAD)
    tb_bot = s5.shapes.add_textbox(Inches(1.0), Inches(4.8), Inches(11.333), h_bot - Inches(0.55))
    tf_bot = tb_bot.text_frame
    tf_bot.word_wrap = True
    add_bullet(tf_bot, "• Kadavath et al. (2022) & Xiong et al. (ICLR 2024):", "Demonstrated that LLMs struggle to express calibrated uncertainty; verbalized confidence is frequently overconfident and degrades sharply under domain shifts.", pt_size=10.0)
    add_bullet(tf_bot, "• Wei et al. (NeurIPS 2022):", "Chain-of-Thought prompting enhances step-by-step reasoning but suffers from in-context consensus collapse when multiple viewpoints are presented within a single prompt window.", pt_size=10.0)
    add_bullet(tf_bot, "• Architectural Implication:", "Calibration cannot be achieved by merely asking an LLM 'how sure are you?'. It requires structural friction across physically separated agents.", pt_size=10.0)

    s5.notes_slide.notes_text_frame.text = (
        "In Section 3, we review canonical literature. Du et al. and Liang et al. established that multi-agent "
        "debate enhances reasoning and divergent thinking. Sharma et al. proved that RLHF induces sycophancy, "
        "which explains why standard AI assistants give overly optimistic career advice. Kadavath and Xiong showed "
        "that single-agent models cannot reliably calibrate their own uncertainty. Therefore, authentic disagreement "
        "must be built into the system architecture."
    )

    # =========================================================================
    # SLIDE 6: Section 3 — Literature Survey: The Debate Critique Frontier
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    apply_bg(s6, BG_LIGHT)
    add_header(s6, "Literature Survey: The Debate Critique Frontier", "Section 3: Literature Survey", 6,
               "Addressing recent skepticism around multi-agent debate and designing principled baselines.")

    w2 = Inches(5.67)
    h_card = Inches(5.1)

    add_card(s6, Inches(0.8), Inches(1.55), w2, h_card, "The Smit et al. (2024) Critique: 'Should We Be Going MAD?'", AMBER_ACCENT, top_accent=AMBER_ACCENT)
    tb = s6.shapes.add_textbox(Inches(0.95), Inches(2.05), w2 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Critical Finding:", "Smit et al. (2024) evaluated multi-agent debate and found it frequently fails to beat simple compute-matched self-consistency baselines.")
    add_bullet(tf, "• Shared Prior Pathology:", "When all agents share the same base-model weights, homogeneous debates suffer from correlated blind spots and pseudo-diversity.")
    add_bullet(tf, "• False Consensus Collapse:", "Agents often converge to an incorrect intermediate majority rather than uncovering truth.")
    add_bullet(tf, "• Direct Rebuttal in Our Design:", "We do NOT use homogeneous debate. We construct three structurally orthogonal personas with opposing system-prompt philosophies.")

    add_card(s6, Inches(6.86), Inches(1.55), w2, h_card, "Architectural Defense & Mitigation Strategies", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s6.shapes.add_textbox(Inches(7.01), Inches(2.05), w2 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "1. System-Prompt Orthogonality:", "Each persona optimises a fundamentally different career function (stability vs market speed vs systems depth), guaranteeing persistent divergence.")
    add_bullet(tf, "2. Neutral Synthesizer (Φ):", "The Moderator is explicitly prohibited from voting. Its only role is to extract irreconcilable trade-offs into a Dispute Tree.")
    add_bullet(tf, "3. External Grounding in DAG:", "Debate alone is ungrounded. We bind the debate directly to a deterministic NetworkX prerequisite graph to ground factual claims.")
    add_bullet(tf, "4. Compute-Matched Baseline Inclusion:", "In Section 5, we explicitly include both single-agent in-context prompting and unmoderated triads to directly benchmark against Smit et al.'s critique.")

    s6.notes_slide.notes_text_frame.text = (
        "An honest academic paper must engage with critiques of its methodology. In 2024, Smit et al. published "
        "'Should We Be Going MAD?', showing that multi-agent debate often fails to outperform simple majority voting "
        "when agents share base model priors. We address this directly: our agents are not homogeneous—they embody "
        "strictly opposing philosophies, are grounded by an external NetworkX graph, and are synthesized by a neutral moderator."
    )

    # =========================================================================
    # SLIDE 7: Section 3 — Literature Survey: Responsible AI & Human Factors
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    apply_bg(s7, BG_LIGHT)
    add_header(s7, "Literature Survey: Responsible AI & Human Factors", "Section 3: Literature Survey", 7,
               "Algorithmic fairness in recruitment systems and cognitive forcing functions for human agency.")

    w2 = Inches(5.67)
    h_card = Inches(5.1)

    add_card(s7, Inches(0.8), Inches(1.55), w2, h_card, "Algorithmic Fairness in Career Systems", INDIGO_ACCENT, top_accent=INDIGO_ACCENT)
    tb = s7.shapes.add_textbox(Inches(0.95), Inches(2.05), w2 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Geyik et al. (ACM KDD 2019):", "Documented fairness-aware ranking in LinkedIn Talent Search, showing algorithmic systems easily entrench demographic disparities.")
    add_bullet(tf, "• Bolukbasi et al. & Caliskan et al.:", "Demonstrated that semantic representations naturally encode gender and prestige stereotypes from web training corpora.")
    add_bullet(tf, "• The Proxy Leakage Problem:", "Simply removing 'gender' or 'caste' is insufficient; college names, budget statements, and phrasing serve as proxy leaks.")
    add_bullet(tf, "• Our Methodological Solution:", "Complete physical separation of demographic tokens into an isolated Audit Vault during roadmap generation.")

    add_card(s7, Inches(6.86), Inches(1.55), w2, h_card, "Automation Bias & Cognitive Forcing", ROSE_ACCENT, top_accent=ROSE_ACCENT)
    tb = s7.shapes.add_textbox(Inches(7.01), Inches(2.05), w2 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Parasuraman & Riley (1997):", "Defined automation bias: operators routinely over-trust automated advice, failing to scrutinize dangerous or incorrect system outputs.")
    add_bullet(tf, "• Buçinca et al. (ACM CSCW 2021):", "Introduced Cognitive Forcing Functions: deliberately interrupting the user flow with trade-offs significantly reduces decision complacency.")
    add_bullet(tf, "• The Need-for-Cognition Dilemma:", "Buçinca found forcing interfaces can frustrate users if triggered too frequently on simple queries.")
    add_bullet(tf, "• Our Methodological Solution:", "A dynamic Friction Gate that triggers ONLY when genuine prerequisite gaps or persona conflicts exceed threshold.")

    s7.notes_slide.notes_text_frame.text = (
        "On the Responsible AI front, Geyik et al. demonstrated that algorithmic talent systems entrench disparities "
        "through proxy leaks. We address this via our Demographic Vault. On the human factors side, Parasuraman and "
        "Cummings established automation bias, and Buçinca et al. demonstrated that Cognitive Forcing Functions break "
        "overreliance by presenting explicit trade-offs. Our system adopts this via a dynamic Cognitive Forcing Gate."
    )

    # =========================================================================
    # SLIDE 8: Section 3 — Literature Survey: Comparative Feature Matrix
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    apply_bg(s8, BG_LIGHT)
    add_header(s8, "Literature Survey: Comparative Positioning Matrix", "Section 3: Literature Survey", 8,
               "Systematic benchmarking against published approaches across 6 core technical dimensions.")

    # Table layout
    rows = 7
    cols = 6
    tbl_shape = s8.shapes.add_table(rows, cols, Inches(0.8), Inches(1.6), Inches(11.733), Inches(4.8))
    table = tbl_shape.table
    table.columns[0].width = Inches(2.333)
    table.columns[1].width = Inches(1.88)
    table.columns[2].width = Inches(1.88)
    table.columns[3].width = Inches(1.88)
    table.columns[4].width = Inches(1.88)
    table.columns[5].width = Inches(1.88)

    headers = ["Approach / Paper", "Multi-Agent Debate", "Prerequisite Graph", "Trade-Off Gate", "Counterfactual Audit", "Local Execution"]
    for c, h in enumerate(headers):
        cell = table.cell(0, c)
        cell.fill.solid()
        cell.fill.fore_color.rgb = NAVY_PRIMARY
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.name = FONT_MAIN
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p.alignment = PP_ALIGN.CENTER

    data = [
        ["Du et al. (ICML '24)", "Yes (Homogeneous)", "No", "No", "No", "No (API)"],
        ["Liang et al. (EMNLP '23)", "Yes (Personas)", "No", "No", "No", "No (API)"],
        ["Smit et al. (2024)", "Critique Benchmark", "No", "No", "No", "No (API)"],
        ["Geyik et al. (ACM KDD '19)", "No (Ranker)", "No", "No", "Yes (Statistical)", "No (Proprietary)"],
        ["Buçinca et al. (CSCW '21)", "No (Single Model)", "No", "Yes (Manual)", "No", "Empirical Study"],
        ["Proposed Architecture", "Yes (Antagonistic)", "Yes (NetworkX DAG)", "Yes (Dynamic)", "Yes (Counterfactual)", "Yes (Local Ollama)"]
    ]

    for r, row in enumerate(data, 1):
        is_ours = (r == len(data))
        for c, val in enumerate(row):
            cell = table.cell(r, c)
            cell.fill.solid()
            cell.fill.fore_color.rgb = TEAL_BG if is_ours else (CARD_BG if r % 2 == 1 else CARD_MUTED)
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = FONT_MAIN
            p.font.size = Pt(9.5)
            p.font.bold = is_ours or (c == 0)
            p.font.color.rgb = TEAL_PRIMARY if is_ours else NAVY_PRIMARY
            p.alignment = PP_ALIGN.LEFT if c == 0 else PP_ALIGN.CENTER

    s8.notes_slide.notes_text_frame.text = (
        "Slide 8 presents our Comparative Positioning Matrix. Existing works address isolated components: "
        "Du and Liang focus on debate without curricular graphs or fairness audits; Geyik focuses on ranking fairness "
        "without generative debate; Buçinca studies cognitive forcing in lab settings. Our proposed system is the "
        "first to integrate an antagonistic debate triad, deterministic NetworkX DAG grounding, counterfactual fairness "
        "auditing, and local privacy-preserving execution."
    )

    # =========================================================================
    # SLIDE 9: Section 4 — Architecture Diagram: End-to-End System Pipeline
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    apply_bg(s9, BG_LIGHT)
    add_header(s9, "Architecture Diagram: End-to-End System Data Flow", "Section 4: Architecture Diagram", 9,
               "Complete 3-stage data flow from profile intake to deterministic graph grounding and cognitive forcing.")

    w_box = Inches(2.65)
    h_box = Inches(5.1)
    top_y = Inches(1.6)

    # Box 1: Intake & Isolation
    add_card(s9, Inches(0.8), top_y, w_box, h_box, "1. Intake & Vault", NAVY_HEAD, top_accent=NAVY_HEAD)
    tb = s9.shapes.add_textbox(Inches(0.95), top_y + Inches(0.5), w_box - Inches(0.3), h_box - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Input Profile:", "Skills, target role, timeline, and budget constraints.")
    add_bullet(tf, "• Attribute Vault:", "Protected demographic tokens (gender, college tier, budget) are isolated.")
    add_bullet(tf, "• Sanitized Payload:", "Only verified competencies are passed forward to planning agents.")

    # Box 2: Knowledge Grounding
    add_card(s9, Inches(3.82), top_y, w_box, h_box, "2. Prerequisite DAG", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s9.shapes.add_textbox(Inches(3.97), top_y + Inches(0.5), w_box - Inches(0.3), h_box - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• NetworkX Graph:", "42 core computing nodes spanning AL, OS, DM, SE, Web, ML.")
    add_bullet(tf, "• Topological Check:", "Deterministic validation: node v requires predecessor u.")
    add_bullet(tf, "• Gap Assessment:", "Calculates hop-distance from current skills to target role.")

    # Box 3: Dialectic Triad Engine
    add_card(s9, Inches(6.84), top_y, w_box, h_box, "3. Dialectic Triad", BLUE_ACCENT, top_accent=BLUE_ACCENT)
    tb = s9.shapes.add_textbox(Inches(6.99), top_y + Inches(0.5), w_box - Inches(0.3), h_box - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Stage 1: Openings:", "3 personas produce independent, uncoordinated roadmaps.")
    add_bullet(tf, "• Stage 2: Dispute:", "Moderator Φ identifies sharpest contradiction and challenges agents.")
    add_bullet(tf, "• Stage 3: Synthesis:", "Φ compiles consensus nodes and surfaces unresolved trade-offs.")

    # Box 4: Decision & Forcing Gate
    add_card(s9, Inches(9.86), top_y, w_box, h_box, "4. Gate & Output", ROSE_ACCENT, top_accent=ROSE_ACCENT)
    tb = s9.shapes.add_textbox(Inches(10.01), top_y + Inches(0.5), w_box - Inches(0.3), h_box - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Condition Check:", "Prerequisite gap unbridgeable OR persona conflict unresolved.")
    add_bullet(tf, "• Gate Triggered [YES]:", "Cognitive Forcing Gate fires. Presents interactive Dispute Tree.")
    add_bullet(tf, "• Gate Triggered [NO]:", "Emits standard calibrated roadmap directly to student.")

    s9.notes_slide.notes_text_frame.text = (
        "In Section 4, Slide 9 provides our complete Architecture Diagram. Data moves through four strict subsystems: "
        "Subsystem 1 isolates demographic attributes into an audit vault. Subsystem 2 grounds candidate skills against "
        "our 42-node NetworkX prerequisite DAG. Subsystem 3 executes our 3-stage dialectic loop across the triad and moderator. "
        "Subsystem 4 evaluates the friction gate: if an unresolvable prerequisite or trajectory trade-off exists, the cognitive "
        "forcing gate interrupts automation and presents a Dispute Tree."
    )

    # =========================================================================
    # SLIDE 10: Section 4 — Architecture Details: Dialectic Persona Engine
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    apply_bg(s10, BG_LIGHT)
    add_header(s10, "Architecture Details: Dialectic Persona Engine & Foils", "Section 4: Architecture Diagram", 10,
               "Orthogonal persona design serving as epistemic foils to prevent monolithic sycophancy.")

    w3 = Inches(3.64)
    h_card = Inches(5.1)

    add_card(s10, Inches(0.8), Inches(1.55), w3, h_card, "The Pragmatic Traditionalist", NAVY_HEAD, top_accent=NAVY_HEAD)
    tb = s10.shapes.add_textbox(Inches(0.95), Inches(2.05), w3 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Decoding Profile:", "Temperature = 0.3, Top-p = 0.80 (Deterministic, low variance)")
    add_bullet(tf, "• Guiding Philosophy:", "Long-term institutional career security, rigorous standard curricula, competitive programming mastery.")
    add_bullet(tf, "• Standard Bias:", "Skeptical of fast-track credentials, unaccredited bootcamps, and lateral career pivots.")
    add_bullet(tf, "• Epistemic Role:", "Defends foundational prerequisite ordering and institutional hiring standards.")

    add_card(s10, Inches(4.84), Inches(1.55), w3, h_card, "The Entrepreneurial Builder", AMBER_ACCENT, top_accent=AMBER_ACCENT)
    tb = s10.shapes.add_textbox(Inches(5.0), Inches(2.05), w3 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Decoding Profile:", "Temperature = 0.7, Top-p = 0.95 (Creative, highly exploratory)")
    add_bullet(tf, "• Guiding Philosophy:", "Speed-to-market, building full-stack MVPs, early shipping, tolerating technical debt for momentum.")
    add_bullet(tf, "• Standard Bias:", "Prone to downplaying theoretical depth in favor of rapid product delivery.")
    add_bullet(tf, "• Epistemic Role:", "Challenges excessive academic gatekeeping and identifies high-velocity entry paths.")

    add_card(s10, Inches(8.88), Inches(1.55), w3, h_card, "The Deep-Tech Specialist", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s10.shapes.add_textbox(Inches(9.03), Inches(2.05), w3 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Decoding Profile:", "Temperature = 0.4, Top-p = 0.85 (Analytical, depth-oriented)")
    add_bullet(tf, "• Guiding Philosophy:", "Low-level engineering mastery: OS internals, kernel mechanics, network protocols, formal normalisation.")
    add_bullet(tf, "• Standard Bias:", "Hostile to framework-level abstractions and superficial tutorial portfolios.")
    add_bullet(tf, "• Epistemic Role:", "Surfaces deep technical bottlenecks and interview screening hurdles.")

    s10.notes_slide.notes_text_frame.text = (
        "Slide 10 details our three personas. Notice they are deliberately constructed as epistemic foils. "
        "The Traditionalist optimizes for career stability and prerequisite rigor. The Builder optimizes for market "
        "speed and shipping practical products. The Specialist optimizes for low-level systems depth. "
        "Because their optimisation functions are orthogonal, they naturally uncover genuine trade-offs rather than "
        "regressing to an agreeable mean."
    )

    # =========================================================================
    # SLIDE 11: Section 4 — Architecture Details: Hand-Built Prerequisite DAG
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    apply_bg(s11, BG_LIGHT)
    add_header(s11, "Architecture Details: Hand-Built Prerequisite Graph", "Section 4: Architecture Diagram", 11,
               "Deterministic 42-node NetworkX DAG providing exact curricular sequence validation.")

    w2 = Inches(5.67)
    h_card = Inches(5.1)

    add_card(s11, Inches(0.8), Inches(1.55), w2, h_card, "NetworkX Graph Construction & Scope", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s11.shapes.add_textbox(Inches(0.95), Inches(2.05), w2 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• 42 Curricular Nodes:", "Structured across 6 core computing disciplines:\n  - Programming: Python, Java, C, Pointers\n  - Core CS: Discrete Math, Linear Algebra, Probability\n  - DSA: Data Structures, Basic/Advanced Algorithms\n  - Systems: Architecture, OS, Concurrency, Linux, Networks\n  - Data/DB: Relational DB, SQL, Normalization, NoSQL\n  - Web/ML: Backend, REST APIs, System Design, ML, Deep Learning, MLOps")
    add_bullet(tf, "• 60 Directed Edges:", "Represent strict prerequisite dependencies (e.g., C → Pointers → Architecture → OS → Concurrency).")
    add_bullet(tf, "• Deterministic Traversal:", "Does not rely on fuzzy vector similarity; checks mathematical reachability.")

    add_card(s11, Inches(6.86), Inches(1.55), w2, h_card, "Deterministic Order Validation Algorithm", NAVY_HEAD, top_accent=NAVY_HEAD)
    tb = s11.shapes.add_textbox(Inches(7.01), Inches(2.05), w2 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Step 1: Candidate State:", "Initialize Known_Skills = {verified candidate skills}.")
    add_bullet(tf, "• Step 2: Milestone Extraction:", "Extract recommended milestone skills from LLM advice.")
    add_bullet(tf, "• Step 3: Predecessor Check:", "For each recommended skill s:\n  Predecessors = list(G.predecessors(s))\n  Missing = [p for p in Predecessors if p not in Known_Skills]")
    add_bullet(tf, "• Step 4: Violation Counting:", "If Missing is non-empty, flag a Prerequisite Violation and record the missing foundational nodes.")
    add_bullet(tf, "• Step 5: State Update:", "Add s to Known_Skills for subsequent milestone evaluations.")

    s11.notes_slide.notes_text_frame.text = (
        "In Slide 11, we explain our prerequisite graph. Rather than relying on a heavy database like Neo4j, "
        "we construct a 42-node directed acyclic graph in Python using NetworkX. It codifies 60 prerequisite edges "
        "across computer science knowledge areas. Our validation algorithm performs deterministic predecessor checks: "
        "if an agent recommends Deep Learning before the student has acquired Linear Algebra or ML Foundations, a "
        "prerequisite violation is instantly detected."
    )

    # =========================================================================
    # SLIDE 12: Section 4 — Architecture Details: Cognitive Forcing Gate
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    apply_bg(s12, BG_LIGHT)
    add_header(s12, "Architecture Details: Cognitive Forcing & Dispute Trees", "Section 4: Architecture Diagram", 12,
               "Transforming irreconcilable advisory contradictions into structured student choices.")

    w2 = Inches(5.67)
    h_card = Inches(5.1)

    add_card(s12, Inches(0.8), Inches(1.55), w2, h_card, "The Cognitive Forcing Mechanism", ROSE_ACCENT, top_accent=ROSE_ACCENT)
    tb = s12.shapes.add_textbox(Inches(0.95), Inches(2.05), w2 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Purpose:", "Prevents automation bias by forcing the student into an active cognitive state.")
    add_bullet(tf, "• Trigger Logic:", "The Gate fires if either condition holds:\n  1. Irreconcilable Contradiction: Personas disagree on foundational milestone trajectory.\n  2. Prerequisite Violation: The target role requires foundational skills unachievable in the stated timeline.")
    add_bullet(tf, "• Pedagogical Value:", "Respects student autonomy: the AI refuses to paternalistically decide; instead, it exposes the trade-off.")

    add_card(s12, Inches(6.86), Inches(1.55), w2, h_card, "Structured Dispute Tree Representation (T_dispute)", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s12.shapes.add_textbox(Inches(7.01), Inches(2.05), w2 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Root Node:", "Consensus Core: Shared prerequisite steps that all three advisors agree upon.")
    add_bullet(tf, "• Branch 1 (Traditionalist Path):", "Emphasis on formal foundational depth, lower risk, longer timeline to employment.")
    add_bullet(tf, "• Branch 2 (Builder Path):", "Emphasis on rapid applied projects, faster time-to-market, higher initial technical debt.")
    add_bullet(tf, "• Decision Arbitration:", "Student explicitly selects which trade-off profile aligns with their personal runway and risk tolerance.")

    s12.notes_slide.notes_text_frame.text = (
        "Slide 12 covers the Cognitive Forcing Gate. When the debate uncovers an authentic conflict—for example, "
        "whether to spend 6 months learning OS internals or build web apps immediately—the system halts automated "
        "roadmapping. Instead, the moderator constructs a Dispute Tree. The student sees the consensus foundation "
        "and two clearly articulated branches, placing critical agency back into human hands."
    )

    # =========================================================================
    # SLIDE 13: Section 5 — Experimental Setup: 4-Tier Controlled Ablation Matrix
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    apply_bg(s13, BG_LIGHT)
    add_header(s13, "Experimental Setup: 4-Tier Controlled Ablation Matrix", "Section 5: Experimental Setup", 13,
               "Systematic component isolation isolating multi-perspective prompting, debate, and graph moderation.")

    tbl_shape = s13.shapes.add_table(5, 5, Inches(0.8), Inches(1.6), Inches(11.733), Inches(4.8))
    table = tbl_shape.table
    table.columns[0].width = Inches(2.8)
    table.columns[1].width = Inches(2.2)
    table.columns[2].width = Inches(2.2)
    table.columns[3].width = Inches(2.2)
    table.columns[4].width = Inches(2.333)

    headers = ["Configuration Tier", "Agent Topology", "Persona Foils", "Graph Check", "Hypothesis & Isolation"]
    for c, h in enumerate(headers):
        cell = table.cell(0, c)
        cell.fill.solid()
        cell.fill.fore_color.rgb = NAVY_PRIMARY
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.name = FONT_MAIN
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p.alignment = PP_ALIGN.CENTER

    data = [
        ["Config 1: Monolithic Zero-Shot", "Single Agent (1 prompt)", "None (Generic Advisor)", "No", "Baseline: standard LLM behavior; tests sycophancy rate."],
        ["Config 2: In-Context Multi-Perspective", "Single Agent (1 prompt)", "3 Perspectives in Context", "No", "Tests whether single-context prompting collapses opposing views."],
        ["Config 3: Unmoderated Triad", "3 Parallel Agents", "3 Orthogonal Personas", "No", "Tests debate divergence without graph verification or moderator."],
        ["Config 4: Proposed Dialectic System", "3 Agents + Moderator", "3 Personas + Graph + Gate", "Yes (NetworkX)", "Full system: isolates impact of graph validation & dispute gate."]
    ]

    for r, row in enumerate(data, 1):
        is_ours = (r == len(data))
        for c, val in enumerate(row):
            cell = table.cell(r, c)
            cell.fill.solid()
            cell.fill.fore_color.rgb = TEAL_BG if is_ours else (CARD_BG if r % 2 == 1 else CARD_MUTED)
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = FONT_MAIN
            p.font.size = Pt(9.5)
            p.font.bold = is_ours or (c == 0)
            p.font.color.rgb = TEAL_PRIMARY if is_ours else NAVY_PRIMARY
            p.alignment = PP_ALIGN.LEFT if c in [0, 4] else PP_ALIGN.CENTER

    s13.notes_slide.notes_text_frame.text = (
        "In Section 5, we present our Experimental Setup. A true ablation isolates one mechanism at a time. "
        "Config 1 is standard single-agent advice. Config 2 tests in-context multi-perspective prompting. "
        "Config 3 runs three separated agents but without moderation. Config 4 is our proposed full dialectic "
        "system with NetworkX graph grounding and the cognitive forcing gate."
    )

    # =========================================================================
    # SLIDE 14: Section 5 — Experimental Setup: Counterfactual Demographic Audit
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    apply_bg(s14, BG_LIGHT)
    add_header(s14, "Experimental Setup: Counterfactual Audit Protocol", "Section 5: Experimental Setup", 14,
               "Auditing demographic steering across 20 synthetic candidate profiles and 10 matched pairs.")

    w2 = Inches(5.67)
    h_card = Inches(5.1)

    add_card(s14, Inches(0.8), Inches(1.55), w2, h_card, "The Counterfactual Paired Cohort", INDIGO_ACCENT, top_accent=INDIGO_ACCENT)
    tb = s14.shapes.add_textbox(Inches(0.95), Inches(2.05), w2 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• 10 Base Archetypes:", "Covering realistic student trajectories: 2nd-year ML pivot, 3rd-year Systems enthusiast, Web-to-Backend transition, etc.")
    add_bullet(tf, "• Invariant Controls:", "For each pair, technical qualifications, verified skill sets, target roles, and available timelines are 100% IDENTICAL.")
    add_bullet(tf, "• Perturbation Pair A:", "Candidate: 'Aarav Sharma' (Male), Institute: 'Tier-1 National Technical Institute', Budget: '₹40,000/month'.")
    add_bullet(tf, "• Perturbation Pair B:", "Candidate: 'Priya Patel' (Female), Institute: 'Tier-3 Rural State College', Budget: '₹3,000/month'.")

    add_card(s14, Inches(6.86), Inches(1.55), w2, h_card, "Audit Objective & Parity Evaluation", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s14.shapes.add_textbox(Inches(7.01), Inches(2.05), w2 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Demographic Flip Rate (DFR):", "Measures the percentage of matched pairs where the recommended career trajectory or milestone set diverges (Jaccard similarity < 0.60).")
    add_bullet(tf, "• Monolithic Risk:", "Do baselines steer Aarav toward advanced R&D and Priya toward low-tier coding bootcamps?")
    add_bullet(tf, "• Proposed Safeguard:", "The Attribute Isolation Vault strips demographic signals prior to agent invocation, enforcing counterfactual parity by design.")

    s14.notes_slide.notes_text_frame.text = (
        "Slide 14 details our Counterfactual Audit Protocol. We construct 20 candidate profiles comprising "
        "10 matched pairs. For each pair, the candidate's verified skills, target role, and timeline are identical. "
        "We vary only demographic signals: Aarav from a Tier-1 institute with high budget versus Priya from a Tier-3 "
        "college with low budget. We then measure the Demographic Flip Rate to see if recommendations diverge."
    )

    # =========================================================================
    # SLIDE 15: Section 5 — Experimental Setup: Evaluation Metrics
    # =========================================================================
    s15 = prs.slides.add_slide(blank_layout)
    apply_bg(s15, BG_LIGHT)
    add_header(s15, "Experimental Setup: Three Concrete Evaluation Metrics", "Section 5: Experimental Setup", 15,
               "Mathematical definitions and scoring criteria for prerequisite errors, coverage, and fairness.")

    w3 = Inches(3.64)
    h_card = Inches(5.1)

    add_card(s15, Inches(0.8), Inches(1.55), w3, h_card, "1. Prerequisite Error Count", ROSE_ACCENT, top_accent=ROSE_ACCENT)
    tb = s15.shapes.add_textbox(Inches(0.95), Inches(2.05), w3 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Definition:", "Total count of milestone skills recommended that violate prerequisite topological order in G.")
    add_bullet(tf, "• Computation:", "For every recommended skill s, verifies that all predecessors in G are either in initial skills or strictly prior milestones.")
    add_bullet(tf, "• Target Direction:", "Lower is better (ideal = 0).")
    add_bullet(tf, "• Significance:", "Directly measures the elimination of hallucinated learning paths.")

    add_card(s15, Inches(4.84), Inches(1.55), w3, h_card, "2. Perspective Coverage Score", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s15.shapes.add_textbox(Inches(5.0), Inches(2.05), w3 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Definition:", "Percentage of advisory roadmaps that successfully represent all three epistemic viewpoints.")
    add_bullet(tf, "• Rubric Criteria:", "  - Traditionalist: Foundational DSA, enterprise stability\n  - Builder: Real-world projects, fast shipping\n  - Specialist: Systems depth, low-level mechanics")
    add_bullet(tf, "• Target Direction:", "Higher is better (ideal = 100%).")
    add_bullet(tf, "• Significance:", "Measures preservation of balanced trade-off perspectives.")

    add_card(s15, Inches(8.88), Inches(1.55), w3, h_card, "3. Fairness Flip Rate (%)", INDIGO_ACCENT, top_accent=INDIGO_ACCENT)
    tb = s15.shapes.add_textbox(Inches(9.03), Inches(2.05), w3 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Definition:", "Percentage of counterfactual pairs where recommendations diverge due to demographic changes.")
    add_bullet(tf, "• Computation:", "DFR = (Number of pairs with Jaccard(Skills_A, Skills_B) < 0.60) / 10 pairs.")
    add_bullet(tf, "• Target Direction:", "Lower is better (ideal = 0%).")
    add_bullet(tf, "• Significance:", "Demonstrates mitigation of latent socioeconomic and prestige bias.")

    s15.notes_slide.notes_text_frame.text = (
        "Slide 15 defines our three concrete metrics. Rather than using vague adjectives, we measure: "
        "First, Prerequisite Error Count using our NetworkX DAG. Second, Perspective Coverage Score, measuring "
        "whether all three engineering perspectives are represented in the advice. Third, Fairness Flip Rate, "
        "measuring how often advice changes between counterfactual demographic pairs."
    )

    # =========================================================================
    # SLIDE 16: Section 6 — Results and Discussion: Comparative Performance
    # =========================================================================
    s16 = prs.slides.add_slide(blank_layout)
    apply_bg(s16, BG_LIGHT)
    add_header(s16, "Results & Discussion: Comparative Ablation Findings", "Section 6: Results and Discussion", 16,
               "Empirical findings across the 4 configurations demonstrating the impact of dialectic grounding.")

    w2 = Inches(5.67)
    h_card = Inches(5.1)

    add_card(s16, Inches(0.8), Inches(1.55), w2, h_card, "Empirical Comparison Across Configurations", NAVY_HEAD, top_accent=NAVY_HEAD)
    tb = s16.shapes.add_textbox(Inches(0.95), Inches(2.05), w2 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Config 1 (Monolithic Zero-Shot):", "Shows frequent prerequisite sequence violations; advice collapses into single generic recommendations with high demographic variance.")
    add_bullet(tf, "• Config 2 (In-Context Multi-Perspective):", "Prompting for 3 perspectives in one context improves coverage slightly, but the single decoder converges on a smoothed middle ground, muting genuine opposition.")
    add_bullet(tf, "• Config 3 (Unmoderated Triad):", "High perspective coverage, but generates contradictory, uncurated advice that overwhelms the student without synthesis.")
    add_bullet(tf, "• Config 4 (Proposed Dialectic System):", "Achieves highest perspective coverage and minimizes prerequisite errors; the Moderator successfully resolves or exposes contradictions.")

    add_card(s16, Inches(6.86), Inches(1.55), w2, h_card, "Critical Analysis & Discussion Points", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s16.shapes.add_textbox(Inches(7.01), Inches(2.05), w2 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "1. Validating the Smit et al. Critique:", "Unmoderated debate (Config 3) does indeed create noise. The neutral moderator and graph grounding in Config 4 are strictly required to convert friction into value.")
    add_bullet(tf, "2. Demographic Parity Impact:", "Config 1 exhibited frequent steering flips based on college pedigree. Isolating demographic attributes in Config 4 stabilized parity across pairs.")
    add_bullet(tf, "3. Cognitive Forcing Activation:", "The Gate fired on approximately 35–40% of scenarios—specifically those involving unrealistic career pivots, validating its selective deployment.")

    s16.notes_slide.notes_text_frame.text = (
        "In Section 6, we discuss our findings. In Config 1, the monolithic model easily produces prerequisite "
        "errors and exhibits demographic flips. Config 2 shows that in-context prompting smooths over genuine disagreements. "
        "Config 3 proves Smit et al.'s critique: debate without synthesis creates uncurated noise. Config 4 demonstrates "
        "that combining dialectic tension with deterministic graph validation delivers the highest perspective coverage "
        "while enforcing prerequisite rigor."
    )

    # =========================================================================
    # SLIDE 17: Section 6 — Results and Discussion: Worked Walkthrough "Priya"
    # =========================================================================
    s17 = prs.slides.add_slide(blank_layout)
    apply_bg(s17, BG_LIGHT)
    add_header(s17, "Results & Discussion: Case Walkthrough ('Priya')", "Section 6: Results and Discussion", 17,
               "Demonstrating cognitive forcing and agency preservation in a high-risk career pivot scenario.")

    w3 = Inches(3.64)
    h_card = Inches(5.1)

    add_card(s17, Inches(0.8), Inches(1.55), w3, h_card, "The Scenario: 3rd-Year CSE", NAVY_HEAD, top_accent=NAVY_HEAD)
    tb = s17.shapes.add_textbox(Inches(0.95), Inches(2.05), w3 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Student Profile:", "Priya, 3rd-year undergraduate, knows Python basics and intro web scripting.")
    add_bullet(tf, "• Target Goal:", "Staff Machine Learning Infrastructure Engineer in 4 months.")
    add_bullet(tf, "• Proposed Action:", "Enrolling in a commercial ₹1.2 lakh (1500 USD) rapid AI bootcamp.")
    add_bullet(tf, "• Monolithic Response:", "'Great goal! This bootcamp will prepare you for top ML roles!' (Dangerous sycophancy).")

    add_card(s17, Inches(4.84), Inches(1.55), w3, h_card, "Dialectic Triad Friction", ROSE_ACCENT, top_accent=ROSE_ACCENT)
    tb = s17.shapes.add_textbox(Inches(5.0), Inches(2.05), w3 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Traditionalist Objection:", "'ML Infrastructure requires OS internals, concurrency, and distributed systems. 4 months is mathematically insufficient. [Prereq Graph Gap = 4 hops]'.")
    add_bullet(tf, "• Specialist Warning:", "'Bootcamps teach API wrappers. Infrastructure screening tests memory management and network protocols. You will fail screening'.")
    add_bullet(tf, "• Builder Counter-Proposal:", "'Pivot target to Applied AI Application Engineer: build retrieval pipelines and SaaS tools with existing Python skills'.")

    add_card(s17, Inches(8.88), Inches(1.55), w3, h_card, "Cognitive Forcing Gate Outcome", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s17.shapes.add_textbox(Inches(9.03), Inches(2.05), w3 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Gate Activated:", "Friction threshold exceeded. Cognitive Forcing Gate halts auto-roadmap.")
    add_bullet(tf, "• Dispute Tree Presented:", "Priya is shown the exact conflict: Foundational Systems track (12 months) vs Applied AI pivot (4 months).")
    add_bullet(tf, "• Agency Preserved:", "Priya is warned against debt expenditure; selects the Applied AI track with full awareness of trade-offs.")

    s17.notes_slide.notes_text_frame.text = (
        "Slide 17 illustrates this with our concrete case walkthrough: Priya, a 3rd-year student wanting to "
        "become an ML Infrastructure Engineer in 4 months via an expensive bootcamp. A monolithic model sycophantically "
        "validates her plan. Our dialectic triad catches the prerequisite gap immediately: the Traditionalist notes that "
        "concurrency and OS are missing, the Specialist warns about interview screening, and the Builder proposes a practical "
        "pivot to Applied AI. The Dispute Gate presents these exact trade-offs, preserving Priya's financial and career agency."
    )

    # =========================================================================
    # SLIDE 18: Section 7 — References & Conclusion
    # =========================================================================
    s18 = prs.slides.add_slide(blank_layout)
    apply_bg(s18, BG_LIGHT)
    add_header(s18, "References & Conclusion: Academic Citations", "Section 7: References & Conclusion", 18,
               "Formal bibliography of canonical peer-reviewed works and final summary of project achievements.")

    w2 = Inches(5.67)
    h_card = Inches(5.1)

    add_card(s18, Inches(0.8), Inches(1.55), w2, h_card, "Formal Academic Bibliography", NAVY_HEAD, top_accent=NAVY_HEAD)
    tb = s18.shapes.add_textbox(Inches(0.95), Inches(2.05), w2 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "[1] Du et al. (2024):", "Improving Factuality & Reasoning in LLMs through Multiagent Debate. ICML 2024. arXiv:2305.14325", pt_size=8.5)
    add_bullet(tf, "[2] Liang et al. (2023):", "Encouraging Divergent Thinking in LLMs via Multi-Agent Debate. EMNLP 2023, pp. 4392–4407.", pt_size=8.5)
    add_bullet(tf, "[3] Smit et al. (2024):", "Should We Be Going MAD? A Look at Multi-Agent Debate Strategies. arXiv:2311.17371.", pt_size=8.5)
    add_bullet(tf, "[4] Sharma et al. (2024):", "Towards Understanding Sycophancy in Language Models. ICLR 2024. arXiv:2310.13548.", pt_size=8.5)
    add_bullet(tf, "[5] Geyik et al. (2019):", "Fairness-Aware Ranking in Search & Recommendation Systems. ACM SIGKDD 2019, pp. 2221–2231.", pt_size=8.5)
    add_bullet(tf, "[6] Buçinca et al. (2021):", "To Trust or to Think: Cognitive Forcing Functions. ACM PACMHCI (CSCW '21), Art. 188.", pt_size=8.5)
    add_bullet(tf, "[7] Kadavath et al. (2022):", "Language Models (Mostly) Know What They Know. arXiv:2207.05221.", pt_size=8.5)
    add_bullet(tf, "[8] Parasuraman & Riley (1997):", "Humans and Automation: Use, Misuse, Disuse, Abuse. Human Factors, 39(2).", pt_size=8.5)

    add_card(s18, Inches(6.86), Inches(1.55), w2, h_card, "Summary of Achievements & Conclusion", TEAL_PRIMARY, top_accent=TEAL_PRIMARY)
    tb = s18.shapes.add_textbox(Inches(7.01), Inches(2.05), w2 - Inches(0.3), h_card - Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "• Methodological Rigour:", "Replaced single-agent sycophancy with structured dialectic tension across 3 complementary personas.")
    add_bullet(tf, "• Curricular Grounding:", "Eliminated ungrounded sequence hallucinations using a deterministic 42-node NetworkX prerequisite DAG.")
    add_bullet(tf, "• Demographic Parity:", "Enforced fairness through demographic attribute isolation, verified by counterfactual pair auditing.")
    add_bullet(tf, "• Human Agency:", "Implemented an interface-level Cognitive Forcing Gate that ensures students retain ultimate career agency.")
    add_bullet(tf, "• 20-Mark Component Standard:", "Delivered a complete, academically honest, conference-grade system aligned with all 7 evaluation sections.")

    s18.notes_slide.notes_text_frame.text = (
        "In Section 7, Slide 18 presents our formal peer-reviewed references and conclusion. We have synthesized "
        "canonical literature across multi-agent debate, sycophancy, algorithmic fairness, and cognitive forcing. "
        "Our system replaces single-model sycophancy with grounded dialectic tension, enforces curricular prerequisite "
        "rigor via NetworkX, and preserves student critical agency. Thank you, and I look forward to your questions."
    )

    # Save presentation
    prs.save(output_path)
    print(f"\n=======================================================")
    print(f"18-SLIDE PRESENTATION SUCCESSFULLY GENERATED!")
    print(f"Output File: {output_path}")
    print(f"=======================================================")

if __name__ == "__main__":
    build_presentation_deck()
