from fastapi import FastAPI,Request,Header,HTTPException
from uuid import UUID
from pydantic import BaseModel
from model_utils_random import predict_cancer 
from typing import List
from typing import Annotated
app = FastAPI()

class TumorFeatures(BaseModel):
    size: float
    p53_concentration: float

@app.get("/ma_route")
async def return_data(request: Request):

    my_header = request.headers
    print(my_header)
    print(my_header.get("token"))

    my_secret_token = "MonSecretToken"

    if my_header.get("token") == my_secret_token:
        return {"data": "Here is your data"}
    else:
        return {"data": "No data for you, you do not provide the correct token"}
    


def get_token_from_headers(request: Request) -> str:
    my_header = request.headers
    return my_header.get("token", "")





@app.post("/predict_cancer")
async def predict_tumor(tumor_features_list: List[TumorFeatures], toker: str = Header(None, alias="token")):
    token = toker  # Use the provided token header

    my_secret_token = "MonSecretToken"

    if token == my_secret_token:
        results = [predict_cancer(tumor_features) for tumor_features in tumor_features_list]
        return {"predictions": results}
    else:
        raise HTTPException(status_code=403, detail="Access denied: Invalid token")
