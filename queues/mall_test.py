
import unittest
from mall_sol import *

def to_list(ordered_dict):
    """
        Return a list of key-value pairs extracted from provided ordered dict
        which must contain either Shop or Client objects
    """
    ret = []
    
    for name in ordered_dict:
        
        shop_or_client = ordered_dict[name]
        if type(shop_or_client) is Shop :
            ret.append((name, shop_or_client._clients))
        elif type(shop_or_client) is Client:
            ret.append((name,shop_or_client._to_visit))        
        else:
            raise Exception("Unrecognized ordered dict: %s" % ordered_dict)
    return ret

class InitTest(unittest.TestCase):

    def test_01_empty(self):
        
        with self.assertRaises(ValueError):
            m = Mall([],[])
        
    def test_02_missing_client(self):

        with self.assertRaises(ValueError):

            m = Mall(
                    [   
                        'x',[]
                    ],
                    [
                        'a',['x']
                    ])


    def test_03_missing_shop(self):
        with self.assertRaises(ValueError):
            m = Mall(
                    [
                        'x',['a']
                    ],
                    [
                        'a',[]
                    ])

    def test_04_non_existing_shop(self):

        with self.assertRaises(ValueError):

            m = Mall(
                    [   
                        'x',['a']
                    ],
                    [
                        'a',['y']
                    ])

    def test_05_non_existing_client(self):

        with self.assertRaises(ValueError):

            m = Mall(
                    [   
                        'x',['a']
                    ],
                    [
                        'b',['x']
                    ])
        

class StrTest(unittest.TestCase):

    def test_01_str(self):

        m = Mall(
                [   
                    'x', ['a','b'], 
                    'y', ['c']                        
                ],
                [
                    'a',['x'],
                    'b',['x'],
                    'c',['x','y']
                ]
                )
        self.assertTrue('x' in str(m))
        self.assertTrue('y' in str(m))
        self.assertTrue("Shop" in str(m))
        self.assertTrue("Client" in str(m))
        self.assertTrue("Mall" in str(m))



class EnqueueTest(unittest.TestCase):

    def test_01_non_existing_shop(self):
        m = Mall(
                [
                    'x',[]
                ],
                [
                ])
        
        with self.assertRaises(ValueError):
           m.enqueue(Client('a',['y']))

    def test_02_missing_shop(self):
        m = Mall(
                [
                    'x',[]
                ],
                [
                ],
            )
        
        with self.assertRaises(ValueError):
           m.enqueue(Client('a',[]))

    def test_03_already_existing_client(self):
        m = Mall(
                [
                    'x',['a'],
                    'y',[]
                ],
                [
                    'a',['x']
                ],
            )
        
        with self.assertRaises(ValueError):
           m.enqueue(Client('a',['y']))

    def test_04_empty(self):
        m = Mall(
                [
                    'x',[]
                ],
                [
                ],
            )
        m.enqueue(Client('a',['x']))
        
        self.assertEqual(to_list(m.shops()),[                                        
                                                ('x',['a'])
                                            ])
        self.assertEqual(to_list(m.clients()),  [
                                                    ('a',['x'])
                                                ])


    def test_05_one_client(self):
        m = Mall(
                [
                    'x',['a']
                ],
                [
                    'a',['x']
                ],
            )
        m.enqueue(Client('b',['x']))
        self.assertEqual(to_list(m.shops()),[                            
                                                ('x',['a','b'])
                                            ])
        self.assertEqual(to_list(m.clients()),  [
                                                    ('a',['x']),
                                                    ('b',['x'])
                                                ])       


    def test_06_d_x_y(self):
        m = Mall(
                [
                    'x',['a','b'],
                    'y',['c']
                ],
                [
                    'a',['y','x'],
                    'b',['x'],
                    'c',['x','y']
                ],
            )

        m.enqueue(Client('d',['x','y']))

        self.assertEqual(to_list(m.shops()),[
                                                ('x',['a','b']),
                                                ('y',['c','d'])
                                            ])

        self.assertEqual(to_list(m.clients()),  [
                                                    ('a',['y','x']),
                                                    ('b',['x']),
                                                    ('c',['x','y']),
                                                    ('d',['x','y'])
                                                ])

