import unittest
from capped_stack_sol import *

class CappedStackTest(unittest.TestCase):    
    """ Test cases for CappedStackTest

         Note this is a *completely* separated class from CappedStack and
         we declare it here just for testing purposes!
         The 'self' you see here have nothing to do with the selfs from the
         CappedStack methods!        
    """

    def test_01_init(self): 
        """ 
            We use the special construct 'self.assertRaises(ValueError)' to state
            we are expecting the calls to CappedStack(0) and CappedStack(-1) to raise
            an ValueError.
        """
        with self.assertRaises(ValueError):
            CappedStack(0)
        with self.assertRaises(ValueError):
            CappedStack(-1)
    

    def test_02_cap(self):        
        self.assertEqual(CappedStack(1).cap(), 1) 
        self.assertEqual(CappedStack(2).cap(), 2) 
        
    def test_03_size(self):
        s = CappedStack(5)        
        self.assertEqual(s.size(), 0)
        s.push("a")
        self.assertEqual(s.size(), 1)
        s.pop()
        self.assertEqual(s.size(), 0)
    
    def test_04_str(self):
        s = CappedStack(4)
        s.push("a")
        s.push("b")        
        self.assertTrue( 'a' in s.__str__())
        self.assertTrue('b' in  s.__str__())
        self.assertTrue('4' in s.__str__())



    def test_05_is_empty(self):
        s = CappedStack(5)
        self.assertTrue(s.is_empty())
        s.push("a")
        self.assertFalse(s.is_empty())
        
                        
    def test_06_push(self):
        s = CappedStack(2)        
        self.assertEqual(s.size(), 0)
        s.push("a")
        self.assertEqual(s.size(), 1)
        s.push("b")
        self.assertEqual(s.size(), 2)
        self.assertEqual(s.peek(), "b")
        s.push("c")  # capped, pushing should do nothing now!
        self.assertEqual(s.size(), 2)
        self.assertEqual(s.peek(), "b")

    
    def test_07_peek(self):
        
        s = CappedStack(5)
        with self.assertRaises(IndexError):
            self.assertEqual(s.peek(), None)         
        s.push("a")
        self.assertEqual(s.peek(), "a")
        self.assertEqual(s.peek(), "a")  # testing peek is not changing the stack
        self.assertEqual(s.size(), 1)
        s.push("b")
        self.assertEqual(s.peek(), "b")

    def test_08_pop(self):
        
        s = CappedStack(5) 
        with self.assertRaises(IndexError):
            s.pop()
        s.push("a")        
        self.assertEqual(s.pop(), "a")

        with self.assertRaises(IndexError):
            s.pop()

class PeeknTest(unittest.TestCase):

    def test_01_peekn(self):
        s = CappedStack(10)
        s.push("a")
        s.push("b")
        s.push("c")
        s.push("d")
        s.push("e")
        self.assertEquals(s.peekn(3), ['c','d','e'])
        #self.assertEquals(s.size(), 2)
        #self.assertEqual(s.peek(), "b")
        

    def test_02_peekn_wrong_n(self):
        s = CappedStack(10)
        s.push("a")
        s.push("b")
        with self.assertRaises(IndexError):
            s.peekn(3)

        with self.assertRaises(IndexError):
            s.peekn(-1)


    def test_03_peekn_five(self):
        s = CappedStack(10)
        s.push("a")
        s.push("b")
        s.push("c")
        s.push("d")
        s.push("e")
        self.assertEquals(s.peekn(3), ['c','d','e'])
        self.assertEquals(s.size(), 5)
        self.assertEquals(s.peekn(3), ['c','d','e'])  # testing peek is not changing the stack

class PopnTest(unittest.TestCase):        
    def test_01_popn_five(self):
        s = CappedStack(10)
        s.push("a")
        s.push("b")
        s.push("c")
        s.push("d")
        s.push("e")
        self.assertEquals(s.popn(3), ['c','d','e'])
        self.assertEquals(s.size(), 2)
        self.assertEqual(s.peek(), "b")
        
class SetCapTest(unittest.TestCase):        

    def test_01_set_cap_return_none(self):        
        s = CappedStack(10)
        self.assertEqual(s.set_cap(10), None)
        
    def test_02_set_cap_too_low(self):
        s = CappedStack(10)
        with self.assertRaises(IndexError):
            s.set_cap(-1)
            
        with self.assertRaises(IndexError):
            s.set_cap(0)
            
        
    def test_03_set_cap_high(self):
        """ Will set a cap high, stack should be preserved """        
        s = CappedStack(10)
        s.push('a')
        s.push('b')
        s.push('c')
        
        s.set_cap(5)
        
        self.assertEqual(s.cap(), 5)
        self.assertEqual(s.size(), 3)
        self.assertEqual(s.peek(), 'c')        


    def test_04_set_cap_low(self):
        """ Will set a cap low, some element will be removed """
        s = CappedStack(10)
        s.push('a')
        s.push('b')
        s.push('c')
        s.push('d')
        s.push('e')
        
        s.set_cap(3)
        
        self.assertEqual(s.cap(), 3)
        self.assertEqual(s.size(), 3)
        self.assertEqual(s.peek(), 'c')        
