import joblib
#import build_model

# model_path="regression.joblib"
def load_model(model_path):
    #build_model()
    loaded_model=joblib.load(model_path)
    return loaded_model
    

def predict(input_data,loaded_model):
  
    predictions = loaded_model.predict(input_data)
    predictions=predictions.tolist()#format json to list
    return predictions