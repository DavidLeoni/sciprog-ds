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

    def bubble_sort(self):
        """ Sorts in-place this linked list using the method of bubble sort

            - MUST execute in O(n^2) where n is the length of the linked list
        """
        #jupman-raise
        cur1 = self._head
        while cur1 != None:
            cur2 = self._head
            while cur2 != None and cur2.get_next() != None:
                d1 = cur2.get_data()
                d2 = cur2.get_next().get_data()
                if d1 > d2:                
                    cur2.set_data(d2)
                    cur2.get_next().set_data(d1)
                cur2 = cur2.get_next()  
            cur1 = cur1.get_next()
        #/jupman-raise

    def merge(self,l2):
        """ Assumes this linkedlist and l2 linkedlist contain integer numbers
            sorted in ASCENDING order, and  RETURN a NEW LinkedList with
            all the numbers from this and l2 sorted in DESCENDING order

            IMPORTANT 1: *MUST* EXECUTE IN O(n1+n2) TIME where n1 and n2 are
                         the sizes of this and l2 linked_list, respectively

            IMPORTANT 2: *DO NOT* attempt to convert linked lists to
                         python lists!
        """
        #jupman-raise
        cur1 = self._head
        cur2 = l2._head

        ret = LinkedList()

        while cur1 != None and cur2 != None:
                
            d1 = cur1.get_data()
            d2 = cur2.get_data()
            if d1 < d2:
                ret.add(d1)
                cur1 = cur1.get_next()
            else:
                ret.add(d2)
                cur2 = cur2.get_next()
            
        # add remaining 

        while cur1 != None:
            ret.add(cur1.get_data())
            cur1 = cur1.get_next()

        while cur2 != None:
            ret.add(cur2.get_data())
            cur2 = cur2.get_next()

        return ret
        #/jupman-raise