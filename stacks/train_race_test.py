import unittest
from train_race_sol import *


class VelocityLessOrEqualThanTrainSizeTest (unittest.TestCase):
    
    def test_01_empty(self):
        
        tr = TrainRace([],[])                
        self.assertEqual(tr.get_paths(), [])
        tr.step()
        self.assertEqual(tr.get_paths(), [])
        
    def test_02_neg(self):
        
        with self.assertRaises(ValueError):
            TrainRace([-1],[3])
            
        with self.assertRaises(ValueError):
            TrainRace([2],[-2])
            
    def test_03_zero(self):
        
        with self.assertRaises(ValueError):
            TrainRace([4,2],[6,0])
        with self.assertRaises(ValueError):
            TrainRace([4,2],[0,3])
            
        with self.assertRaises(ValueError):
            TrainRace([2,0],[5,6])
            
            
    def test_04_mismatch(self):
        
        with self.assertRaises(ValueError):
            TrainRace([4,2],[6,1,3])

        with self.assertRaises(ValueError):
            TrainRace([6,4,3,2],[6,2,4])                        


    def test_05_1_1(self):
        
        tr = TrainRace([1],[1])
        paths = tr.get_paths()
        
        self.assertEqual(len(paths), 1)
        
        self.assertEqual(''.join(paths[0]), '*')        
        
        tr.step()
        paths = tr.get_paths()
        
        self.assertEqual(''.join(paths[0]), '-*')
        
        tr.step()
        paths = tr.get_paths()
        
        self.assertEqual(''.join(paths[0]), '--*')
        
        
    def test_06_2_1(self):
        
        tr = TrainRace([2],[1])
        paths = tr.get_paths()
        
        self.assertEqual(len(paths), 1)
        self.assertEqual(''.join(paths[0]), '**')
        
        tr.step()
        paths = tr.get_paths()
        
        self.assertEqual(''.join(paths[0]), '-**')
        
        tr.step()
        paths = tr.get_paths()
        
        self.assertEqual(''.join(paths[0]), '--**')
        
    def test_07_2_2(self):
        
        tr = TrainRace([2],[2])
        paths = tr.get_paths()
        
        self.assertEqual(len(paths), 1)
        
        self.assertEqual(''.join(paths[0]), '**')
        
        tr.step()
        paths = tr.get_paths()
        
        self.assertEqual(''.join(paths[0]), '--**')
        
        tr.step()
        paths = tr.get_paths()
        
        self.assertEqual(''.join(paths[0]), '----**')
        
    def test_08_4_3_1_2(self):
        
        tr = TrainRace([4,3],[1,2])
        
        paths = tr.get_paths()
        
        self.assertEqual(len(paths), 2)        
        self.assertEqual(''.join(paths[0]), '****')
        self.assertEqual(''.join(paths[1]), '***')
        
        tr.step()
        paths = tr.get_paths()
        
        self.assertEqual(''.join(paths[0]), '-****')        
        self.assertEqual(''.join(paths[1]), '--***')
        
        tr.step()
        paths = tr.get_paths()
        
        self.assertEqual(''.join(paths[0]), '--****')        
        self.assertEqual(''.join(paths[1]), '----***')
        
    def test_09_complex(self):
        
        tr = TrainRace([5,3,6,3], [2,1,3,2])
        
        paths = tr.get_paths()
        
        self.assertEqual(len(paths), 4)        
        self.assertEqual(''.join(paths[0]), '*****')
        self.assertEqual(''.join(paths[1]), '***')
        self.assertEqual(''.join(paths[2]), '******')
        self.assertEqual(''.join(paths[3]), '***')
        
        tr.step()        
        paths = tr.get_paths()
        
        self.assertEqual(len(paths), 4)
        self.assertEqual(''.join(paths[0]), '--*****')
        self.assertEqual(''.join(paths[1]), '-***')
        self.assertEqual(''.join(paths[2]), '---******')
        self.assertEqual(''.join(paths[3]), '--***')
        
        tr.step()        
        paths = tr.get_paths()
        
        self.assertEqual(len(paths), 4)
        self.assertEqual(''.join(paths[0]), '----*****')
        self.assertEqual(''.join(paths[1]), '--***')
        self.assertEqual(''.join(paths[2]), '------******')        
        self.assertEqual(''.join(paths[3]), '----***')
        
        tr.step()
        paths = tr.get_paths()
        
        self.assertEqual(len(paths), 4)        
        self.assertEqual(''.join(paths[0]), '------*****')
        self.assertEqual(''.join(paths[1]), '---***')
        self.assertEqual(''.join(paths[2]), '---------******')        
        self.assertEqual(''.join(paths[3]), '------***')


# EXTRA: NOT REQUIRED TO PASS DURING THE EXAM
class VelocityGreaterThanTrainSizeTest (unittest.TestCase):        
        
    def test_01_1_2(self):
        
        tr = TrainRace([1],[2])
        paths = tr.get_paths()
        
        self.assertEqual(''.join(paths[0]), '*')
        
        tr.step()
        paths = tr.get_paths()
        
        self.assertEqual(''.join(paths[0]), '--*')        
        
        tr.step()
        paths = tr.get_paths()
        
        self.assertEqual(''.join(paths[0]), '----*')


    def test_02_2_4(self):        
        
        tr = TrainRace([2],[4])
        paths = tr.get_paths()
        
        self.assertEqual(''.join(paths[0]), '**')        
        
        tr.step()
        paths = tr.get_paths()
        
        self.assertEqual(''.join(paths[0]), '----**')
        
        tr.step()        
        paths = tr.get_paths()
        
        self.assertEqual(''.join(paths[0]), '--------**')


    def test_03_1_2_3_4(self):
        
        tr = TrainRace([1,2],[3,4])
        paths = tr.get_paths()
        
        self.assertEqual(len(paths), 2)
        self.assertEqual(''.join(paths[0]), '*')
        self.assertEqual(''.join(paths[1]), '**')
        
        tr.step()        
        paths = tr.get_paths()
        
        self.assertEqual(len(paths), 2)        
        self.assertEqual(''.join(paths[0]), '---*')        
        self.assertEqual(''.join(paths[1]), '----**')
        
        tr.step()        
        paths = tr.get_paths()
        
        self.assertEqual(len(paths), 2)        
        self.assertEqual(''.join(paths[0]), '------*')        
        self.assertEqual(''.join(paths[1]), '--------**')

        tr.step()        
        paths = tr.get_paths()
        
        self.assertEqual(len(paths), 2)        
        self.assertEqual(''.join(paths[0]), '---------*')        
        self.assertEqual(''.join(paths[1]), '------------**')
        
