import unittest
from linked_sort_solution import *

def to_py(linked_list):
    """ Return linked_list as a regular Python list - very handy for testing.
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


class BubbleSortTest(unittest.TestCase):

    def test_empty(self):
        ll = to_ll([])
        ll.bubble_sort()
        self.assertEqual(to_py(ll), [])


    def test_5(self):
        ll = to_ll([5])
        ll.bubble_sort()
        self.assertEqual(to_py(ll), [5])

    def test_75(self):
        ll = to_ll([7,5])
        ll.bubble_sort()
        self.assertEqual(to_py(ll), [5,7])

    def test_57(self):
        ll = to_ll([5,7])
        ll.bubble_sort()
        self.assertEqual(to_py(ll), [5,7])

    def test_578(self):
        ll = to_ll([5,7,8])
        ll.bubble_sort()
        self.assertEqual(to_py(ll), [5,7,8])

    def test_587(self):
        ll = to_ll([5,8,7])
        ll.bubble_sort()
        self.assertEqual(to_py(ll), [5,7,8])

    def test_758(self):
        ll = to_ll([7,5,8])
        ll.bubble_sort()
        self.assertEqual(to_py(ll), [5,7,8])

    def test_785(self):
        ll = to_ll([7,8,5])
        ll.bubble_sort()
        self.assertEqual(to_py(ll), [5,7,8])

    def test_857(self):
        ll = to_ll([8,5,7])
        ll.bubble_sort()
        self.assertEqual(to_py(ll), [5,7,8])

    def test_875(self):
        ll = to_ll([8,7,5])
        ll.bubble_sort()
        self.assertEqual(to_py(ll), [5,7,8])

    def test_complex(self):
        ll = to_ll([23, 34, 55, 32, 7777, 98, 3, 2, 1])
        ll.bubble_sort()
        self.assertEqual(to_py(ll), [1, 2,3,23,32,34,55, 98, 7777])


class MergeTest(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(to_py(to_ll([]).merge(to_ll([]))), 
                         [])

    def test_5_7(self):
        self.assertEqual(to_py(to_ll([5]).merge(to_ll([7]))), 
                        [7,5]) 

    def test_7_5(self):
        self.assertEqual(to_py(to_ll([7]).merge(to_ll([5]))), 
                        [7,5])                         

    def test_no_overwrite(self):
        l1 = to_ll([7])
        l2 = to_ll([5])
        self.assertEqual(to_py(l1.merge(l2)), 
                        [7,5])
        self.assertEqual(to_py(l1), [7])
        self.assertEqual(to_py(l2), [5])

    def test_567_empty(self):
        self.assertEqual(to_py(to_ll([5,6,7]).merge(to_ll([]))), 
                        [7,6,5])

    def test_empty_567(self):
        self.assertEqual(to_py(to_ll([]).merge(to_ll([5,6,7]))), 
                        [7,6,5])                        

    def test_57_6(self):
        self.assertEqual(to_py(to_ll([5,7]).merge(to_ll([6]))), 
                        [7,6,5])                     

    def test_6_57(self):
        self.assertEqual(to_py(to_ll([6]).merge(to_ll([5,7]))), 
                        [7,6,5])                     


    def test_complex(self):
        self.assertEqual(to_py(to_ll([5,7,8,12]).merge(to_ll([6,9,10,12,15,16]))), 
                        [16,15,12,12,10,9,8,7,6,5])
