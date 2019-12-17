#*********************************************************************************************************
#@purpose    :performing bubble sort
#@file name  :bubble_sort.py
#@author name:Gursheesh Kour
#*******************************************************************************************************

#method for performing bubble sort
def bubble_sort_(arr):
    n = len(arr)
    for i in range( 0, n ):
        for j in range( 0, n - 1 - i ):
            if arr[j] > arr[ j + 1 ]:
                arr[j], arr[ j + 1 ] = arr[ j + 1 ], arr[ j ]
    return arr

#giving a list
arr = [2, 1, 5, 3, 7, 9, 0]

#calling the method
bubble_sort_(arr)

#printing the sorted list
print(arr)
