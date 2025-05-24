def sum_of_substrings(s):
    total_sum = 0
    prev = 0
    for i in range(len(s)):
        num = int(s[i])
        curr = prev * 10 + num * (i + 1)
        total_sum += curr
        prev = curr
    return total_sum

print(sum_of_substrings('6759'))
print(sum_of_substrings('421'))