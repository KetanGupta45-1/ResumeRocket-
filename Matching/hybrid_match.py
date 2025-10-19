from Matching.semantic_skill_matcher import semantic_skill_matcher

def hybrid_match(user_skills, job_skills, model_name, cache_path, batch_size):
    return semantic_skill_matcher(user_skills, job_skills, model_name, cache_path, batch_size)
