"""
Give a fast algorithm for concatenating two doubly linked lists L and M,
with header and trailer sentinel nodes, into a single list N.
"""


class DoublyLinkedList:
    pass


def concatenate_two_doubly_lists(L, M):
    N = DoublyLinkedList()
    ptr_1 = L.head
    ptr_2 = M.head
    ptr = N.header
    while ptr_1 and ptr_2:
        old_ptr_1 = ptr_1
        old_ptr_2 = ptr_2

        ptr.next = ptr_1
        ptr_1.prev = ptr
        ptr_1.next = ptr_2
        ptr_2.prev = ptr_1
        ptr = ptr_2

        ptr_1 = old_ptr_1.next
        ptr_2 = old_ptr_2.next
    if ptr_1:
        ptr.next = ptr_1
        ptr_1.prev = ptr
    elif ptr_2:
        ptr.next = ptr_2
        ptr_2.prev = ptr
    return ptr