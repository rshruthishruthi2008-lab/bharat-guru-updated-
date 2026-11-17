import streamlit as st
from PIL import Image

st.set_page_config(page_title="BharatGuru  ", layout="wide")
st.title("🚀 BharatGuru")
st.markdown("### FINAL 16.0 | Syllabus + PYQ + Marking Scheme As Per Exam | Presentation Ready")

# CHECK API
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("❌ Add GOOGLE_API_KEY in Secrets")
    st.stop()
st.success("✅ Google API Ready - FREE")

# ALL EXAMS - AS YOU ASKED
all_exams = [
    "PUC I & II", "PUC I", "PUC II", "CBSE 11", "CBSE 12", "SSLC Karnataka",
    "Degree BCom", "Degree BBA", "Degree BCA", "Mangalore Univ", "Bangalore Univ", "VTU BTech",
    "UPSC CSE (IAS/IPS)", "UPSC CAPF", "UPSC NDA/CDS",
    "KPSC KAS", "KPSC FDA/SDA", "KPSC PSI/PC",
    "Railway RRB NTPC", "Railway Group D", "Railway JE/ALP/RPF",
    "Banking IBPS PO/Clerk", "Banking SBI PO/Clerk", "Banking RBI Grade B",
    "SSC CGL", "SSC CHSL", "SSC GD/MTS", "NDA", "CDS", "AFCAT", "KCET", "JEE", "NEET", "CUET"
]

all_langs = ["English", "Kannada", "Hinglish", "Hindi", "Telugu", "Tamil", "Malayalam", "Marathi", "Urdu", "Gujarati", "Bengali", "Punjabi"]

# SYLLABUS AS PER EXAM
syllabus_map = {
    "UPSC CSE (IAS/IPS)": ["UPSC CSE 2025 - Prelims+Mains Syllabus", "UPSC 2024 Old Pattern"],
    "KPSC KAS": ["KPSC KAS New 2025 Syllabus - Kannada + English", "KPSC FDA/SDA Syllabus 2025"],
    "Railway RRB NTPC": ["RRB NTPC 2025 Syllabus - Maths 30 + Reasoning 30 + GK 40", "RRB Group D Syllabus 2025"],
    "Banking IBPS PO/Clerk": ["IBPS PO 2025 Syllabus - Quant+Reasoning+English", "SBI PO 2025", "RBI Grade B Syllabus"],
    "NDA": ["NDA 2025 Syllabus - Maths 300M + GAT 600M", "CDS Syllabus"],
    "PUC I & II": ["Karnataka PUC New 2025-26 Syllabus", "CBSE New 2025-26", "Old 2024-25"]
}

# MARKING SCHEME AS PER EXAM - AUTO
marking_map = {
    "PUC I & II": "PUC: 1M=1 line, 2M=3 points, 5M=10-12 points with format, 10M=full page with example. No GST for PUC Karnataka.",
    "UPSC CSE (IAS/IPS)": "UPSC Mains: 10M=150 words, 15M=250 words. Structure: Intro(20%) Body(60%) Conclusion(20%) + Current Affairs + SC Cases. Prelims: 2M per Q, -0.66 negative.",
    "Railway RRB NTPC": "RRB NTPC: Stage1 - 1M per Q, No negative. Stage2 - 1M, 1/3 negative. Distribution: Maths 30, Reasoning 30, GK 40. Time 90 min.",
    "Banking IBPS PO/Clerk": "IBPS PO: Prelims 1M per Q, 0.25 negative. Mains 155Q 200M. Sectional cutoff. English 40M, Reasoning 40M, Quant 50M.",
    "KPSC KAS": "KPSC KAS: Prelims 2M per Q, 0.5 negative. Mains 9 papers 250M each. Q pattern: 10M=150 words, 15M=250 words. Kannada compulsory.",
    "NDA": "NDA: Maths 120Q 300M (2.5 per Q, -0.83 negative), GAT 150Q 600M (4 per Q, -1.33 negative). Total 900M.",
    "SSC CGL": "SSC CGL: 2M per Q, 0.5 negative. Tier1 100Q 200M, 60 min. Maths 25, Reasoning 25, English 25, GK 25.",
    "Banking RBI Grade B": "RBI Grade B: Phase1 200M, Phase2 300M, Interview 75M. 1M per Q, 0.25 negative."
}

