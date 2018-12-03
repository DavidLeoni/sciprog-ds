
def insertion_sort(A):
    """ Sorts in-place list A with insertion sort.  """
    #jupman-raise
    for i in range(1, len(A)):                
        temp = A[i]                       
        j = i                             
        while j > 0 and A[j-1] > temp:    
            A[j] = A[j-1]                  
            j -= 1                         
        A[j] = temp    
    #/jupman-raise