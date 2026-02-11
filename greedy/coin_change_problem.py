def coin_change(coinsArr, amount):
    # Sort the coins in descending order to try larger denominations first
    coinsArr.sort(reverse=True)
    
    count = 0
    for coin in coinsArr:
        while amount >= coin:
            amount -= coin
            count += 1
            
    return count if amount == 0 else -1

print(coin_change([1, 2, 5], 11))  # Output: 3 (11 = 5 + 5 + 1)
print(coin_change([2], 3))          # Output: -1 (not possible  
print(coin_change([1,2,5,10,50,20,500,100],1024)) # Output: 5 (1024 = 500 + 500 + 20 + 2 + 2)


