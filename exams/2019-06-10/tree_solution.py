

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
