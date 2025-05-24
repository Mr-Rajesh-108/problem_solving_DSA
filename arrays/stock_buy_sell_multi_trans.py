def maxProfit(arr):
    maxProfit= 0
    for i in range(1, len(arr)):
        if arr[i-1]< arr[i]:
            maxProfit+= arr[i]-arr[i-1]
    return maxProfit

prices=[100, 180, 260, 310, 40, 535, 695]
print(maxProfit(prices))