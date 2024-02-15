# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    dictionary = {
        "I":"1",
        "V":"5",
        "X":"10",
        "L":"50",
        "C":"100",
        "D":"500",
        "M":"1000"
    }

    result = 0
    i = 0
    while i < len(s):
        if i != len(s)-1:
            if s[i] == "I" and (s[i+1] == "V" or s[i+1] == "X"):
                if s[i+1] == "V":
                    result += 4
                elif s[i+1] == "X":
                    result += 9
                i+=2
            elif s[i] == "X" and (s[i+1] == "L" or s[i+1] == "C"):
                if s[i+1] == "L":
                    result += 40
                elif s[i+1] == "C":
                    result += 90
                i+= 2
            elif s[i] == "C" and (s[i+1] == "D" or s[i+1] == "M"):
                if s[i+1] == "D":
                    result += 400
                elif s[i+1] == "M":
                    result += 900
                i+=2
            else:
                result += int(dictionary[s[i]])
                i+=1
        else:
            result += int(dictionary[s[i]])
    return result
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.

print(romanToInt("IIIX"))