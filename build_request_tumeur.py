import requests


api_url = "http://localhost:8000/predict_cancer"  


def send_request(tumor_features):
    response = requests.post(api_url, json=tumor_features)
    if response.status_code == 200:
        return response.json()["prediction"]
    else:
        return "Error: Request failed"
    
if __name__ == "__main__":
    examples = [
        {"size": 0.2, "p53_concentration": 0.3},
        {"size": 0.6, "p53_concentration": 0.7}
    ]
    
    for example in examples:
        prediction = send_request(example)
        print(f"Caractéristiques : Size={example['size']}, p53_concentration={example['p53_concentration']}")
        print(f"Prédiction : {prediction}")
