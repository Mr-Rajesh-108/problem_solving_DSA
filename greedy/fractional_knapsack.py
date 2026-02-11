def fractional_knapsack(items_wt, price, capacity):
    n = len(items_wt)
    items = [(price[i] / items_wt[i], items_wt[i], price[i]) for i in range(n)]
    

    # Sort items based on price-to-weight ratio in descending order

    # items.sort(key=lambda x: x[0], reverse=True)

    for i in range(n):
        for j in range(i+1, n):
            if items[i][0] < items[j][0]:
                items[i], items[j] = items[j], items[i]
    
    # Initialize total profit
    total_profit = 0.0
    for pricePerKg, wt, price in items:
        if capacity >= wt:
            total_profit += price
            capacity -= wt
        else:
            total_profit += pricePerKg * capacity
            capacity = 0
            break
    return total_profit

items_wt = [7, 3, 4, 5]
price = [24, 21, 12, 10]
capacity = 20
# The expected output is 60.0 (24 + 21 + 12 + 3.0)
print("Total profit: ", fractional_knapsack(items_wt, price, capacity)) 
print("Total profit: ", fractional_knapsack([7,4,6,5,6], [21,24,12,40,30], 20)) 
