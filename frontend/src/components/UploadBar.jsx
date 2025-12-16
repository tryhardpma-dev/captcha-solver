import { useRef } from "react";

export default function UploadBar({ file, setFile }) {
  const inputRef = useRef();

  const handleClick = () => inputRef.current.click();

  const handleChange = (e) => {
    if (e.target.files[0]) {
      setFile(e.target.files[0]);
    }
  };

  return (
    <>
      <div className="upload" onClick={handleClick}>
        <p>{file ? "Change image" : "Click to upload captcha"}</p>
        {file && <img src={URL.createObjectURL(file)} alt="preview" />}
      </div>

      <input
        ref={inputRef}
        type="file"
        accept="image/*"
        hidden
        onChange={handleChange}
      />
    </>
  );
}
