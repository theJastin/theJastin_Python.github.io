def isValid(s):
    # dictionary = {"(":0, ")":0, "[":0, "]":0, "{":0, "}":0}
    list = []
    dictionary = {")":"(", "]":"[", "}":"{"}
    for char in s:
        if char in ["(", "[", "{"]:
            list.append(char)
        else:
            if len(list) > 0:
                v = list.pop()
                if v != dictionary[char]:
                    return False
            else:
                return False
    return len(list) == 0

s = "([]){}"
print(isValid(s))