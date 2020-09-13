import unittest
from more_sol import *

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


class OccurrencesTest(LinkedListTest):

    def test_01_occurrences_zero(self):
        self.assertEqual(LinkedList().occurrences('a') , 0)
        self.assertEqual(LinkedList().occurrences(7) , 0 )
        
    def test_02_occurrences_one(self):
        
        ul = LinkedList()
        ul.add('a')
        self.assertEqual(ul.occurrences('a') , 1)
        self.assertEqual(ul.occurrences('b') , 0)
        self.assertEqual(ul.occurrences(7) , 0)

    def test_03_occurrences_three(self):
        
        ul = LinkedList()
        ul.add('a')
        ul.add('b')
        ul.add('a')        
        self.assertEqual(ul.occurrences('a'), 2 )
        self.assertEqual(ul.occurrences('b'), 1 )
        self.assertEqual(ul.occurrences('c'), 0 )

class ShrinkTest(LinkedListTest):
    def test_01_shrink_return_none(self):
        ul = LinkedList()         
        self.assertEqual(ul.shrink(), None)
        
    def test_02_shrink_empty(self):
        ul = LinkedList()            
        ul.shrink()
        self.assertEqual(to_py(ul), [])

    def test_03_shrink_one(self):
        ul = LinkedList()
        ul.add('a')
        ul.shrink()
        self.assertEqual(to_py(ul), ['a'])

    def test_04_shrink_two(self):
        ul = LinkedList()
        ul.add('b')
        ul.add('a')
        ul.shrink()
        self.assertEqual(to_py(ul), ['a'])

    def test_05_shrink_three(self):
        ul = LinkedList()
        ul.add('c')
        ul.add('b')
        ul.add('a')
        ul.shrink()
        self.assertEqual(to_py(ul), ['a', 'c'])

        
    def test_06_shrink_four(self):
        ul = LinkedList()
        ul.add('d')
        ul.add('c')
        ul.add('b')        
        ul.add('a')        
        
        ul.shrink()
        self.assertEqual(to_py(ul), ['a','c'])

class DupFirstTest(LinkedListTest):

    def test_01_return_none(self):
        ul = LinkedList()        
        self.assertEqual(ul.dup_first(), None)

    def test_02_empty(self):
        ul = LinkedList()        
        ul.dup_first()
        self.assertEqual(to_py(ul), [])

    def test_03_one(self):
        ul = LinkedList()        
        ul.add('a')
        ul.dup_first()
        self.assertEqual(to_py(ul), ['a', 'a'])

    def test_04_two(self):
        ul = LinkedList()        
        ul.add('b')
        ul.add('a')
        ul.dup_first()
        self.assertEqual(to_py(ul), ['a', 'a', 'b'])

    def test_05_two_dups(self):
        ul = LinkedList()        
        ul.add('a')
        ul.add('a')
        ul.dup_first()
        self.assertEqual(to_py(ul), ['a', 'a', 'a'])

    def test_06_three(self):
        ul = LinkedList()        
        ul.add('c')
        ul.add('b')
        ul.add('a')
        ul.dup_first()
        self.assertEqual(to_py(ul), ['a', 'a', 'b', 'c'])


class DupAllTest(LinkedListTest):

    def test_01_return_none(self):
        ul = LinkedList()        
        self.assertEqual(ul.dup_all(), None)

    def test_02_empty(self):
        ul = LinkedList()        
        ul.dup_all()
        self.assertEqual(to_py(ul), [])

    def test_03_one(self):
        ul = LinkedList()        
        ul.add('a')
        ul.dup_all()
        self.assertEqual(to_py(ul), ['a', 'a'])

    def test_04_two(self):
        ul = LinkedList()        
        ul.add('b')
        ul.add('a')
        ul.dup_all()
        self.assertEqual(to_py(ul), ['a', 'a', 'b', 'b'])

    def test_05_two_dups(self):
        ul = LinkedList()        
        ul.add('a')
        ul.add('a')
        ul.dup_all()
        self.assertEqual(to_py(ul), ['a', 'a', 'a', 'a'])

    def test_06_three(self):
        ul = LinkedList()        
        ul.add('c')
        ul.add('b')
        ul.add('a')
        ul.dup_all()
        self.assertEqual(to_py(ul), ['a', 'a', 'b', 'b', 'c', 'c'])


        
