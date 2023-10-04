import requests

api_url = "http://localhost:8000/predict_wx" 


data = {
    "X": [
        [3.0, 40.0, 0]
    
    ]
}

# Envoyer une requête POST à l'API avec les données
response = requests.post(api_url, json=data)

# Vérifier si la requête a réussi (code de statut HTTP 200)
if response.status_code == 200:
    # Récupére' la réponse JSON sous forme de dictionnaire
    prediction_result = response.json()
    # Afficher la prédiction
    print("Prédiction :", prediction_result["predictionswx"])
else:
    print("La requête a échoué avec le code de statut :", response.status_code)
