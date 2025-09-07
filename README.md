# Smart-Resume-Reviewer
An AI-powered Smart Resume Reviewer using LLMs that analyzes resumes, matches them with job descriptions, and provides tailored feedback with improvement suggestions
# Smart Resume Reviewer

An AI-powered tool that reviews resumes and provides *targeted, constructive feedback* based on a selected job role and/or job description.  
Built for *Hackathon 2025*.

---

## 🚀 Problem Statement
Recruiters and ATS (Applicant Tracking Systems) reject a large percentage of resumes because of:
- Missing keywords
- Poor formatting
- Lack of role-specific skills

Freshers often struggle to tailor resumes for specific job descriptions.

---

## 💡 Our Solution
We built *Smart Resume Reviewer* that:
- 📂 Uploads resumes (PDF, DOCX, TXT)  
- 🎯 Analyzes skills coverage for a selected *job role*  
- 📊 Compares resume with *job descriptions*  
- 📖 Calculates readability & resume impact  
- ✅ Suggests *actionable improvements*  
- 🤖 (Optional) Uses *LLM (GPT)* for crisp personalized suggestions  

---

## 🛠 Tech Stack
- *Frontend/UI*: Streamlit  
- *Backend/Logic*: Python  
- *Libraries*: pdfplumber, docx2txt, scikit-learn, spaCy, textstat, rapidfuzz  
- *(Optional)*: OpenAI API for advanced suggestions  

---

## ⚙ Features
- Resume upload (PDF, DOCX, TXT)  
- Role-specific skills match (must-have & missing skills)  
- Job description similarity score  
- Readability score (ATS friendly check)  
- Action verbs & impact check  
- LLM-based improvement tips (if API key is available)  

---

## 📸 Demo Screenshots
(Add 2–3 screenshots of your app UI here)

---

## 🏗 System Architecture
```mermaid
flowchart TD
    A[Upload Resume] --> B[Text Extraction]
    B --> C[Preprocessing & Cleaning]
    C --> D[Role / JD Matching]
    D --> E[Skills Coverage, Readability, Action Verbs]
    E --> F[Feedback & Score Display]
    F --> G[Optional LLM Suggestions]
