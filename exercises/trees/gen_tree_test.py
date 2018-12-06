from tree import *
from algolab import gt
from algolab import GenericTreeTest
import unittest

                            
class InsertChildTest(GenericTreeTest):

    def test_insert_child(self):        
        ta = GenericTree('a')
        self.assertEqual(ta.child(), None)
        tb = GenericTree('b')        
        ret = ta.insert_child(tb) 
        self.assertEqual(ret, None, self.assertReturnNone(ret, "insert_child"))
        self.assertEqual(ta.child(), tb)
        self.assertEqual(tb.parent(), ta)        
        self.assertEqual(tb.sibling(), None)
        self.assertEqual(tb.child(), None)
        
        tc = GenericTree('c')
        ta.insert_child(tc)
        self.assertEqual(ta.child(), tc)
        self.assertEqual(tc.sibling(), tb)
        self.assertEqual(tc.parent(), ta)
        self.assertEqual(tb.sibling(), None)

class InsertChildrenTest(GenericTreeTest):
        
    def test_insert_children(self):
        
        t = gt('a')
        t.insert_children([gt('d'), gt('e')])        
        self.assertTreeEqual(t, gt('a', gt('d'), gt('e')))
        t.insert_children([gt('b'), gt('c')])
        self.assertTreeEqual(t, gt('a', gt('b'), gt('c'), gt('d'), gt('e')))        

class InsertSiblingTest(GenericTreeTest):
        
    def test_insert_right_sibling(self):
        ta = gt('a')                        
        tb = gt('b')        
        ta.insert_child(tb)        

        tb.insert_sibling(gt('c'))        
        self.assertTreeEqual(ta, gt('a', gt('b'), gt('c')))

    def test_insert_middle_sibling(self):
        
        tb = gt('b')
        ta = gt('a', tb, gt('d'))        

        tb.insert_sibling(gt('c'))        
        self.assertTreeEqual(ta, gt('a', gt('b'), gt('c') , gt('d')))
                
    def test_insert_sibling_to_root(self):
        ta = gt('a')
        
        with self.assertRaises(Exception):
            ta.insert_sibling(gt('b'))
    
class InsertSiblingsTest(GenericTreeTest):
    
    def test_insert_siblings(self):
        tb = gt('b')
        ta = gt('a', tb, gt('e'))        

        tb.insert_siblings([gt('c'), gt('d')])        
        self.assertTreeEqual(ta, gt('a', gt('b'), gt('c') , gt('d'), gt('e')))

    def test_insert_siblings_to_root(self):
        ta = gt('a')
        
        with self.assertRaises(Exception):
            ta.insert_siblings([gt('b'), gt('c')])          

        
        
class DetachChildTest(GenericTreeTest):
            
    def test_detach_child(self):
        
        tb = gt('b')
        tc = gt('c')
        
        t = gt('a', tb, tc)
        
        ret = t.detach_child()                
        self.assertReturnNone(ret, "detach_child") 
        
        self.assertTreeEqual(t, gt('a', gt('c')))
        self.assertTreeEqual(tb, gt('b'))  

        ret = t.detach_child()         
        self.assertTreeEqual(t, gt('a'))
        self.assertTreeEqual(tb, gt('b'))  
        self.assertTreeEqual(tc, gt('c'))
        
        
        with self.assertRaises(Exception):
            ret = t.detach_child()

        
class DetachSiblingTest(GenericTreeTest):
        
    def test_detach_sibling_root(self):
        ta = gt('a')

        with self.assertRaises(Exception):        
            ta.detach_sibling()                        

    def test_detach_sibling_child(self):
        
        tb = gt('b')
        ta = gt('a', tb)

        with self.assertRaises(Exception):        
            tb.detach_sibling()
            
    def test_detach_sibling_three(self):
        tb = gt('b')
        tc = gt('c')
        ta = gt('a', tb, tc)
        
        tb.detach_sibling()                        
        self.assertTreeEqual(ta, gt('a', gt('b')))
        self.assertTreeEqual(tc, gt('c'))

    def test_detach_sibling_four(self):
        tb = gt('b')
        tc = gt('c')
        td = gt('d')
        ta = gt('a', tb, tc, td)
        
        tb.detach_sibling()                        
        self.assertTreeEqual(ta, gt('a', gt('b'), gt('d')))
        self.assertTreeEqual(tc, gt('c'))
        
        tb.detach_sibling() 
        self.assertTreeEqual(ta, gt('a', gt('b')))
        self.assertTreeEqual(tc, gt('c'))
        self.assertTreeEqual(td, gt('d'))        
                    
            
