import unittest
from stacktris_solution import *



class StacktrisTest(unittest.TestCase):    

    def test_init(self): 
       st = Stacktris()
       self.assertEqual(st._stack, [])
    
    def test_str(self):
        s = Stacktris()
        s.drop1(1)
        s.drop1(0)
        self.assertTrue('Stacktris' in s.__str__())
        self.assertTrue( '|11 |' in s.__str__())

    def test_is_empty(self):
        s = Stacktris()
        self.assertTrue(s.is_empty())

        s.drop1(0)
        self.assertFalse(s.is_empty())
        
        
class ShortenTest(unittest.TestCase):

    def test_empty(self):
        st = Stacktris()
        st._shorten()
        self.assertEqual(st._stack, [])

    def test_010(self):
        st = Stacktris()
        st._stack = [
            [0,1,0]
        ]
        st._shorten()
        self.assertEqual(st._stack, [
            [0,1,0]
        ])

    def test_111(self):
        st = Stacktris()
        st._stack = [
            [1,1,1]
        ]
        st._shorten()
        self.assertEqual(st._stack, [            
        ])


    def test_212(self):
        st = Stacktris()
        st._stack = [
            [2,1,2]
        ]
        st._shorten()
        self.assertEqual(st._stack, [            
        ])

    def test_010_221(self):
        st = Stacktris()
        st._stack = [
            [0,1,0],
            [2,2,1]
        ]
        st._shorten()
        self.assertEqual(st._stack, [
            [0,1,0]
        ])

    def test_121_011(self):
        st = Stacktris()
        st._stack = [            
            [1,2,1],
            [0,1,1],            
        ]
        st._shorten()
        self.assertEqual(st._stack, [
            [0,1,1]
        ])

    def test_121_221(self):
        st = Stacktris()
        st._stack = [            
            [1,2,1],
            [2,2,1],            
        ]
        st._shorten()
        self.assertEqual(st._stack, [
            [1,2,1]
        ])

    def test_012_221_011(self):
        st = Stacktris()
        st._stack = [            
            [0,1,2],
            [2,2,1],
            [0,1,1],            
        ]
        st._shorten()
        self.assertEqual(st._stack, [
            [0,1,2],
            [0,1,1]
        ])


class Drop1Test(unittest.TestCase): 
    
    def test_100(self):
        st = Stacktris()
        self.assertEqual(st.drop1(0), [])
        self.assertEqual(st._stack, [
            [1,0,0]
        ])

    def test_010(self):
        st = Stacktris()
        self.assertEqual(st.drop1(1), [])
        self.assertEqual(st._stack, [
            [0,1,0]
        ])        

    def test_001(self):
        st = Stacktris()
        self.assertEqual(st.drop1(2), [])
        self.assertEqual(st._stack, [
            [0,0,1]
        ])

    def test_out_of_bounds(self):
        st = Stacktris()
        with self.assertRaises(ValueError):
            st.drop1(-1)

        with self.assertRaises(ValueError):
            st.drop1(3)

    def test_100_100(self):
        st = Stacktris()
        self.assertEqual(st.drop1(0), [])
        self.assertEqual(st.drop1(0), [])
        self.assertEqual(st._stack, [
            [1,0,0],
            [1,0,0]
        ])        

    def test_220_100(self):
        st = Stacktris()
        st._stack = [
            [2,2,0]
        ]
        self.assertEqual(st.drop1(0), [])
        self.assertEqual(st._stack, [
            [2,2,0],
            [1,0,0]
        ])        


    def test_110(self):
        st = Stacktris()
        self.assertEqual(st.drop1(0), [])
        self.assertEqual(st.drop1(1),[])
        self.assertEqual(st._stack, [
            [1,1,0]
        ])                


    def test_111(self):
        st = Stacktris()
        self.assertEqual(st.drop1(0), [])
        self.assertEqual(st.drop1(1), [])
        self.assertEqual(st.drop1(2), [1,1,1])
        self.assertEqual(st._stack, [
        ])                        

    def test_110_101(self):
        st = Stacktris()
        self.assertEqual(st.drop1(0), [])
        self.assertEqual(st.drop1(1), [])
        self.assertEqual(st.drop1(0), [])
        self.assertEqual(st._stack, [
            [1,1,0],
            [1,0,0]
        ])                        
        self.assertEqual(st.drop1(2), [1,1,1])
        self.assertEqual(st._stack, [
            [1,0,0]
        ])                        

    def test_101_101_101_010(self):
        st = Stacktris()
        self.assertEqual(st.drop1(0), [])
        self.assertEqual(st.drop1(2), [])
        self.assertEqual(st.drop1(0), [])
        self.assertEqual(st.drop1(2), [])
        self.assertEqual(st.drop1(0), [])
        self.assertEqual(st.drop1(2), [])
        self.assertEqual(st.drop1(1), [1,1,1])
        self.assertEqual(st._stack, [
            [1,0,1],
            [1,0,1]
        ])                        


    def test_220_001(self):
        st = Stacktris()
        st._stack = [
            [2,2,0]
        ]
        self.assertEqual(st.drop1(2), [2,2,1])
        self.assertEqual(st._stack, [
        ])        

    def test_022_220_100(self):
        st = Stacktris()
        st._stack = [
            [0,2,2],           
            [2,2,0]
        ]
        self.assertEqual(st.drop1(0), [])
        self.assertEqual(st._stack, [
            [0,2,2],           
            [2,2,0],
            [1,0,0]
        ])        

    def test_022_220_001(self):
        st = Stacktris()
        st._stack = [
            [0,2,2],           
            [2,2,0]
        ]
        self.assertEqual(st.drop1(2), [2,2,1])
        self.assertEqual(st._stack, [
            [0,2,2]
        ])        


