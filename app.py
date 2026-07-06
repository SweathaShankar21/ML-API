import os
import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Tiny ML API", description="Production-ready model-serving backend")

# 1. Enforce strict input validation using Pydantic
class PredictRequest(BaseModel):
    feature_1: float = Field(..., description="First model input metric")
    feature_2: float = Field(..., description="Second model input metric")
    feature_3: float = Field(..., description="Third model input metric")
    feature_4: float = Field(..., description="Fourth model input metric")

# Placeholder or dynamic path for your model loader
MODEL_PATH = os.getenv("MODEL_PATH", "model.pkl")

@app.get("/")
def health_check():
    """Returns the system status."""
    return {"status": "healthy", "model_configured": os.path.exists(MODEL_PATH)}

@app.post("/predict")
def get_prediction(payload: PredictRequest):
    """Takes 4 validated numbers and returns the model inference result."""
    try:
        # Reshape data into the format scikit-learn expects [[f1, f2, f3, f4]]
        input_data = [[payload.feature_1, payload.feature_2, payload.feature_3, payload.feature_4]]
        
        # Simulating model inference (Replace with: model = joblib.load(MODEL_PATH))
        # mock_prediction = model.predict(input_data)[0]
        prediction_result = 1.0 
        
        return {"prediction": prediction_result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference error: {str(e)}")
