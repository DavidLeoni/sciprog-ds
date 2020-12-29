from last_sol import *
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
    """ Creates a LinkedList from a regular Python list - very handy for testing.
    """
    ret = LinkedList()
    
    for el in reversed(python_list):
        ret.add(el)
    return ret


class LinkedListTest(unittest.TestCase):
    """ Test cases for LinkedList v3
    
        Test cases are improved by adding a new method myAssert(self, linked_list, python_list)         
    """    
    
    def myAssert(self, linked_list, python_list):
        """ Checks provided linked_list can be represented as the given python_list. 
        """
        self.assertEqual(to_py(linked_list), python_list)
        # we check this new invariant about the size
        self.assertEqual(linked_list.size(), len(python_list)) 
        # we check this new invariant about the last element        
        if len(python_list) != 0:                                   
            self.assertEqual(linked_list.last(), python_list[-1])   
        
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
            
    def test_03_is_empty(self):
        ul = LinkedList()
        self.assertTrue(ul.is_empty())        
        ul.add('a')
        self.assertFalse(ul.is_empty())        
        
    def test_04_add(self):
        """ Remember 'add' adds stuff at the beginning of the list ! """
        
        ul = LinkedList()
        self.myAssert(ul, [])
        ul.add('b')
        self.myAssert(ul, ['b'])
        ul.add('a')
        self.myAssert(ul, ['a', 'b'])

class SizeTest(LinkedListTest):        
    
    def test_01_size(self):
        ul = LinkedList()
        self.assertEqual(ul.size(), 0)
        ul.add("a")
        self.assertEqual(ul.size(), 1)
        ul.add("b")
        self.assertEqual(ul.size(), 2)

class LastTest(LinkedListTest):
    
    def test_01_last(self):
        """ This tests only simple cases. More in-depth testing will be provided by calls to myAssert """
        
        ul = LinkedList()
        with self.assertRaises(ValueError):
            ul.last()        
        ul.add('b')
        self.assertEqual(ul.last(), 'b')
        ul.add('a')
        self.assertEqual(ul.last(), 'b')


class RotateTest(LinkedListTest):

    def test_01_empty(self):
        ll = LinkedList()
        ll.rotate()
        self.myAssert(ll, [])


    def test_02_a(self):
        ll = to_ll(['a'])
        ll.rotate()
        self.myAssert(ll, ['a'])

    def test_03_b(self):
        ll = to_ll(['b'])
        ll.rotate()
        self.myAssert(ll, ['b'])

    def test_04_ab(self):
        ll = to_ll(['a','b'])
        ll.rotate()
        self.myAssert(ll, ['b','a'])
        ll.rotate()
        self.myAssert(ll, ['a','b'])

    def test_05_abc(self):
        ll = to_ll(['a','b','c'])
        ll.rotate()
        self.myAssert(ll, ['c','a','b'])
        ll.rotate()
        self.myAssert(ll, ['b','c','a'])
        ll.rotate()
        self.myAssert(ll, ['a','b','c'])

    def test_06_abb(self):
        ll = to_ll(['a','b','b'])
        ll.rotate()
        self.myAssert(ll, ['b','a','b'])
        ll.rotate()
        self.myAssert(ll, ['b','b','a'])
        ll.rotate()
        self.myAssert(ll, ['a','b','b'])

    def test_07_abcd(self):
        ll = to_ll(['a','b','c','d'])
        ll.rotate()
        self.myAssert(ll, ['d','a','b','c'])
        ll.rotate()
        self.myAssert(ll, ['c','d','a','b'])
        ll.rotate()
        self.myAssert(ll, ['b','c','d','a'])
        ll.rotate()
        self.myAssert(ll, ['a','b','c','d'])



