def twoSum(nums, target):
    n = len(nums)

    for i in range(n):
        for j in range(i+1, n):
            if (nums[i] + nums[j] == target):
                return [i,j]

nums = [2,5,5,11]
target = 10
print(twoSum(nums,target))