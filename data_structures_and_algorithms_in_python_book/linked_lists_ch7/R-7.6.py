"""
Suppose that x and y are references to nodes of circularly linked lists,
although not necessarily the same list. Describe a fast algorithm for telling
if x and y belong to the same list.
"""


# Solution:
# 1. Suppose that X is the tail of the list
# 2. Traversing the array to find Y
# 3. If exists -> X,Y in the same list
# 4. else -> X,Y in different lists

# TODO
#   what is the code model?
#       IF x is y: True
#       ELIF x: THEN search for y
#       ELIF Y: THEN search for x
#       ELSE: False
def is_the_same_list(x, y) -> bool:
    def _search(tail, target):
        ptr = tail.next
        while ptr and ptr is not tail and target:
            if ptr is target:
                return True
            ptr = ptr.next
        return False
    if x is y:
        return True
    elif x:
        return _search(x, y)
    elif y:
        return _search(y, x)
    return False
