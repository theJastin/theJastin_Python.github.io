# use 2 pointers to iterate the array
# i - step number in loop
# j - index of unique number in the array
def removeDuplicates(nums):
    j = 0
    for i in range(1, len(nums)):
        # element j not equal element of i
        # move j one step up
        # update array of unique number with new element
        if nums[j] != nums[i]:
            j += 1
            nums[j] = nums[i]

    k = j+1
    return nums

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))