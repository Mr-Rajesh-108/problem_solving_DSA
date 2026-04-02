class Solution:
    def is_palindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    def is_palindrome_brute_force(self, s: str) -> bool:
        filtered_s = ''.join(c.lower() for c in s if c.isalnum())
        return filtered_s == filtered_s[::-1]

    def is_palindrome_two_pointers(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True 
    
    
Sol = Solution()
print(Sol.is_palindrome("A man, a plan, a canal: Panama"))  # Output: True
print(Sol.is_palindrome("race a car"))  # Output: False 
print(Sol.is_palindrome_brute_force("A man, a plan, a canal: Panama"))  # Output: True
print(Sol.is_palindrome_brute_force("race a car"))  # Output: False
print(Sol.is_palindrome_two_pointers("A man, a plan, a canal: Panama"))  # Output: True
print(Sol.is_palindrome_two_pointers("race a car"))  # Output: False        