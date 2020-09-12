from italian_queue_v2_sol import *
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
        self.assertEqual(len(q._tails),0)
        
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
        # white box testing: using private '_' fields 
        self.assertEqual(len(q._tails),1)
        self.assertTrue('x' in q._tails)
        self.assertEqual(q._tails['x'], q._head)
        
    def test_02_axby(self):
        q = ItalianQueue()    

        q.enqueue('a', 'x')                      # [(a,x)]                         
        
        q.enqueue('b', 'y')                      # [(a,x), (b,y)]        
        self.assertEqual(q.size(), 2)
        self.assertEqual(q.top(), 'a')           
        self.assertEqual(q.top_group(), 'x')
        self.assertEqual(q.tail(), 'b')
        self.assertEqual(q.tail_group(), 'y')
        # white box testing: using private '_' fields 
        self.assertEqual(len(q._tails),2)
        self.assertTrue('x' in q._tails)
        self.assertEqual(q._tails['x'], q._head)
        self.assertTrue('y' in q._tails)
        self.assertEqual(q._tails['y'], q._head._next)
    
    
    def test_03_axbx(self):
        q = ItalianQueue()    

        q.enqueue('a', 'x')                      # [(a,x)]                                 
        q.enqueue('b', 'x')                      # [(a,x), (b,x)]
        self.assertEqual(q.size(), 2)
        self.assertEqual(q.top(), 'a')
        self.assertEqual(q.top_group(), 'x')
        self.assertEqual(q.tail(), 'b')
        self.assertEqual(q.tail_group(), 'x')                    
        # white box testing: using private '_' fields 
        self.assertEqual(len(q._tails),1)
        self.assertTrue('x' in q._tails)
        self.assertEqual(q._tails['x'], q._head._next)


    def test_04_axbycx(self):
        q = ItalianQueue()    

        q.enqueue('a', 'x')                      # [(a,x)]                                 
        q.enqueue('b', 'y')                      # [(a,x), (b,y)]
        q.enqueue('c', 'x')                      # [(a,x), (c,x), (b,y)]
        self.assertEqual(q.top(), 'a')
        self.assertEqual(q.top_group(), 'x')
        
        self.assertEqual(q._head.get_next().get_data(), 'c')           
        self.assertEqual(q._head.get_next().get_group(), 'x')  
        self.assertEqual(q.tail(), 'b')
        self.assertEqual(q.tail_group(), 'y')                            

        self.assertEqual(len(q._tails),2)
        self.assertTrue('x' in q._tails)
        self.assertEqual(q._tails['x'], q._head._next)
        self.assertTrue('y' in q._tails)
        self.assertEqual(q._tails['y'], q._head._next._next)
        
        
class DequeueTest(unittest.TestCase):
    
    def test_01_empty(self):
        q = ItalianQueue()      
                
        with self.assertRaises(LookupError):
            q.dequeue()
    
    def test_02_ax(self):
        q = ItalianQueue()      
        # [(a,x)]
        q._size = 1
        q._head = Node('a','x')
        q._tail = q._head
        q._tails['x'] = q._head
        
        
        self.assertEqual(q.dequeue(), 'a')       # []
        self.assertEqual(q.size(), 0)        
        self.assertEqual(len(q._tails),0)

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
        
        # [(a,x), (b,y)]  
        q._size = 2
        q._head = Node('a','x')        
        q._head._next = Node('b','y')
        q._tail = q._head._next
        q._tails['x'] = q._head
        q._tails['y'] = q._tail
        
    
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
        # [(a,x), (b,x), (c,y), (d,z), (e,z)]
        q._size = 5
        q._head = Node('a','x')
        q._head._next = Node('b','x')
        q._head._next._next = Node('c','y')
        q._head._next._next._next = Node('d','z')
        q._head._next._next._next._next = Node('e','z')
        q._tail = q._head._next._next._next._next
        q._tails['x'] = q._head
        q._tails['y'] = q._head._next._next
        q._tails['z'] = q._tail
    
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
