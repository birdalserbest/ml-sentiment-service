from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_predict_sentiment_basic() -> None:
    payload = {"texts": ["Unicorn startup announces major deals with 3 new clients.", "Unicorn startup hit with 700 thousand dollar lawsuit."]}

    response = client.post("/v1/predict", json=payload)

    assert response.status_code == 200

    body = response.json()
    assert "results" in body
    assert len(body["results"]) == 2

    result1 = body["results"][0]
    result2 = body["results"][1]
    assert "label" in result1, result2
    assert "score" in result1, result2
    assert isinstance(result1["score"], float)
    assert 0.0 <= result1["score"] <= 1.0
    assert isinstance(result2["score"], float)
    assert 0.0 <= result2["score"] <= 1.0
