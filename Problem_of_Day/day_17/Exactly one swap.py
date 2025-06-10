from collections import Counter

class Solution:
    def countStrings(self, s):
        n = len(s)

        total = n * (n - 1) // 2  # All (i, j) where i < j
        freq = Counter(s)
        identical_swaps = sum((f * (f - 1)) // 2 for f in freq.values())

        result = total - (identical_swaps - 1 if identical_swaps else 0)

        return result if result > 0 else 1



s = "geek"
print(Solution().countStrings(s))  # Output: 6

s = "aaaa"
print(Solution().countStrings(s))  # Output: 1
