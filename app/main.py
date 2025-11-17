from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api import router as api_router
from app.ml.sentiment_model import get_sentiment_model

app = FastAPI(
    title="ML Sentiment Service",
    version="0.1.0",
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Loads the sentiment model on application start
    """
    _ = get_sentiment_model()
    yield

@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


app.include_router(api_router, prefix="/v1")
