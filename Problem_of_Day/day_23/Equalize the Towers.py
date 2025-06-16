class Solution:
    def minCostToEqualize(self, heights, cost):
        def compute_total_cost(target_height):
            return sum(abs(h - target_height) * c for h, c in zip(heights, cost))
        
        low = min(heights)
        high = max(heights)
        result = compute_total_cost(heights[0])
        
        while low <= high:
            mid = (low + high) // 2
            cost_mid = compute_total_cost(mid)
            cost_mid_plus = compute_total_cost(mid + 1)
            
            result = min(result, cost_mid, cost_mid_plus)
            
            if cost_mid < cost_mid_plus:
                high = mid - 1
            else:
                low = mid + 1
        
        return result
    
heights = [1, 2, 3]
cost = [10, 100, 1000]
s=Solution()
print(s.minCostToEqualize(heights,cost))

