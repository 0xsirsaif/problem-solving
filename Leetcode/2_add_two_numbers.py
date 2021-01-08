from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = 0
        dummy = curr = ListNode(-1)
        while l1 or l2:
            result = result // 10
            if not l2:
                result += l1.val
                l1 = l2.next
            elif not l1:
                result += l2.val
                l1 = l1.next
            else:
                result += (l1.val + l2.val)
                l1 = l1.next
                l2 = l2.next

            curr.next = ListNode(result % 10)
            curr = curr.next
        # if the last sum have a carried value, then we must consider it
        if result // 10 == 1:
            curr.next = ListNode(1, None)
        return dummy.next
