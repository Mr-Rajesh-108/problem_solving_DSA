class Solution:
    def allPalindromicPerms(self, s):
        res = []

        def isPalindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                part = s[start:end]
                if isPalindrome(part):
                    path.append(part)
                    backtrack(end, path)
                    path.pop()  # backtrack

        backtrack(0, [])
        return res

sol = Solution()
print(sol.allPalindromicPerms("geeks"))
# Output: [['g', 'e', 'e', 'k', 's'], ['g', 'ee', 'k', 's']]

print(sol.allPalindromicPerms("abcba"))
# Output: [['a', 'b', 'c', 'b', 'a'], ['a', 'bcb', 'a'], ['abcba']]

str=input("Enter the a String to check the Str are palidrome on each posible Sub Str: ")
print("Entered Str: ",str)
print(sol.allPalindromicPerms(str))
