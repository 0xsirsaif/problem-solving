class EmptyQueue(Exception):
    pass


class Queue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * Queue.DEFAULT_CAPACITY
        self._size = 0  # number of current elements
        self._front = 0  # the latest element

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise EmptyQueue("Empty Queue ")
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueue("Empty Queue")

        dequeued_element = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return dequeued_element

    def enqueue(self, element):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        end = (self._front + self._size) % len(self._data)
        self._data[end] = element
        self._size += 1

    def _resize(self, capacity):
        old_data = self._data
        self._data = [None] * capacity
        pointer = self._front
        for i in range(self._size):
            self._data[i] = old_data[pointer]
            pointer = (pointer + 1) % len(old_data)

        self._front = 0

    def print_queue(self):
        print(">>", self._data)

Q = Queue()
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(4)
Q.enqueue(5)
Q.enqueue(6)
Q.enqueue(7)
Q.enqueue(8)
Q.enqueue(9)
Q.enqueue(10)
Q.print_queue()
Q.dequeue()
# Q.dequeue()
# Q.dequeue()
# Q.dequeue()
# Q.dequeue()
# Q.dequeue()
# Q.dequeue()
# Q.dequeue()
# Q.dequeue()
# Q.dequeue()
Q.print_queue()
