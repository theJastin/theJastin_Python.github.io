def plusOne(digits):
    for i in range(len(digits)-1, -1, -1):
        digits[i] +=1
        if digits[i] != 10:
            return digits
        else:
            digits[i] = 0
    return [1] + digits if digits[0] == 0 else digits

digits = [2,1,9,9,9,9]
print(plusOne(digits))