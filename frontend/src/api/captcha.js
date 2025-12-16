const API_BASE_URL = 'http://localhost:8000/captcha/solve';


export async function solveCaptcha(file) {
  const formData = new FormData();
  formData.append('file', file);

  const response = await fetch(API_BASE_URL, {
    method: 'POST',
    body: formData,
  });

  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }

  return await response.json();
}