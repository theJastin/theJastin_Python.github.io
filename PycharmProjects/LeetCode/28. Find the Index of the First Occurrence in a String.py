def strStr(haystack, needle):
    needle_len = len(needle)
    for i in range(len(haystack)):
        if haystack[i:i+needle_len] == needle:
            return i
    return -1
# haystack = "sadbutsad"
# needle = "sad" # output = 0
# haystack = "leetcode"
# needle = "leeto" # output = -1
haystack = "a"
needle = "a"
print(strStr(haystack, needle))