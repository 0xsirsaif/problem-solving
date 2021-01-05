# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        dummy = curr = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        # connect the rest if the non-empty list to the tail of the new list
        curr.next = l1 or l2
        return dummy.next


# Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create & Handle List operations
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to display the list
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    # Method to add element to list
    def addToList(self, newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = newNode

    # Function to merge the lists


def mergeLists(headA, headB):
    dummyNode = Node(0)

    # Tail stores the last node
    tail = dummyNode
    while True:
        print(">>>", tail.data)
        print(">>>", dummyNode.data)
        print("=========")
        # If any of the list gets completely empty
        # directly join all the elements of the other list
        if headA is None:
            tail.next = headB
            break
        if headB is None:
            tail.next = headA
            break

        # Compare the data of the lists and whichever is smaller is
        # appended to the last of the merged list and the head is changed
        if headA.data <= headB.data:
            tail.next = headA
            headA = headA.next
        else:
            tail.next = headB
            headB = headB.next

        # Advance the tail
        tail = tail.next

    return dummyNode.next


listA = LinkedList()
listB = LinkedList()

listA.addToList(5)
listA.addToList(10)
listA.addToList(15)

listB.addToList(2)
listB.addToList(3)
listB.addToList(20)

listA.head = mergeLists(listA.head, listB.head)
listA.printList()

# n6 = ListNode(5)
# n5 = ListNode(5, n6)
# n4 = ListNode(4, n5)
# n3 = ListNode(3, n4)
# n2 = ListNode(3, n3)
# n1 = ListNode(1, n2)
#
# n12 = ListNode(2)
# n11 = ListNode(2, n12)
# n10 = ListNode(2, n11)
# n9 = ListNode(2, n10)
# n8 = ListNode(2, n9)
# n7 = ListNode(2, n8)
#
# obj = Solution()
# print(obj.mergeTwoLists(n1, n7))
#