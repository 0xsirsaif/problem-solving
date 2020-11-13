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
        return self._data


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = Stack()

        for i in range(len(path)):
            # all dots apply here, please!
            if path[i] == ".":
                # nothing to remove if the stack is empty, just skip
                if not stack.is_empty() and i > 0:
                    if stack.top() == "/":
                        stack.pop()
                    else:
                        while not stack.is_empty() and stack.top() != "/":
                            stack.pop()
                        stack.pop()
            elif (path[i] != "/") or (i == 0) or (path[i-1] != "/"):
                stack.push(path[i])

        p = []
        while not stack.is_empty():
            p.append(stack.pop())




s = Solution()
A = "/home/"
print(s.simplifyPath(A))

# p = []
# while not stack.is_empty():
#     p.append(stack.pop())
#
# p = p[::-1]
# if not p:
#     return "/"
# return "".join(i for i in p)
