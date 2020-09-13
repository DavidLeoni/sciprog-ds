
from italian_queue_sol import *
import unittest


def to_py(italian_queue):
    """ Returns provided italian_queue as a regular Python list, in the 
        form [(v1,g1), (v2,g2), ...]. 
        
        WARNING: use it ONLY for testing!
    """
    python_list = []
    current = italian_queue._head        
    
    while (current != None):
        python_list.append((current.get_data(), current.get_group()))
        current = current.get_next()                       
    return python_list        


class InitEmptyTest(unittest.TestCase):
                
    def test_01_empty(self):
        q = ItalianQueue()
                
        self.assertEqual(q.size(), 0)        
        self.assertTrue(q.is_empty())
        
        with self.assertRaises(LookupError):
            q.top()
        
        with self.assertRaises(LookupError):
            q.top_group()

        with self.assertRaises(LookupError):
            q.tail()
        
        with self.assertRaises(LookupError):
            q.tail_group()
            
            
class EnqueueTest(unittest.TestCase):

    
    def test_01_ax(self):
        q = ItalianQueue()    

        q.enqueue('a', 'x')                      # [(a,x)]
        self.assertFalse(q.is_empty())        
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.top(), 'a')           
        self.assertEqual(q.top_group(), 'x')
        self.assertEqual(q.tail(), 'a')
        self.assertEqual(q.tail_group(), 'x')

    
    def test_02_axby(self):
        q = ItalianQueue()    

        q.enqueue('a', 'x')                      # [(a,x)]                         
        
        q.enqueue('b', 'y')                      # [(a,x), (b,y)]        
        self.assertEqual(q.size(), 2)
        self.assertEqual(q.top(), 'a')           
        self.assertEqual(q.top_group(), 'x')
        self.assertEqual(q.tail(), 'b')
        self.assertEqual(q.tail_group(), 'y')
    
    
    def test_03_axbx(self):
        q = ItalianQueue()    

        q.enqueue('a', 'x')                      # [(a,x)]                                 
        q.enqueue('b', 'x')                      # [(a,x), (b,x)]
        self.assertEqual(q.top(), 'a')
        self.assertEqual(q.top_group(), 'x')
        self.assertEqual(q.tail(), 'b')
        self.assertEqual(q.tail_group(), 'x')                    

    def test_04_axbycx(self):
        q = ItalianQueue()    

        q.enqueue('a', 'x')                      # [(a,x)]                                 
        q.enqueue('b', 'y')                      # [(a,x), (b,y)]
        q.enqueue('c', 'x')                      # [(a,x), (c,x), (b,y)]
        self.assertEqual(q.top(), 'a')
        self.assertEqual(q.top_group(), 'x')
        # white box testing: using private '_' fields 
        self.assertEqual(q._head.get_next().get_data(), 'c')   
        # white box testing: using private '_' fields
        self.assertEqual(q._head.get_next().get_group(), 'x')  
        self.assertEqual(q.tail(), 'b')
        self.assertEqual(q.tail_group(), 'y')                    
        
        
        
class DequeueTest(unittest.TestCase):
    
    def test_01_empty(self):
        q = ItalianQueue()      
                
        with self.assertRaises(LookupError):
            q.dequeue()
    
    def test_02_ax(self):
        q = ItalianQueue()      
        q.enqueue('a', 'x')                      # [(a,x)]
        self.assertEqual(q.dequeue(), 'a')       # []
        self.assertEqual(q.size(), 0)        
        
        with self.assertRaises(LookupError):
            q.top()
    
        with self.assertRaises(LookupError):
            q.top_group()
        
        with self.assertRaises(LookupError):
            q.tail()
        
        with self.assertRaises(LookupError):
            q.tail_group()
        
        with self.assertRaises(LookupError):
            q.dequeue()
    
    
    def test_03_axby(self):
        q = ItalianQueue()        
        q.enqueue('a','x')                   # [(a,x)]           
        q.enqueue('b','y')                   # [(a,x), (b,y)]  
    
        self.assertEqual(q.dequeue(), 'a')   # [(b,y)] 
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.top(), 'b')      
        self.assertEqual(q.top_group(), 'y')
        self.assertEqual(q.tail(), 'b')      
        self.assertEqual(q.tail_group(), 'y')
        
        self.assertEqual(q.dequeue(), 'b')   # []       
        self.assertEqual(q.size(), 0)        
        

    def test_04_axbxcydzez(self):
        q = ItalianQueue()        
        q.enqueue('a','x')                   
        q.enqueue('b','x')                   
        q.enqueue('c','y')                    
        q.enqueue('d','z')                   
        q.enqueue('e','z')                   # [(a,x), (b,x), (c,y), (d,z), (e,z)]  
    
        self.assertEqual(q.dequeue(), 'a')   # [(b,x), (c,y), (d,z), (e,z)]  
        self.assertEqual(q.size(), 4)
        self.assertEqual(q.top(), 'b')       # 
        self.assertEqual(q.top_group(), 'x') 
        self.assertEqual(q.tail(), 'e')       
        self.assertEqual(q.tail_group(), 'z')
        
        self.assertEqual(q.dequeue(), 'b')   # [(c,y), (d,z), (e,z)]  
        self.assertEqual(q.size(), 3)          
        self.assertEqual(q.top(), 'c')       
        self.assertEqual(q.top_group(), 'y') 
        self.assertEqual(q.tail(), 'e')       
        self.assertEqual(q.tail_group(), 'z') 

        self.assertEqual(q.dequeue(), 'c')   # [(d,z), (e,z)]  
        self.assertEqual(q.size(), 2)
        self.assertEqual(q.top(), 'd')       
        self.assertEqual(q.top_group(), 'z') 
        self.assertEqual(q.tail(), 'e')       
        self.assertEqual(q.tail_group(), 'z') 

        self.assertEqual(q.dequeue(), 'd')   # [(e,z)]  
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.top(), 'e')       
        self.assertEqual(q.top_group(), 'z') 
        self.assertEqual(q.tail(), 'e')       
        self.assertEqual(q.tail_group(), 'z') 

        self.assertEqual(q.dequeue(), 'e')   # []  
        self.assertEqual(q.size(), 0)



