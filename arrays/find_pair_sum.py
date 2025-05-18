def has_pair_with_sum(arr, target_sum):
    seen = set()
    for num in arr:
        complement = target_sum - num
        if complement in seen:
            return True
        seen.add(num)
    return False

arr1 = [1, -2, 1, 0, 5, -1]
arr2 = [2, 7, 11, 15]
target = 0

# Call the function with two different arrays
print(has_pair_with_sum(arr1, target))  # Output: True (1 + -1 = 0)
print(has_pair_with_sum(arr2, target))  # Output: False (no two numbers sum to 0)

# print(has_pair_with_sum([1,2,3,5,6,7,8,4],11))