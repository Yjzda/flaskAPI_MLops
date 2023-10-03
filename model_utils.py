import joblib
import numpy as np
model_path="regression.joblib"
def load_model(model_path):
   
    loaded_model=joblib.load(model_path)
    return loaded_model
    

def predict(input_data,loaded_model):
  
    predictions = loaded_model.predict(input_data)
    return predictions