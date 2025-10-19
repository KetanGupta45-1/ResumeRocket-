from Parser.ResumeParser import ResumeParser
import json

pdf_file = "D:/Projects/Machine and Deep Learning/New--/Shivank Resume.pdf"
api_token = "add key here"


parser = ResumeParser(pdf_file, api_token)

parser.initialize_model()
parser.extract_resume_text()
parser.setup_prompt()

parsed_resume = parser.process_resume()

if parsed_resume:
    print("✅ Final parsed resume:")
    print(json.dumps(parsed_resume, indent=2))

    output_path = "parsed_resume.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(parsed_resume, f, indent=2, ensure_ascii=False)

    print(f"✅ Saved parsed resume to: {output_path}")

else:
    print("❌ Resume parsing failed.")
