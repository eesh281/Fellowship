def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = [2, 1, 5, 3, 7, 9, 0]
bubble_sort(arr)
print(arr)
