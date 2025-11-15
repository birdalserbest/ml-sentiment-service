from fastapi import FastAPI

app = FastAPI(
    title="ML Sentiment Service",
    version="0.1.0",
)


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}