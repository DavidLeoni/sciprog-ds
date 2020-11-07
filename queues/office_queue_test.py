import unittest
from office_queue_sol import *

SERVICES = { 'x':5,   # minutes
             'y':20,
             'z':30
           }

def to_py(office_queue):
    """ Returns office_queue as a regular Python list - handy for testing
    """
    python_list = []
    current = office_queue._head
    
    while (current != None):
        python_list.append((current.get_data(), current.get_service()))
        current = current.get_next()                       
    return python_list    

class OfficeTest(unittest.TestCase):

    def myAssert(self, office_queue, python_list):
        """ Checks provided office_queue can be represented as the given python_list,
            as a list of tuples like [('a','z'),('b','y'),('c','z')]
        """
        self.assertEqual(to_py(office_queue), python_list)
        self.assertEqual(office_queue._size, len(python_list))
        expected_wait_time = sum([office_queue._services[x[1]] for x in python_list])
        self.assertEqual(office_queue._wait_time, expected_wait_time)
        if len(python_list) > 0:
            self.assertEqual(office_queue._tail._data, python_list[-1][0])

class InitEmptyTest(OfficeTest):

    def test_01_empty(self):
        q = OfficeQueue(SERVICES)

        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())


class TimeToServiceTest(unittest.TestCase):

    def test_01_empty(self):
        oq = OfficeQueue(SERVICES)
        self.assertEqual(oq.time_to_service(), {'x':0, 'y':0,'z':0})

    def test_02_ax(self):
        oq = OfficeQueue(SERVICES)
        oq.enqueue('a','x')
        self.assertEqual(oq.time_to_service(), {'x':0, 'y':5,'z':5})

    def test_03_by(self):
        oq = OfficeQueue(SERVICES)
        oq.enqueue('b','y')
        self.assertEqual(oq.time_to_service(), {'x':20, 'y':0,'z':20})


    def test_04_ax_by(self):
        oq = OfficeQueue(SERVICES)
        oq.enqueue('a','x')
        oq.enqueue('b','y')
        self.assertEqual(oq.time_to_service(), {'x':0, 'y':5,'z':25})

    def test_05_az_bx(self):
        oq = OfficeQueue(SERVICES)
        oq.enqueue('a','z')
        oq.enqueue('b','x')
        self.assertEqual(oq.time_to_service(), {'x':30, 'y':35,'z':0})


    def test_06_ax_by_cz(self):
        oq = OfficeQueue(SERVICES)
        oq.enqueue('a','x')
        oq.enqueue('b','y')
        oq.enqueue('c','z')
        self.assertEqual(oq.time_to_service(), {'x':0, 'y':5,'z':25})

    def test_07_ay_by_cx_dy_ez_fy(self):
        oq = OfficeQueue(SERVICES)
        oq.enqueue('a','y')
        oq.enqueue('b','y')
        oq.enqueue('c','x')
        oq.enqueue('d','y')
        oq.enqueue('e','z')
        oq.enqueue('f','y')
        self.assertEqual(oq.time_to_service(), {'x':20+20, 'y':0,'z':20+20+5+20})

    """ 
        wait time: 155

        cumulative wait:  5    10   15   45   50   55   85   105  110  130  150  155
        wait times:       5    5    5    30   5    5    30   20   5    20   20   5
                          x    x    x    z    x    x    z    y    x    y    y    x
                          a -> b -> c -> d -> e -> f -> g -> h -> i -> l -> m -> n
                         ||              |                   |
                         x : 0           |                   |
                         |               |                   |
                         |---------------|                   |
                         |     z : 15                        | 
                         |                                   |
                         |-----------------------------------|
                                        y : 85
    """
    def test_09_complex(self):
        oq = OfficeQueue(SERVICES)
        oq.enqueue('a','x')
        oq.enqueue('b','x')
        oq.enqueue('c','x')
        oq.enqueue('d','z')
        oq.enqueue('e','x')
        oq.enqueue('f','x')
        oq.enqueue('g','z')
        oq.enqueue('h','y')
        oq.enqueue('i','x')
        oq.enqueue('l','y')
        oq.enqueue('m','y')
        oq.enqueue('n','x')
        self.assertEqual(oq.time_to_service(), {'x':0,
                                                'y':85,
                                                'z':15})
        

class SplitTest(OfficeTest):
    
    def test_01_empty(self):
        oq = OfficeQueue(SERVICES)
        new_oq = oq.split()
        self.myAssert(oq, [])
        self.myAssert(new_oq, [])

    def test_02_ax(self):
        oq = OfficeQueue(SERVICES)
        oq.enqueue('a','x')
        new_oq = oq.split()
        self.myAssert(oq, [('a','x')])
        self.myAssert(new_oq, [])

    def test_03_ax_bx(self):
        oq = OfficeQueue(SERVICES)
        oq.enqueue('a','x')
        oq.enqueue('b','x')
        new_oq = oq.split()
        self.myAssert(oq, [('a','x')])
        self.myAssert(new_oq, [('b','x')])

    def test_04_ay_bx(self):
        oq = OfficeQueue(SERVICES)
        oq.enqueue('a','y')
        oq.enqueue('b','x')
        new_oq = oq.split()
        self.myAssert(oq, [('a','y')])        
        self.myAssert(new_oq, [('b','x')])        

    def test_05_az_by(self):
        oq = OfficeQueue(SERVICES)
        oq.enqueue('a','z')
        oq.enqueue('b','y')
        new_oq = oq.split()
        self.myAssert(oq, [('a','z')])
        self.myAssert(new_oq, [('b','y')])

    def test_06_ax_by(self):
        oq = OfficeQueue(SERVICES)
        oq.enqueue('a','x')
        oq.enqueue('b','y')
        new_oq = oq.split()
        self.myAssert(oq, [('a','x'), ('b','y')])
        self.myAssert(new_oq, [])

    def test_07_ax_bz_cy(self):
        oq = OfficeQueue(SERVICES)
        oq.enqueue('a','x')
        oq.enqueue('b','z')
        oq.enqueue('c','y')
        new_oq = oq.split()
        self.myAssert(oq, [('a','x'), ('b','z')])
        self.myAssert(new_oq, [('c','y')])

    """
        wait times:       30   20   30   30   5    5    20   5    5
        cumulative wait:  30   50   80   110  115  120  140  145  150  
                          z    y    z    z    x    x    y    x    x
                          a -> b -> c -> d -> e -> f -> g -> h -> i                    
                          ^            ^                          ^
                          |            |                          |
                         head       cut here                     tail
    """
    def test_08_complex(self):
        oq = OfficeQueue(SERVICES)
        oq.enqueue('a','z')
        oq.enqueue('b','y')
        oq.enqueue('c','z')
        oq.enqueue('d','z')
        oq.enqueue('e','x')
        oq.enqueue('f','x')
        oq.enqueue('g','y')
        oq.enqueue('h','x')
        oq.enqueue('i','x')
        new_oq = oq.split()
        self.myAssert(oq, [('a','z'),('b','y'),('c','z')])
        self.myAssert(new_oq, [('d','z'), ('e','x'), ('f','x'), ('g','y'), ('h','x'), ('i','x')])

        
        