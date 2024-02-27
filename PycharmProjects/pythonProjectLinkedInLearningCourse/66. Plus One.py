def plusOne(input):
    # i - index of element in the input list
    i = len(input) - 1
    # num - value of element in the input list
    num = input[i]
    # c - carrying the one
    c = 0

    if input[i] != 9:
        input[i] += 1
    else:
        c = 1
        while c == 1:
            input[i] = 0
            if i > 0:
                if input[i-1] != 9:
                    input[i-1] = input[i-1] + 1
                    c = 0
                else:
                    i -= 1
            else:
                input.insert(0, 1)
                c = 0

    return input

input = [2,1,9,9,9,9]
print(plusOne(input))