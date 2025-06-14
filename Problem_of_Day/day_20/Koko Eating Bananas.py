import math

class Solution:
    def minEatingSpeed(self, arr, k):
        low, high = 1, max(arr)
        result = high

        while low <= high:
            mid = (low + high) // 2

            hours = sum(math.ceil(pile / mid) for pile in arr)

            if hours <= k:
                result = mid  # try smaller s
                high = mid - 1
            else:
                low = mid + 1

        return result

s = Solution()

print(s.minEatingSpeed([5, 10, 3], 4))         # Output: 5
print(s.minEatingSpeed([5, 10, 15, 20], 7))    # Output: 10
print(s.minEatingSpeed([30, 11, 23, 4, 20], 5))  # Output: 30
print(s.minEatingSpeed([30, 11, 23, 4, 20], 6))  # Output: 23
