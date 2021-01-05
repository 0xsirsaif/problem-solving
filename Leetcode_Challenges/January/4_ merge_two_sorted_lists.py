class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
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


class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        # Catch cases where one list is None
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        # Save the head node to return
        head = l2 if l2.val <= l1.val else l1

        while l1 and l2:

            # Compare l1 and l2
            bigger = l1 if l1.val >= l2.val else l2
            smaller = l1 if bigger is l2 else l2

            # Find the right spot for the bigger node in the smaller list
            while smaller.next and smaller.next.val <= bigger.val:
                smaller = smaller.next

            # Save the rest of the smaller list
            l1 = smaller.next

            # Splice in the bigger node here
            smaller.next = bigger
            l2 = smaller.next

        return head


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

obj = Solution1()
print(obj.mergeTwoLists(None, n7))