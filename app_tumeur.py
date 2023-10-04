from fastapi import FastAPI
from pydantic import BaseModel
from model_utils_random import predict_cancer 
app = FastAPI()

class TumorFeatures(BaseModel):
    size: float
    p53_concentration: float

@app.post("/predict_cancer")
async def predict_tumor(tumor_features: TumorFeatures):
    result = predict_cancer(tumor_features)  
    return {"prediction": result}
