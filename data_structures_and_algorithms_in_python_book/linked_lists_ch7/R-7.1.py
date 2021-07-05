"""
Give an algorithm for finding the second-to-last node in a singly linked
list in which the last node is indicated by a next reference of None.
"""
# TODO:
#   1. test the algorithm(implement the class)


def find_the_second_to_last_node(singly_linked_list):
    head = singly_linked_list.head
    while head:
        if not head.next:
            return head
        head = head.next






