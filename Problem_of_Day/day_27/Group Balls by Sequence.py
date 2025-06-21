from collections import Counter

class Solution:
    def canGroupBalls(self, arr, k):
        n = len(arr)
        if n % k != 0:
            return False

        count = Counter(arr)
        for num in sorted(count):
            if count[num] > 0:
                freq = count[num]
                # Try forming a group starting from num
                for i in range(num, num + k):
                    if count[i] < freq:
                        return False
                    count[i] -= freq
        return True
sol=Solution()
print(sol.canGroupBalls([10,1,2,11],2))