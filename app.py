import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(
    title="Tiny ML API", 
    description="Interactive model-serving backend for real-time predictions."
)

# 1. Input Validation Schema
class PredictRequest(BaseModel):
    feature_1: float = Field(..., description="First measurement metric", ge=0)
    feature_2: float = Field(..., description="Second measurement metric", ge=0)
    feature_3: float = Field(..., description="Third measurement metric", ge=0)
    feature_4: float = Field(..., description="Fourth measurement metric", ge=0)

@app.get("/")
def health_check():
    """Returns the system infrastructure health status."""
    return {"status": "healthy", "environment": "production"}

@app.post("/predict")
def get_prediction(payload: PredictRequest):
    """Takes 4 validated numeric inputs and returns a real-time prediction."""
    try:
        # Structure the inputs into an array format scikit-learn expects
        input_features = [[payload.feature_1, payload.feature_2, payload.feature_3, payload.feature_4]]
        
        # NOTE: Dummy placeholder value for demonstration
        # In a full app: prediction = model.predict(input_features)[0]
        simulated_prediction = 1.0 
        
        return {
            "prediction": simulated_prediction,
            "status": "success"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference Engine Error: {str(e)}")
