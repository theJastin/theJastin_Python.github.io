# 9. Palindrome Number solution
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

# problem
"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
-231 <= x <= 231 - 1
"""
