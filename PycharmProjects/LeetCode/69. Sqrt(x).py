# 69. Sqrt(x) solution
def mySqrt(x):
    i = 1
    remainder = x
    while remainder != 0:
        remainder = x-i*i
        if remainder < 0:
            return i-1
        i +=1
    return i-1

x = 225
print(mySqrt(x))

# problem
"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 
Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
"""