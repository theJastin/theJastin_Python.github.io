def longestCommonPrefix(strs):
    match = False
    commonstr = ""
    i = 0
    j = 0
    while i < len(strs[0]):
        j = 0
        while j < len(strs):
            if len(strs[j]) > i:
                v = strs[j][i]
                if v == strs[0][i]:
                    j += 1
                    match = True
                else:
                    match = False
                    break
            else:
                match = False
                break
        if match == True:
            i += 1
        else:
            break

    if (i == 0 and match == False):
        return ""
    elif (i == 0 and match == True):
        return strs[0][0]
    elif i > 0:
        return strs[0][0:i]


strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))