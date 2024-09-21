import unittest

from src.utils import format_url

class TestFormatUrl(unittest.TestCase):
    '''
    Test du bon fonctionnement de la fonction format_url()
    '''
    def test_url_formatting(self):
        '''
        test des urls possible fonctionelles
        '''
        self.assertEqual(format_url("https", "google.com", "/fr"), "https://google.com/fr")
        self.assertEqual(format_url("http", "exemple.com", "/index.html"), "http://exemple.com/index.html")
        self.assertEqual(format_url("https", "www.impots.gouv.fr", ""), "https://www.impots.gouv.fr")
        self.assertEqual(format_url("https", "www.impots.gouv.fr", "/exemple/de/redirection/"), "https://www.impots.gouv.fr/exemple/de/redirection/")
        self.assertEqual(format_url("https", "8.8.8.8", ""), "https://8.8.8.8")


if __name__ == "__main__":
    unittest.main()
