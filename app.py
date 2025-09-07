import streamlit as st
import pdfplumber
import docx2txt
import re
import textstat
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------- Utility functions ----------
def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(file):
    return docx2txt.process(file)

def clean_text(text):
    return re.sub(r'\s+', ' ', text)

# ---------- Role Skills Dictionary ----------
ROLE_SKILLS = {
    "Software Developer": ["python", "java", "c++", "data structures", "algorithms", "git", "sql"],
    "Data Analyst": ["python", "excel", "sql", "tableau", "powerbi", "data visualization", "statistics"],
    "AI/ML Engineer": ["python", "machine learning", "deep learning", "tensorflow", "pytorch", "nlp", "computer vision"],
    "Web Developer": ["html", "css", "javascript", "react", "nodejs", "mongodb", "rest api"],
    "Cloud Engineer": ["aws", "azure", "gcp", "docker", "kubernetes", "ci/cd", "terraform"]
}

# ---------- Resume Analysis ----------
def analyze_resume(resume_text, target_role, job_desc=None):
    feedback = []
    score = 0

    resume_text_lower = resume_text.lower()

    # Skills Coverage
    skills = ROLE_SKILLS.get(target_role, [])
    matched = [skill for skill in skills if skill in resume_text_lower]
    missing = [skill for skill in skills if skill not in resume_text_lower]

    feedback.append(f" Matched Skills: {', '.join(matched) if matched else 'None'}")
    feedback.append(f" Missing Skills: {', '.join(missing) if missing else 'None'}")
    score += len(matched) * 5

    # JD Similarity
    if job_desc:
        vectorizer = TfidfVectorizer().fit_transform([resume_text, job_desc])
        sim = cosine_similarity(vectorizer[0:1], vectorizer[1:2])[0][0]
        feedback.append(f" Job Description Match: {sim:.2f}")
        score += int(sim * 50)

    # Readability
    readability = textstat.flesch_reading_ease(resume_text)
    feedback.append(f" Readability Score: {readability}")
    if readability < 40:
        feedback.append("⚠ Resume may be too complex, simplify language.")
    else:
        score += 10

    # Action verbs check
    action_verbs = ["developed", "managed", "created", "designed", "implemented", "led", "built"]
    if not any(verb in resume_text_lower for verb in action_verbs):
        feedback.append("⚠ Add action verbs like 'Developed', 'Created', 'Implemented' to show impact.")
    else:
        score += 10

    return score, feedback

# ---------- Streamlit UI ----------
st.title("📄 Smart Resume Reviewer")

uploaded_file = st.file_uploader("Upload your Resume (PDF/DOCX/TXT)", type=["pdf", "docx", "txt"])
target_role = st.selectbox("Select Target Job Role", list(ROLE_SKILLS.keys()))
job_desc = st.text_area("Paste Job Description (Optional)")

if st.button("Analyze Resume"):
    if uploaded_file is not None:
        if uploaded_file.type == "application/pdf":
            resume_text = extract_text_from_pdf(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            resume_text = extract_text_from_docx(uploaded_file)
        else:
            resume_text = uploaded_file.read().decode("utf-8")

        resume_text = clean_text(resume_text)
        score, feedback = analyze_resume(resume_text, target_role, job_desc)

        st.subheader("📊 Resume Review Report")
        st.write(f"Overall Resume Score: *{score}/100*")
        for fb in feedback:
            st.write("- " + fb)
    else:
        st.warning("Please upload a resume file!")