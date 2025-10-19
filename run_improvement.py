from Improvements.ResumeImprovement import ResumeImprovement

print("🚀 Starting Resume Improvement Pipeline...\n")

# --- Configuration ---
json_path = "parsed_resume.json"     
api_token = "add key here"    
role = "Web Developer"            
debug = True                      


try:
    # Step 1: Initialize
    improver = ResumeImprovement(json_path, api_token, role, debug)
    # Step 2: Load LLM
    improver.initialize_model()
    # Step 3: Extract JSON sections
    sections = improver.extract_sections()
    # Step 4: Clean descriptions
    cleaned_sections = improver.clean_sections(sections)
    # Step 5: Improve using LLM
    improved_sections = improver.improve_sections(cleaned_sections)
    # Step 6 : Display with ease.
    improver.display_sections(improved_sections)
    print("\n🎯 Resume Improvement Complete!\n")

except Exception as e:
    print(f"❌ Pipeline failed: {e}")
