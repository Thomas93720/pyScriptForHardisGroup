from src.utils import parse_arguments,format_url,http_get

if __name__ == "__main__":
    '''
    Lancer le projet avec toutes ses fonctions.
    '''
    arguments = parse_arguments()
    Protocol = arguments.protocol
    Hostname = arguments.hostname
    Uri = arguments.uri
    Threshold = arguments.threshold
    FormattedUrl = format_url(
        protocol=Protocol,
        hostname=Hostname,
        uri=Uri,
    )
    print(
        http_get(
            url=FormattedUrl,
            threshold=Threshold,
        )
    )
