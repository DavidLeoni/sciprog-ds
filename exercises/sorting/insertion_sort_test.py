from insertion_sort_solution import *
import unittest

        
class InsertionSortTest(unittest.TestCase):
   
    def test_01_zero_elements(self):
        v = []
        insertion_sort(v)
        self.assertEqual(v,[])     
        
    def test_02_return_none(self):    
        self.assertEqual(None, insertion_sort([2]))        
        
    def test_03_one_element(self):
        v = ["a"]
        insertion_sort(v)
        self.assertEqual(v,["a"])     
        

    def test_04_two_elements(self):
        v = [2,1]
        insertion_sort(v)
        self.assertEqual(v,[1,2])  
        
    def test_05_three_elements(self):
        v = [2,1,3]
        insertion_sort(v)
        self.assertEqual(v,[1,2,3])
    
    def test_06_piccinno_list(self):        
        v = [23, 34, 55, 32, 7777, 98, 3, 2, 1]        
        insertion_sort(v)
        vcopy = v[:]
        vcopy.sort()
        self.assertEqual(v, vcopy)    