c1, c2 = st.columns(2)
with c1:
    exam = st.selectbox("📚 SELECT EXAM (UPSC/Railway/Banking/KPSC/NDA/PUC)", all_exams, index=12)
    subject = st.selectbox("📖 Subject", ["General Studies", "Computer Science", "Accountancy", "Business Studies", "Polity", "History", "Geography", "Maths", "Reasoning", "Economics", "Science", "Current Affairs", "Karnataka GK"], index=0)
with c2:
    lang = st.selectbox("🌐 Language (16 Indian)", all_langs, index=0)
    # Auto syllabus as per exam
    syl_options = syllabus_map.get(exam, ["New 2025-26", "Old 2024-25", "NEP 2024-25"])
    syllabus = st.selectbox("📘 Syllabus (Auto as per Exam)", syl_options, index=0)

board = st.selectbox("🏛️ Board / Commission", ["Karnataka State", "CBSE", "UPSC", "KPSC", "Railway Board", "IBPS/SBI/RBI", "SSC", "NDA"], index=2)

# SHOW MARKING SCHEME LIVE
current_marking = marking_map.get(exam, "As per board: 1M objective, 2-3M short, 5-6M medium, 10-15M long answer")
st.info(f"📌 **Marking Scheme for {exam}:** {current_marking}")
st.caption(f"📘 Syllabus: {syllabus}")

doubt = st.text_area(f"❓ Doubt for {exam} - {syllabus}?", height=120, placeholder="Type your doubt... Ex: Explain Article 32 for UPSC / What is Arrays for PUC / Maths shortcut for RRB NTPC")
uploaded = st.file_uploader("📸 Upload Photo / Question Paper", type=["jpg","jpeg","png"])

if st.button("🚀 GET ANSWER + PYQ + MARKING SCHEME", type="primary", use_container_width=True):
    if not doubt and not uploaded:
        st.warning("Please write doubt")
        st.stop()
    try:
        with st.spinner(f"Generating {exam} answer + PYQ + Marking..."):
            import google.generativeai as genai
            genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
            model = genai.GenerativeModel("gemini-1.5-flash")
            
            prompt = f"""
            You are BharatGuru by R. Shruthi - Expert for {exam}
            
            Exam: {exam}
            Syllabus: {syllabus}
            Board: {board}
            Subject: {subject}
            Language: {lang}
            Doubt: {doubt}
            Marking Scheme: {current_marking}
            
            Give answer in EXACT format for presentation:
            
            ### 1. SYLLABUS POINT - {syllabus}
            Mention exact syllabus topic number from {syllabus}
            
            ### 2. EXPLANATION - As per {exam} pattern
            Explain in {lang} - Simple, as per {board} pattern
            
            ### 3. PYQ - PREVIOUS YEAR QUESTIONS (3 PYQs with Year+Marks)
            Must give 3 PYQs from {exam} only:
            Format: Year | Exam | Marks | Question
            Example for UPSC: "UPSC CSE 2023 Mains 15M: Discuss Article 32..."
            Example for Railway: "RRB NTPC 2022 CBT2 1M: What is..."
            Example for Banking: "IBPS PO 2024 Prelims 1M: Find..."
            Example for KPSC: "KPSC KAS 2023 Mains 15M: Explain..."
            Example for PUC: "Karnataka PUC 2024 5M: What is Journal?"
            
            ### 4. MARKING SCHEME BREAKDOWN - {exam}
            How examiner gives marks for this question in {exam}:
            {current_marking}
            Breakdown: If 5M, give 1M for definition, 2M for points, 2M for example. If 15M UPSC, give Intro 3M, Body 9M, Conclusion 3M.
            
            ### 5. MODEL ANSWER - TO GET FULL MARKS IN {exam}
            Write final answer that gets full marks as per {current_marking} and {syllabus}
            
            Language: {lang}
            """
            
            if uploaded:
                img = Image.open(uploaded)
                res = model.generate_content([prompt, img])
            else:
                res = model.generate_content(prompt)
            
            st.success(f"✅ {exam} Answer Ready - With PYQ + Marking Scheme!")
            st.markdown(res.text)
            st.markdown("---")
            st.success(f"📊 Marking Scheme Used: {current_marking}")
            st.info(f"📘 Syllabus: {syllabus} | 🏛️ Board: {board}")
            
    except Exception as e:
        st.error(f"Error: {e}")

st.markdown("---")
st.caption(" 👩‍💻 Made by R. Shruthi | Founder - BharatGuru |")
st.caption("Syllabus + PYQ + Marking Scheme | As Per Selected Exam | UPSC | Railway | Banking | KPSC | NDA | PUC | 16 Languages")