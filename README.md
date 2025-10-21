# 🧠 AI Resume Analyzer & ATS Scoring System

This project is an **AI-powered Resume Analyzer** that evaluates resumes against job descriptions, provides **semantic skill matching**, and calculates an **ATS (Applicant Tracking System) score**. It leverages **Natural Language Processing (NLP)** and **semantic similarity models** to analyze candidate profiles and recommend improvements.

---

## 🚀 Features

- 📄 **Resume Parsing:** Automatically extracts text, skills, and experience from PDF or DOCX resumes.  
- 🧩 **Semantic Skill Matching:** Uses sentence embeddings to compare job requirements with candidate skills.  
- 📊 **ATS Score Calculation:** Computes a weighted score based on keyword and semantic similarity.  
- 💡 **AI-Based Suggestions:** Provides tailored recommendations to enhance resume relevance and ATS compatibility.  
- 🌐 **FastAPI Backend:** RESTful API endpoints for parsing, scoring, and serving AI results.  
- 🧱 **Modular Design:** Each module (parser, scorer, suggestion engine) is independent for easy integration.

---

## 🧩 Project Structure

📂 ai_resume_analyzer/
├── aggregate_score.py # Calculates final ATS score based on job skill match
├── parser.py # Extracts and cleans resume text
├── skill_extractor.py # Identifies skills from resume using NLP models
├── semantic_matcher.py # Computes semantic similarity between job & resume skills
├── improvement_suggester.py # Generates improvement recommendations
├── main.py # FastAPI endpoints (core API)
├── requirements.txt # All required dependencies
└── README.md # This documentation

markdown
Copy code

---

## ⚙️ Tech Stack

| Category | Tools & Libraries |
|-----------|-------------------|
| **Language** | Python 3.10+ |
| **Backend** | FastAPI |
| **NLP Models** | Sentence Transformers (e.g., `all-MiniLM-L6-v2`) |
| **Data Handling** | pandas, numpy |
| **Text Parsing** | PyPDF2, python-docx |
| **Deployment** | Uvicorn, Docker (optional) |

---

## 🧠 How It Works

1. **Upload Resume & Job Description**
   - The API accepts both resume and job description as text or file input.

2. **Skill Extraction**
   - Extracts relevant skills using predefined and model-based skill lists.

3. **Semantic Matching**
   - Uses sentence embeddings to compute similarity between resume skills and job requirements.

4. **Aggregate ATS Score**
   - Combines semantic and keyword scores to compute a final percentage score.

5. **AI-Generated Suggestions**
   - Suggests new keywords, improvements, and missing skills for better alignment.

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---------|-----------|-------------|
| `POST` | `/parse_resume/` | Extracts text from uploaded resume file |
| `POST` | `/match_skills/` | Matches job and resume skills using semantic similarity |
| `POST` | `/compute_score/` | Returns ATS score based on similarity results |
| `POST` | `/suggest_improvements/` | Generates personalized improvement tips |

Example request (JSON):

{
  "resume_text": "Experienced data analyst skilled in Python, SQL, and Power BI.",
  "job_description": "Looking for a data analyst with expertise in Python, SQL, and Tableau."
}
Example response:
{
  "ats_score": 87.5,
  "matched_skills": ["Python", "SQL"],
  "missing_skills": ["Tableau"],
  "suggestions": ["Add Tableau to your skills section for better alignment."]
}

🧪 Local Setup
1️⃣ Clone Repository
bash
Copy code
git clone https://github.com/<your-username>/ai-resume-analyzer.git
cd ai-resume-analyzer
2️⃣ Create Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Run FastAPI Server
bash
Copy code
uvicorn main:app --reload
Server will run at:
👉 http://127.0.0.1:8000

You can test endpoints here:
👉 http://127.0.0.1:8000/docs

📈 Example Output
sql
Copy code
Resume matched 83.6% of job description skills.
✅ Strong Match: Python, SQL, Machine Learning  
⚠️ Missing: Tableau, AWS  
💡 Suggestion: Add Tableau projects to showcase data visualization experience.
🧰 Future Enhancements
Integration with LangChain or OpenAI API for advanced feedback.

Support for multi-language resumes.

Frontend dashboard with real-time visual scoring.

Exportable PDF summary reports for candidates.

🧑‍💻 Author
Ketan Gupta
Data Science Enthusiast | Resume Intelligence Developer

📧 Email: [your.email@example.com]
🔗 GitHub: https://github.com/yourusername

🪪 License
This project is licensed under the MIT License — feel free to use, modify, and distribute it.
