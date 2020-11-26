class FullQueue(Exception):
    pass


class EmptyQueue(Exception):
    pass


class Queue:
    def __init__(self, max_len: int):
        self._front = 0
        self._size = 0
        self._capacity = max_len
        self._data = [None] * self._capacity

    def enqueue(self, value: int) -> bool:
        if self.is_full():
            raise FullQueue("Full Queue, no more cells")

        next_insert = (self._front + self._size) % len(self._data)
        self._data[next_insert] = value
        self._size += 1
        return True

    def dequeue(self) -> bool:
        if self.is_empty():
            raise EmptyQueue("Empty Queue")
        self._data[self._front] = None
        self._front = (1 + self._front) % len(self._data)
        self._size -= 1
        return True

    def front(self) -> int:
        if self.is_empty():
            raise EmptyQueue("Empty Queue")
        return self._data[self._front]

    def rear(self) -> int:
        if self.is_empty():
            raise EmptyQueue("Empty Queue")
        end = (self._front + self._size - 1) % len(self._data)
        return self._data[end]

    def is_empty(self) -> bool:
        return self._size == 0

    def is_full(self) -> bool:
        return self._size == self._capacity
