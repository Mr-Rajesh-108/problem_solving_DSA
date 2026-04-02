
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans=""
        strs=sorted(strs) # Sort the strings
        # print(strs)
        first=strs[0]
        last=strs[-1]
        for i in range(min(len(first),len(last))): # Iterate through the characters of the first and last strings
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 
    
strs=["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))

strs=["dog","racecar","car"]
print(Solution().longestCommonPrefix(strs))


