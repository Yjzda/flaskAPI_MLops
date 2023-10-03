import joblib

def load_model(model_path):
    try:
        loaded_model = joblib.load(model_path)
        return loaded_model
    except Exception as e:
        return f"Error loading the model: {str(e)}"
def predict(loaded_model, input_data):
    try:
        predictions = loaded_model.predict(input_data)
        return predictions
    except Exception as e:
        return f"Error making predictions: {str(e)}"