def compute_aggregate_score(semantic_results, job_skills, threshold=0.75):
    """
    Compute an ATS-style score for how well job_skills are covered by semantic_results.

    - semantic_results: list of tuples (resume_skill, job_skill, score) where score in [0,1]
    - job_skills: list of job skill names (strings)
    - threshold: minimum similarity to count as a valid match (default 0.75)

    Returns:
        float: ATS score as percentage (0.0 - 100.0), rounded to 2 decimals.
    """
    if not semantic_results or not job_skills:
        return 0.0

    best_scores = {js: 0.0 for js in job_skills}
    for resume_skill, job_skill, score in semantic_results:
        if job_skill in best_scores and score > best_scores[job_skill]:
            best_scores[job_skill] = score

    avg_score = sum(best_scores.values()) / len(job_skills)
    ats_percentage = avg_score * 100.0
    return round(ats_percentage, 2)
