import unittest

from app import Brother, Ricoh

class TestInkQuantity(unittest.TestCase):
    def test_Ricoh(self):
        printer = Ricoh("x", "x", "x")
        self.assertEqual(printer.calculateFromPx(0), 0)
        self.assertEqual(printer.calculateFromPx(50), 30)
        
    def test_Brother(self):
        printer = Brother("x", "x", "x")

        
         
    
if __name__ == '__main__':
    unittest.main()