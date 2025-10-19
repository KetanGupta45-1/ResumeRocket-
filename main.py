from fastapi import FastAPI
import json
from fastapi import FastAPI, UploadFile, File, Form
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware
from Improvements.ResumeImprovement import ResumeImprovement
from Matching.SkillMatcher import SkillMatcher
from Parser.ResumeParser import ResumeParser


api_token = "add key here"
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # allow all origins
    allow_credentials=True,
    allow_methods=["*"],       # allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],       # allow all headers (Content-Type, Authorization, etc.)
)

# ===============================
# 🏠 Test Route
# ===============================
@app.get("/")
def root():
    return {"message": "Resume Processing API is live!"}


# ===============================
# 📄 Main Resume Processing Endpoint
# ===============================
@app.post("/sections")
async def process_resume_sections(
    role: str = Form(...),
    description: str = Form(...),
    pdf_file: UploadFile = File(...)
):
    """
    Upload a resume + provide job role and description.
    Returns parsed resume, improved sections, and ATS score.
    """

    # ==============================================================
    # 1️⃣ SAVE UPLOADED PDF
    # ==============================================================
    temp_pdf_path = Path(f"temp_{pdf_file.filename}")
    with open(temp_pdf_path, "wb") as f:
        f.write(await pdf_file.read())


    # ==============================================================
    # 2️⃣ PARSE RESUME (like run_parser.py)
    # ==============================================================
    try:
        parser = ResumeParser(temp_pdf_path, api_token)
        parser.initialize_model()
        parser.extract_resume_text()
        parser.setup_prompt()
        parsed_resume = parser.process_resume()

        if not parsed_resume:
            temp_pdf_path.unlink(missing_ok=True)
            return {"error": "❌ Failed to parse resume"}

        # Save parsed JSON
        parsed_json_path = Path("parsed_resume.json")
        with open(parsed_json_path, "w", encoding="utf-8") as f:
            json.dump(parsed_resume, f, indent=2, ensure_ascii=False)

    except Exception as e:
        temp_pdf_path.unlink(missing_ok=True)
        return {"error": f"❌ Resume parsing failed: {e}"}
    

    # ==============================================================
    # 3️⃣ IMPROVE RESUME SECTIONS (like run_improvement.py)
    # ==============================================================
    try:
        improver = ResumeImprovement(parsed_json_path, api_token, role, debug=False)
        improver.initialize_model()
        sections = improver.extract_sections()
        cleaned_sections = improver.clean_sections(sections)
        improved_sections = improver.improve_sections(cleaned_sections)
    except Exception as e:
        temp_pdf_path.unlink(missing_ok=True)
        return {"error": f"❌ Resume improvement failed: {e}"}

    # ==============================================================
    # 4️⃣ RUN ATS MATCHING (like run_matching.py)
    # ==============================================================
    try:
        matcher = SkillMatcher(str(parsed_json_path), description, api_token)
        ats_result = matcher.run_pipeline()

        # Optional: Extract key metrics
        ats_score = ats_result.get("ATS_Score")
        match_percentage = ats_result["final_results"].get("match_percentage")
        threshold = ats_result["final_results"].get("threshold_used")

    except Exception as e:
        temp_pdf_path.unlink(missing_ok=True)
        return {"error": f"❌ Skill matching failed: {e}"}
    

     # ==============================================================
    # 5️⃣ CLEANUP + FINAL RESPONSE
    # ==============================================================
    temp_pdf_path.unlink(missing_ok=True)

    return {
        "job_role": role,
        "job_description": description,
        "parsed_resume": parsed_resume,
        "improved_sections": improved_sections,
        "ATS": {
            "score": ats_score,
            "match_percentage": match_percentage,
            "threshold": threshold,
            "details": ats_result
        }
    }
