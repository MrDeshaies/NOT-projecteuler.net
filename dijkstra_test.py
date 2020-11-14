import unittest
from dijkstra import *

class TestDijkstra(unittest.TestCase):
    def setUp(self):
        pass

    def test_simple_path(self):
        root = Node(1)
        n2, n5 = Node(2), Node(5)
        target = Node(7)
        n2.add_neighbor(target)
        n5.add_neighbor(target)
        root.add_neighbor(n2)
        root.add_neighbor(n5)

        path = dijkstra([root,n2,n5,target], root, target)
        self.assertEqual(value_sum(path), 10)
    
    def test_bidirectional_links(self):
        root = Node(1)
        n2, n5 = Node(2), Node(5)
        target = Node(7)

        root.add_neighbor(n2)
        n2.add_neighbor(root)
        root.add_neighbor(n5)
        n5.add_neighbor(root)
        n2.add_neighbor(target)
        target.add_neighbor(n2)
        n5.add_neighbor(target)
        target.add_neighbor(n5)
        
        path = dijkstra([root,n2,n5,target], root, target)
        self.assertEqual(value_sum(path), 10)

if __name__ == '__main__':
    unittest.main()