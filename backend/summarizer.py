import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
from transformers import pipeline

load_dotenv()

def fetch_article_text(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        res = requests.get(url, headers=headers, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")
        paragraphs = soup.find_all("p")
        text = "\n".join(p.get_text() for p in paragraphs if p.get_text().strip())
        if not text:
            return "Error: No content found in the article."
        return text.strip()
    except Exception as e:
        return f"Error fetching URL: {str(e)}"

def summarize_text(text):
    if not text or text.startswith("Error"):
        return "No valid text found to summarize."
    try:
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        # Truncate text to avoid exceeding model token limits (BART handles ~1024 tokens)
        max_input_length = 1024
        text = text[:max_input_length] if len(text) > max_input_length else text
        summary = summarizer(text, max_length=150, min_length=100, do_sample=False)
        return summary[0]["summary_text"]
    except Exception as e:
        return f"Error summarizing text: {str(e)}"