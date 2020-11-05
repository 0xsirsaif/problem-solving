class AllReserved(Exception):
    pass


class Empty(Exception):
    pass


class LimitedStack:
    def __init__(self, maxlen=None):
        self._data = []
        self._element_num = 0
        self._max_len = maxlen

    def is_empty(self):
        return self._element_num == 0

    def push(self, element):
        if self._element_num == self._max_len:
            raise AllReserved("Limited Stack, All cells are reserved")
        self._data.append(element)
        self._element_num += 1

    def pop(self):
        if self.is_empty():
            raise Empty("Empty Stack")
        self._element_num -= 1
        return self._data.pop()


def empty_stack(stack):
    if stack.is_empty():
        return
    stack.pop()
    return empty_stack(stack)

stack_instance = LimitedStack()
stack_instance.push(10)
stack_instance.push(10)
stack_instance.push(10)
stack_instance.push(10)
stack_instance.push(10)
stack_instance.push(10)
stack_instance.push(10)
stack_instance.push(10)
stack_instance.push(10)
stack_instance.push(10)
empty_stack(stack_instance)