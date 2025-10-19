import os
from Matching.config import EMBEDDING_MODEL, EMBEDDING_CACHE_PATH, EMBEDDING_BATCH_SIZE, CONFIDENCE_THRESHOLD
from Matching.semantic_skill_matcher import semantic_skill_matcher
from Matching.extract_job_skill import extract_job_skills
from Matching.calculate_skill_match import calculate_skill_match
from Matching.aggregate_score import compute_aggregate_score
from Json_Extraction.skills_json import extract_skills
from Matching.skill_inference import expand_skills_with_inference

class SkillMatcher:
    def __init__(self, resume_json_path, job_description, token, use_skill_inference = True):
        self.resume_json_path = resume_json_path
        self.job_description = job_description
        self.token = token
        self.model_name = EMBEDDING_MODEL
        self.cache_path = EMBEDDING_CACHE_PATH
        self.batch_size = EMBEDDING_BATCH_SIZE
        self.confidence_threshold = CONFIDENCE_THRESHOLD
        self.use_skill_inference = use_skill_inference
        self.resume_skills = []
        self.job_skills = []
        self.semantic_results = []
        self.final_skills_for_matching = []
        self.inferred_skills = [] 
        self.final_results = None
        self.project_data = []
        self.ats_score = 0.0

    def extract_resume_data(self):
        if os.path.exists(self.resume_json_path):
            self.resume_skills = extract_skills(self.resume_json_path)
        else:
            self.resume_skills = []
            self.project_data = []

    def extract_job_data(self):
        self.job_skills = extract_job_skills(self.job_description, self.token)

    def expand_skills_with_inference(self):
        """Use the imported function for skill inference"""
        self.final_skills_for_matching, self.inferred_skills = expand_skills_with_inference(
            self.resume_skills, 
            self.use_skill_inference
        )
        # MODIFIED: Add debug output
        if self.use_skill_inference:
            print(f"Skill Inference: {len(self.resume_skills)} original -> {len(self.final_skills_for_matching)} total skills")
            print(f"Inferred skills: {self.inferred_skills}")

    def run_semantic_matching(self):
        # MODIFIED: Use final_skills_for_matching instead of resume_skills
        if not self.final_skills_for_matching or not self.job_skills:
            self.semantic_results = []
        else:
            self.semantic_results = semantic_skill_matcher(
                user_skill_texts=self.final_skills_for_matching,
                target_skill_texts=self.job_skills,
                model_name=self.model_name,
                cache_path=self.cache_path,
                batch_size=self.batch_size
            )

    def compute_final_results(self):
        self.final_results = calculate_skill_match(
            self.semantic_results,
            self.final_skills_for_matching,
            self.job_skills,
            threshold=self.confidence_threshold
        )

        self.ats_score = compute_aggregate_score(
            self.semantic_results, 
            self.job_skills, 
            threshold=self.confidence_threshold
        )

    def run_pipeline(self):
        """
        Runs the full pipeline and returns a structured result dict.
        """
        self.extract_resume_data()
        self.extract_job_data()
        self.expand_skills_with_inference()
        self.run_semantic_matching()
        self.compute_final_results()

        # Build unmatched lists
        matched_job_set = set(self.final_results.get("matched_job_skills", []))
        matched_resume_set = set(self.final_results.get("matched_resume_skills", []))
        
        # MODIFIED: Handle both original and inferred skills in unmatched calculation
        original_resume_set = set(self.resume_skills)
        matched_original_resume = matched_resume_set & original_resume_set

        unmatched_job_skills = [j for j in self.job_skills if j not in matched_job_set]
        unmatched_resume_skills = [r for r in self.resume_skills if r not in matched_original_resume]

        helpful_inferred_skills = []
        for match in self.final_results.get("matched_skills", []):
            resume_skill, job_skill, score = match
            if resume_skill in self.inferred_skills:
                helpful_inferred_skills.append({
                    'inferred_skill': resume_skill,
                    'matched_job_skill': job_skill,
                    'score': score
                })

        results = {
            # Original data
            "resume_skills": self.resume_skills,
            "job_skills": self.job_skills,
            
            # Inference data
            "inferred_skills": self.inferred_skills,
            "final_skills_for_matching": self.final_skills_for_matching,
            "helpful_inferred_skills": helpful_inferred_skills,
            
            # Matching results
            "semantic_results": self.semantic_results,
            "matched_pairs": self.final_results.get("matched_skills", []),
            "matched_job_skills": self.final_results.get("matched_job_skills", []),
            "matched_resume_skills": self.final_results.get("matched_resume_skills", []),
            "unmatched_job_skills": unmatched_job_skills,
            "unmatched_resume_skills": unmatched_resume_skills,
            
            # Scores
            "final_results": {
                "match_percentage": self.final_results.get("match_percentage", 0.0),
                "threshold_used": self.final_results.get("threshold_used", self.confidence_threshold),
            },
            "project_data": self.project_data,
            "ATS_Score": self.ats_score,
            "skill_inference_enabled": self.use_skill_inference
        }

        return results