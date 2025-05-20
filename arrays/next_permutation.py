def nextPermutation(arr):
    n = len(arr)
    
    pivot = -1
    # Step 1: Find the pivot
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            pivot = i
            break
    
    # Step 2: If no pivot, it's the last permutation; reverse the array
    if pivot == -1:
        arr.reverse()
        return
    
    # Step 3: Find the successor to swap with pivot
    for i in range(n - 1, pivot, -1):
        if arr[i] > arr[pivot]:
            arr[i], arr[pivot] = arr[pivot], arr[i]
            break

    # Step 4: Reverse the suffix
    left, right = pivot + 1, n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

arr = [3, 2, 1]
# obj = YourClass()
nextPermutation(arr)
print(arr)  # Output: [1, 2, 3]

arr1 = [2, 4, 1, 7, 5, 0]
# obj = YourClass()
nextPermutation(arr1)
print(arr1)  # Output: [2, 4, 5, 0, 1, 7]
