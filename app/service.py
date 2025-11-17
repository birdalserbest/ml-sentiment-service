from typing import List

from app.ml.sentiment_model import get_sentiment_model
from app.models import SentimentResult


def analyze_sentiment(texts: List[str]) -> List[SentimentResult]:
    """
    Run sentiment analysis on a batch of texts and return structured results
    """
    model = get_sentiment_model()
    raw_predictions = model.predict(texts)

    results: List[SentimentResult] = [
        SentimentResult(label=label, score=score)
        for label, score in raw_predictions
    ]
    return results
