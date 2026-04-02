class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
    
    def removeDuplicatesBruteForce(self, nums: list[int]) -> int:
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
    
    def removeDuplicatesTwoPointers(self, nums: list[int]) -> int:
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
    
    def removeDuplicatesHashMap(self, nums: list[int]) -> int:
        if not nums:
            return 0
        seen = set()
        i = 0
        for j in range(len(nums)):
            if nums[j] not in seen:
                seen.add(nums[j])
                nums[i] = nums[j]
                i += 1
        return i
    
    
# example usage:
sol = Solution()
print(sol.removeDuplicates([1,1,2]))  # Output: 2
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))  # Output: 5
print(sol.removeDuplicatesBruteForce([1,1,2]))  # Output: 2
print(sol.removeDuplicatesBruteForce([0,0,1,1,1,2,2,3,3,4]))  # Output: 5
print(sol.removeDuplicatesTwoPointers([1,1,2]))  # Output: 2
print(sol.removeDuplicatesTwoPointers([0,0,1,1,1,2,2,3,3,4]))  # Output: 5
print(sol.removeDuplicatesHashMap([1,1,2]))  # Output: 2
print(sol.removeDuplicatesHashMap([0,0,1,1,1,2,2,3,3,4]))  # Output: 5
