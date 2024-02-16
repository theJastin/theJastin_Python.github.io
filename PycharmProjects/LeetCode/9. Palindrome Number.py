def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    sx = str(x)
    n = len(sx)

    i = 0
    j = n-1
    result = True
    while j > i:
        if sx[i] != sx[j]:
            result = False
        i+=1
        j-=1
    return result

x = 122334433221
print(isPalindrome(x))