class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy = None
        curr = head
        while curr:
            next_ = curr.next
            curr.next = dummy
            dummy = curr
            curr = next_

        return dummy
