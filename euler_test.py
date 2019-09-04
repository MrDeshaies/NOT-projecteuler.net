import unittest
from euler import *


class TestEuler(unittest.TestCase):

    def test_fact1(self):
        self.assertEqual(fact(1), [1])
    
    def test_fact2(self):
        self.assertEqual(fact(2), [1,2])
    
    def test_fact3(self):
        self.assertEqual(fact(3), [1,3])

    def test_fact4(self):
        self.assertEqual(fact(4), [1,2,4])
    
    def test_fact26(self):
        self.assertEqual(fact(26), [1,2,13,26])

    def test_fact5(self):
        self.assertEqual(fact(5), [1,5])

    def test_fact8(self):
        self.assertEqual(fact(8), [1,2,4,8])
    
    def test_fact24(self):
         self.assertEqual(fact(24), [1,2,3,4,6,8,12,24])
    
    def test_fact41(self): #large-ish prime
         self.assertEqual(fact(41), [1,41])
    
    def test_factLessItself(self):
        # 1 is a special case ?
        self.assertTrue(len(factLessItself(1)) == 0, "1 should yield no factors")
        for x in range(2,100):
            expectedFactors = fact(x)
            expectedFactors.pop() # get rid of itself
            self.assertEquals(factLessItself(x), expectedFactors)

if __name__ == '__main__':
    unittest.main()