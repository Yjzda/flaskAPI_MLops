from fastapi import FastAPI
from model_utils import predict
from pydantic import BaseModel
from model_utils import load_model
import joblib
app = FastAPI()
from typing import List
model_path = "regression.joblib"
loaded_model = joblib.load(model_path)
class Payload(BaseModel):
    X: List[List[float]]#list de liste pour plusiers pred

@app.post("/predict_wx")
async def prediction_house_price(payload:Payload):
    X=payload.X#donnée envoyée par le client dans req c'est dans objet et pas dans la classe que l'on stocke
    #des donnée donc ici payload minuscule

 
    predictions=predict(X,loaded_model)
    
    return {"predictionswx":predictions}

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/predict")
async def prediction_house_price(payload:Payload):
        # Liste de prédictions codée en dur
    predictions=["prediction1","prediction2","prediction3"]
    
    return {"predictions":predictions}

