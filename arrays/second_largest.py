def second_largest(arr):
    if len(arr) < 2:
        return None  # Not enough elements

    first_largest = float('-inf')
    second_largest = float('-inf')

    for element in arr:
        if element > first_largest:
            second_largest = first_largest
            first_largest = element
        elif first_largest > element > second_largest:
            second_largest = element

    return None if second_largest == float('-inf') else second_largest

arr = [12, 35, 1, 10, 34, 1]
#output = 34
print(second_largest(arr))