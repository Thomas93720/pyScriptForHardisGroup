import requests
import argparse

def http_get() -> dict:
    '''
    Envoyer une requête à l'endpoint en get et retourner le resultat si pas d'erreur http
    '''
    Endpoint = 'https://dummyjson.com/products'
    Request = requests.get(Endpoint)
    Request.raise_for_status()
    return Request.json()

def parse_arguments():
    Parser = argparse.ArgumentParser() # Crée un parseur pour la ligne de commande

    # Ajout des arguments requis
    Parser.add_argument(
        '-pro',
        '--protocol',
        type=str,
        required=True,
        help="Le protocole.",
    )
    Parser.add_argument(
        '-host',
        '--hostname',
        type=str,
        required=True,
        help="Le nom d'hôte, ex : 'google.fr'.",
    )
    Parser.add_argument(
        '--uri',
        type=str,
        required=True,
        help="L'URI, ex : '/produits'.",
    )
    Parser.add_argument(
        '-thr',
        '--threshold',
        type=int,
        required=True,
        help="Le seuil de temps (int) en secondes.",
    )
    Args = Parser.parse_args()

    # Validation des valeurs
    ProtocolValues = {
        'http',
        'https',
    }
    if Args.protocol in ProtocolValues is False:
        raise ValueError("Veuillez renseigner un protocole valide")

    if Args.hostname is None or Args.uri is None or Args.threshold is None:
        raise ValueError("Veuillez renseigner tous les arguments")

    return Args

def format_url(
    protocol,
    hostname,
    uri,   
):
    '''
    Permettant de formatter une URL incluant le protocole, le nom d'hôte et l'URI.
    Par exemple, format_url("https", "google.com", "/fr") doit retourner "https://google.com/fr".
    '''
    if isinstance(protocol,str) is False or isinstance(hostname,str) is False or isinstance(uri,str) is False:
        raise ValueError("Paramètre fournis non valide")
    return protocol+'://'+hostname+uri
