import requests
import argparse
import logging

from .exceptions import ThresholdExceededException

# Car par défaut ne montre que les critical
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


def http_get(
        url: str,
        threshold: int,
    ) -> dict:
    '''
    Envoie une requête GET à l'URL spécifiée et retourne la réponse sous forme de dictionnaire JSON.
    Lève des exceptions si des erreurs HTTP ou des dépassements de seuil surviennent.

    Args:
        url (str): L'URL vers laquelle la requête GET doit être envoyée.
        threshold (int): Le délai maximum (en secondes) avant qu'une exception de timeout ne soit levée.

    Returns:
        dict: La réponse JSON sous forme de dictionnaire si la requête réussit.

    Raises:
        ThresholdExceededException: Si le délai de la requête dépasse le seuil.
        HTTPError: Si une erreur HTTP est rencontrée.
        ValueError: Si la réponse n'est pas au format JSON.
    '''
    try:
        Request = requests.get(
            url=url,
            timeout=threshold,
        )
        Request.raise_for_status()

    except requests.Timeout:
        logging.critical("Erreur, detail: Le seuil de temps d'exécution a été dépassé.")
        raise ThresholdExceededException()

    except requests.exceptions.HTTPError as http_error:
        logging.critical(msg=str('Erreur, Code http: '+str(Request.status_code)+' detail: '+str(http_error)))
        raise http_error

    if 'application/json' not in Request.headers.get('Content-Type', ''):
        logging.critical(msg=str('Erreur, Code http:'+str(Request.status_code)+" detail: La réponse n'est pas en format JSON"))
        raise ValueError("La réponse n'est pas en format JSON")

    logging.info(msg=str('Succes, Code http: '+str(Request.status_code)))
    return Request.json()

def parse_arguments():
    '''
    Parse les arguments de la ligne de commande et valide leur format.

    Returns:
        argparse.Namespace: Un objet contenant les arguments de la ligne de commande.

    Raises:
        ValueError: Si un argument n'est pas valide.
    '''
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
    protocol:str,
    hostname:str,
    uri:str,
) -> str:
    '''
    Permet de formatter une URL incluant le protocole, le nom d'hôte et l'URI.

    Args:
        protocol (str): Le protocole ('http' ou 'https').
        hostname (str): Le nom d'hôte (ex: 'dummyjson.com').
        uri (str): L'URI (ex: '/products').

    Returns:
        str: L'URL formatée.

    Exemple:
        format_url("https", "dummyjson.com", "/products") -> "https://dummyjson.com/products"
    '''
    # Les vérifications des champs étant déja dans la fonction avant celle-ci inutile de les
    # remettre pour eviter une duplication de code ainsi qu'ajouter plus de complexité.
    if str(uri).startswith("/") is False and uri.__len__() > 0:
        uri = '/'+uri
    return protocol+'://'+hostname+uri
