
from intro_exercise import *

import unittest

class MyTest(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(3,5), 8)
        
        
    def test_sub(self):
        self.assertEqual(sub(7,4), 3)        