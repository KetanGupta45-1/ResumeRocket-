from langchain_core.messages import HumanMessage
from langchain_core.prompts import PromptTemplate
from Model.initalise_model import initiate_model
from Parser.resume_text_extract import extract_text
from Parser.fix_json import fix_json

class ResumeParser:
    def __init__(self, pdf_path, token):
        self.pdf_path = pdf_path
        self.token = token
        self.model = None
        self.resume_text = ""
        self.prompt_template = None

    # 1) initialise karo model.
    def initialize_model(self):
        print("Initializing model...")
        try:
            self.model = initiate_model(self.token)
            print("Model initialized successfully.")
        except Exception as e:
            print(f"❌ Failed to initialize model: {e}")
            self.model = None

    # 2) resume se text extract karo.
    def extract_resume_text(self):
        print("Extracting resume text from PDF...")
        try:
            self.resume_text = extract_text(self.pdf_path)
            print("Resume text length (words):", len(self.resume_text.split()))
            if not self.resume_text.strip():
                raise ValueError("Resume text extraction returned empty string.")
        except Exception as e:
            print(f"Error extracting resume text: {e}")
            self.resume_text = ""

    # 3) prompt setup karo, using message placeholder.
    def setup_prompt(self):
        print("🧠 Setting up parsing prompt...")
        schema_example = """
You are a resume parser. Extract information from the resume and return ONLY a valid JSON object. 
Do not include any explanations or markdown. 
Extract full LinkedIn and GitHub URLs in quotes, e.g., "https://github.com/username". 
IMPORTANT: Skills should be in a single list. Categories: Languages, Frameworks, Databases, Styling, Tools, ML/DL, Cloud Computing, DevOps, Cybersecurity, Core Computer Subjects, Soft Skills, Others. 
⚠️ Ensure JSON is syntactically correct, all arrays/objects are closed, and there is nothing outside the JSON. 
Return EXACTLY this structure: 
{{
    "Profile": {{
        "name": "",
        "email": "",
        "phone_number": "",
        "country": "",
        "github": "",
        "linkedin": "",
        "summary": ""
    }},
    "Education": [
        {{
        "institution_name": "",
        "degree": "",
        "field_of_study": "",
        "cgpa_or_percent": "",
        "start_date": "",
        "end_date": ""
        }}
    ],
    "Work Experience": [
        {{
        "company_name": "",
        "job_title": "",
        "location": "",
        "start_date": "",
        "end_date": "",
        "descriptions": []
        }}
    ],
    "Projects": [
        {{
        "project_name": "",
        "tech_stack": "",
        "start_date": "",
        "end_date": "",
        "descriptions": []
        }}
    ],
    "Achievements": [
        {{
        "title": "",
        "organization": "",
        "date": "",
        "description": ""
        }}
    ],
    "Skills": [
        {{
        "category": "",
        "skills": ["skill1", "skill2", "skill3"]
        }}
    ]
}}  

Resume Text: {resume_text} JSON Output (no markdown, just pure JSON):
"""
        self.prompt_template = PromptTemplate(template=schema_example, input_variables=['resume_text'])
        print("Prompt template ready.")

    
    def process_resume(self):
        if not self.model or not self.resume_text or not self.prompt_template:
            print("Ensure model, text, and prompt are ready before processing.")
            return None
        
        try:
            prompt = self.prompt_template.format(resume_text=self.resume_text)
            human_msg = HumanMessage(content=prompt)
            response = self.model.invoke([human_msg])
            raw_output = response.content.strip()
            return fix_json(raw_output)
        
        except Exception as e:
            print(f"❌ Error during resume processing: {e}")
            return None
