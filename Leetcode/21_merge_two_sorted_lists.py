# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = curr = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next




n6 = ListNode(5)
n5 = ListNode(5, n6)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(3, n3)
n1 = ListNode(1, n2)

n12 = ListNode(2)
n11 = ListNode(2, n12)
n10 = ListNode(2, n11)
n9 = ListNode(2, n10)
n8 = ListNode(2, n9)
n7 = ListNode(2, n8)

obj = Solution()
print(obj.mergeTwoLists(n1, n7))