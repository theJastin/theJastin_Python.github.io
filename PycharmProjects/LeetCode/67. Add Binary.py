# 0 + 0 = 0, carry 0
# 1 + 0 = 1, carry 0
# 0 + 1 = 1, carry 0
# 1 + 1 = 0, carry 1
def addBinary(a, b):
    result = ""
    # carry - carrying the one
    carry = 0
    # def the shortest string and longest string
    # aa - longest
    # bb - shortest
    if len(a) > len(b):
        aa = a[::-1]
        bb = b[::-1]
    else:
       aa = b[::-1]
       bb = a[::-1]

    for i in range(len(aa)):
        if i < (len(bb)):
            if carry == 0:
                if aa[i] == bb[i] == '0':
                    result = '0' + result
                elif aa[i] == bb[i] == '1':
                    result = '0' + result
                    carry = 1
                else:
                    result = '1' + result
            else:
                if aa[i] == bb[i] == '0':
                    result = '1' + result
                    carry = 0
                elif aa[i] == bb[i] == '1':
                    result = '1' + result
                    carry = 1
                else:
                    result = '0' + result
                    carry = 1
        else:
            if aa[i] == str(carry) == '0':
                result = '0' + result
            elif aa[i] == str(carry) == '1':
                result = '0' + result
                carry = 1
            else:
                result = '1' + result
                carry = 0
    if carry == 1:
        result = '1' + result
    return result


# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

# a = "110010"
# b = "10111"
# Expected = "1001001"

a = "110010"
b = "10111"
print(addBinary(a, b))