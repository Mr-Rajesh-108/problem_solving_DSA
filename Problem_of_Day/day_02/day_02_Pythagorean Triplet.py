def has_pythagorean_triplet(arr):
    n = len(arr)
    # Square all elements
    squares = [x * x for x in arr]
    # Sort the squares to use the two-pointer technique
    squares.sort()

    # Try every element as the largest element of a^2 + b^2 = c^2
    for i in range(n - 1, 1, -1):
        c2 = squares[i]
        left = 0
        right = i - 1
        while left < right:
            if squares[left] + squares[right] == c2:
                return True
            elif squares[left] + squares[right] < c2:
                left += 1
            else:
                right -= 1
    return False
print(has_pythagorean_triplet([3, 2, 4, 6, 5]))  # True
print(has_pythagorean_triplet([3, 8, 5]))        # False
print(has_pythagorean_triplet([1, 1, 1]))        # False

# Optimized Code
def pythagoreanTriplet(arr):
        squares = set(x * x for x in arr)
        n = len(arr)

        # Try all pairs (a, b) and check if a^2 + b^2 exists in the set
        for i in range(n):
            for j in range(i + 1, n):
                a2_b2 = arr[i]**2 + arr[j]**2
                if a2_b2 in squares:
                    return True
                
        return False
arr=[14, 17, 4, 4, 1, 9, 25, 12, 4, 9, 18, 15, 12, 2, 3, 13, 16, 17, 15, 6, 5, 20, 14, 8]
arr1=[3, 2, 4, 6, 5]
arr2=[3,8,5]
arr3=[1,1,1]
print(pythagoreanTriplet(arr))
print(pythagoreanTriplet(arr1))
print(pythagoreanTriplet(arr2))
print(pythagoreanTriplet(arr3))