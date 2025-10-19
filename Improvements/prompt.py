def generate_resume_prompt(title, descriptions, section_name, role=None):
    """
    Create a clean prompt for LLM to improve a resume entry.
    """

    role_text = f"for the role of {role}" if role else ""
    desc_block = "\n".join(f"- {desc}" for desc in descriptions)

    prompt = f"""
    You are a professional resume editor. Improve the descriptions for the {section_name} entry titled "{title}" {role_text}.
    Make them concise, official, and impactful with strong action verbs and quantifiable results.
    IMPORTANT: Do not start lines with '-' in the new version.

    Descriptions to improve:
    {desc_block}

    Return the improved descriptions as a list, each item separate. Do not add extra commentary.
    """
    return prompt
