from fastapi import FastAPI

app = FastAPI()


@app.get("/predict")
async def prediction():
        # Liste de prédictions codée en dur
    predictions=["Prediction 1", "Prediction 2", "Prediction 3"]
    
    return {"predictions":predictions}

@app.get("/")
async def root():
    return {"message": "Hello World"}

