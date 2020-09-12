from merge_sort_sol import *
import unittest


class Merge1Test(unittest.TestCase):
   
    def test_01_empty__empty(self):
        v = []
        w = []
        self.assertEqual(merge1(v, w),[])     
             
    def test_02_7__empty(self):
        v = [7]
        w = []
        self.assertEqual(merge1(v, w),[7])     
        self.assertEqual(v, []) # should empty inputs
        self.assertEqual(w, [])


    def test_03_empty__7(self):
        v = []
        w = [7]        
        self.assertEqual(merge1(v, w),[7])     
        self.assertEqual(v, []) # should empty inputs
        self.assertEqual(w, [])



    def test_04_7_9__6(self):
        v = [7,9]
        w = [6]
        self.assertEqual(merge1(v,w),[6,7,9])  
        
    def test_05_6__7_9(self):
        v = [6]
        w = [7,9]
        self.assertEqual(merge1(v,w),[6,7,9])
    
    def test_06_5_5_8__7_9(self):
        v = [5,5,8]
        w = [7,9]
        self.assertEqual(merge1(v,w),[5,5,7,8,9])

    def test_07_7_9__5_5_8(self):
        v = [7,9]
        w = [5,5,8]
        self.assertEqual(merge1(v,w),[5,5,7,8,9])

class Merge2Test(unittest.TestCase):
   
    def test_01_empty__empty(self):
        v = []
        w = []
        self.assertEqual(merge2(v, w),[])    
        
                
    def test_02_7__empty(self):
        v = [7]
        w = []
        self.assertEqual(merge2(v, w),[7])    
        self.assertEqual(v, [7]) # merge2 should *not* empty inputs
        self.assertEqual(w, [])
  

    def test_03_empty__7(self):
        v = []
        w = [7]        
        self.assertEqual(merge2(v, w),[7])     
        self.assertEqual(v, []) # merge2 should *not* empty inputs
        self.assertEqual(w, [7])

    def test_04_7_9__6(self):
        v = [7,9]
        w = [6]
        self.assertEqual(merge2(v,w),[6,7,9])  
        
    def test_05_6__7_9(self):
        v = [6]
        w = [7,9]
        self.assertEqual(merge2(v,w),[6,7,9])
    
    def test_06_5_5_8__7_9(self):
        v = [5,5,8]
        w = [7,9]
        self.assertEqual(merge2(v,w),[5,5,7,8,9])

    def test_07_7_9__5_5_8(self):
        v = [7,9]
        w = [5,5,8]
        self.assertEqual(merge2(v,w),[5,5,7,8,9])
