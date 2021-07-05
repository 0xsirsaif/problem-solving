"""
Describe a good algorithm for concatenating two singly linked lists L and
M, given only references to the first node of each list, into a single list L'
that contains all the nodes of L followed by all the nodes of M.
"""
# TODO:
#   1. test the algorithm(implement the class)


class SinglyLinkedList:
    pass


def concatenate_two_linked_lists(l_head, m_head):
    n_head = SinglyLinkedList().head

    while l_head or m_head:
        if l_head:
            n_head.next = l_head
            l_head = l_head.next
        elif m_head:
            n_head.next = m_head
            m_head = m_head.next
        else:
            break