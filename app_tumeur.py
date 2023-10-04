from fastapi import FastAPI
from pydantic import BaseModel
from model_utils_random import predict_cancer 
from typing import List
app = FastAPI()

class TumorFeatures(BaseModel):
    size: float
    p53_concentration: float

@app.post("/predict_cancer")
async def predict_tumor(tumor_features_list: List[TumorFeatures]):
    results=[]
    # for tumor_features in tumor_features_list:
    #     results.append(predict_cancer(tumor_features))

    results=[predict_cancer(tumor_features) for tumor_features in tumor_features_list]

       # result = predict_cancer(tumor_features)  
    return {"predictions": results}
