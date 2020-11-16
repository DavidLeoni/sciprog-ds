
import unittest
from sorting_chal_sol import *

class TestLineup(unittest.TestCase):
    
    def test_complex(self):
        waiting_room = {  # height weight beard moustache eye color (RGB)
             'The Saint':   [1.70,    90, 1,    0,        250,100,190],
             'Goliath':     [2.00,   120, 0,    0,        210,230, 30],             
             'Revolvers':   [1.80,    70, 1,    1,         40,120, 30],
             'Mammoth':     [1.60,    60, 1,    0,        110,230, 30],            
             'Razor':       [1.80,   110, 1,    0,        130,230, 20],
             'Shadow':      [1.60,    70, 1,    0,        190,230,140],    
             'Moneybags':   [1.60,    80, 1,    0,        210,230,220],
             'Bomber':      [1.70,   100, 0,    0,        140,110,170],
             'Rifleman':    [1.60,    90, 1,    1,        110, 20, 40],       
             'The Ghost':   [1.60,    50, 0,    0,        150, 70, 90]
        }
        res = lineup(waiting_room, [1.70, 80,0,    1,        190,150,230 ])        
        self.assertEqual(res, ['Revolvers','Rifleman', 'Razor','Mammoth', 'Goliath', 'The Ghost', 'Shadow', 'Bomber', 'The Saint', 'Moneybags'])    
        self.assertEqual(len(waiting_room), 0)

class TestMcFats(unittest.TestCase):
    
    def test_01_empty(self):
        self.assertEqual(mcfats([]), [])
        
    def test_02_10(self):
        self.assertEqual(mcfats([10]), [10])
        
    def test_03_10_20(self):
        self.assertEqual(mcfats([10,20]), [10,20])
        
    def test_04_20_10(self):
        self.assertEqual(mcfats([20,10]), [10,20])
        
    def test_05_keep_orig(self):
        orig = [20,10]
        self.assertEqual(mcfats(orig), [10,20])
        self.assertEqual(orig, [20,10])
        
    def test_06_10_20_30(self):
        self.assertEqual(mcfats([10,20,30]), [10,20,30])
        
    def test_07_10_30_20(self):
        self.assertEqual(mcfats([10,30,20]), [10,20,30])
        
    def test_08_20_10_30(self):
        self.assertEqual(mcfats([20, 10,30]), [10,20,30])
        
    def test_09_20_30_10(self):
        self.assertEqual(mcfats([20, 30, 10]), [10,20,30])
        
    def test_10_30_10_20(self):
        self.assertEqual(mcfats([30, 10, 20]), [10,20,30])
        
    def test_11_30_20_10(self):
        self.assertEqual(mcfats([30, 20, 10]), [10,20,30])

    def test_12_complex(self):
        #      9, 8, 7, 6, 5, 4, 3, 2, 1   # arrival time                
        cs = [80,90,50,60,80,60,80,50,70]  
        self.assertEqual(mcfats(cs), [50,50,60,60,70,80,80,80,90])  # return a new sorted version
        self.assertEqual(cs, [80,90,50,60,80,60,80,50,70])  # don't sort original
        
        
