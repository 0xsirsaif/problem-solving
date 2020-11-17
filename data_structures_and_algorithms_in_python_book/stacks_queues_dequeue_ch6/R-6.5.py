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


def reverse(array):
    stack = Stack()
    for i in array:
        stack.push(i)
    A = []
    while not stack.is_empty():
        A.append(stack.pop())
    return A

print(reverse([1,2,34,5,67,8,9]))