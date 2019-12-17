#*********************************************************************************************************
#@purpose    :performing insertion sort
#@file name  :insertion_sort.py
#@author name:Gursheesh Kour
#*******************************************************************************************************

#method to perform insertion sort
def insertion_sort_(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key

    return arr

#giving a list for sorting
arr = [4, 2, 5, 6, 9, 1]
#calling the method
insertion_sort_(arr)
#printing sorted array
print("sorted array:", arr)
