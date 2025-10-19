from Improvements.improve_sections import improve_sections_core
from Model.initalise_model import initiate_model
from Json_Extraction.proj_exp_ach_json import extract_section
from Improvements.clean_text import clean_text_list
from Improvements.prompt import generate_resume_prompt
from Improvements.parse_llm_output import parse


class ResumeImprovement:
    def __init__(self, json_path, api_token, role=None, debug=False):
        self.json_path = json_path
        self.api_token = api_token
        self.role = role
        self.debug = debug
        self.llm = None
        self.section_map = {
            "projects": "Projects",
            "workExperience": "Work Experience",
            "achievements": "Achievements"
        }



    def initialize_model(self):
        """Initialize the LLM model using provided API token."""
        try:
            if self.debug:
                print("🚀 Initializing LLM model...")
            self.llm = initiate_model(self.api_token)
            if self.debug:
                print("✅ Model initialized successfully.")
        except Exception as e:
            raise RuntimeError(f"❌ Failed to initialize model: {e}")




    def extract_sections(self):
        """Extract structured resume sections (projects, experience, achievements)."""
        try:
            if self.debug:
                print("📄 Extracting resume sections...")

            self.structured_sections = extract_section(self.json_path)
            
            if self.debug:
                print("✅ Sections extracted successfsully.")
            return self.structured_sections

        except Exception as e:
            raise RuntimeError(f"❌ Failed to extract sections: {e}")



    def create_prompt(self, title, descriptions, section_name):
        """Wrapper to generate an LLM prompt."""
        try:
            if self.debug:
                print(f"📝 Creating LLM prompt for section: {section_name}, title: {title}")
            return generate_resume_prompt(title, descriptions, section_name, self.role, self.debug)
        except Exception as e:
            raise RuntimeError(f"❌ Failed to create LLM prompt: {e}")
        
    


    def parse_output(self, raw_output):
        """Wrapper to parse LLM's output."""
        try:
            if self.debug:
                print("🧩 Parsing LLM output text...")
            return parse(raw_output, self.debug)
        except Exception as e:
            raise RuntimeError(f"❌ Failed to parse LLM output: {e}")




    def clean_sections(self, structured_sections):
        """Cleans the description text in each section."""
        if self.debug:
            print("🧹 Cleaning section descriptions...")
        cleaned = {"projects": [], "workExperience": [], "achievements": []}

        for section_key, items in structured_sections.items():
            for item in items:
                title_key = "projectTitle" if section_key == "projects" else "title"
                raw_descriptions = item.get("description", [])
                cleaned_desc = clean_text_list(raw_descriptions) if raw_descriptions else []
                cleaned[section_key].append({
                    title_key: item.get(title_key, ""),
                    "description": cleaned_desc
                })
        if self.debug:
            print("✅ Descriptions cleaned.")
        return cleaned



    def improve_sections(self, structured_sections):
        """Improve resume sections using core function."""
        try:
            if not self.llm:
                raise ValueError("Model not initialized. Run initialize_model() first.")
            if self.debug:
                print("🧠 Improving resume content with LLM...")
            return improve_sections_core(structured_sections, self.llm, self.section_map, self.role, self.debug)
        except Exception as e:
            raise RuntimeError(f"❌ Failed to improve sections: {e}")
        


    def display_sections(self, structured_sections):
        """Print all sections in a clean, readable format."""
        print("\n==============================")
        print("📘 Resume Sections Overview")
        print("==============================\n")

        for section_key, items in structured_sections.items():
            section_title = self.section_map.get(section_key, section_key.capitalize())
            print(f"\n🔹 {section_title}\n")

            for idx, item in enumerate(items, start=1):
                # Pick the right title field
                title = item.get("projectTitle") or item.get("title") or "Untitled"
                print(f"{section_title[:-1]} {idx}: {title}")

                descriptions = item.get("description", [])
                for desc in descriptions:
                    print(f"   - {desc}")
                print()



    
