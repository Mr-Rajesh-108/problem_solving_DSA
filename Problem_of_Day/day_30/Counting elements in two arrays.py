class Solution:
    def binary_search_right(self, arr, target):
        left = 0
        right = len(arr)
        
        while left < right:
            mid = (left + right) // 2
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid
        
        return left  # Number of elements <= target

    def countLessEq(self, a, b):
        # Step 1: Sort b using built-in sort (O(n log n))
        b.sort()

        # Step 2: For each a[i], find count of elements <= a[i] in b[]
        result = []
        for num in a:
            count = self.binary_search_right(b, num)
            result.append(count)
        
        return result


a = [4, 8, 7, 5, 1]
b = [4, 48, 3, 0, 1, 1, 5]

sol = Solution()
print(sol.countLessEq(a, b))  # Output: [5, 6, 6, 6, 3]
