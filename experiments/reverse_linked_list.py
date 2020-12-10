class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head):
    dummy = None
    curr = head
    while curr:
        next_ = curr.next
        curr.next = dummy
        dummy = curr
        curr = next_
    return dummy


n12 = ListNode(12)
n11 = ListNode(11, n12)
n10 = ListNode(10, n11)
n9 = ListNode(9, n10)
n8 = ListNode(8, n9)
n7 = ListNode(7, n8)
n6 = ListNode(6, n7)
n5 = ListNode(5, n6)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

print(reverse_linked_list(n1))