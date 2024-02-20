def findNumber(arr, k):
    for num in arr:
        if num == k:
            return "YES"
    return "NO"


arr = [3,2,1]
k = 3
print(findNumber(arr, k))
