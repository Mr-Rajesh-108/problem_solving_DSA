class Solution:
    def findKClosest(self, arr, k, x):
        # Exclude x from arr
        arr = [a for a in arr if a != x]

        # Sort by closeness: smaller |a - x| comes first, if tie -> larger a comes first
        arr.sort(key=lambda a: (abs(a - x), -a))

        # Get first k elements
        result = arr[:k]
        return result
s = Solution()

print(s.findKClosest([1, 3, 4, 10, 12], 2, 4))  # Output: [3, 1]
print(s.findKClosest([12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56], 4, 35))
# Output: [39, 30, 42, 45]
print(s.findKClosest([2, 5, 8, 9, 12], 3, 10))  # Output: [9, 12, 8]
