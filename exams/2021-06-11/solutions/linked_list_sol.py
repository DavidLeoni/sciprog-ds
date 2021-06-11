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
        
        
    def add(self,item):    
        """ Adds item at the beginning of the list """
        
        new_head = Node(item)
        new_head.set_next(self._head)
        self._head = new_head

             
    
    def sepel(self, el):
        """ Separates this list into two lists:

            - this list will have all nodes without el as data
            - the other list will contain all nodes with el as data
            
            - IMPORTANT: DO *NOT* create new nodes, REUSE existing ones!!
            - MUST execute in O(n), where n is the length of the list
                           
        """
        #jupman-raise

        ret = LinkedList()

        current = self._head
        ret_last = None
        prev = None
        while current != None:
            
            #  a  b  c  b  c  c  b  d  c
            #        |     |  |        |
            
            if current.get_data() == el:
                if ret_last == None:
                    ret._head = current
                else:
                    ret_last.set_next(current)
                ret_last = current                
                nx = current.get_next()
                if prev == None:
                    self._head = nx
                else:
                    prev.set_next(nx)
                current.set_next(None)
                current = nx                
            else:
                prev = current
                current = current.get_next()
        return ret
        #/jupman-raise