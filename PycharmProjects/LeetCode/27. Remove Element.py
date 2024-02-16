def removeElement(nums, val):
    j = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
        else:
            nums[i] = None
    k = j
    return nums

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(nums, val))