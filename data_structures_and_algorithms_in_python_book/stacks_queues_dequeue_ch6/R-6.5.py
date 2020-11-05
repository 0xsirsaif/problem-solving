class AllReserved(Exception):
    pass


class Empty(Exception):
    pass


class LimitedStack:
    def __init__(self, maxlen=None):
        self._data = [None for _ in range(maxlen)] if maxlen else []
        self._element_num = 0
        self._max_len = maxlen

    def is_empty(self):
        return self._element_num == 0

    def push(self, element):
        if self._element_num == self._max_len:
            raise AllReserved("Limited Stack, All cells are reserved")

        if self._max_len is not None:
            self._data[self._element_num] = element
        else:
            self._data.append(element)
        self._element_num += 1

    def pop(self):
        print(self._data)
        if self.is_empty():
            raise Empty("Empty Stack")
        self._element_num -= 1
        return self._data.pop()


def reverse(array):
    stack = LimitedStack()
    for i in array:
        stack.push(i)
    A = []
    for x in range(len(array)):
        A.append(stack.pop())
    return A