import jupman
jupman.mem_limit()

class BinTree:
    """ A simple binary tree with left and right branches
    """
    
    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None

    def data(self):
        return self._data    
    
    def left(self):
        return self._left    
    
    def right(self):
        return self._right
                    
    def __str__(self):
        """ Returns a pretty string of the tree """
        def str_branches(node, branches):
            """ Returns a string with the tree pretty printed. 

                branches: a list of characters representing the parent branches. Characters can be either ` ` or '│'            
            """
            strings = [str(node._data)]

            i = 0           
            if node._left != None or node._right != None:
                for current in [node._left, node._right]:
                    if i == 0:            
                        joint = '├'
                    else:
                        joint = '└' 

                    strings.append('\n')
                    for b in branches:
                        strings.append(b)
                    strings.append(joint)
                    if i == 0:
                        branches.append('│')                    
                    else:
                        branches.append(' ')

                    if current != None:
                        if isinstance(current, BinTree):
                            strings.append(str_branches(current, branches))
                        else:
                            strings.append('ERROR: FOUND CHILD OF TYPE %s' % type(current))
                    branches.pop()                
                    i += 1
            return "".join(strings)
        
        return str_branches(self, [])

    def insert_left(self, data):
        """ Takes as input DATA (*NOT* a node !!) and MODIFIES current node this way:
        
            - First creates a new BinTree (let's call it B) into which provided data is wrapped.
            - Then:
                - if there is no left node in self, new node B is attached to the left of self
                - if there already is a left node L, it is substituted by new node B, and L becomes the 
                  left node of B
        """

        B =  BinTree(data)
        if self._left == None:
            self._left = B
        else:
            B._left = self._left
            self._left = B


    def insert_right(self, data):
        """ Takes as input DATA (*NOT* a node !!) and MODIFIES current node this way:
        
            - First creates a new BinTree (let's call it B) into which provided data is wrapped.
            - Then:
                - if there is no right node in self, new node B is attached to the right of self
                - if there already is a right node L, it is substituted by new node B, and L becomes the 
                  right node of B
        """
        B = BinTree(data)
        if self._right == None:
            self._right = B
        else:
            B._right = self._right
            self._right = B



    def same_rec(self, other):
        """ RETURN True if this binary tree is equal to other binary tree,
            otherwise return False.
            
            - MUST execute in O(n) where n is the number of nodes of the tree
            - NOTE: with big trees a recursive solution would surely 
                    exceed the call stack, but here we don't mind
        """
        #jupman-raise
        
        if other == None:
            return False
        
        if self.data() != other.data():
            return False
        
        if self.left() == None:            
            if other.left() != None:
                return False
        elif not self.left().same_rec(other.left()):
            return False
        
        if self.right() == None:            
            if other.right() != None:
                return False
        elif not self.right().same_rec(other.right()):
            return False                
        
        return True

           
        """ alternative version with helper function, a little cleaner:
        def helper(t1, t2):
            if (t1 == None) != (t2 == None):  # XOR
                return False
            if t1 == None and t2 == None:
                return True
            if t1.data() != t2.data():
                return False
            return helper(t1.left(), t2.left()) and helper(t1.right(), t2.right())

        return helper(self, other)
        """
        #/jupman-raise
        
