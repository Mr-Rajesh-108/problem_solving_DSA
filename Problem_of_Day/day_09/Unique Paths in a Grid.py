def unique_paths(grid):
    n = len(grid)
    m = len(grid[0])
    
    # If start or end is blocked
    if grid[0][0] == 1 or grid[n-1][m-1] == 1:
        return 0

    # Initialize dp table with all zeros
    dp = [[0 for _ in range(m)] for _ in range(n)]

    # Starting point
    dp[0][0] = 1

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                dp[i][j] = 0
            else:
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]

    return dp[n-1][m-1]


# Example 1
grid1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(unique_paths(grid1))  # Output: 2

# Example 2
grid2 = [[1, 0, 1]]
print(unique_paths(grid2))  # Output: 0
