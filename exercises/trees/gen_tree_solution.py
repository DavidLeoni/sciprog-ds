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
        
        new_child._sibling = self._child
        new_child._parent = self
        self._child = new_child
        

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
        for c in reversed(new_children):
            self.insert_child(c)        
        
    def insert_sibling(self, new_sibling):
        """ Inserts new_sibling as the *immediate* next sibling.
            
            If self is a root, raises an Exception.           
        """
        if (self.is_root()):
            raise Exception("Can't add siblings to a root node !!")
            
        new_sibling._parent = self._parent
        new_sibling._sibling = self._sibling
        self._sibling = new_sibling

    def insert_siblings(self, new_siblings):
        """ Inserts new_siblings at the beginning of the siblings sequence.
            
            Nodes are inserted in the same order as they are passed. 
            If self is a root, raises an Exception
            
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
        if (self.is_root()):
            raise Exception("Can't add siblings to a root node !!")
        
        for s in reversed(new_siblings):
            self.insert_sibling(s)
            
    def detach_child(self):
        """ Detaches the first child. 
        
            if there is no child, raises an Exception 
        """

        if (self._child == None):
            raise Exception("There is no child !")            
        else:
                        
            detached = self._child
            self._child = self._child._sibling 
            detached._parent = None
            detached._sibling = None
            
            
    def detach_sibling(self):
        """ Detaches the first sibling.
        
            If there is no sibling, raises an Exception 
        """
        
        if (self._sibling == None):
            raise Exception("There is no sibling !")
        else:
            detached = self._sibling            
            self._sibling = self._sibling._sibling             
            detached._parent = None
            detached._sibling = None
            
    def detach(self, data):
        """ Detaches the first child that holds the provided data.
        
            If no such node is found, raises an Exception
        """

        if (self._child != None):
            current = self._child
            prev = None
            while current != None:
                if (current._data == data):
                    if prev == None: # first element list
                        self.detach_child()
                    else:
                        prev._sibling = current._sibling
                        current._parent = None                        
                        current._sibling = None                        
                    return
                else:
                    prev = current
                    current = current._sibling                        
        raise Exception("Couldn't find any children holding this data:" + str(data))

    def ancestors(self):
        """ Return the ancestors up until the root as a Python list.             
            First item in the list will be the parent of this node.
            
            NOTE: this function return the *nodes*, not the data.
        """
        
        ret = []
        current = self._parent
        while current != None:
            ret.append(current)
            current = current._parent
        return ret
    
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
        ret = []        
        
        c = self._child
        
        while c != None:
            gc = c._child
            while gc != None:
                ret.append(gc._data)
                gc = gc._sibling
            c = c._sibling
        
        return ret

    def zig(self):
                
        ret = [self._data]    
        current = self        

        while current._child != None:
            ret.append(current._child._data)
            current = current._child

        return ret

    def zag(self):

        ret = [self._data]                
        current = self
            
        while current._sibling != None:
            ret.append(current._sibling._data)            
            current = current._sibling    

        return ret
        

    def zigzag(self):
                
        current = self
        
        ret = [self._data]
        
        while True:        
                    
            if current._child == None and current._sibling == None:                                
                return ret
            
            while current._child != None:
                ret.append(current._child._data)
                current = current._child

            while current._sibling != None:
                ret.append(current._sibling._data)
                current = current._sibling    
    
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
        
        ret = []        
        
        father = self._parent
        
        if father != None:
            grandfather = father._parent        
            if grandfather != None:
                current = grandfather._child  # leftmost child
                
                while current != None:
                    if current != father:
                        ret.append(current._data)                    
                    current = current._sibling
                    
        return ret


        
    def common_ancestor(self, gt2):
        """ Return the first common ancestor of current node and the provided gt2 node
            If gt2 is not a node of the same tree, raises LookupError

            NOTE: this function returns a *node*, not the data.
 
            Ideally, this method should perform in O(h) where h is the height of the tree.
            (Hint: you should use a Python Set). If you can't figure out how to make it 
            that fast, try to make it at worst O(h^2)
                        
        """          
        
        anc_gt2_set = set(gt2.ancestors())
        
        ancs = self.ancestors()
        
        for anc in ancs:
            if anc in anc_gt2_set:
                return anc
        
        raise LookupError("Couldn't find any common ancestor !")
              
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
        
        cs = self.children()     
        self._child = None
    
        
        for c in cs:
            self.insert_child(c)
        
        for c in cs:
            c.mirror()

            
    def clone(self):
        """ Clones this tree, by returning an *entirely* new tree which is an 
            exact copy of this tree (so returned node and *all* its descendants must be new). 
            
            - MUST run in O(n) where n is the number of nodes
            - a recursive method is acceptable.
        """
        ret = GenericTree(self._data)
        
        for c in reversed(self.children()):
            ret.insert_child(c.clone())
        
        return ret
            