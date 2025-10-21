Resume Analysis & ATS Matching System
A comprehensive AI-powered system for resume parsing, skill matching, and ATS (Applicant Tracking System) optimization.



📋 Overview
This system provides end-to-end resume analysis with the following capabilities:
Resume Parsing: Extract structured information from PDF resumes
Skill Matching: Semantic matching between resume skills and job requirements
ATS Scoring: Calculate compatibility scores for job applications
Resume Improvement: AI-powered suggestions for enhancing resume sections
Skill Inference: Automatic expansion of related skills based on existing ones



🏗️ Architecture Overview
```mermaid
graph TB
    A[📄 Resume PDF] --> B[🔍 Parser Module]
    B --> C[📊 Structured JSON Data]
    
    D[📋 Job Description] --> E[🎯 Skill Extractor]
    E --> F[🔧 Job Skills]
    
    C --> G[🧠 Skill Matcher]
    F --> G
    
    G --> H[⚡ Semantic Matching]
    H --> I[💡 Skill Inference]
    I --> J[📈 ATS Scoring]
    
    J --> K[✨ Improvement Engine]
    K --> L[🎊 Final Report]
    
    M[⚙️ Config] --> G
    M --> H
    M --> J
    
    N[💾 Embedding Cache] --> H
    
    subgraph "Core Processing Pipeline"
        B --> G --> J --> L
    end
    
    subgraph "AI Components"
        H --> I
    end
```

### Architecture Components:

| Layer | Component | Purpose |
|-------|-----------|---------|
| **📥 Input** | Resume PDF, Job Description | Raw data ingestion |
| **🔍 Processing** | Parser, Skill Extractor, Semantic Matcher | Data extraction & analysis |
| **🧠 Intelligence** | Skill Inference, Embedding Models | AI-powered insights |
| **📊 Scoring** | ATS Engine, Match Calculator | Compatibility assessment |
| **✨ Enhancement** | Improvement Engine | Optimization suggestions |
| **🎯 Output** | Final Report, Scores, Recommendations | Actionable insights |





Architecture Components:
Layer	Component	Purpose
📥 Input	Resume PDF, Job Description	Raw data ingestion
🔍 Processing	Parser, Skill Extractor, Semantic Matcher	Data extraction & analysis
🧠 Intelligence	Skill Inference, Embedding Models	AI-powered insights
📊 Scoring	ATS Engine, Match Calculator	Compatibility assessment
✨ Enhancement	Improvement Engine	Optimization suggestions
🎯 Output	Final Report, Scores, Recommendations	Actionable insights
🏗️ Project Structure



project/
├── Matching/                    # Core matching functionality
│   ├── SkillMatcher.py         # Main matching pipeline
│   ├── semantic_skill_matcher.py # Semantic similarity matching
│   ├── skill_inference.py      # Skill expansion logic
│   ├── skill_inference_map.py  # Skill relationship mappings
│   ├── calculate_skill_match.py # Match percentage calculation
│   ├── aggregate_score.py      # ATS scoring algorithm
│   ├── build_embeddings.py     # Embedding generation/caching
│   ├── compute_similarity.py   # Cosine similarity computation
│   ├── config.py              # Configuration settings
│   ├── embed_text.py          # Text embedding utilities
│   ├── expand_skill.py        # Compound skill expansion
│   ├── extract_job_skill.py   # Job description skill extraction
│   ├── hybrid_match.py        # Hybrid matching strategies
│   ├── load_embedding.py      # Embedding loading utilities
│   ├── normalize_text.py      # Text normalization
│   ├── save_embedding.py      # Embedding saving utilities
│   └── skill_mapping.py       # Skill normalization mappings
├── Model/
│   └── initalise_model.py     # LLM model initialization
├── Parser/
│   ├── ResumeParser.py        # Main resume parsing class
│   ├── fix_json.py           # JSON repair utilities
│   ├── resume_text_extract.py # PDF text extraction
│   
├── Json_Extraction/
│   └── skills_json.py        # Skill extraction from JSON
|   └── proje_exp_ach_json.py # Section-specific extraction
|
├── Improvements/
│   └── ResumeImprovement.py  # Resume enhancement module
├── main.py                   # FastAPI application
├── requirements.txt          # Python dependencies
├── parsed_resume.json       # Sample parsed resume output
└── skill_embeddings.pt      # Cached skill embeddings



🚀 Features


1. Resume Parsing
Extract structured data from PDF resumes
Parse profile information, education, work experience, projects, achievements
Handle malformed JSON with robust repair mechanisms


