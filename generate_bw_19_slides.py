"""
Generate Pure Black & White Master Presentation Deck (19 Slides)
Directly implementing the user's 19-slide content into a pure monochrome academic template.
Theme: 100% Black & White (No colors, pure white backgrounds, crisp black typography, 
structured cards, inverted black section badges, 16:9 widescreen layout).
"""

import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# 100% Black and White Color Palette
COLOR_BLACK = RGBColor(0, 0, 0)
COLOR_WHITE = RGBColor(255, 255, 255)
COLOR_DARK = RGBColor(35, 35, 35)
COLOR_MUTED = RGBColor(90, 90, 90)
COLOR_LIGHT_BG = RGBColor(248, 248, 248)
COLOR_CARD_BORDER = RGBColor(200, 200, 200)
COLOR_BLACK_BORDER = RGBColor(0, 0, 0)

FONT_FAMILY = "Liberation Sans"

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    def set_white_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = COLOR_WHITE
        bg.line.fill.background()
        return bg

    def add_header(slide, tag, title, takeaway=None, slide_num=None):
        # Top black rule
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.45), Inches(11.733), Inches(0.02))
        line.fill.solid()
        line.fill.fore_color.rgb = COLOR_BLACK
        line.line.fill.background()

        # Tag + Slide Number
        box_tag = slide.shapes.add_textbox(Inches(0.8), Inches(0.55), Inches(11.733), Inches(0.3))
        p_tag = box_tag.text_frame.paragraphs[0]
        p_tag.text = tag.upper()
        p_tag.font.name = FONT_FAMILY
        p_tag.font.size = Pt(8.5)
        p_tag.font.bold = True
        p_tag.font.color.rgb = COLOR_MUTED

        if slide_num:
            # Right-aligned slide number
            box_num = slide.shapes.add_textbox(Inches(10.5), Inches(0.55), Inches(2.033), Inches(0.3))
            p_num = box_num.text_frame.paragraphs[0]
            p_num.text = f"{slide_num} / 19"
            p_num.font.name = FONT_FAMILY
            p_num.font.size = Pt(8.5)
            p_num.font.bold = True
            p_num.font.color.rgb = COLOR_MUTED
            p_num.alignment = PP_ALIGN.RIGHT

        # Title
        box_t = slide.shapes.add_textbox(Inches(0.8), Inches(0.82), Inches(11.733), Inches(0.5))
        p_t = box_t.text_frame.paragraphs[0]
        p_t.text = title
        p_t.font.name = FONT_FAMILY
        p_t.font.size = Pt(17)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_BLACK

        # Takeaway / Subtitle
        if takeaway:
            p_sub = box_t.text_frame.add_paragraph()
            p_sub.text = takeaway
            p_sub.font.name = FONT_FAMILY
            p_sub.font.size = Pt(10)
            p_sub.font.italic = True
            p_sub.font.color.rgb = COLOR_DARK
            p_sub.space_before = Pt(2)

    def add_card(slide, left, top, width, height, title=None, bg_color=COLOR_WHITE, border_color=COLOR_BLACK_BORDER, border_width=1.0):
        card = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(border_width)

        tf = None
        if title:
            # Title banner box inside
            t_banner = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, Inches(0.36))
            t_banner.fill.solid()
            t_banner.fill.fore_color.rgb = COLOR_BLACK
            t_banner.line.fill.background()
            p = t_banner.text_frame.paragraphs[0]
            p.text = title.upper()
            p.font.name = FONT_FAMILY
            p.font.size = Pt(9.0)
            p.font.bold = True
            p.font.color.rgb = COLOR_WHITE
            p.alignment = PP_ALIGN.CENTER
            
            tf_box = slide.shapes.add_textbox(left + Inches(0.12), top + Inches(0.40), width - Inches(0.24), height - Inches(0.44))
            tf = tf_box.text_frame
            tf.word_wrap = True
        else:
            tf_box = slide.shapes.add_textbox(left + Inches(0.12), top + Inches(0.12), width - Inches(0.24), height - Inches(0.24))
            tf = tf_box.text_frame
            tf.word_wrap = True
        return tf

    def add_bullet(tf, bold_txt, norm_txt, pt_size=9.2, space_after=4, bold_color=COLOR_BLACK, norm_color=COLOR_DARK):
        p = tf.add_paragraph() if len(tf.paragraphs[0].text) > 0 else tf.paragraphs[0]
        p.space_after = Pt(space_after)
        p.line_spacing = 1.15
        if bold_txt:
            run_b = p.add_run()
            run_b.text = bold_txt + " " if not bold_txt.endswith(" ") else bold_txt
            run_b.font.name = FONT_FAMILY
            run_b.font.size = Pt(pt_size)
            run_b.font.bold = True
            run_b.font.color.rgb = bold_color
        if norm_txt:
            run_n = p.add_run()
            run_n.text = norm_txt
            run_n.font.name = FONT_FAMILY
            run_n.font.size = Pt(pt_size)
            run_n.font.bold = False
            run_n.font.color.rgb = norm_color

    # =========================================================================
    # SLIDE 1: Cover Title Slide
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_white_bg(s1)

    # Frame lines
    top_line = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.8), Inches(11.733), Inches(0.04))
    top_line.fill.solid()
    top_line.fill.fore_color.rgb = COLOR_BLACK
    top_line.line.fill.background()

    tag1 = s1.shapes.add_textbox(Inches(0.8), Inches(0.95), Inches(11.733), Inches(0.35))
    ptag1 = tag1.text_frame.paragraphs[0]
    ptag1.text = "RESPONSIBLE AI  ·  MULTI-PERSONA DIALECTIC ADVISORY"
    ptag1.font.name = FONT_FAMILY
    ptag1.font.size = Pt(10.5)
    ptag1.font.bold = True
    ptag1.font.color.rgb = COLOR_MUTED

    title1 = s1.shapes.add_textbox(Inches(0.8), Inches(1.35), Inches(11.733), Inches(1.3))
    pt1 = title1.text_frame.paragraphs[0]
    pt1.text = "Debate-Based Career Guidance Agent with Complementary Personas"
    pt1.font.name = FONT_FAMILY
    pt1.font.size = Pt(24)
    pt1.font.bold = True
    pt1.font.color.rgb = COLOR_BLACK

    psub1 = title1.text_frame.add_paragraph()
    psub1.text = "Planner, Critic and Ethics-Reviewer personas debate public course and role data, with a heuristic uncertainty gate and human override"
    psub1.font.name = FONT_FAMILY
    psub1.font.size = Pt(12)
    psub1.font.italic = True
    psub1.font.color.rgb = COLOR_DARK
    psub1.space_before = Pt(6)

    # Two metadata cards
    c1_tf = add_card(s1, Inches(0.8), Inches(3.1), Inches(5.7), Inches(3.6), title="Project Academic Profile")
    add_bullet(c1_tf, "Presented by:", "Parth Gupta, B.Tech CSE, SRMIST Kattankulathur", pt_size=10.5, space_after=8)
    add_bullet(c1_tf, "Academic Mentorship:", "Dr. P. Akilandeswari (Faculty) | Pratyush Jha (Industry)", pt_size=10.5, space_after=8)
    add_bullet(c1_tf, "Research Domain:", "Responsible AI, Multi-Agent Debate Systems, Educational Technology", pt_size=10.5, space_after=8)
    add_bullet(c1_tf, "Evaluation Session:", "Academic Evaluation 2025–2026", pt_size=10.5, space_after=8)
    add_bullet(c1_tf, "Empirical Status:", "Pilot study on 20 synthetic counterfactual candidate profiles", pt_size=10.5, space_after=8)

    c2_tf = add_card(s1, Inches(6.8), Inches(3.1), Inches(5.7), Inches(3.6), title="System Implementation Stack")
    add_bullet(c2_tf, "Inference Engine:", "Qwen models (qwen2.5:7b, qwen3:4b-fast, qwen2:0.5b) run locally via Ollama", pt_size=10.5, space_after=8)
    add_bullet(c2_tf, "Deliberation Harness:", "Python multi-agent deliberation loop (Planner, Critic, Ethics, Moderator)", pt_size=10.5, space_after=8)
    add_bullet(c2_tf, "Knowledge Grounding:", "ChromaDB vector store + Neo4j / NetworkX 42-node prerequisite DAG", pt_size=10.5, space_after=8)
    add_bullet(c2_tf, "User Interface:", "Streamlit deliberation trace viewer with human override sliders", pt_size=10.5, space_after=8)
    add_bullet(c2_tf, "Execution Model:", "100% on-device private execution with zero cloud API token cost", pt_size=10.5, space_after=8)

    # Bottom rule
    b_line = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(6.9), Inches(11.733), Inches(0.02))
    b_line.fill.solid()
    b_line.fill.fore_color.rgb = COLOR_BLACK
    b_line.line.fill.background()

    # =========================================================================
    # SLIDE 2: Abstract: Grounded Dialectics for Advisory
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_white_bg(s2)
    add_header(s2, "SECTION 1 · ABSTRACT", "Abstract: Grounded Dialectics for Advisory", "Surface disagreement, check prerequisites, keep the student in control", slide_num=2)

    w2 = Inches(3.75)
    h2 = Inches(3.2)
    t2 = Inches(1.6)

    tf2_1 = add_card(s2, Inches(0.8), t2, w2, h2, title="The Advisory Problem")
    add_bullet(tf2_1, "Sycophancy:", "LLMs tend to agree with users [5], including on unrealistic goals.")
    add_bullet(tf2_1, "Flattened trade-offs:", "One pass can blur competing options and conceal hidden trade-offs.")
    add_bullet(tf2_1, "Steering risk:", "Advice may shift with institution or income cues, causing disparate recommendations.")

    tf2_2 = add_card(s2, Inches(4.78), t2, w2, h2, title="Our Approach")
    add_bullet(tf2_2, "Three personas:", "Planner (growth), Critic (rigor), Ethics-Reviewer (equity, debt).")
    add_bullet(tf2_2, "Grounding:", "Chroma vector retrieval over accredited university course syllabi and O*NET role data.")
    add_bullet(tf2_2, "Check:", "42-node author-curated prerequisite Directed Acyclic Graph (DAG) in pure Python.")

    tf2_3 = add_card(s2, Inches(8.76), t2, w2, h2, title="Evaluation Scope")
    add_bullet(tf2_3, "Configurations:", "Four configurations tested across five author-defined metrics.")
    add_bullet(tf2_3, "Pilot dataset:", "20 synthetic profiles (10 matched counterfactual pairs).")
    add_bullet(tf2_3, "Gate threshold:", "Human review triggered if prerequisite violations exist or uncertainty score >= 0.45.")

    # Lower findings box
    tf2_bot = add_card(s2, Inches(0.8), Inches(5.0), Inches(11.733), Inches(1.9), title="Pilot Findings (Single Run, Synthetic Data, Preliminary)")
    add_bullet(tf2_bot, "1. Prerequisite Integrity:", "The full system emits no prerequisite violations (0.0%). This holds by construction of the DAG check, not as an independent test.", pt_size=9.5)
    add_bullet(tf2_bot, "2. Counterfactual Parity:", "Core milestones match across matched pairs (Jaccard 1.00); the unmoderated triad also reaches 1.00.", pt_size=9.5)
    add_bullet(tf2_bot, "3. Decision Agency:", "Dispute trees and the override gate pass unresolved trade-offs directly to the student. (See Threats to Validity).", pt_size=9.5)

    # =========================================================================
    # SLIDE 3: Flattery vs. Grounded Dialectics
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_white_bg(s3)
    add_header(s3, "SECTION 2 · INTRODUCTION", "Flattery vs. Grounded Dialectics", "Contrasting a typical single-pass LLM failure pattern with our pipeline", slide_num=3)

    w3 = Inches(5.7)
    h3 = Inches(5.3)
    t3 = Inches(1.6)

    tf3_l = add_card(s3, Inches(0.8), t3, w3, h3, title="Single-Pass LLM (Failure Pattern)")
    add_bullet(tf3_l, "1. Unrealistic Request:", "\"Staff ML Engineer in 4 months via commercial bootcamp.\"", pt_size=10.0, space_after=8)
    add_bullet(tf3_l, "2. Agreeableness Bias:", "Preference-tuned models tend to affirm user views [5], validating unfeasible timelines without pushback.", pt_size=10.0, space_after=8)
    add_bullet(tf3_l, "3. Skipped Prerequisites:", "Omits linear algebra, probability, and OS internals; jumps directly to PyTorch and Transformers.", pt_size=10.0, space_after=8)
    add_bullet(tf3_l, "Severe Student Risk:", "Bootcamp loan debt (₹1,20,000) followed by immediate failure in technical screening interviews.", pt_size=10.5, bold_color=COLOR_BLACK, space_after=8)
    add_bullet(tf3_l, "Structural Cause:", "Probabilistic next-token generators optimize for semantic coherence rather than topological dependency validity.", pt_size=9.5)

    tf3_r = add_card(s3, Inches(6.8), t3, w3, h3, title="Proposed Grounded Architecture")
    add_bullet(tf3_r, "1. Intake and Grounding:", "Retrieve accredited course modules and O*NET roles from ChromaDB vector store.", pt_size=10.0, space_after=8)
    add_bullet(tf3_r, "2. Persona Friction:", "Planner (constructive) vs. Critic (skeptical) vs. Ethics-Reviewer (equity & debt safeguards).", pt_size=10.0, space_after=8)
    add_bullet(tf3_r, "3. DAG Traversal:", "NetworkX ancestor check detects missing prerequisite hops; flags Delta_prereq deterministically.", pt_size=10.0, space_after=8)
    add_bullet(tf3_r, "Grounded Outcome:", "Dispute tree, heuristic uncertainty score, and human override sliders restore student decision agency.", pt_size=10.5, bold_color=COLOR_BLACK, space_after=8)
    add_bullet(tf3_r, "Safe Resolution:", "Zero-debt roadmaps backed by MIT OpenCourseWare, CS50, and verifiable GitHub projects.", pt_size=9.5)

    # =========================================================================
    # SLIDE 4: Research Questions and Scope
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_white_bg(s4)
    add_header(s4, "SECTION 2 · INTRODUCTION", "Research Questions and Scope", "Five research questions map one-to-one to five metrics", slide_num=4)

    tf4_l = add_card(s4, Inches(0.8), Inches(1.6), Inches(6.2), Inches(5.3), title="Five Research Questions (RQ1 - RQ5)")
    add_bullet(tf4_l, "RQ1 (Evidence Diversity):", "Does vector retrieval from accredited curricula broaden the range of academic and industry domains cited in roadmaps?", pt_size=9.8, space_after=8)
    add_bullet(tf4_l, "RQ2 (Contradiction Handling):", "Does a dedicated Moderator agent map Critic and Ethics concerns into explicit decision forks rather than averaging them away?", pt_size=9.8, space_after=8)
    add_bullet(tf4_l, "RQ3 (Prerequisite Grounding):", "Does deterministic DAG verification significantly reduce prerequisite-violating milestones compared to unconstrained LLMs?", pt_size=9.8, space_after=8)
    add_bullet(tf4_l, "RQ4 (Demographic Parity):", "Do core technical recommendations stay stable across matched counterfactual pairs varying only by institution tier and budget?", pt_size=9.8, space_after=8)
    add_bullet(tf4_l, "RQ5 (Decision Support):", "Do evaluators rate the full system higher on balance, rigor, equity, transparency, and human override capability?", pt_size=9.8, space_after=8)

    tf4_r = add_card(s4, Inches(7.3), Inches(1.6), Inches(5.2), Inches(5.3), title="Implementation Stack & Principles")
    add_bullet(tf4_r, "Language Models:", "qwen3:4b-fast, qwen3:4b, qwen2:0.5b run locally via Ollama.", pt_size=9.5, space_after=6)
    add_bullet(tf4_r, "Deliberation Harness:", "Pure-Python orchestration loop emitting structured JSON schemas.", pt_size=9.5, space_after=6)
    add_bullet(tf4_r, "Graph Grounding:", "Neo4j with NetworkX fallback; automated Cypher export.", pt_size=9.5, space_after=6)
    add_bullet(tf4_r, "Retrieval & UI:", "ChromaDB vector database and Streamlit trace viewer.", pt_size=9.5, space_after=8)
    add_bullet(tf4_r, "Four Core Principles:", "", pt_size=9.5)
    add_bullet(tf4_r, "  (1)", "Hear several distinct perspectives before synthesis.", pt_size=9.0)
    add_bullet(tf4_r, "  (2)", "Show disagreement explicitly instead of averaging it away.", pt_size=9.0)
    add_bullet(tf4_r, "  (3)", "Surface a heuristic uncertainty score to gate automated release.", pt_size=9.0)
    add_bullet(tf4_r, "  (4)", "Ensure the student or human counselor always makes the final call.", pt_size=9.0)

    # =========================================================================
    # SLIDE 5: Three Theoretical Pillars
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_white_bg(s5)
    add_header(s5, "SECTION 3 · LITERATURE SURVEY", "Three Theoretical Pillars", "Debate, grounding, and fairness with human agency", slide_num=5)

    w5 = Inches(3.75)
    h5 = Inches(5.3)
    t5 = Inches(1.6)

    tf5_1 = add_card(s5, Inches(0.8), t5, w5, h5, title="1. Multi-Agent Debate")
    add_bullet(tf5_1, "Du et al. [1]:", "Demonstrated that multi-agent debate improves factuality and logical reasoning across multiple NLP reasoning tasks.", pt_size=9.5, space_after=8)
    add_bullet(tf5_1, "Liang et al. [2]:", "Showed that conversational debate encourages divergent thinking and surfaces multiple candidate perspectives.", pt_size=9.5, space_after=8)
    add_bullet(tf5_1, "Smit et al. Gap [3]:", "Critiqued uncurated debate, proving it frequently degenerates into expensive majority voting without external grounding.", pt_size=9.5, space_after=8)
    add_bullet(tf5_1, "Our Synthesis:", "We constrain debate using adversarial persona contracts with opposing objective functions.", pt_size=9.2)

    tf5_2 = add_card(s5, Inches(4.78), t5, w5, h5, title="2. Grounding and RAG")
    add_bullet(tf5_2, "ACM/IEEE CS2023 [4]:", "Curricular knowledge areas informed our graph; prerequisite edges are author-curated based on official guidelines.", pt_size=9.5, space_after=8)
    add_bullet(tf5_2, "O*NET & BLS Data:", "Official U.S. occupational taxonomies used as industry role-skill proxies for salary bands and competencies.", pt_size=9.5, space_after=8)
    add_bullet(tf5_2, "Deterministic DAG:", "In-memory topological sort catches sequencing errors that probabilistic LLM token prediction misses.", pt_size=9.5, space_after=8)
    add_bullet(tf5_2, "Neuro-Symbolic Link:", "Combines semantic flexibility with rigid graph invariants.", pt_size=9.2)

    tf5_3 = add_card(s5, Inches(8.76), t5, w5, h5, title="3. Fairness & Agency")
    add_bullet(tf5_3, "Geyik et al. [7]:", "Fairness-aware ranking frameworks establishing demographic parity in recommendation systems.", pt_size=9.5, space_after=8)
    add_bullet(tf5_3, "Buçinca et al. [8]:", "Cognitive forcing functions designed to disrupt passive heuristics and reduce overreliance on automated AI advice.", pt_size=9.5, space_after=8)
    add_bullet(tf5_3, "Sharma [5] & Xiong [6]:", "Highlight pervasive LLM sycophancy and weak verbalized confidence; justifies structural gating signals.", pt_size=9.5, space_after=8)
    add_bullet(tf5_3, "Human Invariant:", "Preserves student autonomy through interactive trade-off sliders.", pt_size=9.2)

    # =========================================================================
    # SLIDE 6: Critique of Debate and Our Response
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_white_bg(s6)
    add_header(s6, "SECTION 3 · LITERATURE SURVEY", "Critique of Debate and Our Response", "Smit et al. [3] and what we do and do not address", slide_num=6)

    w6 = Inches(5.7)
    h6 = Inches(5.3)
    t6 = Inches(1.6)

    tf6_l = add_card(s6, Inches(0.8), t6, w6, h6, title="The Smit et al. Critique [3]")
    add_bullet(tf6_l, "1. Majority-Voting Equivalence:", "Uncurated multi-agent debate often matches cheaper majority voting or self-consistency, consuming extra tokens without better outcomes.", pt_size=9.8, space_after=8)
    add_bullet(tf6_l, "2. Shared Priors & Blindspots:", "When agents stem from the same model family, they share systematic inductive biases and common misconceptions.", pt_size=9.8, space_after=8)
    add_bullet(tf6_l, "3. Error Amplification (Woozle Effect):", "Confident but incorrect agents can persuade other agents to adopt flawed conclusions during free-form dialogue.", pt_size=9.8, space_after=8)
    add_bullet(tf6_l, "Application to Our System:", "Our personas share the local Qwen model family, meaning shared priors are only partially mitigated by prompt differentiation.", pt_size=9.8, bold_color=COLOR_BLACK)

    tf6_r = add_card(s6, Inches(6.8), t6, w6, h6, title="Our Architectural Countermeasures")
    add_bullet(tf6_r, "1. External Symbolic Grounding:", "Retrieved Chroma documents and the 42-node DAG supply deterministic signals completely independent of model weights.", pt_size=9.8, space_after=8)
    add_bullet(tf6_r, "2. Role-Differentiated Prompts:", "Adversarial prompts with opposing objectives (growth vs. skepticism vs. debt); same model, so partial mitigation only.", pt_size=9.8, space_after=8)
    add_bullet(tf6_r, "3. Dispute Trees:", "Disagreements are structured as explicit trade-off forks, never voted away by majority consensus.", pt_size=9.8, space_after=8)
    add_bullet(tf6_r, "4. Human Override Gate:", "Unresolved trade-offs and uncertainty pass directly to the student and counselor.", pt_size=9.8, space_after=8)
    add_bullet(tf6_r, "Not Yet Tested (Honest Scope):", "A compute-matched self-consistency or majority-vote baseline remains future work.", pt_size=9.5, bold_color=COLOR_MUTED)

    # =========================================================================
    # SLIDE 7: Positioning Against Prior Work
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_white_bg(s7)
    add_header(s7, "SECTION 3 · LITERATURE SURVEY", "Positioning Against Prior Work", "Scope comparison, not a performance comparison", slide_num=7)

    # Academic Comparison Table
    rows = 6
    cols = 6
    t_shape = s7.shapes.add_table(rows, cols, Inches(0.8), Inches(1.6), Inches(11.733), Inches(3.8))
    table = t_shape.table

    table.columns[0].width = Inches(2.2)
    table.columns[1].width = Inches(1.8)
    table.columns[2].width = Inches(1.9)
    table.columns[3].width = Inches(2.0)
    table.columns[4].width = Inches(1.9)
    table.columns[5].width = Inches(1.933)

    headers7 = ["Prior Work", "Multi-Agent Debate", "External Data Grounding", "Fairness Audit", "Human in the Loop", "Career-Advice Domain"]
    data7 = [
        ["Du et al. [1]", "Yes", "No", "No", "No", "No"],
        ["Liang et al. [2]", "Yes", "No", "No", "No", "No"],
        ["Geyik et al. [7]", "No", "N/A", "Yes (ranking parity)", "No", "Partly (talent search)"],
        ["Buçinca et al. [8]", "N/A", "N/A", "N/A", "Yes (cognitive forcing)", "No"],
        ["This Work", "Yes (3 personas + Mod)", "Yes (Chroma + DAG)", "Yes (synthetic pairs)", "Yes (override gate)", "Yes"],
    ]

    for col_idx, text in enumerate(headers7):
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

    for row_idx, row in enumerate(data7):
        is_this_work = row_idx == 4
        bg_col = COLOR_LIGHT_BG if row_idx % 2 == 1 else COLOR_WHITE
        for col_idx, val in enumerate(row):
            cell = table.cell(row_idx + 1, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg_col
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = FONT_FAMILY
            p.font.size = Pt(9.2)
            p.font.bold = is_this_work
            p.font.color.rgb = COLOR_BLACK
            p.alignment = PP_ALIGN.CENTER if col_idx > 0 else PP_ALIGN.LEFT

    tf7_foot = add_card(s7, Inches(0.8), Inches(5.6), Inches(11.733), Inches(1.3), border_color=COLOR_CARD_BORDER)
    add_bullet(tf7_foot, "Scope Disclaimer:", "N/A indicates outside the prior work's intended scientific scope. Prior works target distinct research problems; this table clarifies domain coverage and architectural dimensions, not competitive performance superiority.", pt_size=9.2)

    # =========================================================================
    # SLIDE 8: End-to-End Decision Flow
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_white_bg(s8)
    add_header(s8, "SECTION 4 · ARCHITECTURE", "End-to-End Decision Flow", "Intake, retrieval, deliberation, prerequisite check, then a gate", slide_num=8)

    # 5 Sequential Process Cards across width
    w8_step = Inches(2.22)
    h8_step = Inches(2.2)
    t8_step = Inches(1.6)
    gap8 = Inches(0.16)

    steps8 = [
        ("1. Intake", "Skills, Target Role, Timeline, Monthly Budget constraints."),
        ("2. Retrieval", "ChromaDB: Accredited university course modules and O*NET roles."),
        ("3. Triad", "Local Qwen: Planner (growth), Critic (rigor), Ethics (equity)."),
        ("4. Moderator + DAG", "Checks prerequisite reachability, extracts active disputes."),
        ("5. Gate", "Violations > 0 or heuristic uncertainty score >= 0.45?"),
    ]

    for i, (title, desc) in enumerate(steps8):
        x = Inches(0.8) + i * (w8_step + gap8)
        tf = add_card(s8, x, t8_step, w8_step, h8_step, title=title)
        add_bullet(tf, "", desc, pt_size=9.2, space_after=4)

    # Two Branch Outcome Cards Below
    w8_bot = Inches(5.7)
    h8_bot = Inches(2.9)
    t8_bot = Inches(4.0)

    tf8_l = add_card(s8, Inches(0.8), t8_bot, w8_bot, h8_bot, title="Gate Fires: Human Override Path")
    add_bullet(tf8_l, "Trigger Condition:", "Prerequisite violations > 0 OR heuristic score >= 0.45.", pt_size=9.5, bold_color=COLOR_BLACK)
    add_bullet(tf8_l, "Dispute Tree:", "Surfaces explicit decision forks across speed, depth, and financial risk.", pt_size=9.2)
    add_bullet(tf8_l, "Interactive Sliders:", "Student or counselor re-weights speed, prerequisite rigor, and debt avoidance in Streamlit.", pt_size=9.2)
    add_bullet(tf8_l, "Agency Invariant:", "The system ceases autonomous assertion and defers final roadmap selection to the human user.", pt_size=9.2)

    tf8_r = add_card(s8, Inches(6.8), t8_bot, w8_bot, h8_bot, title="Gate Clear: Balanced Roadmap Path")
    add_bullet(tf8_r, "Execution State:", "Prerequisite violations == 0 AND heuristic score < 0.45.", pt_size=9.5, bold_color=COLOR_BLACK)
    add_bullet(tf8_r, "Sequenced Milestones:", "Roadmap ordered so every included curriculum node meets its prerequisite edges.", pt_size=9.2)
    add_bullet(tf8_r, "Verified Citations:", "Every milestone linked to retrieved course syllabi and official O*NET skill entries.", pt_size=9.2)
    add_bullet(tf8_r, "Zero-Debt Guarantee:", "Prioritizes free accredited open courseware within student budget constraints.", pt_size=9.2)

    # =========================================================================
    # SLIDE 9: Complementary Personas
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_white_bg(s9)
    add_header(s9, "SECTION 4 · ARCHITECTURE", "Complementary Personas", "Differentiated prompts with opposing objectives", slide_num=9)

    w9 = Inches(3.75)
    h9 = Inches(5.3)
    t9 = Inches(1.6)

    tf9_1 = add_card(s9, Inches(0.8), t9, w9, h9, title="Planner Persona")
    add_bullet(tf9_1, "Analytical Lens:", "Constructive execution, milestone decomposition, time-to-market speed.", pt_size=9.5, space_after=8)
    add_bullet(tf9_1, "Grounding:", "Maps career goals to concrete course modules (e.g. CS101, CS201, CS330) and O*NET roles.", pt_size=9.5, space_after=8)
    add_bullet(tf9_1, "Core Function:", "Builds actionable forward-moving pathways and actively avoids analysis paralysis.", pt_size=9.5, space_after=8)
    add_bullet(tf9_1, "Potential Blindspot:", "Tendency to bypass foundational prerequisites in favor of exciting portfolio projects.", pt_size=9.2)

    tf9_2 = add_card(s9, Inches(4.78), t9, w9, h9, title="Critic Persona")
    add_bullet(tf9_2, "Analytical Lens:", "Adversarial stress-testing, prerequisite skepticism, and screening realism.", pt_size=9.5, space_after=8)
    add_bullet(tf9_2, "Core Priorities:", "Linear algebra, probability, OS memory management, concurrency depth, and enterprise screening barriers.", pt_size=9.5, space_after=8)
    add_bullet(tf9_2, "Core Function:", "Warns against attempting advanced roles without foundational mastery; flags shallow tutorial projects.", pt_size=9.5, space_after=8)
    add_bullet(tf9_2, "Potential Blindspot:", "Can produce hyper-conservative, multi-year timelines that discourage motivated students.", pt_size=9.2)

    tf9_3 = add_card(s9, Inches(8.76), t9, w9, h9, title="Ethics-Reviewer Persona")
    add_bullet(tf9_3, "Default Safeguard:", "Flags high-cost commercial debt and enforces free open-source educational resources.", pt_size=9.5, space_after=8)
    add_bullet(tf9_3, "Parity Focus:", "Suggests verifiable open-source contributions to offset institutional tier and pedigree bias.", pt_size=9.5, space_after=8)
    add_bullet(tf9_3, "Realistic Caveat:", "Explicitly acknowledges that free open courseware still incurs real costs in time, devices, and internet connectivity.", pt_size=9.5, space_after=8)
    add_bullet(tf9_3, "Override Rule:", "Student can override paid course warnings if all commercial costs are fully disclosed.", pt_size=9.2)

    # =========================================================================
    # SLIDE 10: Career-Skill Graph: 16 of 42 Nodes Shown
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_white_bg(s10)
    add_header(s10, "SECTION 4 · ARCHITECTURE", "Career-Skill Graph: 16 of 42 Nodes Shown", "Four tracks of the author-curated prerequisite DAG", slide_num=10)

    w10 = Inches(2.78)
    h10 = Inches(3.8)
    t10 = Inches(1.6)

    tf10_1 = add_card(s10, Inches(0.8), t10, w10, h10, title="Track 1: DSA & Math")
    add_bullet(tf10_1, "1. Discrete Math:", "Logic, sets, proofs, graph theory.")
    add_bullet(tf10_1, "2. Python / C Basics:", "Syntax, data types, control flow.")
    add_bullet(tf10_1, "3. Data Structures:", "Linked lists, trees, heaps, graphs.")
    add_bullet(tf10_1, "4. Advanced Algorithms:", "Dynamic programming, flows, NP.")

    tf10_2 = add_card(s10, Inches(3.78), t10, w10, h10, title="Track 2: Systems & OS")
    add_bullet(tf10_2, "1. C Pointers & Memory:", "Stack, heap, pointer arithmetic.")
    add_bullet(tf10_2, "2. Computer Architecture:", "Registers, ALU, caches, pipelines.")
    add_bullet(tf10_2, "3. Operating Systems:", "Processes, threads, paging, IPC.")
    add_bullet(tf10_2, "4. Distributed Systems:", "Raft, Paxos, RPCs, replication.")

    tf10_3 = add_card(s10, Inches(6.76), t10, w10, h10, title="Track 3: Web & Cloud")
    add_bullet(tf10_3, "1. HTML / CSS / JS:", "DOM, async events, browser API.")
    add_bullet(tf10_3, "2. Backend APIs:", "FastAPI, Django, REST routing.")
    add_bullet(tf10_3, "3. Docker Containers:", "Namespaces, cgroups, images.")
    add_bullet(tf10_3, "4. System Design / CI:", "Load balancing, sharding, CI/CD.")

    tf10_4 = add_card(s10, Inches(9.74), t10, w10, h10, title="Track 4: ML & AI")
    add_bullet(tf10_4, "1. Linear Algebra:", "Eigenvalues, matrices, probability.")
    add_bullet(tf10_4, "2. Data Analysis:", "Pandas, NumPy, data cleaning.")
    add_bullet(tf10_4, "3. ML Foundations:", "Loss functions, gradient descent.")
    add_bullet(tf10_4, "4. Deep Learning:", "Transformers, backprop, LLMs.")

    tf10_bot = add_card(s10, Inches(0.8), Inches(5.6), Inches(11.733), Inches(1.3), border_color=COLOR_BLACK)
    add_bullet(tf10_bot, "Cross-Track Prerequisite Dependencies:", "Python Basics -> ML Foundations and Backend APIs; Linear Algebra -> Deep Learning; Operating Systems and Docker -> Distributed Systems.", pt_size=9.2)
    add_bullet(tf10_bot, "Curricular Provenance:", "Edges are author-curated based on ACM/IEEE CS2023 body-of-knowledge guidelines, not an external rigid standard. Implemented in NetworkX with automated Neo4j Cypher script export.", pt_size=9.2)

    # =========================================================================
    # SLIDE 11: Dispute Tree and Human Override
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_white_bg(s11)
    add_header(s11, "SECTION 4 · ARCHITECTURE", "Dispute Tree and Human Override", "Unresolved trade-offs become explicit choices for a human", slide_num=11)

    # Top consensus core box
    tf11_core = add_card(s11, Inches(0.8), Inches(1.6), Inches(11.733), Inches(1.0), title="Consensus Core (All Three Personas Unanimously Agree)")
    add_bullet(tf11_core, "Core Agreement:", "Python OOP fundamentals, relational database design with SQL, and version control via Git are unanimously mandated.", pt_size=9.8)

    # Two decision branch cards
    w11 = Inches(5.7)
    h11 = Inches(2.7)
    t11 = Inches(2.8)

    tf11_b1 = add_card(s11, Inches(0.8), t11, w11, h11, title="Branch 1: Foundational Rigor Pathway")
    add_bullet(tf11_b1, "Advocates:", "Critic and Ethics-Reviewer personas.", pt_size=9.5)
    add_bullet(tf11_b1, "Curricular Path:", "Linear Algebra -> Operating Systems -> Concurrency Internals -> Distributed Systems.", pt_size=9.5)
    add_bullet(tf11_b1, "Cost & Timeline:", "10–12 months, zero monetary debt (free MIT OCW + CS50).", pt_size=9.5)
    add_bullet(tf11_b1, "Outcome:", "Durable engineering depth required to clear rigorous enterprise technical screening.", pt_size=9.5)

    tf11_b2 = add_card(s11, Inches(6.8), t11, w11, h11, title="Branch 2: Accelerated Application Pathway")
    add_bullet(tf11_b2, "Advocate:", "Planner persona.", pt_size=9.5)
    add_bullet(tf11_b2, "Curricular Path:", "FastAPI -> REST APIs -> LangChain/RAG -> Shipped Portfolio MVP.", pt_size=9.5)
    add_bullet(tf11_b2, "Cost & Timeline:", "4 months, junior applied-AI startup target.", pt_size=9.5)
    add_bullet(tf11_b2, "Prerequisite Flag:", "Skips foundational math/OS (Delta_prereq > 0): explicitly shown to the human, never auto-recommended.", pt_size=9.5, bold_color=COLOR_BLACK)

    tf11_bot = add_card(s11, Inches(0.8), Inches(5.7), Inches(11.733), Inches(1.2), border_color=COLOR_BLACK)
    add_bullet(tf11_bot, "Human Override Gateway:", "The system stops asserting automated truth. The student or counselor weights speed, rigor, and equity; the tree lists trade-off forks, never voting 2-vs-1 to silence alternative paths.", pt_size=9.5)

    # =========================================================================
    # SLIDE 12: Four Comparative Configurations
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    set_white_bg(s12)
    add_header(s12, "SECTION 5 · EXPERIMENTAL SETUP", "Four Comparative Configurations", "All configurations use the same local Qwen family", slide_num=12)

    w12 = Inches(2.78)
    h12 = Inches(4.3)
    t12 = Inches(1.6)

    cfgs12 = [
        ("Config 1: Single Prompt", [
            ("Design:", "One zero-shot conversational prompt for career guidance."),
            ("Proxy for:", "Generic LLM chat reply, not a commercial enterprise product."),
            ("Inference Cost:", "1 single API/local inference call."),
            ("Guardrail:", "Zero external graph checks or persona separation."),
        ]),
        ("Config 2: Multi-Perspective", [
            ("Design:", "One prompt asks the model to plan, critique, and check ethics internally."),
            ("Scientific Test:", "Internal self-critique without physical agent separation."),
            ("Inference Cost:", "1 long context call."),
            ("Guardrail:", "Chroma retrieval; no external graph validation."),
        ]),
        ("Config 3: Unmoderated Triad", [
            ("Design:", "Planner, Critic, and Ethics answer independently and debate."),
            ("Scientific Test:", "Persona effect without Moderator synthesis or DAG anchor."),
            ("Inference Cost:", "3 separate inference calls."),
            ("Guardrail:", "Evaluates multi-agent conversation in isolation."),
        ]),
        ("Config 4: Full System", [
            ("Design:", "Triad + Moderator + 42-node DAG + Chroma + Gate & Override."),
            ("Output:", "Structured dispute tree and heuristic uncertainty score."),
            ("Inference Cost:", "Multi-call deliberation pipeline."),
            ("Guardrail:", "Deterministic topological sort + Cognitive Forcing Gate."),
        ]),
    ]

    for i, (title, bullets) in enumerate(cfgs12):
        x = Inches(0.8) + i * Inches(2.98)
        tf = add_card(s12, x, t12, w12, h12, title=title)
        for bold, text in bullets:
            add_bullet(tf, bold, text, pt_size=9.2, space_after=6)

    tf12_bot = add_card(s12, Inches(0.8), Inches(6.05), Inches(11.733), Inches(0.9), border_color=COLOR_BLACK)
    add_bullet(tf12_bot, "Ablation Scope Limitation:", "No configuration isolates retrieval, the DAG, or the Moderator alone. These granular component ablations are actively planned as future work (Slide 18).", pt_size=9.2)

    # =========================================================================
    # SLIDE 13: Synthetic Candidate Profiles
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    set_white_bg(s13)
    add_header(s13, "SECTION 5 · EXPERIMENTAL SETUP", "Synthetic Candidate Profiles", "20 author-written profiles: 10 archetypes, each with a matched pair", slide_num=13)

    w13 = Inches(5.7)
    h13 = Inches(3.6)
    t13 = Inches(1.6)

    tf13_l = add_card(s13, Inches(0.8), t13, w13, h13, title="Variant A: \"Aarav Sharma\"")
    add_bullet(tf13_l, "Demographic Signals:", "Male name; Tier-1 national institute (IIT/NIT).", pt_size=9.8, space_after=6)
    add_bullet(tf13_l, "Monthly Budget:", "₹40,000 per month disposable education budget.", pt_size=9.8, space_after=6)
    add_bullet(tf13_l, "Monolithic Tendency:", "Steered by baseline LLMs toward costly cloud infrastructure, high-end tooling, and research labs.", pt_size=9.8, space_after=6)
    add_bullet(tf13_l, "Scientific Invariant:", "Baseline skills, target role, and timeline held 100% identical to Variant B.", pt_size=9.8, bold_color=COLOR_BLACK)

    tf13_r = add_card(s13, Inches(6.8), t13, w13, h13, title="Variant B: \"Priya Patel\"")
    add_bullet(tf13_r, "Demographic Signals:", "Female name; Tier-3 rural state engineering college.", pt_size=9.8, space_after=6)
    add_bullet(tf13_r, "Monthly Budget:", "₹3,000 per month disposable education budget.", pt_size=9.8, space_after=6)
    add_bullet(tf13_r, "Monolithic Tendency:", "Steered by baseline LLMs toward truncated low-tier IT helpdesk plans or predatory bootcamp loans.", pt_size=9.8, space_after=6)
    add_bullet(tf13_r, "Scientific Invariant:", "Baseline skills, target role, and timeline held 100% identical to Variant A.", pt_size=9.8, bold_color=COLOR_BLACK)

    tf13_bot = add_card(s13, Inches(0.8), Inches(5.35), Inches(11.733), Inches(1.6), title="Parity Rules, Confounds, and Limitations")
    add_bullet(tf13_bot, "Parity Rule:", "Core technical milestones should match across a pair. Resource choices (free open-source vs. paid) may differ with budget constraints.", pt_size=9.2)
    add_bullet(tf13_bot, "Confounds and Limits:", "Gender, college tier, and budget change together in this pilot, so effects cannot be pinned on gender alone. Furthermore, names originate from one cultural context; caste, religion, and regional diversity are not yet varied.", pt_size=9.2)

    # =========================================================================
    # SLIDE 14: Evaluation Metrics (Author-Defined)
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    set_white_bg(s14)
    add_header(s14, "SECTION 5 · EXPERIMENTAL SETUP", "Evaluation Metrics (Author-Defined)", "Five metrics, one per research question", slide_num=14)

    w14 = Inches(2.22)
    h14 = Inches(4.3)
    t14 = Inches(1.6)
    gap14 = Inches(0.16)

    metrics14 = [
        ("1. Diversity", "Evidence Diversity", "H = - sum(p_i log2 p_i) / log2 N", "Entropy over N knowledge domains cited. Range 0–1; measures citation breadth across sources, not correctness."),
        ("2. Resolution", "Contradiction Resolution", "CRR = resolved / surfaced * 100%", "Resolved: concern mapped to an explicit tree fork or substantive plan change. Marked n/a if none surfaced."),
        ("3. Unsupported", "Prerequisite Violations", "UCR = violating / total * 100%", "Violating: breaks a DAG prerequisite edge or lacks accredited citation. Lower score is strictly better."),
        ("4. Parity", "Demographic Fairness", "J(A,B) = |S_A & S_B| / |S_A | S_B|", "Jaccard similarity over S: set of core technical curriculum milestones recommended for each profile in a pair."),
        ("5. User Rubric", "Standardized Score", "1 to 5 Likert Scale", "Scored across balance, rigor, equity, transparency, and human override. Needs independent blinded raters."),
    ]

    for i, (m_code, m_name, m_form, m_desc) in enumerate(metrics14):
        x = Inches(0.8) + i * (w14 + gap14)
        tf = add_card(s14, x, t14, w14, h14, title=m_code)
        add_bullet(tf, "Metric:", m_name, pt_size=9.5)
        add_bullet(tf, "Formula:", m_form, pt_size=8.8, bold_color=COLOR_MUTED)
        add_bullet(tf, "Interpretation:", m_desc, pt_size=8.8, space_after=4)

    tf14_bot = add_card(s14, Inches(0.8), Inches(6.05), Inches(11.733), Inches(0.9), border_color=COLOR_BLACK)
    add_bullet(tf14_bot, "Methodological Note:", "These five metrics are author-defined specifically for this advisory safety investigation; they are not established industry benchmarks.", pt_size=9.2)

    # =========================================================================
    # SLIDE 15: Pilot Quantitative Findings
    # =========================================================================
    s15 = prs.slides.add_slide(blank_layout)
    set_white_bg(s15)
    add_header(s15, "SECTION 6 · RESULTS", "Pilot Quantitative Findings", "20 synthetic profiles, 4 configurations, single run", slide_num=15)

    # Table
    rows15 = 5
    cols15 = 6
    t_shape15 = s15.shapes.add_table(rows15, cols15, Inches(0.8), Inches(1.6), Inches(11.733), Inches(2.6))
    table15 = t_shape15.table

    table15.columns[0].width = Inches(2.9)
    table15.columns[1].width = Inches(1.8)
    table15.columns[2].width = Inches(1.6)
    table15.columns[3].width = Inches(2.0)
    table15.columns[4].width = Inches(1.8)
    table15.columns[5].width = Inches(1.633)

    headers15 = ["Configuration", "Evidence Diversity", "CRR", "UCR (Lower Better)", "Parity (Jaccard)", "Rubric (1–5)"]
    data15 = [
        ["Config 1: Single prompt", "0.22", "n/a", "90.9%", "0.32", "2.4"],
        ["Config 2: Multi-perspective", "0.48", "38.0%", "68.2%", "0.93", "3.1"],
        ["Config 3: Unmoderated triad", "0.68", "25.0%", "86.4%", "1.00", "3.5"],
        ["Config 4: Full system", "1.00", "100.0%", "0.0%*", "1.00", "4.7"],
    ]

    for col_idx, text in enumerate(headers15):
        cell = table15.cell(0, col_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_BLACK
        p = cell.text_frame.paragraphs[0]
        p.text = text
        p.font.name = FONT_FAMILY
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE
        p.alignment = PP_ALIGN.CENTER

    for row_idx, row in enumerate(data15):
        is_c4 = row_idx == 3
        bg_col = COLOR_LIGHT_BG if row_idx % 2 == 1 else COLOR_WHITE
        for col_idx, val in enumerate(row):
            cell = table15.cell(row_idx + 1, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg_col
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = FONT_FAMILY
            p.font.size = Pt(9.5)
            p.font.bold = is_c4
            p.font.color.rgb = COLOR_BLACK
            p.alignment = PP_ALIGN.CENTER if col_idx > 0 else PP_ALIGN.LEFT

    # Lower Two Comparative Analysis Cards
    w15_bot = Inches(5.7)
    h15_bot = Inches(2.7)
    t15_bot = Inches(4.35)

    tf15_l = add_card(s15, Inches(0.8), t15_bot, w15_bot, h15_bot, title="What the Pilot Supports")
    add_bullet(tf15_l, "Citation Breadth:", "Debate configurations cite significantly more academic and industry domains than single prompts.", pt_size=9.2)
    add_bullet(tf15_l, "Prerequisite Failure:", "Without the DAG, prerequisite sequencing errors stay unacceptably high across all LLMs (68% to 91%).", pt_size=9.2)
    add_bullet(tf15_l, "Demographic Parity:", "Matched pairs diverge heavily under a single prompt (J = 0.32); Configs 3 and 4 successfully reach full parity (J = 1.00).", pt_size=9.2)

    tf15_r = add_card(s15, Inches(6.8), t15_bot, w15_bot, h15_bot, title="What It Does NOT Show (Critical Candor)")
    add_bullet(tf15_r, "*Circular UCR:", "UCR 0.0% is guaranteed by construction: the 42-node DAG defines and deterministically enforces violations.", pt_size=9.2)
    add_bullet(tf15_r, "Shared Parity:", "Parity 1.00 is already achieved by Config 3, proving parity is driven by persona prompting, not the Moderator or DAG.", pt_size=9.2)
    add_bullet(tf15_r, "Unisolated Drivers:", "Single-run data cannot yet isolate which component drives gains, run-to-run variance, or real-world user outcomes.", pt_size=9.2)

    # =========================================================================
    # SLIDE 16: Case Walkthrough: "Priya"
    # =========================================================================
    s16 = prs.slides.add_slide(blank_layout)
    set_white_bg(s16)
    add_header(s16, "SECTION 6 · RESULTS", "Case Walkthrough: \"Priya\"", "A scripted demonstration of the gate, disputes and override", slide_num=16)

    w16 = Inches(5.7)
    h16 = Inches(2.55)

    tf16_1 = add_card(s16, Inches(0.8), Inches(1.6), w16, h16, title="Candidate Scenario & Baseline Failure")
    add_bullet(tf16_1, "Student Profile:", "3rd-year CSE, rural Tier-3 college, basic Python syntax, ₹3,000/month budget.", pt_size=9.2)
    add_bullet(tf16_1, "Target Career Goal:", "ML Infrastructure Engineer in 4 months.", pt_size=9.2)
    add_bullet(tf16_1, "Debt Vulnerability:", "Advertised ₹1,20,000 commercial bootcamp loan with pay-after-placement trap.", pt_size=9.2)
    add_bullet(tf16_1, "Single Prompt Failure:", "Flattered student, affirmed unfeasible 4-month timeline, and recommended taking the bootcamp debt.", pt_size=9.2)

    tf16_2 = add_card(s16, Inches(6.8), Inches(1.6), w16, h16, title="Triad Deliberation Dynamics")
    add_bullet(tf16_2, "Planner:", "Drafted rapid Pandas wrangling sprints and superficial portfolio projects.", pt_size=9.2)
    add_bullet(tf16_2, "Critic:", "Attacked missing Linear Algebra, probability theory, and OS memory management prerequisites.", pt_size=9.2)
    add_bullet(tf16_2, "Ethics-Reviewer:", "Vetoed the ₹1,20,000 loan; demanded zero-debt MIT OpenCourseWare (18.06) + open-source pull requests.", pt_size=9.2)

    tf16_3 = add_card(s16, Inches(0.8), Inches(4.3), w16, h16, title="Gate Execution & Slider Override")
    add_bullet(tf16_3, "Gate Calculation:", "Friction 0.35 + Prerequisite gap 0.15 = 0.50 >= 0.45, and Delta_prereq > 0.", pt_size=9.2, bold_color=COLOR_BLACK)
    add_bullet(tf16_3, "Autonomous Release:", "Halted automatically; system transitions to interactive Streamlit sliders.", pt_size=9.2)
    add_bullet(tf16_3, "Student Selection:", "Student adjusts sliders to prioritize zero debt and foundation rigor over speed.", pt_size=9.2)

    tf16_4 = add_card(s16, Inches(6.8), Inches(4.3), w16, h16, title="Fairness & Calibration Disclosure")
    add_bullet(tf16_4, "Fairness Invariant:", "Socioeconomic risk (0.20) is presented to the counselor as context but is not added to the gate score, so lower-income students are not gated more often.", pt_size=9.0)
    add_bullet(tf16_4, "Heuristic Calibration:", "The 0.45 threshold is a heuristic setting; the score is uncalibrated with no statistical reliability curve yet.", pt_size=9.0)

    # =========================================================================
    # SLIDE 17: Threats to Validity
    # =========================================================================
    s17 = prs.slides.add_slide(blank_layout)
    set_white_bg(s17)
    add_header(s17, "SECTION 7 · LIMITATIONS", "Threats to Validity", "Stated plainly so the claims stay within the evidence", slide_num=17)

    w17 = Inches(5.7)
    h17 = Inches(5.3)
    t17 = Inches(1.6)

    tf17_l = add_card(s17, Inches(0.8), t17, w17, h17, title="Measurement Threats")
    add_bullet(tf17_l, "1. Circular UCR Metric:", "Config 4 is evaluated by the exact same 42-node DAG it uses for runtime filtering; 0.0% is true by construction.", pt_size=9.5, space_after=8)
    add_bullet(tf17_l, "2. Small Sample Size:", "10 matched pairs (20 profiles) evaluated in a single run; lacks confidence intervals and significance testing.", pt_size=9.5, space_after=8)
    add_bullet(tf17_l, "3. Unvalidated Rubric:", "The 5-point pedagogical rubric has not yet been validated by external, blinded human raters.", pt_size=9.5, space_after=8)
    add_bullet(tf17_l, "4. Uncalibrated Uncertainty:", "Hand-weighted heuristic score without Expected Calibration Error (ECE) or threshold sensitivity testing.", pt_size=9.5, space_after=8)
    add_bullet(tf17_l, "5. Deliberation Latency:", "Takes ~4.5 seconds per debate turn; full end-to-end multi-agent pipeline latency was not profiled.", pt_size=9.5)

    tf17_r = add_card(s17, Inches(6.8), t17, w17, h17, title="Design and Data Threats")
    add_bullet(tf17_r, "1. Single Model Family:", "Personas and Moderator all share local Qwen model priors, limiting genuine cognitive divergence.", pt_size=9.5, space_after=8)
    add_bullet(tf17_r, "2. Missing Component Ablations:", "Retrieval, the DAG, and the Moderator were not isolated in separate component ablation runs.", pt_size=9.5, space_after=8)
    add_bullet(tf17_r, "3. Confounded Synthetic Profiles:", "Author-written profiles vary gender, college tier, and budget simultaneously, preventing isolated attribution.", pt_size=9.5, space_after=8)
    add_bullet(tf17_r, "4. Computing-Specific Graph:", "42 nodes cover computer science only; non-computing career guidance requires authoring new ontologies.", pt_size=9.5, space_after=8)
    add_bullet(tf17_r, "5. Geographic Context Mismatch:", "O*NET and BLS are US labor sources; human override gateway remains untested with real undergraduate cohorts.", pt_size=9.5)

    # =========================================================================
    # SLIDE 18: Validation Plan and Conclusion
    # =========================================================================
    s18 = prs.slides.add_slide(blank_layout)
    set_white_bg(s18)
    add_header(s18, "SECTION 7 · FUTURE WORK", "Validation Plan and Conclusion", "What would turn the pilot into evidence", slide_num=18)

    w18_col = Inches(3.75)
    h18_col = Inches(3.6)
    t18_col = Inches(1.6)

    tf18_1 = add_card(s18, Inches(0.8), t18_col, w18_col, h18_col, title="1. Rigorous Experimental Setup")
    add_bullet(tf18_1, "Component Ablations:", "Single LLM + DAG; triad + DAG without Moderator; full system without ChromaDB retrieval.", pt_size=9.5, space_after=8)
    add_bullet(tf18_1, "Stronger Baselines:", "Compute-matched self-consistency and majority-voting baselines as demanded by Smit et al. [3].", pt_size=9.5)

    tf18_2 = add_card(s18, Inches(4.78), t18_col, w18_col, h18_col, title="2. Statistical & Calibration Rigor")
    add_bullet(tf18_2, "Repeated Statistical Runs:", "Multiple runs across temperatures and random seeds with confidence intervals and significance tests.", pt_size=9.5, space_after=8)
    add_bullet(tf18_2, "Formal Calibration:", "Empirical reliability diagrams, threshold sensitivity analysis, and quantitative gate firing rates.", pt_size=9.5)

    tf18_3 = add_card(s18, Inches(8.76), t18_col, w18_col, h18_col, title="3. Human Studies & Localization")
    add_bullet(tf18_3, "Blinded Human Evaluation:", "Named external raters, double-blinded scoring, and inter-rater agreement metrics (Cohen's kappa).", pt_size=9.5, space_after=8)
    add_bullet(tf18_3, "Real User Cohort:", "Controlled student and counselor user studies with India-specific placement and salary datasets.", pt_size=9.5)

    # Conclusion & Footer
    tf18_bot = add_card(s18, Inches(0.8), Inches(5.35), Inches(11.733), Inches(1.6), title="Research Conclusion & Open-Source Artifacts")
    add_bullet(tf18_bot, "Conclusion:", "Pairing structured multi-persona disagreement with a deterministic prerequisite check produced transparent, human-overridable career advice in a pilot study. Definitive claims of real-world superiority await the formal validation agenda detailed above.", pt_size=9.5)
    add_bullet(tf18_bot, "Open-Source Verification Commands:", "Interactive Web UI: streamlit run app.py   |   Benchmark Suite: python3 run_study.py", pt_size=9.5, bold_color=COLOR_BLACK)

    # =========================================================================
    # SLIDE 19: References
    # =========================================================================
    s19 = prs.slides.add_slide(blank_layout)
    set_white_bg(s19)
    add_header(s19, "SECTION 8 · REFERENCES", "References", "Each source is cited in the body of the deck", slide_num=19)

    w19 = Inches(5.7)
    h19 = Inches(5.3)
    t19 = Inches(1.6)

    tf19_l = add_card(s19, Inches(0.8), t19, w19, h19, title="Debate, Grounding & Curricula")
    add_bullet(tf19_l, "[1] Du et al. (2024):", "Improving Factuality and Reasoning in Language Models through Multiagent Debate. ICML 2024. arXiv:2305.14325.", pt_size=9.0, space_after=8)
    add_bullet(tf19_l, "[2] Liang et al. (2023):", "Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate. EMNLP 2023.", pt_size=9.0, space_after=8)
    add_bullet(tf19_l, "[3] Smit et al. (2024):", "Should We Be Going MAD? A Critical Look at Multi-Agent Debate Strategies. ICML 2024. arXiv:2311.17371.", pt_size=9.0, space_after=8)
    add_bullet(tf19_l, "[4] ACM/IEEE (2023):", "Computer Science Curricula 2023 (CS2023). Joint Task Force on Computing Curricula.", pt_size=9.0, space_after=8)

    tf19_r = add_card(s19, Inches(6.8), t19, w19, h19, title="Sycophancy, Uncertainty, Fairness & Agency")
    add_bullet(tf19_r, "[5] Sharma et al. (2024):", "Towards Understanding Sycophancy in Language Models. ICLR 2024. arXiv:2310.13548.", pt_size=9.0, space_after=8)
    add_bullet(tf19_r, "[6] Xiong et al. (2024):", "Can LLMs Express Their Uncertainty? ICLR 2024. arXiv:2306.13063.", pt_size=9.0, space_after=8)
    add_bullet(tf19_r, "[7] Geyik et al. (2019):", "Fairness-Aware Ranking in Search & Recommendation Systems with Application to LinkedIn Talent Search. KDD 2019, pp. 2221–2231.", pt_size=9.0, space_after=8)
    add_bullet(tf19_r, "[8] Buçinca et al. (2021):", "To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making. PACMHCI 5(CSCW1), Art. 188.", pt_size=9.0, space_after=8)

    # Save output
    output_path = "docs/FINAL_PRESENTATION_BW_19_SLIDES.pptx"
    prs.save(output_path)
    print(f"✅ Successfully generated Pure Black & White 19-Slide Deck at: {output_path}")

if __name__ == "__main__":
    create_deck()
