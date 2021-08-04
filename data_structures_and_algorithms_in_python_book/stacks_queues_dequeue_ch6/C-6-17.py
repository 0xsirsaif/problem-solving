class AllReserved(Exception):
    pass


class Empty(Exception):
    pass


class LimitedStack:
    def __init__(self, maxlen=None):
        self._data = [None for _ in range(maxlen)]
        self._element_num = 0
        self._max_len = maxlen

    def is_empty(self):
        return self._element_num == 0

    def push(self, element):
        if self._element_num == self._max_len:
            raise AllReserved("Limited Stack, All cells are reserved")
        self._data[self._element_num] = element
        self._element_num += 1

    def pop(self):
        if self.is_empty():
            raise Empty("Empty Stack")
        self._element_num -= 1
        poped_num = self._data[self._element_num]
        self._data[self._element_num] = None
        return poped_num

