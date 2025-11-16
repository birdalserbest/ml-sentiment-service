from fastapi import APIRouter
from app.models import SentimentRequest, SentimentResponse, SentimentResult

router = APIRouter()


@router.post("/predict", response_model=SentimentResponse)
def predict_sentiment(payload: SentimentRequest) -> SentimentResponse:
    # Change this when I implement actual model
    dummy_results = [
        SentimentResult(label="neutral", score=0.5)
        for _ in payload.texts
    ]
    return SentimentResponse(results=dummy_results)