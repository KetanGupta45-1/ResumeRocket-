skill_inference_map = {
    # AI/ML Domain
    'machine learning': [
        'data analysis',
        'exploratory data analysis',
        'data visualization',
        'feature engineering',
        'data preprocessing',
        'statistics',
        'python',
        'pandas',
        'numpy',
        'model evaluation',
        'cross validation'
    ],
    'deep learning': [
        'machine learning',
        'neural networks',
        'pytorch',
        'tensorflow',
        'keras',
        'gradient descent',
        'backpropagation'
    ],
    'natural language processing': [
        'machine learning',
        'text processing',
        'tokenization',
        'text classification',
        'sentiment analysis'
    ],
    'computer vision': [
        'deep learning',
        'image processing',
        'opencv',
        'convolutional neural networks',
        'object detection'
    ],
    
    # Data Science
    'data analysis': [
        'data visualization',
        'statistics',
        'eda',
        'python',
        'pandas',
        'data cleaning',
        'data wrangling'
    ],
    'data science': [
        'machine learning',
        'data analysis',
        'statistics',
        'python',
        'data visualization',
        'big data'
    ],
    
    # NEW: Framework-specific inferences
    'scikit-learn': [
        'machine learning',
        'python',
        'data science',
        'classification',
        'regression',
        'clustering',
        'model evaluation'
    ],
    'sklearn': [
        'machine learning',
        'python',
        'data science',
        'classification',
        'regression',
        'clustering',
        'model evaluation'
    ],
    'pytorch': [
        'deep learning',
        'neural networks',
        'machine learning',
        'python',
        'tensor operations',
        'gpu computing'
    ],
    'tensorflow': [
        'deep learning',
        'neural networks',
        'machine learning',
        'python',
        'keras'
    ],
    'nlp': [
        'natural language processing',
        'text processing',
        'machine learning',
        'text analysis',
        'language models'
    ],
    'natural language programming': [
        'natural language processing',
        'nlp',
        'text processing',
        'machine learning'
    ],
    'langchain': [
        'generative ai',
        'llm',
        'large language models',
        'ai applications',
        'prompt engineering',
        'vector databases'
    ],
    'generative ai': [
        'deep learning',
        'llm',
        'large language models',
        'gpt',
        'transformers',
        'ai generation'
    ],
    'genai': [
        'generative ai',
        'llm',
        'large language models',
        'gpt',
        'transformers'
    ],
    'llm': [
        'large language models',
        'generative ai',
        'transformers',
        'gpt',
        'bert',
        'language models'
    ],
    
    # Software Development
    'full stack development': [
        'frontend development',
        'backend development',
        'database management',
        'api development',
        'version control'
    ],
    'backend development': [
        'api development',
        'database management',
        'server management',
        'authentication',
        'rest api'
    ],
    'frontend development': [
        'html',
        'css',
        'javascript',
        'responsive design',
        'ui/ux principles'
    ],
    'devops': [
        'ci/cd',
        'docker',
        'kubernetes',
        'cloud computing',
        'infrastructure as code',
        'monitoring'
    ],
    'cloud computing': [
        'aws',
        'azure',
        'google cloud',
        'server management',
        'scalability'
    ],
    
    # Web Development Frameworks
    'react': [
        'javascript',
        'html',
        'css',
        'frontend development',
        'component based architecture'
    ],
    'node.js': [
        'javascript',
        'backend development',
        'api development',
        'npm'
    ],
    'django': [
        'python',
        'backend development',
        'mvc architecture',
        'orm'
    ],
    'spring boot': [
        'java',
        'backend development',
        'dependency injection',
        'rest api'
    ],
    
    # Database Skills
    'sql': [
        'database management',
        'data modeling',
        'query optimization',
        'relational databases'
    ],
    'nosql': [
        'database management',
        'distributed systems',
        'scalability',
        'data modeling'
    ],
    'database administration': [
        'sql',
        'performance tuning',
        'backup recovery',
        'security'
    ],
    
    # Mobile Development
    'mobile development': [
        'ui/ux design',
        'api integration',
        'performance optimization',
        'cross platform development'
    ],
    'react native': [
        'react',
        'javascript',
        'mobile development',
        'cross platform development'
    ],
    'flutter': [
        'dart',
        'mobile development',
        'cross platform development',
        'ui development'
    ],
    
    # DevOps & Infrastructure
    'docker': [
        'containerization',
        'devops',
        'continuous deployment',
        'microservices'
    ],
    'kubernetes': [
        'docker',
        'container orchestration',
        'devops',
        'scalability',
        'microservices'
    ],
    'ci/cd': [
        'jenkins',
        'gitlab ci',
        'github actions',
        'automated testing',
        'devops'
    ],
    'terraform': [
        'infrastructure as code',
        'cloud computing',
        'devops',
        'automation'
    ],
    
    # Testing
    'test automation': [
        'unit testing',
        'integration testing',
        'python',
        'java',
        'javascript'
    ],
    'quality assurance': [
        'testing',
        'test cases',
        'bug tracking',
        'regression testing'
    ],
    
    # Project Management
    'agile methodology': [
        'scrum',
        'kanban',
        'sprint planning',
        'project management'
    ],
    'project management': [
        'leadership',
        'communication',
        'risk management',
        'stakeholder management'
    ],
    
    # Soft Skills
    'team leadership': [
        'team management',
        'communication',
        'project management',
        'mentoring'
    ],
    'problem solving': [
        'analytical thinking',
        'critical thinking',
        'creativity',
        'decision making'
    ],
    'communication skills': [
        'verbal communication',
        'written communication',
        'presentation skills',
        'stakeholder management'
    ],
    
    # Security
    'cybersecurity': [
        'network security',
        'information security',
        'risk assessment',
        'security protocols'
    ],
    'application security': [
        'secure coding',
        'owasp',
        'authentication',
        'authorization'
    ],
    
    # Business & Analytics
    'business intelligence': [
        'data analysis',
        'data visualization',
        'reporting',
        'sql'
    ],
    'product management': [
        'market research',
        'user stories',
        'agile methodology',
        'stakeholder management'
    ],
    
    # Specialized Domains
    'iot development': [
        'embedded systems',
        'python',
        'cloud computing',
        'data processing'
    ],
    'blockchain development': [
        'smart contracts',
        'cryptography',
        'distributed systems',
        'web3'
    ],
    'game development': [
        'c++',
        'unity',
        '3d modeling',
        'physics engines'
    ],
    'computer vision': [
    'deep learning',
    'image processing',
    'opencv',
    'convolutional neural networks',
    'object detection',
    'image classification',
    'image segmentation',
    'computer vision',
    'cv'
    ],
    'cv': [
        'computer vision',
        'image processing',
        'deep learning',
        'opencv',
        'convolutional neural networks'
    ],
    'opencv': [
        'computer vision',
        'image processing',
        'python',
        'c++',
        'real-time processing',
        'image analysis'
    ],
    'convolutional neural networks': [
        'deep learning',
        'computer vision',
        'image recognition',
        'neural networks',
        'cnn'
    ],
    'cnn': [
        'convolutional neural networks',
        'deep learning',
        'computer vision',
        'image processing'
    ],
    'object detection': [
        'computer vision',
        'deep learning',
        'image analysis',
        'bounding boxes',
        'yolo',
        'faster r-cnn'
    ],
    'image segmentation': [
        'computer vision',
        'deep learning',
        'pixel classification',
        'mask generation',
        'semantic segmentation',
        'instance segmentation'
    ],
    'image classification': [
        'computer vision',
        'deep learning',
        'pattern recognition',
        'feature extraction',
        'transfer learning'
    ],
    'yolo': [
        'object detection',
        'computer vision',
        'real-time detection',
        'deep learning'
    ],
    'faster r-cnn': [
        'object detection',
        'computer vision',
        'deep learning',
        'region proposals'
    ],
    'resnet': [
        'deep learning',
        'computer vision',
        'image classification',
        'convolutional neural networks',
        'transfer learning'
    ],
    'vgg': [
        'deep learning',
        'computer vision',
        'image classification',
        'convolutional neural networks'
    ],
    'tensorflow object detection': [
        'object detection',
        'computer vision',
        'tensorflow',
        'deep learning'
    ],
    'pytorch vision': [
        'computer vision',
        'pytorch',
        'deep learning',
        'image processing'
    ],
    'image processing': [
        'computer vision',
        'opencv',
        'filtering',
        'enhancement',
        'morphological operations'
    ],
    'feature extraction': [
        'computer vision',
        'image processing',
        'pattern recognition',
        'sift',
        'orb'
    ],
    'image recognition': [
        'computer vision',
        'image classification',
        'pattern recognition',
        'deep learning'
    ]
}