from typing import List
from pydantic import BaseModel, Field


class SentimentRequest(BaseModel):
    texts: List[str] = Field(
        ...,
        description="List of input texts to analyze for sentiment.",
        min_length=1,
    )


class SentimentResult(BaseModel):
    label: str = Field(..., description="Predicted sentiment label.")
    score: float = Field(..., ge=0.0, le=1.0, description="Confidence score in [0, 1].")


class SentimentResponse(BaseModel):
    results: List[SentimentResult] = Field(
        ...,
        description="Sentiment predictions for each input text.",
    )