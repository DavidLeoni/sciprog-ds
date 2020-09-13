from selection_sort_solution import *
import unittest

class SwapTest(unittest.TestCase):
   
    def test_01_one_element(self):
        v = ['a'];
        swap(v,0,0)
        self.assertEqual(v, ['a'])

    def test_02_two_elements(self):
        v = ['a','b'];
        swap(v,0,1)
        self.assertEqual(v, ['b','a'])
        
    def test_03_return_none(self):
        v = ['a','b', 'c', 'd'];
        self.assertEqual(None, swap(v,1,3))
        
        
    def test_04_long_list(self):
        v = ['a','b', 'c', 'd'];
        swap(v,1,3)
        self.assertEqual(v, ['a', 'd','c', 'b'])
        
        
    def test_05_swap_property(self):
        v = ['a','b','c','d'];
        w = ['a','b','c','d'];
        swap(v,1,3)
        swap(w,3,1)
        self.assertEqual(v, w)

    def test_06_double_swap(self):
        v = ['a','b','c','d'];        
        swap(v,1,3)
        swap(v,1,3)
        self.assertEqual(v, ['a','b','c','d'])   

        

class ArgminTest(unittest.TestCase):
   
    def test_01_one_element(self):
        self.assertEqual(argmin([1],0),0)     

    def test_02_two_elements(self):
        self.assertEqual(argmin([1,2],0),0)
        self.assertEqual(argmin([2,1],0),1)
        self.assertEqual(argmin([2,1],1),1)
        
    def test_03_long_list(self):
        self.assertEqual(argmin([8,9,6,5,7],2),3) 
        
        
class SelectionSortTest(unittest.TestCase):
   
    def test_01_zero_elements(self):
        v = []
        selection_sort(v)
        self.assertEqual(v,[])     
        
    def test_02_return_none(self):    
        self.assertEqual(None, selection_sort([2]))        
        
    def test_03_one_element(self):
        v = ["a"]
        selection_sort(v)
        self.assertEqual(v,["a"])     
        

    def test_04_two_elements(self):
        v = [2,1]
        selection_sort(v)
        self.assertEqual(v,[1,2])  
        
    def test_05_three_elements(self):
        v = [2,1,3]
        selection_sort(v)
        self.assertEqual(v,[1,2,3])
    
    def test_06_piccinno_list(self):        
        v = [23, 34, 55, 32, 7777, 98, 3, 2, 1]        
        selection_sort(v)
        vcopy = v[:]
        vcopy.sort()
        self.assertEqual(v, vcopy)    