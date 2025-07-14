import { useState } from "react"; // Import only useState
import axios from "axios";
import "./App.css";

function App() {
  const [url, setUrl] = useState("");
  const [summary, setSummary] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSummarize = async () => {
    if (!url) {
      setError("Please enter a valid URL.");
      return;
    }
    setLoading(true);
    setError("");
    setSummary("");
    try {
      const res = await axios.post("http://localhost:5000/summarizer", { url });
      setSummary(res.data.summary || "No summary returned.");
      if (res.data.error) setError(res.data.error);
    } catch (err) {
      console.error("API error:", err);
      setError(err.response?.data?.error || "Failed to summarize article.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>📰 Web Article Summarizer</h1>
      <input
        type="text"
        placeholder="Enter article URL (e.g., https://example.com)"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        disabled={loading}
      />
      <button onClick={handleSummarize} disabled={loading}>
        {loading ? "Summarizing..." : "Summarize"}
      </button>
      {error && <div className="error-box">{error}</div>}
      {summary && (
        <div className="summary-box">
          <h3>🧠 Summary:</h3>
          <p>{summary}</p>
        </div>
      )}
    </div>
  );
}

export default App;