class MirrorTest(LinkedListTest):
    
    def test_01_empty(self):
        self.assertEqual(to_py(mirror([])), [])
    
    def test_02_one(self):
        self.assertEqual(to_py(mirror(['a'])), ['a','a'])
        
    def test_03_two(self):
        self.assertEqual(to_py(mirror(['a', 'b'])), ['a','b','b','a'])

    def test_04_three(self):
        self.assertEqual(to_py(mirror(['a', 'b', 'c'])), ['a','b','c','c','b','a'])



class NorepTest(LinkedListTest):
    
    def test_01_empty(self):
        ul = LinkedList()
        ul.norep()
        self.assertEqual(to_py(ul), [])    
    
    def test_02_a(self):
        ul = LinkedList()
        ul.add('a')
        ul.norep()
        self.assertEqual(to_py(ul), ['a'])    
                
    def test_03_aa(self):
        ul = LinkedList()
        ul.add('a')
        ul.add('a')        
        ul.norep()
        self.assertEqual(to_py(ul), ['a'])    

    def test_04_aaa(self):
        ul = LinkedList()
        ul.add('a')
        ul.add('a')        
        ul.add('a')        
        ul.norep()
        self.assertEqual(to_py(ul), ['a'])    

    def test_05_aaab(self):
        ul = LinkedList()
        ul.add('b')        
        ul.add('a')
        ul.add('a')        
        ul.norep()
        self.assertEqual(to_py(ul), ['a', 'b'])    


    def test_06_baa(self):
        ul = LinkedList()               
        ul.add('a')
        ul.add('a')        
        ul.add('b')        
        ul.norep()
        self.assertEqual(to_py(ul), ['b', 'a'])    


    def test_07_aabb(self):
        ul = LinkedList()                               
        ul.add('b')        
        ul.add('b')        
        ul.add('a')
        ul.add('a')        
        ul.norep()
        self.assertEqual(to_py(ul), ['a', 'b'])    


    def test_08_aabba(self):
        ul = LinkedList()                               
        ul.add('a')
        ul.add('b')        
        ul.add('b')        
        ul.add('a')
        ul.add('a')        
        ul.norep()
        self.assertEqual(to_py(ul), ['a', 'b', 'a'])    

    def test_09_aabcc(self):
        ul = LinkedList()                               
        ul.add('c')
        ul.add('c')        
        ul.add('b')        
        ul.add('a')
        ul.add('a')        
        ul.norep()
        self.assertEqual(to_py(ul), ['a', 'b', 'c'])    

class FindCoupleTest(LinkedListTest):
    
    def test_01_empty(self):
        ul = LinkedList()
        with self.assertRaises(LookupError):
            ul.find_couple('a','b')
        
    def test_02_a(self):
        ul = LinkedList()
        ul.add('a')
        with self.assertRaises(LookupError):
            ul.find_couple('a','b')

    def test_03_ab(self):
        ul = LinkedList()
        ul.add('b')        
        ul.add('a')

        self.assertEqual(ul.find_couple('a','b'), 0)
        
        with self.assertRaises(LookupError):
            ul.find_couple('b','a')
    
    def test_04_abc(self):
        ul = LinkedList()
        ul.add('c')        
        ul.add('b')        
        ul.add('a')

        self.assertEqual(ul.find_couple('a','b'), 0)
        self.assertEqual(ul.find_couple('b','c'), 1)
        
        with self.assertRaises(LookupError):
            ul.find_couple('a','c')

    def test_05_aab(self):
        ul = LinkedList()
        ul.add('b')        
        ul.add('a')        
        ul.add('a')

        self.assertEqual(ul.find_couple('a','b'), 1)

    def test_06_abbb(self):
        ul = LinkedList()
        ul.add('b')        
        ul.add('b')        
        ul.add('b')        
        ul.add('a')

        self.assertEqual(ul.find_couple('a','b'), 0)
        self.assertEqual(ul.find_couple('b','b'), 1)
        
        with self.assertRaises(LookupError):
            ul.find_couple('a','a')


class SwapTest(LinkedListTest):
    
    def test_01_empty(self):
        ul = LinkedList()
        with self.assertRaises(IndexError):
            ul.swap(0,3) 
        with self.assertRaises(IndexError):
            ul.swap(2,0)            

    def test_02_one(self):
        ul = LinkedList()
        ul.add('a')
        ul.swap(0,0)
        self.assertEqual(to_py(ul), ['a'])

    def test_03_one_wrong_indeces(self):
        ul = LinkedList()
        ul.add('a')
        with self.assertRaises(IndexError):
            ul.swap(-1,0)            
        with self.assertRaises(IndexError):
            ul.swap(0,-1)            
        with self.assertRaises(IndexError):
            ul.swap(0,2)            

    def test_04_two(self):
        ul = LinkedList()
        ul.add('b')
        ul.add('a')
        
        ul.swap(0,1)
        self.assertEqual(to_py(ul), ['b','a'])
        ul.swap(0,1)
        self.assertEqual(to_py(ul), ['a', 'b'])

    def test_05_three(self):
        ul = LinkedList()
        ul.add('c')        
        ul.add('b')
        ul.add('a')
        
        ul.swap(0,1)
        self.assertEqual(to_py(ul), ['b','a','c'])
        ul.swap(1,2)
        self.assertEqual(to_py(ul), ['b', 'c','a'])

