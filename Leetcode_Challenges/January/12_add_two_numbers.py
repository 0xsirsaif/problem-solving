class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = curr = ListNode(-1)
        carry = 0
        while l1 or l2:
            if not l2:
                num = l1.val
                l1 = l1.next
            elif not l1:
                num = l2.val
                l2 = l2.next
            else:
                num = (l1.val + l2.val)
                l1 = l1.next
                l2 = l2.next

            carry = num // 10
            curr.next = ListNode((num + carry) % 10)
            curr = curr.next

        if carry == 1:
            curr.next = ListNode(1)
        return dummy.next
