# Article-Summarizer-Using-HuggingFace-Transformer-
The Article Summarizer is a web-based application that fetches text from online articles and generates concise summaries using natural language processing (NLP). The backend is built with Python and Flask, utilizing the Hugging Face Transformers library for summarization, and the frontend (assumed to be React, not included here) communicates with the backend via a REST API. This project is designed to provide a free, open-source alternative to paid summarization APIs, leveraging the power of Hugging Face's pre-trained models.

Features
Article Fetching: Extracts text from articles using a provided URL.
Text Summarization: Generates abstractive summaries (100-150 words) using the facebook/bart-large-cnn model from Hugging Face Transformers.
CORS Support: Configured for integration with a frontend running on http://localhost:3000.
Error Handling: Robust handling for invalid URLs, empty articles, or summarization errors.
No API Key Required: Unlike paid APIs, this project uses the free, open-source Hugging Face Transformers library.

Technologies Used
Hugging Face Transformers:
The transformers library provides pre-trained NLP models for tasks like summarization.
We use the facebook/bart-large-cnn model, optimized for abstractive summarization, which generates human-like summaries by rephrasing key content.
No API keys are needed, as the model runs locally after downloading (~1.5 GB).
Supports offline operation, making it cost-effective and scalable for local deployment.

Python Libraries:
Flask: A lightweight web framework for the backend API.
BeautifulSoup4: Parses HTML to extract article text.
Requests: Fetches article content from URLs.
PyTorch: Required by Transformers for model inference.
Flask-CORS: Enables cross-origin requests for frontend integration.

Deployment: The backend runs on http://0.0.0.0:5000 for local development.


article-summarizer/
└── frontend/    ← React app (UI)
├── backend/
│   ├── app.py              # Flask backend with API endpoints
│   ├── summarizer.py       # Article fetching and summarization logic
│   └── requirements.txt    # Python dependencies
├── .env                    # Optional: Environment variables (not required for this version)
└── README.md               # Project documentation

<img width="1210" height="652" alt="Interface" src="https://github.com/user-attachments/assets/580bdcfa-8f97-4004-9251-e51137551c82" />
