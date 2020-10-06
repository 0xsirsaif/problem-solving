class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # reassign head node to the first distinct node
        curr, count = head, 0
        while curr and curr.next:
            if curr.val != curr.next.val:
                if count == 0:
                    head = curr
                else:
                    head = curr.next
                break
            else:
                count += 1
                curr = curr.next
                if not curr.next:
                    head.next = None

        curr, ptr = head, head.next
        while ptr and ptr.next:
            if ptr.val != ptr.next.val:
                curr.next = ptr
                curr = ptr
                ptr = ptr.next
            else:
                ptr = ptr.next.next
                curr.next = ptr

        curr = head
        while curr:
            print(curr.val)
            curr = curr.next

        return head

class ListNodeB:
    def __init__(self, val=0, next=None, duplicate=True):
        self.val = val
        self.next = next
        self.duplicate = duplicate


# solution using new flag in ListNode class
class SolutionB:
    def deleteDuplicates(self, head: ListNodeB) -> ListNodeB:
        # remove duplicates without removing the duplicated item itself
        curr = head
        while curr and curr.next:
            if curr.next.val == curr.val:
                curr.next = curr.next.next
                curr.duplicate = False
            else:
                curr = curr.next

        # find the first non-duplicated node
        first_distinct, curr = None, head
        while curr:
            if curr.duplicate:
                first_distinct = curr
                break
            curr = curr.next

        # remove the duplicated item itself
        curr, ptr = first_distinct, first_distinct.next
        while ptr:
            if ptr.duplicate:
                curr.next = ptr
                curr, ptr = ptr, ptr.next
            else:
                ptr = ptr.next

        # unchain the last non-distincit items
        curr = first_distinct
        while curr and curr.next:
            if not curr.next.duplicate:
                curr.next = None
            curr = curr.next

        return first_distinct

# n10 = ListNodeB(10)
# n9 = ListNodeB(10, n10)
# n8 = ListNodeB(10, n9)
# n7 = ListNodeB(10, n8)
# n6 = ListNodeB(10, n7)
n5 = ListNodeB(30)
n4 = ListNodeB(20, n5)
n3 = ListNodeB(10, n4)
n2 = ListNodeB(10, n3)
n1 = ListNodeB(10, n2)

s = Solution()
print(s.deleteDuplicates(n1))

# if curr.val == ptr.val:
#     ptr = ptr.next
#     count += 1
#     if not ptr.next:
#         head.next = None
# else:
#     if count > 0:
#         head = ptr
#     else:
#         head = curr
#     break