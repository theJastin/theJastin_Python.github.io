# 94. Binary Tree Inorder Traversal solution
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # def insert(self, val):
    #     if self is not None:
    #         # add node to the left side
    #         if val < self.val:
    #             if self.left is None:
    #                 self.left = TreeNode(val)
    #             else:
    #                 self.left.insert(val)
    #         # add node to the right side
    #         elif val > self.val:
    #             if self.right is None:
    #                 self.right = TreeNode(val)
    #             else:
    #                 self.right.insert(val)

def inOrder(root, list):
    if root is None:
        return
    inOrder(root.left, list)
    list.append(root.val)
    inOrder(root.right, list)

def inorderTraversal(root):
    list = []
    inOrder(root, list)
    return list

# root = [1,null,2,3]
# Output: [1,3,2]

# node3 = TreeNode(3)
# node2 = TreeNode(2, node3, None)
root = TreeNode(1)

# print(node3.val)
# print(f'{node2.val}, left: {node2.left.val}')
# print(f'{root.val}, right: {root.right.val}')

print(inorderTraversal(root))

# problem
"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""