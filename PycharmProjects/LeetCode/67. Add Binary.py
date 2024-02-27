# 0 + 0 = 0, carry 0
# 1 + 0 = 1, carry 0
# 0 + 1 = 1, carry 0
# 1 + 1 = 0, carry 1
def addBinary(a, b):
    result = ""
    sum = 0
    # carry - carrying the one
    carry = 0
    if len(a) > len(b):
        bb = b.zfill(len(a))
        aa = a
    else:
        aa = a.zfill(len(b))
        bb = b
    for i in range(len(aa)-1, -1, -1):
        sum = carry + int(aa[i]) + int(bb[i])
        if sum > 1:
            if sum == 2:
                result += '0'
                carry = 1
            else:
                result += '1'
                carry = 1
        else:
            result += str(sum)
            carry = 0
    if carry == 1:
        result += '1'
    return result[::-1]

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

# a = "110010"
# b = "10111"
# Expected = "1001001"

a = "1010"
b = "1011"
print(addBinary(a, b))