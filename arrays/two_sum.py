from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in seen:
                return [seen[needed],i]

            seen[nums[i]]=i


# Example usage:
sol = Solution()
print(sol.twoSum([2,7,11,15],9))  # Output: [0, 1]