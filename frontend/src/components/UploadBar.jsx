import { useState } from "react";
import { solveCaptcha } from "../api/captcha";
import "../styles/main.css";

export default function UploadBar() {
    const [file, setFile] = useState(null);
    const [preview, setPreview] = useState(null);
    const [result, setResult] = useState("");
    const [loading, setLoading] = useState(false);

    const handleFile = (e) => {
        const f = e.target.files[0];
        if (!f) return;

        setFile(f);
        setPreview(URL.createObjectURL(f));
        setResult("");
    };

    const handleSolve = async () => {
        if (!file) return;
        setLoading(true);

        try {
        const data = await solveCaptcha(file);
        setResult(data.captcha);
        } catch (e) {
        alert("Error solving captcha" + e.message);
        }

        setLoading(false);
    };

    return (
        <div className="card">
        <h1>Captcha Solver</h1>

        <label className="upload">
            Upload Captcha
            <input type="file" accept="image/*" onChange={handleFile} hidden />
        </label>

        {preview && <img src={preview} className="preview" />}

        <button onClick={handleSolve} disabled={loading || !file}>
            {loading ? "Detecting..." : "Solve"}
        </button>

        {result && (
            <div className="result">
            Result: <span>{result}</span>
            </div>
        )}
        </div>
    );
}
