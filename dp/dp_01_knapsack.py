def dp_01_knapsack( wt, value, capacity):
    n = len(wt)
    # dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if wt[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - wt[i - 1]] + value[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]


    return dp[n][capacity]

wt = [7, 3, 4, 5]
value = [24, 21, 12, 10]
capacity = 7

print("Maximum value in Knapsack =", dp_01_knapsack(wt, value, capacity))


print("Maximum value in Knapsack =", dp_01_knapsack([2,3,4,5], [3,4,5,6], 5))
