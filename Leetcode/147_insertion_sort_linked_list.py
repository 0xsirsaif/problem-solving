# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        curr = head
        while curr and curr.next:
            print("CC", curr.val)
            hand = curr
            prev, ptr = curr, curr.next
            while ptr and ptr.next:
                print(curr.next.val, curr.next.next.val)
                if ptr.val < hand.val:
                    ptr = ptr.next
                    prev = ptr
                else:
                    print("::::")
                    ptr = ptr.next
            else:
                # arrive to the last node
                # hand > ptr2 or hand < ptr2
                print(hand.val,"DD")
                hold = hand.next
                if ptr.val < hand.val:
                    print("FFF")
                    next_hand = ptr.next
                    ptr.next = hand
                    hand.next = next_hand
                else:
                    prev.next = hand
                    hand.next = ptr

                curr = hold



        # c = curr
        # while c:
        #     print(c.val)
        #     c = c.next

class Solution2:
    def insertionSortList(self, head):
        dummyHead = ListNode(0)
        dummyHead.next = nodeToInsert = head

        while head and head.next:
            if head.val > head.next.val:
                # Locate nodeToInsert.
                nodeToInsert = head.next
                # Locate nodeToInsertPre.
                nodeToInsertPre = dummyHead
                while nodeToInsertPre.next.val < nodeToInsert.val:
                    nodeToInsertPre = nodeToInsertPre.next

                head.next = nodeToInsert.next
                # Insert nodeToInsert between nodeToInsertPre and nodeToInsertPre.next.
                nodeToInsert.next = nodeToInsertPre.next
                nodeToInsertPre.next = nodeToInsert
            else:
                head = head.next

        # c = dummyHead.next
        # while c:
        #     print(c.val)
        #     c = c.next

        return dummyHead.next





n10 = ListNode(100)
n9 = ListNode(90, n10)
n8 = ListNode(80, n9)
n7 = ListNode(70, n8)
n6 = ListNode(60, n7)
n5 = ListNode(50, n6)
n4 = ListNode(40, n5)
n3 = ListNode(1)
n2 = ListNode(2, n3)
n1 = ListNode(3, n2)


s = Solution()
print(s.insertionSortList(n1))