class GapsTest(LinkedListTest):

    def test_empty(self):
        ul = LinkedList()

        self.assertEqual(ul.gaps(), [])

    def test_one(self):
        ul = LinkedList()
        ul.add(5)
        self.assertEqual(ul.gaps(), [])

    def test_5_7_one_gap(self):
        """    data: 5 7
              index: 0 1
        """
        ul = LinkedList()
        ul.add(7)
        ul.add(5)
        self.assertEqual(ul.gaps(), [1])  

    def test_7_5_no_gap(self):
        """    data: 7 5
              index: 0 1
        """
        ul = LinkedList()
        ul.add(5)
        ul.add(7)
        self.assertEqual(ul.gaps(), [])  

    def test_5_5_same(self):
        """   data:  5 5
              index: 0 1
        """
        ul = LinkedList()
        ul.add(5)
        ul.add(5)
        self.assertEqual(ul.gaps(), [])  


    def test_5_7_8_two_gaps(self):
        """    data: 5 7 8
              index: 0 1 2
        """
        ul = LinkedList()
        ul.add(8)
        ul.add(7)
        ul.add(5)
        self.assertEqual(ul.gaps(), [1,2])  

    def test_9_7_8_one_gap(self):
        """   9 7 8
              0 1 2
        """
        ul = LinkedList()
        ul.add(8)
        ul.add(7)
        ul.add(9)
        self.assertEqual(ul.gaps(), [2])  


    def test_complex(self):
        """   
              data:  9 7 6 8 9 2 2 5 
              index: 0 1 2 3 4 5 6 7              
        """
        ul = LinkedList()
        
        ul.add(5)
        ul.add(2)
        ul.add(2)
        ul.add(9)
        ul.add(8)
        ul.add(6)
        ul.add(7)
        ul.add(9)
        self.assertEqual(ul.gaps(), [3,4,7]) 
        
class FlatvTest(unittest.TestCase):

    def test_01_empty(self):
        ul = LinkedList()
        ul.flatv()
        self.assertEqual(to_py(ul),[] )

    def test_02_5(self): 
        ul = LinkedList()
        ul.add(5)
        ul.flatv()
        self.assertEqual(to_py(ul),[5] )

    def test_03_57(self): 
        ul = LinkedList()
        ul.add(7)
        ul.add(5)
        ul.flatv()
        self.assertEqual(to_py(ul),[5,7] )

    def test_04_757(self): 
        ul = LinkedList()
        ul.add(7)
        ul.add(5)
        ul.add(7)
        ul.flatv()
        self.assertEqual(to_py(ul),[7,5,5,7] )

    def test_05_657(self): 
        ul = LinkedList()
        ul.add(7)
        ul.add(5)
        ul.add(6)
        ul.flatv()
        self.assertEqual(to_py(ul),[6,5,5,7] )

    def test_06_9557(self): 
        ul = LinkedList()
        ul.add(7)
        ul.add(5)
        ul.add(5)
        ul.add(9)
        ul.flatv()
        self.assertEqual(to_py(ul),[9,5,5,7] )

    def test_07_757636(self): 
        """ Changes only first v
        """
        ul = LinkedList()
        ul.add(6)
        ul.add(3)
        ul.add(6)
        ul.add(7)
        ul.add(5)
        ul.add(7)
        ul.flatv()
        self.assertEqual(to_py(ul),[7,5,5,7,6,3,6] )

    def test_08_388758639(self): 
        """ Changes only first v
        """
        ul = LinkedList()
        ul.add(9)
        ul.add(3)
        ul.add(6)
        ul.add(8)
        ul.add(5)
        ul.add(7)
        ul.add(8)
        ul.add(8)
        ul.add(3)        
        ul.flatv()
        self.assertEqual(to_py(ul),[3,8,8,7,5,5,8,6,3,9] )      

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
      
       
#unittest.main()        