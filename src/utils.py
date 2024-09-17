import requests

def http_get() -> dict:
    '''
    Envoyer une requête à l'endpoint en get et retourner le resultat si pas d'erreur http
    '''
    Endpoint = 'https://dummyjson.com/products'
    Request = requests.get(Endpoint)
    Request.raise_for_status()
    return Request.json()