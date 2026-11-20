"""
Generate Exact 15-Slide Pure Black & White Master Presentation Deck
Matches the user's exact 15-slide consolidated project deck verbatim.
Theme: 100% Black & White (Pure white background, crisp black cards, inverted header badges,
16:9 widescreen layout, perfectly proportioned typography).
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# 100% Black and White Color Palette
COLOR_BLACK = RGBColor(0, 0, 0)
COLOR_WHITE = RGBColor(255, 255, 255)
COLOR_DARK = RGBColor(30, 30, 30)
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

    def add_header(slide, title, subtitle=None, slide_num=None):
        # Top rule
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.45), Inches(11.733), Inches(0.02))
        line.fill.solid()
        line.fill.fore_color.rgb = COLOR_BLACK
        line.line.fill.background()

        # Slide Number
        if slide_num:
            box_num = slide.shapes.add_textbox(Inches(10.5), Inches(0.55), Inches(2.033), Inches(0.3))
            p_num = box_num.text_frame.paragraphs[0]
            p_num.text = f"{slide_num} / 15"
            p_num.font.name = FONT_FAMILY
            p_num.font.size = Pt(8.5)
            p_num.font.bold = True
            p_num.font.color.rgb = COLOR_MUTED
            p_num.alignment = PP_ALIGN.RIGHT

        # Title
        box_t = slide.shapes.add_textbox(Inches(0.8), Inches(0.70), Inches(10.0), Inches(0.5))
        p_t = box_t.text_frame.paragraphs[0]
        p_t.text = title
        p_t.font.name = FONT_FAMILY
        p_t.font.size = Pt(17)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_BLACK

        # Subtitle
        if subtitle:
            p_sub = box_t.text_frame.add_paragraph()
            p_sub.text = subtitle
            p_sub.font.name = FONT_FAMILY
            p_sub.font.size = Pt(9.5)
            p_sub.font.italic = True
            p_sub.font.color.rgb = COLOR_DARK
            p_sub.space_before = Pt(2)

    def add_card(slide, left, top, width, height, title=None, bg_color=COLOR_WHITE, border_color=COLOR_BLACK_BORDER, border_width=1.0):
        card = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(border_width)

        if title:
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
    # SLIDE 1: Title & Implementation
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_white_bg(s1)

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
    psub1.text = "Planner, Critic and Ethics-Reviewer personas debate public course and role data, with an uncertainty gate and human override"
    psub1.font.name = FONT_FAMILY
    psub1.font.size = Pt(12)
    psub1.font.italic = True
    psub1.font.color.rgb = COLOR_DARK
    psub1.space_before = Pt(6)

    c1_tf = add_card(s1, Inches(0.8), Inches(3.1), Inches(5.7), Inches(3.6), title="Project")
    add_bullet(c1_tf, "Presented by:", "Parth Gupta, B.Tech CSE, SRMIST Kattankulathur", pt_size=10.5, space_after=8)
    add_bullet(c1_tf, "Mentorship:", "Dr. P. Akilandeswari (Faculty) | Pratyush Jha (Industry)", pt_size=10.5, space_after=8)
    add_bullet(c1_tf, "Domain:", "Responsible AI, multi-agent debate systems", pt_size=10.5, space_after=8)
    add_bullet(c1_tf, "Session:", "Academic evaluation 2025–2026", pt_size=10.5, space_after=8)
    add_bullet(c1_tf, "Status:", "Pilot study on 20 synthetic profiles", pt_size=10.5, space_after=8)

    c2_tf = add_card(s1, Inches(6.8), Inches(3.1), Inches(5.7), Inches(3.6), title="Implementation")
    add_bullet(c2_tf, "LLM:", "Qwen models run locally via Ollama", pt_size=10.5, space_after=8)
    add_bullet(c2_tf, "Harness:", "Python loop (Planner, Critic, Ethics, Moderator)", pt_size=10.5, space_after=8)
    add_bullet(c2_tf, "Grounding:", "Chroma vector store + 42-node prerequisite graph", pt_size=10.5, space_after=8)
    add_bullet(c2_tf, "Interface:", "Streamlit trace viewer with human override", pt_size=10.5, space_after=8)
    add_bullet(c2_tf, "Execution Model:", "100% private on-device execution, zero cloud API fees", pt_size=10.5, space_after=8)

    b_line = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(6.9), Inches(11.733), Inches(0.02))
    b_line.fill.solid()
    b_line.fill.fore_color.rgb = COLOR_BLACK
    b_line.line.fill.background()

    # =========================================================================
    # SLIDE 2: Abstract
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_white_bg(s2)
    add_header(s2, "Abstract", "Surface disagreement, check prerequisites, keep the student in control", slide_num=2)

    w2 = Inches(3.75)
    h2 = Inches(3.2)
    t2 = Inches(1.5)

    tf2_1 = add_card(s2, Inches(0.8), t2, w2, h2, title="The Advisory Problem")
    add_bullet(tf2_1, "Sycophancy:", "LLMs tend to agree with users [5], including on unrealistic goals.")
    add_bullet(tf2_1, "Flattened trade-offs:", "one pass can blur competing options.")
    add_bullet(tf2_1, "Steering risk:", "advice may shift with institution or income cues.")

    tf2_2 = add_card(s2, Inches(4.78), t2, w2, h2, title="Our Approach")
    add_bullet(tf2_2, "Three personas:", "Planner (growth), Critic (rigor), Ethics-Reviewer (equity, debt).")
    add_bullet(tf2_2, "Grounding:", "Chroma over course and O*NET role data.")
    add_bullet(tf2_2, "Check:", "42-node author-curated prerequisite graph.")

    tf2_3 = add_card(s2, Inches(8.76), t2, w2, h2, title="Evaluation Scope")
    add_bullet(tf2_3, "Scope:", "Four configurations, five author-defined metrics.")
    add_bullet(tf2_3, "Pilot:", "20 synthetic profiles (10 matched pairs).")
    add_bullet(tf2_3, "Gate:", "human review if prerequisite violations exist or score >= 0.45.")

    tf2_bot = add_card(s2, Inches(0.8), Inches(4.9), Inches(11.733), Inches(2.0), title="Pilot Findings (Single Run, Synthetic Data, Preliminary)")
    add_bullet(tf2_bot, "1. Prerequisite Compliance:", "The full system emits no prerequisite violations. This holds by construction of the graph check, not as an independent test.", pt_size=9.5)
    add_bullet(tf2_bot, "2. Demographic Parity:", "Core milestones match across matched pairs (Jaccard 1.00); the unmoderated triad also reaches 1.00.", pt_size=9.5)
    add_bullet(tf2_bot, "3. Decision Support Agency:", "Dispute trees and the override gate pass unresolved trade-offs to the student. See Limitations.", pt_size=9.5)

    # =========================================================================
    # SLIDE 3: Problem: Single-Pass LLM vs. Proposed Pipeline
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_white_bg(s3)
    add_header(s3, "Problem: Single-Pass LLM vs. Proposed Pipeline", "Contrasting a typical single-pass LLM failure pattern with our pipeline", slide_num=3)

    w3 = Inches(5.7)
    h3 = Inches(5.4)
    t3 = Inches(1.5)

    tf3_l = add_card(s3, Inches(0.8), t3, w3, h3, title="Single-Pass LLM (Failure Pattern)")
    add_bullet(tf3_l, "1. Unrealistic request:", "\"Staff ML Engineer in 4 months via bootcamp\"", pt_size=10.0, space_after=8)
    add_bullet(tf3_l, "2. Agreeableness bias:", "Preference-tuned models tend to affirm user views [5]", pt_size=10.0, space_after=8)
    add_bullet(tf3_l, "3. Skipped prerequisites:", "Omits linear algebra and OS, jumps to Transformers", pt_size=10.0, space_after=8)
    add_bullet(tf3_l, "Risk:", "Bootcamp debt (₹1,20,000) and failed technical screening", pt_size=10.5, bold_color=COLOR_BLACK, space_after=8)

    tf3_r = add_card(s3, Inches(6.8), t3, w3, h3, title="Proposed Grounded Architecture")
    add_bullet(tf3_r, "1. Intake and grounding:", "Retrieve course modules and O*NET roles from Chroma", pt_size=10.0, space_after=8)
    add_bullet(tf3_r, "2. Persona friction:", "Planner vs. Critic vs. Ethics-Reviewer", pt_size=10.0, space_after=8)
    add_bullet(tf3_r, "3. Graph traversal:", "Detect missing prerequisite hops, flag Delta_prereq", pt_size=10.0, space_after=8)
    add_bullet(tf3_r, "Outcome:", "Dispute tree, uncertainty score, human override", pt_size=10.5, bold_color=COLOR_BLACK, space_after=8)

    # =========================================================================
    # SLIDE 4: Literature Survey
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_white_bg(s4)
    add_header(s4, "Literature Survey", "Debate, grounding, and fairness with human agency", slide_num=4)

    w4 = Inches(3.75)
    h4 = Inches(3.1)
    t4 = Inches(1.5)

    tf4_1 = add_card(s4, Inches(0.8), t4, w4, h4, title="1. Multi-Agent Debate")
    add_bullet(tf4_1, "Du et al. [1]:", "debate improved factuality and reasoning.")
    add_bullet(tf4_1, "Liang et al. [2]:", "debate encourages divergent thinking.")
    add_bullet(tf4_1, "Smit et al. [3]:", "uncurated debate can reduce to costly majority voting.")

    tf4_2 = add_card(s4, Inches(4.78), t4, w4, h4, title="2. Grounding and RAG")
    add_bullet(tf4_2, "CS2023 [4]:", "curricular knowledge areas informed our graph; edges are author-curated.")
    add_bullet(tf4_2, "O*NET and BLS:", "US occupational taxonomies, used as a role-skill proxy.")
    add_bullet(tf4_2, "Prerequisite graph:", "catches sequencing errors an LLM may miss.")

    tf4_3 = add_card(s4, Inches(8.76), t4, w4, h4, title="3. Fairness and Agency")
    add_bullet(tf4_3, "Geyik et al. [7]:", "fairness-aware ranking.")
    add_bullet(tf4_3, "Buçinca et al. [8]:", "cognitive forcing reduces overreliance on AI.")
    add_bullet(tf4_3, "Sharma [5], Xiong [6]:", "sycophancy and weak verbalized confidence, so the gate uses structural signals.")

    tf4_bot = add_card(s4, Inches(0.8), Inches(4.8), Inches(11.733), Inches(2.1), title="Critique of Debate (Smit et al. [3]) and Our Response")
    add_bullet(tf4_bot, "Concerns:", "debate may match majority voting, share priors, and amplify confident errors.", pt_size=9.5)
    add_bullet(tf4_bot, "Our response:", "external grounding, role-differentiated prompts, dispute trees, human override gate.", pt_size=9.5)
    add_bullet(tf4_bot, "Limit:", "personas share one model family (partial mitigation); no compute-matched majority-vote baseline yet.", pt_size=9.5)

    # =========================================================================
    # SLIDE 5: Positioning Against Prior Work
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_white_bg(s5)
    add_header(s5, "Positioning Against Prior Work", "Scope comparison, not a performance comparison", slide_num=5)

    rows5 = 6
    cols5 = 6
    t_shape5 = s5.shapes.add_table(rows5, cols5, Inches(0.8), Inches(1.5), Inches(11.733), Inches(3.8))
    table5 = t_shape5.table

    table5.columns[0].width = Inches(2.2)
    table5.columns[1].width = Inches(1.8)
    table5.columns[2].width = Inches(1.9)
    table5.columns[3].width = Inches(2.0)
    table5.columns[4].width = Inches(1.9)
    table5.columns[5].width = Inches(1.933)

    headers5 = ["Work", "Multi-Agent Debate", "External Data Grounding", "Fairness Audit", "Human in the Loop", "Career-Advice Domain"]
    data5 = [
        ["Du et al. [1]", "Yes", "No", "No", "No", "No"],
        ["Liang et al. [2]", "Yes", "No", "No", "No", "No"],
        ["Geyik et al. [7]", "No", "N/A", "Yes (ranking parity)", "No", "Partly (talent search)"],
        ["Buçinca et al. [8]", "N/A", "N/A", "N/A", "Yes (cognitive forcing)", "No"],
        ["This work", "Yes (3 personas + Mod)", "Yes (Chroma + graph)", "Yes (synthetic pairs)", "Yes (override gate)", "Yes"],
    ]

    for col_idx, text in enumerate(headers5):
        cell = table5.cell(0, col_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_BLACK
        p = cell.text_frame.paragraphs[0]
        p.text = text
        p.font.name = FONT_FAMILY
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE
        p.alignment = PP_ALIGN.CENTER

    for row_idx, row in enumerate(data5):
        is_this_work = row_idx == 4
        bg_col = COLOR_LIGHT_BG if row_idx % 2 == 1 else COLOR_WHITE
        for col_idx, val in enumerate(row):
            cell = table5.cell(row_idx + 1, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg_col
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = FONT_FAMILY
            p.font.size = Pt(9.2)
            p.font.bold = is_this_work
            p.font.color.rgb = COLOR_BLACK
            p.alignment = PP_ALIGN.CENTER if col_idx > 0 else PP_ALIGN.LEFT

    tf5_foot = add_card(s5, Inches(0.8), Inches(5.5), Inches(11.733), Inches(1.4), border_color=COLOR_CARD_BORDER)
    add_bullet(tf5_foot, "Scope Disclaimer:", "N/A: outside the work's scope. Prior works target different problems, so this table shows what each covers, not which is better.", pt_size=9.2)

    # =========================================================================
    # SLIDE 6: System Architecture: End-to-End Decision Flow
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_white_bg(s6)
    add_header(s6, "System Architecture: End-to-End Decision Flow", "Intake, retrieval, deliberation, prerequisite check, then a gate", slide_num=6)

    w6_step = Inches(2.22)
    h6_step = Inches(2.1)
    t6_step = Inches(1.5)
    gap6 = Inches(0.16)

    steps6 = [
        ("1. Intake", "Skills, role, timeline, budget"),
        ("2. Retrieval", "Chroma: courses and O*NET roles"),
        ("3. Triad", "Local Qwen: Planner, Critic, Ethics"),
        ("4. Moderator+Graph", "Checks prerequisites, extracts disputes"),
        ("5. Gate", "Violations > 0 or score >= 0.45?"),
    ]

    for i, (title, desc) in enumerate(steps6):
        x = Inches(0.8) + i * (w6_step + gap6)
        tf = add_card(s6, x, t6_step, w6_step, h6_step, title=title)
        add_bullet(tf, "", desc, pt_size=9.2)

    w6_bot = Inches(5.7)
    h6_bot = Inches(2.5)
    t6_bot = Inches(3.8)

    tf6_l = add_card(s6, Inches(0.8), t6_bot, w6_bot, h6_bot, title="Gate Fires: Human Override")
    add_bullet(tf6_l, "Dispute tree:", "forks across speed, depth and financial risk.", pt_size=9.5)
    add_bullet(tf6_l, "Sliders:", "student or counselor re-weights speed, prerequisite rigor and debt avoidance.", pt_size=9.5)

    tf6_r = add_card(s6, Inches(6.8), t6_bot, w6_bot, h6_bot, title="Gate Clear: Balanced Roadmap")
    add_bullet(tf6_r, "Milestones:", "sequenced so every included node meets its prerequisite edges.", pt_size=9.5)
    add_bullet(tf6_r, "Citations:", "linked to retrieved course modules and O*NET entries.", pt_size=9.5)

    tf6_impl = add_card(s6, Inches(0.8), Inches(6.45), Inches(11.733), Inches(0.55), border_color=COLOR_BLACK)
    add_bullet(tf6_impl, "Implementation:", "Models qwen3:4b-fast, qwen3:4b, qwen2:0.5b via Ollama · pure-Python loop with structured JSON · Neo4j graph (NetworkX fallback) · ChromaDB · Streamlit", pt_size=8.8)

    # =========================================================================
    # SLIDE 7: Complementary Personas
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_white_bg(s7)
    add_header(s7, "Complementary Personas", "Differentiated prompts with opposing objectives", slide_num=7)

    w7 = Inches(3.75)
    h7 = Inches(5.4)
    t7 = Inches(1.5)

    tf7_1 = add_card(s7, Inches(0.8), t7, w7, h7, title="Planner")
    add_bullet(tf7_1, "Lens:", "Constructive execution, milestones, time-to-market", pt_size=9.5, space_after=8)
    add_bullet(tf7_1, "Focus:", "Maps goals to course modules (e.g. CS101, CS201, CS330) and O*NET roles", pt_size=9.5, space_after=8)
    add_bullet(tf7_1, "Function:", "Builds actionable pathways and avoids analysis paralysis", pt_size=9.5, space_after=8)

    tf7_2 = add_card(s7, Inches(4.78), t7, w7, h7, title="Critic")
    add_bullet(tf7_2, "Lens:", "Adversarial stress-testing and prerequisite skepticism", pt_size=9.5, space_after=8)
    add_bullet(tf7_2, "Focus:", "Linear algebra, OS and concurrency depth, screening barriers", pt_size=9.5, space_after=8)
    add_bullet(tf7_2, "Function:", "Warns against advanced roles without foundations; flags thin tutorial-level projects", pt_size=9.5, space_after=8)

    tf7_3 = add_card(s7, Inches(8.76), t7, w7, h7, title="Ethics-Reviewer")
    add_bullet(tf7_3, "Lens:", "Equity and debt safeguards", pt_size=9.5, space_after=8)
    add_bullet(tf7_3, "Focus:", "Flags high-cost debt and prefers free resources; the student can override with costs shown", pt_size=9.5, space_after=8)
    add_bullet(tf7_3, "Function:", "Suggests verifiable open-source work to offset institution bias; notes free courses still cost time and connectivity", pt_size=9.5, space_after=8)

    # =========================================================================
    # SLIDE 8: Career-Skill Graph: 16 of 42 Nodes Shown
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_white_bg(s8)
    add_header(s8, "Career-Skill Graph: 16 of 42 Nodes Shown", "Four tracks of the author-curated prerequisite DAG", slide_num=8)

    w8 = Inches(2.78)
    h8 = Inches(4.0)
    t8 = Inches(1.5)

    tf8_1 = add_card(s8, Inches(0.8), t8, w8, h8, title="Track 1: DSA and Math")
    add_bullet(tf8_1, "Discrete Math:", "Logic, graph theory")
    add_bullet(tf8_1, "Python / C Basics:", "Syntax, control flow")
    add_bullet(tf8_1, "Data Structures:", "Trees, heaps, graphs")
    add_bullet(tf8_1, "Advanced Algorithms:", "Dynamic programming, flows")

    tf8_2 = add_card(s8, Inches(3.78), t8, w8, h8, title="Track 2: Systems and OS")
    add_bullet(tf8_2, "C Memory & Pointers:", "Stack, heap, allocation")
    add_bullet(tf8_2, "Computer Architecture:", "Registers, ALU, caches")
    add_bullet(tf8_2, "Operating Systems:", "Processes, paging, IPC")
    add_bullet(tf8_2, "Distributed Systems:", "Raft, Paxos, replication")

    tf8_3 = add_card(s8, Inches(6.76), t8, w8, h8, title="Track 3: Web and Cloud")
    add_bullet(tf8_3, "HTML / CSS / JS:", "DOM, event loop")
    add_bullet(tf8_3, "Backend APIs:", "FastAPI, REST routing")
    add_bullet(tf8_3, "Docker Containers:", "Namespaces, cgroups")
    add_bullet(tf8_3, "System Design, CI/CD:", "Load balancing, sharding")

    tf8_4 = add_card(s8, Inches(9.74), t8, w8, h8, title="Track 4: Machine Learning")
    add_bullet(tf8_4, "Linear Algebra & Stats:", "Eigenvalues, probability")
    add_bullet(tf8_4, "Data Analysis (Pandas):", "Wrangling, cleaning")
    add_bullet(tf8_4, "ML Foundations:", "Loss functions, gradients")
    add_bullet(tf8_4, "Deep Learning and LLMs:", "Transformers, backprop")

    tf8_bot = add_card(s8, Inches(0.8), Inches(5.7), Inches(11.733), Inches(1.2), border_color=COLOR_BLACK)
    add_bullet(tf8_bot, "Navigation & Edges:", "Read each column top to bottom (prerequisite order). Cross-track edges: Python Basics -> ML Foundations and Backend APIs; Linear Algebra -> Deep Learning; OS and Docker -> Distributed Systems. Edges are author-curated, informed by CS2023, not an external standard.", pt_size=9.2)

    # =========================================================================
    # SLIDE 9: Dispute Tree and Human Override
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_white_bg(s9)
    add_header(s9, "Dispute Tree and Human Override", "Unresolved trade-offs become explicit choices for a human", slide_num=9)

    tf9_core = add_card(s9, Inches(0.8), Inches(1.5), Inches(11.733), Inches(0.9), title="Consensus Core (All Three Personas Agree)")
    add_bullet(tf9_core, "Python OOP, relational SQL, Git", "", pt_size=10.0, bold_color=COLOR_BLACK)

    w9 = Inches(5.7)
    h9 = Inches(2.9)
    t9 = Inches(2.6)

    tf9_b1 = add_card(s9, Inches(0.8), t9, w9, h9, title="Branch 1: Foundational Rigor")
    add_bullet(tf9_b1, "Advocates:", "Critic and Ethics-Reviewer.", pt_size=9.5)
    add_bullet(tf9_b1, "Path:", "Linear Algebra -> OS -> Concurrency -> Distributed Systems.", pt_size=9.5)
    add_bullet(tf9_b1, "Cost and time:", "10–12 months, zero debt (free open courseware).", pt_size=9.5)
    add_bullet(tf9_b1, "Outcome:", "durable depth for enterprise screening.", pt_size=9.5)

    tf9_b2 = add_card(s9, Inches(6.8), t9, w9, h9, title="Branch 2: Accelerated Application")
    add_bullet(tf9_b2, "Advocate:", "Planner.", pt_size=9.5)
    add_bullet(tf9_b2, "Path:", "FastAPI -> REST -> LangChain/RAG -> shipped MVP.", pt_size=9.5)
    add_bullet(tf9_b2, "Cost and time:", "4 months, junior applied-AI target.", pt_size=9.5)
    add_bullet(tf9_b2, "Flag:", "skips prerequisites (Delta_prereq > 0); shown to the human, never auto-recommended.", pt_size=9.5, bold_color=COLOR_BLACK)

    tf9_bot = add_card(s9, Inches(0.8), Inches(5.7), Inches(11.733), Inches(1.2), border_color=COLOR_BLACK)
    add_bullet(tf9_bot, "Human override gateway:", "the system stops asserting. The student or counselor weights speed, rigor and equity; the tree lists forks, it does not vote 2-vs-1.", pt_size=9.5)

    # =========================================================================
    # SLIDE 10: Experimental Setup: Configurations and Profiles
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_white_bg(s10)
    add_header(s10, "Experimental Setup: Configurations and Profiles", "Systematic evaluation across 20 synthetic candidate profiles", slide_num=10)

    # Table of 4 Configurations
    rows10 = 5
    cols10 = 3
    t_shape10 = s10.shapes.add_table(rows10, cols10, Inches(0.8), Inches(1.5), Inches(11.733), Inches(2.5))
    table10 = t_shape10.table

    table10.columns[0].width = Inches(2.8)
    table10.columns[1].width = Inches(6.0)
    table10.columns[2].width = Inches(2.933)

    headers10 = ["Configuration", "Design", "Tests / Cost"]
    data10 = [
        ["Config 1: Single prompt", "One zero-shot prompt for career advice (proxy for a generic chat reply)", "1 call"],
        ["Config 2: Multi-perspective", "One prompt asks the model to plan, critique and check ethics", "Internal self-critique; 1 long call"],
        ["Config 3: Unmoderated triad", "Planner, Critic and Ethics answer independently", "Persona effect without Moderator or graph; 3 calls"],
        ["Config 4: Full system", "Triad + Moderator + graph + Chroma + gate and override", "Dispute tree and uncertainty score; multi-call"],
    ]

    for col_idx, text in enumerate(headers10):
        cell = table10.cell(0, col_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_BLACK
        p = cell.text_frame.paragraphs[0]
        p.text = text
        p.font.name = FONT_FAMILY
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE
        p.alignment = PP_ALIGN.CENTER

    for row_idx, row in enumerate(data10):
        is_c4 = row_idx == 3
        bg_col = COLOR_LIGHT_BG if row_idx % 2 == 1 else COLOR_WHITE
        for col_idx, val in enumerate(row):
            cell = table10.cell(row_idx + 1, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg_col
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = FONT_FAMILY
            p.font.size = Pt(9.2)
            p.font.bold = is_c4
            p.font.color.rgb = COLOR_BLACK
            p.alignment = PP_ALIGN.LEFT

    tf10_bot = add_card(s10, Inches(0.8), Inches(4.2), Inches(11.733), Inches(2.7), title="Synthetic Profiles (20 Author-Written: 10 Archetypes, Each with Matched Pair)")
    add_bullet(tf10_bot, "Variant A \"Aarav Sharma\":", "male name, Tier-1 national institute, ₹40,000 per month.", pt_size=9.5)
    add_bullet(tf10_bot, "Variant B \"Priya Patel\":", "female name, Tier-3 rural state college, ₹3,000 per month.", pt_size=9.5)
    add_bullet(tf10_bot, "Parity rule:", "skills, target role and timeline are identical; core milestones should match, free vs. paid resources may differ.", pt_size=9.5)
    add_bullet(tf10_bot, "Confounds:", "gender, tier and budget change together; names come from one cultural context.", pt_size=9.5)

    # =========================================================================
    # SLIDE 11: Research Questions and Evaluation Metrics
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_white_bg(s11)
    add_header(s11, "Research Questions and Evaluation Metrics", "Quantitative criteria mapping to each research question", slide_num=11)

    rows11 = 6
    cols11 = 3
    t_shape11 = s11.shapes.add_table(rows11, cols11, Inches(0.8), Inches(1.5), Inches(11.733), Inches(4.3))
    table11 = t_shape11.table

    table11.columns[0].width = Inches(3.4)
    table11.columns[1].width = Inches(3.2)
    table11.columns[2].width = Inches(5.133)

    headers11 = ["Research Question", "Metric", "Definition"]
    data11 = [
        ["RQ1: Does retrieval broaden the domains cited?", "Evidence diversity: H = - sum(p_i log2 p_i) / log2 N", "Entropy over N domains cited; range 0–1; breadth, not correctness"],
        ["RQ2: Does Moderator map concerns to explicit forks?", "CRR = resolved / surfaced * 100%", "Resolved: concern mapped to a fork or plan change"],
        ["RQ3: Does graph verification reduce violations?", "UCR = violating / total milestones * 100%", "Violating: breaks a graph edge or lacks a citation; lower is better"],
        ["RQ4: Do core recommendations stay stable?", "Parity: J(A,B) = |S_A & S_B| / |S_A | S_B|", "S: set of core technical milestones for each profile in a pair"],
        ["RQ5: Do reviewers rate full system higher?", "Rubric score, 1–5", "Balance, rigor, equity, transparency, override; needs blinded raters"],
    ]

    for col_idx, text in enumerate(headers11):
        cell = table11.cell(0, col_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_BLACK
        p = cell.text_frame.paragraphs[0]
        p.text = text
        p.font.name = FONT_FAMILY
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE
        p.alignment = PP_ALIGN.CENTER

    for row_idx, row in enumerate(data11):
        bg_col = COLOR_LIGHT_BG if row_idx % 2 == 1 else COLOR_WHITE
        for col_idx, val in enumerate(row):
            cell = table11.cell(row_idx + 1, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg_col
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = FONT_FAMILY
            p.font.size = Pt(9.0)
            p.font.color.rgb = COLOR_BLACK
            p.alignment = PP_ALIGN.LEFT

    tf11_bot = add_card(s11, Inches(0.8), Inches(6.05), Inches(11.733), Inches(0.9), border_color=COLOR_BLACK)
    add_bullet(tf11_bot, "Benchmark Status:", "These metrics are defined by the authors for this study; they are not standard benchmarks.", pt_size=9.2)

    # =========================================================================
    # SLIDE 12: Pilot Quantitative Results
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    set_white_bg(s12)
    add_header(s12, "Pilot Quantitative Results", "20 synthetic profiles, 4 configurations, single run", slide_num=12)

    rows12 = 5
    cols12 = 6
    t_shape12 = s12.shapes.add_table(rows12, cols12, Inches(0.8), Inches(1.5), Inches(11.733), Inches(2.6))
    table12 = t_shape12.table

    table12.columns[0].width = Inches(2.9)
    table12.columns[1].width = Inches(1.8)
    table12.columns[2].width = Inches(1.6)
    table12.columns[3].width = Inches(2.0)
    table12.columns[4].width = Inches(1.8)
    table12.columns[5].width = Inches(1.633)

    headers12 = ["Configuration", "Evidence Diversity", "CRR", "UCR (Lower Better)", "Parity (Jaccard)", "Rubric (1–5)"]
    data12 = [
        ["Config 1: Single prompt", "0.22", "n/a", "90.9%", "0.32", "2.4"],
        ["Config 2: Multi-perspective", "0.48", "38.0%", "68.2%", "0.93", "3.1"],
        ["Config 3: Unmoderated triad", "0.68", "25.0%", "86.4%", "1.00", "3.5"],
        ["Config 4: Full system", "1.00", "100.0%", "0.0%*", "1.00", "4.7"],
    ]

    for col_idx, text in enumerate(headers12):
        cell = table12.cell(0, col_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_BLACK
        p = cell.text_frame.paragraphs[0]
        p.text = text
        p.font.name = FONT_FAMILY
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE
        p.alignment = PP_ALIGN.CENTER

    for row_idx, row in enumerate(data12):
        is_c4 = row_idx == 3
        bg_col = COLOR_LIGHT_BG if row_idx % 2 == 1 else COLOR_WHITE
        for col_idx, val in enumerate(row):
            cell = table12.cell(row_idx + 1, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg_col
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = FONT_FAMILY
            p.font.size = Pt(9.5)
            p.font.bold = is_c4
            p.font.color.rgb = COLOR_BLACK
            p.alignment = PP_ALIGN.CENTER if col_idx > 0 else PP_ALIGN.LEFT

    w12_bot = Inches(5.7)
    h12_bot = Inches(2.7)
    t12_bot = Inches(4.35)

    tf12_l = add_card(s12, Inches(0.8), t12_bot, w12_bot, h12_bot, title="What the Pilot Supports")
    add_bullet(tf12_l, "Diversity:", "Debate configurations cite more domains than a single prompt.", pt_size=9.2)
    add_bullet(tf12_l, "Sequencing:", "Without the graph, prerequisite violations stay high (68–91%).", pt_size=9.2)
    add_bullet(tf12_l, "Parity:", "Matched pairs diverge under a single prompt (J = 0.32); Configs 3 and 4 reach parity.", pt_size=9.2)

    tf12_r = add_card(s12, Inches(6.8), t12_bot, w12_bot, h12_bot, title="What It Does NOT Show (Critical Candor)")
    add_bullet(tf12_r, "*UCR Invariant:", "*UCR 0.0% holds by construction: the graph defines and enforces violations.", pt_size=9.2)
    add_bullet(tf12_r, "Shared Parity:", "Parity 1.00 is shared by Config 3, so it is not unique to the Moderator or graph.", pt_size=9.2)
    add_bullet(tf12_r, "Attribution:", "Does not show which component drives the gains, run-to-run stability, or real-user outcomes.", pt_size=9.2)

    # =========================================================================
    # SLIDE 13: Case Walkthrough: "Priya"
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    set_white_bg(s13)
    add_header(s13, "Case Walkthrough: \"Priya\"", "A scripted demonstration of the gate, disputes and override", slide_num=13)

    w13 = Inches(3.75)
    h13 = Inches(3.8)
    t13 = Inches(1.5)

    tf13_1 = add_card(s13, Inches(0.8), t13, w13, h13, title="Scenario")
    add_bullet(tf13_1, "Profile:", "3rd-year CSE, Tier-3 college, Python basics, ₹3,000 per month.", pt_size=9.2)
    add_bullet(tf13_1, "Goal:", "ML infrastructure engineer in 4 months.", pt_size=9.2)
    add_bullet(tf13_1, "Risk:", "₹1,20,000 loan for a bootcamp.", pt_size=9.2)
    add_bullet(tf13_1, "Single prompt:", "affirms the goal and promises senior roles.", pt_size=9.2)

    tf13_2 = add_card(s13, Inches(4.78), t13, w13, h13, title="Triad Deliberation")
    add_bullet(tf13_2, "Planner:", "data-wrangling sprints and a portfolio.", pt_size=9.2)
    add_bullet(tf13_2, "Critic:", "missing linear algebra, probability, OS.", pt_size=9.2)
    add_bullet(tf13_2, "Ethics-Reviewer:", "advises against the loan; suggests free courses and open-source pull requests.", pt_size=9.2)

    tf13_3 = add_card(s13, Inches(8.76), t13, w13, h13, title="Gate and Override")
    add_bullet(tf13_3, "Gate:", "friction 0.35 + prerequisite gap 0.15 = 0.50 >= 0.45, and Delta_prereq > 0.", pt_size=9.2, bold_color=COLOR_BLACK)
    add_bullet(tf13_3, "Override:", "sliders in Streamlit; zero-debt path chosen.", pt_size=9.2)

    tf13_bot = add_card(s13, Inches(0.8), Inches(5.5), Inches(11.733), Inches(1.4), title="Fairness & Calibration Note")
    add_bullet(tf13_bot, "Fairness note:", "socioeconomic risk (0.20) is shown to the counselor as context but is not added to the gate score, so lower-income students are not gated more often.", pt_size=9.2)
    add_bullet(tf13_bot, "Calibration note:", "The 0.45 threshold is a heuristic setting and the score is uncalibrated.", pt_size=9.2)

    # =========================================================================
    # SLIDE 14: Limitations, Future Work and Conclusion
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    set_white_bg(s14)
    add_header(s14, "Limitations, Future Work and Conclusion", "Transparent boundary conditions and the empirical roadmap", slide_num=14)

    w14 = Inches(5.7)
    h14 = Inches(4.1)
    t14 = Inches(1.5)

    tf14_l = add_card(s14, Inches(0.8), t14, w14, h14, title="Threats to Validity")
    add_bullet(tf14_l, "Circular UCR:", "Config 4 is scored by the graph it uses.", pt_size=9.2)
    add_bullet(tf14_l, "Small sample:", "10 pairs, one run, no confidence intervals.", pt_size=9.2)
    add_bullet(tf14_l, "Rubric:", "not validated with blinded raters.", pt_size=9.2)
    add_bullet(tf14_l, "Uncertainty score:", "is hand-weighted and uncalibrated.", pt_size=9.2)
    add_bullet(tf14_l, "Model family:", "One model family; no component ablations.", pt_size=9.2)
    add_bullet(tf14_l, "Data source:", "Synthetic, confounded pairs; US-based O*NET and BLS data.", pt_size=9.2)
    add_bullet(tf14_l, "Real users:", "Override untested with real users; latency about 4.5 s per debate turn.", pt_size=9.2)

    tf14_r = add_card(s14, Inches(6.8), t14, w14, h14, title="Validation Plan")
    add_bullet(tf14_r, "Ablations:", "Component ablations (graph only, no Moderator, no Chroma).", pt_size=9.2)
    add_bullet(tf14_r, "Baselines:", "Compute-matched majority-vote baselines.", pt_size=9.2)
    add_bullet(tf14_r, "Statistics:", "Repeated runs with confidence intervals and significance tests.", pt_size=9.2)
    add_bullet(tf14_r, "Blinded rubric:", "Blinded rubric with inter-rater agreement.", pt_size=9.2)
    add_bullet(tf14_r, "Calibration:", "Calibration and threshold sensitivity.", pt_size=9.2)
    add_bullet(tf14_r, "Real users:", "Real student and counselor study, India-specific role data.", pt_size=9.2)

    tf14_bot = add_card(s14, Inches(0.8), Inches(5.8), Inches(11.733), Inches(1.1), border_color=COLOR_BLACK)
    add_bullet(tf14_bot, "Conclusion:", "pairing structured disagreement with a deterministic prerequisite check produced transparent, human-overridable advice in a pilot. Claims of superiority await the validation above.", pt_size=9.2)
    add_bullet(tf14_bot, "Thank you · Questions", "", pt_size=9.5, bold_color=COLOR_BLACK)

    # =========================================================================
    # SLIDE 15: References
    # =========================================================================
    s15 = prs.slides.add_slide(blank_layout)
    set_white_bg(s15)
    add_header(s15, "References", "Each source is cited in the body of the deck", slide_num=15)

    w15 = Inches(5.7)
    h15 = Inches(5.4)
    t15 = Inches(1.5)

    tf15_l = add_card(s15, Inches(0.8), t15, w15, h15, title="References [1] - [4]")
    add_bullet(tf15_l, "[1] Du et al. (2024):", "Improving Factuality and Reasoning in Language Models through Multiagent Debate. ICML 2024. arXiv:2305.14325.", pt_size=9.0, space_after=8)
    add_bullet(tf15_l, "[2] Liang et al. (2023):", "Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate. EMNLP 2023.", pt_size=9.0, space_after=8)
    add_bullet(tf15_l, "[3] Smit et al. (2024):", "Should We Be Going MAD? A Critical Look at Multi-Agent Debate Strategies. ICML 2024. arXiv:2311.17371.", pt_size=9.0, space_after=8)
    add_bullet(tf15_l, "[4] ACM/IEEE (2023):", "Computer Science Curricula 2023 (CS2023). Joint Task Force on Computing Curricula.", pt_size=9.0, space_after=8)

    tf15_r = add_card(s15, Inches(6.8), t15, w15, h15, title="References [5] - [8]")
    add_bullet(tf15_r, "[5] Sharma et al. (2024):", "Towards Understanding Sycophancy in Language Models. ICLR 2024. arXiv:2310.13548.", pt_size=9.0, space_after=8)
    add_bullet(tf15_r, "[6] Xiong et al. (2024):", "Can LLMs Express Their Uncertainty? ICLR 2024. arXiv:2306.13063.", pt_size=9.0, space_after=8)
    add_bullet(tf15_r, "[7] Geyik et al. (2019):", "Fairness-Aware Ranking in Search & Recommendation Systems with Application to LinkedIn Talent Search. KDD 2019, pp. 2221–2231.", pt_size=9.0, space_after=8)
    add_bullet(tf15_r, "[8] Buçinca et al. (2021):", "To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making. PACMHCI 5(CSCW1), Art. 188.", pt_size=9.0, space_after=8)

    output_path = "docs/FINAL_PRESENTATION_EXACT_15_SLIDES.pptx"
    prs.save(output_path)
    print(f"✅ Successfully generated Exact 15-Slide Master Deck at: {output_path}")

if __name__ == "__main__":
    create_deck()
