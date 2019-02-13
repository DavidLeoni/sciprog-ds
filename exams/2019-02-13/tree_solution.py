

class GenericTree:
   
    """ A stripped down version of the GenericTree seen in class
        
        A tree in which each node can have any number of children. 
    
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
        new_child._sibling = self._child
        new_child._parent = self
        self._child = new_child

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