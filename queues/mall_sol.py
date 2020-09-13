from collections import OrderedDict

class Client:
    """ ****   WARNING: DO NOT EDIT THIS CLASS !!!   ****     
    """

    def __init__(self, name, to_visit):
        """ Initializes the client.
            - Complexity: O(1)
        """

        self._name = name
        self._to_visit = to_visit


    def name(self): 
        """ Return the client name
        """
        return self._name

    def to_visit(self):
        """Return the shop names to visit
        """
        return self._to_visit

    def __repr__(self):
        return "Client %s : %s" % (self._name, self._to_visit)


class Shop:
    """ ****   WARNING: DO NOT EDIT THIS CLASS !!!   ****
    """

    def __init__(self, name):
        """ Initializes the shop.
            - Complexity: O(1)
        """

        self._name = name
        self._clients = []  # a list-like queue, clients enter from the right

    def __repr__(self):
        return "Shop %s : %s" % (self._name, self._clients)
        #__str__(self)

    def name(self):
        """ Return the name of the shop
        """
        return self._name


    def size(self):
        """ Return the size of the queue.
        """
        return len(self._clients)

    def is_empty(self):
        """ Return True if the queue is empty, False otherwise.
        """
        return len(self._clients) == 0

           
    def enqueue(self, client_name):
        """ Enqueues provided list of elements at the tail of the queue
        """

        self._clients.append(client_name)
        
    def dequeue(self):
        """ Removes client from the head at the left of the queue, and return it
        """
        if self.is_empty():
            raise LookupError("Shop is empty !")
        else:
            return self._clients.pop(0)  # inefficient, but for this exercise we don't care


