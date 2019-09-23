import unittest
import euler_035
from euler_035 import contains_even_digits
from euler_035 import find_rotations

class Test35(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_contains_even_digits(self):
        for d in (2,4,6,8,0):
            self.assertTrue(contains_even_digits(d))
        for d in (1,3,5,7,9):
            self.assertFalse(contains_even_digits(d))
        
        self.assertTrue(contains_even_digits(12))
        self.assertTrue(contains_even_digits(21))
        self.assertTrue(contains_even_digits(121))
        
        self.assertFalse(contains_even_digits(13))
        self.assertFalse(contains_even_digits(31))
        self.assertFalse(contains_even_digits(135))
    
    def test_rotation(self):
        self.assertEqual(find_rotations(1), [1])
        self.assertEqual(find_rotations(12), [12,21])
        self.assertEqual(find_rotations(123), [123,231,312])
        self.assertEqual(find_rotations(1234), [1234,2341,3412,4123])



if __name__ == '__main__':
    unittest.main()