class DetachTest(GenericTreeTest):        
    
    def test_detach_one_node(self):
        t = gt('a')    
        
        with self.assertRaises(Exception):
            t.detach('a')
            
        self.assertTreeEqual(t, gt('a'))

    def test_detach_two_nodes(self):
        tb = gt('b')
        ta = gt('a', tb)
        ta.detach('b')
        self.assertTreeEqual(tb, gt('b')) 
        self.assertTreeEqual(ta, gt('a'))

    def test_detach_three_nodes_child(self):
        tb = gt('b')
        tc = gt('c')
        ta = gt('a', tb, tc)
        ta.detach('b')
        self.assertTreeEqual(tb, gt('b'))         
        self.assertTreeEqual(ta, gt('a', gt('c')))


    def test_detach_three_nodes_second(self):
        tb = gt('b')
        tc = gt('c')
        ta = gt('a', tb, tc)
        ta.detach('c')
        self.assertTreeEqual(tc, gt('c'))         
        self.assertTreeEqual(ta, gt('a', gt('b')))
        
    def test_detach_three_nodes_duplicates(self):
        tb1 = gt('b')
        tb2 = gt('b')
        ta = gt('a', tb1, tb2)
        ta.detach('b')
        self.assertTreeEqual(tb1, gt('b'))
        self.assertTreeEqual(ta, gt('a', tb2))     
        

class AncestorsTest(GenericTreeTest):

    def test_root(self):        
        ta = gt('a')
        self.assertEqual(ta.ancestors(), [])

    """
        a
        └b  <-
    """                
    def test_two(self):        

        tb = gt('b')        
        ta = gt('a', tb)
        self.assertEqual(tb.ancestors(), [ta])

    """
        a
        |-b
        └c  <-
    """        
    def test_brothers(self):        

        tb = gt('b')       
        tc = gt('c')
        ta = gt('a', tb, tc)
        self.assertEqual(tb.ancestors(), [ta])

    """
        a
        |-b
        | |-d
        | └e
        └c
         └f
    """   
    def test_level2(self):        

        te = gt('e')
        td = gt('d')
        tf = gt('f')
        tb = gt('b', td, te)        
        tc = gt('c', tf)
        ta = gt('a', tb, tc)            

        self.assertEqual(tc.ancestors(), [ta])
        self.assertEqual(tf.ancestors(), [tc, ta])
        self.assertEqual(te.ancestors(), [tb, ta])

class GrandChildrenTest(GenericTreeTest):
            
    def test_grandchildren_root(self):
        self.assertEquals(gt('a').grandchildren(), [])

    """
        a
        \-b
    """            
    def test_grandchildren_one_child_no_children(self):
        self.assertEquals(gt('a',  gt('b')).grandchildren(), [])        

    """
        a
        \-b
          \-c
    """            
    def test_grandchildren_one_child_one_grandchildren(self):
        self.assertEquals(gt('a',  gt('b', gt('c'))).grandchildren(), ['c'])        

    """
        a
        \-b
          |-c
          \-d
    """            
    def test_grandchildren_one_child_two_grandchildren(self):
        self.assertEquals(gt('a',  gt('b', gt('c'), gt('d'))).grandchildren(), ['c', 'd'])        

    """
        a
        |-b
        | \-c
        \-d
          \-e
    """            
    def test_grandchildren_two_children_two_grandchildren(self):
        self.assertEquals(gt('a',  gt('b', gt('c')), gt('d', gt('e'))).grandchildren(), ['c', 'e'])        

    """
            a
            |-b
            | |-c
            | \-d
            |   \-g
            |-e
            | \-h  
            \-f    
    """
    def test_grandchildren_complex_grandgrandchildren(self):
        self.assertEquals(gt('a',  gt('b', gt('c'), gt('d', gt('g'))), 
                                   gt('e', gt('h')),
                                   gt('f')).grandchildren(), ['c', 'd', 'h'])
        
        
class ZigTest(GenericTreeTest):
    
    def test_zig_last_root(self):        
        self.assertEqual(gt('a').zig(), ['a'])

    
    def test_zig_last__one_child(self):
        """ 
            a
            \-b <-
        """
        self.assertEqual(gt('a', gt('b')).zig(), ['a', 'b'])

    def test_zig_last_two_children(self):
        """ 
            a
            |-b 
            \-c 
        """    
        self.assertEqual(gt('a', gt('b'), gt('c')).zig(), ['a', 'b'])
        
    def test_zig_depth_three(self):
        """ 
            a
            |-b
            | |-c
            | \-d
            \-e 
        """    
        self.assertEqual(gt('a', gt('b', gt('c'), gt('d')), gt('e')).zig(), ['a','b', 'c'])        

