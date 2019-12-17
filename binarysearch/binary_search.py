#*********************************************************************************************************
#@purpose    :performing binary search
#@file name  :binary_search.py
#@author name:Gursheesh Kour
#*******************************************************************************************************

#method for performing binary search
def binary_search_(arr, l, r, x):
    if r >= l:
        mid = l + (r - 1) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search_(arr, l, mid - 1, x)
        else:
            return binary_search_(arr, mid + 1, r, x)
    else:
        return -1

#giving a list
arr = ['a', 'ab', 'hb', 'sb']

#giving a element to be searched
x = 'hb'

#storing the result
result = binary_search_(arr, 0, len(arr) - 1, x)

if result != -1:
    print("element is present at index:", result)
else:
    print("not present")
