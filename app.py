from fastapi import FastAPI
from services import voice_biometrics, behavior_analytics, network_intelligence
from utils import risk_scoring

app = FastAPI(title="VoiceGuard UEBA", description="AI-Powered Voice Banking Fraud Detection")

@app.get("/")
def root():
    return {"message": "VoiceGuard UEBA API Running"}

@app.post("/analyze")
def analyze_call(audio_input: str, metadata: dict):
    # Step 1: Voice biometrics
    biometrics_result = voice_biometrics.verify(audio_input)

    # Step 2: Behavior analytics
    behavior_result = behavior_analytics.analyze(audio_input)

    # Step 3: Network intelligence
    network_result = network_intelligence.check(metadata)

    # Step 4: Risk scoring
    risk = risk_scoring.calculate(biometrics_result, behavior_result, network_result)

    return {"biometrics": biometrics_result, "behavior": behavior_result,
            "network": network_result, "risk_score": risk}
