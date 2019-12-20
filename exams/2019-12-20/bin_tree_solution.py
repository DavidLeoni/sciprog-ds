
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
                        strings.append(str_branches(current, branches))
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
        

    def sum_leaves_rec(self):
        """ Supposing the tree holds integer numbers in all nodes,
            RETURN the sum of ONLY the numbers in the leaves.

            - a root with no children is considered a leaf
            - implement it as a recursive Depth First Search (DFS) traversal
              NOTE: with big trees a recursive solution would surely 
                    exceed the call stack, but here we don't mind            
        """ 
   
        #jupman-raise
        
        if self.left() == None and self.right() == None:
            ret = self.data()
        else:
            ret = 0
        if self.left() != None:
            ret += self.left().sum_leaves_rec()
        if self.right() != None:
            ret += self.right().sum_leaves_rec()
        return ret
        #/jupman-raise      


    def leaves_stack(self):
        """ RETURN a list holding the *data* of all the leaves  of the tree,
            in left to right order.
            - a root with no children is considered a leaf

            - DO *NOT* use recursion
            - implement it with a while and a stack (as a python list)            
        """        
        #jupman-raise
        ret = []
        stack = [self]
        while len(stack) > 0:
            node = stack.pop()
            if node.left() == None and node.right() == None:
                ret.append(node.data())
            # first right then left so we don't need to reverse later
            if node.right() != None:
                stack.append( node.right() )
            if node.left() != None:
                stack.append( node.left() )
        
        return ret
        #/jupman-raise        

    
