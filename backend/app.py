# backend/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from summarizer import fetch_article_text, summarize_text

app = Flask(__name__)
CORS(app, resources={r"/summarizer": {"origins": "http://localhost:3000"}})  # Explicit CORS for React

@app.route("/summarizer", methods=["POST"])
def summarize():
    data = request.get_json()
    url = data.get("url")
    if not url:
        return jsonify({"error": "No URL provided."}), 400

    try:
        article_text = fetch_article_text(url)
        if article_text.startswith("Error"):
            return jsonify({"error": article_text}), 500

        summary = summarize_text(article_text)
        return jsonify({"summary": summary})
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500

@app.route("/test", methods=["GET"])  # Added for debugging
def test():
    return jsonify({"message": "Backend is working"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
