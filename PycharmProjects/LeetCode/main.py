class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# create linked list from 1 to n and return first element
def ListToN(n):
    head = ListNode()
    node = head
    for i in range(n):
        node.next = ListNode(i)
        node = node.next
    return head.next

# print linked list
def print_LL(node):
    while node: #while node != None
        print(node.val)
        node = node.next

print_LL(ListToN(10))