2. Skill Matching & ATS Scoring
Semantic Matching: Uses sentence transformers for intelligent skill matching
ATS Score: Percentage-based compatibility scoring
Confidence Threshold: Configurable matching threshold (default: 0.75)

3. Multi-level Analysis:
Direct skill matches
Inferred skill matches
Weighted scoring (70% job coverage, 30% resume breadth)


4. Skill Inference
Automatic expansion of related skills
Domain-specific inference mappings (AI/ML, Web Dev, Data Science, etc.)
Configurable inference enabling/disabling


5. Resume Improvement
AI-powered section enhancement
Context-aware improvements based on job role
Professional phrasing and formatting suggestions


🛠️ Installation
Prerequisites
Python 3.8+
Groq API key for LLM access

Setup
Clone the repository:

bash
git clone <repository-url>
cd project
Create virtual environment:

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
pip install -r requirements.txt
Set up environment variables:

bash
export GROQ_API_KEY="your_groq_api_key_here"


📖 Usage
API Endpoints
Main Processing Endpoint
http
POST /sections
Content-Type: multipart/form-data

Parameters:
- role: string (Job role/title)
- description: string (Job description)
- pdf_file: file (Resume PDF)
Example Response:

json
{
  "job_role": "Software Engineer",
  "job_description": "Looking for Python developer...",
  "parsed_resume": { ... },
  "improved_sections": { ... },
  "ATS": {
    "score": 85.5,
    "match_percentage": 78.2,
    "threshold": 0.75,
    "details": {
      "resume_skills": ["python", "javascript", "react"],
      "job_skills": ["python", "django", "aws"],
      "matched_pairs": [...],
      "unmatched_job_skills": [...],
      "inferred_skills": [...]
    }
  }
}
Standalone Components

Resume Parsing
from Parser.ResumeParser import ResumeParser
parser = ResumeParser("resume.pdf", "your_api_token")
parser.initialize_model()
parser.extract_resume_text()
parser.setup_prompt()
parsed_data = parser.process_resume()

Skill Matching
from Matching.SkillMatcher import SkillMatcher
matcher = SkillMatcher(
    resume_json_path="parsed_resume.json",
    job_description="Job description text",
    token="your_api_token",
    use_skill_inference=True
)
results = matcher.run_pipeline()


Resume Improvement
from Improvements.ResumeImprovement import ResumeImprovement
improver = ResumeImprovement(
    json_path="parsed_resume.json",
    api_token="your_api_token",
    role="Target Job Role"
)
improved_sections = improver.improve_sections()



⚙️ Configuration
Key configuration in Matching/config.py:
EMBEDDING_MODEL = "all-MiniLM-L6-v2"  # Sentence transformer model
CONFIDENCE_THRESHOLD = 0.75           # Minimum similarity score
EMBEDDING_BATCH_SIZE = 64            # Batch size for embeddings
EMBEDDING_CACHE_PATH = "skill_embeddings.pt"  # Cache file


🔧 Customization
Adding New Skill Mappings
Edit Matching/skill_inference_map.py:

skill_inference_map = {
    'your_skill': [
        'related_skill_1',
        'related_skill_2',
        # ...
    ],
    # Add more mappings...
}
Modifying Matching Threshold
Update in Matching/config.py:
python
CONFIDENCE_THRESHOLD = 0.80  # Higher for stricter matching


📊 Output Metrics
The system provides comprehensive analysis including:
ATS Score: Overall compatibility percentage
Match Percentage: Weighted skill coverage
Matched Skills: Specific skill pairs with similarity scores
Unmatched Skills: Skills lacking in resume or job description
Inferred Skills: Automatically expanded relevant skills
Confidence Levels: Individual match confidence scores



🚨 Error Handling
The system includes robust error handling for:
Malformed PDF files
Invalid JSON responses from LLM
Network timeouts
Missing required fields
Embedding generation failures



📈 Performance
Embedding Cache: Skills embeddings are cached for faster subsequent runs
Batch Processing: Efficient batch processing of text embeddings
Memory Efficient: GPU-optimized tensor operations
Parallel Processing: Concurrent skill matching operations



🔮 Future Enhancements
Multi-language support
Industry-specific skill mappings
Real-time collaboration features
Advanced ATS optimization suggestions
Integration with job boards
Resume template generation



🤝 Contributing
Fork the repository
Create a feature branch
Make your changes
Add tests if applicable
Submit a pull request


📄 License
This project is licensed under the MIT License - see the LICENSE file for details.



🆘 Support
For support and questions:
Check the documentation
Open an issue on GitHub
Contact the development team

