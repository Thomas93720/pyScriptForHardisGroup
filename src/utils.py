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
