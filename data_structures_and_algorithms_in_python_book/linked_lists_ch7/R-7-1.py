from DataStructures.LinkedLists import SinglyLinkedList, DummyNode
import unittest

"""
Give an algorithm for finding the second-to-last node in a singly linked
list in which the last node is indicated by a next reference of None.
"""


# TODO:
#   1. test the algorithm(implement the class)


def find_the_second_to_last_node(head):
    ptr = head
    prev = DummyNode(head)
    while ptr:
        ptr = ptr.next
        prev = prev.next
    return prev.element


if __name__ == "__main__":
    class TestFindTheSecondToLastNode(unittest.TestCase):
        def test_find_the_second_to_last_node(self):
            singly_linked_list = SinglyLinkedList()
            # add some nodes
            for i in range(10):
                singly_linked_list.add_first(i)
            head = singly_linked_list.head
            actual = find_the_second_to_last_node(head)
            expected = 8
            self.assertEqual(actual, expected)





