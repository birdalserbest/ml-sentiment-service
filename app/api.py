from fastapi import APIRouter
from app.models import SentimentRequest, SentimentResponse, SentimentResult
from app.service import analyze_sentiment

router = APIRouter()


@router.post("/predict", response_model=SentimentResponse)
def predict_sentiment(payload: SentimentRequest) -> SentimentResponse:
    # Change this when I implement actual model
    results = analyze_sentiment(payload.texts)
    return SentimentResponse(results=results)