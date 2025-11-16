from fastapi import FastAPI
from app.api import router as api_router

app = FastAPI(
    title="ML Sentiment Service",
    version="0.1.0",
)

@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}

app.include_router(api_router, prefix="/v1")