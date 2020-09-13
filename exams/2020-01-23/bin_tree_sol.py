
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

    def add_row(self, elems):
        """ Takes as input a list of data and MODIFIES the tree by adding
            a row of new leaves, each having as data one element of elems,
            in order.
            
            - elems size can be less than 2*|leaves|
            - if elems size is more than 2*|leaves|, raises ValueError
            - for simplicity, you can assume assume self is a perfect 
              binary tree, that is a binary tree in which all interior nodes 
              have two children and all leaves have the same depth
            - MUST execute in O(n+|elems|)  where n is the size of the tree
            - DO *NOT* use recursion
            - implement it with a while and a stack (as a Python list)
        """         #jupman-raise
        leaves = []
        stack = [self]
        while len(stack) > 0:
            node = stack.pop()
            if node.left() == None and node.right() == None:
                leaves.append(node)
            # first right then left so we don't need to reverse later
            if node.right() != None:
                stack.append( node.right() )
            if node.left() != None:
                stack.append( node.left() )

        if len(elems) > 2*len(leaves):
            raise ValueError("Not enough nodes ! Tried to append row of %s elements to %s leaves !" % (len(elems), len(leaves)))

        j = 0
        for i in range(len(elems)):            
            if i % 2 == 0:
                leaves[j].insert_left(elems[i])
            else:
                leaves[j].insert_right(elems[i])
                j += 1
            
        #/jupman-raise        

    
