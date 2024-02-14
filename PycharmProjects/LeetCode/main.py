def twoSum(nums, target):
    n = len(nums)
    List = []

    for i in range(n):
        if (nums[i] + nums[i + 1] == target):
            List.append(i)
            List.append(i + 1)
            return List

nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))