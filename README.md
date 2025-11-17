# ML Sentiment Service

The ML Sentiment Service is an API that exposes a sentiment analysis model over HTTP. This service can run in a Docker container. The model downloads on application startup so expect around a minute for the startup time.

Technologies used:

- FastAPI — API framework
- Hugging Face Transformers — sentiment model
- Uvicorn — ASGI server
- Docker — containerization
- Pytest — tests

---

## ENDPOINTS

GET /health
Simple health check.

Response:
{
"status": "ok"
}

---

POST /v1/predict
Runs sentiment analysis on a batch of input texts.

Request:
{
"texts": [
"I absolutely love this product.",
"This was the worst experience I've had."
]
}

Response:
{
"results": [
{
"label": "positive",
"score": 0.98
},
{
"label": "negative",
"score": 0.99
}
]
}

label: predicted sentiment
score: confidence in [0.0, 1.0]

---

## RUNNING LOCALLY

1. Create and activate virtual environment:
   python3 -m venv .venv
   source .venv/bin/activate

2. Install dependencies:
   pip install .
   pip install ".[dev]" (installs test dependencies)

3. Start the API:
   uvicorn app.main:app --reload

Docs: http://127.0.0.1:8000/docs
Health: http://127.0.0.1:8000/health
Predict: POST http://127.0.0.1:8000/v1/predict

---

## RUNNING WITH DOCKER

1. Build the image:
   docker build -t ml-sentiment-service .

2. Run the container:
   docker run --rm -p 8000:8000 ml-sentiment-service

API available at:
http://127.0.0.1:8000

Note:
First startup may take longer while the model downloads.

---

## TESTS

Tests written with pytest using FastAPI’s TestClient.

Run:
pytest

Covers:

- /health
- basic structure of /v1/predict response

---

## DESIGN NOTES

Batch-first API:

- /v1/predict accepts a list of strings for batch inference.

Pydantic models:

- SentimentRequest, SentimentResponse, SentimentResult provide schema validation and OpenAPI generation.

Model wrapper:

- app/ml/sentiment_model.py wraps the Hugging Face pipeline behind a simple predict(texts) interface.

Startup model loading:

- Model loads during FastAPI lifespan startup so first request does not incur model load time.

Separation of concerns:

- app/api.py — routing
- app/service.py — app logic
- app/ml/sentiment_model.py — ML integration
- app/models.py — request/response schemas
