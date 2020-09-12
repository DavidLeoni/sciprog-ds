from digi_list_sol import *
import unittest

def to_py(linked_list):
    """ Returns linked_list as a regular Python list - very handy for testing.
    """
    python_list = []
    current = linked_list._head        
    
    while (current != None):
        python_list.append(current.get_data())
        current = current.get_next()                       
    return python_list        

def to_ll(python_list):
    """ Creates a DigiList from a regular Python list - very handy for testing.
    """
    ret = DigiList()
    
    for el in reversed(python_list):
        ret.add(el)
    return ret


class DigiListTest(unittest.TestCase):
    """ Test cases for DigiList v3
    
        Test cases are improved by adding a new method myAssert(self, linked_list, python_list)         
    """    
    
    def myAssert(self, linked_list, python_list):
        """ Checks provided linked_list can be represented as the given python_list. 
        """
        self.assertEqual(to_py(linked_list), python_list)
        # we check this new invariant about the last element        
        if len(python_list) != 0:                                   
            self.assertEqual(linked_list.last(), python_list[-1])   
    
class AddTest(DigiListTest):
    
    def test_01_init(self):
        ul = DigiList()
    
    def test_02_str(self):
        ul = DigiList()
        self.assertTrue('DigiList' in str(ul))
        ul.add(4)
        self.assertTrue('4' in str(ul))
        ul.add(2)
        self.assertTrue('2' in str(ul))
        self.assertTrue('4' in str(ul))
            
    def test_03_is_empty(self):
        ul = DigiList()
        self.assertTrue(ul.is_empty())        
        ul.add(5)
        self.assertFalse(ul.is_empty())
        
    def test_04_add(self):
        """ Remember 'add' adds stuff at the beginning of the list ! """
        
        ul = DigiList()
        self.myAssert(ul, [])
        ul.add(7)
        self.myAssert(ul, [7])
        ul.add(3)
        self.myAssert(ul, [3, 7])

    def test_05_wrong(self):
        ll = DigiList()

        with self.assertRaises(ValueError):
            ll.add(-3)

        with self.assertRaises(ValueError):
            ll.add(10)

        with self.assertRaises(ValueError):
            ll.add("ciao")

        with self.assertRaises(ValueError):
            ll.add(4.7)


class LastTest(DigiListTest):
    
    def test_01_last(self):
        """ This tests only simple cases. More in-depth testing will be provided by calls to myAssert """
        
        ul = DigiList()
        with self.assertRaises(ValueError):
            ul.last()        
        ul.add(8)
        self.assertEqual(ul.last(), 8)
        ul.add(6)
        self.assertEqual(ul.last(), 8)


class PlusOneTest(DigiListTest):

    def test_empty(self):
        ll = DigiList()
        ll.plus_one()
        self.myAssert(ll, [1])

    def test_0(self):
        ll = to_ll([0])
        ll.plus_one()
        self.myAssert(ll, [1])

    def test_1(self):
        ll = to_ll([1])
        ll.plus_one()
        self.myAssert(ll, [2])

    def test_37(self):
        ll = to_ll([3,7])
        ll.plus_one()
        self.myAssert(ll, [3,8])

    def test_10(self):
        ll = to_ll([1,0])
        ll.plus_one()
        self.myAssert(ll, [1,1])


    def test_39(self):
        ll = to_ll([3,9])
        ll.plus_one()
        self.myAssert(ll, [4,0])

    def test_749(self):
        ll = to_ll([7,4,9])
        ll.plus_one()
        self.myAssert(ll, [7,5,0])

    def test_793(self):
        ll = to_ll([7,9,3])
        ll.plus_one()
        self.myAssert(ll, [7,9,4])

    def test_799(self):
        ll = to_ll([7,9,9])
        ll.plus_one()
        self.myAssert(ll, [8,0,0])

    def test_949(self):
        ll = to_ll([9,4,9])
        ll.plus_one()
        self.myAssert(ll, [9,5,0])

    def test_9(self):
        ll = to_ll([9])
        ll.plus_one()
        self.myAssert(ll, [1,0])

    def test_99(self):
        ll = to_ll([9,9])
        ll.plus_one()
        self.myAssert(ll, [1,0,0])

    def test_999(self):
        ll = to_ll([9,9,9])
        ll.plus_one()
        self.myAssert(ll, [1,0,0,0])


