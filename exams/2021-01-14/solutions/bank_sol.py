


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
        
        z = len(self._trans)
        if z > 0:
            last = self._trans[-1]  
            if (last, transaction) in self._index:
                self._index[(last, transaction)].append(z - 1)
            else:
                self._index[(last, transaction)] = [z - 1]
                
        self._trans.append(transaction)
        #/jupman-raise
    
    
    def pos(self, biseq):
        """ RETURN a NEW list with all the indeces where the sequence of 
            two transactions can be found
        
            - MUST execute in O(1)
        """
        #jupman-raise
        if biseq in self._index:
            return list(self._index[biseq])  # defensive copy, we don't want the user 
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
        
        z = len(self._trans)
        
        if z == 0:
            raise IndexError('No transactions to pop!')
        
        if z > 1:
            bi = tuple(self._trans[-2:])
            if bi in self._index:
                indeces = self._index[bi]
                if len(indeces) > 0:
                    if indeces[-1] == z - 2:
                        indeces.pop()
                if len(indeces) == 0:
                    del self._index[bi]
                    
        return self._trans.pop()
        #/jupman-raise
        
    def max_interval(self, bi_start, bi_end):
        """ RETURN a list with all the transactions occurred between 
            the *largest* interval among bi-sequences bi_start and bi_end
        
            - bi_start and bi_end are EXCLUDED 
            - if bi_start / bi_end are not found, or if bi_end is before/includes bi_start, 
              raise LookupError

            
            - DO *NOT* MODIFY the data structure
            - MUST EXECUTE IN O(k) where k is the length of the *largest* interval you can return
            - consider number of repetitions a negligible size
        """
        #jupman-raise
        if not bi_start in self._index:
            raise LookupError("Couldn't find bi_start %s" % str(bi_start))
        
        if not bi_end in self._index:
            raise LookupError("Couldn't find bi_end %s" % str(bi_end))
                    
            
        istart = self._index[bi_start][0]
        iend = self._index[bi_end][-1]
        
        if iend < istart + 2:
            raise LookupError("Couldn't find a valid interval! istart:%s iend:%s" % (istart, iend))
            
        return self._trans[istart+2:iend]  # takes only O(k) , no need to scan the whole list
        
        #/jupman-raise
