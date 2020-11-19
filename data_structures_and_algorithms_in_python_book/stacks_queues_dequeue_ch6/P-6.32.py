class EmptyQueue(Exception):
    pass


class DeQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * DeQueue.DEFAULT_CAPACITY
        self._capacity = DeQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        self._back = 0

    def add_last(self, element):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        end = (self._front + self._size) % len(self._data)
        self._data[end] = element
        self._size += 1
        self._back = (self._front + self._size -1) % len(self._data)

    def delete_first(self):
        if self.is_empty():
            raise EmptyQueue("Empty Queue")

        self._data[self._front] = None
        self._size -= 1
        self._front = (self._front + 1) % len(self._data)

    def add_first(self, element):
        if self.is_full():
            self._resize(2 * len(self._data))

        # implement Right Shift
        self.rotate(1)
        self._data[self._front] = element
        self._size += 1
        self._back = (self._front + self._size - 1) % len(self._data)

    def delete_last(self):
        if self.is_empty():
            raise EmptyQueue("Empty Queue")

        self._data[self._back] = None
        self._size -= 1
        self._back = (self._front + self._size - 1) % len(self._data)

    def first(self):
        if self.is_empty():
            raise EmptyQueue("Empty Queue !")
        return self._data[self._front]

    def last(self):
        if self.is_empty():
            raise EmptyQueue("Empty Queue !")
        return self._data[self._back]

    def _resize(self, capacity):
        old_data = self._data
        self._data = [None] * capacity
        pointer = self._front
        for i in range(self._size):
            self._data[i] = old_data[pointer]
            pointer = (pointer + 1) % len(old_data)

        self._front = 0
        self._back = self._size
        self._capacity = capacity

    def rotate(self, k):
        new_data = [None] * self._capacity
        for i in range(self._size):
            new_data[i+k] = self._data[i]
        self._data = new_data

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self._capacity

    def print_queue(self):
        print(">>", self._data)

