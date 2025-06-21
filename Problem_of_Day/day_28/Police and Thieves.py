from collections import deque

class Solution:
    def catchThieves(self, arr, k):
        police = deque()
        thieves = deque()
        count = 0

        for i in range(len(arr)):
            if arr[i] == 'P':
                police.append(i)
            elif arr[i] == 'T':
                thieves.append(i)

        while police and thieves:
            if abs(police[0] - thieves[0]) <= k:
                count += 1
                police.popleft()
                thieves.popleft()
            elif thieves[0] < police[0]:
                thieves.popleft()
            else:
                police.popleft()

        return count

sol=Solution()
arr = ['P', 'T', 'T', 'P', 'T']
k = 1
# Expected Output: 2
# Explanation: P[0] ↔ T[1], P[3] ↔ T[2]
print(sol.catchThieves(arr,k))