# 100. Same Tree
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):
    same = False
    if p is None and q is None:
        return True
    if (p is None and q is not None) or (p is not None and q is None):
        return False
    same = isSameTree(p.left, q.left)
    if not same:
        return False
    same = True if p.val == q.val else False
    if not same:
        return same
    same = isSameTree(p.right, q.right)
    return same

# p = [1,2,3], q = [1,2,3]
p2 = TreeNode(-5)
# p3 = TreeNode(3)
ppp = TreeNode(0, p2, None)

q2 = TreeNode(-8)
# q3 = TreeNode(3)
qqq = TreeNode(0, q2, None)

print(isSameTree(ppp,qqq))
"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:
The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
"""