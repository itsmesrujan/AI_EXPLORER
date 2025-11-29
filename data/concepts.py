CONCEPT_INFO = {
    "Concepts Overview": {
        "title": "AI Concepts Overview",
        "description": "This application provides interactive demonstrations of various AI concepts including Linear Regression, Classification, Neural Networks, NLP Sentiment Analysis, Computer Vision Edge Detection, and K-Means Clustering.",
        "how_it_works": [
            "Select a concept from the sidebar.",
            "Read the description and how-it-works section.",
            "Click 'Run Demo' to see an interactive demonstration.",
        ],
        "examples": [
            "Linear Regression: Predicting house prices.",
            "Classification: Spam email detection.",
            "Neural Networks: Image recognition tasks.",
            "NLP Sentiment: Analyzing customer reviews.",
            "Computer Vision Edges: Detecting edges in images.",
            "K-Means Clustering: Market segmentation.",
            "Generative AI: Text generation."
        ]
    },
    "Linear Regression": {
        "title": "Linear Regression",
        "description": "In statistics, linear regression is a linear approach to modeling the relationship between a dependent variable and one or more independent variables.",
        "how_it_works": [
            "Fits a straight line to the data.",
            "Minimizes the error between predictions and actual values using least squares.",
        ],
        "examples": [
            "Predicting house prices",
            "Estimating demand",
            "Trend forecasting",
        ]
    },

    "Classification": {
        "title": "Classification",
        "description": "When classification is used in machine learning, it refers to the task of predicting the category or class label of new observations based on past observations with known labels.",
        "how_it_works": [
            "Learns patterns from labeled training data.",
            "Separates classes using boundaries or probability models.",
        ],
        "examples": [
            "Spam detection",
            "Medical diagnosis",
            "Credit risk assessment",
        ]
    },

    "Neural Network": {
        "title": "Neural Network",
        "description": "Neural network is a computational model inspired by the human brain that learn complex patterns.",
        "how_it_works": [
            "Inputs move through layers of neurons.",
            "Activation functions introduce nonlinearity.",
            "Weights adjust using back propagation.",
        ],
        "examples": [
            "Image recognition",
            "Speech processing",
            "Predictive analytics",
        ]
    },

    "NLP Sentiment": {
        "title": "NLP Sentiment",
        "description": "Natural Language Processing Sentiment analysis determines the emotional tone behind text.",
        "how_it_works": [
            "Uses lexicons or machine learning models.",
            "Scores text as positive, negative, or neutral.",
        ],
        "examples": [
            "Social media monitoring",
            "Customer feedback analysis",
            "Product review interpretation",
        ]
    },

    "Computer Vision Edges": {
        "title": "Computer Vision Edges",
        "description": "Edge detection identifies points in an image where brightness changes sharply, indicating object boundaries.",
        "how_it_works": [
            "Computes gradients in the image.",
            "Highlights boundaries of objects.",
        ],
        "examples": [
            "Object detection",
            "Image segmentation",
            "Medical imaging",
        ]
    },

    "K-Means Clustering": {
        "title": "K-Means Clustering",
        "description": "K-Means Clustering is an unsupervised learning algorithm that partitions data into K distinct clusters based on feature similarity.",
        "how_it_works": [
            "Choose K cluster centers.",
            "Assign points to nearest center.",
            "Recalculate centers.",
            "Repeat until convergence.",
        ],
        "examples": [
            "Market segmentation",
            "Image compression",
            "Document clustering",
        ]
    },
}

# Additional AI Concepts
# [TODO] Review the correctness of these entries.
CONCEPT_INFO.update({

    "Generative AI": {
        "title": "Generative AI",
        "description": "Generative AI creates new content such as text, images, or music by learning patterns from existing data.",
        "how_it_works": [
            "Trained on large datasets to learn patterns.",
            "Uses deep learning models like GANs, VAEs, and Transformers.",
            "Generates new content through sampling and decoding."
        ],
        "examples": [
            "ChatGPT generating text.",
            "Stable Diffusion creating images.",
            "Music or code generation using AI."
        ]
    },

    "Reinforcement Learning": {
        "title": "Reinforcement Learning",
        "description": "Reinforcement Learning is concerned with how an intelligent agent should take actions in a dynamic environment to maximize cumulative reward.",
        "how_it_works": [
            "Agent interacts with an environment.",
            "Receives rewards or penalties.",
            "Learns optimal policy through trial and error."
        ],
        "examples": [
            "Game-playing AI like AlphaGo.",
            "Robotics navigation.",
            "ATM cash dispensing optimization."
        ]
    },

    "Genetic Algorithms": {
        "title": "Genetic Algorithms",
        "description": "Genetic Algorithms are inspired by biological evolution to optimize complex problems.",
        "how_it_works": [
            "Create population of solutions.",
            "Use crossover and mutation to evolve.",
            "Select best individuals over generations."
        ],
        "examples": [
            "Traveling salesman optimization.",
            "Automated design generation.",
            "Feature selection in ML."
        ]
    },

    "Search & Planning": {
        "title": "Search and Planning",
        "description": "AI uses search to explore possible actions and planning to find optimal paths or strategies.",
        "how_it_works": [
            "Uses algorithms like A*, BFS, DFS.",
            "Builds decision trees or state graphs.",
            "Evaluates cost and chooses best path."
        ],
        "examples": [
            "Maze solving.",
            "Robot delivery route planning.",
            "Chess move prediction."
        ]
    },

    "Knowledge Representation": {
        "title": "Knowledge Representation",
        "description": "AI systems represent facts, rules, and relationships to reason and make decisions.",
        "how_it_works": [
            "Uses logic, graphs, or ontologies.",
            "Applies inference and reasoning.",
            "Derives new facts from known knowledge."
        ],
        "examples": [
            "Medical diagnosis expert systems.",
            "Legal reasoning systems.",
            "Knowledge graphs (Google Knowledge Graph)."
        ]
    },

    "Expert Systems": {
        "title": "Expert Systems",
        "description": "Expert systems simulate human experts using rules and knowledge inference.",
        "how_it_works": [
            "Define knowledge rules and facts.",
            "Use rule engines to evaluate input.",
            "Provide recommendations based on logic."
        ],
        "examples": [
            "Medical diagnostic systems.",
            "Loan approval systems.",
            "Troubleshooting assistants."
        ]
    },

    "Explainable AI": {
        "title": "Explainable AI",
        "description": "Explains how ML models make predictions, making them transparent and trustworthy.",
        "how_it_works": [
            "Analyzes model features and decisions.",
            "Uses methods like SHAP or LIME.",
            "Shows importance and effect of features."
        ],
        "examples": [
            "Explaining credit risk prediction.",
            "Bias detection in healthcare models.",
            "AI fairness audits."
        ]
    },

    "Robotics and Perception": {
        "title": "Robotics and AI Perception",
        "description": "Robotics combines AI with physical sensors to understand and move in real environments.",
        "how_it_works": [
            "Uses computer vision and LIDAR for perception.",
            "Plans actions using reinforcement learning or planning.",
            "Executes motions through control algorithms."
        ],
        "examples": [
            "Self-driving cars.",
            "Warehouse robots.",
            "Delivery drones."
        ]
    },
})