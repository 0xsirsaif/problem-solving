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

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = Stack()
        s_list = list(s)
        for i in range(len(s_list)):
            if s_list[i] == "(":
                stack.push(i)
            elif s_list[i] == ")":
                if stack.is_empty():
                    s_list[i] = None
                    continue
                stack.pop()

        while not stack.is_empty():
            idx = stack.pop()
            s_list[idx] = None

        return "".join(i for i in s_list if i is not None)

s = Solution()
print(s.minRemoveToMakeValid("(a(b(c)d)"))