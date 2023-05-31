import unittest
import re
from tkinter import *
import math
from unittest.mock import patch

# Import the code to be tested
from Calcfortest import input_key, verifyString, CosFunc, SinFunc, TanFunc, filterString, clear

class TestCalculator(unittest.TestCase):

 
        
    def test_verifyString(self):
        # Test basic  input
        result = verifyString('2+2')
        self.assertEqual(result, 4.0)
        
        # Test negative sign input
        result = verifyString(' -3+4')
        self.assertEqual(result, 1.0)
        
        # Test division and multiplication
        result = verifyString('2*3/4')
        self.assertEqual(result, 1.5)
        
        # Test parentheses
        result = verifyString('(2+3)*4')
        self.assertEqual(result, 20.0)
        

        

        
if __name__ == '__main__':
    unittest.main()