#User function Template for python3
class Solution:
    def findLength(self, color, radius):
        stack = []

        for c, r in zip(color, radius):
            if stack and stack[-1] == (c, r):
                stack.pop()  # Remove matching pair
            else:
                stack.append((c, r))  # Add current ball

        return len(stack)

print(Solution().findLength([2, 3, 5], [3, 3, 5]))   # Output: 3
print(Solution().findLength([2, 2, 5], [3, 3, 5]))   # Output: 1
print(Solution().findLength([1, 1, 1, 1], [2, 2, 2, 2]))  # Output: 0
print(Solution().findLength([1, 2, 2, 1], [1, 2, 2, 1]))  # Output: 0
print(Solution().findLength([1], [1]))   # Output: 1
