DEBUG = True

def debug(msg):
    if DEBUG:
        print("DEBUG: ", str(msg).replace('\n', '\n' + (' '*8)))
        
class Stacktris:

    def __init__(self):
        """ Creates a Stacktris
        """
        self._stack = []


    def __str__(self):
        if len(self._stack) == 0:
            s = "EMPTY"
        else:
            s = ""
            for row in reversed(self._stack):
                s = s + '|' + "".join((str(x) if x > 0 else ' ' for x in row)) + '|\n'         

        return "Stacktris: \n%s" % s
        
    def __repr__(self):
        return self.__str__()


    def is_empty(self):
        """ RETURN True if the Stacktris empty, False otherwise
        """
        return len(self._stack) == 0

    def _shorten(self):      
        """ Scans the Stacktris from top to bottom searching for a completely filled line:
            - If it finds it, removes it from the Stacktris and return it as a list.
            - if it doesn't find it, return an empty list.
        """
        #jupman-raise          
        debug(self.__str__())        
        for i in reversed(range(len(self._stack))):
            if sum((1 if x > 0 else 0 for x in self._stack[i])) == 3:            
                row = self._stack.pop(i)
                debug("POPPING %s" % row)
                debug(self.__str__())
                return row
            
        return []
        #/jupman-raise          


    def drop1(self, j):
        """ Drops a 1-block on column j. 
        
             - If another block is found,  place the 1-block on top of that block,
               otherwise place it on the ground.

            - If, after the 1-block is placed, a row results completely filled, removes 
              the row and RETURN it. Otherwise, RETURN an empty list.

            - if index `j` is outside bounds, raises ValueError
        """        
        #jupman-raise
        
        if j < 0 or j > 2:
            raise ValueError("Expected a value between 0 and 2 included , found instead %s" % j)

        # search from top to bottom a suitable line
        for i in reversed(range(len(self._stack))):
            if self._stack[i][j] == 0:
                if i == 0:  # we're in first line
                    self._stack[i][j] = 1
                    return self._shorten()
                elif self._stack[i-1][j] > 0:   # check cell in line below is not empty
                    self._stack[i][j] = 1
                    return self._shorten()
            else:
                break
        # if we arrived till here without finding an empty cell, then we must add a new line

        lst = [0]*3
        lst[j] = 1
        self._stack.append(lst)  
        return self._shorten()
                 
        #/jupman-raise


    def drop2h(self, j):
        """ Drops a 2-block horizontally with left block on column j, 

             - If another block is found,  place the 2-block on top of that block,
               otherwise place it on the ground.

            - If, after the 2-block is placed, a row results completely filled, 
              removes the row and RETURN it. Otherwise, RETURN an empty list.        
        
            - if index `j` is outside bounds, raises ValueError
        """        
        #jupman-raise
        
        if j < 0 or j > 1:
            raise ValueError("Expected a value between 0 and 1 included , found instead %s" % j)

        # search from top to bottom a suitable line
        for i in reversed(range(len(self._stack))):
            if self._stack[i][j] == 0 and self._stack[i][j+1] == 0:
                if i == 0:   # we're in first line
                    self._stack[i][j] = 2
                    self._stack[i][j+1] = 2
                    return self._shorten()
                    # check cell in line below is not empty
                elif self._stack[i-1][j] > 0 or self._stack[i-1][j+1] > 0 :
                    self._stack[i][j] = 2
                    self._stack[i][j+1] = 2
                    return self._shorten()
            else:
                break
        
        # if we arrived till here without finding an empty cell, then we must add a new line

        lst = [0]*3
        lst[j] = 2
        lst[j+1] = 2
        self._stack.append(lst)  
        return self._shorten()           
                 
        #/jupman-raise



