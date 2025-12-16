import { useState } from "react";
import { solveCaptcha } from "./api/captcha";
import UploadBox from "./components/UploadBar.jsx";
import "./styles/main.css";

export default function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSolve = async () => {
    if (!file) return;

    setLoading(true);
    setError("");
    setResult("");

    try {
      const data = await solveCaptcha(file);
      setResult(data.captcha);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <div className="card">
        <h1>Captcha Solver</h1>

        <UploadBox file={file} setFile={setFile} />

        <button onClick={handleSolve} disabled={loading}>
          {loading ? "Solving..." : "Solve"}
        </button>

        {result && <div className="result">{result}</div>}
        {error && <div className="error">{error}</div>}
      </div>
    </div>
  );
}
