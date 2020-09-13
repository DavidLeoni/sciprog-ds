

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
        #jupman-raise
        new_child._sibling = self._child
        new_child._parent = self
        self._child = new_child
        #/jupman-raise

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
        #jupman-raise
        for c in reversed(new_children):
            self.insert_child(c)        
        #/jupman-raise

    def insert_sibling(self, new_sibling):
        """ Inserts new_sibling as the *immediate* next sibling.
            
            If self is a root, raises an Exception.           
        """
        #jupman-raise
        if (self.is_root()):
            raise Exception("Can't add siblings to a root node !!")
            
        new_sibling._parent = self._parent
        new_sibling._sibling = self._sibling
        self._sibling = new_sibling
        #/jupman-raise

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
        #jupman-raise
        if (self.is_root()):
            raise Exception("Can't add siblings to a root node !!")
        
        for s in reversed(new_siblings):
            self.insert_sibling(s)
        #/jupman-raise

    def detach_child(self):
        """ Detaches the first child. 
        
            if there is no child, raises an Exception 
        """
        #jupman-raise
        if (self._child == None):
            raise Exception("There is no child !")            
        else:
                        
            detached = self._child
            self._child = self._child._sibling 
            detached._parent = None
            detached._sibling = None
        #/jupman-raise
            
    def detach_sibling(self):
        """ Detaches the first sibling.
        
            If there is no sibling, raises an Exception 
        """
        #jupman-raise
        if (self._sibling == None):
            raise Exception("There is no sibling !")
        else:
            detached = self._sibling            
            self._sibling = self._sibling._sibling             
            detached._parent = None
            detached._sibling = None
        #/jupman-raise

    def detach(self, data):
        """ Detaches the first child that holds the provided data.
        
            If no such node is found, raises an Exception
        """
        #jupman-raise
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
        #/jupman-raise

    def ancestors(self):
        """ Return the ancestors up until the root as a Python list.             
            First item in the list will be the parent of this node.
            
            NOTE: this function return the *nodes*, not the data.
        """
        #jupman-raise
        ret = []
        current = self._parent
        while current != None:
            ret.append(current)
            current = current._parent
        return ret
        #/jupman-raise

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
        #jupman-raise
        ret = []        
        
        c = self._child
        
        while c != None:
            gc = c._child
            while gc != None:
                ret.append(gc._data)
                gc = gc._sibling
            c = c._sibling
        
        return ret
        #/jupman-raise

    def zig(self):
        """ RETURN as output a list of data of the root and all the nodes in the chain of child attributes.
            Basically, you just have to follow the red lines and gather data in a list, 
            until there are no more red lines to follow. 

            See site for more info
        
        """
        #jupman-raise        
        ret = [self._data]    
        current = self        

        while current._child != None:
            ret.append(current._child._data)
            current = current._child

        return ret
        #/jupman-raise

    def zag(self):
        """ This function is quite similar to zig, but this time it RETURN the data it gathers going right,
            along the sibling arrows. 
        
            See site for more info
        """
        #jupman-raise
        ret = [self._data]                
        current = self
            
        while current._sibling != None:
            ret.append(current._sibling._data)            
            current = current._sibling    

        return ret
        #/jupman-raise

    def zigzag(self):
        """
            First zigs collecting data along the child vertical red chain as much as it can. Then, if the last node links to at least a sibling, the method continues to collect data along the siblings horizontal chain as much as it can. At this point, if it finds a child, it goes zigging again along the child vertical red chain as much as it can, and then horizontal zaging, and so on. It continues zig-zaging like this until it reaches a node that has no child nor sibling: when this happens returns the list of data found so far.

            See site for more info.
        """
        #jupman-raise        
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
        #/jupman-raise

    def uncles(self):
        """ RETURN a python list containing the data of all the uncles of this
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
        """ RETURN the first common ancestor of current node and the provided gt2 node
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
        
        cs = []
        current = self._child
        while current != None:
            cs.append(current)
            current = current.sibling()
        
        
        self._child = None
    
        for c in cs:
            self.insert_child(c)
        
        for c in cs:
            c.mirror()

            
    def clone(self):
        """ Clones this tree, by RETURNING an *entirely* new tree which is an 
            exact copy of this tree (so returned node and *all* its descendants must be new). 
            
            - MUST run in O(n) where n is the number of nodes
            - a recursive method is acceptable.
        """
        ret = GenericTree(self._data)
        
        cs = []
        current = self._child
        while current != None:
            cs.append(current)
            current = current.sibling()
        
        for c in reversed(cs):
            ret.insert_child(c.clone())
        
        return ret
            
    def rightmost(self):
        """ RETURN a list containing the *data* of the nodes 
            in the *rightmost* branch of the tree. 

            Example: 

            a
            ├b
            ├c
            |└e
            └d
             ├f
             └g
              ├h
              └i

            should give

            ['a','d','g','i']
        """
        #jupman-raise
        ret = []        
        last = self
        while last != None:
            ret.append(last.data())
            current = last._child
            last = None
            while current != None:
                last = current
                current = current.sibling()
        return ret              
        #/jupman-raise             

    def fill_left(self, stuff):
        """ MODIFIES the tree by filling the leftmost branch data
            with values from provided array 'stuff'
            
            - if there aren't enough nodes to fill, raise ValueError
            - root data is not modified
            - *DO NOT* use recursion

        """
        #jupman-raise
        lev = 0
        current = self._child
        while lev < len(stuff):
            if current == None:
                raise ValueError("Not enough nodes !")
            current._data = stuff[lev]
            current = current._child
            lev += 1
        #/jupman-raise
        
    def follow(self, positions):
        """
            RETURN an array of node data, representing a branch from the
            root down to a certain depth.
            The path to follow is determined by given positions, which
            is an array of integer indeces, see example.

            - if provided indeces lead to non-existing nodes, raise ValueError
            - IMPORTANT: *DO NOT* use recursion, use a couple of while instead.
            - IMPORTANT: *DO NOT* attempt to convert siblings to 
                         a python list !!!! Doing so will give you less points!

        """
        #jupman-raise
        ret = [self._data]
        current = self._child
        lev = 0
        
        while lev < len(positions):
            if current == None:
                raise ValueError("Can't find the position !")
            
            i = 0
            while i < positions[lev]:
                if current == None:
                    raise ValueError("Can't find the position !")
                current = current._sibling
                i += 1
            if current == None:
                raise ValueError("Can't find position !")
            ret.append(current._data)
            current = current._child
            lev += 1

        return ret
           
        #/jupman-raise    
        
    def is_triangle(self, elems):
        """ RETURN True if this node is a triangle matching the data  
            given by list elems. 
            
            In order to match:
            - first list item must be equal to this node data
            - second list item must be equal to this node first child data
            - third list item must be equal to this node second child data

            - if elems has less than three elements, raises ValueError
        """
        #jupman-raise
        if len(elems) != 3:
            raise ValueError("Must receive exactly 3 elements, got %s instead" % elems)
        
        if self._data != elems[0]:
            return False
        if self._child == None:
            return False
        if self._child._data != elems[1]:
            return False
        if self._child._sibling == None:
            return False
        if self._child._sibling._data != elems[2]:
            return False
        return self._child._sibling._sibling == None
        #/jupman-raise

    def has_triangle(self, elems):
        """ RETURN True is this node *or one of its descendants* is a triangle
            matching given elems. Otherwise, return False.

            - a recursive solution is acceptable
        """
        #jupman-raise
        if self.is_triangle(elems):
            return True
        else:
            current = self._child
            while current != None:
                if current.has_triangle(elems):
                    return True
                current = current._sibling
        return False
        #/jupman-raise        