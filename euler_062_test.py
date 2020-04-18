import unittest
from euler_062 import is_permutation

class Test62(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_is_permutation(self):
        self.assertTrue(is_permutation(1,1))
        self.assertTrue(is_permutation(123,321))
        self.assertTrue(is_permutation(123,213))
        self.assertTrue(is_permutation(112,121))

        self.assertFalse(is_permutation(1,2))
        self.assertFalse(is_permutation(12,34))
        self.assertFalse(is_permutation(1122,1233))

if __name__ == '__main__':
    unittest.main()