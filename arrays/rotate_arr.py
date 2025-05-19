def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotateArr(arr, d):
    n = len(arr)
    d %= n  # In case d > n

    reverse(arr, 0, d - 1)
    reverse(arr, d, n - 1)
    reverse(arr, 0, n - 1)
    return arr

# Test
arr = [1, 2, 3, 4, 5]
d = 2
rotateArr(arr, d)
print("Rotated array:", arr)