class Mall:
    """ A model of shopping mall shop queues, which should maximize the number of served clients

        Each Shop has a name and queue of clients represented as strings. A Shop
        supports the enqueue, dequeue and size operations.

        The whole Mall itself can be seen as a particular kind of queue, which supports
        the enqueue and dequeue operations described as follows:
        
    
        by calling mall.enqueue(client) a client gets enqueued in the first Shop the client wants to visit (its desired shop visits doesn't change)

        by calling mall.dequeue()
            - all clients which are at the heads of non-empty Shops are dequeued all at once
            - their first desired shop to visit is removed
            - if a client has any shop to visit left, he is automatically enqueued in that Shop
            - the list of clients with no shops to visit is returned (this simulates parallelism)
.
    """

    def __init__(self, shops_as_list, clients_as_list):
        """ ****  WARNING:  DO NOT MODIFY THIS METHOD  ****

            A shopping Mall contains several shops and clients. It is possible to initialize a Mall by providing:

            1. shops as a list of values shop name , client list, where the first clients arrived are      on the left, and the last clients are on the right.
            2. clients as a list of values client name , shop to visit 

            For example, by calling:

            m = Mall(
            [
                'x', ['a','b','c'],     # <------ clients arrive from right
                'y', ['d'],
                'z', ['f','g']
            ],
            [                         
                'a',['y','x'],        
                'b',['x'],
                'c',['x'],
                'd',['z','y'],        # shops to visit stack grows from right, so
                'f',['y','x','z'],    # client 'f' wants to visit first shop 'z', then 'x', then 'y'
                'g',['x','z']
            ])

            A Mall must have at least one shop and may have zero clients
            All clients must want to visit existing shops.            

        """

        if len(shops_as_list) == 0:
            raise ValueError("No shops as list were provided!" )
        if len(shops_as_list) % 2 != 0:
            raise ValueError("shops list should be of even size ! Found instead %s " % shops_as_list )
        if len(clients_as_list) % 2 != 0:
            raise ValueError("clients list should be of even size ! Found instead %s " % clients_as_list )
        
        self._shops = OrderedDict()
        self._clients = OrderedDict()
        
        shop_it = iter(shops_as_list)
        for shop_name in shop_it:
            s = Shop(shop_name)            
            for client in next(shop_it):
                s.enqueue(client)
            self._shops[shop_name] = s

        client_it = iter(clients_as_list)
        for client_name in client_it:
            
            to_visit = next(client_it)
            if len(to_visit) == 0:
                raise ValueError("Found client with no shop to visit! Client is %s " % client_name)
            
            c = Client(client_name, to_visit)            

            for shop_name in c.to_visit():
                if shop_name not in self._shops:
                    raise ValueError("Passed a client wanting to visit a non-existing shop ! Client is %s and shop is %s " % (client_name,shop_name))
            
            top_shop_name = c.to_visit()[-1]
            if client_name not in self._shops[top_shop_name]._clients:
                raise ValueError("Passed a client which is not in line in its current top shop! Client %s shop %s" % (client_name, top_shop_name))
            
            self._clients[client_name] = c

    def shops(self):
        """ Return the shops as a OrderedDict
        """
        return self._shops

    def clients(self):
        """ Return the clients as a OrderedDict
        """
        return self._clients


    def __repr__(self):
        """ DO NOT MODIFY THIS METHOD """

        ret = "Mall\n"
        
        for shop_name in self._shops:
            ret += "  %s\n" % self._shops[shop_name]
        ret += "\n"
        for client_name in self._clients:
            ret += "  %s\n" % self._clients[client_name]

        return ret


    def enqueue(self, client):    
        """ Enqueue provided client in the top shop he wants to visit

            - If client is already in the mall, raise ValueError 
            - if client has no shop to visit, raise ValueError
            - If any of the shops to visit are not in the mall, raise ValueError

            For example:

            If we have this mall:

            Mall
                Shop x: ['a','b']
                Shop y: ['c']

                Client a: ['y','x']
                Client b: ['x']
                Client c: ['x','y']
                
            mall.enqueue(Client('d',['x','y'])) will enqueue the client in Shop y : 

            Mall
                Shop x: ['a','b']
                Shop y: ['c','d']

                Client a: ['y','x']
                Client b: ['x']
                Client c: ['x','y']
                Client d: ['x','y']

        """    
        #jupman-raise
        if client.name() in self._clients:
            raise ValueError("Client is already in the mall !")
        if len(client.to_visit()) == 0:
            raise ValueError("Client should visit at least one shop !")
        
        for shop_name in client.to_visit():
            if shop_name not in self._shops:
                raise ValueError("Client has to visit a non existing shop %s!" % shop_name )

        self._shops[client.to_visit()[-1]].enqueue(client.name())
        self._clients[client.name()] = client
        #/jupman-raise

    def dequeue(self):
        """ Dequeue all the clients which are at the heads of non-empty shop queues,
            and return a list of such client names.

            - shop list is scanned, and all clients which are at the heads of non-empty Shops are dequeued
              VERY IMPORTANT HINT: FIRST put all this clients in a list, 
                                   THEN using that list do all of the following

            - for each dequeued client, his top desired shop is removed from his visit list
            - if a client has a shop to visit left, he is automatically enqueued in that Shop
                - clients are enqueued in the same order they were dequeued from shops
            - the list of clients with no shops to visit anymore is returned (this simulates parallelism)
                - clients are returned in the same order they were dequeued from shops
            - if mall has no clients, an empty list is returned

        """
        #jupman-raise
        ret = []

        dequeued_clients = []

        for shop_name in self._shops:
            s = self._shops[shop_name]
            if not s.is_empty():
                dequeued_clients.append(s.dequeue())

        for client_name in dequeued_clients:
            client = self._clients[client_name]
            if len(client.to_visit()) == 1:
                ret.append(client_name)
                del self._clients[client_name]
            else: # > 1
                client.to_visit().pop()
                next_shop_name = client.to_visit()[-1]
                self._shops[next_shop_name].enqueue(client.name())
        return ret
        #/jupman-raise
    
