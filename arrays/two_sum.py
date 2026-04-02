from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # Dictionary to store the indices of the numbers we've seen so far
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in seen:
                return [seen[needed],i]

            seen[nums[i]]=i
            


    def two_sum_brute_force(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
                
                
    def two_sum_pointer(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        nums = sorted(nums) # Sort the list to use two pointers
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                return [left, right]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []
            
                
# Example usage:
list1 = [2, 12, 3, 4, 51, 7, 11, 15]
target1 = 9
sol = Solution()
print(sol.twoSum(list1, target1))  # Output: [0, 1]
print(sol.two_sum_brute_force(list1, target1))  # Output: [0, 1]
print(sol.two_sum_pointer(list1, target1))  # Output: [0, 1]