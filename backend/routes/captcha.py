from fastapi import APIRouter, UploadFile, File
from backend.services.captcha_solver import solve_captcha


router = APIRouter()

@router.post("/solve")
async def solve(file: UploadFile = File(...)):
    img_bytes = await file.read()
    text = solve_captcha(img_bytes)
    return {"captcha": text}
