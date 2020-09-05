# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        sorted_list = sorted(self._convert_to_list(l1) + self._convert_to_list(l2))
        sorted_linked_list = []
        for i in sorted_list:
            next_node = ListNode(i+1) if (i < len(sorted_list)) else None
            node = ListNode(i, next_node)
            sorted_linked_list.append(node)
        return sorted_linked_list[0].next

    def _convert_to_list(self, start_node):
        array = [start_node.val]
        n = start_node.next
        while n:
            array.append(n.val)
            n = n.next
        return array


n6 = ListNode(6)
n5 = ListNode(2, n6)
n4 = ListNode(4, n5)
n3 = ListNode(6, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

n12 = ListNode(5)
n11 = ListNode(11, n12)
n10 = ListNode(4, n11)
n9 = ListNode(9, n10)
n8 = ListNode(0, n9)
n7 = ListNode(7, n8)

obj = Solution()
print(obj.mergeTwoLists(n1, n7))