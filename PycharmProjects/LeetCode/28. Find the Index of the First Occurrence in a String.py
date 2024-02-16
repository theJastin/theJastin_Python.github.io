def strStr(haystack, needle):
    return haystack.find(needle)

# haystack = "sadbutsad"
# needle = "sad" # output = 0
haystack = "leetcode"
needle = "leeto" # output = -1
print(strStr(haystack, needle))