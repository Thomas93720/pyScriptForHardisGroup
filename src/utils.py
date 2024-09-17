import argparse

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
