💼 Resume Analysis & ATS Matching System

A comprehensive AI-powered system for resume parsing, skill matching, and ATS (Applicant Tracking System) optimization.

🧾 Overview

This system provides end-to-end resume analysis with the following capabilities:

Resume Parsing: Extract structured information from PDF resumes

Skill Matching: Perform semantic matching between resume skills and job requirements

ATS Scoring: Calculate compatibility scores for job applications

Resume Improvement: Get AI-powered suggestions for enhancing resume sections

Skill Inference: Automatically expand related skills based on existing ones

🏗️ Architecture Overview
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

🧩 Architecture Components
Layer	Component	Purpose
📥 Input	Resume PDF, Job Description	Raw data ingestion
🔍 Processing	Parser, Skill Extractor, Semantic Matcher	Data extraction & analysis
🧠 Intelligence	Skill Inference, Embedding Models	AI-powered insights
📊 Scoring	ATS Engine, Match Calculator	Compatibility assessment
✨ Enhancement	Improvement Engine	Optimization suggestions
🎯 Output	Final Report, Scores, Recommendations	Actionable insights
📂 Project Structure
project/
├── 📁 Matching/                    # Core matching functionality
│   ├── SkillMatcher.py             # Main matching pipeline
│   ├── semantic_skill_matcher.py   # Semantic similarity matching
│   ├── skill_inference.py          # Skill expansion logic
│   ├── skill_inference_map.py      # Skill relationship mappings
│   ├── calculate_skill_match.py    # Match percentage calculation
│   ├── aggregate_score.py          # ATS scoring algorithm
│   ├── build_embeddings.py         # Embedding generation/caching
│   ├── compute_similarity.py       # Cosine similarity computation
│   ├── config.py                   # Configuration settings
│   ├── embed_text.py               # Text embedding utilities
│   ├── expand_skill.py             # Compound skill expansion
│   ├── extract_job_skill.py        # Job description skill extraction
│   ├── hybrid_match.py             # Hybrid matching strategies
│   ├── load_embedding.py           # Embedding loading utilities
│   ├── normalize_text.py           # Text normalization
│   ├── save_embedding.py           # Embedding saving utilities
│   └── skill_mapping.py            # Skill normalization mappings
│
├── 📁 Model/
│   └── initialise_model.py         # LLM model initialization
│
├── 📁 Parser/
│   ├── ResumeParser.py             # Main resume parsing class
│   ├── fix_json.py                 # JSON repair utilities
│   └── resume_text_extract.py      # PDF text extraction
│
├── 📁 Json_Extraction/
│   ├── skills_json.py              # Skill extraction from JSON
│   └── proje_exp_ach_json.py       # Section-specific extraction
│
├── 📁 Improvements/
│   └── ResumeImprovement.py        # Resume enhancement module
│
├── 📄 main.py                      # FastAPI application entry point
├── 📄 requirements.txt             # Python dependencies
├── 📄 parsed_resume.json           # Sample parsed resume output
└── 📄 skill_embeddings.pt          # Cached skill embeddings

📦 Directory Overview
Directory	Purpose	Key Files
📁 Matching/	Core matching & scoring logic	SkillMatcher.py, semantic_skill_matcher.py, aggregate_score.py
📁 Model/	AI model initialization	initialise_model.py
📁 Parser/	Resume parsing utilities	ResumeParser.py, resume_text_extract.py
📁 Json_Extraction/	JSON data extraction	skills_json.py, proje_exp_ach_json.py
📁 Improvements/	Resume enhancement module	ResumeImprovement.py
📄 Root Files	Application entry & dependencies	main.py, requirements.txt, skill_embeddings.pt
🚀 Features
1. Resume Parsing

Extract structured data from PDF resumes

Parse profile info, education, work experience, projects, and achievements

Handle malformed JSON with robust repair mechanisms

2. Skill Matching & ATS Scoring

Semantic Matching: Uses Sentence Transformers for intelligent matching

ATS Score: Percentage-based compatibility scoring

Confidence Threshold: Configurable (default: 0.75)

3. Multi-Level Analysis

Direct and inferred skill matches

Weighted scoring (70% job coverage, 30% resume breadth)

4. Skill Inference

Automatic expansion of related skills

Domain-specific mappings (AI/ML, Web Dev, Data Science, etc.)

Configurable inference toggle

5. Resume Improvement

AI-powered section-level improvements

Context-aware feedback based on job roles

Professional phrasing and formatting suggestions

🛠️ Installation
Prerequisites

Python 3.8+

Groq API key for LLM access

# Clone the repository
git clone https://github.com/yourusername/resume-ats-analyzer.git
cd resume-ats-analyzer

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py

📊 Output Metrics
Metric	Description
🧮 ATS Score	Overall compatibility percentage
🎯 Match Percentage	Weighted skill coverage
🧩 Matched Skills	Skill pairs with similarity scores
⚠️ Unmatched Skills	Missing or mismatched skills
🔍 Inferred Skills	Automatically expanded related skills
📈 Confidence Levels	Individual match confidence
🚨 Error Handling

Handles the following gracefully:

Malformed PDF files

Invalid JSON from LLM

Network timeouts

Missing required fields

Embedding generation failures

⚡ Performance

Embedding Cache: Speeds up repeated skill comparisons

Batch Processing: Efficient vector embedding

Memory Efficient: GPU-optimized tensor operations

Parallel Processing: Faster multi-skill comparisons

🔮 Future Enhancements

🌐 Multi-language support

🧭 Industry-specific skill mappings

🤝 Real-time collaboration

📈 Advanced ATS optimization

🔗 Job board integration

🧾 Resume template generation

🤝 Contributing

Fork the repository

Create a new feature branch

Commit your changes

Add tests (if applicable)

Submit a Pull Request

📄 License

This project is licensed under the MIT License — see the LICENSE file for details.

🆘 Support

For support and inquiries:

📘 Check the documentation

🐞 Open an issue on GitHub

💬 Contact the development team
