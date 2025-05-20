def getMinDiff(arr, k):
    n = len(arr)
    
    # Step 1: Sort the array to make it easier to find min and max after modification
    arr.sort()
    
    # Step 2: Initialize result with the maximum possible difference (unmodified array)
    res = arr[n - 1] - arr[0]
    
    # Step 3: Try modifying the array such that:
    # Elements from 0 to i-1 are increased by k
    # Elements from i to n-1 are decreased by k
    for i in range(1, n):
        
        # If decreasing arr[i] by k makes it negative, skip this partition
        if arr[i] - k < 0:
            continue

        # Calculate the possible new minimum height
        # Either the smallest element increased by k or current element decreased by k
        minH = min(arr[0] + k, arr[i] - k)

        # Calculate the possible new maximum height
        # Either the previous element increased by k or the largest element decreased by k
        maxH = max(arr[i - 1] + k, arr[n - 1] - k)

        # Update result with the minimum difference found so far
        res = min(res, maxH - minH)
    
    return res


arr = [3, 9, 12, 16, 20]
k = 3
print(getMinDiff(arr, k))  # Output: 11

arr1 = [1, 5, 8, 10]
k = 2
print(getMinDiff(arr1, k))  # Output: 5
