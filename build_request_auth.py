# build_request_auth.py
from fastapi import Header, HTTPException

# Fonction de vérification de l'Authorization Header
def verify_authorization(auth_header: str = Header(None)):
    expected_value = "4242"  # La valeur attendue dans l'Authorization Header
    
    if auth_header != expected_value:
        raise HTTPException(status_code=403, detail="Accès non autorisé")
