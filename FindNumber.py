N = int(input("think of a number within 0 to the upper limit of?: "))


def binary_search(arr, l, r, x):
    if r >= l:
        mid =( l + r) // 2
        if arr[mid] == x:
            return mid
        p = input(f"Is it between {l} and {mid}")
        if p == 'True':
            return binary_search(arr, l, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, r, x)
    else:
        return -1


arr = list(range(0, N))
l = 0
r = len(arr)-1

B = binary_search(arr, l, r, 21)
print("The number is",B)
