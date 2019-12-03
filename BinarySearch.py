def binary_search(arr, l, r, x):
    if r >= l:
        mid = l + (r - 1) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, r, x)
    else:
        return -1


arr = ['a', 'ab', 'hb', 'sb']
x = 'hb'
result = binary_search(arr, 0, len(arr) - 1, x)
if result != -1:
    print("element is present at index:", result)
else:
    print("not present")
