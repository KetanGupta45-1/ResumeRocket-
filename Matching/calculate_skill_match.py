from Matching.config import CONFIDENCE_THRESHOLD

def calculate_skill_match(semantic_results, resume_skills, job_skills, threshold=None):
    """
    Calculate weighted skill match percentage based on semantic similarity.

    - semantic_results: list of tuples (resume_skill, job_skill, score)
    - resume_skills: list of resume skill strings
    - job_skills: list of job skill strings
    - threshold: optional threshold (float). If None, uses CONFIDENCE_THRESHOLD from config.

    Returns:
        dict {
            "match_percentage": float (0-100),
            "matched_skills": list of (resume_skill, job_skill, score) that met threshold,
            "matched_job_skills": list of job skills matched,
            "matched_resume_skills": list of resume skills matched
        }
    """
    if threshold is None:
        threshold = CONFIDENCE_THRESHOLD

    if not job_skills:
        return {"match_percentage": 0.0, "matched_skills": [], "matched_job_skills": [], "matched_resume_skills": []}
    if not resume_skills:
        return {"match_percentage": 0.0, "matched_skills": [], "matched_job_skills": [], "matched_resume_skills": []}

    matched = [(a, b, s) for a, b, s in semantic_results if s >= threshold]

    matched_job_set = set(b for _, b, _ in matched)
    matched_resume_set = set(a for a, _, _ in matched)

    job_covered = len(matched_job_set) / len(job_skills) if job_skills else 0.0
    resume_covered = len(matched_resume_set) / len(resume_skills) if resume_skills else 0.0

    # Weighted: prioritize covering job skills (70%) and then resume breadth (30%)
    weighted_score = (0.7 * job_covered + 0.3 * resume_covered) * 100.0

    return {
        "match_percentage": round(weighted_score, 2),
        "matched_skills": matched,
        "matched_job_skills": list(matched_job_set),
        "matched_resume_skills": list(matched_resume_set),
        "threshold_used": threshold
    }