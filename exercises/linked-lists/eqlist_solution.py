class Node:
    """ A Node of a EqList. Holds data provided by the user. """
    
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


class EqList:
    """
        EqList - this is a stripped down verison of the LinkedList as seen in class
        
    """
        
    def __init__(self):
        self._head = None

        
    def __str__(self):
        """ For potentially complex data structures like this one, having a __str__ method is essential to 
            quickly inspect the data by printing it. 
        """
        current = self._head
        strings = []
        
        while (current != None):
            strings.append(str(current.get_data()))            
            current = current.get_next()            
        
        return "EqList: " + ",".join(strings)
        
        
    def is_empty(self):
        return self._head == None

    def add(self,item):    
        """ Adds item at the beginning of the list """
        new_head = Node(item)
        new_head.set_next(self._head)
        self._head = new_head

    def __eq__(self, other):
        """ Returns True if self is equal to other, that is, if all the data elements in the respective
            nodes are the same. Otherwise, return False.
            
            NOTE: compares the *data* in the nodes, NOT the nodes themselves !
        """
        #jupman-raise
        cur1 = self._head
        cur2 = other._head
                                
        while cur1 != None and cur2 != None:                
            if cur1.get_data() != cur2.get_data():
                return False
            
            cur1 = cur1.get_next()            
            cur2 = cur2.get_next()
            
        return cur1 == None and cur2 == None
        #/jupman-raise
        
    def remsub(self, rem):
        """ Removes the first elements found in this EqList that match subsequence rem
            rem: the subsequence to eliminate, which is also an EqList.
            
            Examples:
                aabca  remsub ac  =  aba 
                aabca  remsub cxa =  aaba  # when we find a never matching character in rem like 'x', 
                                             the rest of rem after 'x' is not considered.
                aabca  remsub ba  =  aac
                aabca  remsub a   =  abca
                abcbab remsub bb  =  acab
        """
        #jupman-raise
        cur1 = self._head
        cur2 = rem._head

        prev1 = None
                   
        while cur1 != None and cur2 != None:                
            
            if cur1.get_data() == cur2.get_data():
                
                if self._head == cur1:
                    self._head = cur1.get_next()
                    prev1 = None
                else:
                    prev1.set_next(cur1.get_next())
                    
                cur2 = cur2.get_next()
            else:
                prev1 = cur1
            
            cur1 = cur1.get_next()                        
        #/jupman-raise
        
