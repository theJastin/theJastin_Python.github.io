def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
        else:
            nums[i] = None
    return k

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(nums, val))