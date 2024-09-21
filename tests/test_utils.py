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
        def test_protocol_https(self):
            self.assertEqual(format_url("https", "google.com", "/fr"), "https://google.com/fr")
        
        def test_protocol_http(self):
            self.assertEqual(format_url("http", "exemple.com", "/index.html"), "http://exemple.com/index.html")
        
        def test_no_uri(self):
            self.assertEqual(format_url("https", "www.impots.gouv.fr", ""), "https://www.impots.gouv.fr")
        
        def test_complex_uri(self):
            self.assertEqual(format_url("https", "www.impots.gouv.fr", "/exemple/de/redirection/"), "https://www.impots.gouv.fr/exemple/de/redirection/")
        
        def test_ip_address_formatting(self):
            self.assertEqual(format_url("https", "8.8.8.8", ""), "https://8.8.8.8")


if __name__ == "__main__":
    unittest.main()
