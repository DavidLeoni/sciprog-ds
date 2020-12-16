class Node:
    
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
        """ Return True if the list is empty, False otherwise
        
            - MUST execute in O(1)
        """        
        return self._head == None
        

    def add(self,item):            
        """ Adds item at the beginning of the list 
        
            - MUST execute in O(1)
        """
        
        new_head = Node(item)
        new_head.set_next(self._head)
        self._head = new_head
        


    def pivot(self):
        """
            Selects first node data as pivot, and then MOVES before the pivot
            all the nodes which have data value STRICTLY LESS (<) than the pivot.
            Finally, RETURN the number of moved nodes.

            IMPORTANT:
            - *DO NOT* create new nodes
            - nodes less than pivot must be in the reversed order they were found
            - nodes greater or equal than pivot will maintain the original order
            - MUST EXECUTE in O(n), where n is the list size
        """
        #jupman-raise

        if self._head == None:
            return 0

        piv = self._head.get_data()

        prev = self._head
        current = self._head.get_next()
        ret = 0


        while current != None:
            if current.get_data() < piv:
                tmp = current.get_next()
                prev.set_next(tmp)
                current.set_next(self._head)
                self._head = current

                current = tmp
                ret += 1
            else:
                prev = current
                current = current.get_next()

        return ret
        #/jupman-raise


