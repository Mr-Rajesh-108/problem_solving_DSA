class Solution:
    def findMajority(self, arr):
        n = len(arr)
        freq = {}
        res = []
        
        # Count the frequency of each element
        for element in arr:
            freq[element] = freq.get(element, 0) + 1

        # Check which elements occur more than n // 3 times
        for ele, cnt in freq.items():
            if cnt > n // 3:
                res.append(ele)

        # Return sorted result
        return sorted(res)


# optimized Boyer-Moore Voting Algorithm version

    def findMajorityOptimaized(self, arr):
        if not arr:
            return []

        # Step 1: Find up to two potential candidates
        count1, count2 = 0, 0
        candidate1, candidate2 = None, None

        for num in arr:
            # If the current number matches one of the candidates, increment the count
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            # If count1 is 0, assign candidate1 to current number
            elif count1 == 0:
                candidate1, count1 = num, 1
            # If count2 is 0, assign candidate2 to current number
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                # If current number is different from both candidates, decrement both counts
                count1 -= 1
                count2 -= 1

        # Step 2: Verify the candidates actually appear more than n // 3 times
        res = []
        for c in (candidate1, candidate2):
            if c is not None and arr.count(c) > len(arr) // 3:
                res.append(c)

        # Return the result sorted
        return sorted(res)

# Test cases
sol = Solution()
arr = [1, 2, 5, 4, 5, 6, 4, 5, 4, 5, 5, 3, 4, 5, 6, 3, 4, 5]

print(sol.findMajority([3, 2, 3]))            # Output: [3]
print(sol.findMajority([1, 1, 1, 3, 3, 2, 2, 2]))  # Output: [1, 2]
print(sol.findMajority([1]))                 # Output: [1]
print(sol.findMajority(arr))                 # Output: [5]
print(sol.findMajority([1, 2, 3, 4]))         # Output: []

print('optimized Boyer-Moore Voting Algorithm version')


print(sol.findMajorityOptimaized(arr))         # Output: [5]