class ZagTest(GenericTreeTest):        
    
    def test_zag_root(self):        
        self.assertEqual(gt('a').zag(), ['a'])


    def test_zag_one_child(self):
        """ 
            a    
            \-b 
        """
        self.assertEqual(gt('a', gt('b')).zag(), ['a'])
        self.assertEqual(gt('a', gt('b')).child().zag(), ['b'])

    def test_zag_two_children(self):
        """ 
            a
            |-b 
            \-c 
        """    
        self.assertEqual(gt('a', gt('b'), gt('c')).child().zag(),
                         ['b', 'c'])
        
    def test_zag_depth_three(self):
        """ 
            a
            |-b   <-- start from
            | |-c
            | \-d
            \-e   
        """    
        t = gt('a', gt('b', gt('c'), gt('d')), gt('e'))
            
        self.assertEqual(t.child().zag(),
                         ['b','e'])        

class ZigZagTest(GenericTreeTest):
    
    def test_zigzag_root(self):        
        self.assertEqual(gt('a').zigzag(),
                         ['a'])

    
    def test_zigzag_one_child(self):
        """ 
            a
            \-b 
            
        """
        self.assertEqual(gt('a', gt('b')).zigzag(),
                         ['a','b'])

    def test_zigzag_two_children(self):
        """ 
            a
            |-b 
            \-c 
        """    
        self.assertEqual(gt('a', gt('b'), gt('c')).zigzag(),
                         ['a', 'b', 'c'])

    def test_zigzag_middle_child(self):
        """ 
            a
            |-b  
            |-c
            | \-e
            \-d 
            
            Notice the siblings chain must arrive to the end up to 'd' !
        """    
        self.assertEqual(gt('a', gt('b', gt('d')), gt('c')).zigzag(),
                         ['a', 'b', 'd'])

        
    def test_zigzag_complex(self):
        """ 
            a
            |-b
            |-c
            | |-e
            \-d
              |-f
              \-g
            
        """    
        self.assertEqual( gt('a', gt('b'), gt('c', gt('e')), gt('d', gt('f'), gt('g'))).zigzag(),
                         ['a','b','c', 'd','f', 'g'])


      
        
class UnclesTest(GenericTreeTest):

    """
        a
        \-b    <- 
          \-c          
    """            
    def test_uncles_unique_single_child(self):
        
        tb = gt('b')
        ta = gt('a',  tb, gt('c') )
        
        self.assertEquals(tb.uncles(), [])        


    """
        a
        \-b
          \-c <-         
    """            
    def test_uncles_unique_single_grandchild(self):
        
        tc = gt('c')
        ta = gt('a',  gt('b'), tc)
        
        self.assertEquals(tc.uncles(), [])        

    """
        a
        |-b
          \-c <-         
        \-d  
    """            
    def test_uncles_one_uncle_after(self):
        
        tc = gt('c')
        ta = gt('a',  gt('b', tc), gt('d'))
        
        self.assertEquals(tc.uncles(), ['d'])        



    """
        a
        |-b
        \-c
          \-d <-         
          
    """            
    def test_uncles_one_uncle_before(self):
        
        td = gt('d')
        ta = gt('a',  gt('b'), gt('c', td))
        
        self.assertEquals(td.uncles(), ['b'])


    """
        a
        |-b
        |-c
        | \-d <-
        \-e
          
    """            
    def test_uncles_middle(self):
        
        td = gt('d')
        ta = gt('a',  gt('b'), gt('c', td), gt('e'))
        
        self.assertEquals(td.uncles(), ['b', 'e'])
        
    """
            a
            |-b
            | |-c
            | \-d
            |   \-g
            |-e
            | \-h  <- 
            \-f    
    """
    def test_uncles_complex_1(self):
        
        th = gt('h')
        ta = gt('a',  gt('b', gt('c'), gt('d', gt('g'))), 
                      gt('e', th),
                      gt('f'))
        self.assertEquals(th.uncles(), ['b', 'f'])

    """
            a
            |-b
            | |-c
            | \-d
            |   \-g <-            
            |-e
            | \-h   
            \-f    
    """
    def test_uncles_complex_2(self):
        
        tg = gt('g')
        ta = gt('a',  gt('b', gt('c'), gt('d', tg)), 
                      gt('e', gt('h')),
                      gt('f'))
        self.assertEquals(tg.uncles(), ['c'])

        
