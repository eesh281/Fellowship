#*********************************************************************************************************
#@purpose    :performing merge sort
#@file name  :merge_sort.py
#@author name:Gursheesh Kour
#*******************************************************************************************************

#method to perform merge sort
def merge_sort(list1):
    if len(list1) > 1:
        #finding middle value
        mid = len(list1) // 2
        left_list = list1[:mid]
        right_list = list1[mid:]

        #calling method by passing left list and right list
        merge_sort(left_list)
        merge_sort(right_list)
        i = 0
        j = 0
        k = 0

        while (i < len(left_list) and j < len(right_list)):
            if left_list[i] < right_list[j]:
                list1[k] = left_list[i]
                i += 1
                k += 1
            list1[k] = right_list[j]
            j += 1
            k += 1
        while (i < len(left_list)):
                list1[k] = left_list[i]
                i += 1
                k += 1
        while (j < len(right_list)):
            list1[k] = right_list[j]
            j += 1
            k += 1

#taking a list of values
list1=[20,45,2,54,7]
#calling function by passing the given list
merge_sort(list1)
#printing sorted list
print(list1)
