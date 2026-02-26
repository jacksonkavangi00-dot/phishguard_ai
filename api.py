from fastapi import FastAPI
import joblib
from features import extract_features

app = FastAPI(title="PhishGuard AI API")

model = joblib.load("phishing_model.pkl")

@app.get("/")
def home():
    return {"message": "PhishGuard AI is running"}

@app.post("/check")
def check_url(url: str):
    features = extract_features(url)
    prediction = model.predict([features])[0]
    prob = model.predict_proba([features])[0][1] * 100

    return {
        "url": url,
        "phishing": bool(prediction),
        "risk_score": round(prob, 2)
    }
