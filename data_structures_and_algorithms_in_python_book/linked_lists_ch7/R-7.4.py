"""
Describe in detail how to swap two nodes x and y (and not just their con-
tents) in a singly linked list L given references only to x and y. Repeat
this exercise for the case when L is a doubly linked list. Which algorithm
takes more time?
"""


class SinglyLinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


L = SinglyLinkedList()


def swap_singly(x, y):
    head = ptr_1 = ptr_2 = L.head
    while ptr_1:
        if ptr_1.next == x:
            while ptr_2:
                if ptr_2.next == y:
                    # swap logic
                    ptr_1.next = ptr_2.next
                    ptr_2 = ptr_1
                ptr_2 = ptr_2.next
        ptr_1 = ptr_1.next
    return L

def swap_doubly():
    pass