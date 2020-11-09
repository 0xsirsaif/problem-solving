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
    def removeDuplicates(self, s: str, k: int) -> str:
        value = None
        count = 0
        hummer = 0
        stack = Stack()

        # remove k elements
        for i in s:
            if value == i:
                count += 1
            else:
                value = i
                count = 1

            # remove last k-1 similar elements, and ignore the Kth one
            if count == k:
                hummer += 1
                for x in range(k-1):
                    stack.pop()

            else:
                stack.push(i)

        p = []
        while not stack.is_empty():
            p.append(stack.pop())

        p = p[::-1]
        if p:
            if hummer:
                return self.removeDuplicates("".join(p), k)
            else:
                return "".join(p)

s = Solution()
print(s.removeDuplicates("pbbcggttciiippooaais", 2))