class CommonAncestorTest(GenericTreeTest):
    
    def test_itself(self):
        tb = gt('b')
        ta = gt('a', tb)
        self.assertEqual(tb.common_ancestor(tb), ta)       
        
    def test_forest(self):
        tb = gt('b')
        ta = gt('a')
        with self.assertRaises(LookupError):
            ta.common_ancestor(tb)               
        
    def test_immediate(self):
        tb = gt('b')
        tc = gt('b')        
        ta = gt('a', tb, tc)
        self.assertTreeEqual(tb.common_ancestor(tc), ta)       
        
    def test_brothers(self):
        tb = gt('b')
        tc = gt('c')     
        ta = gt('a', tb, tc)
        self.assertTreeEqual(tb.common_ancestor(tc), ta)       
        
    """
        a
        |-b
        | |-d
        | \-e
        \-c
          \-f
    """   
    def test_level_2(self):
        
        te = gt('e')
        td = gt('d')
        tf = gt('f')
        tb = gt('b', td, te)        
        tc = gt('c', tf)
        ta = gt('a', tb, tc)
        self.assertTreeEqual(td.common_ancestor(te), tb)
        self.assertTreeEqual(tf.common_ancestor(tf), tc)
        self.assertTreeEqual(td.common_ancestor(tf), ta)
        self.assertTreeEqual(te.common_ancestor(tb), ta)
        

    """
        a
        \-b
          |-c
          |  |-d
          |  \-e
          \-f
        
    """   
    def test_level_3(self):
        
        te = gt('e')
        td = gt('d')
        tf = gt('f')
        tc = gt('c', td, te)
        tb = gt('b', tc, tf)
        ta = gt('a', tb)
        self.assertTreeEqual(tf.common_ancestor(tc), tb)
        self.assertTreeEqual(tf.common_ancestor(td), tb)
        self.assertTreeEqual(td.common_ancestor(te), tc)
            
class MirrorTest(GenericTreeTest):
    """
    a  <-   Becomes:   a
    """
    def test_root(self):
        t = gt('a')
        t.mirror()
        self.assertTreeEqual(t, gt('a'))

    """
    a   <-   Becomes  a
    \-b               \-b
    """       
    def test_ab(self):
        t = gt('a',gt('b'))
        t.mirror()
        self.assertTreeEqual(t, gt('a', gt('b')))
    

    """
    a   <-   Becomes:  a
    |-b                |-c
    \-c                \-b
    
    """    
    def test_abc(self):
        t = gt('a',gt('b'),gt('c'))
        t.mirror()
        self.assertTreeEqual(t, gt('a', gt('c'), gt('b')))


    """
    a   <-     Becomes:     a
    |-b                     |-f
    | |-c                   \-b
    | |-d                     |-e
    | \-e                     |-d
    \-f                       \-c 
                          
    """    
    def test_abcdef(self):
        t = gt('a',gt('b', gt('c'), gt('d'), gt('e')),gt('f'))
        t.mirror()
        self.assertTreeEqual(t, gt('a', gt('f'), gt('b', gt('e'), gt('d'), gt('c'))))
    
    
    """
    a                         a 
    |-b   <-     Becomes:     |-b
    | |-c                     | |-d
    | \-d                     | \-c
    \-e                       \-e
    """
    def test_non_root(self):
        tb = gt('b', gt('c'), gt('d'))        
        ta = gt('a',tb,gt('e'))
        tb.mirror()
        self.assertTreeEqual(ta, gt('a', gt('b', gt('d'), gt('c')),  gt('e')))
    
class CloneTest(GenericTreeTest):
    """
    a
    """
    def test_root(self):
        ta = gt('a')
        t2 = ta.clone()        

        self.assertTreeEqual(ta,t2)
        ta._data = 'b'  # if we change the original data, clone should be unaffected
        self.assertTreeEqual(t2, gt('a'))        
        ta.insert_child(gt('c')) # same if we insert an extra child 
        self.assertTreeEqual(t2, gt('a'))        
        

    """
    a
    \-b
    """
    def test_ab(self):
        tb= gt('b')
        ta = gt('a', tb)
        
        t2 = ta.clone()        

        self.assertTreeEqual(ta,t2)
        ta._data = 'x'  # if we change the original, clone should be unaffected
        tb._data = 'y'        
        self.assertTreeEqual(t2, gt('a',gt('b')))

    """
    a
    |-b
    |-c
      \-d
    """
    def test_abcd(self):
        td = gt('d')
        tc= gt('c', td)
        tb= gt('b')
        ta = gt('a', tb, tc)
        t2 = ta.clone()  
        
        self.assertTreeEqual(ta,t2)
        ta._data = 'x'  # if we change the original, clone should be unaffected
        tb._data = 'y' 
        tc._data = 'y'
        td._data = 'w'
        self.assertTreeEqual(t2, gt('a',gt('b'), gt('c', gt('d'))))

    