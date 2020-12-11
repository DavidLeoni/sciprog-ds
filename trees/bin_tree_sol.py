
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

    def sum_rec(self):
        """ Supposing the tree holds integer numbers in all nodes,
            RETURN the sum of the numbers.

            - implement it as a recursive Depth First Search (DFS) traversal
              NOTE: with big trees a recursive solution would surely 
                    exceed the call stack, but here we don't mind            
        """ 
   
        #jupman-raise
        ret = self._data
        if self.left() != None:
            ret += self.left().sum_rec()
        if self.right() != None:
            ret += self.right().sum_rec()
        return ret
        #/jupman-raise      

    def height_rec(self):
        """ RETURN an integer which is the height of the tree

            - implement it as recursive call which does NOT modify the tree
              NOTE: with big trees a recursive solution would surely exceed the call stack,
                    but here we don't mind
            - A tree with only one node has height zero.
            
        """
        #jupman-raise
        if self.left() == None:
            h_left = 0
        else:
            h_left = self.left().height_rec() + 1
        
        if self.right() == None:
            h_right = 0
        else:
            h_right = self.right().height_rec() + 1

        
        return max(h_left, h_right)
        #/jupman-raise
    
    
    

    def depth_rec(self, level):
        """ MODIFIES the tree by putting in the data field the provided value level (which is an integer),
            and recursively calls itself on left and right nodes (if present)  passing level + 1
            
            - implement it as a recursive Depth First Search (DFS) traversal
              NOTE: with big trees a recursive solution would surely exceed the call stack,
                    but here we don't mind
            - The root of a tree has depth zero.
            - does not return anything            
        """
        #jupman-raise
        self._data = level
        if self.left() != None:
            self.left().depth_rec(level + 1) 
        if self.right() != None:
            self.right().depth_rec(level + 1)        
        #/jupman-raise        

    def contains_rec(self, item):
        """ RETURN True if at least one node in the tree has data equal to item, otherwise RETURN False.

            - implement it as a recursive Depth First Search (DFS) traversal
              NOTE: with big trees a recursive solution would surely exceed the call stack,
                    but here we don't mind            
        """        
        #jupman-raise
        if self._data == item:
            return True
        else:
            if self.left() != None and self.left().contains_rec(item):
                return True                
            if self.right() != None and self.right().contains_rec(item):
                return True 
        return False
        #/jupman-raise


  

    def join_rec(self):
        """ Supposing the tree nodes hold a character each, RETURN a STRING holding 
            all characters with a IN-ORDER visit

            - implement it as a recursive Depth First Search (DFS) traversal
              NOTE: with big trees a recursive solution would surely 
                    exceed the call stack, but here we don't mind            
        """ 
   
        #jupman-raise
        ret = ''
        if self.left() != None:
            ret +=  self.left().join_rec()
        ret += self._data
        if self.right() != None:
            ret += self.right().join_rec()
        return ret
        #/jupman-raise        


    def fun_rec(self):
        """ Supposing the tree nodes hold expressions which can either be
            functions or single variables, RETURN a STRING holding 
            the complete formula with needed parenthesis

            - implement it as a recursive Depth First Search (DFS)
              PRE-ORDER visit
            - NOTE: with big trees a recursive solution would surely 
                    exceed the call stack, but here we don't mind            
        """ 
   
        #jupman-raise
        ret = self._data
        if self.left() != None:
            ret += '('
            ret +=  self.left().fun_rec()
            if self.right() != None:
                ret += ',' + self.right().fun_rec() 
            ret += ')'
        return ret
        #/jupman-raise        

    def bin_search_rec(self, m):
        """ Assuming the tree is a binary search tree of integer numbers, 
            RETURN True if m is present in the tree, False otherwise
        
            - MUST EXECUTE IN O(height(t))
            - NOTE: with big trees a recursive solution would surely 
                    exceed the call stack, but here we don't mind
        """
        #jupman-raise
        if m == self.data():
            return True
        elif m < self.data():
            return self.left() != None and self.left().bin_search_rec(m)
        else:
            return self.right() != None and self.right().bin_search_rec(m)
        #/jupman-raise

    def bin_insert_rec(self, m):
        """ Assuming the tree is a binary search tree of integer numbers, 
            MODIFIES the tree by inserting a new node with the value m
            in the appropriate position. Node is always added as a leaf.

            - MUST EXECUTE IN O(height(t))
            - NOTE: with big trees a recursive solution would surely 
                    exceed the call stack, but here we don't mind
        """
        #jupman-raise
        if m < self._data:            
            if self.left() == None:
                self.insert_left(m)
            else:
                self._left.bin_insert_rec(m)
        else:
            if self.right() == None:
                self.insert_right(m)
            else:                
                self.right().bin_insert_rec(m)
        #/jupman-raise

    def univalued_rec(self):
        """ RETURN True if the tree is univalued, otherwise RETURN False. 

            - a tree is univalued when all nodes have the same value as data
            - MUST execute in O(n) where n is the number of nodes of the tree
            - NOTE: with big trees a recursive solution would surely 
                    exceed the call stack, but here we don't mind
        """
        #jupman-raise
        if self.left() != None:
            if self.left().data() != self.data() or not self.left().univalued_rec():
                return False
        if self.right() != None:
            if self.right().data() != self.data() or not self.right().univalued_rec():
                return False

        return True
        #/jupman-raise

    def same_rec(self, other):
        """ RETURN True if this binary tree is equal to other binary tree,
            otherwise return False.
            
            - MUST execute in O(n) where n is the number of nodes of the tree
            - NOTE: with big trees a recursive solution would surely 
                    exceed the call stack, but here we don't mind
            - HINT: defining a helper function 
                    
                    def helper(t1, t2):

                    which recursively calls itself and assumes both of the
                    inputs can be None may reduce the number of ifs to write.
        """
        #jupman-raise
        def helper(t1, t2):
            if (t1 == None) != (t2 == None):  # XOR
                return False
            if t1 == None and t2 == None:
                return True
            if t1.data() != t2.data():
                return False
            return helper(t1.left(), t2.left()) and helper(t1.right(), t2.right())

        return helper(self, other)
        #/jupman-raise
        
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
        
         

    def schedule_rec(self):
        """ RETURN a list of task labels in the order they will be completed.

            - Implement it with recursive calls.
            - MUST run in O(n) where n is the size of the tree
            
            NOTE: with big trees a recursive solution would surely
                  exceed the call stack, but here we don't mind
        """
        #jupman-raise
        ret = []
        if self._left != None:
            ret.extend(self._left.schedule_rec())
        if self._right != None:
            ret.extend(self._right.schedule_rec())
        ret.append(self._data)
        return ret
        #/jupman-raise
           
    
    def paths_slow_rec(self):
        """ RETURN a list of all paths from this node to the each leaf.
            A path is a list which holds the nodes data found while traversing the tree.
                                    
            - for this slow version, you can only use + operator or .extend() method
              which will bring an O(n^3) complexity
            - implement it as recursive call 
              NOTE: with big trees a recursive solution would surely exceed the call stack,
                    but here we don't mind                          
        """        
        #jupman-raise        
        if self._left == None and self._right == None:
            return [[self._data]]
        
        left_paths = self._left.paths_slow_rec() if self._left != None else []
        right_paths = self._right.paths_slow_rec() if self._right != None else []                    
                
        return [[self._data] + path for path in left_paths] \
               + [[self._data] + path for path in right_paths]
        #/jupman-raise    
    
    def _paths_fast_helper(self):
        """ DO NOT use + operator nor .extend() method         
        """
        #jupman-raise                                
        if self._left == None and self._right == None:
            return [[self._data]]
        
        ret = []
        if self._left != None:            
            left_paths = self._left._paths_fast_helper()
            for path in left_paths:
                path.append(self._data)
                ret.append(path)
            
        if self._right != None:
            right_paths = self._right._paths_fast_helper()
            for path in right_paths:
                path.append(self._data)
                ret.append(path)
                
        return ret
        #/jupman-raise
                        
    def paths_fast_rec(self):
        """ RETURN a list of all paths from this node to the each leaf.
            A path is a list which holds the nodes data found while traversing the tree.
                        
            - DO NOT use + operator nor .extend() method 
            - MUST work in O(n^2) where n is the number of nodes in the tree
            - implement it as recursive call 
              NOTE: with big trees a recursive solution would surely exceed the call stack,
                    but here we don't mind                          
        """        
        #jupman-raise        
        ret = self._paths_fast_helper()
        for r in ret:
            r.reverse()
        return ret
        #/jupman-raise
        

    def sum_stack(self):
        """ Supposing the tree holds integer numbers in all nodes,
            RETURN the sum of the numbers.
            
            - DO *NOT* use recursion
            - implement it with a while and a stack (as a python list)
            - In the stack place nodes to process
        """ 
   
        #jupman-raise
        ret = 0
        stack = [self]
        while len(stack) > 0:
            node = stack.pop()
            ret += node.data()
            if node.left() != None:
                stack.append(node.left())
            if node.right() != None:
                stack.append(node.right())
        return ret

        #/jupman-raise      


    def height_stack(self):
        """ RETURN an integer which is the height of the tree

            - A tree with only one node has height zero.
            - DO *NOT* use recursion
            - implement it with a while and a stack (as a python list). 
            - In the stack place *tuples* holding a node *and* its level
            
        """
   
        #jupman-raise
        ret = 0
        stack = [(self, 0)]
        while len(stack) > 0:
            node,level = stack.pop()        
            ret = max(level, ret)
            if node.left() != None:
                stack.append( (node.left(), level + 1) )
            if node.right() != None:
                stack.append((node.right(), level + 1) )
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
        """        
        #jupman-raise
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
        
    def prune_rec(self, el):
        """ MODIFIES the tree by cutting all the subtrees that have their 
            root node data equal to el. By 'cutting' we mean they are no longer linked 
            by the tree on which prune is called.

            - if prune is called on a node having data equal to el, raises ValueError
            
            - MUST execute in O(n) where n is the number of nodes of the tree
            - NOTE: with big trees a recursive solution would surely 
                    exceed the call stack, but here we don't mind            
        """
        #jupman-raise

        if self._data == el:
            raise ValueError('Tried to prune the tree root!')
                
        if self._left != None:
            if self._left._data == el:
                self._left = None
            else:
                self._left.prune_rec(el)

        if self._right != None:
            if self._right._data == el:
                self._right = None
            else:
                self._right.prune_rec(el)

        #/jupman-raise