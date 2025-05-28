def has_rectangle_with_ones(mat):
    if not mat or not mat[0]:
        return False

    rows = len(mat)
    cols = len(mat[0])
    seen_pairs = set()

    for i in range(rows):
        ones = [j for j in range(cols) if mat[i][j] == 1]

        # Check all pairs of 1s in the current row
        for x in range(len(ones)):
            for y in range(x + 1, len(ones)):
                pair = (ones[x], ones[y])
                if pair in seen_pairs:
                    return True
                seen_pairs.add(pair)

    return False

mat1 = [
    [1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0], 
    [1, 0, 1, 0, 1]
]
mat2 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

print(has_rectangle_with_ones(mat1))  # Output: True
print(has_rectangle_with_ones(mat2))  # Output: False
