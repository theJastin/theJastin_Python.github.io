# 876. Middle of the Linked List
class listNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

def middleNode(head):
    node = head
    count = 0
    while node:
        count +=1
        node = node.next
    mid = (count+2)// 2
    node = head
    for i in range(1, mid):
        node = node.next
    return node

def createLL(list):
    listLL = listNode()
    head = listLL
    node = head
    for num in list:
       node.next = listNode(num)
       node = node.next
    return head.next

def printLL(node):
    while node:
        print(node.val)
        node = node.next

LL = createLL([1,2,3,4,5])
# printLL(LL)
printLL(middleNode(LL))

"""
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Constraints:
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""