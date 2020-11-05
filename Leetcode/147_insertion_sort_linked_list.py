# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        pass





n10 = ListNode(-1)
n9 = ListNode(0, n10)
n8 = ListNode(1, n9)
n7 = ListNode(2, n8)
n6 = ListNode(3, n7)
n5 = ListNode(4, n6)
n4 = ListNode(5, n5)
n3 = ListNode(6, n4)
n2 = ListNode(7, n3)
n1 = ListNode(8, n2)


s = Solution()
print(s.insertionSortList(n1))