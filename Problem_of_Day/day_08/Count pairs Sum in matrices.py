def count_pairs_sum(mat1, mat2, x):
    n = len(mat1)
    
    # Flatten mat2 into a set for quick lookup
    elements_mat2 = set()
    for row in mat2:
        for val in row:
            elements_mat2.add(val)

    # Count pairs
    count = 0
    for row in mat1:
        for val in row:
            if (x - val) in elements_mat2:
                count += 1
    
    return count

# Example 1
n = 3
x = 21
mat1 = [[1, 5, 6], [8, 10, 11], [15, 16, 18]]
mat2 = [[2, 4, 7], [9, 10, 12], [13, 16, 20]]
print("Output:", count_pairs_sum(mat1, mat2, x))  # Output: 4

# Example 2
n = 2
x = 10
mat1 = [[1, 2], [3, 4]]
mat2 = [[4, 5], [6, 7]]
print("Output:", count_pairs_sum(mat1, mat2, x))  # Output: 2
