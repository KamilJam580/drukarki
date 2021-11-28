
from requests.api import request
import requests
from unittest.mock import patch

import unittest
from bs4 import BeautifulSoup as bs4
from mocks import mock_request
from app import Ricoh, Ricoh2000
from app import Printer

class PrintersIngegrated(unittest.TestCase):
    @patch('requests.get', mock_request.ricoh)

    def test_Ricoh_class(self):
        printer = Ricoh("Ricoh MP C2051", "BORT Guido", "192.168.20.28")
        printer.Refresh()
        self.assertEqual(printer.toners["C"], 49)
        self.assertEqual(printer.toners["M"], 24)
        self.assertEqual(printer.toners["Y"], 61)
        self.assertEqual(printer.toners["K"], 30)

    @patch('requests.get', mock_request.ricoh2000)
    def test_Ricoh2000_class(self):
        printer = Ricoh2000("Ricoh MP C2051", "BORT Guido", "192.168.20.28")
        printer.Refresh()
        self.assertEqual(printer.toners["C"], 49)
        self.assertEqual(printer.toners["M"], 24)
        self.assertEqual(printer.toners["Y"], 61)
        self.assertEqual(printer.toners["K"], 30)
        
if __name__ == '__main__':
    unittest.main()
