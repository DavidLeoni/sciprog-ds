
def insertion_sort(A):
    """ Sorts in-place list A with insertion sort  

        Remember insertion sort has complexity O(n^2) where n is the 
        size of the list.
    """
    #jupman-raise
    for i in range(1, len(A)):                
        temp = A[i]                       
        j = i                             
        while j > 0 and A[j-1] > temp:    
            A[j] = A[j-1]                  
            j -= 1                         
        A[j] = temp    
    #/jupman-raise