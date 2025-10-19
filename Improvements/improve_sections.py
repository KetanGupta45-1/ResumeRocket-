from Improvements.prompt import generate_resume_prompt
from Improvements.parse_llm_output import parse
from langchain.schema import AIMessage

def improve_sections_core(structured_sections, llm, section_map, role=None, debug=False):
    """Core logic to improve resume sections using the LLM model."""
    improved = {"projects": [], "workExperience": [], "achievements": []}

    for section_key, items in structured_sections.items():
        if debug:
            print(f"🔹 Processing section: {section_key}")

        for item in items:
            title_key = "projectTitle" if section_key == "projects" else "title"
            title = item.get(title_key, "")
            descriptions = item.get("description", [])

            if not descriptions:
                improved[section_key].append({title_key: title, "description": []})
                continue

            prompt = generate_resume_prompt(title, descriptions, section_map[section_key], role=role)
            response = llm.invoke(prompt)
            raw_output = response.content if isinstance(response, AIMessage) else str(response)
            improved_desc = parse(raw_output)

            improved[section_key].append({
                title_key: title,
                "description": improved_desc
            })

            if debug:
                print(f"✅ Improved '{title}' ({len(improved_desc)} lines)")

    if debug:
        print("🎯 All sections improved successfully.")

    return improved
