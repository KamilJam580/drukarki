
from requests.api import request
import requests
from unittest.mock import patch

import unittest
from bs4 import BeautifulSoup as bs4
from mocks import mock_request
from Printer import *
from Printer import Ricoh
class PrintersIngegrated(unittest.TestCase):
    
    @patch('requests.get', mock_request.ricoh_selfMadePage)
    @patch('Printer.Ricoh.readPageCount', mock_request.pageCounter)
    def test_TonersRicohWithSelfmadePage(self):
        printer = Ricoh("Ricoh MP C2051", "BORT Guido", "192.168.20.28")
        printer.Refresh()
        
        self.assertEqual(printer.toners["C"], 49)
        self.assertEqual(printer.toners["M"], 24)
        self.assertEqual(printer.toners["Y"], 61)
        self.assertEqual(printer.toners["K"], 30)
        print(printer.pageCounter)

    @patch('requests.get', mock_request.ricoh_goodPage1)
    @patch('Printer.Ricoh.readPageCount', mock_request.pageCounter)
    def test_TonersRicohRealPage1(self):
        printer = Ricoh("Ricoh MP C2051", "BORT Guido", "192.168.20.28")
        printer.Refresh()

        self.assertEqual(printer.toners["C"], 79)
        self.assertEqual(printer.toners["M"], 39)
        self.assertEqual(printer.toners["Y"], 69)
        self.assertEqual(printer.toners["K"], 19)
        print(printer.pageCounter)

    def test_TonersEmptyPage(self):
        printer = Ricoh("Ricoh MP C2051", "BORT Guido", "192.168.20.28")
        printer.Refresh()



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
