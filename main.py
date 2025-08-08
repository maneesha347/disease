from fastapi import FastAPI,HTTPException
from predict import predict_heart_disease
app=FastAPI()
@app.post("/heart_pred")
def heart_predict(features: list[float]):
    try:
        risk=predict_heart_disease(features)
        return {"risk_score":risk}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
