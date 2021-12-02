import unittest
from mocks import mock_request
from unittest.mock import patch

from app import Brother, Ricoh

class TestInkQuantity(unittest.TestCase):
    @patch('requests.get', mock_request.ricoh_selfMadePage)
    def test_Ricoh(self):
        printer = Ricoh("x", "x", "x")
        
        printer.readInkQuantity()
        #bars = [50,30,70]

        self.assertEqual(printer.toners["C"], 49)
        self.assertEqual(printer.toners["M"], 24)
        self.assertEqual(printer.toners["Y"], 61)
        self.assertEqual(printer.toners["K"], 30)
        
        
    def test_RicohInkCalculation_BarsWrongIntType(self):
        printer = Ricoh("x", "x", "x")
        bars = 200
        printer.calculateInkQuantity(bars)
        self.assertEqual(printer.toners["C"], 0)
        self.assertEqual(printer.toners["M"], 0)
        self.assertEqual(printer.toners["Y"], 0)
        self.assertEqual(printer.toners["K"], 0)
        
    def test_RicohInkCalculation_EmptyBars(self):
        printer = Ricoh("x", "x", "x")
        bars = []
        printer.calculateInkQuantity(bars)
        self.assertEqual(printer.toners["C"], 0)
        self.assertEqual(printer.toners["M"], 0)
        self.assertEqual(printer.toners["Y"], 0)
        self.assertEqual(printer.toners["K"], 0)
        
    def test_Brother(self):
        printer = Brother("x", "x", "x")

        
         
    
if __name__ == '__main__':
    unittest.main()