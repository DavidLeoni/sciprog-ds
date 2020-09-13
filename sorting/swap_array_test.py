import unittest
from swap_array_sol import *

class SwapTest(unittest.TestCase):

    def test_01_zero_element(self):
        sarr = SwapArray([]);
        with self.assertRaises(IndexError):
            sarr.swap_next( 0)
        with self.assertRaises(IndexError):
            sarr.swap_next(1)
        with self.assertRaises(IndexError):
            sarr.swap_next(-1)

    
    def test_02_one_element(self):
        sarr = SwapArray(['a']);
        with self.assertRaises(IndexError):
            sarr.swap_next(0)
        

    def test_03_two_elements(self):
        sarr = SwapArray(['a','b']);
        sarr.swap_next(0)
        self.assertEqual(sarr._arr, ['b','a'])
        
    def test_04_return_none(self):
        sarr = SwapArray(['a','b', 'c', 'd']);
        self.assertEqual(None, sarr.swap_next(1))
                
    def test_05_long_list(self):
        sarr = SwapArray(['a','b', 'c', 'd']);
        sarr.swap_next(1)
        self.assertEqual(sarr._arr, ['a', 'c','b', 'd'])
        

class IsSortedTest(unittest.TestCase):
    
    def test_01_is_sorted_empty(self):
        self.assertTrue(is_sorted(SwapArray([])))

    def test_02_is_sorted_one(self):
        self.assertTrue(is_sorted(SwapArray([6])))

    def test_03_is_sorted_two(self):
        self.assertTrue(is_sorted(SwapArray([7,7])))
        self.assertTrue(is_sorted(SwapArray([6,7])))
        self.assertFalse(is_sorted(SwapArray([7,6])))    

    def test_04_is_sorted_three(self):
        self.assertTrue(is_sorted(SwapArray([6,7,8])))
        self.assertFalse(is_sorted(SwapArray([8,8,7])))


class MaxToRightTest(unittest.TestCase):
    
    def test_01_max_to_right_empty(self):        
        sarr = SwapArray([])
        max_to_right(sarr,0)
        self.assertEqual(sarr._arr, [])

    def test_02_max_to_right_return_none(self):        
        sarr = SwapArray([])
        self.assertEqual(None, max_to_right(sarr,0))


    def test_03_right_max_to_right_1(self):        
        
        sarr = SwapArray([5])
        max_to_right(sarr,0)
        self.assertEqual(5, sarr.get(0))

    def test_04_right_max_to_right_2_first(self):        
        sarr = SwapArray([7, 6])
        max_to_right(sarr,0)
        self.assertEqual(sarr.get(0), 7)
        self.assertEqual(sarr.get(1), 6)

    def test_05_right_max_to_right_2_first(self):        
        sarr = SwapArray([7, 6])
        max_to_right(sarr,1)
        self.assertEqual(sarr.get(0), 6)
        self.assertEqual(sarr.get(1), 7)

    def test_06_right_max_to_right_2_last(self):        
        sarr = SwapArray([6,7])
        max_to_right(sarr,0)
        self.assertEqual(sarr.get(0), 6)
        self.assertEqual(sarr.get(1), 7)


    def test_07_right_max_to_right_2_last(self):        
        sarr = SwapArray([6,7])
        max_to_right(sarr,1)
        self.assertEqual(sarr.get(0), 6)
        self.assertEqual(sarr.get(1), 7)
        

    def test_08_right_max_to_right_3_first(self):        
        sarr = SwapArray([8,6, 7])
        max_to_right(sarr,0)
        self.assertEqual(sarr.get(0), 8)
        self.assertTrue(6 in sarr._arr[1:3])
        self.assertTrue(7 in sarr._arr[1:3])        

    def test_09_right_max_to_right_3_first(self):        
        sarr = SwapArray([8,6, 7])
        max_to_right(sarr,1)
        self.assertEqual(sarr.get(1), 8)
        self.assertTrue(sarr._arr[0] == 6 or sarr._arr[2] == 6)
        self.assertTrue(sarr._arr[0] == 7 or sarr._arr[2] == 7)
        

    def test_10_right_max_to_right_3_first(self):        
        sarr = SwapArray([8,6, 7])
        max_to_right(sarr,2)
        self.assertEqual(sarr.get(2), 8)
        self.assertTrue(6 in sarr._arr[0:2])
        self.assertTrue(7 in sarr._arr[0:2])        

    def test_11_right_max_to_right_3_middle(self):        
        sarr = SwapArray([7, 8, 6])
        max_to_right(sarr,0)
        self.assertEqual(sarr.get(0), 7)
        self.assertTrue(6 in sarr._arr[1:3])
        self.assertTrue(8 in sarr._arr[1:3])        


    def test_12_right_max_to_right_3_middle(self):        
        sarr = SwapArray([7, 8, 6])
        max_to_right(sarr,1)
        self.assertEqual(sarr.get(1), 8)
        self.assertTrue(sarr._arr[0] == 6 or sarr._arr[2] == 6)
        self.assertTrue(sarr._arr[0] == 7 or sarr._arr[2] == 7)


    def test_13_right_max_to_right_3_middle(self):        
        sarr = SwapArray([7, 8, 6])
        max_to_right(sarr,2)
        self.assertEqual(sarr.get(2), 8)
        self.assertTrue(6 in sarr._arr[0:2])
        self.assertTrue(7 in sarr._arr[0:2])        


    def test_14_right_max_to_right_3_last(self):        
        sarr = SwapArray([7, 6, 8])
        max_to_right(sarr,0)
        self.assertEqual(sarr.get(0), 7)
        self.assertTrue(6 in sarr._arr[1:3])
        self.assertTrue(8 in sarr._arr[1:3])        

             
    def test_15_right_max_to_right_3_last(self):        
        sarr = SwapArray([7, 6, 8])
        max_to_right(sarr,1)
        self.assertEqual(sarr.get(1), 7)
        self.assertTrue(sarr._arr[0] == 6 or sarr._arr[2] == 6)
        self.assertTrue(sarr._arr[0] == 8 or sarr._arr[2] == 8)


    def test_16_right_max_to_right_3_last(self):        
        sarr = SwapArray([7, 6, 8])
        max_to_right(sarr,2)
        self.assertEqual(sarr.get(2), 8)
        self.assertTrue(6 in sarr._arr[0:2])
        self.assertTrue(7 in sarr._arr[0:2])        

class SwapSortTest(unittest.TestCase):
    """ Test cases for swapsort function

    """    
            
    def test_zero_elements(self):
        v = SwapArray([])
        swapsort(v)
        self.assertEqual(v._arr,[])     
        
    def test_return_none(self):    
        self.assertEqual(None, swapsort(SwapArray([2])))        
        
    def test_one_element(self):
        v = SwapArray(["a"])
        swapsort(v)
        self.assertEqual(v._arr,["a"])     
        

    def test_two_elements(self):
        v = SwapArray([2,1])
        swapsort(v)
        self.assertEqual(v._arr,[1,2])  
        
    def test_three_elements(self):
        v = SwapArray([2,1,3])
        swapsort(v)
        self.assertEqual(v._arr,[1,2,3])
    
    def test_piccinno_list(self):        
        v = SwapArray([23, 34, 55, 32, 7777, 98, 3, 2, 1])
        swapsort(v)
        vcopy = v._arr[:]
        vcopy.sort()
        self.assertEqual(v._arr, vcopy) 