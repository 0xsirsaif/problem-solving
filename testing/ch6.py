class EmptyStackException(Exception):
    """Empty Stack"""
    pass

class ArrayStack:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def push(self, element):
        self._data.append(element)

    def is_empty(self):
        return len(self._data) == 0

    def top(self):
        if self.is_empty():
            raise EmptyStackException("Stack is Empty")
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise EmptyStackException("Stack is Empty")
        return self._data.pop()

    def all_items(self):
        return self._data

stack = ArrayStack()
for i in range(100):
    stack.push(i)
print(stack.all_items())