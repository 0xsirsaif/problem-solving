class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        curr = head
        _binary_nums = []
        while curr:
            _binary_nums.append(str(curr.val))
            curr = curr.next

        print(''.join(_binary_nums))
        return int(''.join(_binary_nums), 2)

n15 = ListNode(0)
n14 = ListNode(0, n15)
n13 = ListNode(0, n14)
n12 = ListNode(0, n13)
n11 = ListNode(0, n12)
n10 = ListNode(0, n11)
n9 = ListNode(1, n10)
n8 = ListNode(1, n9)
n7 = ListNode(1, n8)
n6 = ListNode(0, n7)
n5 = ListNode(0, n6)
n4 = ListNode(1, n5)
n3 = ListNode(0, n4)
n2 = ListNode(0, n3)
n1 = ListNode(1, n2)

s = Solution()
print(s.getDecimalValue(n1))