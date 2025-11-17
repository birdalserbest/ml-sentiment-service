from functools import lru_cache
from typing import List, Tuple
from transformers import pipeline


class SentimentModel:
    """Wrapper around Hugging Face sentiment analysis pipeline"""

    def __init__(
        self,
        model_name: str = "distilbert-base-uncased-finetuned-sst-2-english",
    ) -> None:
        # download/load the model on first use only
        self._pipeline = pipeline("sentiment-analysis", model=model_name) # type: ignore

    def predict(self, texts: List[str]) -> List[Tuple[str, float]]:
        """
        Run sentiment analysis on a batch of texts
        Returns a list of (label, score) tuples
        """
        outputs = self._pipeline(texts)

        results: List[Tuple[str, float]] = []
        for output in outputs:
            label = output["label"].lower()
            score = float(output["score"])
            results.append((label, score))

        return results


@lru_cache(maxsize=1)
def get_sentiment_model() -> SentimentModel:
    """
    Return a singleton SentimentModel instance
    lru_cache ensures the model is loaded only once per process
    """
    return SentimentModel()
