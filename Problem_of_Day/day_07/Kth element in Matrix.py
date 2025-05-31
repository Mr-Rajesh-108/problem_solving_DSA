class Solution:
    def kthSmallest(self, mat, k):
        n = len(mat)

        def count_less_equal(mid):
            count = 0
            i, j = n - 1, 0
            while i >= 0 and j < n:
                if mat[i][j] <= mid:
                    count += i + 1
                    j += 1
                else:
                    i -= 1
            return count

        low = mat[0][0]
        high = mat[n - 1][n - 1]

        while low < high:
            mid = (low + high) // 2
            if count_less_equal(mid) < k:
                low = mid + 1
            else:
                high = mid

        return low

sol=Solution()

mat1 = [[16, 28, 60, 64], [22, 41, 63, 91], [27, 50, 87, 93], [36, 78, 87, 94]]
print(sol.kthSmallest(mat1, 3))  # Output: 27

mat2 = [[10, 20, 30, 40], [15, 25, 35, 45], [24, 29, 37, 48], [32, 33, 39, 50]]
print(sol.kthSmallest(mat2, 7))  # Output: 30
