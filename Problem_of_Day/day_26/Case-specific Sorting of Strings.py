# Case-specific Sorting of Strings
class Solution:
    def caseSort(self, s: str) -> str:
        upper = sorted([ch for ch in s if ch.isupper()])
        lower = sorted([ch for ch in s if ch.islower()])

        result = []
        u = l = 0

        for ch in s:
            if ch.isupper():
                result.append(upper[u])
                u += 1
            else:
                result.append(lower[l])
                l += 1

        return ''.join(result)
sol = Solution()
print(sol.caseSort("GEekS"))    # Output: EGekS
print(sol.caseSort("XWMSPQ"))   # Output: MPQSWX
print(sol.caseSort("abcXYZ"))   # Output: abcXYZ
