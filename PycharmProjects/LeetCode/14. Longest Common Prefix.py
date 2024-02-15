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
    # if (i > 0):
    #     return first[0:i]
    # elif (i == 0 and match == True):
    #     return first[0]
    # else:
    #     return ""
    return first[i]
    # match = False
    # commonstr = ""
    # i = 0
    # j = 0
    # while i < len(strs[0]):
    #     j = 0
    #     while j < len(strs):
    #         if len(strs[j]) > i:
    #             v = strs[j][i]
    #             if v == strs[0][i]:
    #                 j += 1
    #                 match = True
    #             else:
    #                 match = False
    #                 break
    #         else:
    #             match = False
    #             break
    #     if match == True:
    #         i += 1
    #     else:
    #         break
    #
    # if (i == 0 and match == False):
    #     return ""
    # elif (i == 0 and match == True):
    #     return strs[0][0]
    # elif i > 0:
    #     return strs[0][0:i]


strs = ["a"]
print(longestCommonPrefix(strs))