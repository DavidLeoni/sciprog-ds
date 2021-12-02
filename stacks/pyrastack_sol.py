import jupman;

DEBUG = True

def debug(msg):
    if DEBUG:
        print("DEBUG: ", msg.replace('\n', '\n' + (' '*8)))

class PyraStack:

    def __init__(self):        
        self._rows = []

    def __str__(self):        
        """ NOTE: rows are printed bottom-up
        """
        return "\n".join(''.join(row) for row in reversed(self._rows))    

    

    def drop(self, w):
        """ Drops a block of size w on the pyrastack, trying to place it on
            the top leftmost position without having missing blocks below.
            If top row is not feasible, scans for the first available leftmost 
            place which can fully accomodate the block.            

            - if w is negative, raise ValueError
            - if w is zero, no change is made

            - MUST run in O(h + w) where h is the stack height 
        """
        #jupman-raise
        
        def h():                        
            if w < 0:
                raise ValueError("Invalid negative width: %s" % w)
            if w == 0:
                return
            
            i = len(self._rows)

            if i == 0:
                self._rows.append(['-']*w)
                return

            if i > 0 and w <= len(self._rows[-1]):
                self._rows.append(['-']*w)
                return

            while i > 0:
                i -= 1
                if len(self._rows[i]) + w <= len(self._rows[i-1]):
                    self._rows[i].extend(['-'] * w)                
                    return                             

            self._rows[0].extend(['-']*w)                
        h()
        debug("Dropped %s, pyrastack is:\n%s" % (w, str(self)))
        #/jupman-raise

