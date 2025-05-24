def maxSubArraySum(arr):
    maxSub= arr[0]
    res= arr[0]
    for i in range(1,len(arr)):
        maxSub= max(maxSub+arr[i],arr[i])
        res=max(maxSub,res)
    return res


print(maxSubArraySum([2, 3, -8, 7, -1, 2, 3]))
arr=[-2,-4]
print(maxSubArraySum(arr))