class DequeueTest(unittest.TestCase):

    def test_01_empty(self):
        m = Mall(
                [
                    'x',[],
                    'y',[]
                ],
                [
                ],
            )
        self.assertEqual(m.dequeue(), [])

        self.assertEqual(to_list(m.shops()),[                                        
                                                ('x',[]),
                                                ('y',[])
                                            ])
        self.assertEqual(to_list(m.clients()), [])


    def test_02_one_client_one_shop(self):
        m = Mall(
                [
                    'x',['a']                    
                ],
                [
                    'a',['x']
                ],
            )
        self.assertEqual(m.dequeue(), ['a'])

        self.assertEqual(to_list(m.shops()),[                                        
                                                ('x',[])
                                            ])

        self.assertEqual(to_list(m.clients()),[])

    def test_03_one_client_two_shops(self):
        m = Mall(
                [
                    'x',['a'],
                    'y',[]                    
                ],
                [
                    'a',['y','x']
                ],
            )
        self.assertEqual(m.dequeue(), [])
        self.assertEqual(to_list(m.shops()),[                                        
                                                ('x',[]),
                                                ('y',['a'])
                                            ])
                                            
        self.assertEqual(to_list(m.clients()),  [                                        
                                                    ('a',['y'])
                                                ])

        self.assertEqual(m.dequeue(), ['a'])

        self.assertEqual(to_list(m.shops()),[
                                                ('x',[]),
                                                ('y',[])
                                            ])

        self.assertEqual(to_list(m.clients()), []) 

        self.assertEqual(m.dequeue(), [])

        self.assertEqual(to_list(m.shops()),[
                                                ('x',[]),
                                                ('y',[])
                                            ])

        self.assertEqual(to_list(m.clients()), []) 

    def test_04_two_clients_go_to_same_shop(self):
        m = Mall(
                [
                    'x',[],
                    'y',['b'],
                    'z',['a']
                ],
                [
                    'a',['x', 'z'],
                    'b',['x', 'y']                    
                ],
            )
        self.assertEqual(m.dequeue(), [])

        self.assertEqual(to_list(m.shops()),[                                        
                                                ('x',['b','a']),
                                                ('y',[]),
                                                ('z',[])
                                            ])

        self.assertEqual(to_list(m.clients()),  [
                                                    ('a',['x']),
                                                    ('b',['x'])
                                                ])
                                    

        self.assertEqual(m.dequeue(), ['b'])


        self.assertEqual(to_list(m.shops()),[
                                                ('x',['a']),
                                                ('y',[]),
                                                ('z',[])
                                            ])

        self.assertEqual(to_list(m.clients()),  [
                                                    ('a',['x'])
                                                ])

        self.assertEqual(m.dequeue(), ['a'])


        self.assertEqual(to_list(m.shops()),[
                                                ('x',[]),
                                                ('y',[]),
                                                ('z',[])
                                            ])
        self.assertEqual(to_list(m.clients()),[])


    def test_05_complex(self):

        m = Mall([
                    'x', ['a', 'b', 'c'],
                    'y', ['d'],
                    'z', ['f', 'g']
                ],
                [   
                    'a', ['y', 'x'],
                    'b', ['x'],
                    'c', ['x'],
                    'd', ['z','y'],
                    'f', ['y','x','z'],
                    'g', ['x','z']
                ])

        self.assertEqual(m.dequeue(), [])  # first call
        self.assertEqual(to_list(m.shops()),[                                        
                                                ('x', ['b','c','f']),
                                                ('y', ['a']),
                                                ('z', ['g', 'd'])
                                            ])
        self.assertEqual(to_list(m.clients()),  [
                                                    ('a', ['y']),
                                                    ('b', ['x']),
                                                    ('c', ['x']),
                                                    ('d', ['z']),
                                                    ('f', ['y','x']),
                                                    ('g', ['x','z'])
                                                ])
                                        

        self.assertEqual(m.dequeue(), ['b','a']) # second call
        self.assertEqual(to_list(m.shops()),[
                                                ('x', ['c','f','g']),
                                                ('y', []),
                                                ('z', ['d'])
                                            ])

        self.assertEqual(to_list(m.clients()),  [   
                                                    ('c', ['x']),
                                                    ('d', ['z']),
                                                    ('f', ['y','x']),
                                                    ('g', ['x'])
                                                ])

        self.assertEqual(m.dequeue(), ['c','d'])  # third call
        self.assertEqual(to_list(m.shops()),[
                                                ('x', ['f','g']),
                                                ('y', []),
                                                ('z', [])
                                            ])
        self.assertEqual(to_list(m.clients()),  [   
                                                    ('f', ['y','x']),
                                                    ('g', ['x'])
                                                ])
                                        


        self.assertEqual(m.dequeue(), [])  # fourth call
        self.assertEqual(to_list(m.shops()),[
                                                ('x', ['g']),
                                                ('y', ['f']),
                                                ('z', [])
                                            ])
        self.assertEqual(to_list(m.clients()),  [   
                                                    ('f', ['y']),
                                                    ('g', ['x'])
                                                ])


        self.assertEqual(m.dequeue(), ['g','f']) # fifth call
        self.assertEqual(to_list(m.shops()),[
                                                ('x', []),
                                                ('y', []),
                                                ('z', [])
                                            ])
                                            
        self.assertEqual(to_list(m.clients()),[])        
                                             