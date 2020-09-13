from concert_solution import *
import unittest


class DequeueTest(unittest.TestCase):

    def test_00_empty(self):

        con = Concert()
        self.assertEqual(con.dequeue(), [])

    def test_01_a(self):
        con = Concert()
        con.enqc(Person('a','x', False))
        self.assertEqual(con.dequeue(), [])
        self.assertEqual(con._cash, deque([]))
        self.assertEqual(con._entrance, deque([Person('a','x',True)]))
        
        self.assertEqual(con.dequeue(), ['a'])
        self.assertEqual(con._cash, deque([]))
        self.assertEqual(con._entrance, deque([]))

        self.assertEqual(con.dequeue(), [])
        self.assertEqual(con._cash, deque([]))
        self.assertEqual(con._entrance, deque([]))

    def test_02_axbx(self):
        con = Concert()
        con.enqc(Person('a','x', False))
        con.enqc(Person('b','x', False))
        self.assertEqual(con.dequeue(), [])
        self.assertEqual(con._cash, deque([]))
        self.assertEqual(con._entrance, deque([Person('a','x',True),Person('b','x',True)]))
        
        self.assertEqual(con.dequeue(), ['a','b'])
        self.assertEqual(con._cash, deque([]))
        self.assertEqual(con._entrance, deque([]))

        self.assertEqual(con.dequeue(), [])
        self.assertEqual(con._cash, deque([]))
        self.assertEqual(con._entrance, deque([]))

    def test_03_axbxcy(self):
        con = Concert()
        con.enqc(Person('a','x', False))
        con.enqc(Person('b','x', False))
        con.enqc(Person('c','y', False))
        self.assertEqual(con.dequeue(), [])
        self.assertEqual(con._cash, deque([Person('c','y',False)]))
        self.assertEqual(con._entrance, deque([Person('a','x',True),Person('b','x',True)]))
        
        self.assertEqual(con.dequeue(), ['a','b'])
        self.assertEqual(con._cash, deque([]))
        self.assertEqual(con._entrance, deque([Person('c','y',True)]))

        self.assertEqual(con.dequeue(), ['c'])
        self.assertEqual(con._cash, deque([]))
        self.assertEqual(con._entrance, deque([]))

    def test_04_axby_no_ticket(self):
        con = Concert()
        con.enqc(Person('a','x', False))
        con.enqe(Person('b','y', False))  # this guy is at entrance with no ticket
        
        self.assertEqual(con.dequeue(), [])
        self.assertEqual(con._cash, deque([Person('b','y',False)]))
        self.assertEqual(con._entrance, deque([Person('a','x',True)]))
        
        self.assertEqual(con.dequeue(), ['a'])
        self.assertEqual(con._cash, deque([]))
        self.assertEqual(con._entrance, deque([Person('b','y', True)]))

        self.assertEqual(con.dequeue(), ['b'])
        self.assertEqual(con._cash, deque([]))
        self.assertEqual(con._entrance, deque([]))

    def test_05_broken_queue(self):
        con = Concert()
        con.enqe(Person('a','x',True))  
        con.enqe(Person('b','x',False))
        con.enqe(Person('c','x',True)) 
        con.enqc(Person('f','y',False)) 

        self.assertEqual(con.dequeue(), ['a', 'c'])
        self.assertEqual(con.dequeue(), ['f'])
        self.assertEqual(con.dequeue(), ['b'])
        self.assertEqual(con.dequeue(), [])


    def test_06_complex(self):
        con = Concert()

        con.enqc(Person('a','x',False))
        con.enqc(Person('b','x',False))
        con.enqc(Person('c','x',False))
        con.enqc(Person('d','y',False))
        con.enqc(Person('e','z',False))
        con.enqc(Person('f','z',False))
        con.enqc(Person('g','w',False))

        self.assertEqual(con.dequeue(), [])

        self.assertEqual(con.dequeue(), ['a','b','c'])
        self.assertEqual(con.dequeue(), ['d'])
        self.assertEqual(con.dequeue(), ['e','f'])
        self.assertEqual(con.dequeue(), ['g'])
