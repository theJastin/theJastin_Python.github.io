class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# return which node to use
def ChooseNode(node1, node2):
    if not node1:
        return 2
    if not node2:
        return 1
    if node1.val > node2.val:
        return 2
    return 1

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