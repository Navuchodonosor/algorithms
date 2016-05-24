"""
    heap_sort.py

    Implementation of heap sort on a list and returns a sorted list.

    Heap Sort Overview:
    -------------------
    Uses the max heap data structure implemented in a list.

    Time Complexity: O(n log n)

    Space Complexity: O(1) Auxiliary

    Stable: Yes

    Psuedo Code: CLRS. Introduction to Algorithms. 3rd ed.

"""


def heapSort(array):
    
    def shiftDown (object, i, j):
 
        n_el= object[i]
        while 2*i+1 < j:
            Child = 2*i+1
            if Child+1 < j and object[Child] < object[Child+1]:
               Child+= 1
            if n_el >= object[Child]:
               break
            object[i] = object[Child]
            i = Child
        object[i] = n_el
    
    leng = len(array)
    for i in range(leng//2-1,-1,-1):
        shiftDown(array, i, leng)
        
    for i in range(leng-1, 0, -1):
        temp= array[i]
        array[i]=array[0]
        array[0]= temp
        shiftDown(array,0,i)
    
    return array