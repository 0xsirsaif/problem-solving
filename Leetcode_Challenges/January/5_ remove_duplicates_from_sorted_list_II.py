class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None

        dummy = curr = ListNode(0)
        while head:
            if head.next and head.val == head.next.val:
                # reach the last node
                # reach the last in duplicated nodes
                while head.next and head.val == head.next.val:
                    head = head.next
            else:
                curr.next = head
                curr = curr.next

            head = head.next

        s = dummy.next
        while s:
            print(">>", s.val)
            s = s.next

        return dummy.next


n7 = ListNode(5)
n6 = ListNode(4, n7)
n5 = ListNode(4, n6)
n4 = ListNode(3, n5)
n3 = ListNode(2)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

obj = Solution()
print(obj.deleteDuplicates(n1))
