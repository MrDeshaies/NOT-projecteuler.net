import unittest
from euler_089 import *

class Test89(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_num_to_roman_unit(self):
        self.assertEqual(num_to_roman(0), "")
        self.assertEqual(num_to_roman(1), "I")
        self.assertEqual(num_to_roman(3), "III")
        self.assertEqual(num_to_roman(4), "IV")
        self.assertEqual(num_to_roman(6), "VI")
        self.assertEqual(num_to_roman(9), "IX")

    def test_num_to_roman_tens(self):
        self.assertEqual(num_to_roman(10), "X")
        self.assertEqual(num_to_roman(11), "XI")
        self.assertEqual(num_to_roman(23), "XXIII")
        self.assertEqual(num_to_roman(42), "XLII")
        self.assertEqual(num_to_roman(62), "LXII")
        self.assertEqual(num_to_roman(99), "XCIX")
    
    def test_num_to_roman_all(self):
        self.assertEqual(num_to_roman(100), "C")
        self.assertEqual(num_to_roman(1000), "M")
        self.assertEqual(num_to_roman(501), "DI")
        self.assertEqual(num_to_roman(1999), "MCMXCIX")
        self.assertEqual(num_to_roman(1606), "MDCVI")
        self.assertEqual(num_to_roman(2021), "MMXXI")
    
    def test_parse_roman(self):
        self.assertEqual(parse_roman("I"), 1)
        self.assertEqual(parse_roman("II"), 2)
        self.assertEqual(parse_roman("IIII"), 4)
        self.assertEqual(parse_roman("XI"), 11)
        self.assertEqual(parse_roman("IX"), 9)



if __name__ == '__main__':
    unittest.main()