from fastapi import FastAPI
from backend.routes.captcha import router as captcha_router

app = FastAPI()
app.include_router(captcha_router, prefix="/captcha")
