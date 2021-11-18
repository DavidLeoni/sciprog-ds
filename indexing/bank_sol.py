


class Bank:

    def __init__(self):
        """ Initializes an empty bank
        
            Add a data structure of your choice for indexing the log
        """
        self._trans = []
        #jupman-raise
        self._index = {}
        #/jupman-raise

    def __str__(self):
        """Already implemented, if you want you can add display of your own index (not mandatory)
        """
        return "%s: %s" % (self.__class__.__name__, ','.join(str(t) for t in self._trans))
        
    def log(self, transaction):
        """ Appends transaction to the log
        
            - REMEMBER to also update the index
            - MUST EXECUTE IN O(1)
        """
        #jupman-raise

        #     0 a
        #     1 d
        #     2 e
        #     3 r
        #     4 u
        #     5 m  
        #z -> 6 
        
        z = len(self._trans)
        if z > 1:            
            triple = (self._trans[-2], self._trans[-1], transaction)
            if triple in self._index:
                self._index[triple].append(z - 2)
            else:
                self._index[triple] = [z - 2]
                
        self._trans.append(transaction)
        #/jupman-raise
    
    
    def pos(self, triseq):
        """ RETURN a NEW list with all the indeces where the sequence of 
            three transactions can be found
        
            - MUST execute in O(1)
        """
        #jupman-raise
        if triseq in self._index:
            return list(self._index[triseq])  # defensive copy, we don't want the user 
                                              # to mess with our internal data !
        else:
            return []
        
        #/jupman-raise
        
    def revert(self):
        """ Completely eliminates last transaction and RETURN it

            - if bank is empty, raises IndexError
            
            - REMEMBER to update any index referring to it
            - *MUST* EXECUTE IN O(1) 
        """        
        #jupman-raise                                

        #     0 a
        #     1 d
        #     2 e
        #     3 r
        #     4 u
        #     5 m  
        #z -> 6 


        z = len(self._trans)
        
        if z == 0:
            raise IndexError('No transactions to pop!')
                
        if z > 2:
            tri = tuple(self._trans[-3:])
            if tri in self._index:
                indeces = self._index[tri]
                if len(indeces) > 0:
                    if indeces[-1] == z - 3:
                        indeces.pop()
                if len(indeces) == 0:
                    del self._index[tri]
                    
        return self._trans.pop()
        #/jupman-raise
        
    def max_interval(self, tri_start, tri_end):
        """ RETURN a list with all the transactions occurred between 
            the *largest* interval among tri-sequences tri_start and tri_end
        
            - tri_start and tri_end are EXCLUDED 
            - if tri_start / tri_end are not found, or if tri_end is before/includes tri_start, 
              raise LookupError

            
            - DO *NOT* MODIFY the data structure
            - MUST EXECUTE IN O(k) where k is the length of the *largest* interval you can return
            - consider number of repetitions a negligible size
        """
        #jupman-raise
        if not tri_start in self._index:
            raise LookupError("Couldn't find tri_start %s" % str(tri_start))
        
        if not tri_end in self._index:
            raise LookupError("Couldn't find tri_end %s" % str(tri_end))
                            
        istart = self._index[tri_start][0]
        iend = self._index[tri_end][-1]
        
        if iend < istart + 3:
            raise LookupError("Couldn't find a valid interval! istart:%s iend:%s" % (istart, iend))
            
        return self._trans[istart+3:iend]  # takes only O(k) , no need to scan the whole list
        
        #/jupman-raise
