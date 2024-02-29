# 14. Longest Common Prefix solution
def longestCommonPrefix(strs):
    # sort strs lexicographic
    strs.sort()
    min_len = min(len(s) for s in strs)
    common_prefix = ""
    for i in range(min_len):
        current_char = strs[0][i]
        for s in strs:
            if s[i] != current_char:
                return common_prefix
        common_prefix += current_char
    return common_prefix

strs = ["a"]
print(longestCommonPrefix(strs))

# problem
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
