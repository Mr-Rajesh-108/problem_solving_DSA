def lcs_of_three(s1, s2, s3):
    len1, len2, len3 = len(s1), len(s2), len(s3)

    # Create a 3D DP table initialized with 0s
    dp = [[[0] * (len3 + 1) for _ in range(len2 + 1)] for __ in range(len1 + 1)]

    # Fill the DP table
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            for k in range(1, len3 + 1):
                if s1[i - 1] == s2[j - 1] == s3[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(
                        dp[i - 1][j][k],
                        dp[i][j - 1][k],
                        dp[i][j][k - 1]
                    )

    return dp[len1][len2][len3]

# Example test cases
print(lcs_of_three("geeks", "geeksfor", "geeksforgeeks"))  # Output: 5
print(lcs_of_three("abcd1e2", "bc12ea", "bd1ea"))           # Output: 3