class Drop2hTest(unittest.TestCase): 

    def test_empty_220(self):
        st = Stacktris()
        self.assertEqual(st.drop2h(0), [])
        self.assertEqual(st._stack, [
            [2,2,0]
        ])        

    def test_empty_022(self):
        st = Stacktris()
        self.assertEqual(st.drop2h(1), [])
        self.assertEqual(st._stack, [
            [0,2,2]
        ])                

    def test_out_of_bounds(self):
        st = Stacktris()
        
        with self.assertRaises(ValueError):
            st.drop2h(-1)
                        
        with self.assertRaises(ValueError):
            st.drop2h(2)

        with self.assertRaises(ValueError):
            st.drop2h(3)

    def test_100_022(self):
        st = Stacktris()
        st.drop1(0)
        self.assertEqual(st.drop2h(1), [1,2,2])
        self.assertEqual(st._stack, [
        ])                


    def test_110_220(self):
        st = Stacktris()
        st.drop1(0)
        st.drop1(1)
        self.assertEqual(st.drop2h(0), [])
        self.assertEqual(st._stack, [
            [1,1,0],
            [2,2,0]
        ])                

    def test_110_022(self):
        st = Stacktris()
        st.drop1(0)
        st.drop1(1)
        self.assertEqual(st.drop2h(1), [])
        self.assertEqual(st._stack, [
            [1,1,0],
            [0,2,2]
        ])                


    def test_101_220_001(self):
        st = Stacktris()
        st.drop1(0)
        st.drop1(2)
        st.drop2h(0)
        self.assertEqual(st._stack, [
            [1,0,1],
            [2,2,0]
        ])                
        st.drop1(2)
        self.assertEqual(st._stack, [
            [1,0,1]
        ])                

    def test_complex(self):
        st = Stacktris()
        self.assertEqual(st.drop1(2), [])
        self.assertEqual(st._stack, [
            [0,0,1]
        ])
        self.assertEqual(st.drop2h(1), [])
        self.assertEqual(st._stack, [
            [0,0,1],
            [0,2,2],
        ])
        self.assertEqual(st.drop1(0), [])
        self.assertEqual(st._stack, [
            [1,0,1],
            [0,2,2],
        ])
        self.assertEqual(st.drop2h(1), [])
        self.assertEqual(st._stack, [
            [1,0,1],
            [0,2,2],
            [0,2,2],
        ])
        self.assertEqual(st.drop1(0), [1,2,2])
        self.assertEqual(st._stack, [
            [1,0,1],
            [0,2,2],
        ])
        self.assertEqual(st.drop2h(0), [])
        self.assertEqual(st._stack, [
            [1,0,1],
            [0,2,2],
            [2,2,0]
        ])
        self.assertEqual(st.drop1(2), [2,2,1])
        self.assertEqual(st._stack, [
            [1,0,1],
            [0,2,2]
        ])
        self.assertEqual(st.drop1(0), [1,2,2])
        self.assertEqual(st._stack, [
            [1,0,1],
            
        ])
