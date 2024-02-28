# 20. Valid Parentheses solution
def isValid(s):
    # dictionary = {"(":0, ")":0, "[":0, "]":0, "{":0, "}":0}
    list = []
    dictionary = {")":"(", "]":"[", "}":"{"}
    for char in s:
        if char in ["(", "[", "{"]:
            list.append(char)
        else:
            if len(list) > 0:
                v = list.pop()
                if v != dictionary[char]:
                    return False
            else:
                return False
    return len(list) == 0

s = "([]){}"
print(isValid(s))

# problem
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
 
Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
