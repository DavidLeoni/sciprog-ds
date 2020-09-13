import unittest
from chains_sol import *


class TestHasDuplicates(unittest.TestCase):

    def test_01_empty(self):
        self.assertEqual(has_duplicates([]),
                         False)

    def test_02_one_empty(self):
        self.assertEqual(has_duplicates([[]]),
                         False)

    def test_03_a(self):
        self.assertEqual(has_duplicates([['a']]),
                         False)

    def test_04_ab_c(self):
        self.assertEqual(has_duplicates([['ab','c']]),
                         False)

    def test_05_ab_c_ab(self):
        self.assertEqual(has_duplicates([['ab','c','ab']]),
                         True)

    def test_05_g_h__a_b_c(self):
        self.assertEqual(has_duplicates([
                                          ['g','h'],
                                          ['a','b','c']                                          
                                        ]),
                         False)

    def test_06_g_h__a_g_c(self):
        self.assertEqual(has_duplicates([
                                          ['g','h'],
                                          ['a','g','c']                                          
                                        ]),
                         True)

    def test_07_g_h__hhh__a_b_c(self):
        self.assertEqual(has_duplicates([
                                          ['g','h'],
                                          ['hhh'],
                                          ['a','b','c'],                                                                                    
                                        ]),
                         False)

    def test_08_g_h__h__a_g_c(self):
        self.assertEqual(has_duplicates([
                                          ['g','h'],
                                          ['h'],
                                          ['a','g','c'],                                                                                    
                                        ]),
                         True)

class TestChain(unittest.TestCase):

    def test_01_ab(self):
        self.assertEqual(chain( [
                                    ['a', 'b']
                                ]),
                                ['a', 'b'])

    def test_02_ab_c(self):
        self.assertEqual(chain( [
                                    ['ab', 'c']
                                ]),
                                ['ab', 'c'])


    def test_03_ab_c_de(self):
        self.assertEqual(chain( [
                                    ['ab', 'c', 'de']
                                ]),
                                ['ab', 'c', 'de'])

    def test_04_b_a__a_c(self):
        self.assertEqual(chain( [
                                    ['b', 'a'],
                                    ['a', 'c']
                                ]),
                                ['b', 'a', 'c'])
    
    def test_05_not_chainable(self):
        with self.assertRaises(ValueError):
            chain([
                    ['a','b'],
                    ['b','c'],
                    ['g','h']
                  ])

    def test_06_a_b_c__c_d(self):
        self.assertEqual(chain( [
                                    ['a', 'b','c'],
                                    ['c', 'd']
                                ]),
                                ['a', 'b', 'c', 'd'])

    def test_07_a_b_c__d_e_f__c_d(self):
        self.assertEqual(chain( [
                                    ['a', 'b','c'],                              
                                    ['d','e','f'],
                                    ['c', 'd'],
                                ]),
                                ['a', 'b', 'c','d','e','f'])


    def test_08_complex(self):
        self.assertEqual(chain( [
                                    ['ab', 'c', 'de'],
                                    ['gh', 'i'],
                                    ['de', 'f', 'gh']
                                    ]), 
                                    ['ab', 'c', 'de', 'f', 'gh', 'i'])