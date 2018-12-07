
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
                    
                
    def insert_left(self, data):
        """ Takes as input DATA (*NOT* a node !!) and MODIFIES current node this way:
        
            - First creates a new BinaryTree (let's call it B) into which provided data is wrapped.
            - Then:
                - if there is no left node in self, new node B is attached to the left of self
                - if there already is a left node L, it is substituted by new node B, and L becomes the 
                  left node of B
        """
        #jupman-raise
        B =  BinaryTree(data)
        if self._left == None:
            self._left = B
        else:
            B._left = self._left
            self._left = B
        #/jupman-raise

    def insert_right(self, data):
        """ Takes as input DATA (*NOT* a node !!) and MODIFIES current node this way:
        
            - First creates a new BinaryTree (let's call it B) into which provided data is wrapped.
            - Then:
                - if there is no right node in self, new node B is attached to the right of self
                - if there already is a right node L, it is substituted by new node B, and L becomes the 
                  right node of B
        """
        #jupman-raise
        B = BinaryTree(data)
        if self._right == None:
            self._right = B
        else:
            B._right = self._right
            self._right = B
        #/jupman-raise

    def height_rec(self):
        """ RETURN an integer which is the height of the tree

            - implement it as recursive call which does NOT modify the tree
              NOTE: with big trees a recursive solution would surely exceed the call stack,
                    but here we don't mind
            - A tree with only one node has height zero.
            
        """
        #jupman-raise
        if self.left() != None:
            h_left = self.left().height() 
        if self.right() != None:
            h_right = self.right().height() 
        
        return max(h_left, h_right) + 1
        #/jupman-raise

    def depth_dfs(self, level):
        """
            - MODIFIES the tree by putting in the data field the value level + 1,
              and recursively calls itself on left and right nodes (if present)  passing level + 1
            - implement it as a recursive Depth First Search (DFS) traversal
              NOTE: with big trees a recursive solution would surely exceed the call stack,
                    but here we don't mind
            - The root of a tree has depth zero.
            
        """
        #jupman-raise
        self._data = level + 1
        if self.left() != None:
            self.left().depth_dfs(level + 1) 
        if self.right() != None:
            self.right().depth_dfs(level + 1)         
        #/jupman-raise        

    