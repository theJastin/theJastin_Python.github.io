# 70. Climbing Stairs solution

def climbStairs(n,map):
    # map to memorise already calculated results to reduce time complexity
    if n in map:
        return map[n]
    map[n] = climbStairs(n-2,map) + climbStairs(n-1,map)
    return map[n]

n = 45
print(climbStairs(n, {0:1, 1:1}))

# problem
"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 
Constraints:
1 <= n <= 45
"""