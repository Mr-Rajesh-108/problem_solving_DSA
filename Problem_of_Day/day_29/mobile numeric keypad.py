def get_count(n):
    if n <= 0:
        return 0
    if n == 1:
        return 10

    # Valid moves from each key
    neighbors = {
        0: [0, 8],
        1: [1, 2, 4],
        2: [2, 1, 3, 5],
        3: [3, 2, 6],
        4: [4, 1, 5, 7],
        5: [5, 2, 4, 6, 8],
        6: [6, 3, 5, 9],
        7: [7, 4, 8],
        8: [8, 5, 7, 9, 0],
        9: [9, 6, 8]
    }

    # Initialize dp table: dp[i][j] means count of numbers of length i ending with digit j
    dp = [[0 for _ in range(10)] for _ in range(n + 1)]

    # Base case: length 1, each digit appears once
    for i in range(10):
        dp[1][i] = 1

    # Fill dp table
    for i in range(2, n + 1):
        for digit in range(10):
            for nei in neighbors[digit]:
                dp[i][digit] += dp[i - 1][nei]

    # Total sequences of length n
    return sum(dp[n][i] for i in range(10))

# Example usage:
print(get_count(1))  # Output: 10
print(get_count(2))  # Output: 36
