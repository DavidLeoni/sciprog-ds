import pprint

class Node:
    """ A Node of an ItalianQueue. 
        Holds both data and group provided by the user. 
    """
    
    def __init__(self, initdata, initgroup):
        self._data = initdata
        self._group = initgroup
        self._next = None

    def get_data(self):
        return self._data

    def get_group(self):
        return self._group
    
    def get_next(self):
        return self._next

    def set_data(self,newdata):
        self._data = newdata

    def set_next(self,newnext):
        self._next = newnext

    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return 'Node(%s,%s)' % (self._data, self._group)

class ItalianQueue:
    """ An Italian queue, v2.  
    
        - Implemented as a LinkedList
        - In this case, worst case enqueue MUST be O(1)
        - has extra methods, for accessing groups and tail:
            - top_group()
            - tail()
            - tail_group()
                        
        Each element is assigned a group; during enqueing, queue is 
        scanned from head to tail to find if there is another element
        with a matching group. 
            - If there is, element to be enqueued is inserted after the 
              last element in the same group sequence (that is, to the 
              right of the group)
            - otherwise the element is inserted at the end of the queue

    """
    
    def __init__(self):
        """ Initializes the queue. Note there is no capacity as parameter
                
            - Complexity: O(1)
        """
        self._head = None
        self._tail = None
        self._tails = {}
        self._size = 0

               
    def __str__(self):
        """ For potentially complex data structures like this one, having 
            a __str__ method is essential to quickly inspect the data by printing it. 
        """
        current = self._head
        sdata = []
        sgroups = []
        
        while (current != None):
            sdata.append(str((current.get_data())))            
            sgroups.append(str((current.get_group())))            
            current = current.get_next()            
        
        if type(self._tails) == dict:
            stails = ("{" + "\n               ".join("{!r}: {!r},".format(k, v) for k, v in self._tails.items()) + "}")
        else:
            stails = pprint.pformat(stails)
        return "ItalianQueue: " + "->".join(sdata) + "\n              " + "  ".join(sgroups) + \
             "\n       _head: %s" % self._head + \
             "\n       _tail: %s" % self._tail + \
             "\n      _tails: %s" % stails
    
    def size(self):
        """ Return the size of the queue.
        
            - MUST perform in O(1)
        """
        return self._size

    def is_empty(self):
        """ Return True if the queue is empty, False otherwise.
        
            - MUST perform in O(1)
        """
        return self._head == None
    
    def top(self):
        """ Return the element at the head of the queue, without removing it. 
        
            - If the queue is empty, raises LookupError.            
            - MUST perform in O(1)
        """
        if self._head != None:
            return self._head.get_data()
        else:
            raise LookupError("Queue is empty !")    


    def top_group(self):
        """ Return the group of the element at the head of the queue, 
            without removing it. 
        
            - If the queue is empty, raises LookupError.
            - MUST perform in O(1)
        """
        if self._head != None:
            return self._head.get_group()
        else:
            raise LookupError("Queue is empty !")    


    def tail(self):
        """ Return the element at the tail of the queue (without removing it)
        
            - If the queue is empty, raises LookupError.            
            - MUST perform in O(1)
        """
        if self._tail != None:
            return self._tail.get_data()
        else:
            raise LookupError("Queue is empty !")    

    def tail_group(self):
        """ Return the group of the element at the tail of the queue (without removing it). 
        
            - If the queue is empty, raises LookupError.
            - MUST perform in O(1)
        """
        if self._tail != None:
            return self._tail.get_group()
        else:
            raise LookupError("Queue is empty !")    
                        
    def enqueue(self, v, g):
        """ Enqueues provided element v having group g, with the following 
            criteria:
        
            Queue is scanned from head to find if there is another element 
            with a matching group:
                - if there is, v is inserted after the last element in the 
                  same group sequence (so to the right of the group)
                - otherwise v is inserted at the end of the queue

            - MUST run in O(1)
        """
        #jupman-raise
        new_node = Node(v,g)
        self._size += 1        

        if self._head == None:     # empty queue
            self._head = new_node
            self._tail = new_node
            self._tails[g] = new_node
        else:                      # non-empty queue
        
            if g in self._tails:
                gt = self._tails[g]
            else:
                gt = self._tail
            new_node.set_next(gt.get_next())
            gt.set_next(new_node)
            if new_node.get_next() == None:
                self._tail = new_node
            self._tails[g] = new_node

        #/jupman-raise
    
    def dequeue(self):
        """ Removes head element and returns it.
            
            - If the queue is empty, raises a LookupError.            
            - MUST perform in O(1)
            - REMEMBER to clean unused _tails keys
        """
        #jupman-raise
        if self._head == None:
            raise LookupError("Queue is empty !")                    
        
        g = self._head.get_group()
        second = self._head.get_next()
        ret = self._head.get_data()

        if second == None:
            self._tail = None
            self._tails = {}
        else: # no more group g
            if g != second.get_group():
                del self._tails[g]
        self._head = second
        self._size -= 1            
        return ret
        
        
        #/jupman-raise

