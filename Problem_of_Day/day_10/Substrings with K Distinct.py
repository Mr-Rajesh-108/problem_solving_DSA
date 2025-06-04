from collections import defaultdict

def substrings_with_k_distinct(s: str, k: int) -> int:
    def at_most_k_distinct(s, k):
        count = defaultdict(int)
        left = 0
        result = 0
        for right in range(len(s)):
            count[s[right]] += 1
            while len(count) > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
            result += right - left + 1
        return result

    return at_most_k_distinct(s, k) - at_most_k_distinct(s, k - 1)

# Examples
print(substrings_with_k_distinct("abc", 2))  # Output: 2
print(substrings_with_k_distinct("aba", 2))  # Output: 3
print(substrings_with_k_distinct("aa", 1))   # Output: 3
