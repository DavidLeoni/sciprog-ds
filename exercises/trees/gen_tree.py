
class GenericTree:
    """ A tree in which each node can have any number of children. 
    
        Each node is linked to its parent and to its immediate sibling on the right
    """
    
    def __init__(self, data):
        self._data = data
        self._child = None
        self._sibling = None
        self._parent = None        

    def data(self):
        return self._data    
    
    def child(self):
        return self._child    
    
    def sibling(self):
        return self._sibling
    
    def parent(self):
        return self._parent
        
    def is_root(self):
        """ Return True if the node is a root of a tree, False otherwise
        
            A node is a root whenever it has no parent nor siblings.
        """
        return self._parent == None and self._sibling == None
    
    def is_subtree(self):
        """ Returns True if the node is a subtree of another tree
        
            A subtree always has a parent 
        """
        return self._parent != None
        
        
    def children(self):
        """ Returns the children as a Python list

            NOTE 1: this method return the *nodes*, not the data.  
            NOTE 2: This method is O(n) where n is the number of children, 
                    DO NOT abuse it for i.e. only getting easily first or second child !
        """
        
        ret = []
        current = self._child
        while current != None:
            ret.append(current)
            current = current._sibling
        return ret    
        
    def __str__(self):
        """ Returns a pretty string of the tree """
        
        def str_branches(node, branches):
            """ Returns a string with the tree pretty printed. 

                branches: a list of characters representing the parent branches. Characters can be either ` ` or '│'            
            """
            strings = [str(node._data)]
            current = node._child
            while (current != None):
                if current._sibling == None:            
                    joint = '└'  
                else:
                    joint = '├'


                strings.append('\n')
                for b in branches:
                     strings.append(b)
                strings.append(joint)
                if current._sibling == None:            
                    branches.append(' ')
                else:
                    branches.append('│')                        
                strings.append(str_branches(current, branches))
                branches.pop()
                current = current._sibling

            return "".join(strings)
        
        return str_branches(self, [])
                
    def has_child(self):
        """ Returns True if this node has a child, False otherwise """
        return self._child != None

    def insert_child(self, new_child):        
        """ Inserts new_child at the beginning of the children sequence. """    
        raise Exception("TODO Implement me !" )
        
    def insert_children(self, new_children):        
        """ Takes a list of children and inserts them at the beginning of the current children sequence,
            
            NOTE: in the new sequence new_children appear in the order they are passed to the function!
            
        
            For example:
                >>> t = gt('a', gt('b'), gt('c))
                >>> print t                                
                a
                ├b
                └c

                >>>  t.insert_children([gt('d'), gt('e')])
                >>> print t
                a
                ├d
                ├e
                ├b
                └c
        """
        raise Exception("TODO Implement me !" )
        
    def insert_sibling(self, new_sibling):
        """ Inserts new_sibling as the *immediate* next sibling.
            
            If self is a root, raises an Exception             
        """
        raise Exception("TODO Implement me !" )

    def insert_siblings(self, new_siblings):
        """ Inserts new_siblings at the beginning of the siblings sequence, 
            in the same order as they are passed. 
            
            For example:
            
                >>> bt =  gt('b')
                >>> t = gt('a', bt , gt('c))
                >>> print t
                a
                ├b
                └c

                >>>  bt.insert_children([gt('d'), gt('e')])
                >>> print t
                a
                ├b
                ├d
                ├e
                └c
        """
        raise Exception("TODO Implement me !" )
        
    
    def detach_child(self):
        """ Detaches the first child.
        
            if there is no child, raises an Exception 
        """
        raise Exception("TODO Implement me !" )
            
            
    def detach_sibling(self):
        """ Detaches the first sibling.
        
            If there is no sibling, raises an Exception 
        """
        
        raise Exception("TODO Implement me !" )
            
    def detach(self, data):
        """ Detaches the first child that holds the provided data.
        
            If no such node is found, raises an Exception
        """

        raise Exception("TODO Implement me !" )
        
    def ancestors(self):
        """ Return the ancestors up until the root as a Python list.             
            First item in the list will be the parent of this node.
            
            NOTE: this function return the *nodes*, not the data.
        """
        raise Exception("TODO Implement me !" )
        
    def grandchildren(self):
        """ Returns a python list containing the data of all the grandchildren of this
            node.
            
            - Data must be from left to right order in the tree horizontal representation 
              (or up to down in the vertical representation). 
            - If there are no grandchildren, returns an empty array.
            
            For example, for this tree:
            
            a
            ├b
            │├c
            │└d
            │ └g
            ├e
            └f
             └h  
            
            Returns ['c','d','h']
        """        
        raise Exception("TODO Implement me !" )

        
    def zig(self):
        raise Exception("TODO Implement me !" )

    def zag(self):
        raise Exception("TODO Implement me !" )

    def zigzag(self):
        raise Exception("TODO Implement me !" )

    def uncles(self):
        """ Returns a python list containing the data of all the uncles of this
            node (that is, *all* the siblings of its parent).
            
            NOTE: returns also the father siblings which are *BEFORE* the father !! 
            
            - Data must be from left to right order in the tree horizontal representation 
              (or up to down in the vertical representation). 
            - If there are no uncles, returns an empty array.
            
            For example, for this tree:
            
            a
            ├b
            │├c
            │└d
            │ └g
            ├e
            │└h  
            └f

            
            calling this method on 'h' returns ['b','f']
        """        
        raise Exception("TODO Implement me !" )

    def common_ancestor(self, gt2):
        """ Return the first common ancestor of current node and the provided gt2 node
            If gt2 is not a node of the same tree, raises LookupError

            NOTE: this function returns a *node*, not the data.
 
            Ideally, this method should perform in O(h) where h is the height of the tree.
            (Hint: you should use a Python Set). If you can't figure out how to make it 
            that fast, try to make it at worst O(h^2)
                        
        """          
        raise Exception("TODO Implement me !" )

    def mirror(self):
        """ Modifies this tree by mirroring it, that is, reverses the order
            of all children of this node and of all its descendants
            
            - MUST work in O(n) where n is the number of nodes
            - MUST change the order of nodes, NOT the data (so don't touch the data !)
            - DON'T create new nodes            
            - It is acceptable to use a recursive method.
                    
            
            Example:
            
            a     <-    Becomes:    a
            ├b                      ├i
            │├c                     ├e
            │└d                     │├h
            ├e                      │├g
            │├f                     │└f 
            │├g                     └b
            │└h                      ├d
            └i                       └c
            
              
        """
        raise Exception("TODO Implement me !" )

    def clone(self):
        """ Clones this tree, by returning an *entirely* new tree which is an 
            exact copy of this tree (so returned node and *all* its descendants must be new). 
            
            - MUST run in O(n) where n is the number of nodes
            - a recursive method is acceptable.
        """
        raise Exception("TODO Implement me !" )
        
