def twoSum(nums, target):
    d = {}
    for index, value in enumerate(nums):
        key = target - value
        if key in d:
            print(d[key])
            return [d[key], index]
        d[value] = index
        print(index)
        print(value)
        print(key)
        print("_____")

# Input: nums = [2,7,11,15], target = 9
nums = [2,11,15,7]
target = 9
result = twoSum(nums, target)
print(result)

c = [2,11,15,7]
for a,b in enumerate(c):
    if b == 7:
        print("found")
    print("not found")
