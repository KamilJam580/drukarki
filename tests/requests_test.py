from requests.api import request
import requests
from unittest.mock import patch

import unittest
from bs4 import BeautifulSoup as bs4
from mocks import mock_request

class TestRequests(unittest.TestCase):

    @patch('requests.get', mock_request.ricoh_selfMadePage)
    def test_ricoh(self):
        response = requests.get(f"http:///web/guest/pl/websys/webArch/topPage.cgi").text
        self.assertNotEquals(response.count, 0)
        #print(response)

        
if __name__ == '__main__':
    unittest.main()