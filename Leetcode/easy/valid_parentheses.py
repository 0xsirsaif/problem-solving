from collections import deque


class Solution:
    def isValid(self, s):
        if len(s) % 2 != 0:  # it's not a valid if the string len is odd
            return False
        opened_parentheses = "([{"
        opened_parentheses_stack = deque()
        parentheses_pairs = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for element in s:
            if element in opened_parentheses:
                opened_parentheses_stack.append(element)
            else:
                try:
                    # parentheses are disproportionate
                    if parentheses_pairs[opened_parentheses_stack.pop()] != element:
                        return False
                except IndexError: # the stack is empty
                    return False
        if len(opened_parentheses_stack): # stack must be empty because all pairs are matched
            return False
        return True


obj = Solution()
print(obj.isValid("(){[][[][][][][]{{{{{]}}}}}]}"))

