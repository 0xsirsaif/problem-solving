"""
Describe a nonrecursive method for finding, by link hopping, the middle
node of a doubly linked list with header and trailer sentinels. In the case
of an even number of nodes, report the node slightly left of center as the
“middle.” (Note: This method must only use link hopping; it cannot use a counter.)
What is the running time of this method?
"""


# TODO
# 1. What is the advantage of being a doubly linked list in this problem?

# o(n) + o(n//2 + 1) = o(n)
def find_the_middle(L):
    head = L.head
    count = 0
    while head:
        count += 1
        head = head.next
    count -= 1  # neglect the trailer node
    ptr = L.header.head
    while count:
        count -= 1
        ptr = ptr.next
    return ptr
