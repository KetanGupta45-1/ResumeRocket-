from Matching.SkillMatcher import SkillMatcher


def display_detailed_summary(result):
    """Detailed summary with comprehensive analysis"""
    print("\n" + "📊 DETAILED SKILL MATCH ANALYSIS")
    print("=" * 50)
    
    # Overall Scores Section
    print("\n🎯 OVERALL SCORES")
    print("-" * 30)
    print(f"• Match Percentage: {result['final_results']['match_percentage']}%")
    print(f"• ATS Score: {result['ATS_Score']}%")
    print(f"• Confidence Threshold: {result['final_results']['threshold_used']}")
    print(f"• Skill Inference: {'ENABLED' if result['skill_inference_enabled'] else 'DISABLED'}")
    
    # Skills Overview Section
    print("\n📈 SKILLS OVERVIEW")
    print("-" * 30)
    print(f"• Resume Skills: {len(result['resume_skills'])}")
    print(f"• Job Skills: {len(result['job_skills'])}")
    print(f"• Skills Matched: {len(result['matched_pairs'])}")
    print(f"• Match Rate: {(len(result['matched_pairs']) / len(result['job_skills']) * 100):.1f}% of job skills covered")
    
    if result['skill_inference_enabled']:
        print(f"• Inferred Skills: {len(result['inferred_skills'])}")
        print(f"• Helpful Inferences: {len(result['helpful_inferred_skills'])}")
        print(f"• Total Skills for Matching: {len(result['final_skills_for_matching'])}")
    
    # Matched Skills Section
    print("\n✅ MATCHED SKILLS")
    print("-" * 30)
    if result['matched_pairs']:
        for i, (resume_skill, job_skill, score) in enumerate(result['matched_pairs'][:10], 1):
            inference_indicator = " 🎯" if resume_skill in result['inferred_skills'] else ""
            print(f"{i}. {resume_skill} → {job_skill} ({score:.3f}){inference_indicator}")
        
        if len(result['matched_pairs']) > 10:
            print(f"... and {len(result['matched_pairs']) - 10} more matches")
    else:
        print("No skills matched above the confidence threshold")
    
    # Helpful Inferred Skills Section
    if result['skill_inference_enabled'] and result['helpful_inferred_skills']:
        print("\n🎯 HELPFUL INFERRED SKILLS")
        print("-" * 30)
        for i, inference in enumerate(result['helpful_inferred_skills'][:5], 1):
            print(f"{i}. {inference['inferred_skill']} → {inference['matched_job_skill']} ({inference['score']:.3f})")
        
        if len(result['helpful_inferred_skills']) > 5:
            print(f"... and {len(result['helpful_inferred_skills']) - 5} more helpful inferences")
    
    # Unmatched Skills Section
    print("\n❌ UNMATCHED JOB SKILLS")
    print("-" * 30)
    if result['unmatched_job_skills']:
        for i, skill in enumerate(result['unmatched_job_skills'][:10], 1):
            print(f"{i}. {skill}")
        
        if len(result['unmatched_job_skills']) > 10:
            print(f"... and {len(result['unmatched_job_skills']) - 10} more unmatched skills")
    else:
        print("All job skills were matched! 🎉")
    
    # Unmatched Resume Skills Section
    print("\n📝 UNMATCHED RESUME SKILLS")
    print("-" * 30)
    if result['unmatched_resume_skills']:
        for i, skill in enumerate(result['unmatched_resume_skills'][:10], 1):
            print(f"{i}. {skill}")
        
        if len(result['unmatched_resume_skills']) > 10:
            print(f"... and {len(result['unmatched_resume_skills']) - 10} more unmatched skills")
    else:
        print("All resume skills were utilized! 🎉")
    
    # Inferred Skills List (if any)
    if result['skill_inference_enabled'] and result['inferred_skills']:
        print("\n🧠 INFERRED SKILLS ADDED")
        print("-" * 30)
        for i, skill in enumerate(result['inferred_skills'][:10], 1):
            helpful = any(inf['inferred_skill'] == skill for inf in result['helpful_inferred_skills'])
            helpful_indicator = " ✅" if helpful else ""
            print(f"{i}. {skill}{helpful_indicator}")
        
        if len(result['inferred_skills']) > 10:
            print(f"... and {len(result['inferred_skills']) - 10} more inferred skills")
    
    # Performance Metrics Section
    print("\n📊 PERFORMANCE METRICS")
    print("-" * 30)
    total_job_skills = len(result['job_skills'])
    matched_job_skills = len(result['matched_job_skills'])
    coverage_percentage = (matched_job_skills / total_job_skills * 100) if total_job_skills > 0 else 0
    
    total_resume_skills = len(result['resume_skills'])
    utilized_resume_skills = len(result['matched_resume_skills'])
    utilization_percentage = (utilized_resume_skills / total_resume_skills * 100) if total_resume_skills > 0 else 0
    
    print(f"• Job Skills Coverage: {matched_job_skills}/{total_job_skills} ({coverage_percentage:.1f}%)")
    print(f"• Resume Skills Utilization: {utilized_resume_skills}/{total_resume_skills} ({utilization_percentage:.1f}%)")
    
    if result['semantic_results']:
        avg_similarity = sum(score for _, _, score in result['semantic_results']) / len(result['semantic_results'])
        max_similarity = max(score for _, _, score in result['semantic_results'])
        print(f"• Average Similarity Score: {avg_similarity:.3f}")
        print(f"• Maximum Similarity Score: {max_similarity:.3f}")
    
    # Recommendations Section
    print("\n💡 RECOMMENDATIONS")
    print("-" * 30)
    
    if coverage_percentage < 50:
        print("• ⚠️  Low job skills coverage - consider adding more relevant skills")
    elif coverage_percentage < 80:
        print("• 📈 Good coverage - focus on high-demand missing skills")
    else:
        print("• ✅ Excellent job skills coverage!")
    
    if utilization_percentage < 50:
        print("• ⚠️  Low resume utilization - highlight your key skills more prominently")
    
    if result['skill_inference_enabled'] and result['helpful_inferred_skills']:
        print(f"• 🎯 Skill inference helped match {len(result['helpful_inferred_skills'])} additional skills")
    
    if result['unmatched_job_skills']:
        print(f"• 🔍 Focus on acquiring: {', '.join(result['unmatched_job_skills'][:3])}")

# Your existing code
resume_path = "parsed_resume.json"

job_description = '''
    Looking for a talented data scientist skilled in Python, machine learning, deep learning, and statistical analysis to build predictive models and extract insights from complex datasets.
    Must have experience with natural language processing (NLP), generative AI, and large language models (LLMs). Strong problem-solving skills and a passion for deriving actionable insights from data are essential.
'''

token = "add key here"

# Run the matcher
matcher = SkillMatcher(resume_path, job_description, token, True)
result = matcher.run_pipeline()
display_detailed_summary(result)

