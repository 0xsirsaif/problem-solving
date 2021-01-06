class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head and not head.next:
            return head

        dummy = curr = ListNode(-1, head)
        while head:
            if head.next and head.val == head.next.val:
                # loop till the last duplicated node
                while head.next and head.val == head.next.val:
                    head = head.next
                curr.next = head.next
            else:
                # confirmed to be distinct
                curr = curr.next
            head = head.next

        return dummy.next


def skip_duplicates(head: ListNode):
    if not head or not head.next:
        # List only has a single elemnet
        return head

    if head.val == head.next.val:
        # Remove the duplicated element
        r = skip_duplicates(head.next)
        return r.next if r == head.next else r

    head.next = skip_duplicates(head.next)

    return head


class Solution1:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        return skip_duplicates(head)

n7 = ListNode(5)
n6 = ListNode(4)
n5 = ListNode(4, n6)
n4 = ListNode(2, n5)
n3 = ListNode(2, n4)
n2 = ListNode(1, n3)
n1 = ListNode(1, n2)

obj = Solution()
print(obj.deleteDuplicates(n1))