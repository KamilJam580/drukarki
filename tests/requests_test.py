

from requests.api import request
import requests
from unittest.mock import patch
from functools import partial
import sys
import unittest
from bs4 import BeautifulSoup as bs4
class mock_request:
    text = "0"

class TestRequests(unittest.TestCase):
    
    def request_ricoh(self):
        f = open(r"tests\mockpages\demofile.html", "r")
        mockobj = mock_request()  
        mockobj.text = f
        return mockobj
  
    @patch('requests.get', request_ricoh)
    def test_ricoh_request(self):
        response = requests.get(f"http:///web/guest/pl/websys/webArch/topPage.cgi").text
        print(response)

        
if __name__ == '__main__':
    unittest.main()