class MyCircularQueue:

    def __init__(self, k: int):
        self._front = 0
        self._size = 0
        self._capacity = k
        self._data = [None] * self._capacity

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        next_insert = (self._front + self._size) % len(self._data)
        self._data[next_insert] = value
        self._size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self._data[self._front] = None
        self._front = (1 + self._front) % len(self._data)
        self._size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self._data[self._front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        end = (self._front + self._size - 1) % len(self._data)
        return self._data[end]

    def isEmpty(self) -> bool:
        return self._size == 0

    def isFull(self) -> bool:
        return self._size == self._capacity

    def print_queue(self):
        print(">>", self._data)


Q = MyCircularQueue(10)
Q.isFull()
Q.enQueue(1)
Q.enQueue(2)
Q.enQueue(3)
Q.enQueue(4)
Q.enQueue(5)
Q.enQueue(6)
Q.enQueue(7)
Q.enQueue(8)
Q.enQueue(9)
Q.enQueue(10)
Q.print_queue()
Q.deQueue()
Q.deQueue()
Q.deQueue()
Q.deQueue()
Q.deQueue()
Q.deQueue()
Q.enQueue(100)
Q.enQueue(101)
Q.enQueue(102)
Q.enQueue(103)
Q.enQueue(104)
Q.enQueue(105)
Q.deQueue()
Q.enQueue(106)
Q.deQueue()
# Q.deQueue()
# Q.deQueue()
# Q.deQueue()
Q.print_queue()

