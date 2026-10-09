#!/usr/bin/env python3
"""
Generate a professional 16:9 PowerPoint presentation for:
Debate-Based Career Guidance Agent with Complementary Personas
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]  # completely blank

    # Color Palette: Modern Academic & Technical (Navy, Slate, Teal, White)
    BG_DARK = RGBColor(15, 23, 42)       # Slate 900
    BG_LIGHT = RGBColor(248, 250, 252)   # Slate 50
    CARD_BG = RGBColor(255, 255, 255)    # Pure White
    CARD_BORDER = RGBColor(226, 232, 240)# Slate 200
    NAVY_PRIMARY = RGBColor(30, 41, 59)  # Slate 800
    TEAL_ACCENT = RGBColor(13, 148, 136) # Teal 600
    TEAL_LIGHT = RGBColor(204, 251, 241) # Teal 100
    AMBER_ACCENT = RGBColor(217, 119, 6) # Amber 600
    ROSE_ACCENT = RGBColor(225, 29, 72)  # Rose 600
    TEXT_MAIN = RGBColor(15, 23, 42)     # Slate 900
    TEXT_MUTED = RGBColor(100, 116, 139) # Slate 500
    TEXT_LIGHT = RGBColor(241, 245, 249) # Slate 100

    def add_header(slide, title_text, category_text="RESPONSIBLE AI & MULTI-AGENT SYSTEMS"):
        # Category badge/kicker
        tb_cat = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.4))
        p_cat = tb_cat.text_frame.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = TEAL_ACCENT

        # Main Title
        tb_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.7), Inches(0.8))
        p_title = tb_title.text_frame.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(24)
        p_title.font.bold = True
        p_title.font.color.rgb = NAVY_PRIMARY

        # Thin divider line
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.5), Inches(11.733), Inches(0.02))
        line.fill.solid()
        line.fill.fore_color.rgb = CARD_BORDER
        line.line.color.rgb = CARD_BORDER

    def add_card(slide, left, top, width, height, title="", title_color=NAVY_PRIMARY, border_color=CARD_BORDER, bg_color=CARD_BG):
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = bg_color
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1.2)
        
        if title:
            tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.2), width - Inches(0.4), Inches(0.5))
            p = tb.text_frame.paragraphs[0]
            p.text = title
            p.font.size = Pt(15)
            p.font.bold = True
            p.font.color.rgb = title_color
            return tb
        return shape

    # =========================================================================
    # SLIDE 1: Title Slide (Dark Theme)
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = BG_DARK
    bg1.line.fill.background()

    # Kicker
    kicker_box = slide1.shapes.add_textbox(Inches(1.0), Inches(1.2), Inches(11.3), Inches(0.5))
    kp = kicker_box.text_frame.paragraphs[0]
    kp.text = "RESPONSIBLE AI · MULTI-AGENT DELIBERATION · KNOWLEDGE GRAPHS"
    kp.font.size = Pt(13)
    kp.font.bold = True
    kp.font.color.rgb = TEAL_ACCENT

    # Main Title
    title_box = slide1.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.3), Inches(2.2))
    tp = title_box.text_frame.paragraphs[0]
    tp.text = "Debate-Based Career Guidance Agent\nwith Complementary Personas"
    tp.font.size = Pt(36)
    tp.font.bold = True
    tp.font.color.rgb = TEXT_LIGHT

    # Subtitle
    sub_box = slide1.shapes.add_textbox(Inches(1.0), Inches(4.2), Inches(11.3), Inches(1.2))
    sp = sub_box.text_frame.paragraphs[0]
    sp.text = "Mitigating Sycophancy, Ensuring Fairness, and Calibrating Epistemic Uncertainty via Dialectic Deliberation (Planner, Critic, Ethics-Reviewer)"
    sp.font.size = Pt(16)
    sp.font.color.rgb = RGBColor(148, 163, 184) # Slate 400

    # Tech Stack Footer
    footer_box = slide1.shapes.add_textbox(Inches(1.0), Inches(5.8), Inches(11.3), Inches(0.8))
    fp = footer_box.text_frame.paragraphs[0]
    fp.text = "Tech Stack: Qwen Local (Ollama/vLLM) · LangGraph Python Multi-Agent · Neo4j Career Graph · Chroma/FAISS · Streamlit"
    fp.font.size = Pt(13)
    fp.font.bold = True
    fp.font.color.rgb = RGBColor(226, 232, 240)

    # =========================================================================
    # SLIDE 2: Problem & Motivation (The Sycophancy-Viability Trap)
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    add_header(slide2, "The Problem: Why Single-Agent LLMs Fail in Career Guidance", "MOTIVATION & SYSTEMIC PITFALLS")

    # 3 Column Cards
    col_w = Inches(3.64)
    h = Inches(4.8)
    top_pos = Inches(1.8)

    # Card 1: Sycophancy
    add_card(slide2, Inches(0.8), top_pos, col_w, h, "1. The Sycophancy Trap", ROSE_ACCENT)
    tb1 = slide2.shapes.add_textbox(Inches(0.95), top_pos + Inches(0.8), col_w - Inches(0.3), h - Inches(1.0))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    tf1.paragraphs[0].text = "• LLMs naturally agree with user preconceptions (Sharma et al., 2023)."
    tf1.paragraphs[0].font.size = Pt(13)
    tf1.paragraphs[0].font.color.rgb = TEXT_MAIN
    p = tf1.add_paragraph()
    p.text = "\n• Validates unrealistic pivots (e.g. novice to Senior ML Engineer in 3 months) to maximize conversational pleasantness."
    p.font.size = Pt(13)
    p = tf1.add_paragraph()
    p.text = "\n• Results in catastrophic credential debt and abandoned transitions."
    p.font.size = Pt(13)

    # Card 2: False Certainty
    add_card(slide2, Inches(4.84), top_pos, col_w, h, "2. Illusion of Certainty", AMBER_ACCENT)
    tb2 = slide2.shapes.add_textbox(Inches(4.99), top_pos + Inches(0.8), col_w - Inches(0.3), h - Inches(1.0))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    tf2.paragraphs[0].text = "• Emits authoritative, single-path roadmaps without epistemic humility."
    tf2.paragraphs[0].font.size = Pt(13)
    tf2.paragraphs[0].font.color.rgb = TEXT_MAIN
    p = tf2.add_paragraph()
    p.text = "\n• Masks severe market volatility, skill deprecation rates, and course completion dropouts."
    p.font.size = Pt(13)
    p = tf2.add_paragraph()
    p.text = "\n• Collapses multi-attribute trade-offs (pay vs work-life balance) into silent compromises."
    p.font.size = Pt(13)

    # Card 3: Demographic Bias
    add_card(slide2, Inches(8.88), top_pos, col_w, h, "3. Demographic Stereotyping", NAVY_PRIMARY)
    tb3 = slide2.shapes.add_textbox(Inches(9.03), top_pos + Inches(0.8), col_w - Inches(0.3), h - Inches(1.0))
    tf3 = tb3.text_frame
    tf3.word_wrap = True
    tf3.paragraphs[0].text = "• Inherits historical labor biases from training corpora (Bolukbasi et al., 2016)."
    tf3.paragraphs[0].font.size = Pt(13)
    tf3.paragraphs[0].font.color.rgb = TEXT_MAIN
    p = tf3.add_paragraph()
    p.text = "\n• Disproportionately steers non-traditional or underrepresented profiles into lower-agency certifications."
    p.font.size = Pt(13)
    p = tf3.add_paragraph()
    p.text = "\n• Lacks transparent oversight or counterfactual verification."
    p.font.size = Pt(13)

    # =========================================================================
    # SLIDE 3: Proposed Solution & Core Innovation
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    add_header(slide3, "The Solution: Dialectic Multi-Persona Deliberation", "CORE ARCHITECTURAL INNOVATION")

    card_left_w = Inches(5.6)
    card_right_w = Inches(5.8)
    h3 = Inches(4.8)

    # Left Card: Core Philosophy
    add_card(slide3, Inches(0.8), Inches(1.8), card_left_w, h3, "Dialectic Triad Architecture", TEAL_ACCENT)
    tb_left = slide3.shapes.add_textbox(Inches(1.0), Inches(2.6), card_left_w - Inches(0.4), h3 - Inches(1.0))
    tfl = tb_left.text_frame
    tfl.word_wrap = True
    tfl.paragraphs[0].text = "Instead of a single AI giving advice, three adversarial personas debate in structured rounds:\n"
    tfl.paragraphs[0].font.size = Pt(14)
    tfl.paragraphs[0].font.color.rgb = TEXT_MAIN
    
    bullets = [
        "Planner (Thesis): Proposes optimistic pathways and career milestones.",
        "Critic (Antithesis): Scrutinizes prerequisites, time bounds, and labor risks.",
        "Ethics-Reviewer (Guardrail): Audits credential debt, well-being, and fairness.",
        "Arbiter (Synthesis): Produces balanced guidance, maps dispute traces, and calibrates uncertainty."
    ]
    for b in bullets:
        p = tfl.add_paragraph()
        p.text = "• " + b + "\n"
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_MAIN

    # Right Card: The 4 Responsible AI Pillars
    add_card(slide3, Inches(6.7), Inches(1.8), card_right_w, h3, "Key Pillars of Responsible AI", NAVY_PRIMARY)
    tb_right = slide3.shapes.add_textbox(Inches(6.9), Inches(2.6), card_right_w - Inches(0.4), h3 - Inches(1.0))
    tfr = tb_right.text_frame
    tfr.word_wrap = True
    
    pillars = [
        ("Avoiding One-Sided Advice: ", "Adversarial cross-examination eliminates sycophancy."),
        ("Transparency of Disagreement: ", "Explicit dispute graph reveals real-world trade-offs."),
        ("Demographic Fairness: ", "Tested via 500+ counterfactual synthetic profile audits."),
        ("Calibrated Uncertainty: ", "Explicit score U(R) separates known skills from market risk."),
        ("Meaningful Human Override: ", "Cognitive forcing function gives user final veto power.")
    ]
    for i, (head, desc) in enumerate(pillars):
        p = tfr.paragraphs[0] if i == 0 else tfr.add_paragraph()
        p.text = f"{i+1}. {head}"
        p.font.bold = True
        p.font.size = Pt(13)
        p.font.color.rgb = TEAL_ACCENT
        p2 = tfr.add_paragraph()
        p2.text = f"   {desc}\n"
        p2.font.size = Pt(12)
        p2.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 4: Complementary Personas Deep-Dive
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    add_header(slide4, "Complementary Personas: Conflicting Objective Functions", "AGENT CONTRACTS & PERSONA DESIGN")

    p_w = Inches(3.64)
    p_h = Inches(4.8)

    # Persona 1: Planner
    add_card(slide4, Inches(0.8), Inches(1.8), p_w, p_h, "Planner Persona (π_P)", TEAL_ACCENT)
    tbp1 = slide4.shapes.add_textbox(Inches(0.95), Inches(2.5), p_w - Inches(0.3), p_h - Inches(0.9))
    tfp1 = tbp1.text_frame
    tfp1.word_wrap = True
    tfp1.paragraphs[0].text = "Role: Proactive Opportunity Optimizer\n"
    tfp1.paragraphs[0].font.bold = True
    tfp1.paragraphs[0].font.size = Pt(13)
    tfp1.paragraphs[0].font.color.rgb = TEAL_ACCENT
    items1 = [
        "Maps candidate skills to target occupation graph nodes.",
        "Generates milestone sequence (courses, certifications, roles).",
        "Optimizes forward career momentum and upward trajectory.",
        "Must defend plans using grounded course & salary citations."
    ]
    for item in items1:
        p = tfp1.add_paragraph()
        p.text = "• " + item
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_MAIN

    # Persona 2: Critic
    add_card(slide4, Inches(4.84), Inches(1.8), p_w, p_h, "Critic Persona (π_C)", ROSE_ACCENT)
    tbp2 = slide4.shapes.add_textbox(Inches(4.99), Inches(2.5), p_w - Inches(0.3), p_h - Inches(0.9))
    tfp2 = tbp2.text_frame
    tfp2.word_wrap = True
    tfp2.paragraphs[0].text = "Role: Adversarial Feasibility Auditor\n"
    tfp2.paragraphs[0].font.bold = True
    tfp2.paragraphs[0].font.size = Pt(13)
    tfp2.paragraphs[0].font.color.rgb = ROSE_ACCENT
    items2 = [
        "Attacks prerequisite DAG violations in the Neo4j graph.",
        "Calculates time infeasibility (weekly study hours vs workload).",
        "Flags market displacement risks & local hiring bottlenecks.",
        "Forces Planner to either concede or adapt milestones."
    ]
    for item in items2:
        p = tfp2.add_paragraph()
        p.text = "• " + item
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_MAIN

    # Persona 3: Ethics-Reviewer
    add_card(slide4, Inches(8.88), Inches(1.8), p_w, p_h, "Ethics-Reviewer (π_E)", AMBER_ACCENT)
    tbp3 = slide4.shapes.add_textbox(Inches(9.03), Inches(2.5), p_w - Inches(0.3), p_h - Inches(0.9))
    tfp3 = tbp3.text_frame
    tfp3.word_wrap = True
    tfp3.paragraphs[0].text = "Role: Socio-Economic Equity Guardian\n"
    tfp3.paragraphs[0].font.bold = True
    tfp3.paragraphs[0].font.size = Pt(13)
    tfp3.paragraphs[0].font.color.rgb = AMBER_ACCENT
    items3 = [
        "Audits tuition cost-to-income risk and predatory certificates.",
        "Evaluates work-life sustainability and caregiver constraints.",
        "Checks for accessible alternatives (e.g. open courseware).",
        "Prevents demographic stereotyping across socioeconomic tiers."
    ]
    for item in items3:
        p = tfp3.add_paragraph()
        p.text = "• " + item
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_MAIN

    # =========================================================================
    # SLIDE 5: Multi-Turn Dialectic Protocol
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    add_header(slide5, "Multi-Turn Dialectic Protocol & State Machine", "INTERACTION PROTOCOL & DELIBERATION LOOP")

    steps = [
        ("Round 1: Thesis", "Planner constructs initial milestone trajectory grounded in Neo4j skill graph and course catalog.", TEAL_ACCENT),
        ("Round 2: Operational Attack", "Critic interrogates prerequisite gaps, temporal overload, and hiring risk metrics.", ROSE_ACCENT),
        ("Round 3: Normative Review", "Ethics-Reviewer challenges predatory credential pricing, debt exposure, and burnout potential.", AMBER_ACCENT),
        ("Round 4: Rebuttal & Adaptation", "Planner adapts milestones, concedes unviable steps, or provides grounded evidence refutations.", NAVY_PRIMARY),
        ("Convergence: Arbiter Synthesis", "Arbiter extracts dispute graph, computes calibrated uncertainty U(R), and triggers override gates.", TEAL_ACCENT)
    ]

    card_h = Inches(0.85)
    for i, (title_s, desc_s, col_s) in enumerate(steps):
        top_s = Inches(1.8) + Inches(i * 0.95)
        add_card(slide5, Inches(0.8), top_s, Inches(11.733), card_h, "", border_color=col_s)
        
        # Step Number Badge
        badge = slide5.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.0), top_s + Inches(0.15), Inches(2.2), Inches(0.55))
        badge.fill.solid()
        badge.fill.fore_color.rgb = col_s
        badge.line.fill.background()
        bp = badge.text_frame.paragraphs[0]
        bp.text = f"STEP {i+1}"
        bp.font.size = Pt(12)
        bp.font.bold = True
        bp.font.color.rgb = CARD_BG
        bp.alignment = PP_ALIGN.CENTER

        # Content box
        tbs = slide5.shapes.add_textbox(Inches(3.4), top_s + Inches(0.08), Inches(8.9), Inches(0.7))
        tfs = tbs.text_frame
        p_t = tfs.paragraphs[0]
        p_t.text = title_s + " — "
        p_t.font.size = Pt(13)
        p_t.font.bold = True
        p_t.font.color.rgb = NAVY_PRIMARY
        
        p_d = tfs.add_paragraph()
        p_d.text = desc_s
        p_d.font.size = Pt(12)
        p_d.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 6: Hybrid GraphRAG Grounding
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    add_header(slide6, "Hybrid GraphRAG: Structured Graph + Dense Retrieval", "DATA GROUNDING & FACTUAL INTEGRITY")

    add_card(slide6, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8), "Neo4j Career Knowledge Graph", TEAL_ACCENT)
    tbg1 = slide6.shapes.add_textbox(Inches(1.0), Inches(2.5), Inches(5.2), Inches(3.9))
    tfg1 = tbg1.text_frame
    tfg1.word_wrap = True
    tfg1.paragraphs[0].text = "Why Structured Graph Matters:\n"
    tfg1.paragraphs[0].font.bold = True
    tfg1.paragraphs[0].font.size = Pt(13)
    tfg1.paragraphs[0].font.color.rgb = TEAL_ACCENT
    g_items = [
        "Ontology: Formal O*NET & ESCO hierarchical taxonomies.",
        "Deterministic Prerequisites: Enforces DAG constraints (Skill A must precede Skill B).",
        "Role-Competency Edges: Weighted necessity scores (w ∈ [0, 1]) prevent hallucinated requirements.",
        "Cypher Queries: Planner and Critic verify paths via exact graph traversals."
    ]
    for it in g_items:
        p = tfg1.add_paragraph()
        p.text = "• " + it
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_MAIN

    add_card(slide6, Inches(6.9), Inches(1.8), Inches(5.6), Inches(4.8), "Chroma / FAISS Vector Store", NAVY_PRIMARY)
    tbg2 = slide6.shapes.add_textbox(Inches(7.1), Inches(2.5), Inches(5.2), Inches(3.9))
    tfg2 = tbg2.text_frame
    tfg2.word_wrap = True
    tfg2.paragraphs[0].text = "Why Vector RAG Completes The System:\n"
    tfg2.paragraphs[0].font.bold = True
    tfg2.paragraphs[0].font.size = Pt(13)
    tfg2.paragraphs[0].font.color.rgb = NAVY_PRIMARY
    v_items = [
        "Unstructured Course Syllabi: Embeddings of public university and MOOC course outlines.",
        "Real-Time Job Postings: Regional hiring trends and employer skill mentions.",
        "Wage & Outlook Tables: BLS percentiles and projected 10-year growth.",
        "Attribution Score: Every factual claim in debate requires cosine similarity citation > 0.85."
    ]
    for it in v_items:
        p = tfg2.add_paragraph()
        p.text = "• " + it
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_MAIN

    # =========================================================================
    # SLIDE 7: Responsible AI, Calibrated Uncertainty & Override
    # =========================================================================
    slide7 = prs.slides.add_slide(blank_layout)
    add_header(slide7, "Calibrated Uncertainty & Meaningful Human Override", "RESPONSIBLE AI GOVERNANCE")

    add_card(slide7, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8), "Calibrated Uncertainty Metric", AMBER_ACCENT)
    tbu = slide7.shapes.add_textbox(Inches(1.0), Inches(2.5), Inches(5.2), Inches(3.9))
    tfu = tbu.text_frame
    tfu.word_wrap = True
    tfu.paragraphs[0].text = "Formulation of Epistemic Uncertainty U(R):\n"
    tfu.paragraphs[0].font.bold = True
    tfu.paragraphs[0].font.size = Pt(13)
    tfu.paragraphs[0].font.color.rgb = AMBER_ACCENT
    u_points = [
        "U(R) = α·H(Π) + β·Sparsity(G, P) + γ·(1 - GroundingScore)",
        "H(Π): Persona Position Entropy (measures degree of internal disagreement).",
        "Sparsity(G, P): Graph distance between user's current skills and target role.",
        "GroundingScore: Empirical citation density from retrieved data.",
        "Calibrated Output: High uncertainty communicates risk rather than false confidence."
    ]
    for pt in u_points:
        p = tfu.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_MAIN

    add_card(slide7, Inches(6.9), Inches(1.8), Inches(5.6), Inches(4.8), "Human Override Gate & Friction", TEAL_ACCENT)
    tbo = slide7.shapes.add_textbox(Inches(7.1), Inches(2.5), Inches(5.2), Inches(3.9))
    tfo = tbo.text_frame
    tfo.word_wrap = True
    tfo.paragraphs[0].text = "Cognitive Forcing Trigger Condition:\n"
    tfo.paragraphs[0].font.bold = True
    tfo.paragraphs[0].font.size = Pt(13)
    tfo.paragraphs[0].font.color.rgb = TEAL_ACCENT
    o_points = [
        "TriggerOverride = 1[ U(R) > θ_unc ∨ |K_unresolved| ≥ 1 ∨ Risk > θ_risk ]",
        "Mitigates Automation Bias: Halts autonomous execution when high disagreement occurs.",
        "Presents Dispute Graph: Visualizes explicit trade-offs (e.g. speed vs accreditation).",
        "Mandatory Human Veto: System requires active user steering before finalizing commitments."
    ]
    for pt in o_points:
        p = tfo.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_MAIN

    # =========================================================================
    # SLIDE 8: Evaluation Framework & Metrics
    # =========================================================================
    slide8 = prs.slides.add_slide(blank_layout)
    add_header(slide8, "Evaluation Methodology: Quantitative & Qualitative Metrics", "RIGOROUS EVALUATION MATRIX")

    # Table of 5 Key Metrics
    metrics = [
        ("Evidence Diversity (ED)", "Shannon entropy across O*NET, university syllabi, labor stats", "ED > 1.85 bits"),
        ("Contradiction-Resolution Rate (CRR)", "Ratio of Critic challenges successfully resolved or conceded", "CRR ≥ 85%"),
        ("Unsupported-Claim Rate (UCR)", "Percentage of factual assertions lacking graph/vector grounding", "UCR < 5.0%"),
        ("Counterfactual Parity (Δ_parity)", "Recommendation divergence across 500+ demographic synthetic pairs", "Δ_parity ≤ 0.05"),
        ("Expected Calibration Error (ECE)", "Reliability calibration of predicted completion difficulty vs empirical", "ECE < 0.08"),
        ("User & Expert Rubric Score", "Double-blind evaluation by certified career counselors (1–5 Likert)", "Avg ≥ 4.5 / 5.0")
    ]

    for i, (m_name, m_desc, m_tgt) in enumerate(metrics):
        top_m = Inches(1.8) + Inches(i * 0.78)
        add_card(slide8, Inches(0.8), top_m, Inches(11.733), Inches(0.7), "")
        
        # Name
        tbm = slide8.shapes.add_textbox(Inches(1.0), top_m + Inches(0.08), Inches(4.0), Inches(0.5))
        pm = tbm.text_frame.paragraphs[0]
        pm.text = m_name
        pm.font.bold = True
        pm.font.size = Pt(13)
        pm.font.color.rgb = NAVY_PRIMARY

        # Description
        tbd = slide8.shapes.add_textbox(Inches(5.0), top_m + Inches(0.08), Inches(4.8), Inches(0.5))
        pd = tbd.text_frame.paragraphs[0]
        pd.text = m_desc
        pd.font.size = Pt(12)
        pd.font.color.rgb = TEXT_MUTED

        # Target Badge
        tbt = slide8.shapes.add_textbox(Inches(10.0), top_m + Inches(0.08), Inches(2.3), Inches(0.5))
        pt = tbt.text_frame.paragraphs[0]
        pt.text = m_tgt
        pt.font.bold = True
        pt.font.size = Pt(13)
        pt.font.color.rgb = TEAL_ACCENT
        pt.alignment = PP_ALIGN.RIGHT

    # =========================================================================
    # SLIDE 9: Comparative Baseline & Ablation Matrix
    # =========================================================================
    slide9 = prs.slides.add_slide(blank_layout)
    add_header(slide9, "Ablation Study: 4-Way Comparative Architecture", "EXPERIMENTAL SETUP & ABLATION MATRIX")

    col_ab_w = Inches(2.7)
    ab_h = Inches(4.8)

    ab_cards = [
        ("Baseline 1\nVanilla Qwen", "Single Agent", "Parametric Only", "Severe sycophancy, hallucinatory roadmaps, zero calibrated uncertainty.", ROSE_ACCENT),
        ("Baseline 2\nSingle-Agent RAG", "Single Agent", "Vector Search (FAISS)", "Factual retrieval improves, but suffers from monolithic confirmation bias.", AMBER_ACCENT),
        ("Ablation\nDyadic Debate", "Planner + Critic", "GraphRAG (Neo4j)", "Strong operational scrutiny, but vulnerable to socio-economic & ethics blindspots.", NAVY_PRIMARY),
        ("Full Proposed\nDialectic System", "Planner + Critic + Ethics-Reviewer", "Hybrid GraphRAG + Dispute Graph", "Balanced trade-offs, highest CRR, lowest UCR, guaranteed demographic fairness.", TEAL_ACCENT)
    ]

    for i, (title_ab, persona_ab, ground_ab, defect_ab, col_ab) in enumerate(ab_cards):
        left_ab = Inches(0.8) + Inches(i * 2.95)
        add_card(slide9, left_ab, Inches(1.8), col_ab_w, ab_h, "", border_color=col_ab)
        
        # Header Box
        tb_ah = slide9.shapes.add_textbox(left_ab + Inches(0.15), Inches(1.95), col_ab_w - Inches(0.3), Inches(1.0))
        pah = tb_ah.text_frame.paragraphs[0]
        pah.text = title_ab
        pah.font.bold = True
        pah.font.size = Pt(14)
        pah.font.color.rgb = col_ab

        # Content Box
        tb_ac = slide9.shapes.add_textbox(left_ab + Inches(0.15), Inches(3.0), col_ab_w - Inches(0.3), Inches(3.4))
        tf_ac = tb_ac.text_frame
        tf_ac.word_wrap = True
        
        p1 = tf_ac.paragraphs[0]
        p1.text = "Personas: " + persona_ab + "\n"
        p1.font.bold = True
        p1.font.size = Pt(11)
        p1.font.color.rgb = NAVY_PRIMARY
        
        p2 = tf_ac.add_paragraph()
        p2.text = "Grounding: " + ground_ab + "\n"
        p2.font.size = Pt(11)
        p2.font.color.rgb = TEXT_MUTED

        p3 = tf_ac.add_paragraph()
        p3.text = "Outcome Profile:\n" + defect_ab
        p3.font.size = Pt(11)
        p3.font.color.rgb = TEXT_MAIN

    # =========================================================================
    # SLIDE 10: Streamlit UI & Interactive Trace Viewer
    # =========================================================================
    slide10 = prs.slides.add_slide(blank_layout)
    add_header(slide10, "Prototype Implementation: Streamlit Debate Trace Viewer", "USER INTERACTION & HUMAN OVERSIGHT")

    add_card(slide10, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8), "Front-End Experience (Streamlit)", TEAL_ACCENT)
    tbu1 = slide10.shapes.add_textbox(Inches(1.0), Inches(2.5), Inches(5.2), Inches(3.9))
    tfu1 = tbu1.text_frame
    tfu1.word_wrap = True
    ui_points = [
        "Interactive Debate Trace: Displays side-by-side round arguments between Planner, Critic, and Ethics-Reviewer.",
        "Dispute Tree Visualizer: Highlights exact nodes of contention (cost vs speed, certification value).",
        "Calibrated Risk Gauges: Real-time meters for Epistemic Uncertainty and Market Volatility.",
        "One-Click Override Panel: Candidate can steer personas, inject constraints, or veto pathways."
    ]
    for pt in ui_points:
        p = tfu1.add_paragraph()
        p.text = "• " + pt + "\n"
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_MAIN

    add_card(slide10, Inches(6.9), Inches(1.8), Inches(5.6), Inches(4.8), "Local Infrastructure Architecture", NAVY_PRIMARY)
    tbu2 = slide10.shapes.add_textbox(Inches(7.1), Inches(2.5), Inches(5.2), Inches(3.9))
    tfu2 = tbu2.text_frame
    tfu2.word_wrap = True
    infra_points = [
        "100% Local Inference: Powered by Qwen (e.g. Qwen2.5-7B/14B) via Ollama/vLLM for complete privacy.",
        "Zero Cloud Dependency: User candidate data and resumes remain securely on-premise.",
        "Graph Backend: Neo4j community edition hosting O*NET/ESCO career taxonomy.",
        "Vector Engine: Chroma/FAISS managing local embeddings of open university syllabi."
    ]
    for pt in infra_points:
        p = tfu2.add_paragraph()
        p.text = "• " + pt + "\n"
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_MAIN

    # =========================================================================
    # SLIDE 11: Summary & Project Impact
    # =========================================================================
    slide11 = prs.slides.add_slide(blank_layout)
    add_header(slide11, "Conclusion & Academic Significance", "SUMMARY & FUTURE ROADMAP")

    add_card(slide11, Inches(0.8), Inches(1.8), Inches(11.733), Inches(4.8), "Key Contributions to Responsible AI", TEAL_ACCENT)
    tbc = slide11.shapes.add_textbox(Inches(1.1), Inches(2.5), Inches(11.1), Inches(3.8))
    tfc = tbc.text_frame
    tfc.word_wrap = True

    c_points = [
        ("Eliminates Single-Agent Sycophancy: ", "Introduces structured adversarial cross-examination that forces feasibility and prerequisite compliance."),
        ("Democratizes GraphRAG Grounding: ", "Combines Neo4j structural DAG constraints with dense vector course catalogs to eliminate hallucinations."),
        ("First Calibrated Dialectic Career Agent: ", "Replaces blind confidence with calibrated epistemic uncertainty and transparent dispute graphs."),
        ("Protects Human Agency: ", "Mitigates automation complacency through cognitive forcing functions and interactive override gates."),
        ("Guarantees Demographic Fairness: ", "Empirically validated through counterfactual synthetic profile audits to eliminate historical labor bias.")
    ]
    for i, (head, desc) in enumerate(c_points):
        p = tfc.paragraphs[0] if i == 0 else tfc.add_paragraph()
        p.text = f"✔ {head}"
        p.font.bold = True
        p.font.size = Pt(14)
        p.font.color.rgb = TEAL_ACCENT
        p2 = tfc.add_paragraph()
        p2.text = f"   {desc}\n"
        p2.font.size = Pt(13)
        p2.font.color.rgb = TEXT_MAIN

    # Save presentation
    output_path = "/home/thor/Desktop/RAI Project/Debate_Career_Guidance_Agent_Presentation.pptx"
    prs.save(output_path)
    print(f"Presentation saved successfully to: {output_path}")

if __name__ == "__main__":
    create_presentation()
