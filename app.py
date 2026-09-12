from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np

# Initialize the FastAPI app
app = FastAPI(
    title="ML Model API",
    description="FastAPI Web Interface for ML Model Predictions",
    version="1.0.0"
)

# Define input data schema using Pydantic
class InputData(BaseModel):
    # Adjust these fields based on the columns expected by your ml_example.py dataset/model
    feature1: float
    feature2: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the ML Model API! Go to /docs for the interactive UI."}

@app.post("/predict")
def predict(data: InputData):
    # Extract features from input request
    f1 = data.feature1
    f2 = data.feature2
    
    # Perform prediction logic (placeholder prediction using input features)
    prediction = f1 * 0.5 + f2 * 1.2
    
    return {
        "prediction": float(prediction),
        "status": "success"
    }