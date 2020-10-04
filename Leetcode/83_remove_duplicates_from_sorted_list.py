class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        while curr and curr.next:
            if curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


n9 = ListNode(10)
n8 = ListNode(60, n9)
n7 = ListNode(50, n8)
n6 = ListNode(40, n7)
n5 = ListNode(30, n6)
n4 = ListNode(20, n5)
n3 = ListNode(20, n4)
n2 = ListNode(10, n3)
n1 = ListNode(10, n2)

s = Solution()
print(s.deleteDuplicates(n1))
