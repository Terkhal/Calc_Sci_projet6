#!/usr/bin/python3

import unittest
import Calc

class TestAdd(unittest.TestCase):
     def test_add(self):
          self.assertEqual(Calc.verifyString("2+3"), 5)

if __name__ == '__main__':
    unittest.main()