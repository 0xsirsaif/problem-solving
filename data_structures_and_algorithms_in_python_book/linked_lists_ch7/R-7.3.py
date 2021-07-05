"""
Describe a recursive algorithm that counts the number of nodes in a singly
linked list.
"""
# TODO:
#   1. test the algorithm(implement the class)


def count_nodes_recursively(head, count):
    if not head:
        return count
    count_nodes_recursively(head.next, count+1)