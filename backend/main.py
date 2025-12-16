from fastapi import FastAPI
from backend.routes.captcha import router as captcha_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(captcha_router, prefix="/captcha")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)
