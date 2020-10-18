import unittest
from euler_066 import *
from fractions import Fraction

class Test66(unittest.TestCase):
    def setUp(self):
        pass

    def test_build_fraction(self):
        bcfa = build_continued_fraction_approximation
        # single values
        self.assertEqual(Fraction(1), bcfa([1]))
        self.assertEqual(Fraction(2), bcfa([2]))

        # two values
        self.assertEqual(Fraction(3,2), bcfa([1,2]))
        self.assertEqual(Fraction(7,3), bcfa([2,3]))

        # three values
        self.assertEqual(Fraction(37,16), bcfa([2,3,5]))

if __name__ == '__main__':
    unittest.main()