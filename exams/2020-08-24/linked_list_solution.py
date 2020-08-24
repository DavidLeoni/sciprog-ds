class Node:
    """ A Node of an LinkedList. Holds data provided by the user. """
    
    def __init__(self,initdata):
        self._data = initdata
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self,newdata):
        self._data = newdata

    def set_next(self,newnext):
        self._next = newnext


class LinkedList:
    """
        This is a stripped down version of the LinkedList as previously seen.
        Note it also holds _size and _last attributes.
        
    """
        
    def __init__(self):
        self._head = None        

        
    def __str__(self):
        current = self._head
        strings = []
        
        while (current != None):
            strings.append(str(current.get_data()))            
            current = current.get_next()            
        
        return "LinkedList: " + ",".join(strings)
        

    def is_empty(self):
        return self._head == None


    def add(self,item):    
        """ Adds item at the beginning of the list """

        new_head = Node(item)
        new_head.set_next(self._head)
        self._head = new_head

                        
    def couple_sort(self):
        """MODIFIES the linked list by considering couples of nodes at even indexes
           and their successors: if a node data is lower than its successor data, swaps the nodes *data*.
           
           - ONLY swap *data*, DO NOT change node links.
           - if linked list has odd size, simply ignore the exceeding node.
           - MUST execute in O(n), where n is the size of the list
        """
        #jupman-raise

        if self._head == None:
            return

        prev = self._head
        current = self._head.get_next()
            
        while current != None:
            tmp = current.get_data()
            if prev.get_data() > current.get_data():
                current.set_data(prev.get_data())
                prev.set_data(tmp)

            if current.get_next() == None:
                current = None
            else:
                prev = current.get_next()
                current = current.get_next().get_next()
        
        #/jupman-raise
