# 69. Sqrt(x) solution
# Binary Search Algorithm
def mySqrt(x):
    low = 0
    high = 65536
    mid = high//2
    while (low < high):
        ll = list[mid-1]
        if ll == x:
            return mid
        elif x < ll:
            high = mid
            mid = (high- low)//2
        elif x > ll:
            low = mid
            mid = low + (high - low)//2
        if mid == low or mid == high or mid == 0:
            return low

x = 2147395599
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