def findKthNumber(m, n, k):
    # Helper function to count how many numbers are less than or equal to 'x' in the multiplication table
    def countLessEqual(x):
        count = 0
        for i in range(1, m + 1):
            # Each row has values: i*1, i*2, ..., i*n
            # Number of elements <= x in row i is: min(x // i, n)
            count += min(x // i, n)
        return count

    # Binary search on the value space (not the indices)
    low, high = 1, m * n
    while low < high:
        mid = (low + high) // 2
        # Count how many numbers are <= mid
        if countLessEqual(mid) < k:
            # Not enough elements ≤ mid, need to go higher
            low = mid + 1
        else:
            # Enough (or too many) elements ≤ mid, might be the answer, so go lower
            high = mid

    # When low == high, we've found the
    return low

print(findKthNumber(2, 3, 6))      # Expected: 6
print(findKthNumber(3, 3, 1))      # Expected: 1
print(findKthNumber(3, 3, 9))      # Expected: 9
print(findKthNumber(10, 10, 50))   # Expected: 24
print(findKthNumber(3, 3, 5))  # Expected Output: 3
