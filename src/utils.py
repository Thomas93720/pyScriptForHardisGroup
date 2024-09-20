import re

def format_url(
    protocol,
    hostname,
    uri,   
) -> str:
    '''
    Permettant de formatter une URL incluant le protocole, le nom d'hôte et l'URI.
    Par exemple, format_url("https", "google.com", "/fr") doit retourner "https://google.com/fr".
    '''
    # La vérification du protocole ("http" ou "https") étant déja dans la fonction avant celle-ci j'ai choisi de ne pas
    # la remettre pour eviter une duplication de code ainsi qu'ajouter plus de complexité.
    HostnameRegex = re.compile(
        r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.[A-Za-z0-9-]{1,63})+$"
    )
    if isinstance(protocol,str) is False or isinstance(hostname,str) is False or isinstance(uri,str) is False:
        raise ValueError("Paramètre fournis non valide")
    if str(uri).startswith("/") is False and uri.__len__() > 0:
        uri = '/'+uri
    if HostnameRegex.match(hostname) is None:
        raise ValueError("Paramètre fournis non valide")
    return protocol+'://'+hostname+uri
