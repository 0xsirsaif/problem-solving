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

    def print_stack(self):
        print(">>", self._data)


def transfer(s, t):
    while not s.is_empty():
        t.push(s.pop())
    return t


def reverse_stack(S, A, B):
    transfer(transfer(transfer(S, A), B), S)

S = Stack()
tem_A = Stack()
temp_B = Stack()

S.push(1)
S.push(2)
S.push(3)
S.push(4)
S.push(5)

S.print_stack()
reverse_stack(S, tem_A, temp_B)
S.print_stack()
