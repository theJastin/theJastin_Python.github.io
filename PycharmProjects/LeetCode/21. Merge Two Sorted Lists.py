# 21. Merge Two Sorted Lists solution
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# return which node to use

def mergeTwoLists(list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        node = ListNode()
        head = node
        while list1 and list2:
            node.next = ListNode()
            node = node.next
            if list1.val < list2.val:
                node.val = list1.val
                list1 = list1.next
            else:
                node.val = list2.val
                list2 = list2.next
        node.next = list1 or list2
        return head.next

def createLL(list):
    listLL = ListNode()
    head = listLL
    node = head
    for num in list:
        node.next = ListNode(num)
        node = node.next
    return head.next

def print_LL(node):
    while node: #while node != None
        print(node.val)
        node = node.next

# list1 = [1,2,4], list2 = [1,3,4]

list1LL = createLL([1,2,4])
list2LL = createLL([1,3,4])
# print_LL(list1LL)
# print_LL(list2LL)
print_LL(mergeTwoLists(list1LL, list2LL))

# problem
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
 
Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
