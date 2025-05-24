class Solution:
    def minDeletions(self, s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for cl in range(2, n + 1):
            for i in range(n - cl + 1):
                j = i + cl - 1
                if s[i] == s[j] and cl == 2:
                    dp[i][j] = 2
                elif s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

        return n - dp[0][n - 1]  # This returns min deletions directly

# Example usage:
sol = Solution()
s = "abcda"
print(sol.minDeletions(s))  # Output: number of deletions to make it a palindrome
