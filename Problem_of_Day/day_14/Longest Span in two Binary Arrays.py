def longest_common_span(a1, a2):
    n = len(a1)
    # Create a difference array
    diff = [a1[i] - a2[i] for i in range(n)]

    # Dictionary to store prefix sums
    prefix_sum_map = {}
    max_len = 0
    prefix_sum = 0

    for i in range(n):
        prefix_sum += diff[i]

        if prefix_sum == 0:
            max_len = i + 1
        elif prefix_sum in prefix_sum_map:
            max_len = max(max_len, i - prefix_sum_map[prefix_sum])
        else:
            prefix_sum_map[prefix_sum] = i

    return max_len

# Example usage:
a1 = [0, 1, 0, 0, 0, 0]
a2 = [1, 0, 1, 0, 0, 1]
print(longest_common_span(a1, a2))  # Output: 4

a1 = [0, 1, 0, 1, 1, 1, 1]
a2 = [1, 1, 1, 1, 1, 0, 1]
print(longest_common_span(a1, a2))  # Output: 6
