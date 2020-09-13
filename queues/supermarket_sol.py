

class CashQueue:
    """ ****   WARNING: DO NOT EDIT THIS CLASS !!!   ****

        A simple queue of clients, which are represented as strings.
    
        - Clients are enqueued at the right, in the tail
        - Clients are dequeued from the left, removing them from the head
  
        For example:

        q = CashQueue()
       
        q.is_empty()      # True

        q.enqueue('a')    #  a
        q.enqueue('b')    #  a,b
        q.enqueue('c')    #  a,b,c
        
        q.size()   # 3

        q.dequeue()   #       returns:  a
                      # queue becomes:  [b,c]

        q.dequeue()   #       returns:  b
                      # queue becomes:  [c]

        q.dequeue()   #       returns:  c
                      # queue becomes:  []

        q.dequeue()   # raises LookupError as there aren't enough elements to remove
    """

    def __init__(self):
        """ Initializes the queue. Note there is no capacity as parameter
            - Complexity: O(1)
        """

        self._list = []

    def __str__(self):
        return "CashQueue: " + str(self._list)


    def size(self):
        """ Return the size of the queue.
        """
        return len(self._list)

    def is_empty(self):
        """ Return True if the queue is empty, False otherwise.
        """
        return len(self._list) == 0

           
    def enqueue(self, client):
        """ Enqueues provided list of elements at the tail of the queue
        """

        self._list.append(client)
        
    def dequeue(self):
        """ Removes client from the head at the left of the queue, and return it
        """
        if self.is_empty():
            raise LookupError("CashQueue is empty !")
        else:
            return self._list.pop(0)  # inefficient, but for this exercise we don't care


class Supermarket:
    """ A model of supermarket cash queues, which should maximize the number of served clients

        Each CashQueue is a simple queue of clients represented as strings. A CashQueue
        supports the enqueue, dequeue and size operations.

        The whole supermarket itself can be seen as a particular kind of queue, which supports
        the enqueue and dequeue operations described as follows:
        
            by calling supermarket.enqueue(client) a client gets enqueued in the shortest cash queue.

            by calling supermarket.dequeue(), all clients which are at the head of 
            non-empty cash queues are dequeued all at once, and their list is returned.
    """

    def __init__(self, queues_as_lists):
        """ ****  WARNING:  DO NOT MODIFY THIS METHOD  ****

            Initializes the Supermarket queues with python lists provided in input,
            where the first clients arrived are on the left,
            and the last clients are on the right. 
            
            For example:

            [                  
                ['a','b'],
                ['c','d','e'],
                ['f']
            ]

            clients 'a', 'c', 'f' are at the heads of the cash queues.

            A supermarket must have at least one queue.

        """

        if len(queues_as_lists) == 0:
            raise ValueError("No queues as lists were provided!" )
        self._queues = []
        for lst in queues_as_lists:
            q = CashQueue()
            self._queues.append(q)
            for elem in lst:
                q.enqueue(elem)


    def __str__(self):
        """ DO NOT MODIFY THIS METHOD """

        ret = "Supermarket\n"
        j = 0
        for q in self._queues:
            ret += str(j) + " " + str(q) + "\n"
            j += 1
        return ret

   

    def size(self):
        """ Return the total number of clients present in all cash queues.
        """
        #jupman-raise
        ret = 0
        for q in self._queues:
            ret += q.size()
        return ret
        #/jupman-raise


    def dequeue(self):
        """ Dequeue all the clients which are at the heads of non-empty cash queues,
            and return a list of such clients.

            - clients are returned in the same order as found in the queues.
            - if supermarket is empty, an empty list is returned

            For example, suppose we have following supermarket:

            0  ['a','b','c']
            1  []
            2  ['d','e']
            3  ['f']
            

            A call to deque() will return ['a','d','f']
            and the supermarket will now look like this:
            
            0  ['b','c']
            1  []
            2  ['e']
            3  []            
        """
        #jupman-raise
        ret = []
        for q in self._queues:
            if not q.is_empty():
                elem = q.dequeue()
                ret.append(elem)
        return ret
        #/jupman-raise

    def enqueue(self, client):    
        """ Enqueue provided client in the cash queue with minimal length.
            
            If more than one minimal length cash queue is available, the one
            with smallest index is chosen. 
            
            For example:

            If we have this supermarket

            0  ['a','b','c']
            1  ['d','e','f','g']
            2  ['h','i']
            3  ['m','n']

            since queues 2 and 3 have both minimal length 2, supermarket.enqueue('z') will enqueue
            the client on queue 2 : 

            0  ['a','b','c']
            1  ['d','e','f','g']
            2  ['h','i','z']
            3  ['m','n']
        """
        #jupman-raise    
        qmin = self._queues[0]        
        for q in self._queues:
            if q.size() < qmin.size():
                qmin = q
        qmin.enqueue(client)
        #/jupman-raise
   
