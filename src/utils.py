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
    
