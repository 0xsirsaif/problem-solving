class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head
        slow = fast = head
        if n == 1:
            fast = head

        steps = n
        while fast and steps:
            fast = fast.next
            steps -= 1

        while fast:
            if not fast.next:
                node = slow.next.next
                slow.next = node
                return head
            else:
                fast = fast.next
                slow = slow.next

        return head.next

n6 = ListNode(2)
n5 = ListNode(5)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2)
n1 = ListNode(1, n2)

S = Solution()
print(S.removeNthFromEnd(n1, 2))
# print(slow.val)
#         print(fast.val)
#         print(">>>")
#         s = head
#         while s:
#             print("==", s.val)
#             s = s.next