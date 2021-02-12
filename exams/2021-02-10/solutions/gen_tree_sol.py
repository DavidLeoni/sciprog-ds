

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
        
    def __repr__(self):
        return '%s(%s) with id=%s' % (self.__class__.__name__, repr(self._data), id(self))
                
    def __str__(self):
        """ Returns a pretty string of the tree """
        
        def str_branches(node, branches):
            """ Returns a string with the tree pretty printed. 

                branches: a list of characters representing the parent branches. Characters can be either ` ` or '│'            
            """
            strings = [str(node._data)]
            current = node._child
            i = 0
            while (current != None):
                
                if not isinstance(current, GenericTree):                    
                    strings.append('\n')
                    strings.append('└')
                    strings.append('ERROR: FOUND CHILD OF TYPE %s AT INDEX %s' % (type(current), i))
                    break
                    
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
                i += 1

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
        

    
    def marvelous(self):
        """ MODIFIES each node data replacing it with the concatenation 
            of its leaves data 
            
            - MUST USE a recursive solution
            - assume node data is always a string

        """
        #jupman-raise
        
        ret = []
        
        if self._child == None:
            return 
        
        current = self._child
            
        work = []
        while current != None:
            current.marvelous()
            work.extend(current._data)
            current = current._sibling
        
        self._data = ''.join(work)
        #/jupman-raise            
