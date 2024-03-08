# 83. Remove Duplicates from Sorted List

class listNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
def createLL(list):
    listLL = listNode()
    head = listLL
    node = listLL
    for num in list:
        node.next = listNode(num)
        node = node.next
    return head.next
def printLL(node):
    while node:
        print(node.val)
        node = node.next
def deleteDuplicates(head):
    res_list = head
    node = head
    if head:
        while node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
    return res_list

LL = createLL([1,1,2,3,3])
# printLL(LL)
printLL(deleteDuplicates(LL))
"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]

Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""