class RotatenTest(LinkedListTest):

    def test_01_empty(self):
        ll = LinkedList()
        ll.rotaten(0)
        self.myAssert(ll, [])
        ll.rotaten(1)
        self.myAssert(ll, [])
        ll.rotaten(2)
        self.myAssert(ll, [])

        with self.assertRaises(ValueError):
            ll.rotaten(-1)
        with self.assertRaises(ValueError):
            ll.rotaten(-2)

    def test_02_a(self):
        ll = to_ll(['a'])
        ll.rotaten(0)
        self.myAssert(ll, ['a'])
        ll.rotaten(1)
        self.myAssert(ll, ['a'])
        ll.rotaten(2)
        self.myAssert(ll, ['a'])

        with self.assertRaises(ValueError):
            ll.rotaten(-1)
        with self.assertRaises(ValueError):
            ll.rotaten(-2)


    def test_03_b(self):
        ll = to_ll(['b'])
        ll.rotaten(0)
        self.myAssert(ll, ['b'])
        ll.rotaten(1)
        self.myAssert(ll, ['b'])
        ll.rotaten(2)
        self.myAssert(ll, ['b'])

    def test_04_ab_0(self):
        ll = to_ll(['a','b'])
        ll.rotaten(0)
        self.myAssert(ll, ['a','b'])

        with self.assertRaises(ValueError):
            ll.rotaten(-1)
        with self.assertRaises(ValueError):
            ll.rotaten(-2)


    def test_05_ab_1(self):
        ll = to_ll(['a','b'])
        ll.rotaten(1)
        self.myAssert(ll, ['b','a'])
        ll.rotaten(1)
        self.myAssert(ll, ['a','b'])

    def test_06_ab_2(self):
        ll = to_ll(['a','b'])
        ll.rotaten(2)
        self.myAssert(ll, ['a','b'])

    def test_07_ab_3(self):
        ll = to_ll(['a','b'])
        ll.rotaten(3)
        self.myAssert(ll, ['b','a'])

    def test_08_ab_4(self):
        ll = to_ll(['a','b'])
        ll.rotaten(4)
        self.myAssert(ll, ['a','b'])

    def test_09_ab_forever(self):
        """ Is this taking forever? If you wrote something like this:            
        
            for i in range(k):
                self.rotate()   
                
            think instead how to cut the linked list to avoid the for !
        """
        ll = to_ll(['a','b'])
        ll.rotaten(11**18)
        self.myAssert(ll, ['b','a'])
        
        
    def test_10_abc_0(self):
        ll = to_ll(['a','b','c'])
        ll.rotaten(0)
        self.myAssert(ll, ['a','b','c'])

    def test_11_abc_1(self):
        ll = to_ll(['a','b','c'])
        ll.rotaten(1)
        self.myAssert(ll, ['c','a','b'])
        ll.rotaten(1)
        self.myAssert(ll, ['b','c','a'])
        ll.rotaten(1)
        self.myAssert(ll, ['a','b','c'])

    def test_12_abc_2(self):
        ll = to_ll(['a','b','c'])
        ll.rotaten(2)
        self.myAssert(ll, ['b','c','a'])
        ll.rotaten(2)
        self.myAssert(ll, ['c','a','b'])
        ll.rotaten(2)
        self.myAssert(ll, ['a','b','c'])


    def test_13_abc_3(self):
        ll = to_ll(['a','b','c'])
        ll.rotaten(3)
        self.myAssert(ll, ['a','b','c'])

    def test_14_abc_4(self):
        ll = to_ll(['a','b','c'])
        ll.rotaten(4)
        self.myAssert(ll, ['c','a','b'])

    def test_15_abc_5(self):
        ll = to_ll(['a','b','c'])
        ll.rotaten(5)
        self.myAssert(ll, ['b','c','a'])

    def test_16_abc_6(self):
        ll = to_ll(['a','b','c'])
        ll.rotaten(6)
        self.myAssert(ll, ['a','b','c'])

    def test_17_abc_forever(self):
        """ Is this taking forever? If you wrote something like this:            
        
            for i in range(k):
                self.rotate()   
                
            think instead how to cut the linked list to avoid the for !
        """
        ll = to_ll(['a','b','c'])
        ll.rotaten(11**18)
        self.myAssert(ll, ['c','a','b'])
        
                
    def test_18_abb_2(self):
        ll = to_ll(['a','b','b'])
        ll.rotaten(2)
        self.myAssert(ll, ['b','b','a'])
        ll.rotaten(2)
        self.myAssert(ll, ['b','a','b'])
        ll.rotaten(2)
        self.myAssert(ll, ['a','b','b'])

    def test_19_abb_3(self):
        ll = to_ll(['a','b','b'])
        ll.rotaten(3)        
        self.myAssert(ll, ['a','b','b'])

    def test_20_abcd(self):
        ll = to_ll(['a','b','c','d'])
        ll.rotaten(2)
        self.myAssert(ll, ['c','d','a','b'])
        ll.rotaten(1)
        self.myAssert(ll, ['b','c','d','a'])
        ll.rotaten(3)
        self.myAssert(ll, ['c','d','a','b'])

    

class PlusOneTest(LinkedListTest):

    def test_empty(self):
        ll = LinkedList()
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
