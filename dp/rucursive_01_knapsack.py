def knapsack_01(wt, value, capacity, n):
    # Base case: no items or no capacity
    if n == 0 or capacity == 0:
        return 0

    # If the weight of the nth item is less than or equal to the capacity
    if wt[n - 1] <= capacity: # If we include the nth item, we add its value and reduce the capacity by its weight
    
        return max(value[n - 1] + knapsack_01(wt, value, capacity - wt[n - 1], n - 1),
                   knapsack_01(wt, value, capacity, n - 1))
    else:
        # If the weight of the nth item is greater than the capacity, we cannot include it, so we move to the next item
        return knapsack_01(wt, value, capacity, n - 1)
    
    
wt = [7, 3, 4, 5]
value = [24, 21, 12, 10]
capacity = 7
n = len(wt)
# The expected output is 24 (only the first item can be included)
print("Maximum value in Knapsack =", knapsack_01(wt, value, capacity, n))
