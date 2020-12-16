class BinaryTree:

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
        
        B = BinaryTree(data)
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
        

    def swap_stack(self, a, b):
        """ Given two elements a and b, locates the two nodes where they are contained
            and swaps *only the data* in the found nodes.

            - if a or b are not found, raise LookupError

            - IMPORTANT 1: assume tree is NOT ordered
            - IMPORTANT 2: assume all nodes have different data
            - Implement it with a while and a stack
            - MUST execute in O(n) where n is the size of the tree
        """
        #jupman-raise
        node_a = None
        node_b = None

        stack = [self]

        while len(stack) > 0:
            node = stack.pop()

            if node._data == a:
                node_a = node
            if node._data == b:
                node_b = node
            if node_a != None and node_b != None:
                node_a._data, node_b._data = node_b._data, node_a._data
                return

            if node._left != None:
                stack.append(node._left)
            if node._right != None:
                stack.append(node._right)

        raise LookupError("Couldn't find elements! node_a=%s node_b=%s" % (node_a, node_b))
        #/jupman-raise

    def family_sum_rec(self):
        """ MODIFIES the tree by adding to each node data its *original* parent and children data

            - MUST execute in O(n) where n is the size of the tree
            - a recursive implementation is acceptable
            - HINT: you will probably want to define a helper function
        """
        #jupman-raise
        def helper(node, pdata):
            tmp = node.data()
            d = node.data()

            if pdata != None:
                d += pdata
            if node._left != None:
                d += node._left.data()
                helper(node._left, tmp)
            if node._right != None:
                d += node._right.data()
                helper(node._right, tmp)
            node._data = d

        helper(self, None)
        #/jupman-raise