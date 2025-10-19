from Matching.skill_inference_map import skill_inference_map
from Matching.normalize_text import normalize_skill_text

def expand_skills_with_inference(resume_skills, use_skill_inference=True):
    """
    Simple skill inference: resume_skills + inferred_skills
    Args:
        resume_skills: List of original resume skills
        use_skill_inference: Boolean to enable/disable inference
    
    Returns:
        tuple: (final_skills_for_matching, inferred_skills)
    """
    
    if not use_skill_inference or not resume_skills:
        return resume_skills.copy(), []

    inferred_skills_set = set()
    
    for skill in resume_skills:
        normalized_skill = normalize_skill_text(skill)
        if normalized_skill in skill_inference_map:
            inferred_skills = skill_inference_map[normalized_skill]
            inferred_skills_set.update(inferred_skills)
    
    # MODIFIED: Use normalized comparison to avoid duplicates
    normalized_resume_skills = [normalize_skill_text(s) for s in resume_skills]
    inferred_skills_list = [
        skill for skill in inferred_skills_set 
        if normalize_skill_text(skill) not in normalized_resume_skills
    ]
    
    final_skills_for_matching = list(set(resume_skills + inferred_skills_list))
    
    return final_skills_for_matching, inferred_skills_list