
import unittest
from linked_queue_solution import *


class InitEmptyTest(unittest.TestCase):

    def test_01_empty(self):
        q = LinkedQueue()

        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())

        with self.assertRaises(LookupError):
            q.top()

        with self.assertRaises(LookupError):
            q.tail()


class EnqnTest(unittest.TestCase):


    def test_01_a(self):
        q = LinkedQueue()

        q.enqn(['a'])                      # [a]
        self.assertFalse(q.is_empty())
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.top(), 'a')
        self.assertEqual(q.tail(), 'a')


    def test_02_ab(self):
        q = LinkedQueue()

        q.enqn(['a','b'])                     # [a,b]

        self.assertEqual(q.size(), 2)
        self.assertEqual(q.top(), 'a')
        self.assertEqual(q.tail(), 'b')


    def test_03_a_bc(self):
        q = LinkedQueue()

        q.enqn(['a'])                      # [a]
        q.enqn(['b', 'c'])                      # [a, b, c]

        self.assertEqual(q.size(), 3)
        self.assertEqual(q.top(), 'a')
        self.assertEqual(q._head.get_next().get_data(), 'b')   # white box testing: using private '_' fields
        self.assertEqual(q.tail(), 'c')

    def test_04_ab_c(self):
        q = LinkedQueue()

        q.enqn(['a', 'b'])                      # [a]
        q.enqn(['c'])                      # [a, b, c]
        self.assertEqual(q.size(), 3)
        self.assertEqual(q.top(), 'a')
        self.assertEqual(q._head.get_next().get_data(), 'b')   # white box testing: using private '_' fields
        self.assertEqual(q.tail(), 'c')


    def test_04_ab_cdef(self):
        q = LinkedQueue()

        q.enqn(['a', 'b'])                      # [a,'b']
        q.enqn(['c','d','e'])                   # [a, b, c,'d','e']
        self.assertEqual(q.size(), 5)
        self.assertEqual(q.top(), 'a')
        self.assertEqual(q._head.get_next().get_data(), 'b')   # white box testing: using private '_' fields
        self.assertEqual(q._head.get_next().get_next().get_data(), 'c')   # white box testing: using private '_' fields
        self.assertEqual(q._head.get_next().get_next().get_next().get_data(), 'd')   # white box testing: using private '_' fields
        self.assertEqual(q.tail(), 'e')


class DeqnTest(unittest.TestCase):

    def test_01_empty(self):
        q = LinkedQueue()

        q.deqn(0)

        with self.assertRaises(LookupError):
            q.deqn(1)

        with self.assertRaises(LookupError):
            q.deqn(2)


    def test_02_a(self):
        q = LinkedQueue()
        q.enqn(['a'])                           # [a]
        self.assertEqual(q.deqn(1), ['a'])       # []
        self.assertEqual(q.size(), 0)

        with self.assertRaises(LookupError):
            q.top()

        with self.assertRaises(LookupError):
            q.tail()

        with self.assertRaises(LookupError):
            q.deqn(2)


    def test_03_ab_c(self):
        q = LinkedQueue()
        q.enqn(['a', 'b','c'])                # [a,b,c]

        self.assertEqual(q.deqn(1), ['a'])   # [b,c]
        self.assertEqual(q.size(), 2)
        self.assertEqual(q.top(), 'b')
        self.assertEqual(q.tail(), 'c')
        self.assertEqual(q.deqn(2), ['b','c'])   # []
        self.assertEqual(q.size(), 0)

        with self.assertRaises(LookupError):
            q.top()

        with self.assertRaises(LookupError):
            q.tail()

    def test_03_ab_cde(self):
        q = LinkedQueue()
        q.enqn(['a', 'b','c','d','e'])               # [a,b,c,d,e]

        self.assertEqual(q.deqn(3), ['a','b','c'])   # [d,e]
        self.assertEqual(q.size(), 2)
        self.assertEqual(q.top(), 'd')
        self.assertEqual(q.tail(), 'e')
        self.assertEqual(q.deqn(1), ['d'])   # [e]
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.top(), 'e')
        self.assertEqual(q.tail(), 'e')

        self.assertEqual(q.deqn(1), ['e'])   # []
        self.assertEqual(q.size(), 0)

        with self.assertRaises(LookupError):
            q.top()

        with self.assertRaises(LookupError):
            q.tail()
