import unittest
from linked_list_sol import *

def to_py(linked_list):
    """ Creates a regular Python list from a LinkedList - very handy for testing.
    """
    python_list = []
    current = linked_list._head        
    
    while (current != None):
        python_list.append(current.get_data())
        current = current.get_next()                       
    return python_list        

def to_ll(python_list):
    """ Creates a LinkedList from a regular Python list - very handy for testing.
    """
    ret = LinkedList()
    
    for el in reversed(python_list):
        ret.add(el)
    return ret

class LinkedListTest(unittest.TestCase):

    def myAssert(self, linked_list, python_list):
        """ Checks provided linked_list can be represented as the given python_list.
        """
        self.assertEqual(to_py(linked_list), python_list)


class AddTest(LinkedListTest):
    
    def test_01_init(self):
        ul = LinkedList()
    
    def test_02_str(self):
        ul = LinkedList()
        self.assertTrue('LinkedList' in str(ul))
        ul.add('z')
        self.assertTrue('z' in str(ul))
        ul.add('w')
        self.assertTrue('z' in str(ul))
        self.assertTrue('w' in str(ul))
        
    def test_04_add(self):
        """ Remember 'add' adds stuff at the beginning of the list ! """
        
        ul = LinkedList()
        self.assertEqual(to_py(ul), [])
        ul.add('b')
        self.assertEqual(to_py(ul), ['b'])
        ul.add('a')
        self.assertEqual(to_py(ul), ['a', 'b'])

        
class PivotTest(LinkedListTest):

    def test_01_empty(self):
        ll = LinkedList()
        res = ll.pivot()
        self.assertEqual(to_py(ll), [])
        self.assertEqual(res, 0)

    def test_02_one(self):
        ll = to_ll([5])
        orig_node = ll._head
        res = ll.pivot()
        self.assertEqual(id(orig_node), id(ll._head))   # shouldn't create new nodes
        self.assertEqual(res, 0)

    def test_03_8_6(self):
        ll = to_ll([8,6])
        orig_node0 = ll._head
        orig_node1 = ll._head.get_next()
        res = ll.pivot()
        self.assertEqual(to_py(ll), [6,8])
        self.assertEqual(res, 1)
        self.assertEqual(id(orig_node0), id(ll._head.get_next()))   # shouldn't create new nodes
        self.assertEqual(id(orig_node1), id(ll._head))              # shouldn't create new nodes

    def test_04_5_5(self):
        ll = to_ll([5,5])
        orig_node0 = ll._head
        orig_node1 = ll._head.get_next()
        res = ll.pivot()
        self.assertEqual(to_py(ll), [5,5])
        self.assertEqual(res, 0)
        # should only move nodes which are STRICTLY LESS (<) than pivot
        self.assertEqual(id(orig_node0), id(ll._head))              # shouldn't create new nodes
        self.assertEqual(id(orig_node1), id(ll._head.get_next()))   # shouldn't create new nodes

    def test_05_4_7(self):
        ll = to_ll([4, 7])
        orig_node0 = ll._head
        orig_node1 = ll._head.get_next()
        res = ll.pivot()
        self.assertEqual(to_py(ll), [4, 7])
        self.assertEqual(res, 0)
        self.assertEqual(id(orig_node0), id(ll._head))
        self.assertEqual(id(orig_node1), id(ll._head.get_next()))

    def test_06_7_9_4(self):
        ll = to_ll([7, 9, 4])
        orig_node0 = ll._head
        orig_node1 = ll._head.get_next()
        orig_node2 = ll._head.get_next().get_next()
        res = ll.pivot()
        self.assertEqual(to_py(ll), [4, 7, 9])
        self.assertEqual(res, 1)
        self.assertEqual(id(orig_node2), id(ll._head))
        self.assertEqual(id(orig_node0), id(ll._head.get_next()))
        self.assertEqual(id(orig_node1), id(ll._head.get_next().get_next()))

    def test_06_7_9_4_6(self):
        ll = to_ll([7, 9, 4, 6])
        res = ll.pivot()
        # NOTICE nodes are placed before pivot in reverse order as we find them
        self.assertEqual(to_py(ll), [6, 4, 7, 9])
        self.assertEqual(res, 2)


    def test_07_7_6_9_4(self):
        ll = to_ll([7, 6, 9, 4])
        res = ll.pivot()
        # NOTICE nodes before pivot are placed in reverse order as we find them
        self.assertEqual(to_py(ll), [4, 6, 7, 9])
        self.assertEqual(res, 2)

    def test_08_7_4_6_9(self):
        ll = to_ll([7, 4, 6, 9])
        res = ll.pivot()
        # NOTICE nodes before pivot are placed in reverse order as we find them
        self.assertEqual(to_py(ll), [6, 4, 7, 9])
        self.assertEqual(res, 2)

    def test_09_9_4_8(self):
        ll = to_ll([7, 9, 4, 8])
        res = ll.pivot()
        # order of nodes after pivot should be the same as in the original list
        self.assertEqual(to_py(ll), [4, 7, 9, 8])
        self.assertEqual(res, 1)


    def test_complex(self):
        ll = to_ll([7, 12, 1, 3, 8, 9, 6, 4, 7, 2, 10])
        res = ll.pivot()
        # order of nodes after pivot should be the same as in the original list
        self.assertEqual(to_py(ll), [2, 4, 6, 3, 1, 7, 12, 8, 9, 7, 10])
        self.assertEqual(res, 5)        
