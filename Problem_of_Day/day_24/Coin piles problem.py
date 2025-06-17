from collections import Counter
import bisect

class Solution:
    def minCoinsToMakePilesWithinK(self, arr, k):
        arr.sort()
        freq = Counter(arr)
        unique_vals = sorted(freq)
        prefix_freq = [0]
        prefix_coins = [0]

        # Build prefix arrays
        for val in unique_vals:
            prefix_freq.append(prefix_freq[-1] + freq[val])
            prefix_coins.append(prefix_coins[-1] + freq[val] * val)

        total = sum(arr)
        result = float('inf')

        for i, h in enumerate(unique_vals):
            # Remove all elements less than h
            left_cost = prefix_coins[i]

            # Find upper bound index where value > h + k
            upper_idx = bisect.bisect_right(unique_vals, h + k)

            # Remove excess coins from piles > h + k
            right_freq = prefix_freq[-1] - prefix_freq[upper_idx]
            right_sum = prefix_coins[-1] - prefix_coins[upper_idx]
            right_cost = right_sum - right_freq * (h + k)

            total_cost = left_cost + right_cost
            result = min(result, total_cost)

        return result

arr = [1, 5, 1, 2, 5, 1]
k = 3
print(Solution().minCoinsToMakePilesWithinK(arr,k))