# 83. Remove Duplicates from Sorted List

class listNode:
    def __init__(self, value = 0, next = None):
        self.value = value
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
        print(node.value)
        node = node.next
def deleteDuplicates(head):
    res_list = head
    node = head
    while node:
        nodenext = node.next
        if nodenext:
            if node.value == nodenext.value:
                node.next = nodenext.next
            else:
                node = node.next
        else:
            node.next = None
            node = node.next
    return res_list

LL = createLL([1,1,2])
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