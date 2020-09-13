import unittest
from wstack_sol import *

class WStackTest(unittest.TestCase):    

    def test_01_init(self): 
        s = WStack()

    def test_02_weight(self):
        s = WStack()
        self.assertEqual(s.weight(), 0)
        

    def test_03_size(self):
        s = WStack()        
        self.assertEqual(s.size(), 0)
        s.push(7)
        self.assertEqual(s.size(), 1)
        s.pop()
        self.assertEqual(s.size(), 0)
    
    def test_04_str(self):
        s = WStack()
        s.push(5)
        s.push(3)
        self.assertTrue('weight' in s.__str__())
        self.assertTrue( '8' in s.__str__())
        self.assertTrue( '5' in s.__str__())
        self.assertTrue('3' in  s.__str__())
        self.assertTrue('5' in s.__str__())


    def test_05_is_empty(self):
        s = WStack()
        self.assertTrue(s.is_empty())
        s.push(4)
        self.assertFalse(s.is_empty())
        
                        
    def test_06_push(self):
        s = WStack()        
        self.assertEqual(s.size(), 0)
        s.push(3)
        self.assertEqual(s.size(), 1)
        self.assertEqual(s.peek(), 3)
        self.assertEqual(s.weight(), 3)
        s.push(5)
        self.assertEqual(s.size(), 2)
        self.assertEqual(s.peek(), 5)
        self.assertEqual(s.weight(), 8)
        s.push(1)  
        self.assertEqual(s.size(), 3)
        self.assertEqual(s.peek(), 1)
        self.assertEqual(s.weight(), 9)

    
    def test_07_peek(self):
        
        s = WStack()
        with self.assertRaises(IndexError):
            self.assertEqual(s.peek(), None)         
        s.push(4)
        self.assertEqual(s.peek(), 4)
        self.assertEqual(s.peek(), 4)  # testing peek is not changing the stack
        self.assertEqual(s.size(), 1)
        s.push(5)
        self.assertEqual(s.peek(), 5)

    def test_08_pop(self):
        
        s = WStack() 
        self.assertEqual(s.weight(), 0)
        with self.assertRaises(IndexError):
            s.pop()
        s.push(3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.weight(), 0)
        s.push(4)
        s.push(5)
        self.assertEqual(s.weight(), 9)
        self.assertEqual(s.pop(), 5)
        self.assertEqual(s.weight(), 4)
        self.assertEqual(s.pop(), 4)
        self.assertEqual(s.weight(), 0)

        with self.assertRaises(IndexError):
            s.pop()


class AccumulateTest(unittest.TestCase):    

    def test_01_empty_empty_0(self):
        s1 = WStack()
        s2 = WStack()
        accumulate(s1,s2,0)
        self.assertTrue(s1.is_empty())
        self.assertTrue(s2.is_empty())

    def test_02_empty_empty_1(self):
        s1 = WStack()
        s2 = WStack()
        try:
            accumulate(s1,s2,1)
            self.fail("Should have failed !")
        except ValueError:
            pass
        self.assertTrue(s1.is_empty())
        self.assertTrue(s2.is_empty())


    def test_03_empty_empty_minus1(self):
        s1 = WStack()
        s2 = WStack()
        accumulate(s1,s2,-1)
        self.assertTrue(s1.is_empty())
        self.assertTrue(s2.is_empty())

    def test_04_5_empty_3(self):
        s1 = WStack()
        s2 = WStack()
        s1.push(5)
        accumulate(s1,s2,3)
        self.assertTrue(s1.is_empty())
        self.assertTrue(s2.size(), 1)
        self.assertTrue(s2.peek(), 5)

    def test_05_5_empty_7(self):
        s1 = WStack()
        s2 = WStack()
        s1.push(5)
        try:
            accumulate(s1,s2,7)
            self.fail("Should have failed !")
        except ValueError:
            pass
        self.assertEqual(s1.size(), 1)
        # if there is not enough amount to transfer, shouldn't even try to modify original
        self.assertEqual(s1.peek(), 5)  

    def test_06_3592_471_17(self):
        s1 = WStack()
        s2 = WStack()
        s1.push(2)
        s1.push(9)
        s1.push(5)
        s1.push(3)

        s2.push(1)
        s2.push(7)
        s2.push(4)
        accumulate(s1,s2,17)
        self.assertTrue(s1._elements == [2,9])
        self.assertTrue(s2._elements == [1,7,4,3,5])  # tot 20 >= 17