import sys
sys.path.append('../../../')
import jupman
jupman.mem_limit()

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

                
    def find_couple(self,a,b):
        """ Search the list for the first two consecutive elements having data 
            equal to provided a and b, respectively. If such elements are found,
            the position of the first one is returned, otherwise raises LookupError.
            
            - MUST run in O(n), where n is the size of the list.
            - Returned index start from 0 included
            
        """
        #jupman-raise                
        current = self._head
        i = 0
        
        while current != None:
            if current._data == a:
                if current._next != None:
                    if current._next._data == b:
                        return i
            i += 1
            current = current._next
            
        raise LookupError("Couldn't find couple " + str(a) + "," + str(b) + "!")
        #/jupman-raise

    def swap (self, i, j):
        """
            Swap the data of nodes at index i and j. Indeces start from 0 included.
            If any of the indeces is out of bounds, rises IndexError.
            
            NOTE: You MUST implement this function with a single scan of the list.
            
        """
        #jupman-raise
        if i < 0 or j < 0:
            raise IndexError("Invalid indeces! Both must be non-negative, found instead: i="+str(i) +", j="+str(j))
        
        current = self._head

        k = 0
        nodei = None
        nodej = None
        while current != None:
            if k == i:
                nodei = current
                if nodej != None:
                    break
            if k == j:
                nodej = current
                if nodei != None:
                    break
            current = current.get_next()
            k += 1
        
        if nodei == None or nodej == None:
            raise IndexError("Out of bounds ! i = " + str(i) + " j = " + str(j) )
        
        tmp = nodej.get_data()
        nodej.set_data(nodei.get_data())
        nodei.set_data(tmp)
        #/jupman-raise
