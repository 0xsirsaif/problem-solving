class Empty(Exception):
    pass


class Stack:
    def __init__(self):
        self._data = []

    def is_empty(self):
        return len(self._data) == 0

    def push(self, element):
        self._data.append(element)

    def pop(self):
        if self.is_empty():
            raise Empty("Empty Stack")
        return self._data.pop()

    def top(self):
        if self.is_empty():
            raise Empty("Empty Stack")
        return self._data[-1]


def transfer(s, t):
    while not s.is_empty():
        t.push(s.pop())


s = Stack()
t = Stack()

transfer(s, t)
