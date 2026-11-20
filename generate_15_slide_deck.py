#!/usr/bin/env python3
"""
Master Academic Presentation Generator (15 Slides) — Pure Black & White Executive Edition
Debate-Based Career Guidance Agent with Complementary Personas

Style:
- Strict Black and White / Monochrome Academic Theme
- Zero bright colors (no teal, blue, red, amber, green)
- Crisp black lines, high-contrast typography, academic table layouts
- High theoretical depth and complete numerical empirical benchmark data
- Verified Mentors (Dr. P. Akilandeswari, Pratyush Jha) & Authors
- Exactly 15 slides (Maximum 15 pages)
"""

import os
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt


def build_bw_deck(output_pptx="docs/FINAL_PRESENTATION_15_SLIDES.pptx"):
    os.makedirs(os.path.dirname(output_pptx), exist_ok=True)
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Pure Monochrome / Black & White Palette
    COLOR_WHITE = RGBColor(255, 255, 255)
    COLOR_BLACK = RGBColor(0, 0, 0)
    COLOR_DARK = RGBColor(17, 24, 39)        # Very dark charcoal #111827
    COLOR_MID = RGBColor(55, 65, 81)         # Medium dark charcoal #374151
    COLOR_MUTED = RGBColor(107, 114, 128)    # Medium gray #6B7280
    COLOR_LIGHT = RGBColor(243, 244, 246)    # Light gray tint #F3F4F6
    COLOR_BORDER = RGBColor(0, 0, 0)         # Crisp solid black border
    COLOR_LINE = RGBColor(156, 163, 175)     # Subdued divider #9CA3AF

    FONT_FAMILY = "Liberation Sans"
    TOTAL_SLIDES = 15

    def set_white_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = COLOR_WHITE
        bg.line.fill.background()
        return bg

    def add_academic_header(slide, title, category, slide_num, takeaway=""):
        # Section Tag
        tag_tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.35), Inches(8.0), Inches(0.28))
        ptag = tag_tb.text_frame.paragraphs[0]
        ptag.text = category.upper()
        ptag.font.name = FONT_FAMILY
        ptag.font.size = Pt(9.0)
        ptag.font.bold = True
        ptag.font.color.rgb = COLOR_MUTED

        # Slide Number
        num_tb = slide.shapes.add_textbox(Inches(11.0), Inches(0.35), Inches(1.533), Inches(0.28))
        pnum = num_tb.text_frame.paragraphs[0]
        pnum.text = f"{slide_num:02d} / {TOTAL_SLIDES}"
        pnum.font.name = FONT_FAMILY
        pnum.font.size = Pt(9.5)
        pnum.font.bold = True
        pnum.font.color.rgb = COLOR_BLACK
        pnum.alignment = PP_ALIGN.RIGHT

        # Main Slide Title
        t_tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.62), Inches(11.733), Inches(0.42))
        pt = t_tb.text_frame.paragraphs[0]
        pt.text = title
        pt.font.name = FONT_FAMILY
        pt.font.size = Pt(20)
        pt.font.bold = True
        pt.font.color.rgb = COLOR_BLACK

        # Takeaway Subtitle
        if takeaway:
            sub_tb = slide.shapes.add_textbox(Inches(0.8), Inches(1.04), Inches(11.733), Inches(0.28))
            psub = sub_tb.text_frame.paragraphs[0]
            psub.text = takeaway
            psub.font.name = FONT_FAMILY
            psub.font.size = Pt(10.5)
            psub.font.color.rgb = COLOR_MID

        # Crisp Horizontal Header Rule
        rule = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.36), Inches(11.733), Inches(0.015))
        rule.fill.solid()
        rule.fill.fore_color.rgb = COLOR_BLACK
        rule.line.fill.background()

    def add_box(slide, left, top, width, height, title="", title_size=12.0, fill_color=COLOR_WHITE, border_color=COLOR_BLACK, border_width=1.0):
        box = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
        box.fill.solid()
        box.fill.fore_color.rgb = fill_color
        box.line.color.rgb = border_color
        box.line.width = Pt(border_width)

        if title:
            # Title banner inside box
            title_bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, Inches(0.38))
            title_bg.fill.solid()
            title_bg.fill.fore_color.rgb = COLOR_BLACK
            title_bg.line.fill.background()

            tb = slide.shapes.add_textbox(left + Inches(0.12), top + Inches(0.04), width - Inches(0.24), Inches(0.30))
            p = tb.text_frame.paragraphs[0]
            p.text = title
            p.font.name = FONT_FAMILY
            p.font.size = Pt(title_size)
            p.font.bold = True
            p.font.color.rgb = COLOR_WHITE
            tb.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

        return box

    def add_bullet(tf, bold_prefix, text, pt_size=10.0, space_after=4, bold_color=COLOR_BLACK, norm_color=COLOR_DARK):
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
    # SLIDE 1: Title Slide (Black & White Academic Masterpiece)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_white_bg(s1)

    # Top border line
    t_line = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.8), Inches(11.733), Inches(0.03))
    t_line.fill.solid()
    t_line.fill.fore_color.rgb = COLOR_BLACK
    t_line.line.fill.background()

    # Meta Tag
    tag1 = s1.shapes.add_textbox(Inches(0.8), Inches(0.95), Inches(11.733), Inches(0.3))
    ptag1 = tag1.text_frame.paragraphs[0]
    ptag1.text = "ACADEMIC RESEARCH PRESENTATION  •  RESPONSIBLE ARTIFICIAL INTELLIGENCE"
    ptag1.font.name = FONT_FAMILY
    ptag1.font.size = Pt(9.5)
    ptag1.font.bold = True
    ptag1.font.color.rgb = COLOR_MUTED

    # Title
    tb_title = s1.shapes.add_textbox(Inches(0.8), Inches(1.35), Inches(11.733), Inches(1.5))
    pt1 = tb_title.text_frame.paragraphs[0]
    pt1.text = "Debate-Based Career Guidance Agent\nwith Complementary Personas"
    pt1.font.name = FONT_FAMILY
    pt1.font.size = Pt(28)
    pt1.font.bold = True
    pt1.font.color.rgb = COLOR_BLACK

    # Subtitle
    tb_sub1 = s1.shapes.add_textbox(Inches(0.8), Inches(3.0), Inches(11.733), Inches(0.6))
    psub1 = tb_sub1.text_frame.paragraphs[0]
    psub1.text = "A Grounded Multi-Agent Architecture with Prerequisite Knowledge Graph Verification, Calibrated Uncertainty, and Cognitive Forcing"
    psub1.font.name = FONT_FAMILY
    psub1.font.size = Pt(12.5)
    psub1.font.color.rgb = COLOR_MID

    # Mid divider
    m_line = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(3.75), Inches(11.733), Inches(0.015))
    m_line.fill.solid()
    m_line.fill.fore_color.rgb = COLOR_BLACK
    m_line.line.fill.background()

    # Left Box: Authors & Department
    b1_left = add_box(s1, Inches(0.8), Inches(4.05), Inches(5.6), Inches(2.55), title="Candidate Research Team", border_width=1.0)
    tf1_l = s1.shapes.add_textbox(Inches(1.0), Inches(4.55), Inches(5.2), Inches(1.9)).text_frame
    add_bullet(tf1_l, "Authors:", "Gedela Rishikesh Reddy, Aniket Srivastava, Parth Gupta", pt_size=10.5)
    add_bullet(tf1_l, "Department:", "Department of Computing Technologies", pt_size=10.0)
    add_bullet(tf1_l, "Institution:", "SRM Institute of Science and Technology", pt_size=10.0)
    add_bullet(tf1_l, "Integrity Audit:", "Noplag Engine: 0.00% Plagiarism, 0.0% AI Slop", pt_size=10.0, bold_color=COLOR_BLACK)

    # Right Box: Mentors & Runtime Stack
    b1_right = add_box(s1, Inches(6.8), Inches(4.05), Inches(5.733), Inches(2.55), title="Mentorship & System Specification", border_width=1.0)
    tf1_r = s1.shapes.add_textbox(Inches(7.0), Inches(4.55), Inches(5.333), Inches(1.9)).text_frame
    add_bullet(tf1_r, "Faculty Mentor:", "Dr. P. Akilandeswari", pt_size=10.5)
    add_bullet(tf1_r, "Industry Mentor:", "Pratyush Jha", pt_size=10.5)
    add_bullet(tf1_r, "Official Stack:", "Qwen Local (7B) via Ollama • Python Harness • 42-Node DAG • ChromaDB • Streamlit", pt_size=9.5)
    add_bullet(tf1_r, "Architecture Mode:", "100% On-Device Local Inference (Zero API Cost, Full Privacy)", pt_size=9.5)

    add_notes(s1, "Respected committee members and mentors, we present our research on a Debate-Based Career Guidance Agent with Complementary Personas. Our system eliminates the catastrophic failure modes of unconstrained language models by introducing dialectic adversarial debate, deterministic knowledge graph verification, and calibrated human override.")

    # =========================================================================
    # SLIDE 2: Problem Statement & Advisory Hazards
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_white_bg(s2)
    add_academic_header(s2, "Systemic Failure Modes of Monolithic LLMs in Career Advising", "Section 1: Problem Formulation", 2, "Unconstrained generative chatbots exhibit severe pedagogical failure modes that derail student career preparation.")

    w2 = Inches(2.78)
    h2 = Inches(5.5)
    t2 = Inches(1.5)

    hazards = [
        ("Conversational Sycophancy", [
            ("Core Vulnerability:", "Autoregressive generation prioritizes user agreement over rigorous pedagogical assessment."),
            ("Observed Failure:", "Affirms unrealistic goals, e.g., validating a novice's claim to master Senior MLOps in 60 days."),
            ("Consequence:", "Students enter technical screening interviews unprepared, facing immediate rejection."),
            ("Benchmark:", "Monolithic baseline pushes back in 0.0% of unrealistic student queries."),
        ]),
        ("Prerequisite Skipping", [
            ("Core Vulnerability:", "Next-token prediction lacks structured dependency awareness across academic disciplines."),
            ("Observed Failure:", "Sequences Deep Learning, Transformers, or Distributed Systems before Linear Algebra or OS fundamentals."),
            ("Consequence:", "Superficial memorization without fundamental conceptual grounding."),
            ("Benchmark:", "Monolithic LLM exhibits a 90.9% prerequisite violation rate across curriculum paths."),
        ]),
        ("Predatory Debt Steering", [
            ("Core Vulnerability:", "Pretraining corpora heavily over-represent aggressive commercial marketing."),
            ("Observed Failure:", "Recommends ₹1,20,000 commercial bootcamps and loans to students with ₹3,000/month budgets."),
            ("Consequence:", "Induces catastrophic educational debt when high-quality free alternatives exist."),
            ("Benchmark:", "Monolithic baseline fails to filter predatory commercial offerings for low-budget profiles."),
        ]),
        ("Institutional Pedigree Bias", [
            ("Core Vulnerability:", "Training distribution reflects systemic historical disparities in hiring outcomes."),
            ("Observed Failure:", "Holding skills constant, suggests ML engineering to Tier-1 students but IT helpdesk to Tier-3 peers."),
            ("Consequence:", "Perpetuates socio-economic gatekeeping and reinforces institutional prejudice."),
            ("Benchmark:", "Monolithic LLM achieves a dismal Jaccard curriculum similarity of J = 0.32 between matched pairs."),
        ]),
    ]

    for i, (title, bullets) in enumerate(hazards):
        x = Inches(0.8) + i * Inches(2.98)
        add_box(s2, x, t2, w2, h2, title=title, title_size=11.0)
        tf = s2.shapes.add_textbox(x + Inches(0.12), t2 + Inches(0.48), w2 - Inches(0.24), h2 - Inches(0.58)).text_frame
        for bold, text in bullets:
            add_bullet(tf, bold, text, pt_size=9.2, space_after=5)

    add_notes(s2, "Slide 2 outlines the four critical failure modes documented in baseline conversational models: Sycophancy, Prerequisite Skipping, Predatory Debt Steering, and Pedigree Bias. Without deterministic grounding, monolithic LLMs fail 90.9% of prerequisite checks and embed socio-economic prejudice.")

    # =========================================================================
    # SLIDE 3: Theoretical Foundations
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_white_bg(s3)
    add_academic_header(s3, "Three Theoretical Pillars of Responsible AI Advisory", "Section 2: Theoretical Foundations", 3, "Synthesizing Hegelian dialectics, public curricular standards, and dual-process cognitive psychology.")

    w3 = Inches(3.78)
    h3 = Inches(5.5)
    t3 = Inches(1.5)

    pillars = [
        ("1. Multi-Agent Dialectics", [
            ("Seminal Literature:", "Du et al. (2023) 'Improving Factuality via Multi-Agent Debate'; Liang et al. (2023) 'Encouraging Divergent Thinking'."),
            ("Philosophical Root:", "Hegelian dialectic progression: Thesis (Planner proposal), Antithesis (Critic pushback), and Synthesis (Moderator reconciliation)."),
            ("Mathematical Rationale:", "Decomposing generation into adversarial personas forces divergent arguments into the context window, breaking single-prompt consensus collapse."),
            ("Pedagogical Outcome:", "Forces explicit trade-off exploration between speed and foundational rigor."),
        ]),
        ("2. Public Curricular Grounding", [
            ("Accredited Standards:", "ACM/IEEE CS2023 Curricular Guidelines for Undergraduate Degree Programs; U.S. Bureau of Labor Statistics O*NET Standard Occupational Taxonomy."),
            ("Information Retrieval:", "Lewis et al. (2020) Dense Retrieval-Augmented Generation (RAG)."),
            ("Systemic Constraint:", "Restricts persona deliberations to verified course descriptions (MIT OCW, Harvard CS50, Berkeley CS61) and empirical hiring requirements."),
            ("Pedagogical Outcome:", "Eliminates ungrounded commercial claims and unverifiable certificate marketing."),
        ]),
        ("3. Cognitive Forcing & Agency", [
            ("Seminal Literature:", "Buçinca et al. (2021) 'To Trust or to Think: Cognitive Forcing Functions in AI-Assisted Decision Making'."),
            ("Cognitive Architecture:", "Kahneman (2011) dual-process theory: Disrupts heuristic System 1 passive acceptance by triggering deliberative System 2 reflection."),
            ("Systemic Threshold:", "When calibrated uncertainty U_cal >= 0.45 or prerequisite violations occur, autonomous release is blocked; student must engage with Dispute Tree sliders."),
            ("Pedagogical Outcome:", "Restores student decision agency without passive overreliance on AI recommendations."),
        ]),
    ]

    for i, (title, bullets) in enumerate(pillars):
        x = Inches(0.8) + i * Inches(3.98)
        add_box(s3, x, t3, w3, h3, title=title, title_size=12.0)
        tf = s3.shapes.add_textbox(x + Inches(0.14), t3 + Inches(0.48), w3 - Inches(0.28), h3 - Inches(0.58)).text_frame
        for bold, text in bullets:
            add_bullet(tf, bold, text, pt_size=9.5, space_after=6)

    add_notes(s3, "Slide 3 establishes our theoretical foundations: multi-agent dialectics from Du and Liang et al., public knowledge grounding via ACM/IEEE CS2023 and O*NET standards, and cognitive forcing functions from Bucinca et al. to prevent passive student overreliance.")

    # =========================================================================
    # SLIDE 4: Countering Critiques of Multi-Agent Debate
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_white_bg(s4)
    add_academic_header(s4, "Overcoming Agreement Collapse & The Woozle Effect", "Section 2: Literature Survey & Defense", 4, "Directly resolving the failure modes identified by Smit et al. (EMNLP 2024).")

    w4_split = Inches(5.7)
    h4_split = Inches(5.5)
    t4_split = Inches(1.5)

    # Left: The Critique
    add_box(s4, Inches(0.8), t4_split, w4_split, h4_split, title="The Academic Critique: Smit et al. (EMNLP 2024)", title_size=12.0)
    tf4_l = s4.shapes.add_textbox(Inches(1.0), t4_split + Inches(0.48), w4_split - Inches(0.4), h4_split - Inches(0.58)).text_frame
    add_bullet(tf4_l, "Paper Reference:", "'Should We Be Going MAD? Multi-Agent Debate and Consensus Failure' (EMNLP 2024).")
    add_bullet(tf4_l, "Vulnerability 1 (Agreement Collapse):", "Agents sharing the same foundational model weights rapidly converge toward superficial harmony, smoothing away contradictions into unprincipled compromises.")
    add_bullet(tf4_l, "Vulnerability 2 (The Woozle Effect):", "When an early persona asserts an unfounded claim, peer agents frequently amplify and validate the mistake, cascading hallucinations across rounds.")
    add_bullet(tf4_l, "Vulnerability 3 (Correlated Errors):", "Majority voting fails because agents share underlying pretraining biases; multiplying agents merely multiplies shared blindspots.")
    add_bullet(tf4_l, "Empirical Baseline Failure:", "Unmoderated multi-agent debate (Config 3) still resulted in an 86.4% prerequisite error rate due to mutual error reinforcement.")

    # Right: Our Solutions
    add_box(s4, Inches(6.8), t4_split, w4_split, h4_split, title="Our Architectural Invariants & Mathematical Solutions", title_size=12.0)
    tf4_r = s4.shapes.add_textbox(Inches(7.0), t4_split + Inches(0.48), w4_split - Inches(0.4), h4_split - Inches(0.58)).text_frame
    add_bullet(tf4_r, "Solution 1: Decoupled Persona Temperatures:", "We break shared priors by assigning distinct inference temperatures (Planner T = 0.3 for structured planning; Critic T = 0.6 for aggressive adversarial scrutiny).")
    add_bullet(tf4_r, "Solution 2: Deterministic 42-Node Knowledge Graph:", "Personas cannot invent dependencies. Prerequisite reachability is verified externally by NetworkX in O(|V|+|E|) time, mathematically eliminating the Woozle Effect.")
    add_bullet(tf4_r, "Solution 3: Transparent Dispute Trees:", "We abandon forced consensus. Disagreements are compiled into an explicit Dispute Tree, presenting genuine pedagogical trade-offs for student resolution.")
    add_bullet(tf4_r, "Empirical Result:", "Our proposed architecture (Config 4) achieved strictly 0.0% prerequisite errors and 100.0% contradiction resolution across all 80 benchmark runs.")

    add_notes(s4, "Slide 4 is essential for viva defense. We directly address the EMNLP 2024 critique by Smit et al. regarding consensus failure. We explain how asymmetric inference temperatures, external knowledge graph verification, and explicit dispute trees overcome agreement collapse.")

    # =========================================================================
    # SLIDE 5: End-to-End System Architecture
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_white_bg(s5)
    add_academic_header(s5, "End-to-End Decision Flow Architecture", "Section 3: System Architecture", 5, "Candidate Intake -> Dense Retrieval -> Persona Deliberation -> Moderator Synthesis -> Graph Verification -> Cognitive Gate.")

    w5_box = Inches(1.8)
    h5_box = Inches(3.6)
    t5_box = Inches(1.5)
    spacing5 = Inches(0.18)

    flow_steps = [
        ("1. Intake", "Candidate profile ingestion: skills, target role, monthly budget, timeline."),
        ("2. Retrieval", "ChromaDB retrieves top-4 ACM CS2023 course syllabi and O*NET standards."),
        ("3. Triad Debate", "Planner (milestones), Critic (systems & math gaps), Ethics (debt & bias audit)."),
        ("4. Synthesis", "Moderator resolves disputes, constructs Dispute Tree, calculates uncertainty U."),
        ("5. Graph Check", "Deterministic 42-node DAG checks topological ordering in < 0.2 ms."),
        ("6. Human Gate", "Blocks release if U >= 0.45 or Delta >= 1; activates Streamlit sliders for override."),
    ]

    for i, (title, desc) in enumerate(flow_steps):
        x = Inches(0.8) + i * (w5_box + spacing5)
        add_box(s5, x, t5_box, w5_box, h5_box, title=title, title_size=10.0)
        tf = s5.shapes.add_textbox(x + Inches(0.08), t5_box + Inches(0.44), w5_box - Inches(0.16), h5_box - Inches(0.52)).text_frame
        add_bullet(tf, "", desc, pt_size=9.2, space_after=4)

    # Lower Box: Systemic Properties
    add_box(s5, Inches(0.8), Inches(5.3), Inches(11.733), Inches(1.7), title="Architectural Safety & Verification Separation", title_size=11.5)
    tf5_bot = s5.shapes.add_textbox(Inches(1.0), Inches(5.68), Inches(11.333), Inches(1.2)).text_frame
    add_bullet(tf5_bot, "Separation of Powers:", "Generative reasoning is strictly isolated in the persona triad; deterministic structural verification is enforced separately by graph traversal algorithms.", pt_size=9.8)
    add_bullet(tf5_bot, "Local Edge Execution:", "Entire pipeline executes locally on consumer hardware via local Qwen 2.5 7B, guaranteeing student privacy and ₹0.00 cloud API costs.", pt_size=9.8)

    add_notes(s5, "Slide 5 illustrates our end-to-end decision flow. From student intake and ChromaDB retrieval to three-agent deliberation, moderator synthesis, deterministic graph verification, and the interactive cognitive forcing gate. Advisory generation and structural verification remain strictly decoupled.")

    # =========================================================================
    # SLIDE 6: Persona Specifications
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_white_bg(s6)
    add_academic_header(s6, "The Dialectic Triad: Operational Mandates & Persona Prompts", "Section 3: Persona Specifications", 6, "Planner, Critic, and Ethics-Reviewer operating under asymmetric temperatures.")

    w6 = Inches(3.78)
    h6 = Inches(5.5)
    t6 = Inches(1.5)

    triad_specs = [
        ("The Planner Persona (T = 0.3)", [
            ("Operational Role:", "Constructive curriculum designer and milestone formulator."),
            ("Systemic Mandate:", "Converts student aspirations into sequential quarterly milestones, practical projects, and verifiable deliverables."),
            ("Knowledge Grounding:", "Adheres to accredited ACM/IEEE CS2023 contact-hour credit requirements."),
            ("Temperature Setting:", "T = 0.3 enforces low entropy, structural consistency, and reliable formatting."),
        ]),
        ("The Critic Persona (T = 0.6)", [
            ("Operational Role:", "Skeptical technical interviewer and curriculum auditor."),
            ("Systemic Mandate:", "Proactively attacks missing mathematical and systems prerequisites; exposes timeline compression hazards."),
            ("Target Vulnerabilities:", "Penalizes superficial portfolio projects (e.g. wrapper APIs without fundamental algorithmic depth)."),
            ("Temperature Setting:", "T = 0.6 encourages creative counter-arguments and divergent failure hypothesis generation."),
        ]),
        ("The Ethics-Reviewer (T = 0.3)", [
            ("Operational Role:", "Financial debt auditor and socio-economic fairness guardian."),
            ("Systemic Mandate:", "Enforces zero-debt policy; blocks ₹1,20,000 commercial bootcamps; mandates MIT OCW and CS50."),
            ("Pedigree Equity:", "Guarantees that Tier-3 rural students receive identical rigorous technical training as Tier-1 peers."),
            ("Alternative Routing:", "Recommends open-source contributions (GitHub proof-of-work) to bypass institutional resume filters."),
        ]),
    ]

    for i, (title, bullets) in enumerate(triad_specs):
        x = Inches(0.8) + i * Inches(3.98)
        add_box(s6, x, t6, w6, h6, title=title, title_size=11.5)
        tf = s6.shapes.add_textbox(x + Inches(0.14), t6 + Inches(0.48), w6 - Inches(0.28), h6 - Inches(0.58)).text_frame
        for bold, text in bullets:
            add_bullet(tf, bold, text, pt_size=9.5, space_after=6)

    add_notes(s6, "Slide 6 defines the operational mandates and prompt configurations of our dialectic triad. The Planner builds constructive milestones at temperature 0.3; the Critic attacks gaps and timeline assumptions at temperature 0.6; and the Ethics-Reviewer guarantees financial safety and institutional fairness.")

    # =========================================================================
    # SLIDE 7: The 42-Node Knowledge Graph
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_white_bg(s7)
    add_academic_header(s7, "The 42-Node Prerequisite Knowledge Graph", "Section 4: Knowledge Graph Engineering", 7, "A deterministic DAG spanning 9 CS domains with automated Neo4j Cypher synchronization.")

    w7 = Inches(5.7)
    h7 = Inches(5.5)
    t7 = Inches(1.5)

    add_box(s7, Inches(0.8), t7, w7, h7, title="Curriculum Taxonomy & Domain Coverage", title_size=12.0)
    tf7_l = s7.shapes.add_textbox(Inches(1.0), t7 + Inches(0.48), w7 - Inches(0.4), h7 - Inches(0.58)).text_frame
    add_bullet(tf7_l, "Node Coverage (42 Total Nodes):", "Covers 9 core ACM/IEEE CS2023 domains:")
    add_bullet(tf7_l, "1. Foundations (3):", "Discrete Math, Linear Algebra, Probability & Statistics.")
    add_bullet(tf7_l, "2. Programming Core (5):", "Python Basics, Python OOP, C Basics, Pointers & Memory, Java.")
    add_bullet(tf7_l, "3. Systems & Architecture (7):", "Computer Architecture, OS Internals, Concurrency, Linux/POSIX, Networking, Distributed Systems, System Design.")
    add_bullet(tf7_l, "4. Databases & Storage (4):", "RDBMS, SQL Optimization, Indexing/Normalization, NoSQL.")
    add_bullet(tf7_l, "5. Web & Engineering (4):", "HTML/CSS, JavaScript, Backend Frameworks, REST APIs.")
    add_bullet(tf7_l, "6. Machine Learning (7):", "Data Wrangling, ML Foundations, Deep Learning, NLP/Transformers, LLMs/RAG, MLOps, AI Ethics.")
    add_bullet(tf7_l, "7. Security & Cloud (8):", "DSA (3), DevOps/Cloud (4), Security & Mobile (5).")
    add_bullet(tf7_l, "Directed Edges (47 Total Edges):", "Rigorous prerequisite constraints (e.g. Linear Algebra -> ML Foundations -> Deep Learning).")

    add_box(s7, Inches(6.8), t7, w7, h7, title="Deterministic Traversal & Neo4j Export", title_size=12.0)
    tf7_r = s7.shapes.add_textbox(Inches(7.0), t7 + Inches(0.48), w7 - Inches(0.4), h7 - Inches(0.58)).text_frame
    add_bullet(tf7_r, "Mathematical Violation Formulation:", "A milestone v violates prerequisite ordering if prerequisite u is neither completed nor scheduled earlier:")
    add_bullet(tf7_r, "Delta_prereq =", "|{ (u, v) in E_prereq : v in M and u not in (S_curr union M_<v) }|", pt_size=10.0, bold_color=COLOR_BLACK)
    add_bullet(tf7_r, "Algorithmic Complexity:", "Checked via NetworkX topological sorting in deterministic O(|V| + |E|) time (< 0.2 milliseconds).")
    add_bullet(tf7_r, "Why In-Memory NetworkX:", "Sub-millisecond latency without external socket overhead or JVM server memory footprint on student laptops.")
    add_bullet(tf7_r, "Enterprise Neo4j Integration:", "Includes automated Cypher query generator (sync_to_neo4j) allowing the exact same 42-node schema to export to Neo4j graph databases.")

    add_notes(s7, "Slide 7 outlines the 42-node prerequisite knowledge graph. Spanning 9 computer science domains with 47 directed edges, our NetworkX engine checks topological reachability in under 0.2 milliseconds. We also support seamless synchronization with Neo4j via automated Cypher query exports.")

    # =========================================================================
    # SLIDE 8: Dispute Tree & Cognitive Forcing Gate
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_white_bg(s8)
    add_academic_header(s8, "Dispute Trees, Calibrated Uncertainty, and Human Override", "Section 4: Mediation & Human Agency", 8, "Structuring disagreements and restoring student decision autonomy through interactive sliders.")

    w8 = Inches(5.7)
    h8 = Inches(5.5)
    t8 = Inches(1.5)

    add_box(s8, Inches(0.8), t8, w8, h8, title="Calibrated Uncertainty Formulation (U_cal)", title_size=12.0)
    tf8_l = s8.shapes.add_textbox(Inches(1.0), t8 + Inches(0.48), w8 - Inches(0.4), h8 - Inches(0.58)).text_frame
    add_bullet(tf8_l, "Mathematical Formulation:", "Calibrated risk score calculated across four advisory friction dimensions:")
    add_bullet(tf8_l, "U_cal =", "0.30 * F_triad + 0.35 * Delta_prereq + 0.20 * R_socio + 0.15 * R_timeline", pt_size=10.5, bold_color=COLOR_BLACK)
    add_bullet(tf8_l, "F_triad (Persona Friction):", "Disagreement index across Planner, Critic, and Ethics outputs (0.0 to 1.0).", pt_size=9.2)
    add_bullet(tf8_l, "Delta_prereq (Graph Violations):", "Prerequisite sequence errors flagged by the 42-node DAG traversal.", pt_size=9.2)
    add_bullet(tf8_l, "R_socio (Financial Exposure):", "min(1.0, Cost / (12 * Budget)). Evaluates to 0.0 for MIT OCW; spikes only on debt.", pt_size=9.2)
    add_bullet(tf8_l, "R_timeline (Compression Risk):", "Timeline compression index when student timeline is below curriculum norms.", pt_size=9.2)
    add_bullet(tf8_l, "Case Study Proof (Priya):", "0.30(0.80) + 0.35(0.75) + 0.20(0.85) + 0.15(0.65) = 0.77 >= 0.45 -> Gate Triggers.", pt_size=9.2, bold_color=COLOR_BLACK)
    add_bullet(tf8_l, "Trigger Invariant:", "If U_cal >= 0.45 or Delta_prereq >= 1, autonomous roadmap release is blocked; sliders activate.", pt_size=9.2)

    add_box(s8, Inches(6.8), t8, w8, h8, title="Dispute Tree & Student Slider Controls", title_size=12.0)
    tf8_r = s8.shapes.add_textbox(Inches(7.0), t8 + Inches(0.48), w8 - Inches(0.4), h8 - Inches(0.58)).text_frame
    add_bullet(tf8_r, "Dispute Tree Structure:", "Rather than hiding disagreement, the Moderator maps active debate friction into three explicit student trade-off nodes:")
    add_bullet(tf8_r, "Trade-off 1 (Speed vs. Rigor):", "Rushing immediate portfolio projects vs. spending 8 weeks mastering foundational algorithms.")
    add_bullet(tf8_r, "Trade-off 2 (Debt vs. Open Source):", "Borrowing for a private commercial bootcamp vs. completing MIT OpenCourseWare + GitHub proof-of-work.")
    add_bullet(tf8_r, "Trade-off 3 (Placement vs. Proof-of-Work):", "Overcoming institutional tier bias via open-source pull requests.")
    add_bullet(tf8_r, "Interactive Override Sliders:", "Streamlit UI features Speed vs. Rigor vs. Budget sliders, enabling students to weigh trade-offs and customize their final roadmap.")

    add_notes(s8, "Slide 8 details our calibrated uncertainty formula and interactive Dispute Tree. When risk exceeds 0.45 or a prerequisite error occurs, the Cognitive Forcing Gate halts release. Students adjust three sliders—Speed, Rigor, and Budget—restoring human-in-the-loop decision agency.")

    # =========================================================================
    # SLIDE 9: Experimental Methodology
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_white_bg(s9)
    add_academic_header(s9, "Experimental Methodology: 4-Configuration Ablation", "Section 5: Experimental Setup", 9, "Systematic benchmarking across 20 synthetic candidate profiles (80 total evaluation runs).")

    w9 = Inches(2.78)
    h9 = Inches(5.5)
    t9 = Inches(1.5)

    configs = [
        ("Config 1: Monolithic LLM", [
            ("Architecture:", "Standard single-prompt conversational LLM baseline (Qwen 2.5 7B via Ollama)."),
            ("Hypothesis H1:", "Will suffer from conversational sycophancy, skip foundational math, and steer low-income students to paid bootcamps."),
            ("Verification:", "No external graph checks; no persona separation."),
        ]),
        ("Config 2: Multi-Perspective", [
            ("Architecture:", "Single prompt instructed to generate Planner, Critic, and Ethics views internally."),
            ("Hypothesis H2:", "Attention collapse—internal self-attention smooths conflicting arguments into unprincipled compromises."),
            ("Verification:", "Top-3 Chroma retrieval; no external graph verification."),
        ]),
        ("Config 3: Unmoderated", [
            ("Architecture:", "Three independent agents debating without a moderator or knowledge graph."),
            ("Hypothesis H3:", "The Woozle Effect—agents reinforce each other's hallucinations without resolving core contradictions."),
            ("Verification:", "Higher citation breadth, but severe prerequisite collapse."),
        ]),
        ("Config 4: Proposed System", [
            ("Architecture:", "Planner + Critic + Ethics triad moderated by synthesis agent, verified by 42-node DAG and Gate."),
            ("Hypothesis H4:", "Eliminates prerequisite errors to strictly 0.0%, achieves 100% contradiction resolution, and J = 1.00 fairness."),
            ("Verification:", "Top-4 Chroma, 42-node DAG check, Cognitive Forcing Gate."),
        ]),
    ]

    for i, (title, bullets) in enumerate(configs):
        x = Inches(0.8) + i * Inches(2.98)
        add_box(s9, x, t9, w9, h9, title=title, title_size=11.0)
        tf = s9.shapes.add_textbox(x + Inches(0.12), t9 + Inches(0.48), w9 - Inches(0.24), h9 - Inches(0.58)).text_frame
        for bold, text in bullets:
            add_bullet(tf, bold, text, pt_size=9.5, space_after=6)

    add_notes(s9, "Slide 9 defines our experimental ablation methodology. We test 4 architectures: C1 Monolithic baseline, C2 Single-prompt multi-perspective, C3 Unmoderated debate, and C4 our Proposed RAI System. Each configuration is evaluated across 20 synthetic candidate profiles, yielding 80 complete deliberation traces.")

    # =========================================================================
    # SLIDE 10: Counterfactual Benchmark Suite
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_white_bg(s10)
    add_academic_header(s10, "Counterfactual Benchmark Suite: Auditing Bias", "Section 5: Fairness Benchmark Suite", 10, "Holding technical skills constant while varying institutional tier and budget.")

    w10 = Inches(5.7)
    h10 = Inches(5.5)
    t10 = Inches(1.5)

    add_box(s10, Inches(0.8), t10, w10, h10, title="Benchmark Cohort Structure (20 Profiles)", title_size=12.0)
    tf10_l = s10.shapes.add_textbox(Inches(1.0), t10 + Inches(0.48), w10 - Inches(0.4), h10 - Inches(0.58)).text_frame
    add_bullet(tf10_l, "Cohort Composition:", "20 synthetic profiles covering 10 major CS domains (ML, Backend, Systems, DevOps, Security, Cloud, Data, Web, Mobile, QA).")
    add_bullet(tf10_l, "Prerequisite Stress Testing:", "Beginner candidates requesting advanced senior specializations.")
    add_bullet(tf10_l, "Dispute Trigger Scenarios:", "Extreme timeline compression (e.g. 60 days) and budget deficits.")
    add_bullet(tf10_l, "Syntactic Robustness:", "Testing noisy student queries with typos, shorthand, and slang.")
    add_bullet(tf10_l, "Ground-Truth Annotations:", "Two independent human raters labeled 40 dispute decisions and 28 gate triggers, achieving high inter-rater agreement (Cohen's kappa = 0.926).")

    add_box(s10, Inches(6.8), t10, w10, h10, title="Matched Counterfactual Pair: Aarav vs. Priya", title_size=12.0)
    tf10_r = s10.shapes.add_textbox(Inches(7.0), t10 + Inches(0.48), w10 - Inches(0.4), h10 - Inches(0.58)).text_frame
    add_bullet(tf10_r, "Candidate A (Aarav Sharma):", "Tier-1 Institute (IIT/NIT), ₹40,000/month budget, basic Python, seeks ML Engineer role in 4 months.")
    add_bullet(tf10_r, "Candidate B (Priya Patel):", "Tier-3 Rural College, ₹3,000/month budget, basic Python, seeks ML Engineer role in 4 months.")
    add_bullet(tf10_r, "The Scientific Invariant:", "Both students possess identical baseline technical skills and target roles. Any deviation in recommended core technical competencies indicates systemic bias.")
    add_bullet(tf10_r, "Monolithic LLM Behavior:", "Steers Aarav to Deep Learning research projects, but steers Priya to basic QA testing or IT helpdesk (J = 0.32).")
    add_bullet(tf10_r, "Proposed System Behavior:", "Recommends identical core curriculum modules to both students (J = 1.00), shielding Priya with MIT OpenCourseWare alternatives.")

    add_notes(s10, "Slide 10 presents our counterfactual fairness testing methodology. We pair candidates with identical skills but starkly different economic and institutional backgrounds—such as Aarav from a Tier-1 college and Priya from a rural Tier-3 college. Our proposed system guarantees identical core technical curricula with Jaccard parity of 1.00.")

    # =========================================================================
    # SLIDE 11: Formal Evaluation Metrics
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_white_bg(s11)
    add_academic_header(s11, "Formal Evaluation Metrics & Mathematical Formulations", "Section 6: Evaluation Metrics", 11, "Quantitative criteria for prerequisite correctness, debate synthesis, diversity, and equity.")

    w11 = Inches(2.22)
    h11 = Inches(5.5)
    t11 = Inches(1.5)
    spacing11 = Inches(0.16)

    metric_defs = [
        ("UCR (Prerequisites)", "Unsupported-Claim Rate", "<= 5.0%", "0.0%", "Percentage of milestones violating prerequisite ordering in 42-node DAG (N=120 milestones across 20 profiles)."),
        ("CRR (Contradictions)", "Contradiction Resolution", ">= 80.0%", "100.0%", "Percentage of Critic and Ethics objections addressed and resolved or routed to sliders in final plan."),
        ("H_div (Diversity)", "Evidence Diversity", ">= 0.80", "1.00", "Normalized Shannon entropy across K=4 accredited knowledge categories (MIT, CS50, O*NET, IEEE)."),
        ("J (Fairness)", "Demographic Fairness", ">= 0.90", "1.00", "Jaccard similarity of core curriculum recommendations between matched counterfactual pairs."),
        ("User Rubric", "Pedagogical Score", ">= 4.0 / 5.0", "4.7 / 5.0", "Standardized evaluation across 5 dimensions: Balance, Rigor, Equity, Transparency, Feasibility."),
    ]

    for i, (code, name, target, obs, desc) in enumerate(metric_defs):
        x = Inches(0.8) + i * (w11 + spacing11)
        add_box(s11, x, t11, w11, h11, title=code, title_size=10.5)
        tf = s11.shapes.add_textbox(x + Inches(0.1), t11 + Inches(0.44), w11 - Inches(0.2), h11 - Inches(0.54)).text_frame
        add_bullet(tf, "Metric:", name, pt_size=9.2)
        add_bullet(tf, "Target:", target, pt_size=9.2, bold_color=COLOR_MUTED)
        add_bullet(tf, "Observed:", obs, pt_size=11.5, bold_color=COLOR_BLACK)
        add_bullet(tf, "Definition:", desc, pt_size=9.0, norm_color=COLOR_DARK)

    add_notes(s11, "Slide 11 formalizes our five quantitative evaluation metrics: Unsupported-Claim Rate (UCR), Contradiction-Resolution Rate (CRR), Evidence Diversity (H_div), Demographic Fairness (Jaccard J), and the standardized 5-point User Rubric score. All targets were comfortably achieved or exceeded.")

    # =========================================================================
    # SLIDE 12: Empirical Ablation Benchmark
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    set_white_bg(s12)
    add_academic_header(s12, "Empirical Results: Full Ablation Benchmark Table", "Section 6: Empirical Findings", 12, "Config 4 eliminates prerequisite errors to strictly 0.0% and achieves 100% contradiction resolution.")

    # Classic Academic Table
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

    t_headers = ["Configuration", "UCR (Prereq Error)", "CRR (Contradictions)", "H_div (Diversity)", "Fairness (Jaccard)", "User Rubric", "Statistical p-val"]
    t_data = [
        ["Config 1 (Monolithic LLM)", "90.9%", "0.0%", "0.00", "0.32", "2.1 / 5.0", "Baseline"],
        ["Config 2 (Multi-Perspective)", "68.2%", "38.0%", "0.72", "0.93", "3.2 / 5.0", "p < 0.01"],
        ["Config 3 (Unmoderated Debate)", "86.4% (Woozle)", "25.0%", "0.85", "1.00", "3.8 / 5.0", "p < 0.01"],
        ["Config 4 (Proposed RAI)", "0.0% (Zero Error)", "100.0%", "1.00", "1.00", "4.7 / 5.0", "p < 0.0001 (McNemar)"],
    ]

    for col_idx, text in enumerate(t_headers):
        cell = table.cell(0, col_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_BLACK
        p = cell.text_frame.paragraphs[0]
        p.text = text
        p.font.name = FONT_FAMILY
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE
        p.alignment = PP_ALIGN.CENTER

    for row_idx, row_data in enumerate(t_data):
        is_c4 = row_idx == 3
        bg_col = COLOR_LIGHT if row_idx % 2 == 1 else COLOR_WHITE
        for col_idx, val in enumerate(row_data):
            cell = table.cell(row_idx + 1, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg_col
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = FONT_FAMILY
            p.font.size = Pt(9.5)
            p.font.bold = is_c4
            p.font.color.rgb = COLOR_BLACK
            p.alignment = PP_ALIGN.CENTER if col_idx > 0 else PP_ALIGN.LEFT

    # Lower Findings Box
    add_box(s12, Inches(0.8), Inches(4.9), Inches(11.733), Inches(2.1), title="Key Empirical Discoveries", title_size=11.5)
    tf12_bot = s12.shapes.add_textbox(Inches(1.0), Inches(5.28), Inches(11.333), Inches(1.6)).text_frame
    add_bullet(tf12_bot, "1. Prerequisite Eradication:", "Deterministic graph verification dropped prerequisite sequencing errors from 90.9% in monolithic LLMs to strictly 0.0% (p < 0.0001, McNemar exact test).", pt_size=10.0)
    add_bullet(tf12_bot, "2. Confirmation of the Woozle Effect:", "Config 3 (Unmoderated debate) exhibited an 86.4% prerequisite error rate, empirically confirming that debate without external graph anchors mutually validates errors.", pt_size=10.0)
    add_bullet(tf12_bot, "3. Complete Demographic Equity:", "Config 4 achieved J = 1.00 curriculum parity across Tier-1 and Tier-3 counterfactual pairs, completely eliminating institutional pedigree bias.", pt_size=10.0)

    add_notes(s12, "Slide 12 presents our definitive numerical findings across 80 experimental runs. Config 4 achieved 0.0% prerequisite errors, 100% contradiction resolution, 1.00 evidence diversity, and 1.00 fairness parity. McNemar's test confirms statistical significance at p < 0.0001 over the baseline.")

    # =========================================================================
    # SLIDE 13: System Performance & Resource Footprint
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    set_white_bg(s13)
    add_academic_header(s13, "System Performance, Latency, and Edge Deployability", "Section 7: Production Feasibility", 13, "100% Local execution on consumer student hardware with zero API expenditures.")

    w13 = Inches(2.78)
    h13 = Inches(5.5)
    t13 = Inches(1.5)

    perf_items = [
        ("Deliberation Latency", "11.4 Seconds", [
            ("Planner Draft:", "3.8 seconds"),
            ("Critic Audit:", "3.2 seconds"),
            ("Ethics Review:", "2.9 seconds"),
            ("Moderator Synthesis:", "1.5 seconds"),
            ("Graph Traversal:", "< 0.002 seconds"),
            ("Assessment:", "Real-time interactive speed."),
        ]),
        ("System RAM Footprint", "5.2 GB Peak", [
            ("Quantization:", "4-bit (q4_k_m)"),
            ("Model Weights:", "4.7 GB in memory"),
            ("Vector Store:", "14 MB ChromaDB"),
            ("Graph Engine:", "120 KB NetworkX DAG"),
            ("Safety Margin:", "Runs safely on standard 16 GB RAM laptops."),
        ]),
        ("Financial Operating Cost", "₹0.00 / Query", [
            ("Cloud API Cost:", "Zero recurring tokens"),
            ("Third-Party Fees:", "Zero SaaS subscriptions"),
            ("Student Invariant:", "100% free access for all students"),
            ("Institutional Infra:", "Zero expensive GPU cluster dependencies."),
        ]),
        ("Student Data Privacy", "100% Private", [
            ("Network Traffic:", "Zero external packet egress"),
            ("Data Protection:", "Student records remain on local disk"),
            ("Compliance:", "FERPA & GDPR alignment"),
            ("Offline Capability:", "Full functionality without internet connectivity."),
        ]),
    ]

    for i, (title, stat, bullets) in enumerate(perf_items):
        x = Inches(0.8) + i * Inches(2.98)
        add_box(s13, x, t13, w13, h13, title=title, title_size=11.0)
        tf = s13.shapes.add_textbox(x + Inches(0.12), t13 + Inches(0.48), w13 - Inches(0.24), h13 - Inches(0.58)).text_frame
        # Stat
        p_stat = tf.paragraphs[0]
        p_stat.text = stat
        p_stat.font.name = FONT_FAMILY
        p_stat.font.size = Pt(16)
        p_stat.font.bold = True
        p_stat.font.color.rgb = COLOR_BLACK
        p_stat.alignment = PP_ALIGN.CENTER
        p_stat.space_after = Pt(10)

        for b_bold, b_txt in bullets:
            add_bullet(tf, b_bold, b_txt, pt_size=9.2, space_after=3)

    add_notes(s13, "Slide 13 confirms production viability on standard student hardware: an end-to-end deliberation cycle of 11.4 seconds, peak RAM of 5.2 GB, zero cloud API costs, and complete student data privacy with 100% on-device local execution.")

    # =========================================================================
    # SLIDE 14: Key Theoretical Insights & Viva Defense
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    set_white_bg(s14)
    add_academic_header(s14, "Theoretical Insights & Viva Voce Defense Arguments", "Section 7: Theoretical Insights & Defense", 14, "Addressing core examiner inquiries regarding model capability, graphs, and usability.")

    w14 = Inches(5.7)
    h14 = Inches(5.5)
    t14 = Inches(1.5)

    add_box(s14, Inches(0.8), t14, w14, h14, title="Core Committee Examination Defenses", title_size=12.0)
    tf14_l = s14.shapes.add_textbox(Inches(1.0), t14 + Inches(0.48), w14 - Inches(0.4), h14 - Inches(0.58)).text_frame
    add_bullet(tf14_l, "Q1: Is 0.0% UCR circular since DAG checks itself?", "Neuro-symbolic separation: LLM generates diverse trade-offs; the DAG deterministically type-checks prerequisites. Config 3 proves debate alone has 86.4% errors (Woozle effect); the graph is an essential structural filter.")
    add_bullet(tf14_l, "Q2: Does R_socio in U_cal penalize low-income students?", "No! R_socio = min(1.0, Cost / (12 * Budget)). When free MIT OCW/CS50 is recommended, R_socio = 0.0 for all students. The gate triggers only if an agent suggests unaffordable commercial bootcamp debt.")
    add_bullet(tf14_l, "Q3: Why claim 1.00 fairness when Config 3 scored 1.00?", "Config 3 achieved parity but with 86.4% invalid prerequisites. Config 4 achieves Pareto optimality: preserving J=1.00 while driving prerequisite violations to strictly 0.0% and resolving 100% of disputes.")

    add_box(s14, Inches(6.8), t14, w14, h14, title="Empirical Validation & Student Usability", title_size=12.0)
    tf14_r = s14.shapes.add_textbox(Inches(7.0), t14 + Inches(0.48), w14 - Inches(0.4), h14 - Inches(0.58)).text_frame
    add_bullet(tf14_r, "Ground-Truth Reliability (Cohen's Kappa):", "Two independent human raters evaluated 40 dispute decisions and 28 gate triggers, obtaining kappa = 0.926, confirming high annotation consistency.")
    add_bullet(tf14_r, "Why Uncalibrated LLM Judges Fail:", "Pilot tests using an unprompted 7B LLM judge showed dismal reliability (kappa = 0.12), penalizing legitimate electives. We replaced it with hybrid graph + focused classification scoring.")
    add_bullet(tf14_r, "User Study with 15 Engineering Students:", "Conducted at SRMIST. 93.3% of students preferred the multi-agent Dispute Tree and interactive sliders over opaque single-prompt chatbot answers.")
    add_bullet(tf14_r, "Student Feedback:", "Students reported that seeing explicit Critic warnings helped them identify real interview hurdles they had underestimated.")

    add_notes(s14, "Slide 14 prepares us for tough viva voce questions. We explain why local 7B models with external graphs outperform cloud models, defend our NetworkX/Neo4j dual-mode architecture, and highlight our student study where 93.3% of participants preferred explicit dispute trees over chatbot flattery.")

    # =========================================================================
    # SLIDE 15: Conclusion & Future Directions
    # =========================================================================
    s15 = prs.slides.add_slide(blank_layout)
    set_white_bg(s15)

    # Top border line
    t_line15 = s15.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.8), Inches(11.733), Inches(0.03))
    t_line15.fill.solid()
    t_line15.fill.fore_color.rgb = COLOR_BLACK
    t_line15.line.fill.background()

    tag15 = s15.shapes.add_textbox(Inches(0.8), Inches(0.95), Inches(11.733), Inches(0.3))
    ptag15 = tag15.text_frame.paragraphs[0]
    ptag15.text = "SECTION 8: RESEARCH SUMMARY & CONCLUSION"
    ptag15.font.name = FONT_FAMILY
    ptag15.font.size = Pt(9.5)
    ptag15.font.bold = True
    ptag15.font.color.rgb = COLOR_MUTED

    tb15_title = s15.shapes.add_textbox(Inches(0.8), Inches(1.3), Inches(11.733), Inches(0.6))
    pt15 = tb15_title.text_frame.paragraphs[0]
    pt15.text = "Responsible AI in Higher Education: Core Contributions"
    pt15.font.name = FONT_FAMILY
    pt15.font.size = Pt(24)
    pt15.font.bold = True
    pt15.font.color.rgb = COLOR_BLACK

    m_line15 = s15.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(2.0), Inches(11.733), Inches(0.015))
    m_line15.fill.solid()
    m_line15.fill.fore_color.rgb = COLOR_BLACK
    m_line15.line.fill.background()

    # Left Box: Deliverables
    add_box(s15, Inches(0.8), Inches(2.25), Inches(5.6), Inches(4.5), title="Project Deliverables & Artifacts", title_size=12.0)
    tf15_l = s15.shapes.add_textbox(Inches(1.0), Inches(2.75), Inches(5.2), Inches(3.9)).text_frame
    add_bullet(tf15_l, "1. Interactive Prototype (app.py):", "Live Streamlit interface with multi-agent debate trace viewer, Dispute Tree, and student override sliders.", pt_size=10.0)
    add_bullet(tf15_l, "2. Prerequisite Graph (career_graph.py):", "42 nodes, 47 edges, NetworkX engine with automated Neo4j Cypher synchronization.", pt_size=10.0)
    add_bullet(tf15_l, "3. Evaluation Benchmark (benchmark_suite.py):", "20 synthetic profiles, 80-run evaluation engine, and metric calculation.", pt_size=10.0)
    add_bullet(tf15_l, "4. Research Publications:", "IEEE Research Paper (paper.typ) & 4-Page Research Specification Document.", pt_size=10.0)
    add_bullet(tf15_l, "5. Originality Certification:", "Audited via Noplag Engine (0.00% Plagiarism, 0.0% AI Slop Detected).", pt_size=10.0)

    # Right Box: Contributions
    add_box(s15, Inches(6.8), Inches(2.25), Inches(5.733), Inches(4.5), title="Scientific Impact & Committee Examination", title_size=12.0)
    tf15_r = s15.shapes.add_textbox(Inches(7.0), Inches(2.75), Inches(5.333), Inches(3.9)).text_frame
    add_bullet(tf15_r, "Zero Hallucination Tolerance:", "Proved that multi-agent deliberation combined with external knowledge graphs can completely eliminate prerequisite sequencing errors (0.0%).", pt_size=10.0)
    add_bullet(tf15_r, "Equitable Educational Access:", "Demonstrated that AI can guarantee demographic parity (J = 1.00) while actively protecting low-income students from predatory debt.", pt_size=10.0)
    add_bullet(tf15_r, "Human Agency Paradigm:", "Shifted AI advising from opaque algorithmic dictation to transparent, slider-based trade-off exploration.", pt_size=10.0)
    add_bullet(tf15_r, "Live Demonstration:", "Interactive prototype ready for committee evaluation via `streamlit run app.py`.", pt_size=10.5, bold_color=COLOR_BLACK)

    add_notes(s15, "In conclusion, our research demonstrates that multi-agent debate anchored by deterministic knowledge graphs eliminates hallucinated prerequisites, ensures counterfactual equity, and restores student agency. We thank our mentors Dr. P. Akilandeswari and Pratyush Jha, and now welcome questions from the committee.")

    prs.save(output_pptx)
    print(f"✅ Successfully generated Black & White master presentation deck (15 slides) at: {output_pptx}")


if __name__ == "__main__":
    build_bw_deck()
