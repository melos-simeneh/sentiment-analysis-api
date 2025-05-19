from fastapi import FastAPI
from schemas.sentiment import SentimentRequest, SentimentResponse
import joblib

app = FastAPI()
model = joblib.load("model/sentiment_model.pkl")

@app.get("/api/")
def health_check():
    return {"status": "Sentiment Analysis API is running."}

@app.post("/api/predict", response_model=SentimentResponse)
def predict_sentiment(req: SentimentRequest):
    pred = model.predict([req.text])[0]
    return SentimentResponse(sentiment=pred)
