

from requests.api import request
import pytest
import requests
from unittest.mock import patch
from functools import partial
import sys
import unittest

class mock_request:
    text = "0"



class TestCalc(unittest.TestCase):
    
    def request_ricoh(self):
        mockobj = mock_request()  
        return mockobj
  
    @patch('requests.get', request_ricoh)
    def test_ricoh_request(self):
        response = requests.get(f"http:///web/guest/pl/websys/webArch/topPage.cgi").text
        print(response)

        
if __name__ == '__main__':
    unittest.main()