import math

class Solution:
    def smallestDivisor(self, arr, k):
        def compute_sum(divisor):
            return sum(math.ceil(x / divisor) for x in arr)
        
        low, high = 1, max(arr)
        answer = high
        
        while low <= high:
            mid = (low + high) // 2
            total = compute_sum(mid)
            
            if total <= k:
                answer = mid  # possible answer, try smaller
                high = mid - 1
            else:
                low = mid + 1
        
        return answer
s = Solution()
print(s.smallestDivisor([1, 2, 5, 9], 6))  # Output: 5
print(s.smallestDivisor([1, 1, 1, 1], 4))  # Output: 1
