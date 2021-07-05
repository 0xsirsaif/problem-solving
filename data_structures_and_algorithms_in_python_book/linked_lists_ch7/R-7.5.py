"""
Implement a function that counts the number of nodes in a circularly
linked list.
"""


def count_circularly_nodes(tail):
    if not tail:
        return 0
    head = tail.next
    count = 1
    while head and head != tail:
        count += 1
        head = head.next
    return count