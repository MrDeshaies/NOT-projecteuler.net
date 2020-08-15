import unittest
import euler_061
from euler_061 import is_cyclic_set

class Test61(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_cyclic_sets(self):
        self.assertTrue(is_cyclic_set([1234,3412]))
        self.assertTrue(is_cyclic_set([1234,3456,5612]))
        self.assertTrue(is_cyclic_set([1111,1111,1111]))
        self.assertTrue(is_cyclic_set([1234,3456,5678,7812]))
        
        self.assertFalse(is_cyclic_set([1234,3456,5678]))
        self.assertFalse(is_cyclic_set([1234,3456,5678,7813]))
        # must all be length 4
        self.assertFalse(is_cyclic_set([111, 111, 111]))
        self.assertFalse(is_cyclic_set([1111, 1111, 11111]))

if __name__ == '__main__':
    unittest.main()