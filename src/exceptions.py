class ThresholdExceededException(Exception):
    '''
    Exception pour le dépassement du seuil de temps de la requête
    '''
    def __init__(self, reason="Le seuil de temps d'exécution a été dépassé"):
        self.reason = reason
        super().__init__(self.reason)
