from langchain.prompts import PromptTemplate
from Model.initalise_model import initiate_model
import json
import re

def extract_job_skills(job_description, token=None):
    if not job_description:
        return []

    chat_model = initiate_model(token)
    prompt_template = PromptTemplate.from_template("""
    Extract only the skills mentioned in the following job description (JD).
    Include both technical skills (e.g., programming languages, tools, frameworks) and soft skills (e.g., communication, problem-solving, teamwork).
    Output should be a clean list of skill names only — no explanations, comments, or additional text.
    Do not include generic sentences like “note” or “I have extracted…” etc.
    Example output format:
    ["Python", "JavaScript", "React", "Problem Solving", "Communication"]

    Job Description:
    {job_description}
""")
    formatted = prompt_template.format(job_description=job_description)
    try:
        response = chat_model.invoke(formatted)
        text = response.content.strip()
        text = text.replace('*', '').replace('-', '').replace('•', '')

        try:
            arr = json.loads(text)
        except Exception:
            arr = []
            for line in text.splitlines():
                line = line.strip()
                if not line:
                    continue
                line = re.sub(r'^\d+\.\s*', '', line)
                line = re.sub(r'[^\w\s\-\&\+]', '', line).strip()
                if line:
                    arr.append(line.lower())

        arr = list(dict.fromkeys([a.lower().strip() for a in arr if a and isinstance(a, str)]))
        print(f"extracted skills from jd: {arr}")
        return arr
    except Exception as e:
        print(f"error extracting from jd: {e}")
        return []
