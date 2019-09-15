import unittest
import euler_031
from euler_031 import find

PENCE = 7

class Test31(unittest.TestCase):

    def setUp(self):
        euler_031.total_count = 0
    
    def test_pence(self):
        find(1,PENCE)
        self.assertEqual(euler_031.total_count, 1)
        find(150,PENCE)
        self.assertEqual(euler_031.total_count, 2)
    
    def test_3(self):
        find(3,0)
        # 1x3 and (1x1 + 2x1)
        self.assertEqual(euler_031.total_count, 2)
    
    def test_6(self):
        find(6,0)
        # 1x6
        # 1x4 + 2x1
        # 1x2 + 2x2
        # 1x0 + 2x3
        # 1x1 + 2x0 + 5x1
        self.assertEqual(euler_031.total_count, 5)


if __name__ == '__main__':
    unittest.main()