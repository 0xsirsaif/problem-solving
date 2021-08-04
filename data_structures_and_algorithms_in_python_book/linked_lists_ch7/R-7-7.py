"""
Our CircularQueue class of Section 7.2.2 provides a rotate( ) method that
has semantics equivalent to Q.enqueue(Q.dequeue( )), for a nonempty queue.
Implement such a method for the LinkedQueue class of Section 7.1.2 without the creation of any new nodes.
"""


class Empty(Exception):
    pass


class CircularQueue:
    class _Node:
        __slots__ = 'element', 'next'

        def __init__(self, element, next):
            self.element = element
            self.next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def first(self):
        if self.is_empty():
            Empty("Empty Queue")
        head = self._tail.next
        return head.element

    def dequeue(self):
        if self.is_empty():
            Empty("Empty Queue")
        old_head = self._tail.next
        if self._size == 1:
            self._tail = None
        else:
            self._tail.next = old_head.next
        self._size -= 1
        return old_head.element

    def enqueue(self, e):
        new_node = self._Node(e, None)
        if self.is_empty():
            new_node.next = new_node
        else:
            new_node.next = self._tail.next
            self._tail.next = new_node
        self._tail = new_node
        self._size += 1

    def rotate(self):
        if not self.is_empty():
            self._tail = self._tail.next


class LinkedQueue:
    class _Node:
        __slots__ = 'element', 'next'

        def __init__(self, element, next):
            self.element = element
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.head.element

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self.head
        self.head = self.head.next
        self._size -= 1
        if self.is_empty():
            self.tail = None
        return answer.element

    def enqueue(self, e):
        new_node = self._Node(e, None)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self._size += 1

    def rotate(self):
        """
        1. A -> B -> C -> D
        2. rotate()
        3. B -> C -> D -> A
        """
        if not self.is_empty():
            self.tail.next = self.head
            new_head = self.head.next
            self.head.next = None
            self.head = new_head

