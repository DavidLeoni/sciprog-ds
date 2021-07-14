import jupman;
jupman.mem_limit()

class BinaryTree:
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
                        if isinstance(current, BinaryTree):
                            strings.append(str_branches(current, branches))
                        else:
                            strings.append('ERROR: FOUND CHILD OF TYPE %s' % type(current))
                    branches.pop()                
                    i += 1
            return "".join(strings)
        
        return str_branches(self, [])

    def insert_left(self, data):
        """ Takes as input DATA (*NOT* a node !!) and MODIFIES current node this way:
        
            - First creates a new BinaryTree (let's call it B) into which provided data is wrapped.
            - Then:
                - if there is no left node in self, new node B is attached to the left of self
                - if there already is a left node L, it is substituted by new node B, and L becomes the 
                  left node of B
        """
        B =  BinaryTree(data)
        if self._left == None:
            self._left = B
        else:
            B._left = self._left
            self._left = B


    def insert_right(self, data):
        """ Takes as input DATA (*NOT* a node !!) and MODIFIES current node this way:
        
            - First creates a new BinaryTree (let's call it B) into which provided data is wrapped.
            - Then:
                - if there is no right node in self, new node B is attached to the right of self
                - if there already is a right node L, it is substituted by new node B, and L becomes the 
                  right node of B
        """
        B = BinaryTree(data)
        if self._right == None:
            self._right = B
        else:
            B._right = self._right
            self._right = B


    def union_rec(self, other):
        """ Supposing this is a binary tree of integers, takes another binary tree
            and MODIFIES self so it becomes the union of the two.            

            Imagine to overlay the two trees, and:
            - whenever two nodes occupy the same position, the self one is updated 
                by summing the corresponding node data from other
            - if other has more nodes than self, create corresponding NEW nodes in self
           
            - a recursive solution is acceptable
            - DO *NOT* share nodes between the trees
            - DO *NOT* throw away existing nodes in self
            - MUST run in O(max(n,m)) where n,m are the number of nodes in self 
              and other
        """
        #jupman-raise
        if other == None:  
            return
        
        self._data += other._data
        
        if self._left and other._left:
            self._left.union_rec(other._left)
        elif not self._left and other._left:
            self.insert_left(0)
            self._left.union_rec(other._left)
        
        if self._right and other._right:
            self._right.union_rec(other._right)
        elif not self._right and other._right:
            self.insert_right(0)
            self._right.union_rec(other._right)

        #/jupman-raise




