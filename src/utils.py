import requests
import argparse
import logging

from exceptions import ThresholdExceededException

# Car par défaut ne montre que les critical
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


def http_get(
        url,
        threshold,
    ) -> dict:
    '''
    Envoyer une requête GET à l'url en argument et retourner le resultat si pas d'erreur http
    '''
    try:
        Request = requests.get(
            url=url,
            timeout=threshold,
        )
        Request.raise_for_status()

    except requests.Timeout:
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
) -> str:
    '''
    Permettant de formatter une URL incluant le protocole, le nom d'hôte et l'URI.
    Par exemple, format_url("https", "google.com", "/fr") doit retourner "https://google.com/fr".
    '''
    # Les vérifications des champs étant déja dans la fonction avant celle-ci inutile de les
    # remettre pour eviter une duplication de code ainsi qu'ajouter plus de complexité.
    if str(uri).startswith("/") is False and uri.__len__() > 0:
        uri = '/'+uri
    return protocol+'://'+hostname+uri
